rhs_zsu234_aa = {
    "editorPreview": "rhsafrf|addons|rhs_editorPreviews|data|rhs_zsu234_aa.paa",
    "author": "RHS",
    "scope": 2,
    "displayName": "ZSU-23-4V",
    "faction": "rhs_faction_vpvo",
    "vehicleClass": "rhs_vehclass_aa",
    "editorSubcategory": "rhs_EdSubcat_aa",
    "dlc": "RHS_AFRF",
    "rhs_decalParameters": ["['Number',cRHSZSUNumberPlaces,'Default']"],
    "category": "Armored",
    "driveOnComponent": ["Slide"],
    "simulation": "tankX",
    "maxFordingDepth": 0,
    "waterResistance": 0,
    "waterDamageEngine": 0.2,
    "waterLeakiness": 10,
    "enginePower": 209,
    "peakTorque": 1176,
    "minOmega": 61,
    "maxOmega": 209.44,
    "idleRpm": 600,
    "redRpm": 2000,
    "torqueCurve": [[0,0],[0.3,0.757238],[0.4,0.868597],[0.6,0.957684],[0.7,1],[0.8,0.746102],[1,0.534521],[1.5,0]],
    "thrustDelay": 0.6,
    "clutchStrength": 80,
    "fuelCapacity": 30,
    "RHS_fuelCapacity": 520,
    "brakeIdleSpeed": 1.78,
    "latency": 1.1,
    "tankTurnForce": 330000,
    "tankTurnForceAngMinSpd": 0.6,
    "tankTurnForceAngSpd": 0.91,
    "accelAidForceYOffset": -3.5,
    "accelAidForceCoef": 4,
    "accelAidForceSpd": 1.9,
    "engineLosses": 25,
    "transmissionLosses": 15,
    "normalSpeedForwardCoef": 0.7,
    "changeGearType": "rpmratio",
    "changeGearOmegaRatios": [1,0.7,0.75,0.55,0.65,0.5,0.75,0.7,0.75,0.7,0.75,0.55,1,0.5],
    # Class: CfgVehicles\rhs_zsutank_base\complexGearbox,
    "complexGearbox": {
        "GearboxRatios": ["R2",-7,"N",0,"D1",1.25,"D2",1.2,"D3",1.15,"D4",1.05,"D5",0.95],
        "TransmissionRatios": ["High",15.8],
        "gearBoxMode": "auto",
        "moveOffGear": 1,
        "driveString": "D",
        "neutralString": "N",
        "reverseString": "R",
        "transmissionDelay": 0.6
    },
    # Class: CfgVehicles\rhs_zsutank_base\Wheels,
    "Wheels": {
        # Class: CfgVehicles\rhs_zsutank_base\Wheels\L2
        "L2": {
            "suspTravelDirection": [-0.125,-1,0],
            "side": "left",
            "boneName": "wheel_podkoloL1",
            "center": "wheel_1_2_axis",
            "boundary": "wheel_1_2_bound",
            "steering": 0,
            "width": 0.33,
            "mass": 150,
            "MOI": 10,
            "maxBrakeTorque": 8000,
            "sprungMass": -1,
            "springStrength": 150000,
            "springDamperRate": 11000,
            "dampingRate": 2174,
            "dampingRateInAir": 2174,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "latStiffX": 3.5,
            "latStiffY": 35,
            "longitudinalStiffnessPerUnitGravity": 14000,
            "frictionVsSlipGraph": [[0,0.45],[0.18,1],[0.6,0.6]]
        },
        # Class: CfgVehicles\rhs_zsutank_base\Wheels\L3,
        "L3": {
            "boneName": "wheel_podkolol2",
            "center": "wheel_1_3_axis",
            "boundary": "wheel_1_3_bound",
            "suspTravelDirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.33,
            "mass": 150,
            "MOI": 10,
            "maxBrakeTorque": 8000,
            "sprungMass": -1,
            "springStrength": 150000,
            "springDamperRate": 11000,
            "dampingRate": 2174,
            "dampingRateInAir": 2174,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "latStiffX": 3.5,
            "latStiffY": 35,
            "longitudinalStiffnessPerUnitGravity": 14000,
            "frictionVsSlipGraph": [[0,0.45],[0.18,1],[0.6,0.6]]
        },
        # Class: CfgVehicles\rhs_zsutank_base\Wheels\L4,
        "L4": {
            "boneName": "wheel_podkolol3",
            "center": "wheel_1_4_axis",
            "boundary": "wheel_1_4_bound",
            "suspTravelDirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.33,
            "mass": 150,
            "MOI": 10,
            "maxBrakeTorque": 8000,
            "sprungMass": -1,
            "springStrength": 150000,
            "springDamperRate": 11000,
            "dampingRate": 2174,
            "dampingRateInAir": 2174,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "latStiffX": 3.5,
            "latStiffY": 35,
            "longitudinalStiffnessPerUnitGravity": 14000,
            "frictionVsSlipGraph": [[0,0.45],[0.18,1],[0.6,0.6]]
        },
        # Class: CfgVehicles\rhs_zsutank_base\Wheels\L5,
        "L5": {
            "boneName": "wheel_podkolol4",
            "center": "wheel_1_5_axis",
            "boundary": "wheel_1_5_bound",
            "suspTravelDirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.33,
            "mass": 150,
            "MOI": 10,
            "maxBrakeTorque": 8000,
            "sprungMass": -1,
            "springStrength": 150000,
            "springDamperRate": 11000,
            "dampingRate": 2174,
            "dampingRateInAir": 2174,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "latStiffX": 3.5,
            "latStiffY": 35,
            "longitudinalStiffnessPerUnitGravity": 14000,
            "frictionVsSlipGraph": [[0,0.45],[0.18,1],[0.6,0.6]]
        },
        # Class: CfgVehicles\rhs_zsutank_base\Wheels\L6,
        "L6": {
            "boneName": "wheel_podkolol5",
            "center": "wheel_1_6_axis",
            "boundary": "wheel_1_6_bound",
            "suspTravelDirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.33,
            "mass": 150,
            "MOI": 10,
            "maxBrakeTorque": 8000,
            "sprungMass": -1,
            "springStrength": 150000,
            "springDamperRate": 11000,
            "dampingRate": 2174,
            "dampingRateInAir": 2174,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "latStiffX": 3.5,
            "latStiffY": 35,
            "longitudinalStiffnessPerUnitGravity": 14000,
            "frictionVsSlipGraph": [[0,0.45],[0.18,1],[0.6,0.6]]
        },
        # Class: CfgVehicles\rhs_zsutank_base\Wheels\L7,
        "L7": {
            "boneName": "wheel_podkolol6",
            "center": "wheel_1_7_axis",
            "boundary": "wheel_1_7_bound",
            "suspTravelDirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.33,
            "mass": 150,
            "MOI": 10,
            "maxBrakeTorque": 8000,
            "sprungMass": -1,
            "springStrength": 150000,
            "springDamperRate": 11000,
            "dampingRate": 2174,
            "dampingRateInAir": 2174,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "latStiffX": 3.5,
            "latStiffY": 35,
            "longitudinalStiffnessPerUnitGravity": 14000,
            "frictionVsSlipGraph": [[0,0.45],[0.18,1],[0.6,0.6]]
        },
        # Class: CfgVehicles\rhs_zsutank_base\Wheels\L9,
        "L9": {
            "boneName": "wheel_podkolol9",
            "center": "wheel_1_9_axis",
            "boundary": "wheel_1_9_bound",
            "maxDroop": 0,
            "maxCompression": 0,
            "suspTravelDirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.33,
            "mass": 150,
            "MOI": 10,
            "maxBrakeTorque": 8000,
            "sprungMass": -1,
            "springStrength": 150000,
            "springDamperRate": 11000,
            "dampingRate": 2174,
            "dampingRateInAir": 2174,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3.5,
            "latStiffY": 35,
            "longitudinalStiffnessPerUnitGravity": 14000,
            "frictionVsSlipGraph": [[0,0.45],[0.18,1],[0.6,0.6]]
        },
        # Class: CfgVehicles\rhs_zsutank_base\Wheels\L1,
        "L1": {
            "boneName": "",
            "center": "wheel_1_1_axis",
            "boundary": "wheel_1_1_bound",
            "maxDroop": 0,
            "maxCompression": 0,
            "suspTravelDirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.33,
            "mass": 150,
            "MOI": 10,
            "maxBrakeTorque": 8000,
            "sprungMass": -1,
            "springStrength": 150000,
            "springDamperRate": 11000,
            "dampingRate": 2174,
            "dampingRateInAir": 2174,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3.5,
            "latStiffY": 35,
            "longitudinalStiffnessPerUnitGravity": 14000,
            "frictionVsSlipGraph": [[0,0.45],[0.18,1],[0.6,0.6]]
        },
        # Class: CfgVehicles\rhs_zsutank_base\Wheels\R2,
        "R2": {
            "boneName": "wheel_podkolop1",
            "center": "wheel_2_2_axis",
            "boundary": "wheel_2_2_bound",
            "side": "right",
            "suspTravelDirection": [0.125,-1,0],
            "steering": 0,
            "width": 0.33,
            "mass": 150,
            "MOI": 10,
            "maxBrakeTorque": 8000,
            "sprungMass": -1,
            "springStrength": 150000,
            "springDamperRate": 11000,
            "dampingRate": 2174,
            "dampingRateInAir": 2174,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "latStiffX": 3.5,
            "latStiffY": 35,
            "longitudinalStiffnessPerUnitGravity": 14000,
            "frictionVsSlipGraph": [[0,0.45],[0.18,1],[0.6,0.6]]
        },
        # Class: CfgVehicles\rhs_zsutank_base\Wheels\R3,
        "R3": {
            "boneName": "wheel_podkolop2",
            "center": "wheel_2_3_axis",
            "boundary": "wheel_2_3_bound",
            "side": "right",
            "suspTravelDirection": [0.125,-1,0],
            "steering": 0,
            "width": 0.33,
            "mass": 150,
            "MOI": 10,
            "maxBrakeTorque": 8000,
            "sprungMass": -1,
            "springStrength": 150000,
            "springDamperRate": 11000,
            "dampingRate": 2174,
            "dampingRateInAir": 2174,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "latStiffX": 3.5,
            "latStiffY": 35,
            "longitudinalStiffnessPerUnitGravity": 14000,
            "frictionVsSlipGraph": [[0,0.45],[0.18,1],[0.6,0.6]]
        },
        # Class: CfgVehicles\rhs_zsutank_base\Wheels\R4,
        "R4": {
            "boneName": "wheel_podkolop3",
            "center": "wheel_2_4_axis",
            "boundary": "wheel_2_4_bound",
            "side": "right",
            "suspTravelDirection": [0.125,-1,0],
            "steering": 0,
            "width": 0.33,
            "mass": 150,
            "MOI": 10,
            "maxBrakeTorque": 8000,
            "sprungMass": -1,
            "springStrength": 150000,
            "springDamperRate": 11000,
            "dampingRate": 2174,
            "dampingRateInAir": 2174,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "latStiffX": 3.5,
            "latStiffY": 35,
            "longitudinalStiffnessPerUnitGravity": 14000,
            "frictionVsSlipGraph": [[0,0.45],[0.18,1],[0.6,0.6]]
        },
        # Class: CfgVehicles\rhs_zsutank_base\Wheels\R5,
        "R5": {
            "boneName": "wheel_podkolop4",
            "center": "wheel_2_5_axis",
            "boundary": "wheel_2_5_bound",
            "side": "right",
            "suspTravelDirection": [0.125,-1,0],
            "steering": 0,
            "width": 0.33,
            "mass": 150,
            "MOI": 10,
            "maxBrakeTorque": 8000,
            "sprungMass": -1,
            "springStrength": 150000,
            "springDamperRate": 11000,
            "dampingRate": 2174,
            "dampingRateInAir": 2174,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "latStiffX": 3.5,
            "latStiffY": 35,
            "longitudinalStiffnessPerUnitGravity": 14000,
            "frictionVsSlipGraph": [[0,0.45],[0.18,1],[0.6,0.6]]
        },
        # Class: CfgVehicles\rhs_zsutank_base\Wheels\R6,
        "R6": {
            "boneName": "wheel_podkolop5",
            "center": "wheel_2_6_axis",
            "boundary": "wheel_2_6_bound",
            "side": "right",
            "suspTravelDirection": [0.125,-1,0],
            "steering": 0,
            "width": 0.33,
            "mass": 150,
            "MOI": 10,
            "maxBrakeTorque": 8000,
            "sprungMass": -1,
            "springStrength": 150000,
            "springDamperRate": 11000,
            "dampingRate": 2174,
            "dampingRateInAir": 2174,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "latStiffX": 3.5,
            "latStiffY": 35,
            "longitudinalStiffnessPerUnitGravity": 14000,
            "frictionVsSlipGraph": [[0,0.45],[0.18,1],[0.6,0.6]]
        },
        # Class: CfgVehicles\rhs_zsutank_base\Wheels\R7,
        "R7": {
            "boneName": "wheel_podkolop6",
            "center": "wheel_2_7_axis",
            "boundary": "wheel_2_7_bound",
            "side": "right",
            "suspTravelDirection": [0.125,-1,0],
            "steering": 0,
            "width": 0.33,
            "mass": 150,
            "MOI": 10,
            "maxBrakeTorque": 8000,
            "sprungMass": -1,
            "springStrength": 150000,
            "springDamperRate": 11000,
            "dampingRate": 2174,
            "dampingRateInAir": 2174,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "latStiffX": 3.5,
            "latStiffY": 35,
            "longitudinalStiffnessPerUnitGravity": 14000,
            "frictionVsSlipGraph": [[0,0.45],[0.18,1],[0.6,0.6]]
        },
        # Class: CfgVehicles\rhs_zsutank_base\Wheels\R9,
        "R9": {
            "boneName": "wheel_podkolop9",
            "center": "wheel_2_9_axis",
            "boundary": "wheel_2_9_bound",
            "maxDroop": 0,
            "maxCompression": 0,
            "side": "right",
            "suspTravelDirection": [0.125,-1,0],
            "steering": 0,
            "width": 0.33,
            "mass": 150,
            "MOI": 10,
            "maxBrakeTorque": 8000,
            "sprungMass": -1,
            "springStrength": 150000,
            "springDamperRate": 11000,
            "dampingRate": 2174,
            "dampingRateInAir": 2174,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3.5,
            "latStiffY": 35,
            "longitudinalStiffnessPerUnitGravity": 14000,
            "frictionVsSlipGraph": [[0,0.45],[0.18,1],[0.6,0.6]]
        },
        # Class: CfgVehicles\rhs_zsutank_base\Wheels\R1,
        "R1": {
            "boneName": "",
            "center": "wheel_2_1_axis",
            "boundary": "wheel_2_1_bound",
            "maxDroop": 0,
            "maxCompression": 0,
            "side": "right",
            "suspTravelDirection": [0.125,-1,0],
            "steering": 0,
            "width": 0.33,
            "mass": 150,
            "MOI": 10,
            "maxBrakeTorque": 8000,
            "sprungMass": -1,
            "springStrength": 150000,
            "springDamperRate": 11000,
            "dampingRate": 2174,
            "dampingRateInAir": 2174,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3.5,
            "latStiffY": 35,
            "longitudinalStiffnessPerUnitGravity": 14000,
            "frictionVsSlipGraph": [[0,0.45],[0.18,1],[0.6,0.6]]
        }
    },
    "accuracy": 0.3,
    "destrType": "DestructDefault",
    "model": "rhsafrf|addons|rhs_a2port_armor|rhs_zsu",
    "picture": "rhsafrf|addons|rhs_a2port_armor|pictures|rhs_zsu23_pic_ca.paa",
    "Icon": "rhsafrf|addons|rhs_a2port_armor|data|icomap_zsu_CA.paa",
    "crew": "rhs_msv_crew",
    "typicalCargo": [],
    "side": 0,
    "tracksSpeed": 1,
    "irTarget": 1,
    "irTargetSize": 1,
    "visualTarget": 1,
    "visualTargetSize": 1,
    "radarTarget": 1,
    "radarTargetSize": 1.2,
    "receiveRemoteTargets": 1,
    "cost": 1.5e+006,
    "damageResistance": 0.02,
    "crewVulnerable": 1,
    "drivercompartments": "Compartment1",
    "getInAction": "GetInLow",
    "getOutAction": "GetOutLow",
    "driverAction": "RHS_ZSU_Driver",
    "driverInAction": "RHS_ZSU_Driver",
    "driverDoor": "hatchD",
    "forceHideDriver": 0,
    "driverForceOptics": 1,
    "viewDriverInExternal": 1,
    "LODDriverOpticsIn": 0,
    "LODDriverOpticsOut": 0,
    "LODDriverTurnedIn": 0,
    "LODDriverTurnedOut": 0,
    "unitInfoType": "RHS_RscUnitInfoEastTank",
    "mapSize": 6.5,
    "commanderCanSee": 31,
    "gunnerCanSee": "1+16+4+8",
    "threat": [0.5,0.5,1],
    "irScanGround": 0,
    "irScanRangeMax": 19000,
    "radarType": 4,
    "incomingMissileDetectionSystem": 0,
    "driverOpticsModel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tnpo170a",
    "armor": 200,
    "armorStructural": 600,
    # Class: CfgVehicles\rhs_zsutank_base\ViewOptics,
    "ViewOptics": {
        "initFov": 0.7,
        "minFov": 0.7,
        "maxFov": 0.7,
        "visionMode": ["Normal","NVG"],
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
    # Class: CfgVehicles\rhs_zsutank_base\HitPoints,
    "HitPoints": {
        # Class: CfgVehicles\rhs_zsutank_base\HitPoints\HitHull
        "HitHull": {
            "armor": 0.45,
            "material": -1,
            "name": "telo",
            "visual": "zbytek",
            "passThrough": 0,
            "minimalHit": 0.14,
            "explosionShielding": 0.5,
            "radius": 0.25,
            "armorComponent": "hit_hull"
        },
        # Class: CfgVehicles\rhs_zsutank_base\HitPoints\HitEngine,
        "HitEngine": {
            "armor": 0.45,
            "material": -1,
            "name": "motor",
            "visual": "zbytek",
            "passThrough": 0.01,
            "minimalHit": 0.03,
            "explosionShielding": 0.05,
            "radius": 0.2,
            # Class: CfgVehicles\rhs_zsutank_base\HitPoints\HitEngine\DestructionEffects,
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\rhs_zsutank_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Smoke,
                "RHS_Engine_Smoke": {
                    "simulation": "particles",
                    "type": "SmallWreckSmoke",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\rhs_zsutank_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Fire,
                "RHS_Engine_Fire": {
                    "type": "SmallFireFPlace",
                    "simulation": "particles",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\rhs_zsutank_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Sparks,
                "RHS_Engine_Sparks": {
                    "type": "RHS_FireSparks",
                    "simulation": "particles",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\rhs_zsutank_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Sounds,
                "RHS_Engine_Sounds": {
                    "simulation": "sound",
                    "type": "Fire",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\rhs_zsutank_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Smoke_small1,
                "RHS_Engine_Smoke_small1": {
                    "type": "WeaponWreckSmoke",
                    "position": "engine_smoke2",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\rhs_zsutank_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Smoke_small2,
                "RHS_Engine_Smoke_small2": {
                    "position": "engine_smoke3",
                    "type": "WeaponWreckSmoke",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\rhs_zsutank_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Smoke_small3,
                "RHS_Engine_Smoke_small3": {
                    "position": "engine_smoke4",
                    "simulation": "particles",
                    "type": "SmallWreckSmoke",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\rhs_zsutank_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Fire2,
                "RHS_Engine_Fire2": {
                    "type": "SmallFireFPlace",
                    "position": "engine_smoke4",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\rhs_zsutank_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Sparks2,
                "RHS_Engine_Sparks2": {
                    "type": "RHS_FireSparks",
                    "position": "engine_smoke4",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                }
            }
        },
        # Class: CfgVehicles\rhs_zsutank_base\HitPoints\HitLTrack,
        "HitLTrack": {
            "armor": 0.5,
            "material": -1,
            "name": "pas_L",
            "passThrough": 0,
            "minimalHit": 0.15,
            "explosionShielding": 0.5,
            "radius": 0.3,
            "armorComponent": "hit_trackL",
            "visual": "pas_L"
        },
        # Class: CfgVehicles\rhs_zsutank_base\HitPoints\HitRTrack,
        "HitRTrack": {
            "armor": 0.5,
            "material": -1,
            "name": "pas_P",
            "passThrough": 0,
            "minimalHit": 0.15,
            "explosionShielding": 0.5,
            "radius": 0.3,
            "armorComponent": "hit_trackR",
            "visual": "pas_P"
        },
        # Class: CfgVehicles\APC_Tracked_02_base_F\HitPoints\HitFuel,
        "HitFuel": {
            "armor": 0.5,
            "material": -1,
            "armorComponent": "hit_fuel",
            "name": "hit_fuel_point",
            "visual": "-",
            "passThrough": 0.1,
            "minimalHit": 0.1,
            "explosionShielding": 0.6,
            "radius": 0.3
        },
        # Class: CfgVehicles\APC_Tracked_02_base_F\HitPoints\HitSLAT_Left_1,
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
        # Class: CfgVehicles\APC_Tracked_02_base_F\HitPoints\HitSLAT_Left_2,
        "HitSLAT_Left_2": {
            "armorComponent": "cage_left_2_geo",
            "name": "cage_left_2_point",
            "visual": "-",
            "simulation": "Armor_SLAT",
            "armor": -200,
            "minimalHit": 0.3,
            "passThrough": 0,
            "explosionShielding": 2,
            "radius": 0.25
        },
        # Class: CfgVehicles\APC_Tracked_02_base_F\HitPoints\HitSLAT_Left_3,
        "HitSLAT_Left_3": {
            "armorComponent": "cage_left_3_geo",
            "name": "cage_left_3_point",
            "visual": "-",
            "simulation": "Armor_SLAT",
            "armor": -200,
            "minimalHit": 0.3,
            "passThrough": 0,
            "explosionShielding": 2,
            "radius": 0.25
        },
        # Class: CfgVehicles\APC_Tracked_02_base_F\HitPoints\HitSLAT_Right_1,
        "HitSLAT_Right_1": {
            "armorComponent": "cage_right_1_geo",
            "name": "cage_right_1_point",
            "visual": "-",
            "simulation": "Armor_SLAT",
            "armor": -200,
            "minimalHit": 0.3,
            "passThrough": 0,
            "explosionShielding": 2,
            "radius": 0.25
        },
        # Class: CfgVehicles\APC_Tracked_02_base_F\HitPoints\HitSLAT_Right_2,
        "HitSLAT_Right_2": {
            "armorComponent": "cage_right_2_geo",
            "name": "cage_right_2_point",
            "visual": "-",
            "simulation": "Armor_SLAT",
            "armor": -200,
            "minimalHit": 0.3,
            "passThrough": 0,
            "explosionShielding": 2,
            "radius": 0.25
        },
        # Class: CfgVehicles\APC_Tracked_02_base_F\HitPoints\HitSLAT_Right_3,
        "HitSLAT_Right_3": {
            "armorComponent": "cage_right_3_geo",
            "name": "cage_right_3_point",
            "visual": "-",
            "simulation": "Armor_SLAT",
            "armor": -200,
            "minimalHit": 0.3,
            "passThrough": 0,
            "explosionShielding": 2,
            "radius": 0.25
        },
        # Class: CfgVehicles\APC_Tracked_02_base_F\HitPoints\HitSLAT_back,
        "HitSLAT_back": {
            "armorComponent": "cage_back_geo",
            "name": "cage_back_point",
            "visual": "-",
            "simulation": "Armor_SLAT",
            "armor": -200,
            "minimalHit": 0.3,
            "passThrough": 0,
            "explosionShielding": 2,
            "radius": 0.25
        },
        # Class: CfgVehicles\APC_Tracked_02_base_F\HitPoints\HitSLAT_front,
        "HitSLAT_front": {
            "armorComponent": "cage_front_geo",
            "name": "cage_front_point",
            "visual": "-",
            "simulation": "Armor_SLAT",
            "armor": -200,
            "minimalHit": 0.3,
            "passThrough": 0,
            "explosionShielding": 2,
            "radius": 0.25
        }
    },
    # Class: CfgVehicles\rhs_zsutank_base\RenderTargets,
    "RenderTargets": {
    },
    # Class: CfgVehicles\rhs_zsutank_base\TransportMagazines,
    "TransportMagazines": {
        # Class: CfgVehicles\rhs_zsutank_base\TransportMagazines\_xx_30Rnd_545x39_AK
        "_xx_30Rnd_545x39_AK": {
            "magazine": "rhs_30Rnd_545x39_7N10_AK",
            "count": "10"
        },
        # Class: CfgVehicles\rhs_zsutank_base\TransportMagazines\_xx_HandGrenade_East,
        "_xx_HandGrenade_East": {
            "magazine": "rhs_mag_rgd5",
            "count": "10"
        },
        # Class: CfgVehicles\rhs_zsutank_base\TransportMagazines\_xx_signal_rounds,
        "_xx_signal_rounds": {
            "magazine": "rhs_mag_nspn_red",
            "count": "10"
        }
    },
    # Class: CfgVehicles\rhs_zsutank_base\TransportWeapons,
    "TransportWeapons": {
        # Class: CfgVehicles\rhs_zsutank_base\TransportWeapons\_xx_AK74M
        "_xx_AK74M": {
            "weapon": "rhs_weap_ak74m",
            "count": 1
        }
    },
    # Class: CfgVehicles\rhs_zsutank_base\TransportItems,
    "TransportItems": {
        # Class: CfgVehicles\rhs_zsutank_base\TransportItems\_xx_FirstAidKit
        "_xx_FirstAidKit": {
            "name": "FirstAidKit",
            "count": 4
        }
    },
    "hiddenSelections": ["camo1","camo2","camo3","n1","n2","n3"],
    "hiddenSelectionsTextures": ["|rhsafrf|addons|rhs_a2port_armor|data|zsu_01_co.paa","|rhsafrf|addons|rhs_a2port_armor|data|zsu_02_co.paa","|rhsafrf|addons|rhs_a2port_armor|data|zsu_03_co.paa","rhsafrf|addons|rhs_decals|Data|Labels|Misc|no_ca.paa","rhsafrf|addons|rhs_decals|Data|Labels|Misc|no_ca.paa","rhsafrf|addons|rhs_decals|Data|Labels|Misc|no_ca.paa"],
    # Class: CfgVehicles\rhs_zsutank_base\textureSources,
    "textureSources": {
        # Class: CfgVehicles\rhs_zsutank_base\textureSources\standard
        "standard": {
            "displayName": "Standard",
            "textures": ["|rhsafrf|addons|rhs_a2port_armor|data|zsu_01_co.paa","|rhsafrf|addons|rhs_a2port_armor|data|zsu_02_co.paa","|rhsafrf|addons|rhs_a2port_armor|data|zsu_03_co.paa"],
            "factions": ["rhs_faction_vpvo"]
        },
        # Class: CfgVehicles\rhs_zsutank_base\textureSources\Chdkz,
        "Chdkz": {
            "displayName": "Chedaki",
            "textures": ["|rhsafrf|addons|rhs_a2port_armor|data|zsu_01_gue_co.paa","|rhsafrf|addons|rhs_a2port_armor|data|zsu_02_gue_co.paa","|rhsafrf|addons|rhs_a2port_armor|data|zsu_03_gue_co.paa"],
            "factions": []
        },
        # Class: CfgVehicles\rhs_zsutank_base\textureSources\rhs_sand,
        "rhs_sand": {
            "displayName": "Sand",
            "author": "beaar",
            "textures": ["|rhsafrf|addons|rhs_a2port_armor_camo|data|zsu_01_des_co.paa","|rhsafrf|addons|rhs_a2port_armor_camo|data|zsu_02_des_co.paa","|rhsafrf|addons|rhs_a2port_armor_camo|data|zsu_03_des_co.paa"],
            "factions": []
        },
        # Class: CfgVehicles\rhs_zsutank_base\textureSources\CDF,
        "CDF": {
            "displayName": "CDF",
            "author": "Red Hammer Studios",
            "textures": ["|rhsgref|addons|rhsgref_vehicles_ret|data|cdf|zsu_01_cdf_co.paa","|rhsgref|addons|rhsgref_vehicles_ret|data|cdf|zsu_02_cdf_co.paa","|rhsgref|addons|rhsgref_vehicles_ret|data|cdf|zsu_03_cdf_co.paa"],
            "factions": []
        }
    },
    "textureList": [],
    # Class: CfgVehicles\rhs_zsutank_base\Attributes,
    "Attributes": {
        # Class: CfgVehicles\rhs_zsutank_base\Attributes\ObjectTexture
        "ObjectTexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayName": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        # Class: CfgVehicles\rhs_zsutank_base\Attributes\rhs_decalNumber_type,
        "rhs_decalNumber_type": {
            "displayName": "Define font type of plate number",
            "tooltip": "Define kind of font that will be drawn on vehicle.",
            "property": "rhs_decalNumber_type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value,true];[_this,[['Number', cRHSZSUNumberPlaces, _value]]] call rhs_fnc_decalsInit",
            "defaultValue": 0,
            "typeName": "STRING",
            # Class: CfgVehicles\rhs_zsutank_base\Attributes\rhs_decalNumber_type\values,
            "values": {
                # Class: CfgVehicles\rhs_zsutank_base\Attributes\rhs_decalNumber_type\values\Default
                "Default": {
                    "name": "Default",
                    "value": "Default",
                    "defaultValue": "Default"
                },
                # Class: CfgVehicles\rhs_zsutank_base\Attributes\rhs_decalNumber_type\values\DefaultRed,
                "DefaultRed": {
                    "name": "Default (Red)",
                    "value": "DefaultRed"
                },
                # Class: CfgVehicles\rhs_zsutank_base\Attributes\rhs_decalNumber_type\values\BoldRed,
                "BoldRed": {
                    "name": "Bold Red",
                    "value": "BoldRed"
                },
                # Class: CfgVehicles\rhs_zsutank_base\Attributes\rhs_decalNumber_type\values\CDF,
                "CDF": {
                    "name": "CDF",
                    "value": "CDF"
                },
                # Class: CfgVehicles\rhs_zsutank_base\Attributes\rhs_decalNumber_type\values\Handpaint,
                "Handpaint": {
                    "name": "Handpaint",
                    "value": "Handpaint"
                },
                # Class: CfgVehicles\rhs_zsutank_base\Attributes\rhs_decalNumber_type\values\HandpaintBlack,
                "HandpaintBlack": {
                    "name": "Handpaint Black",
                    "value": "HandpaintBlack"
                },
                # Class: CfgVehicles\rhs_zsutank_base\Attributes\rhs_decalNumber_type\values\Iraqi,
                "Iraqi": {
                    "name": "Iraqi",
                    "value": "Iraqi"
                },
                # Class: CfgVehicles\rhs_zsutank_base\Attributes\rhs_decalNumber_type\values\LicensePlate,
                "LicensePlate": {
                    "name": "License Plate",
                    "value": "LicensePlate"
                }
            }
        },
        # Class: CfgVehicles\rhs_zsutank_base\Attributes\rhs_decalNumber,
        "rhs_decalNumber": {
            "collapsed": 1,
            "displayName": "Set side number",
            "tooltip": "Set side number. 4 numbers are required. Type 0 to hide numbers complety & leave at -1 to get random number",
            "property": "rhs_decalNumber",
            "control": "Edit",
            "validate": "Number",
            "typeName": "Number",
            "defaultValue": "-1",
            "expression": "if( _value >= 0)then{if( _value == 0)then{{[_this setobjectTexture [_x,'a3|data_f|clear_empty.paa']]}foreach cRHSZSUNumberPlaces}else{[_this, [['Number', cRHSZSUNumberPlaces, _this getVariable ['rhs_decalNumber_type','Default'], _value] ] ] call rhs_fnc_decalsInit}};"
        }
    },
    # Class: CfgVehicles\rhs_zsutank_base\Turrets,
    "Turrets": {
        # Class: CfgVehicles\rhs_zsutank_base\Turrets\MainTurret
        "MainTurret": {
            # Class: CfgVehicles\rhs_zsutank_base\Turrets\MainTurret\Turrets
            "Turrets": {
                # Class: CfgVehicles\rhs_zsutank_base\Turrets\MainTurret\Turrets\CommanderOptics
                "CommanderOptics": {
                    "gunBeg": "gun_muzzle",
                    "gunEnd": "gun_chamber",
                    "body": "ObsTurret",
                    "gun": "ObsGun",
                    "gunnerOutOpticsModel": "",
                    "memoryPointGunnerOutOptics": "commanderview",
                    "memoryPointGunnerOptics": "commanderview",
                    "LODTurnedOut": 1100,
                    "gunnerOpticsEffect": ["TankCommanderOptics1"],
                    "weapons": [],
                    "magazines": [],
                    "turretInfoType": "RscWeaponEmpty",
                    "forceHideGunner": 0,
                    "gunnerInAction": "RHS_ZSU_Commander",
                    "gunnerAction": "RHS_ZSU_CommanderOut",
                    "gunnerDoor": "hatchC",
                    "gunnerForceOptics": 1,
                    "gunnerOpticsModel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tkn3.p3d",
                    "minElev": -10,
                    "maxElev": 60,
                    "initElev": 0,
                    "minTurn": -360,
                    "maxTurn": 360,
                    "initTurn": 0,
                    # Class: CfgVehicles\rhs_zsutank_base\Turrets\MainTurret\Turrets\CommanderOptics\ViewOptics,
                    "ViewOptics": {
                        "initFov": 0.111,
                        "minFov": 0.111,
                        "maxFov": 0.111,
                        "visionMode": ["Normal","NVG"],
                        "initAngleX": 0,
                        "minAngleX": -30,
                        "maxAngleX": 30,
                        "initAngleY": 0,
                        "minAngleY": -100,
                        "maxAngleY": 100,
                        "thermalMode": [0,1],
                        "minMoveX": 0,
                        "maxMoveX": 0,
                        "minMoveY": 0,
                        "maxMoveY": 0,
                        "minMoveZ": 0,
                        "maxMoveZ": 0
                    },
                    "startEngine": 0,
                    "outGunnerMayFire": 0,
                    "maxHorizontalRotSpeed": 2,
                    "maxVerticalRotSpeed": 2,
                    "inGunnerMayFire": 1,
                    "viewGunnerInExternal": 1,
                    # Class: CfgVehicles\rhs_zsutank_base\Turrets\MainTurret\Turrets\CommanderOptics\OpticsIn,
                    "OpticsIn": {
                        # Class: CfgVehicles\rhs_zsutank_base\Turrets\MainTurret\Turrets\CommanderOptics\OpticsIn\Wide
                        "Wide": {
                            "gunnerOpticsModel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tkn3.p3d",
                            "gunnerOutOpticsModel": "",
                            "initFov": 0.111,
                            "minFov": 0.111,
                            "maxFov": 0.111,
                            "visionMode": ["Normal","NVG"],
                            "initAngleX": 0,
                            "minAngleX": -30,
                            "maxAngleX": 30,
                            "initAngleY": 0,
                            "minAngleY": -100,
                            "maxAngleY": 100,
                            "thermalMode": [0,1],
                            "minMoveX": 0,
                            "maxMoveX": 0,
                            "minMoveY": 0,
                            "maxMoveY": 0,
                            "minMoveZ": 0,
                            "maxMoveZ": 0
                        },
                        # Class: CfgVehicles\rhs_zsutank_base\Turrets\MainTurret\Turrets\CommanderOptics\OpticsIn\Periscope,
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
                            "gunnerOpticsModel": "a3|weapons_f|reticle|Optics_Driver_01_f",
                            "gunnerOpticsEffect": ["TankGunnerOptics1","OpticsBlur2","OpticsCHAbera2"],
                            "thermalMode": [0,1],
                            "minMoveX": 0,
                            "maxMoveX": 0,
                            "minMoveY": 0,
                            "maxMoveY": 0,
                            "minMoveZ": 0,
                            "maxMoveZ": 0
                        }
                    },
                    # Class: CfgVehicles\rhs_zsutank_base\Turrets\MainTurret\Turrets\CommanderOptics\Components,
                    "Components": {
                        # Class: CfgVehicles\rhs_zsutank_base\Turrets\MainTurret\Turrets\CommanderOptics\Components\AICarSteeringComponent
                        "AICarSteeringComponent": {
                            "steeringPIDWeights": [1.2,0.1,0.2],
                            "speedPIDWeights": [1.7,1.3,1.1],
                            "doRemapSpeed": 1,
                            "remapSpeedRange": [40,50],
                            "remapSpeedScalar": [1,0.35],
                            "doPredictForward": 1,
                            "predictForwardRange": [0.1,20],
                            "steerAheadSaturation": [0.01,0.4],
                            "speedPredictionMethod": 1,
                            "wheelAngleCoef": 0.7,
                            "forwardAngleCoef": 0.7,
                            "steeringAngleCoef": 1,
                            "differenceAngleCoef": 1,
                            "stuckMaxTime": 3,
                            "allowOvertaking": 1,
                            "allowCollisionAvoidance": 1,
                            "allowDrifting": 0,
                            "maxWheelAngleDiff": 0.2616,
                            "minSpeedToKeep": 0.1,
                            "commandTurnFactor": 1
                        },
                        # Class: CfgVehicles\rhs_zsutank_base\Turrets\MainTurret\Turrets\CommanderOptics\Components\VehicleSystemsDisplayManagerComponentLeft,
                        "VehicleSystemsDisplayManagerComponentLeft": {
                            # Class: CfgVehicles\rhs_zsutank_base\Turrets\MainTurret\Turrets\CommanderOptics\Components\VehicleSystemsDisplayManagerComponentLeft\Components
                            "Components": {
                                # Class: CfgVehicles\rhs_zsutank_base\Turrets\MainTurret\Turrets\CommanderOptics\Components\VehicleSystemsDisplayManagerComponentLeft\Components\EmptyDisplay
                                "EmptyDisplay": {
                                    "componentType": "EmptyDisplayComponent"
                                },
                                # Class: CfgVehicles\rhs_zsutank_base\Turrets\MainTurret\Turrets\CommanderOptics\Components\VehicleSystemsDisplayManagerComponentLeft\Components\CrewDisplay,
                                "CrewDisplay": {
                                    "componentType": "CrewDisplayComponent",
                                    "resource": "RscCustomInfoCrew"
                                },
                                # Class: CfgVehicles\rhs_zsutank_base\Turrets\MainTurret\Turrets\CommanderOptics\Components\VehicleSystemsDisplayManagerComponentLeft\Components\SensorDisplay,
                                "SensorDisplay": {
                                    "componentType": "SensorsDisplayComponent",
                                    "range": [2000,4000,8000,14000],
                                    "resource": "RscCustomInfoSensors"
                                }
                            },
                            "componentType": "VehicleSystemsDisplayManager",
                            "left": 1,
                            "defaultDisplay": "EmptyDisplay",
                            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,	(safezoneX + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40))])",
                            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                        },
                        # Class: CfgVehicles\rhs_zsutank_base\Turrets\MainTurret\Turrets\CommanderOptics\Components\VehicleSystemsDisplayManagerComponentRight,
                        "VehicleSystemsDisplayManagerComponentRight": {
                            "defaultDisplay": "SensorDisplay",
                            # Class: CfgVehicles\rhs_zsutank_base\Turrets\MainTurret\Turrets\CommanderOptics\Components\VehicleSystemsDisplayManagerComponentRight\Components,
                            "Components": {
                                # Class: CfgVehicles\rhs_zsutank_base\Turrets\MainTurret\Turrets\CommanderOptics\Components\VehicleSystemsDisplayManagerComponentRight\Components\EmptyDisplay
                                "EmptyDisplay": {
                                    "componentType": "EmptyDisplayComponent"
                                },
                                # Class: CfgVehicles\rhs_zsutank_base\Turrets\MainTurret\Turrets\CommanderOptics\Components\VehicleSystemsDisplayManagerComponentRight\Components\CrewDisplay,
                                "CrewDisplay": {
                                    "componentType": "CrewDisplayComponent",
                                    "resource": "RscCustomInfoCrew"
                                },
                                # Class: CfgVehicles\rhs_zsutank_base\Turrets\MainTurret\Turrets\CommanderOptics\Components\VehicleSystemsDisplayManagerComponentRight\Components\SensorDisplay,
                                "SensorDisplay": {
                                    "componentType": "SensorsDisplayComponent",
                                    "range": [2000,4000,8000,14000],
                                    "resource": "RscCustomInfoSensors"
                                }
                            },
                            "componentType": "VehicleSystemsDisplayManager",
                            "right": 1,
                            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,	((safezoneX + safezoneW) - (		(10 * 			(			((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40)))])",
                            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                        }
                    },
                    "minCamElev": -90,
                    "maxCamElev": 90,
                    "soundServo": ["A3|Sounds_F|vehicles|armor|APC|noises|servo_APC_comm",0.562341,1,30],
                    "soundServoVertical": ["A3|Sounds_F|vehicles|armor|APC|noises|servo_APC_comm",0.562341,1,30],
                    "gunnerGetInAction": "GetInAMV_cargo",
                    "gunnerGetOutAction": "GetOutLow",
                    "usePip": 2,
                    "turretFollowFreeLook": 2,
                    "LODOpticsIn": 0,
                    "isPersonTurret": 1,
                    "personTurretAction": "vehicle_turnout_1",
                    "minOutElev": -20,
                    "maxOutElev": 40,
                    "initOutElev": 0,
                    "minOutTurn": -150,
                    "maxOutTurn": 120,
                    "initOutTurn": 0,
                    "animationSourceStickX": "com_turret_control_x",
                    "animationSourceStickY": "com_turret_control_y",
                    "gunnerLeftHandAnimName": "com_turret_control",
                    "viewGunnerShadowAmb": 0.5,
                    "viewGunnerShadowDiff": 0.05,
                    # Class: CfgVehicles\APC_Tracked_02_base_F\Turrets\MainTurret\Turrets\CommanderOptics\ViewGunner,
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
                    "showCrewAim": 1,
                    # Class: CfgVehicles\APC_Tracked_02_base_F\Turrets\MainTurret\Turrets\CommanderOptics\HitPoints,
                    "HitPoints": {
                        # Class: CfgVehicles\APC_Tracked_02_base_F\Turrets\MainTurret\Turrets\CommanderOptics\HitPoints\HitComTurret
                        "HitComTurret": {
                            "armor": 0.08,
                            "material": -1,
                            "armorComponent": "hit_com_turret",
                            "name": "hit_com_turret_point",
                            "visual": "vezVelitele",
                            "passThrough": 0.4,
                            "minimalHit": 0.1,
                            "explosionShielding": 1,
                            "radius": 0.15,
                            "isTurret": 1
                        },
                        # Class: CfgVehicles\APC_Tracked_02_base_F\Turrets\MainTurret\Turrets\CommanderOptics\HitPoints\HitComGun,
                        "HitComGun": {
                            "armor": 0.04,
                            "material": -1,
                            "armorComponent": "hit_com_gun",
                            "name": "hit_com_gun_point",
                            "visual": "zbranVelitele",
                            "passThrough": 0,
                            "minimalHit": 0.1,
                            "explosionShielding": 1,
                            "radius": 0.15,
                            "isGun": 1
                        }
                    },
                    "stabilizedInAxes": 3,
                    "gunnerHasFlares": 1,
                    "proxyType": "CPCommander",
                    "proxyIndex": 1,
                    "gunnerName": "Commander",
                    "primaryGunner": 0,
                    "primaryObserver": 1,
                    "animationSourceBody": "obsTurret",
                    "animationSourceGun": "obsGun",
                    "animationSourceHatch": "hatchCommander",
                    "animationSourceCamElev": "camElev",
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
                    "gunnerOpticsShowCursor": 0,
                    "gunnerFireAlsoInInternalCamera": 1,
                    "gunnerOutFireAlsoInInternalCamera": 1,
                    "gunnerUsesPilotView": 0,
                    "castGunnerShadow": 0,
                    "viewGunnerShadow": 1,
                    "ejectDeadGunner": 0,
                    "hideWeaponsGunner": 1,
                    "canHideGunner": -1,
                    "showHMD": 0,
                    "lockWhenDriverOut": 0,
                    "lockWhenVehicleSpeed": -1,
                    "gunnerCompartments": "Compartment1",
                    "LODTurnedIn": -1,
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
                    "gunnerRightHandAnimName": "",
                    "gunnerLeftLegAnimName": "",
                    "gunnerRightLegAnimName": "",
                    "preciseGetInOut": 0,
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
                    }
                }
            },
            # Class: CfgVehicles\rhs_zsutank_base\Turrets\MainTurret\Components,
            "Components": {
                # Class: CfgVehicles\rhs_zsutank_base\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentLeft
                "VehicleSystemsDisplayManagerComponentLeft": {
                    # Class: CfgVehicles\rhs_zsutank_base\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentLeft\Components
                    "Components": {
                        # Class: CfgVehicles\rhs_zsutank_base\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentLeft\Components\EmptyDisplay
                        "EmptyDisplay": {
                            "componentType": "EmptyDisplayComponent"
                        },
                        # Class: CfgVehicles\rhs_zsutank_base\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentLeft\Components\CrewDisplay,
                        "CrewDisplay": {
                            "componentType": "CrewDisplayComponent",
                            "resource": "RscCustomInfoCrew"
                        },
                        # Class: CfgVehicles\rhs_zsutank_base\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentLeft\Components\SensorDisplay,
                        "SensorDisplay": {
                            "componentType": "SensorsDisplayComponent",
                            "range": [2000,4000,8000,16000],
                            "resource": "RscCustomInfoSensors"
                        }
                    },
                    "componentType": "VehicleSystemsDisplayManager",
                    "left": 1,
                    "defaultDisplay": "EmptyDisplay",
                    "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,	(safezoneX + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40))])",
                    "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                },
                # Class: CfgVehicles\rhs_zsutank_base\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentRight,
                "VehicleSystemsDisplayManagerComponentRight": {
                    "defaultDisplay": "SensorDisplay",
                    # Class: CfgVehicles\rhs_zsutank_base\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentRight\Components,
                    "Components": {
                        # Class: CfgVehicles\rhs_zsutank_base\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentRight\Components\EmptyDisplay
                        "EmptyDisplay": {
                            "componentType": "EmptyDisplayComponent"
                        },
                        # Class: CfgVehicles\rhs_zsutank_base\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentRight\Components\CrewDisplay,
                        "CrewDisplay": {
                            "componentType": "CrewDisplayComponent",
                            "resource": "RscCustomInfoCrew"
                        },
                        # Class: CfgVehicles\rhs_zsutank_base\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentRight\Components\SensorDisplay,
                        "SensorDisplay": {
                            "componentType": "SensorsDisplayComponent",
                            "range": [2000,4000,8000,16000],
                            "resource": "RscCustomInfoSensors"
                        }
                    },
                    "componentType": "VehicleSystemsDisplayManager",
                    "right": 1,
                    "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,	((safezoneX + safezoneW) - (		(10 * 			(			((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40)))])",
                    "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                }
            },
            "LODTurnedOut": 1100,
            "weapons": ["RHS_weap_AZP23"],
            "magazines": ["rhs_mag_AZP23_2000"],
            "forceHideGunner": 0,
            "minElev": -4.5,
            "maxElev": 85,
            "minTurn": -360,
            "maxTurn": 360,
            "maxHorizontalRotSpeed": 0.94,
            "maxVerticalRotSpeed": 0.6,
            # Class: CfgVehicles\rhs_zsutank_base\Turrets\MainTurret\OpticsIn,
            "OpticsIn": {
                # Class: CfgVehicles\rhs_zsutank_base\Turrets\MainTurret\OpticsIn\Wide
                "Wide": {
                    "initFov": 0.35,
                    "minFov": 0.35,
                    "maxFov": 0.35,
                    "gunnerOpticsModel": "rhsafrf|addons|rhs_a2port_armor|2Dscope_RUAA8",
                    "gunnerOutOpticsModel": "",
                    "visionMode": ["Normal"],
                    "gunnerOpticsEffect": ["TankGunnerOptics1","OpticsBlur2","OpticsCHAbera2"],
                    "initAngleX": 0,
                    "minAngleX": -30,
                    "maxAngleX": 30,
                    "initAngleY": 0,
                    "minAngleY": -100,
                    "maxAngleY": 100,
                    "thermalMode": [0,1],
                    "minMoveX": 0,
                    "maxMoveX": 0,
                    "minMoveY": 0,
                    "maxMoveY": 0,
                    "minMoveZ": 0,
                    "maxMoveZ": 0
                },
                # Class: CfgVehicles\rhs_zsutank_base\Turrets\MainTurret\OpticsIn\Auto,
                "Auto": {
                    "initFov": 0.175,
                    "minFov": 0.175,
                    "maxFov": 0.175,
                    "directionStabilized": 1,
                    "gunnerOpticsModel": "rhsafrf|addons|rhs_a2port_armor|2Dscope_RUAA8",
                    "gunnerOutOpticsModel": "",
                    "visionMode": ["Normal"],
                    "gunnerOpticsEffect": ["TankGunnerOptics1","OpticsBlur2","OpticsCHAbera2"],
                    "initAngleX": 0,
                    "minAngleX": -30,
                    "maxAngleX": 30,
                    "initAngleY": 0,
                    "minAngleY": -100,
                    "maxAngleY": 100,
                    "thermalMode": [0,1],
                    "minMoveX": 0,
                    "maxMoveX": 0,
                    "minMoveY": 0,
                    "maxMoveY": 0,
                    "minMoveZ": 0,
                    "maxMoveZ": 0
                }
            },
            "gunnerAction": "RHS_ZSU_GunnerOut",
            "gunnerInAction": "RHS_ZSU_Gunner",
            "gunnerForceOptics": 1,
            # Class: CfgVehicles\rhs_zsutank_base\Turrets\MainTurret\ViewOptics,
            "ViewOptics": {
                "initAngleX": 0,
                "minAngleX": -30,
                "maxAngleX": 30,
                "initAngleY": 0,
                "minAngleY": -100,
                "maxAngleY": 100,
                "initFov": 0.2,
                "minFov": 0.058,
                "maxFov": 0.2,
                "visionMode": ["Normal","NVG"]
            },
            "gunnerDoor": "hatchG",
            "memoryPointGun": ["chase01","chase02","chase03","chase04"],
            "turretInfoType": "RscWeaponZeroing",
            "discreteDistance": [100,200,300,400,500,600,700,800,900,1000],
            "discreteDistanceInitIndex": 5,
            "selectionFireAnim": "zasleh",
            "viewGunnerInExternal": 1,
            # Class: CfgVehicles\rhs_zsutank_base\Turrets\MainTurret\HitPoints,
            "HitPoints": {
                # Class: CfgVehicles\rhs_zsutank_base\Turrets\MainTurret\HitPoints\HitTurret
                "HitTurret": {
                    "armor": 0.5,
                    "material": -1,
                    "name": "vez",
                    "visual": "vez",
                    "passThrough": 0,
                    "minimalHit": 0.14,
                    "explosionShielding": 0.001,
                    "radius": 0.2
                },
                # Class: CfgVehicles\rhs_zsutank_base\Turrets\MainTurret\HitPoints\HitGun,
                "HitGun": {
                    "armor": 0.6,
                    "material": -1,
                    "name": "zbran",
                    "visual": "-",
                    "passThrough": 0,
                    "minimalHit": 0.13,
                    "explosionShielding": 0.001,
                    "radius": 0.2
                }
            },
            "body": "mainTurret",
            "gun": "mainGun",
            "soundServo": ["A3|Sounds_F|vehicles|armor|APC|noises|servo_APC_gunner",0.562341,1,10],
            "soundServoVertical": ["A3|Sounds_F|vehicles|armor|APC|noises|servo_APC_gunner_vertical",0.562341,1,30],
            "initElev": 1,
            "minCamElev": -90,
            "maxCamElev": 90,
            "gunnerGetInAction": "GetInAMV_cargo",
            "gunnerGetOutAction": "GetOutLow",
            "castGunnerShadow": 1,
            "startEngine": 0,
            "stabilizedInAxes": 3,
            "gunnerOpticsModel": "A3|weapons_f|reticle|Optics_Gunner_02_F",
            "gunnerOutOpticsModel": "",
            "usePip": 1,
            "LODOpticsIn": 0,
            "isPersonTurret": 1,
            "personTurretAction": "vehicle_turnout_2",
            "minOutElev": -20,
            "maxOutElev": 40,
            "initOutElev": 0,
            "minOutTurn": -120,
            "maxOutTurn": 150,
            "initOutTurn": 0,
            "animationSourceStickX": "turret_control_x",
            "animationSourceStickY": "turret_control_y",
            "gunnerLeftHandAnimName": "turret_control",
            "viewGunnerShadowAmb": 0.5,
            "viewGunnerShadowDiff": 0.05,
            "memoryPointGunnerOptics": "gunnerview",
            # Class: CfgVehicles\APC_Tracked_02_base_F\Turrets\MainTurret\ViewGunner,
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
            "showCrewAim": 2,
            "commanding": 1,
            "gunBeg": "usti hlavne",
            "gunEnd": "konec hlavne",
            "memoryPointsGetInGunner": "pos gunner",
            "memoryPointsGetInGunnerDir": "pos gunner dir",
            "primaryGunner": 1,
            "gunnerOutOpticsEffect": [],
            "gunnerOpticsEffect": ["TankGunnerOptics2","OpticsBlur1","OpticsCHAbera1"],
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
            "initTurn": 0,
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
            "gunnerOpticsShowCursor": 0,
            "gunnerOutOpticsColor": [0,0,0,1],
            "memoryPointGunnerOutOptics": "",
            "gunnerOutForceOptics": 0,
            "gunnerOutOpticsShowCursor": 0,
            "gunnerFireAlsoInInternalCamera": 1,
            "gunnerOutFireAlsoInInternalCamera": 1,
            "gunnerUsesPilotView": 0,
            "viewGunnerShadow": 1,
            "ejectDeadGunner": 0,
            "hideWeaponsGunner": 1,
            "canHideGunner": -1,
            "outGunnerMayFire": 0,
            "inGunnerMayFire": 1,
            "showHMD": 0,
            "lockWhenDriverOut": 0,
            "lockWhenVehicleSpeed": -1,
            "gunnerCompartments": "Compartment1",
            "LODTurnedIn": -1,
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
            "gunnerRightHandAnimName": "",
            "gunnerLeftLegAnimName": "",
            "gunnerRightLegAnimName": "",
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
            }
        }
    },
    # Class: CfgVehicles\rhs_zsutank_base\Damage,
    "Damage": {
        "tex": [],
        "mat": ["rhsafrf|addons|rhs_a2port_armor|data|ZSU_01.rvmat","rhsafrf|addons|rhs_a2port_armor|data|ZSU_01_damage.rvmat","rhsafrf|addons|rhs_a2port_armor|data|ZSU_01_destruct.rvmat","rhsafrf|addons|rhs_a2port_armor|data|ZSU_02.rvmat","rhsafrf|addons|rhs_a2port_armor|data|ZSU_02_damage.rvmat","rhsafrf|addons|rhs_a2port_armor|data|ZSU_02_destruct.rvmat","rhsafrf|addons|rhs_a2port_armor|data|ZSU_03.rvmat","rhsafrf|addons|rhs_a2port_armor|data|ZSU_03_damage.rvmat","rhsafrf|addons|rhs_a2port_armor|data|ZSU_03_destruct.rvmat","rhsafrf|addons|rhs_a2port_armor|data|ZSU_track.rvmat","rhsafrf|addons|rhs_a2port_armor|data|ZSU_track_damage.rvmat","rhsafrf|addons|rhs_a2port_armor|data|ZSU_track_destruct.rvmat","a3|data_f|default.rvmat","a3|data_f|default.rvmat","a3|data_f|default_destruct.rvmat"]
    },
    # Class: CfgVehicles\rhs_zsutank_base\AnimationSources,
    "AnimationSources": {
        # Class: CfgVehicles\rhs_zsutank_base\AnimationSources\HatchC
        "HatchC": {
            "source": "door",
            "animPeriod": 2.1
        },
        # Class: CfgVehicles\rhs_zsutank_base\AnimationSources\HatchG,
        "HatchG": {
            "source": "door",
            "animPeriod": 2.1
        },
        # Class: CfgVehicles\rhs_zsutank_base\AnimationSources\HatchD,
        "HatchD": {
            "source": "door",
            "animPeriod": 2.1
        },
        # Class: CfgVehicles\rhs_zsutank_base\AnimationSources\muzzle_rot1,
        "muzzle_rot1": {
            "weapon": "RHS_weap_AZP23",
            "source": "ammorandom"
        }
    },
    # Class: CfgVehicles\rhs_zsutank_base\Reflectors,
    "Reflectors": {
        # Class: CfgVehicles\rhs_zsutank_base\Reflectors\Left
        "Left": {
            "color": [190,130,95],
            "ambient": [0.1,0.1,0.1,1],
            "position": "L svetlo",
            "direction": "konec L svetla",
            "hitpoint": "L svetlo",
            "selection": "L svetlo",
            "size": 1,
            "innerAngle": 100,
            "outerAngle": 179,
            "coneFadeCoef": 10,
            "intensity": 1,
            "useFlare": 0,
            "dayLight": 0,
            "flareSize": 1,
            # Class: CfgVehicles\rhs_zsutank_base\Reflectors\Left\Attenuation,
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardLimitStart": 30,
                "hardLimitEnd": 60
            }
        },
        # Class: CfgVehicles\rhs_zsutank_base\Reflectors\Right,
        "Right": {
            "position": "P svetlo",
            "direction": "konec P svetla",
            "hitpoint": "P svetlo",
            "selection": "P svetlo",
            "color": [190,130,95],
            "ambient": [0.1,0.1,0.1,1],
            "size": 1,
            "innerAngle": 100,
            "outerAngle": 179,
            "coneFadeCoef": 10,
            "intensity": 1,
            "useFlare": 0,
            "dayLight": 0,
            "flareSize": 1,
            # Class: CfgVehicles\rhs_zsutank_base\Reflectors\Left\Attenuation,
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
    "aggregateReflectors": [["Left","Right"]],
    # Class: CfgVehicles\rhs_zsutank_base\Exhausts,
    "Exhausts": {
        # Class: CfgVehicles\rhs_zsutank_base\Exhausts\Exhaust1
        "Exhaust1": {
            "position": "exhaust",
            "direction": "exhaust_dir",
            "effect": "ExhaustEffectTankBack"
        }
    },
    # Class: CfgVehicles\rhs_zsutank_base\Components,
    "Components": {
        # Class: CfgVehicles\rhs_zsutank_base\Components\SensorsManagerComponent
        "SensorsManagerComponent": {
            # Class: CfgVehicles\rhs_zsutank_base\Components\SensorsManagerComponent\Components
            "Components": {
                # Class: CfgVehicles\rhs_zsutank_base\Components\SensorsManagerComponent\Components\ActiveRadarSensorComponent
                "ActiveRadarSensorComponent": {
                    # Class: CfgVehicles\rhs_zsutank_base\Components\SensorsManagerComponent\Components\ActiveRadarSensorComponent\AirTarget
                    "AirTarget": {
                        "minRange": 14000,
                        "maxRange": 14000,
                        "objectDistanceLimitCoef": -1,
                        "viewDistanceLimitCoef": -1
                    },
                    # Class: CfgVehicles\rhs_zsutank_base\Components\SensorsManagerComponent\Components\ActiveRadarSensorComponent\GroundTarget,
                    "GroundTarget": {
                        "minRange": -1,
                        "maxRange": -1,
                        "objectDistanceLimitCoef": -1,
                        "viewDistanceLimitCoef": -1
                    },
                    "angleRangeHorizontal": 360,
                    "angleRangeVertical": 100,
                    "typeRecognitionDistance": 4000,
                    "groundNoiseDistanceCoef": 0.05,
                    "maxGroundNoiseDistance": 60,
                    "minSpeedThreshold": 20,
                    "maxSpeedThreshold": 90,
                    "maxFogSeeThrough": 1,
                    "aimDown": -35,
                    "minTrackableSpeed": 25,
                    "maxTrackableSpeed": 555,
                    "minTrackableATL": 50,
                    "componentType": "ActiveRadarSensorComponent",
                    "color": [0,1,1,1],
                    "allowsMarking": 1,
                    "animDirection": "",
                    "maxTrackableATL": 1e+010
                }
            }
        },
        # Class: CfgVehicles\Tank_F\Components\VehicleSystemsDisplayManagerComponentLeft,
        "VehicleSystemsDisplayManagerComponentLeft": {
            # Class: VehicleSystemsTemplateLeftDriver\Components
            "Components": {
                # Class: VehicleSystemsTemplateLeftDriver\Components\VehiclePrimaryGunnerDisplay
                "VehiclePrimaryGunnerDisplay": {
                    "componentType": "TransportFeedDisplayComponent",
                    "source": "PrimaryGunner"
                },
                # Class: VehicleSystemsTemplateLeftDriver\Components\VehicleCommanderDisplay,
                "VehicleCommanderDisplay": {
                    "componentType": "TransportFeedDisplayComponent",
                    "source": "Commander"
                },
                # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\EmptyDisplay,
                "EmptyDisplay": {
                    "componentType": "EmptyDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\MinimapDisplay,
                "MinimapDisplay": {
                    "componentType": "MinimapDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\MineDetectorDisplay,
                "MineDetectorDisplay": {
                    "componentType": "MineDetectorDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\CrewDisplay,
                "CrewDisplay": {
                    "componentType": "CrewDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\UAVDisplay,
                "UAVDisplay": {
                    "componentType": "UAVFeedDisplayComponent"
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
        # Class: CfgVehicles\Tank_F\Components\VehicleSystemsDisplayManagerComponentRight,
        "VehicleSystemsDisplayManagerComponentRight": {
            # Class: VehicleSystemsTemplateRightDriver\Components
            "Components": {
                # Class: VehicleSystemsTemplateRightDriver\Components\VehiclePrimaryGunnerDisplay
                "VehiclePrimaryGunnerDisplay": {
                    "componentType": "TransportFeedDisplayComponent",
                    "source": "PrimaryGunner"
                },
                # Class: VehicleSystemsTemplateRightDriver\Components\VehicleCommanderDisplay,
                "VehicleCommanderDisplay": {
                    "componentType": "TransportFeedDisplayComponent",
                    "source": "Commander"
                },
                # Class: DefaultVehicleSystemsDisplayManagerRight\Components\EmptyDisplay,
                "EmptyDisplay": {
                    "componentType": "EmptyDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerRight\Components\MinimapDisplay,
                "MinimapDisplay": {
                    "componentType": "MinimapDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerRight\Components\MineDetectorDisplay,
                "MineDetectorDisplay": {
                    "componentType": "MineDetectorDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerRight\Components\CrewDisplay,
                "CrewDisplay": {
                    "componentType": "CrewDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerRight\Components\UAVDisplay,
                "UAVDisplay": {
                    "componentType": "UAVFeedDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerRight\Components\SlingLoadDisplay,
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
    # Class: CfgVehicles\rhs_zsutank_base\EventHandlers,
    "EventHandlers": {
        # Class: CfgVehicles\rhs_zsutank_base\EventHandlers\RHS_EventHandlers
        "RHS_EventHandlers": {
            "init": "_this call rhs_fnc_bmp3_init",
            "getOut": "_this call rhs_fnc_hatchAbandon"
        },
        "init": "if (local (_this select 0)) then {[(_this select 0), `, [], false] call bis_fnc_initVehicle;};",
        "fired": "[_this select 0,_this select 6,'missile_move','MissileBase'] call BIS_fnc_missileLaunchPositionFix; _this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');",
        # Class: DefaultEventHandlers\RHS_DefaultEventhandlers,
        "RHS_DefaultEventhandlers": {
            "hitpart": "_this call rhs_fnc_hitPart"
        }
    },
    "attenuationEffectType": "TankAttenuation",
    "soundGetIn": ["A3|Sounds_F_EPB|Tracked|noises|get_in_out",0.562341,1],
    "soundGetOut": ["A3|Sounds_F_EPB|Tracked|noises|get_in_out",0.562341,1,20],
    "soundTurnIn": ["A3|Sounds_F|vehicles|noises|Turn_in_out",1.77828,1,20],
    "soundTurnOut": ["A3|Sounds_F|vehicles|noises|Turn_in_out",1.77828,1,20],
    "soundTurnInInternal": ["A3|Sounds_F|vehicles|noises|Turn_in_out",1.77828,1,20],
    "soundTurnOutInternal": ["A3|Sounds_F|vehicles|noises|Turn_in_out",1.77828,1,20],
    "soundDammage": ["",0.562341,1],
    "soundEngineOnInt": ["A3|Sounds_F|vehicles2|armor|MBT_03|MBT_03_Engine_Int_Start",0.501187,1],
    "soundEngineOffInt": ["A3|Sounds_F|vehicles2|armor|MBT_03|MBT_03_Engine_Int_Stop",0.707946,1],
    "soundEngineOnExt": ["A3|Sounds_F|vehicles2|armor|MBT_03|MBT_03_Engine_Ext_Start",1.99526,1,70],
    "soundEngineOffExt": ["A3|Sounds_F|vehicles2|armor|MBT_03|MBT_03_Engine_Ext_Stop",1.99526,1,70],
    "BushCrash1": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_Collision_Light_Bush_01",0.630957,1,100],
    "BushCrash2": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_Collision_Light_Bush_02",0.630957,1,100],
    "BushCrash3": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_Collision_Light_Bush_03",0.630957,1,100],
    "soundBushCrash": ["BushCrash1",0.33,"BushCrash2",0.33,"BushCrash3",0.33],
    "buildCrash0": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_01",3.16228,1,200],
    "buildCrash1": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_02",3.16228,1,200],
    "buildCrash2": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_03",3.16228,1,200],
    "buildCrash3": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_04",3.16228,1,200],
    "buildCrash4": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_05",3.16228,1,200],
    "buildCrash5": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_06",3.16228,1,200],
    "soundBuildingCrash": ["buildCrash0",0.166,"buildCrash1",0.166,"buildCrash2",0.166,"buildCrash3",0.166,"buildCrash4",0.166,"buildCrash5",0.166],
    "woodCrash0": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_01",3.16228,1,200],
    "woodCrash1": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_02",3.16228,1,200],
    "woodCrash2": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_03",3.16228,1,200],
    "woodCrash3": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_04",3.16228,1,200],
    "woodCrash4": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_05",3.16228,1,200],
    "woodCrash5": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_06",3.16228,1,200],
    "soundWoodCrash": ["woodCrash0",0.166,"woodCrash1",0.166,"woodCrash2",0.166,"woodCrash3",0.166,"woodCrash4",0.166,"woodCrash5",0.166],
    "ArmorCrash0": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_01",3.16228,1,200],
    "ArmorCrash1": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_02",3.16228,1,200],
    "ArmorCrash2": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_03",3.16228,1,200],
    "ArmorCrash3": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_04",3.16228,1,200],
    "ArmorCrash4": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_05",3.16228,1,200],
    "ArmorCrash5": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_06",3.16228,1,200],
    "soundArmorCrash": ["ArmorCrash0",0.166,"ArmorCrash1",0.166,"ArmorCrash2",0.166,"ArmorCrash3",0.166,"ArmorCrash4",0.166,"ArmorCrash5",0.166],
    # Class: CfgVehicles\APC_Tracked_02_base_F\Sounds,
    "Sounds": {
        "soundSetsInt": ["APC_Tracked_02_Engine_RPM0_INT_SoundSet","APC_Tracked_02_Engine_RPM1_INT_SoundSet","APC_Tracked_02_Engine_RPM2_INT_SoundSet","APC_Tracked_02_Engine_RPM3_INT_SoundSet","APC_Tracked_02_Engine_RPM4_INT_SoundSet","APC_Tracked_02_Tracks_01_INT_SoundSet","APC_Tracked_02_Tracks_02_INT_SoundSet","APC_Tracked_02_Tracks_03_INT_SoundSet","APC_Tracked_02_Tracks_04_INT_SoundSet","APC_Tracked_02_Tracks_05_INT_SoundSet","APC_Tracked_02_Tracks_06_INT_SoundSet","APC_Tracked_02_Interior_Tone_Engine_Off_SoundSet","APC_Tracked_02_Interior_Tone_Engine_On_SoundSet","APC_Tracked_02_Rattling_INT_SoundSet","APC_Tracked_02_Stress_INT_SoundSet","APC_Tracked_02_Rain_INT_SoundSet","APC_Tracked_02_Tracks_Brake_Hard_INT_SoundSet","APC_Tracked_02_Tracks_Brake_Soft_INT_SoundSet","APC_Tracked_02_Tracks_Turn_Hard_INT_SoundSet","APC_Tracked_02_Tracks_Turn_Soft_INT_SoundSet","APC_Tracked_02_Drive_Water_INT_SoundSet","APC_Tracked_02_Drive_Dirt_INT_SoundSet","Tracks_Movement_Dirt_Int_01_SoundSet","Tracks_Surface_Soft_Int_SoundSet","Tracks_Surface_Sand_Int_SoundSet","Tracks_Surface_Squeaks_Soft_Int_SoundSet","Tracks_Surface_Squeaks_Hard_Int_SoundSet","Tanks_Material_Strain_Int_SoundSet"],
        "soundSetsExt": ["APC_Tracked_02_Engine_RPM0_EXT_SoundSet","APC_Tracked_02_Engine_RPM1_EXT_SoundSet","APC_Tracked_02_Engine_RPM2_EXT_SoundSet","APC_Tracked_02_Engine_RPM3_EXT_SoundSet","APC_Tracked_02_Engine_RPM4_EXT_SoundSet","APC_Tracked_02_Tracks_01_EXT_SoundSet","APC_Tracked_02_Tracks_02_EXT_SoundSet","APC_Tracked_02_Tracks_03_EXT_SoundSet","APC_Tracked_02_Tracks_04_EXT_SoundSet","APC_Tracked_02_Tracks_05_EXT_SoundSet","APC_Tracked_02_Tracks_06_EXT_SoundSet","APC_Tracked_02_Rattling_EXT_SoundSet","APC_Tracked_02_Rain_EXT_SoundSet","APC_Tracked_02_Tracks_Brake_Hard_EXT_SoundSet","APC_Tracked_02_Tracks_Brake_Soft_EXT_SoundSet","APC_Tracked_02_Tracks_Turn_Hard_EXT_SoundSet","APC_Tracked_02_Tracks_Turn_Soft_EXT_SoundSet","APC_Tracked_02_Drive_Water_EXT_SoundSet","APC_Tracked_02_Drive_Dirt_EXT_SoundSet","Tracks_Movement_Dirt_Ext_01_SoundSet","Tracks_Surface_Soft_Ext_SoundSet","Tracks_Surface_Sand_Ext_SoundSet","Tracks_Surface_Squeaks_Soft_Ext_SoundSet","Tracks_Surface_Squeaks_Hard_Ext_SoundSet"]
    },
    "_generalMacro": "APC_Tracked_02_base_F",
    "maxSpeed": 87,
    "slowSpeedForwardCoef": 0.6435,
    "waterResistanceCoef": 0.25,
    "engineMOI": 7,
    "dampingRateFullThrottle": 0.8,
    "dampingRateZeroThrottleClutchEngaged": 4,
    "dampingRateZeroThrottleClutchDisengaged": 0.5,
    "switchTime": 0,
    "antiRollbarForceCoef": 20,
    "antiRollbarForceLimit": 10,
    "antiRollbarSpeedMin": 10,
    "antiRollbarSpeedMax": 55,
    # Class: CfgVehicles\APC_Tracked_02_base_F\MFD,
    "MFD": {
        # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Driver_Heading
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
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Driver_Heading\material,
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Driver_Heading\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Driver_Heading\Draw,
            "Draw": {
                "color": [0.61,0.62,0],
                "alpha": 1,
                "condition": "on",
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Driver_Heading\Draw\Driver_Heading,
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
        # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Driver_Heading_text,
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
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Driver_Heading_text\material,
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Driver_Heading_text\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Driver_Heading_text\Draw,
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Driver_Heading_text\Draw\Driver_Heading,
                "Driver_Heading": {
                    "type": "text",
                    "source": "static",
                    "text": "АЗИМУТ",
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
        # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Driver_Heading_second,
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
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Driver_Heading_second\material,
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Driver_Heading_second\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Driver_Heading_second\Draw,
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Driver_Heading_second\Draw\Driver_Heading,
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
        # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_AmmoType,
        "MFD_Gunner_AmmoType": {
            "topLeft": "MFD_5_TL",
            "topRight": "MFD_5_TR",
            "bottomLeft": "MFD_5_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "turret": [0],
            "enableParallax": 0,
            "font": "LCD14",
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_AmmoType\material,
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_AmmoType\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_AmmoType\Draw,
            "Draw": {
                "color": [0.92,0.01,0],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_AmmoType\Draw\Gunner_AmmoType,
                "Gunner_AmmoType": {
                    "type": "text",
                    "source": "ammoFormat",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.455,0.05],1],
                    "right": [[1.355,0.05],1],
                    "down": [[0.455,0.76],1]
                }
            }
        },
        # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_AmmoIndicator,
        "MFD_Gunner_AmmoIndicator": {
            "topLeft": "MFD_3_TL",
            "topRight": "MFD_3_TR",
            "bottomLeft": "MFD_3_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "enableParallax": 0,
            "turret": [0],
            "font": "LCD14",
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_AmmoIndicator\material,
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_AmmoIndicator\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_AmmoIndicator\Draw,
            "Draw": {
                "color": [0.92,0.01,0],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_AmmoIndicator\Draw\Gunner_Text_1,
                "Gunner_Text_1": {
                    "type": "text",
                    "source": "ammo",
                    "sourceScale": 1,
                    "sourceLength": 2,
                    "sourceIndex": 1000,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.5,0],1],
                    "right": [[1.3,0],1],
                    "down": [[0.5,0.3],1]
                },
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_AmmoIndicator\Draw\Gunner_Text_2,
                "Gunner_Text_2": {
                    "type": "text",
                    "source": "ammo",
                    "sourceScale": 1,
                    "sourceLength": 2,
                    "sourceIndex": 1001,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.5,0.3],1],
                    "right": [[1.3,0.3],1],
                    "down": [[0.5,0.6],1]
                },
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_AmmoIndicator\Draw\Gunner_Text_3,
                "Gunner_Text_3": {
                    "type": "text",
                    "source": "ammo",
                    "sourceScale": 1,
                    "sourceLength": 2,
                    "sourceIndex": 1002,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.5,0.6],1],
                    "right": [[1.3,0.6],1],
                    "down": [[0.5,0.9],1]
                }
            }
        },
        # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_Ready_To_Fire,
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
            "font": "RobotoCondensedLight",
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_Ready_To_Fire\material,
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_Ready_To_Fire\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_Ready_To_Fire\Draw,
            "Draw": {
                "color": [0,0,0],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_Ready_To_Fire\Draw\Top_text,
                "Top_text": {
                    "type": "text",
                    "source": "static",
                    "text": "К СТРЕЛЬБЕ",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.45,0.05],1],
                    "right": [[0.67,0.05],1],
                    "down": [[0.45,0.55],1]
                },
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_Ready_To_Fire\Draw\Bottom_text,
                "Bottom_text": {
                    "type": "text",
                    "source": "static",
                    "text": "ГОТОВ",
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
        # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_Display,
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
            "font": "RobotoCondensedLight",
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_Display\material,
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_Display\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_Display\Draw,
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_Display\Draw\Main_armament,
                "Main_armament": {
                    "type": "text",
                    "source": "static",
                    "text": "ГЛАВНОЕ ОРУДИЕ",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshRate": 0.1,
                    "pos": [[0.015,-0.005],1],
                    "right": [[0.075,-0.005],1],
                    "down": [[0.015,0.073],1]
                },
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_Display\Draw\Machinegun,
                "Machinegun": {
                    "type": "text",
                    "source": "static",
                    "text": "ПУЛЕМЕТ",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshRate": 0.1,
                    "pos": [[0.015,0.31],1],
                    "right": [[0.075,0.31],1],
                    "down": [[0.015,0.388],1]
                },
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_Display\Draw\Main_armament_ammo_type,
                "Main_armament_ammo_type": {
                    "type": "text",
                    "source": "static",
                    "text": "ТИП АМУНИЦИИ",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.55,-0.005],1],
                    "right": [[0.61,-0.005],1],
                    "down": [[0.55,0.073],1]
                },
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_Display\Draw\Lased_distance_elevation,
                "Lased_distance_elevation": {
                    "type": "text",
                    "source": "static",
                    "text": "ДАЛЬНОСТЬ",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshRate": 0.1,
                    "pos": [[0.015,0.84],1],
                    "right": [[0.075,0.84],1],
                    "down": [[0.015,0.918],1]
                },
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_Display\Draw\Azimut,
                "Azimut": {
                    "type": "text",
                    "source": "static",
                    "text": "АЗИМУТ",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshRate": 0.1,
                    "pos": [[0.015,0.915],1],
                    "right": [[0.075,0.915],1],
                    "down": [[0.015,0.993],1]
                },
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_Display\Draw\Damage,
                "Damage": {
                    "type": "text",
                    "source": "static",
                    "text": "ПОВРЕЖДЕНИЯ",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshRate": 0.1,
                    "pos": [[0.015,0.39],1],
                    "right": [[0.075,0.39],1],
                    "down": [[0.015,0.468],1]
                },
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_Display\Draw\Heading,
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
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_Display\Draw\Lased_Range,
                "Lased_Range": {
                    "type": "text",
                    "source": "laserDist",
                    "sourceScale": 1,
                    "sourceLength": 4,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.34,0.84],1],
                    "right": [[0.4,0.84],1],
                    "down": [[0.34,0.918],1]
                }
            }
        },
        # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_Main_Armament_Ammo_Type,
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
            "font": "RobotoCondensedLight",
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_Main_Armament_Ammo_Type\material,
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_Main_Armament_Ammo_Type\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_Main_Armament_Ammo_Type\Draw,
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_Main_Armament_Ammo_Type\Draw\Gunner_AmmoType,
                "Gunner_AmmoType": {
                    "type": "text",
                    "source": "ammoFormat",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.555,0.065],1],
                    "right": [[0.635,0.065],1],
                    "down": [[0.555,0.185],1]
                }
            }
        },
        # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_Coax_Ammo,
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
            "font": "RobotoCondensedLight",
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_Coax_Ammo\material,
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_Coax_Ammo\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_Coax_Ammo\Draw,
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_Coax_Ammo\Draw\Gunner_Text_1,
                "Gunner_Text_1": {
                    "type": "text",
                    "source": "ammo",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "sourceIndex": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.31,0.31],1],
                    "right": [[0.37,0.31],1],
                    "down": [[0.31,0.388],1]
                }
            }
        },
        # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_AmmoIndicator_Main_Armament,
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
            "font": "RobotoCondensedLight",
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_AmmoIndicator_Main_Armament\material,
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_AmmoIndicator_Main_Armament\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_AmmoIndicator_Main_Armament\Draw,
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_AmmoIndicator_Main_Armament\Draw\Main_Armament_Ammo_Type_1,
                "Main_Armament_Ammo_Type_1": {
                    "type": "text",
                    "source": "static",
                    "text": "БР",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshRate": 0.1,
                    "pos": [[0.015,0.065],1],
                    "right": [[0.075,0.065],1],
                    "down": [[0.015,0.143],1]
                },
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_AmmoIndicator_Main_Armament\Draw\Gunner_Text_1,
                "Gunner_Text_1": {
                    "type": "text",
                    "source": "ammo",
                    "sourceScale": 1,
                    "sourceLength": 2,
                    "sourceIndex": 0,
                    "sourcePrecision": 1,
                    "scale": 1,
                    "align": "left",
                    "refreshRate": 0.1,
                    "pos": [[0.395,0.065],1],
                    "right": [[0.455,0.065],1],
                    "down": [[0.395,0.143],1]
                },
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_AmmoIndicator_Main_Armament\Draw\Main_Armament_Ammo_Type_2,
                "Main_Armament_Ammo_Type_2": {
                    "type": "text",
                    "source": "static",
                    "text": "ОФ",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshRate": 0.1,
                    "pos": [[0.015,0.125],1],
                    "right": [[0.075,0.125],1],
                    "down": [[0.015,0.203],1]
                },
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_AmmoIndicator_Main_Armament\Draw\Gunner_Text_2,
                "Gunner_Text_2": {
                    "type": "text",
                    "source": "ammo",
                    "sourceScale": 1,
                    "sourceLength": 2,
                    "sourceIndex": 0,
                    "scale": 1,
                    "align": "left",
                    "refreshRate": 0.1,
                    "pos": [[0.395,0.125],1],
                    "right": [[0.455,0.125],1],
                    "down": [[0.395,0.203],1]
                },
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_AmmoIndicator_Main_Armament\Draw\Main_Armament_Ammo_Type_3,
                "Main_Armament_Ammo_Type_3": {
                    "type": "text",
                    "source": "static",
                    "text": "Р",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshRate": 0.1,
                    "pos": [[0.015,0.185],1],
                    "right": [[0.075,0.185],1],
                    "down": [[0.015,0.263],1]
                },
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Gunner_AmmoIndicator_Main_Armament\Draw\Gunner_Text_3,
                "Gunner_Text_3": {
                    "type": "text",
                    "source": "ammo",
                    "sourceScale": 1,
                    "sourceLength": 2,
                    "sourceIndex": 2,
                    "scale": 1,
                    "align": "left",
                    "refreshRate": 0.1,
                    "pos": [[0.395,0.185],1],
                    "right": [[0.455,0.185],1],
                    "down": [[0.395,0.263],1]
                }
            }
        },
        # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Display,
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
            "turret": [0,0],
            "font": "RobotoCondensedLight",
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Display\material,
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Display\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Display\Draw,
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Display\Draw\Main_armament,
                "Main_armament": {
                    "type": "text",
                    "source": "static",
                    "text": "ГЛАВНОЕ ОРУДИЕ",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshRate": 0.1,
                    "pos": [[0.015,-0.005],1],
                    "right": [[0.075,-0.005],1],
                    "down": [[0.015,0.145],1]
                },
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Display\Draw\Machinegun,
                "Machinegun": {
                    "type": "text",
                    "source": "static",
                    "text": "ПУЛЕМЕТ",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.51,-0.005],1],
                    "right": [[0.57,-0.005],1],
                    "down": [[0.51,0.145],1]
                },
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Display\Draw\Commander_machinegun,
                "Commander_machinegun": {
                    "type": "text",
                    "source": "static",
                    "text": "----",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.81,0.19],1],
                    "right": [[0.87,0.19],1],
                    "down": [[0.81,0.34],1]
                },
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Display\Draw\Commander_armament,
                "Commander_armament": {
                    "type": "text",
                    "source": "static",
                    "text": "ОРУДИЕ КОМАНДИРА",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.795,0.005],1],
                    "right": [[0.845,0.005],1],
                    "down": [[0.795,0.125],1]
                },
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Display\Draw\Commander_armament_magazines,
                "Commander_armament_magazines": {
                    "type": "text",
                    "source": "static",
                    "text": "МАГ.",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.47,0.4],1],
                    "right": [[0.53,0.4],1],
                    "down": [[0.47,0.55],1]
                },
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Display\Draw\Main_armament_ammo_type,
                "Main_armament_ammo_type": {
                    "type": "text",
                    "source": "static",
                    "text": "ТИП АМУНИЦИИ",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshRate": 0.1,
                    "pos": [[0.015,0.61],1],
                    "right": [[0.075,0.61],1],
                    "down": [[0.015,0.76],1]
                },
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Display\Draw\Lased_distance_elevation,
                "Lased_distance_elevation": {
                    "type": "text",
                    "source": "static",
                    "text": "ДАЛЬНОСТЬ",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.73,0.61],1],
                    "right": [[0.785,0.61],1],
                    "down": [[0.73,0.75],1]
                },
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Display\Draw\Azimut,
                "Azimut": {
                    "type": "text",
                    "source": "static",
                    "text": "АЗИМУТ",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.71,0.8],1],
                    "right": [[0.77,0.8],1],
                    "down": [[0.71,0.95],1]
                },
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Display\Draw\Damage,
                "Damage": {
                    "type": "text",
                    "source": "static",
                    "text": "ПОВРЕЖДЕНИЯ",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshRate": 0.1,
                    "pos": [[0.015,0.82],1],
                    "right": [[0.075,0.82],1],
                    "down": [[0.015,0.97],1]
                },
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Display\Draw\Heading,
                "Heading": {
                    "type": "text",
                    "source": "[x]turretworld",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 0.2,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.925,0.8],1],
                    "right": [[0.985,0.8],1],
                    "down": [[0.925,0.95],1]
                },
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Display\Draw\Lased_Range,
                "Lased_Range": {
                    "type": "text",
                    "source": "laserDist",
                    "sourceScale": 1,
                    "sourceLength": 4,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.925,0.61],1],
                    "right": [[0.985,0.61],1],
                    "down": [[0.925,0.76],1]
                }
            }
        },
        # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Ready_To_Fire,
        "MFD_Commander_Ready_To_Fire": {
            "topLeft": "mfd_com_cli_TL",
            "topRight": "mfd_com_cli_TR",
            "bottomLeft": "mfd_com_cli_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0,0,0],
            "alpha": 0.5,
            "enableParallax": 0,
            "font": "RobotoCondensedLight",
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Ready_To_Fire\material,
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Ready_To_Fire\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Ready_To_Fire\Draw,
            "Draw": {
                "color": [0,0,0],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Ready_To_Fire\Draw\Top_text,
                "Top_text": {
                    "type": "text",
                    "source": "static",
                    "text": "К СТРЕЛЬБЕ",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "center",
                    "pos": [[0.48,0.05],1],
                    "right": [[0.68,0.05],1],
                    "down": [[0.48,0.56],1]
                },
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Ready_To_Fire\Draw\Bottom_text,
                "Bottom_text": {
                    "type": "text",
                    "source": "static",
                    "text": "ГОТОВ",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "center",
                    "pos": [[0.5,0.41],1],
                    "right": [[0.7,0.41],1],
                    "down": [[0.5,0.92],1]
                }
            }
        },
        # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Smoke_Indicator,
        "MFD_Commander_Smoke_Indicator": {
            "topLeft": "mfd_com_smoke_TL",
            "topRight": "mfd_com_smoke_TR",
            "bottomLeft": "mfd_com_smoke_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0,0,0],
            "alpha": 0.5,
            "enableParallax": 0,
            "font": "RobotoCondensedLight",
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Smoke_Indicator\material,
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Smoke_Indicator\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Smoke_Indicator\Draw,
            "Draw": {
                "color": [0,0,0],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Smoke_Indicator\Draw\Top_text,
                "Top_text": {
                    "type": "text",
                    "source": "static",
                    "text": "ДЫМОВАЯ",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "center",
                    "pos": [[0.47,0],1],
                    "right": [[0.67,0],1],
                    "down": [[0.47,0.5],1]
                },
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Smoke_Indicator\Draw\Bottom_text,
                "Bottom_text": {
                    "type": "text",
                    "source": "static",
                    "text": "ЗАВЕСА",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "center",
                    "pos": [[0.5,0.4],1],
                    "right": [[0.7,0.4],1],
                    "down": [[0.5,0.9],1]
                }
            }
        },
        # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Main_Armament_Ammo_Type,
        "MFD_Commander_Main_Armament_Ammo_Type": {
            "topLeft": "mfd_com_TL",
            "topRight": "mfd_com_TR",
            "bottomLeft": "mfd_com_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "turret": [0],
            "enableParallax": 0,
            "font": "RobotoCondensedLight",
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Main_Armament_Ammo_Type\material,
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Main_Armament_Ammo_Type\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Main_Armament_Ammo_Type\Draw,
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Main_Armament_Ammo_Type\Draw\Gunner_AmmoType,
                "Gunner_AmmoType": {
                    "type": "text",
                    "source": "ammoFormat",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.36,0.61],1],
                    "right": [[0.42,0.61],1],
                    "down": [[0.36,0.76],1]
                }
            }
        },
        # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_AmmoIndicator_Main_Armament,
        "MFD_Commander_AmmoIndicator_Main_Armament": {
            "topLeft": "mfd_com_TL",
            "topRight": "mfd_com_TR",
            "bottomLeft": "mfd_com_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "enableParallax": 0,
            "turret": [0],
            "font": "RobotoCondensedLight",
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_AmmoIndicator_Main_Armament\material,
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_AmmoIndicator_Main_Armament\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_AmmoIndicator_Main_Armament\Draw,
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_AmmoIndicator_Main_Armament\Draw\Main_Armament_Ammo_Type_1,
                "Main_Armament_Ammo_Type_1": {
                    "type": "text",
                    "source": "static",
                    "text": "БР",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshRate": 0.1,
                    "pos": [[0.015,0.13],1],
                    "right": [[0.075,0.13],1],
                    "down": [[0.015,0.28],1]
                },
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_AmmoIndicator_Main_Armament\Draw\Gunner_Text_1,
                "Gunner_Text_1": {
                    "type": "text",
                    "source": "ammo",
                    "sourceScale": 1,
                    "sourceLength": 2,
                    "sourceIndex": 0,
                    "sourcePrecision": 1,
                    "scale": 1,
                    "align": "left",
                    "refreshRate": 0.1,
                    "pos": [[0.39,0.13],1],
                    "right": [[0.45,0.13],1],
                    "down": [[0.39,0.28],1]
                },
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_AmmoIndicator_Main_Armament\Draw\Main_Armament_Ammo_Type_2,
                "Main_Armament_Ammo_Type_2": {
                    "type": "text",
                    "source": "static",
                    "text": "ОФ",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshRate": 0.1,
                    "pos": [[0.015,0.23],1],
                    "right": [[0.075,0.23],1],
                    "down": [[0.015,0.38],1]
                },
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_AmmoIndicator_Main_Armament\Draw\Gunner_Text_2,
                "Gunner_Text_2": {
                    "type": "text",
                    "source": "ammo",
                    "sourceScale": 1,
                    "sourceLength": 2,
                    "sourceIndex": 0,
                    "scale": 1,
                    "align": "left",
                    "refreshRate": 0.1,
                    "pos": [[0.39,0.23],1],
                    "right": [[0.45,0.23],1],
                    "down": [[0.39,0.38],1]
                },
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_AmmoIndicator_Main_Armament\Draw\Main_Armament_Ammo_Type_3,
                "Main_Armament_Ammo_Type_3": {
                    "type": "text",
                    "source": "static",
                    "text": "Р",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshRate": 0.1,
                    "pos": [[0.015,0.33],1],
                    "right": [[0.075,0.33],1],
                    "down": [[0.015,0.48],1]
                },
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_AmmoIndicator_Main_Armament\Draw\Gunner_Text_3,
                "Gunner_Text_3": {
                    "type": "text",
                    "source": "ammo",
                    "sourceScale": 1,
                    "sourceLength": 2,
                    "sourceIndex": 2,
                    "scale": 1,
                    "align": "left",
                    "refreshRate": 0.1,
                    "pos": [[0.39,0.33],1],
                    "right": [[0.45,0.33],1],
                    "down": [[0.39,0.48],1]
                }
            }
        },
        # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Coax_Ammo,
        "MFD_Commander_Coax_Ammo": {
            "topLeft": "mfd_com_ammo_count_TL",
            "topRight": "mfd_com_ammo_count_TR",
            "bottomLeft": "mfd_com_ammo_count_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "enableParallax": 0,
            "turret": [0],
            "font": "RobotoCondensedLight",
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Coax_Ammo\material,
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Coax_Ammo\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Coax_Ammo\Draw,
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Coax_Ammo\Draw\Gunner_Text_1,
                "Gunner_Text_1": {
                    "type": "text",
                    "source": "ammo",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "sourceIndex": 1,
                    "align": "left",
                    "refreshRate": 0.1,
                    "pos": [[1.32,0.2],1],
                    "right": [[1.97,0.2],1],
                    "down": [[1.32,1],1]
                }
            }
        },
        # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Coax_Magazines,
        "MFD_Commander_Coax_Magazines": {
            "topLeft": "mfd_com_mag_count_TL",
            "topRight": "mfd_com_mag_count_TR",
            "bottomLeft": "mfd_com_mag_count_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "enableParallax": 0,
            "turret": [0],
            "font": "RobotoCondensedLight",
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Coax_Magazines\material,
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Coax_Magazines\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Coax_Magazines\Draw,
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Coax_Magazines\Draw\Gunner_Text_1,
                "Gunner_Text_1": {
                    "type": "text",
                    "source": "ammo",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "sourceIndex": 1,
                    "align": "left",
                    "refreshRate": 0.1,
                    "pos": [[0.1,0.11],1],
                    "right": [[0.85,0.11],1],
                    "down": [[0.1,0.81],1]
                }
            }
        },
        # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Second_Display,
        "MFD_Commander_Second_Display": {
            "topLeft": "MFD_7_TL",
            "topRight": "MFD_7_TR",
            "bottomLeft": "MFD_7_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [1,1,1],
            "alpha": 0.5,
            "enableParallax": 0,
            "font": "EtelkaMonospacePro",
            "turret": [0,0],
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Second_Display\material,
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Second_Display\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Second_Display\Draw,
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Second_Display\Draw\Crosshair,
                "Crosshair": {
                    "type": "line",
                    "width": 3,
                    "points": [[[0.5,0.423413],1],[[0.5,0.346429],1],[],[[0.5,0.577381],1],[[0.5,0.654365],1],[],[[0.55,0.500397],1],[[0.6,0.500397],1],[],[[0.4,0.500397],1],[[0.45,0.500397],1],[],[[0.3,0.346429],1],[[0.3,0.269444],1],[],[[0.3,0.269444],1],[[0.35,0.269444],1],[],[[0.7,0.346429],1],[[0.7,0.269444],1],[],[[0.65,0.269444],1],[[0.7,0.269444],1],[],[[0.7,0.654365],1],[[0.7,0.731349],1],[],[[0.65,0.731349],1],[[0.7,0.731349],1],[],[[0.3,0.654365],1],[[0.3,0.731349],1],[],[[0.3,0.731349],1],[[0.35,0.731349],1],[]]
                },
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Second_Display\Draw\Heading,
                "Heading": {
                    "type": "text",
                    "source": "[x]turretworld",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 0.2,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.83,0.25],1],
                    "right": [[0.88,0.25],1],
                    "down": [[0.83,0.33],1]
                },
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Second_Display\Draw\Lased_Range_Background,
                "Lased_Range_Background": {
                    "color": [0,0,0],
                    # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Second_Display\Draw\Lased_Range_Background\Background,
                    "Background": {
                        "type": "polygon",
                        "points": [[[[0.43,0.81],1],[[0.57,0.81],1],[[0.57,0.87],1],[[0.43,0.87],1]]]
                    }
                },
                # Class: CfgVehicles\APC_Tracked_02_base_F\MFD\MFD_Commander_Second_Display\Draw\Lased_Range,
                "Lased_Range": {
                    "type": "text",
                    "source": "laserDist",
                    "sourceScale": 1,
                    "sourceLength": 4,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.494,0.8],1],
                    "right": [[0.544,0.8],1],
                    "down": [[0.494,0.88],1]
                }
            }
        }
    },
    # Class: CfgVehicles\APC_Tracked_02_base_F\Library,
    "Library": {
        "libTextDesc": "The infantry fighting vehicle BTR-K Kamysh and its anti-aircraft cousin ZSU-39 Tigris share the same vehicle platform. Developed by Russia with a pinch of undeniable inspiration from Israeli IFVs, they serve in the OPFOR army as a prime example of a leveling of the technology field with the West. The Kamysh is equipped with a CTWS turret fitted with a 30 mm cannon, coaxial machinegun and 2 guided AT missiles, making the vehicle significant in the infantry support role. The Tigris is fitted with a 35 mm autocannon and 4 Titan AA missiles."
    },
    "memoryPointTaskMarker": "TaskMarker_1_pos",
    "transportSoldier": 0,
    "cargoGetInAction": ["GetInAMV_cargo"],
    "cargoGetOutAction": ["GetOutLow"],
    "cargoAction": ["passenger_apc_narrow_generic02","passenger_apc_narrow_generic03","passenger_apc_generic02","passenger_apc_generic04","passenger_apc_narrow_generic01","passenger_generic01_foldhands","passenger_generic01_leanleft","passenger_generic01_leanright"],
    "hideProxyInCombat": 1,
    "hideWeaponsDriver": 1,
    "hideWeaponsCargo": 1,
    "viewDriverShadowAmb": 0.5,
    "viewDriverShadowDiff": 0.05,
    "driverInfoPanelCameraPos": "driverview_old",
    "driverLeftHandAnimName": "drivingstick_left",
    "driverRightHandAnimName": "drivingstick_right",
    "driverLeftLegAnimName": "pedal_brake",
    "driverRightLegAnimName": "pedal_thrust",
    # Class: CfgVehicles\APC_Tracked_02_base_F\ViewPilot,
    "ViewPilot": {
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
    "armorLights": 0.1,
    "crewExplosionProtection": 0.999,
    "waterPPInVehicle": 0,
    "fireDustEffect": "emptyEffect",
    "wheelCircumference": 2.18,
    "animationSourceHatch": "",
    "insideSoundCoef": 0.9,
    "soundLocked": ["|A3|Sounds_F|weapons|Rockets|locked_1",1,1],
    "soundIncommingMissile": ["|A3|Sounds_F|vehicles|air|noises|alarm_locked_by_missile_4",0.398107,1],
    "smokeLauncherGrenadeCount": 8,
    "smokeLauncherVelocity": 14,
    "smokeLauncherOnTurret": 0,
    "smokeLauncherAngle": 120,
    "extCameraPosition": [0,2.75,-9.5],
    # Class: CfgVehicles\APC_Tracked_02_base_F\compartmentsLights,
    "compartmentsLights": {
        # Class: CfgVehicles\APC_Tracked_02_base_F\compartmentsLights\Comp1
        "Comp1": {
            # Class: CfgVehicles\APC_Tracked_02_base_F\compartmentsLights\Comp1\Light1
            "Light1": {
                "color": [10,15,17],
                "ambient": [0,0,0],
                "intensity": 1,
                "size": 0,
                "useFlare": 0,
                "flareSize": 0,
                "flareMaxDistance": 0,
                "dayLight": 0,
                "blinking": 0,
                # Class: CfgVehicles\APC_Tracked_02_base_F\compartmentsLights\Comp1\Light1\Attenuation,
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
            # Class: CfgVehicles\APC_Tracked_02_base_F\compartmentsLights\Comp1\Light2,
            "Light2": {
                "point": "light_interior2",
                "color": [10,15,17],
                "ambient": [0,0,0],
                "intensity": 0.3,
                "size": 0,
                "useFlare": 0,
                "flareSize": 0,
                "flareMaxDistance": 0,
                "dayLight": 0,
                "blinking": 0,
                # Class: CfgVehicles\APC_Tracked_02_base_F\compartmentsLights\Comp1\Light1\Attenuation,
                "Attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardLimitStart": 0.15,
                    "hardLimitEnd": 1.15
                }
            },
            # Class: CfgVehicles\APC_Tracked_02_base_F\compartmentsLights\Comp1\Light3,
            "Light3": {
                "point": "light_interior3",
                "color": [10,15,17],
                "ambient": [0,0,0],
                "intensity": 0.4,
                "size": 0,
                "useFlare": 0,
                "flareSize": 0,
                "flareMaxDistance": 0,
                "dayLight": 0,
                "blinking": 0,
                # Class: CfgVehicles\APC_Tracked_02_base_F\compartmentsLights\Comp1\Light1\Attenuation,
                "Attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardLimitStart": 0.15,
                    "hardLimitEnd": 1.15
                }
            },
            # Class: CfgVehicles\APC_Tracked_02_base_F\compartmentsLights\Comp1\Light4,
            "Light4": {
                "point": "light_interior4",
                "color": [10,15,17],
                "ambient": [0,0,0],
                "intensity": 0.5,
                "size": 0,
                "useFlare": 0,
                "flareSize": 0,
                "flareMaxDistance": 0,
                "dayLight": 0,
                "blinking": 0,
                # Class: CfgVehicles\APC_Tracked_02_base_F\compartmentsLights\Comp1\Light1\Attenuation,
                "Attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardLimitStart": 0.15,
                    "hardLimitEnd": 1.15
                }
            },
            # Class: CfgVehicles\APC_Tracked_02_base_F\compartmentsLights\Comp1\Light5,
            "Light5": {
                "point": "light_interior5",
                "color": [10,15,17],
                "ambient": [0,0,0],
                "intensity": 0.3,
                "size": 0,
                "useFlare": 0,
                "flareSize": 0,
                "flareMaxDistance": 0,
                "dayLight": 0,
                "blinking": 0,
                # Class: CfgVehicles\APC_Tracked_02_base_F\compartmentsLights\Comp1\Light1\Attenuation,
                "Attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardLimitStart": 0.15,
                    "hardLimitEnd": 1.15
                }
            },
            # Class: CfgVehicles\APC_Tracked_02_base_F\compartmentsLights\Comp1\Light6,
            "Light6": {
                "point": "light_interior6",
                "color": [12,12,12],
                "ambient": [0,0,0],
                "intensity": 3,
                "size": 0,
                "useFlare": 0,
                "flareSize": 0,
                "flareMaxDistance": 0,
                "dayLight": 0,
                "blinking": 0,
                # Class: CfgVehicles\APC_Tracked_02_base_F\compartmentsLights\Comp1\Light1\Attenuation,
                "Attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardLimitStart": 0.15,
                    "hardLimitEnd": 1.15
                }
            },
            # Class: CfgVehicles\APC_Tracked_02_base_F\compartmentsLights\Comp1\Light7,
            "Light7": {
                "point": "light_interior7",
                "color": [12,12,12],
                "ambient": [0,0,0],
                "intensity": 3,
                "size": 0,
                "useFlare": 0,
                "flareSize": 0,
                "flareMaxDistance": 0,
                "dayLight": 0,
                "blinking": 0,
                # Class: CfgVehicles\APC_Tracked_02_base_F\compartmentsLights\Comp1\Light1\Attenuation,
                "Attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardLimitStart": 0.15,
                    "hardLimitEnd": 1.15
                }
            },
            # Class: CfgVehicles\APC_Tracked_02_base_F\compartmentsLights\Comp1\Light8,
            "Light8": {
                "point": "light_interior8",
                "color": [12,12,12],
                "ambient": [0,0,0],
                "intensity": 3,
                "size": 0,
                "useFlare": 0,
                "flareSize": 0,
                "flareMaxDistance": 0,
                "dayLight": 0,
                "blinking": 0,
                # Class: CfgVehicles\APC_Tracked_02_base_F\compartmentsLights\Comp1\Light1\Attenuation,
                "Attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardLimitStart": 0.15,
                    "hardLimitEnd": 1.15
                }
            },
            # Class: CfgVehicles\APC_Tracked_02_base_F\compartmentsLights\Comp1\Light9,
            "Light9": {
                "point": "light_interior9",
                "color": [12,12,12],
                "ambient": [0,0,0],
                "intensity": 3,
                "size": 0,
                "useFlare": 0,
                "flareSize": 0,
                "flareMaxDistance": 0,
                "dayLight": 0,
                "blinking": 0,
                # Class: CfgVehicles\APC_Tracked_02_base_F\compartmentsLights\Comp1\Light1\Attenuation,
                "Attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardLimitStart": 0.15,
                    "hardLimitEnd": 1.15
                }
            },
            # Class: CfgVehicles\APC_Tracked_02_base_F\compartmentsLights\Comp1\Light10,
            "Light10": {
                "point": "light_interior10",
                "color": [20,20,20],
                "ambient": [0,0,0],
                "intensity": 5,
                "size": 0,
                "useFlare": 0,
                "flareSize": 0,
                "flareMaxDistance": 0,
                "dayLight": 0,
                "blinking": 0,
                # Class: CfgVehicles\APC_Tracked_02_base_F\compartmentsLights\Comp1\Light1\Attenuation,
                "Attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardLimitStart": 0.15,
                    "hardLimitEnd": 1.15
                }
            },
            # Class: CfgVehicles\APC_Tracked_02_base_F\compartmentsLights\Comp1\Light11,
            "Light11": {
                "point": "light_interior11",
                "color": [20,20,20],
                "ambient": [0,0,0],
                "intensity": 5,
                "size": 0,
                "useFlare": 0,
                "flareSize": 0,
                "flareMaxDistance": 0,
                "dayLight": 0,
                "blinking": 0,
                # Class: CfgVehicles\APC_Tracked_02_base_F\compartmentsLights\Comp1\Light1\Attenuation,
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
    "occludeSoundsWhenIn": 0,
    "obstructSoundsWhenIn": 0,
    "driverCanSee": "1 + 2 + 4 + 8 + 32",
    "sensorPosition": "gunnerView",
    "audible": 18,
    "sensitivityEar": "0.0075 /3",
    "turnCoef": 5,
    "steerAheadSimul": 0.3,
    "steerAheadPlan": 0.4,
    "brakeDistance": 5,
    "precision": 10,
    "irScanRangeMin": 0,
    "irScanToEyeFactor": 1,
    "enableRadio": 1,
    "LockDetectionSystem": 0,
    "countermeasureActivationRadius": 2000,
    "memoryPointCargoLight": "cargo light",
    "dampersBumpCoef": 4.5,
    "explosionShielding": 1,
    "minTotalDamageThreshold": 0.005,
    "crewCrashProtection": 0.25,
    "secondaryExplosion": -1,
    "fuelExplosionPower": 1,
    "weapons": [],
    "magazines": [],
    "transportMaxWeapons": 12,
    "transportMaxMagazines": 128,
    "transportMaxBackpacks": 12,
    "maximumLoad": 3000,
    "supplyRadius": -1,
    "memoryPointSupply": "doplnovani",
    # Class: CfgVehicles\Tank_F\TransportBackpacks,
    "TransportBackpacks": {
    },
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
    # Class: CfgVehicles\Tank\CargoLight,
    "CargoLight": {
        "color": [0,0,0,0],
        "ambient": [0.6,0,0.15,1],
        "brightness": 0.007
    },
    "enableGPS": 1,
    # Class: CfgVehicles\Tank\SpeechVariants,
    "SpeechVariants": {
        # Class: CfgVehicles\Tank\SpeechVariants\Default
        "Default": {
            "speechSingular": ["veh_vehicle_tank_s"],
            "speechPlural": ["veh_vehicle_tank_p"]
        }
    },
    "textSingular": "tank",
    "textPlural": "tanks",
    "nameSound": "veh_vehicle_tank_s",
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
    "headGforceLeaningFactor": [0.0075,0.005,0.0075],
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
    "weaponsGroup1": 1,
    "weaponsGroup2": "2 + 		4",
    "weaponsGroup3": "8 + 	16 + 	32",
    "weaponsGroup4": "64 + 		128",
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
    "cargoProxyIndexes": [],
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
    "dustFrontLeftPos": "dustFrontLeft",
    "dustFrontRightPos": "dustFrontRight",
    "dustBackLeftPos": "dustBackLeft",
    "dustBackRightPos": "dustBackRight",
    "waterLinearDampingCoefX": 0,
    "waterLinearDampingCoefY": 0,
    "waterAngularDampingCoef": 0,
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
    "cargoIsCoDriver": [0],
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
    "features": "",
    "insideDetectCoef": 0.05,
}