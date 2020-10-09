rhsusf_m113_usarmy = {
    "editorPreview": "rhsusf|addons|rhsusf_editorPreviews|data|rhsusf_m113_usarmy.paa",
    "faction": "rhs_faction_usarmy_wd",
    "vehicleClass": "rhs_vehclass_apc",
    "crew": "rhsusf_army_ucp_crewman",
    "author": "Red Hammer Studios",
    "scope": 2,
    "displayName": "M113A3 (M2)",
    "model": "rhsusf|addons|rhsusf_m113|m113a3_M2",
    "picture": "rhsusf|addons|rhsusf_m113|UI|M113A3_M2_ca",
    "Icon": "rhsusf|addons|rhsusf_m113|data|icom113_ca",
    "dlc": "RHS_USAF",
    "category": "Armored",
    "destrType": "DestructDefault",
    "insideSoundCoef": 0.8,
    # Class: CfgVehicles|rhsusf_m113tank_base|SpeechVariants [Indent level: 1],
    "SpeechVariants": {
        # Class: CfgVehicles|rhsusf_m113tank_base|SpeechVariants|Default [Indent level: 2]
        "Default": {
            "speechSingular": ["veh_vehicle_APC_s"],
            "speechPlural": ["veh_vehicle_APC_p"]
        }
    },
    "textSingular": "APC",
    "textPlural": "APCs",
    "nameSound": "veh_vehicle_APC_s",
    "accuracy": 0.3,
    # Class: CfgVehicles|rhsusf_m113tank_base|RenderTargets [Indent level: 1],
    "RenderTargets": {
    },
    "typicalCargo": [],
    "side": 1,
    "hasGunner": 1,
    "hasCommander": 0,
    "HeadAimDown": 19,
    "incomingMissileDetectionSystem": 0,
    "mapSize": 4.8,
    "slingLoadCargoMemoryPoints": ["SlingLoadCargo1","SlingLoadCargo2","SlingLoadCargo3","SlingLoadCargo4"],
    "driverDoor": "hatchD",
    "getInAction": "GetInLow",
    "getOutAction": "GetOutLow",
    "driverAction": "RHS_M113_DriverOut",
    "driverInAction": "RHS_M113_Driver",
    "driverLeftHandAnimName": "driverstick_left",
    "driverRightHandAnimName": "driverstick_right",
    "cargoProxyIndexes": [1,2,4,5,6,8,9,10,11],
    "getInProxyOrder": [1,2,3,4,5,6,7,8,9,10,11],
    "cargoDoors": ["ramp"],
    "cargoGetInAction": ["GetInLow"],
    "cargoGetOutAction": ["GetOutLow"],
    "cargoAction": ["RHS_M113_Cargo01","RHS_M113_Cargo03","RHS_M113_Cargo02","RHS_M113_Cargo02","RHS_M113_Cargo02","RHS_M113_Cargo02","RHS_M113_Cargo03","RHS_M113_Cargo01","RHS_M113_Cargo03","RHS_M113_Cargo03","RHS_M113_Cargo01"],
    "memoryPointsGetInCargo": ["pos cargo","pos cargo 1","pos cargo 2","pos cargo 3"],
    "memoryPointsGetInCargoDir": ["pos cargo dir","pos cargo 1 dir","pos cargo dir","pos cargo 2 dir","pos cargo 3 dir"],
    "weapons": ["rhs_weap_smokegen"],
    "magazines": ["rhs_mag_smokegen"],
    "simulation": "tankX",
    "normalSpeedForwardCoef": 0.82,
    "slowSpeedForwardCoef": 0.65,
    "maxSpeed": 72,
    "fuelCapacity": 24,
    "RHS_fuelCapacity": 360,
    "tankTurnForce": 400000,
    "tankTurnForceAngMinSpd": 0.5,
    "tankTurnForceAngSpd": 0.72,
    "accelAidForceCoef": 4,
    "accelAidForceYOffset": -3.3,
    "accelAidForceSpd": 3.23,
    "canFloat": 1,
    "waterLeakiness": 250,
    "maxFordingDepth": 0.1,
    "waterResistance": 1,
    "waterDamageEngine": 0.9,
    "engineShiftY": 0.6,
    "waterLinearDampingCoefY": 2,
    "waterLinearDampingCoefX": 2,
    "waterAngularDampingCoef": 1.2,
    "waterResistanceCoef": 0.475,
    "waterEffectSpeed": 5,
    "engineEffectSpeed": 5,
    "waterFastEffectSpeed": 28,
    "torqueCurve": [[0.22,0.584416],[0.4,0.646753],[0.5,0.824675],[0.6,0.968831],[0.72,1],[0.8,0.964935],[0.9,0.924675],[1.1056,0]],
    "engineMOI": 10,
    "enginePower": 205,
    "peakTorque": 770,
    "minOmega": 60,
    "maxOmega": 261.8,
    "idleRPM": 550,
    "redRPM": 2500,
    "thrustDelay": 0.3,
    "dampingRateFullThrottle": 0.3,
    "dampingRateZeroThrottleClutchEngaged": 3,
    "dampingRateZeroThrottleClutchDisengaged": 0.25,
    "engineLosses": 25,
    "transmissionLosses": 15,
    "clutchStrength": 15,
    "switchTime": 0.1,
    "latency": 0.1,
    "changeGearType": "rpmratio",
    "changeGearOmegaRatios": [1,0.4,0.4,0,0.84,0.56,0.94,0.56,0.96,0.56,1,0.6],
    # Class: CfgVehicles|rhsusf_m113tank_base|complexGearbox [Indent level: 1],
    "complexGearbox": {
        "GearboxRatios": ["R1",-6.62,"N",0,"D1",4.16,"D2",2.14,"D3",1.46,"D4",1.02],
        "TransmissionRatios": ["High",12.3],
        "AmphibiousRatios": ["R1",-10,"N",0,"D1",10],
        "gearBoxMode": "auto",
        "moveOffGear": 1,
        "driveString": "D",
        "neutralString": "N",
        "reverseString": "R",
        "transmissionDelay": 0.6
    },
    # Class: CfgVehicles|rhsusf_m113tank_base|Wheels [Indent level: 1],
    "Wheels": {
        # Class: CfgVehicles|rhsusf_m113tank_base|Wheels|L2 [Indent level: 2]
        "L2": {
            "suspTravelDirection": [-0.125,-1,0],
            "boneName": "wheel_podkoloL1",
            "center": "wheel_1_2_axis",
            "boundary": "wheel_1_2_bound",
            "side": "left",
            "width": 0.36,
            "steering": 0,
            "mass": 100,
            "MOI": 7.22,
            "maxBrakeTorque": 3000,
            "maxDroop": 0.15,
            "maxCompression": 0.15,
            "sprungMass": 1250,
            "springStrength": 163500,
            "springDamperRate": 7458,
            "dampingRate": 700,
            "dampingRateInAir": 700,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 30,
            "longitudinalStiffnessPerUnitGravity": 25000,
            "frictionVsSlipGraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhsusf_m113tank_base|Wheels|L3 [Indent level: 2],
        "L3": {
            "boneName": "wheel_podkolol2",
            "center": "wheel_1_3_axis",
            "boundary": "wheel_1_3_bound",
            "suspTravelDirection": [-0.125,-1,0],
            "side": "left",
            "width": 0.36,
            "steering": 0,
            "mass": 100,
            "MOI": 7.22,
            "maxBrakeTorque": 3000,
            "maxDroop": 0.15,
            "maxCompression": 0.15,
            "sprungMass": 1250,
            "springStrength": 163500,
            "springDamperRate": 7458,
            "dampingRate": 700,
            "dampingRateInAir": 700,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 30,
            "longitudinalStiffnessPerUnitGravity": 25000,
            "frictionVsSlipGraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhsusf_m113tank_base|Wheels|L4 [Indent level: 2],
        "L4": {
            "boneName": "wheel_podkolol3",
            "center": "wheel_1_4_axis",
            "boundary": "wheel_1_4_bound",
            "suspTravelDirection": [-0.125,-1,0],
            "side": "left",
            "width": 0.36,
            "steering": 0,
            "mass": 100,
            "MOI": 7.22,
            "maxBrakeTorque": 3000,
            "maxDroop": 0.15,
            "maxCompression": 0.15,
            "sprungMass": 1250,
            "springStrength": 163500,
            "springDamperRate": 7458,
            "dampingRate": 700,
            "dampingRateInAir": 700,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 30,
            "longitudinalStiffnessPerUnitGravity": 25000,
            "frictionVsSlipGraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhsusf_m113tank_base|Wheels|L5 [Indent level: 2],
        "L5": {
            "boneName": "wheel_podkolol4",
            "center": "wheel_1_5_axis",
            "boundary": "wheel_1_5_bound",
            "suspTravelDirection": [-0.125,-1,0],
            "side": "left",
            "width": 0.36,
            "steering": 0,
            "mass": 100,
            "MOI": 7.22,
            "maxBrakeTorque": 3000,
            "maxDroop": 0.15,
            "maxCompression": 0.15,
            "sprungMass": 1250,
            "springStrength": 163500,
            "springDamperRate": 7458,
            "dampingRate": 700,
            "dampingRateInAir": 700,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 30,
            "longitudinalStiffnessPerUnitGravity": 25000,
            "frictionVsSlipGraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhsusf_m113tank_base|Wheels|L6 [Indent level: 2],
        "L6": {
            "boneName": "wheel_podkolol5",
            "center": "wheel_1_6_axis",
            "boundary": "wheel_1_6_bound",
            "suspTravelDirection": [-0.125,-1,0],
            "side": "left",
            "width": 0.36,
            "steering": 0,
            "mass": 100,
            "MOI": 7.22,
            "maxBrakeTorque": 3000,
            "maxDroop": 0.15,
            "maxCompression": 0.15,
            "sprungMass": 1250,
            "springStrength": 163500,
            "springDamperRate": 7458,
            "dampingRate": 700,
            "dampingRateInAir": 700,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 30,
            "longitudinalStiffnessPerUnitGravity": 25000,
            "frictionVsSlipGraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhsusf_m113tank_base|Wheels|L9 [Indent level: 2],
        "L9": {
            "boneName": "wheel_podkolol9",
            "center": "wheel_1_9_axis",
            "boundary": "wheel_1_9_bound",
            "maxDroop": 0,
            "maxCompression": 0,
            "suspTravelDirection": [-0.125,-1,0],
            "side": "left",
            "width": 0.36,
            "steering": 0,
            "mass": 100,
            "MOI": 7.22,
            "maxBrakeTorque": 3000,
            "sprungMass": 1250,
            "springStrength": 163500,
            "springDamperRate": 7458,
            "dampingRate": 700,
            "dampingRateInAir": 700,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 30,
            "longitudinalStiffnessPerUnitGravity": 25000,
            "frictionVsSlipGraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhsusf_m113tank_base|Wheels|L1 [Indent level: 2],
        "L1": {
            "boneName": "",
            "center": "wheel_1_1_axis",
            "boundary": "wheel_1_1_bound",
            "maxDroop": 0,
            "maxCompression": 0,
            "suspTravelDirection": [-0.125,-1,0],
            "side": "left",
            "width": 0.36,
            "steering": 0,
            "mass": 100,
            "MOI": 7.22,
            "maxBrakeTorque": 3000,
            "sprungMass": 1250,
            "springStrength": 163500,
            "springDamperRate": 7458,
            "dampingRate": 700,
            "dampingRateInAir": 700,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 30,
            "longitudinalStiffnessPerUnitGravity": 25000,
            "frictionVsSlipGraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhsusf_m113tank_base|Wheels|R2 [Indent level: 2],
        "R2": {
            "suspTravelDirection": [0.125,-1,0],
            "boneName": "wheel_podkolop1",
            "center": "wheel_2_2_axis",
            "boundary": "wheel_2_2_bound",
            "side": "right",
            "width": 0.36,
            "steering": 0,
            "mass": 100,
            "MOI": 7.22,
            "maxBrakeTorque": 3000,
            "maxDroop": 0.15,
            "maxCompression": 0.15,
            "sprungMass": 1250,
            "springStrength": 163500,
            "springDamperRate": 7458,
            "dampingRate": 700,
            "dampingRateInAir": 700,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 30,
            "longitudinalStiffnessPerUnitGravity": 25000,
            "frictionVsSlipGraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhsusf_m113tank_base|Wheels|R3 [Indent level: 2],
        "R3": {
            "boneName": "wheel_podkolop2",
            "center": "wheel_2_3_axis",
            "boundary": "wheel_2_3_bound",
            "suspTravelDirection": [0.125,-1,0],
            "side": "right",
            "width": 0.36,
            "steering": 0,
            "mass": 100,
            "MOI": 7.22,
            "maxBrakeTorque": 3000,
            "maxDroop": 0.15,
            "maxCompression": 0.15,
            "sprungMass": 1250,
            "springStrength": 163500,
            "springDamperRate": 7458,
            "dampingRate": 700,
            "dampingRateInAir": 700,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 30,
            "longitudinalStiffnessPerUnitGravity": 25000,
            "frictionVsSlipGraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhsusf_m113tank_base|Wheels|R4 [Indent level: 2],
        "R4": {
            "boneName": "wheel_podkolop3",
            "center": "wheel_2_4_axis",
            "boundary": "wheel_2_4_bound",
            "suspTravelDirection": [0.125,-1,0],
            "side": "right",
            "width": 0.36,
            "steering": 0,
            "mass": 100,
            "MOI": 7.22,
            "maxBrakeTorque": 3000,
            "maxDroop": 0.15,
            "maxCompression": 0.15,
            "sprungMass": 1250,
            "springStrength": 163500,
            "springDamperRate": 7458,
            "dampingRate": 700,
            "dampingRateInAir": 700,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 30,
            "longitudinalStiffnessPerUnitGravity": 25000,
            "frictionVsSlipGraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhsusf_m113tank_base|Wheels|R5 [Indent level: 2],
        "R5": {
            "boneName": "wheel_podkolop4",
            "center": "wheel_2_5_axis",
            "boundary": "wheel_2_5_bound",
            "suspTravelDirection": [0.125,-1,0],
            "side": "right",
            "width": 0.36,
            "steering": 0,
            "mass": 100,
            "MOI": 7.22,
            "maxBrakeTorque": 3000,
            "maxDroop": 0.15,
            "maxCompression": 0.15,
            "sprungMass": 1250,
            "springStrength": 163500,
            "springDamperRate": 7458,
            "dampingRate": 700,
            "dampingRateInAir": 700,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 30,
            "longitudinalStiffnessPerUnitGravity": 25000,
            "frictionVsSlipGraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhsusf_m113tank_base|Wheels|R6 [Indent level: 2],
        "R6": {
            "boneName": "wheel_podkolop5",
            "center": "wheel_2_6_axis",
            "boundary": "wheel_2_6_bound",
            "suspTravelDirection": [0.125,-1,0],
            "side": "right",
            "width": 0.36,
            "steering": 0,
            "mass": 100,
            "MOI": 7.22,
            "maxBrakeTorque": 3000,
            "maxDroop": 0.15,
            "maxCompression": 0.15,
            "sprungMass": 1250,
            "springStrength": 163500,
            "springDamperRate": 7458,
            "dampingRate": 700,
            "dampingRateInAir": 700,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 30,
            "longitudinalStiffnessPerUnitGravity": 25000,
            "frictionVsSlipGraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhsusf_m113tank_base|Wheels|R9 [Indent level: 2],
        "R9": {
            "boneName": "wheel_podkolop9",
            "center": "wheel_2_9_axis",
            "boundary": "wheel_2_9_bound",
            "maxDroop": 0,
            "maxCompression": 0,
            "suspTravelDirection": [0.125,-1,0],
            "side": "right",
            "width": 0.36,
            "steering": 0,
            "mass": 100,
            "MOI": 7.22,
            "maxBrakeTorque": 3000,
            "sprungMass": 1250,
            "springStrength": 163500,
            "springDamperRate": 7458,
            "dampingRate": 700,
            "dampingRateInAir": 700,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 30,
            "longitudinalStiffnessPerUnitGravity": 25000,
            "frictionVsSlipGraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhsusf_m113tank_base|Wheels|R1 [Indent level: 2],
        "R1": {
            "boneName": "",
            "center": "wheel_2_1_axis",
            "boundary": "wheel_2_1_bound",
            "maxDroop": 0,
            "maxCompression": 0,
            "suspTravelDirection": [0.125,-1,0],
            "side": "right",
            "width": 0.36,
            "steering": 0,
            "mass": 100,
            "MOI": 7.22,
            "maxBrakeTorque": 3000,
            "sprungMass": 1250,
            "springStrength": 163500,
            "springDamperRate": 7458,
            "dampingRate": 700,
            "dampingRateInAir": 700,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 30,
            "longitudinalStiffnessPerUnitGravity": 25000,
            "frictionVsSlipGraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        }
    },
    "tracksSpeed": 1.35,
    "wheelCircumference": 2.375,
    "attenuationEffectType": "TankAttenuation",
    "extCameraPosition": [0,2,-11],
    "forceHideDriver": 0,
    "viewDriverInExternal": 1,
    "driverOpticsModel": "rhsusf|addons|rhsusf_optics|data|rhs_periscope_BISType",
    "DriverForceOptics": 0,
    "cost": 1.5e+006,
    "damageResistance": 0.004,
    "crewVulnerable": 1,
    "hideproxyincombat": 1,
    "transportSoldier": 9,
    "LODDriverTurnedIn": 1100,
    "LODDriverTurnedOut": 0,
    "showNVGGunner": 1,
    "headGforceLeaningFactor": [0.015,0.011,0.015],
    # Class: CfgVehicles|rhsusf_m113tank_base|Exhausts [Indent level: 1],
    "Exhausts": {
        # Class: CfgVehicles|rhsusf_m113tank_base|Exhausts|Exhaust1 [Indent level: 2]
        "Exhaust1": {
            "position": "vyfuk start",
            "direction": "vyfuk konec",
            "effect": "ExhaustsEffectBig"
        }
    },
    "armor": 200,
    "armorStructural": 350,
    "explosionShielding": 70,
    "minTotalDamageTreshold": 0.4,
    # Class: CfgVehicles|rhsusf_m113tank_base|HitPoints [Indent level: 1],
    "HitPoints": {
        # Class: CfgVehicles|rhsusf_m113tank_base|HitPoints|HitHull [Indent level: 2]
        "HitHull": {
            "armor": 5.9,
            "material": -1,
            "name": "telo",
            "visual": "zbytek",
            "passThrough": 0,
            "minimalHit": 0.14,
            "explosionShielding": 0.005,
            "radius": 0.01,
            "armorComponent": "hit_hull"
        },
        # Class: CfgVehicles|rhsusf_m113tank_base|HitPoints|HitEngine [Indent level: 2],
        "HitEngine": {
            "armor": 0.45,
            "material": -1,
            "name": "motor",
            "visual": "zbytek",
            "passThrough": 0,
            "minimalHit": 0.039,
            "explosionShielding": 0.009,
            "radius": 0.27,
            # Class: CfgVehicles|rhsusf_m113tank_base|HitPoints|HitEngine|DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles|rhsusf_m113tank_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Smoke [Indent level: 4],
                "RHS_Engine_Smoke": {
                    "simulation": "particles",
                    "type": "SmallWreckSmoke",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles|rhsusf_m113tank_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Fire [Indent level: 4],
                "RHS_Engine_Fire": {
                    "type": "SmallFireFPlace",
                    "simulation": "particles",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles|rhsusf_m113tank_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Sparks [Indent level: 4],
                "RHS_Engine_Sparks": {
                    "type": "RHS_FireSparks",
                    "simulation": "particles",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles|rhsusf_m113tank_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Sounds [Indent level: 4],
                "RHS_Engine_Sounds": {
                    "simulation": "sound",
                    "type": "Fire",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles|rhsusf_m113tank_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Smoke_small1 [Indent level: 4],
                "RHS_Engine_Smoke_small1": {
                    "type": "WeaponWreckSmoke",
                    "position": "engine_smoke2",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles|rhsusf_m113tank_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Smoke_small2 [Indent level: 4],
                "RHS_Engine_Smoke_small2": {
                    "position": "engine_smoke3",
                    "type": "WeaponWreckSmoke",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                }
            },
            "armorComponent": "hit_engine"
        },
        # Class: CfgVehicles|rhsusf_m113tank_base|HitPoints|HitLTrack [Indent level: 2],
        "HitLTrack": {
            "armor": -150,
            "material": -1,
            "name": "pas_L",
            "passThrough": 0,
            "minimalHit": -0.25,
            "explosionShielding": 0.5,
            "radius": 0.3,
            "armorComponent": "hit_trackL",
            "visual": "pas_L"
        },
        # Class: CfgVehicles|rhsusf_m113tank_base|HitPoints|HitRTrack [Indent level: 2],
        "HitRTrack": {
            "armor": -150,
            "material": -1,
            "name": "pas_P",
            "passThrough": 0,
            "minimalHit": -0.25,
            "explosionShielding": 0.5,
            "radius": 0.3,
            "armorComponent": "hit_trackR",
            "visual": "pas_P"
        },
        # Class: CfgVehicles|rhsusf_m113tank_base|HitPoints|HitFuel [Indent level: 2],
        "HitFuel": {
            "armor": 0.25,
            "material": -1,
            "name": "palivo",
            "visual": "",
            "passThrough": 0.5,
            "explosionShielding": 0.5,
            "minimalHit": 0.7,
            "radius": 0.3
        },
        # Class: CfgVehicles|APC_Tracked_02_base_F|HitPoints|HitSLAT_Left_1 [Indent level: 2],
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
        # Class: CfgVehicles|APC_Tracked_02_base_F|HitPoints|HitSLAT_Left_2 [Indent level: 2],
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
        # Class: CfgVehicles|APC_Tracked_02_base_F|HitPoints|HitSLAT_Left_3 [Indent level: 2],
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
        # Class: CfgVehicles|APC_Tracked_02_base_F|HitPoints|HitSLAT_Right_1 [Indent level: 2],
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
        # Class: CfgVehicles|APC_Tracked_02_base_F|HitPoints|HitSLAT_Right_2 [Indent level: 2],
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
        # Class: CfgVehicles|APC_Tracked_02_base_F|HitPoints|HitSLAT_Right_3 [Indent level: 2],
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
        # Class: CfgVehicles|APC_Tracked_02_base_F|HitPoints|HitSLAT_back [Indent level: 2],
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
        # Class: CfgVehicles|APC_Tracked_02_base_F|HitPoints|HitSLAT_front [Indent level: 2],
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
    # Class: CfgVehicles|rhsusf_m113tank_base|Turrets [Indent level: 1],
    "Turrets": {
        # Class: CfgVehicles|rhsusf_m113tank_base|Turrets|MainTurret [Indent level: 2]
        "MainTurret": {
            # Class: CfgVehicles|rhsusf_m113tank_base|Turrets|MainTurret|Turrets [Indent level: 3]
            "Turrets": {
            },
            "gunnerDoor": "ramp",
            "animationsourcehatch": "",
            "body": "mainTurret",
            "gun": "mainGun",
            "gunBeg": "usti hlavne",
            "gunEnd": "konec hlavne",
            "memoryPointGun": ["usti hlavne"],
            "gunnerName": "Commander",
            "weapons": ["RHS_M2","rhsusf_weap_M259"],
            "magazines": ["rhs_mag_100rnd_127x99_mag_Tracer_Red","rhs_mag_100rnd_127x99_mag_Tracer_Red","rhs_mag_100rnd_127x99_mag_Tracer_Red","rhs_mag_100rnd_127x99_mag_Tracer_Red","rhs_mag_100rnd_127x99_mag_Tracer_Red","rhs_mag_100rnd_127x99_mag_Tracer_Red","rhs_mag_100rnd_127x99_mag_Tracer_Red","rhs_mag_100rnd_127x99_mag_Tracer_Red","rhs_mag_100rnd_127x99_mag_Tracer_Red","rhs_mag_100rnd_127x99_mag_Tracer_Red","rhs_mag_100rnd_127x99_mag_Tracer_Red","rhs_mag_100rnd_127x99_mag_Tracer_Red","rhs_mag_100rnd_127x99_mag_Tracer_Red","rhs_mag_100rnd_127x99_mag_Tracer_Red","rhs_mag_100rnd_127x99_mag_Tracer_Red","rhsusf_mag_L8A3_8","rhsusf_mag_L8A3_8","rhsusf_mag_L8A3_8"],
            "canUseScanners": 0,
            "allowTabLock": 0,
            "soundServo": ["A3|sounds_f|dummysound",0.01,1,10],
            "isPersonTurret": 0,
            "usePip": 0,
            "commanding": 2,
            "minElev": -10,
            "initElev": 0,
            "maxElev": 60,
            "gunnerAction": "RHS_M113_Gunner_M2",
            "gunnerInAction": "RHS_M113_Gunner_M2",
            "gunnerGetInAction": "GetInLow",
            "gunnerGetOutAction": "GetOutLow",
            "viewGunnerInExternal": 1,
            "castGunnerShadow": 1,
            "forceHideGunner": 0,
            "canHideGunner": 0,
            "lodturnedout": 1000,
            "lodturnedin": 1000,
            "lodopticsout": 1000,
            "lodopticsin": 1000,
            "stabilizedInAxes": 0,
            "gunnerForceOptics": 0,
            "inGunnerMayFire": 1,
            "outGunnerMayFire": 1,
            "gunnerOpticsModel": "A3|weapons_f|reticle|optics_empty",
            "gunnerOutOpticsModel": "A3|weapons_f|reticle|optics_empty",
            "discreteDistance": [100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500],
            "discreteDistanceInitIndex": 2,
            "turretInfoType": "RHS_RscWeaponZeroing",
            "memoryPointGunnerOptics": "gunnerview",
            "memoryPointGunnerOutOptics": "gunnerview",
            "gunnerCompartments": "Compartment1",
            "selectionFireAnim": "zasleh",
            "primaryGunner": 1,
            "primaryObserver": 0,
            "startEngine": 0,
            "maxhorizontalrotspeed": 1.04,
            "maxverticalrotspeed": 1.04,
            "soundAttenuationTurret": "HeliAttenuationGunner",
            "disableSoundAttenuation": 1,
            "gunnerlefthandanimname": "OtocHlaven_Shake",
            "gunnerrighthandanimname": "OtocHlaven_Shake",
            # Class: CfgVehicles|rhsusf_m113tank_base|Turrets|MainTurret|ViewOptics [Indent level: 3],
            "ViewOptics": {
                "initFov": 0.375,
                "minFov": 0.375,
                "maxFov": 0.375,
                "visionMode": ["Normal"],
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
            # Class: CfgVehicles|rhsusf_m113tank_base|Turrets|MainTurret|ViewGunner [Indent level: 3],
            "ViewGunner": {
                "initAngleX": 0,
                "minAngleX": -45,
                "maxAngleX": 45,
                "initFov": 0.75,
                "minFov": 0.375,
                "maxFov": 0.75,
                "visionMode": [],
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
            # Class: CfgVehicles|rhsusf_m113tank_base|Turrets|MainTurret|OpticsIn [Indent level: 3],
            "OpticsIn": {
                # Class: CfgVehicles|rhsusf_m113tank_base|Turrets|MainTurret|OpticsIn|ViewOptics [Indent level: 4]
                "ViewOptics": {
                    "gunnerOpticsModel": "A3|weapons_f|reticle|optics_empty",
                    "gunnerOutOpticsModel": "A3|weapons_f|reticle|optics_empty",
                    "initAngleX": 0,
                    "minAngleX": -45,
                    "maxAngleX": 45,
                    "initFov": 0.75,
                    "minFov": 0.375,
                    "maxFov": 0.75,
                    "visionMode": [],
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
            # Class: CfgVehicles|rhsusf_m113tank_base|Turrets|MainTurret|HitPoints [Indent level: 3],
            "HitPoints": {
                # Class: CfgVehicles|rhsusf_m113tank_base|Turrets|MainTurret|HitPoints|HitTurret [Indent level: 4]
                "HitTurret": {
                    "armor": 0.5,
                    "material": -1,
                    "name": "vez",
                    "visual": "vez",
                    "passThrough": 0,
                    "minimalHit": 0.14,
                    "explosionShielding": 0.001,
                    "radius": 0.25
                },
                # Class: CfgVehicles|rhsusf_m113tank_base|Turrets|MainTurret|HitPoints|HitGun [Indent level: 4],
                "HitGun": {
                    "armor": 0.6,
                    "material": -1,
                    "name": "zbran",
                    "visual": "-",
                    "passThrough": 0,
                    "minimalHit": 0.13,
                    "explosionShielding": 0.001,
                    "radius": 0.25
                }
            },
            # Class: CfgVehicles|rhsusf_m113tank_base|Turrets|MainTurret|CommanderOptics [Indent level: 3],
            "CommanderOptics": {
            },
            # Class: CfgVehicles|rhsusf_m113tank_base|Turrets|MainTurret|Reflectors [Indent level: 3],
            "Reflectors": {
                # Class: CfgVehicles|rhsusf_m113tank_base|Turrets|MainTurret|Reflectors|cabin [Indent level: 4]
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
                    # Class: CfgVehicles|rhsusf_m113tank_base|Turrets|MainTurret|Reflectors|cabin|Attenuation [Indent level: 5],
                    "Attenuation": {
                        "start": 0,
                        "constant": 0,
                        "linear": 1,
                        "quadratic": 50,
                        "hardLimitStart": 1,
                        "hardLimitEnd": 1.5
                    }
                },
                # Class: CfgVehicles|rhsusf_m113tank_base|Turrets|MainTurret|Reflectors|cargo_light_1 [Indent level: 4],
                "cargo_light_1": {
                    "color": [800,900,650],
                    "position": "cargo_light_1",
                    "direction": "cargo_light_1_dir",
                    "hitpoint": "cargo_light_1",
                    "selection": "cargo_light_1",
                    "intensity": 4,
                    "useFlare": 0,
                    "coneFadeCoef": 0.1,
                    "innerAngle": 140,
                    "outerAngle": 175,
                    # Class: CfgVehicles|rhsusf_m113tank_base|Turrets|MainTurret|Reflectors|cargo_light_1|Attenuation [Indent level: 5],
                    "Attenuation": {
                        "start": 0,
                        "constant": 0,
                        "linear": 1,
                        "quadratic": 70,
                        "hardLimitStart": 0.4,
                        "hardLimitEnd": 1.5
                    },
                    "ambient": [5,5,5],
                    "size": 1,
                    "flareSize": 1,
                    "flareMaxDistance": 5,
                    "dayLight": 1,
                    "blinking": 0
                }
            },
            "soundServoVertical": ["A3|Sounds_F|vehicles|armor|APC|noises|servo_APC_gunner_vertical",0.562341,1,30],
            "minCamElev": -90,
            "maxCamElev": 90,
            "personTurretAction": "vehicle_turnout_2",
            "minOutElev": -20,
            "maxOutElev": 40,
            "initOutElev": 0,
            "minOutTurn": -120,
            "maxOutTurn": 150,
            "initOutTurn": 0,
            "animationSourceStickX": "turret_control_x",
            "animationSourceStickY": "turret_control_y",
            "viewGunnerShadowAmb": 0.5,
            "viewGunnerShadowDiff": 0.05,
            "showCrewAim": 2,
            "memoryPointsGetInGunner": "pos gunner",
            "memoryPointsGetInGunnerDir": "pos gunner dir",
            "gunnerOutOpticsEffect": [],
            "gunnerOpticsEffect": ["TankGunnerOptics2","OpticsBlur1","OpticsCHAbera1"],
            # Class: CfgVehicles|Tank_F|Turrets|MainTurret|Components [Indent level: 3],
            "Components": {
                # Class: CfgVehicles|Tank_F|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 4]
                "VehicleSystemsDisplayManagerComponentLeft": {
                    # Class: VehicleSystemsTemplateLeftGunner|Components [Indent level: 0]
                    "Components": {
                        # Class: VehicleSystemsTemplateLeftGunner|Components|VehicleDriverDisplay [Indent level: 1]
                        "VehicleDriverDisplay": {
                            "componentType": "TransportFeedDisplayComponent",
                            "source": "Driver"
                        },
                        # Class: VehicleSystemsTemplateLeftGunner|Components|VehicleCommanderDisplay [Indent level: 1],
                        "VehicleCommanderDisplay": {
                            "componentType": "TransportFeedDisplayComponent",
                            "source": "Commander"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|EmptyDisplay [Indent level: 1],
                        "EmptyDisplay": {
                            "componentType": "EmptyDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|MinimapDisplay [Indent level: 1],
                        "MinimapDisplay": {
                            "componentType": "MinimapDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|MineDetectorDisplay [Indent level: 1],
                        "MineDetectorDisplay": {
                            "componentType": "MineDetectorDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|CrewDisplay [Indent level: 1],
                        "CrewDisplay": {
                            "componentType": "CrewDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|UAVDisplay [Indent level: 1],
                        "UAVDisplay": {
                            "componentType": "UAVFeedDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|SlingLoadDisplay [Indent level: 1],
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
                # Class: CfgVehicles|Tank_F|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 4],
                "VehicleSystemsDisplayManagerComponentRight": {
                    # Class: VehicleSystemsTemplateRightGunner|Components [Indent level: 0]
                    "Components": {
                        # Class: VehicleSystemsTemplateRightGunner|Components|VehicleDriverDisplay [Indent level: 1]
                        "VehicleDriverDisplay": {
                            "componentType": "TransportFeedDisplayComponent",
                            "source": "Driver"
                        },
                        # Class: VehicleSystemsTemplateRightGunner|Components|VehicleCommanderDisplay [Indent level: 1],
                        "VehicleCommanderDisplay": {
                            "componentType": "TransportFeedDisplayComponent",
                            "source": "Commander"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerRight|Components|EmptyDisplay [Indent level: 1],
                        "EmptyDisplay": {
                            "componentType": "EmptyDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerRight|Components|MinimapDisplay [Indent level: 1],
                        "MinimapDisplay": {
                            "componentType": "MinimapDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerRight|Components|MineDetectorDisplay [Indent level: 1],
                        "MineDetectorDisplay": {
                            "componentType": "MineDetectorDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerRight|Components|CrewDisplay [Indent level: 1],
                        "CrewDisplay": {
                            "componentType": "CrewDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerRight|Components|UAVDisplay [Indent level: 1],
                        "UAVDisplay": {
                            "componentType": "UAVFeedDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerRight|Components|SlingLoadDisplay [Indent level: 1],
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
            "animationSourceBody": "mainTurret",
            "animationSourceGun": "mainGun",
            "animationSourceCamElev": "camElev",
            "proxyType": "CPGunner",
            "proxyIndex": 1,
            "gunnerType": "",
            "soundElevation": ["",0.00316228,1],
            "minTurn": -360,
            "maxTurn": 360,
            "initTurn": 0,
            "initCamElev": 0,
            "primary": 1,
            "hasGunner": 1,
            "turretCanSee": 0,
            # Class: CfgVehicles|AllVehicles|NewTurret|TurretSpec [Indent level: 2],
            "TurretSpec": {
                "showHeadPhones": 0
            },
            "gunnerOpticsColor": [0,0,0,1],
            "gunnerOpticsShowCursor": 0,
            "gunnerOutOpticsColor": [0,0,0,1],
            "gunnerOutForceOptics": 0,
            "gunnerOutOpticsShowCursor": 0,
            "gunnerFireAlsoInInternalCamera": 1,
            "gunnerOutFireAlsoInInternalCamera": 1,
            "gunnerUsesPilotView": 0,
            "viewGunnerShadow": 1,
            "ejectDeadGunner": 0,
            "hideWeaponsGunner": 1,
            "showHMD": 0,
            "lockWhenDriverOut": 0,
            "lockWhenVehicleSpeed": -1,
            "memoryPointsGetInGunnerPrecise": "",
            "missileBeg": "spice rakety",
            "missileEnd": "konec rakety",
            "armorLights": 0.4,
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
                    # Class: WeaponFireGun|Table|T0 [Indent level: 1]
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
                    # Class: WeaponCloudsGun|Table|T0 [Indent level: 1]
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
                    # Class: WeaponCloudsMGun|Table|T0 [Indent level: 1]
                    "T0": {
                        "maxT": 0,
                        "color": [1,1,1,0]
                    }
                }
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
            }
        },
        # Class: CfgVehicles|rhsusf_m113tank_base|Turrets|CargoTurret_01 [Indent level: 2],
        "CargoTurret_01": {
            "weapons": ["rhsusf_weap_DummyLauncher"],
            "gunnerAction": "vehicle_turnout_1",
            "gunnerInAction": "RHS_M113_Cargo01_FFV",
            "animationSourceHatch": "rear_hatch_handler_1",
            "isPersonTurret": 1,
            "gunnerGetInAction": "GetInMantis",
            "gunnerGetOutAction": "GetOutMantis",
            "memoryPointsGetInGunner": "pos cargo 1",
            "memoryPointsGetInGunnerDir": "pos cargo 1 dir",
            "commanding": -2,
            "rhs_hatch_control": 1,
            "rhs_hatch_control_depeneds": ["rear_hatch_handler_2"],
            "enabledByAnimationSource": "rear_hatch",
            "gunnerForceOptics": 0,
            "gunnerName": "Passenger (Rear Hatch Right)",
            "gunnerCompartments": "Compartment1",
            "gunnerDoor": "Ramp",
            "memoryPointGunnerOptics": "",
            "selectionFireAnim": "",
            "canHideGunner": 1,
            "LODTurnedIn": 1200,
            "LODTurnedOut": 1,
            "proxyIndex": 3,
            "maxElev": 45,
            "minElev": -20,
            "maxTurn": 160,
            "minTurn": -120,
            # Class: CfgVehicles|rhsusf_m113tank_base|Turrets|CargoTurret_01|TurnIn [Indent level: 3],
            "TurnIn": {
                "limitsArrayTop": [[1,-1],[1,1]],
                "limitsArrayBottom": [[-1,-1],[-1,1]]
            },
            # Class: CfgVehicles|rhsusf_m113tank_base|Turrets|CargoTurret_01|TurnOut [Indent level: 3],
            "TurnOut": {
                "limitsArrayTop": [[45,-160],[45,160]],
                "limitsArrayBottom": [[-7.4646,-161.174],[-7.4264,-106.981],[-12.8388,-102.043],[-10.6611,-88.8004],[-18.2532,-59.667],[-7.4306,-49.4319],[-11.1057,-49.3832],[-7.7205,-46.9855],[-10.1225,-44.3478],[-19.7726,-28.4836],[-16.0375,17.8663],[-11.9149,29.7774],[-7.7212,38.3127],[-4.4575,39.3049],[-5.2729,43.6182],[-1.9005,48.6889],[-4.8722,73.8609],[-3.9671,78.4205],[6.3736,79.8659],[15.175,91.7335],[30.0065,113.787],[26.6582,129.369],[3.4023,135.919],[-15.3679,144.278],[-16.1314,160.087]]
            },
            # Class: CfgVehicles|rhsusf_m113tank_base|Turrets|CargoTurret_01|Hitpoints [Indent level: 3],
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
                    # Class: WeaponFireGun|Table|T0 [Indent level: 1]
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
                    # Class: WeaponCloudsGun|Table|T0 [Indent level: 1]
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
                    # Class: WeaponCloudsMGun|Table|T0 [Indent level: 1]
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
        # Class: CfgVehicles|rhsusf_m113tank_base|Turrets|CargoTurret_02 [Indent level: 2],
        "CargoTurret_02": {
            "proxyIndex": 7,
            "isPersonTurret": 1,
            "gunnerInAction": "RHS_M113_Cargo02_FFV",
            "animationSourceHatch": "rear_hatch_handler_2",
            "rhs_hatch_control_depeneds": ["rear_hatch_handler_1"],
            "gunnerName": "Passenger (Rear Hatch Left)",
            "memoryPointsGetInGunner": "pos cargo",
            "memoryPointsGetInGunnerDir": "pos cargo dir",
            # Class: CfgVehicles|rhsusf_m113tank_base|Turrets|CargoTurret_02|TurnOut [Indent level: 3],
            "TurnOut": {
                "limitsArrayTop": [[45,-120],[45,160]],
                "limitsArrayBottom": [[-15.0098,-171.623],[-16.6821,-154.958],[-11.7215,-148.149],[-9.7461,-147.78],[-9.8556,-146.773],[-11.4685,-146.32],[-11.573,-145.918],[-16.224,-137.448],[-11.0125,-100.247],[9.7255,-98.4888],[18.6911,-96.8685],[-9.7613,-96.5088],[23.9199,-91.8655],[27.0373,-83.6022],[27.0452,-68.9423],[21.0796,-57.9417],[19.9345,-56.8518],[12.8666,-54.0844],[-2.7019,-45.4012],[-2.7096,-44.2127],[-0.2736,-43.947],[0.1972,-38.4689],[-1.9929,-37.4971],[-2.2836,-35.1064],[-0.0074,-34.8379],[-0.0715,-32.4873],[-2.0306,-31.7878],[-5.3829,-23.1603],[0.1307,-21.0844],[-8.0524,-10.9118],[-19.3082,20.7243],[-18.4856,31.6046],[-12.0216,43.6287],[-8.3882,45.7286],[-19.8808,58.2848],[-18.524,94.6759],[-14.4017,104.768],[-11.3235,106.299],[-12.9417,112.353],[-14.7703,127.591],[-9.6985,128.747],[-9.2638,131.578],[-9.9322,162.423],[-9.1396,170.774]]
            },
            "weapons": ["rhsusf_weap_DummyLauncher"],
            "gunnerAction": "vehicle_turnout_1",
            "gunnerGetInAction": "GetInMantis",
            "gunnerGetOutAction": "GetOutMantis",
            "commanding": -2,
            "rhs_hatch_control": 1,
            "enabledByAnimationSource": "rear_hatch",
            "gunnerForceOptics": 0,
            "gunnerCompartments": "Compartment1",
            "gunnerDoor": "Ramp",
            "memoryPointGunnerOptics": "",
            "selectionFireAnim": "",
            "canHideGunner": 1,
            "LODTurnedIn": 1200,
            "LODTurnedOut": 1,
            "maxElev": 45,
            "minElev": -20,
            "maxTurn": 160,
            "minTurn": -120,
            # Class: CfgVehicles|rhsusf_m113tank_base|Turrets|CargoTurret_01|TurnIn [Indent level: 3],
            "TurnIn": {
                "limitsArrayTop": [[1,-1],[1,1]],
                "limitsArrayBottom": [[-1,-1],[-1,1]]
            },
            # Class: CfgVehicles|rhsusf_m113tank_base|Turrets|CargoTurret_01|Hitpoints [Indent level: 3],
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
                    # Class: WeaponFireGun|Table|T0 [Indent level: 1]
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
                    # Class: WeaponCloudsGun|Table|T0 [Indent level: 1]
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
                    # Class: WeaponCloudsMGun|Table|T0 [Indent level: 1]
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
        }
    },
    # Class: CfgVehicles|rhsusf_m113tank_base|Damage [Indent level: 1],
    "Damage": {
        "tex": [],
        "mat": ["rhsusf|addons|rhsusf_m113|data_new|m113a3_01.rvmat","rhsusf|addons|rhsusf_m113|data_new|m113a3_01_dam.rvmat","rhsusf|addons|rhsusf_m113|data_new|m113a3_01_destr.rvmat","rhsusf|addons|rhsusf_m113|data_new|m113a3_02.rvmat","rhsusf|addons|rhsusf_m113|data_new|m113a3_02_dam.rvmat","rhsusf|addons|rhsusf_m113|data_new|m113a3_02_destr.rvmat","rhsusf|addons|rhsusf_m113|data_new|m113a3_03.rvmat","rhsusf|addons|rhsusf_m113|data_new|m113a3_03_dam.rvmat","rhsusf|addons|rhsusf_m113|data_new|m113a3_03_destr.rvmat","rhsusf|addons|rhsusf_m113|data_new|m113a3_int01.rvmat","rhsusf|addons|rhsusf_m113|data_new|m113a3_int01_dam.rvmat","rhsusf|addons|rhsusf_m113|data_new|m113a3_int01_destr.rvmat","rhsusf|addons|rhsusf_m113|data_new|m113a3_int02.rvmat","rhsusf|addons|rhsusf_m113|data_new|m113a3_int02_dam.rvmat","rhsusf|addons|rhsusf_m113|data_new|m113a3_int02_destr.rvmat","rhsusf|addons|rhsusf_m113|data_new|m113a3_int03.rvmat","rhsusf|addons|rhsusf_m113|data_new|m113a3_int03_dam.rvmat","rhsusf|addons|rhsusf_m113|data_new|m113a3_int03_destr.rvmat","rhsusf|addons|rhsusf_m113|data_new|M23_pintle.rvmat","rhsusf|addons|rhsusf_m113|data_new|M23_pintle_dam.rvmat","rhsusf|addons|rhsusf_m113|data_new|m113a3_01_destr.rvmat","rhsusf|addons|rhsusf_m113|data_new|m113a3_t.rvmat","rhsusf|addons|rhsusf_m113|data_new|m113a3_t_dam.rvmat","rhsusf|addons|rhsusf_m113|data_new|m113a3_t_destr.rvmat","rhsusf|addons|rhsusf_m113|data_new|m113a3_shield.rvmat","rhsusf|addons|rhsusf_m113|data_new|m113a3_shield_dam.rvmat","rhsusf|addons|rhsusf_m113|data_new|m113a3_shield_destr.rvmat","a3|data_f|default.rvmat","a3|data_f|default.rvmat","a3|data_f|default_destruct.rvmat"]
    },
    # Class: CfgVehicles|rhsusf_m113tank_base|AnimationSources [Indent level: 1],
    "AnimationSources": {
        # Class: CfgVehicles|rhsusf_m113tank_base|AnimationSources|cargolights_hide [Indent level: 2]
        "cargolights_hide": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 0
        },
        # Class: CfgVehicles|rhsusf_m113tank_base|AnimationSources|cabinlights_hide [Indent level: 2],
        "cabinlights_hide": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 0
        },
        # Class: CfgVehicles|rhsusf_m113tank_base|AnimationSources|IFF_Panels_Hide [Indent level: 2],
        "IFF_Panels_Hide": {
            "source": "user",
            "mass": -20,
            "displayName": "hide IFF Panels",
            "author": "Red Hammer Studios",
            "animPeriod": 1e-005,
            "initPhase": 0
        },
        # Class: CfgVehicles|rhsusf_m113tank_base|AnimationSources|ReloadAnim [Indent level: 2],
        "ReloadAnim": {
            "source": "reload",
            "weapon": "RHS_M2"
        },
        # Class: CfgVehicles|rhsusf_m113tank_base|AnimationSources|ReloadMagazine [Indent level: 2],
        "ReloadMagazine": {
            "source": "reloadmagazine",
            "weapon": "RHS_M2"
        },
        # Class: CfgVehicles|rhsusf_m113tank_base|AnimationSources|Revolving [Indent level: 2],
        "Revolving": {
            "source": "revolving",
            "weapon": "RHS_M2"
        },
        # Class: CfgVehicles|rhsusf_m113tank_base|AnimationSources|muzzle_rot_hmg [Indent level: 2],
        "muzzle_rot_hmg": {
            "source": "ammorandom",
            "weapon": "RHS_M2"
        },
        # Class: CfgVehicles|rhsusf_m113tank_base|AnimationSources|smoke_revolving_source [Indent level: 2],
        "smoke_revolving_source": {
            "source": "revolving",
            "weapon": "rhsusf_weap_M259"
        },
        # Class: CfgVehicles|rhsusf_m113tank_base|AnimationSources|HatchD [Indent level: 2],
        "HatchD": {
            "source": "door",
            "animPeriod": 2.1
        },
        # Class: CfgVehicles|rhsusf_m113tank_base|AnimationSources|rear_hatch [Indent level: 2],
        "rear_hatch": {
            "source": "door",
            "animPeriod": 0.8,
            "initPhase": 0
        },
        # Class: CfgVehicles|rhsusf_m113tank_base|AnimationSources|ramp [Indent level: 2],
        "ramp": {
            "source": "door",
            "animPeriod": 3.285,
            "initPhase": 0,
            "sound": "rhs_ramp",
            "soundPosition": "ramp_axis"
        },
        # Class: CfgVehicles|rhsusf_m113tank_base|AnimationSources|hatchGunner [Indent level: 2],
        "hatchGunner": {
            "source": "door",
            "animPeriod": 1e-005,
            "initPhase": 0,
            "displayName": "close commander hatch"
        }
    },
    "smokeLauncherGrenadeCount": 4,
    "smokeLauncherVelocity": 14,
    "smokeLauncherOnTurret": 0,
    "smokeLauncherAngle": 90,
    # Class: CfgVehicles|rhsusf_m113tank_base|ViewOptics [Indent level: 1],
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
    # Class: CfgVehicles|rhsusf_m113tank_base|Reflectors [Indent level: 1],
    "Reflectors": {
        # Class: CfgVehicles|rhsusf_m113tank_base|Reflectors|Left [Indent level: 2]
        "Left": {
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "position": "l svetlo",
            "direction": "konec l svetla",
            "hitpoint": "l svetlo",
            "selection": "L svetlo",
            "size": 1,
            "innerAngle": 30,
            "outerAngle": 100,
            "coneFadeCoef": 10,
            "intensity": 1,
            "useFlare": 1,
            "dayLight": 0,
            "flareSize": 1,
            # Class: CfgVehicles|rhsusf_m113tank_base|Reflectors|Left|Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardLimitStart": 30,
                "hardLimitEnd": 60
            }
        },
        # Class: CfgVehicles|rhsusf_m113tank_base|Reflectors|Right [Indent level: 2],
        "Right": {
            "position": "p svetlo",
            "direction": "konec p svetla",
            "hitpoint": "p svetlo",
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
            # Class: CfgVehicles|rhsusf_m113tank_base|Reflectors|Left|Attenuation [Indent level: 3],
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
    # Class: CfgVehicles|rhsusf_m113tank_base|TransportBackpacks [Indent level: 1],
    "TransportBackpacks": {
        # Class: CfgVehicles|rhsusf_m113tank_base|TransportBackpacks|_xx_rhsusf_falconii [Indent level: 2]
        "_xx_rhsusf_falconii": {
            "backpack": "rhsusf_falconii",
            "count": 4
        }
    },
    # Class: CfgVehicles|rhsusf_m113tank_base|TransportMagazines [Indent level: 1],
    "TransportMagazines": {
        # Class: CfgVehicles|rhsusf_m113tank_base|TransportMagazines|_xx_rhs_mag_30Rnd_556x45_M855A1_Stanag [Indent level: 2]
        "_xx_rhs_mag_30Rnd_556x45_M855A1_Stanag": {
            "magazine": "rhs_mag_30Rnd_556x45_M855A1_Stanag",
            "count": 50
        },
        # Class: CfgVehicles|rhsusf_m113tank_base|TransportMagazines|_xx_rhs_mag_M433_HEDP [Indent level: 2],
        "_xx_rhs_mag_M433_HEDP": {
            "magazine": "rhs_mag_M433_HEDP",
            "count": 20
        },
        # Class: CfgVehicles|rhsusf_m113tank_base|TransportMagazines|_xx_rhsusf_100Rnd_556x45_soft_pouch [Indent level: 2],
        "_xx_rhsusf_100Rnd_556x45_soft_pouch": {
            "magazine": "rhsusf_100Rnd_556x45_soft_pouch",
            "count": 11
        },
        # Class: CfgVehicles|rhsusf_m113tank_base|TransportMagazines|_xx_rhs_mag_M441_HE [Indent level: 2],
        "_xx_rhs_mag_M441_HE": {
            "magazine": "rhs_mag_M441_HE",
            "count": 20
        },
        # Class: CfgVehicles|rhsusf_m113tank_base|TransportMagazines|_xx_rhs_mag_M714_white [Indent level: 2],
        "_xx_rhs_mag_M714_white": {
            "magazine": "rhs_mag_M714_white",
            "count": 8
        },
        # Class: CfgVehicles|rhsusf_m113tank_base|TransportMagazines|_xx_rhs_mag_M662_red [Indent level: 2],
        "_xx_rhs_mag_M662_red": {
            "magazine": "rhs_mag_M662_red",
            "count": 4
        },
        # Class: CfgVehicles|rhsusf_m113tank_base|TransportMagazines|_xx_rhs_mag_m67 [Indent level: 2],
        "_xx_rhs_mag_m67": {
            "magazine": "rhs_mag_m67",
            "count": 10
        },
        # Class: CfgVehicles|rhsusf_m113tank_base|TransportMagazines|_xx_rhs_mag_m18_green [Indent level: 2],
        "_xx_rhs_mag_m18_green": {
            "magazine": "rhs_mag_m18_green",
            "count": 4
        },
        # Class: CfgVehicles|rhsusf_m113tank_base|TransportMagazines|_xx_rhs_mag_m18_red [Indent level: 2],
        "_xx_rhs_mag_m18_red": {
            "magazine": "rhs_mag_m18_red",
            "count": 4
        },
        # Class: CfgVehicles|rhsusf_m113tank_base|TransportMagazines|_xx_rhs_mag_an_m8hc [Indent level: 2],
        "_xx_rhs_mag_an_m8hc": {
            "magazine": "rhs_mag_an_m8hc",
            "count": 10
        }
    },
    # Class: CfgVehicles|rhsusf_m113tank_base|TransportItems [Indent level: 1],
    "TransportItems": {
        # Class: CfgVehicles|rhsusf_m113tank_base|TransportItems|_xx_FirstAidKit [Indent level: 2]
        "_xx_FirstAidKit": {
            "name": "FirstAidKit",
            "count": 10
        },
        # Class: CfgVehicles|rhsusf_m113tank_base|TransportItems|_xx_Medikit [Indent level: 2],
        "_xx_Medikit": {
            "name": "Medikit",
            "count": 2
        },
        # Class: CfgVehicles|rhsusf_m113tank_base|TransportItems|_xx_Toolkit [Indent level: 2],
        "_xx_Toolkit": {
            "name": "Toolkit",
            "count": 1
        }
    },
    # Class: CfgVehicles|rhsusf_m113tank_base|TransportWeapons [Indent level: 1],
    "TransportWeapons": {
        # Class: CfgVehicles|rhsusf_m113tank_base|TransportWeapons|_xx_rhs_weap_m4_carryhandle [Indent level: 2]
        "_xx_rhs_weap_m4_carryhandle": {
            "weapon": "rhs_weap_m4_carryhandle",
            "count": 4
        }
    },
    # Class: CfgVehicles|rhsusf_m113tank_base|EventHandlers [Indent level: 1],
    "EventHandlers": {
        # Class: CfgVehicles|rhsusf_m113tank_base|EventHandlers|RHSUSF_EventHandlers [Indent level: 2]
        "RHSUSF_EventHandlers": {
            "hitpart": "_this call rhsusf_fnc_hitSpall",
            "getIn": "_this call rhs_fnc_m2_doors",
            "getOut": "_this call rhs_fnc_m2_doors",
            "turnIn": "([0] + _this)  call rhsusf_fnc_turretAction;",
            "turnOut": "([1] + _this) call rhsusf_fnc_turretAction;",
            "engine": "[_this select 0,_this select 1,2] call rhs_fnc_engineStartupDelay"
        },
        "init": "if (local (_this select 0)) then {[(_this select 0), `, [], false] call bis_fnc_initVehicle;};",
        "fired": "[_this select 0,_this select 6,'missile_move','MissileBase'] call BIS_fnc_missileLaunchPositionFix; _this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');",
        # Class: DefaultEventHandlers|RHS_DefaultEventhandlers [Indent level: 0],
        "RHS_DefaultEventhandlers": {
            "hitpart": "_this call rhs_fnc_hitPart"
        }
    },
    "hiddenSelections": ["camo1","camo2","camo3","camo4","camo5","camo6"],
    "hiddenSelectionsTextures": ["rhsusf|addons|rhsusf_m113|data_new|m113a3_01_wd_h_co.paa","rhsusf|addons|rhsusf_m113|data_new|m113a3_02_wd_h_co.paa","rhsusf|addons|rhsusf_m113|data_new|m113a3_03_wd_co.paa","rhsusf|addons|rhsusf_m113|data_new|m113a3_int03_wd_co.paa","rhsusf|addons|rhsusf_m113|data_new|m23_pintle_wd_co.paa","rhsusf|addons|rhsusf_m113|data_new|m113a3_shield_wd_co.paa"],
    # Class: CfgVehicles|rhsusf_m113tank_base|textureSources [Indent level: 1],
    "textureSources": {
        # Class: CfgVehicles|rhsusf_m113tank_base|textureSources|standard [Indent level: 2]
        "standard": {
            "displayName": "Woodland",
            "author": "Red Hammer Studios",
            "textures": ["rhsusf|addons|rhsusf_m113|data_new|m113a3_01_wd_h_co.paa","rhsusf|addons|rhsusf_m113|data_new|m113a3_02_wd_h_co.paa","rhsusf|addons|rhsusf_m113|data_new|m113a3_03_wd_co.paa","rhsusf|addons|rhsusf_m113|data_new|m113a3_int03_wd_co.paa","rhsusf|addons|rhsusf_m113|data_new|m23_pintle_wd_co.paa","rhsusf|addons|rhsusf_m113|data_new|m113a3_shield_wd_co.paa"],
            "factions": ["rhs_faction_usarmy_wd"]
        },
        # Class: CfgVehicles|rhsusf_m113tank_base|textureSources|Desert [Indent level: 2],
        "Desert": {
            "displayName": "Desert",
            "author": "Red Hammer Studios",
            "textures": ["rhsusf|addons|rhsusf_m113|data_new|m113a3_01_d_h_co.paa","rhsusf|addons|rhsusf_m113|data_new|m113a3_02_d_h_co.paa","rhsusf|addons|rhsusf_m113|data_new|m113a3_03_d_co.paa","rhsusf|addons|rhsusf_m113|data_new|m113a3_int03_d_co.paa","rhsusf|addons|rhsusf_m113|data_new|m23_pintle_d_co.paa","rhsusf|addons|rhsusf_m113|data_new|m113a3_shield_d_co.paa"],
            "factions": ["rhs_faction_usarmy_d"]
        },
        # Class: CfgVehicles|rhsusf_m113tank_base|textureSources|Olive [Indent level: 2],
        "Olive": {
            "displayName": "Olive",
            "author": "Red Hammer Studios",
            "textures": ["rhsusf|addons|rhsusf_m113|data_new|m113a3_01_sup_wd_co.paa","rhsusf|addons|rhsusf_m113|data_new|m113a3_02_sup_wd_co.paa","rhsusf|addons|rhsusf_m113|data_new|m113a3_03_wd_co.paa","rhsusf|addons|rhsusf_m113|data_new|m113a3_int03_wd_co.paa","rhsusf|addons|rhsusf_m113|data_new|m23_pintle_wd_co.paa","rhsusf|addons|rhsusf_m113|data_new|m113a3_shield_od_co.paa"],
            "factions": ["rhs_faction_usarmy_wd"]
        }
    },
    "textureList": [],
    # Class: CfgVehicles|rhsusf_m113tank_base|ViewPilot [Indent level: 1],
    "ViewPilot": {
        "initAngleX": 7,
        "minAngleX": -45,
        "maxAngleX": 35,
        "initAngleY": 0,
        "minAngleY": -90,
        "maxAngleY": 90,
        "minFov": 0.25,
        "maxFov": 1.25,
        "initFov": 0.75,
        "minMoveX": -0.075,
        "maxMoveX": 0.075,
        "minMoveY": -0.075,
        "maxMoveY": 0.075,
        "minMoveZ": -0.075,
        "maxMoveZ": 0.1,
        "speedZoomMaxSpeed": 1e+010,
        "speedZoomMaxFOV": 0
    },
    # Class: CfgVehicles|rhsusf_m113tank_base|UserActions [Indent level: 1],
    "UserActions": {
        # Class: CfgVehicles|rhsusf_m113tank_base|UserActions|OpenCargoDoor [Indent level: 2]
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
        # Class: CfgVehicles|rhsusf_m113tank_base|UserActions|CloseCargoDoor [Indent level: 2],
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
        # Class: CfgVehicles|rhsusf_m113tank_base|UserActions|ToggleLight [Indent level: 2],
        "ToggleLight": {
            "displayName": "Toggle interior light",
            "position": "pos driver",
            "radius": 15,
            "showwindow": 0,
            "condition": "player in this;",
            "statement": "[this,'cargolights_hide'] call rhs_fnc_toggleIntLight",
            "onlyforplayer": 1
        }
    },
    # Class: CfgVehicles|rhsusf_m113tank_base|Attributes [Indent level: 1],
    "Attributes": {
        # Class: CfgVehicles|rhsusf_m113tank_base|Attributes|ObjectTexture [Indent level: 2]
        "ObjectTexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayName": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        # Class: CfgVehicles|rhsusf_m113tank_base|Attributes|rhs_hideIFFPanel [Indent level: 2],
        "rhs_hideIFFPanel": {
            "displayName": "Hide IFF Panel",
            "property": "rhs_hideIFFPanel",
            "control": "CheckboxNumber",
            "expression": "_this animate ['IFF_Panels_Hide',_value,true]",
            "defaultValue": "0"
        },
        # Class: CfgVehicles|rhsusf_m113tank_base|Attributes|rhs_openRamp [Indent level: 2],
        "rhs_openRamp": {
            "displayName": "Open rear ramp",
            "property": "rhs_openRamp",
            "control": "CheckboxNumber",
            "expression": "_this animateDoor ['ramp',_value,true]",
            "defaultValue": "0"
        }
    },
    "soundGetIn": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|handling|getin|light_2.ogg",0.5,1],
    "soundGetOut": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|handling|getout|light_2.ogg",0.5,1,40],
    "soundTurnIn": ["A3|Sounds_F|vehicles|noises|Turn_in_out",1.77828,1,20],
    "soundTurnOut": ["A3|Sounds_F|vehicles|noises|Turn_in_out",1.77828,1,20],
    "soundTurnInInternal": ["A3|Sounds_F|vehicles|noises|Turn_in_out",1.77828,1,20],
    "soundTurnOutInternal": ["A3|Sounds_F|vehicles|noises|Turn_in_out",1.77828,1,20],
    "soundDammage": [".ogg",0.5,1],
    "soundEngineOnInt": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|engines|tracked_apc_02|tracked_apc_02_start_int.ogg",0.5,1],
    "soundEngineOffInt": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|engines|tracked_apc_02|tracked_apc_02_shut_int.ogg",0.5,1],
    "soundEngineOnExt": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|engines|tracked_apc_02|tracked_apc_02_start_ext.ogg",0.5,1,125],
    "soundEngineOffExt": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|engines|tracked_apc_02|tracked_apc_02_shut_ext.ogg",0.5,1,100],
    "BushCrash1": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_Collision_Light_Bush_01",0.630957,1,100],
    "BushCrash2": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_Collision_Light_Bush_02",0.630957,1,100],
    "BushCrash3": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_Collision_Light_Bush_03",0.630957,1,100],
    "soundBushCrash": ["BushCrash1",0.33,"BushCrash2",0.33,"BushCrash3",0.33],
    "buildCrash0": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_building_01.ogg",1.5,1,300],
    "buildCrash1": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_building_02.ogg",1.5,1,300],
    "buildCrash2": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_building_03.ogg",1.5,1,300],
    "buildCrash3": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_building_04.ogg",1.5,1,300],
    "buildCrash4": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_05",3.16228,1,200],
    "buildCrash5": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_06",3.16228,1,200],
    "soundBuildingCrash": ["buildcrash0",0.25,"buildcrash1",0.25,"buildcrash2",0.25,"buildcrash3",0.25],
    "woodCrash0": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_mix_wood_01.ogg",1.5,1,300],
    "woodCrash1": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_mix_wood_02.ogg",1.5,1,300],
    "woodCrash2": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_mix_wood_03.ogg",1.5,1,300],
    "woodCrash3": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_mix_wood_04.ogg",1.5,1,300],
    "woodCrash4": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_mix_wood_05.ogg",1.5,1,300],
    "woodCrash5": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_mix_wood_06.ogg",1.5,1,300],
    "soundWoodCrash": ["woodcrash0",0.166,"woodcrash1",0.166,"woodcrash2",0.166,"woodcrash3",0.166,"woodcrash4",0.166,"woodcrash5",0.166],
    "ArmorCrash0": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_vehicle_01.ogg",1.5,1,300],
    "ArmorCrash1": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_vehicle_02.ogg",1.5,1,300],
    "ArmorCrash2": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_vehicle_03.ogg",1.5,1,300],
    "ArmorCrash3": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_vehicle_04.ogg",1.5,1,300],
    "ArmorCrash4": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_05",3.16228,1,200],
    "ArmorCrash5": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_06",3.16228,1,200],
    "soundArmorCrash": ["armorcrash0",0.25,"armorcrash1",0.25,"armorcrash2",0.25,"armorcrash3",0.25],
    # Class: CfgVehicles|APC_Tracked_02_base_F|Sounds [Indent level: 1],
    "Sounds": {
        "soundSetsInt": ["jsrs_tracked_apc_02_idle_interior_soundset","jsrs_tracked_apc_02_low_interior_soundset","jsrs_tracked_apc_02_high_interior_soundset","jsrs_tracked_apc_02_start_interior_soundset","jsrs_tracked_rolling_int_soundset","jsrs_tracked_offroad_rolling_int_soundset","jsrs_vehicle_interior_silent_soundset","jsrs_heavy_vehicle_rain_int_soundset","jsrs_tracked_rattle_int_soundset","jsrs_light_tracks_slow_int_soundset","jsrs_light_tracks_fast_int_soundset","jsrs_light_tracks_grass_int_soundset","jsrs_light_tracks_dirt_int_soundset","jsrs_gear_interior_02_soundset","jsrs_heavy_vehicle_water_moving_ext_soundset"],
        "soundSetsExt": ["jsrs_tracked_apc_02_idle_exterior_soundset","jsrs_tracked_apc_02_low_exterior_soundset","jsrs_tracked_apc_02_high_exterior_soundset","jsrs_tracked_apc_02_start_exterior_soundset","jsrs_tracked_apc_02_distance_soundset","jsrs_heavy_vehicle_rain_ext_soundset","jsrs_tracked_rattle_ext_soundset","jsrs_light_tracks_slow_ext_soundset","jsrs_light_tracks_fast_ext_soundset","jsrs_light_tracks_grass_ext_soundset","jsrs_light_tracks_dirt_ext_soundset","jsrs_gear_exterior_02_soundset","jsrs_heavy_vehicle_water_moving_ext_soundset"]
    },
    "_generalMacro": "APC_Tracked_02_base_F",
    "brakeIdleSpeed": 0.1,
    "antiRollbarForceCoef": 20,
    "antiRollbarForceLimit": 10,
    "antiRollbarSpeedMin": 10,
    "antiRollbarSpeedMax": 55,
    # Class: CfgVehicles|APC_Tracked_02_base_F|MFD [Indent level: 1],
    "MFD": {
        # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Driver_Heading [Indent level: 2]
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
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Driver_Heading|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Driver_Heading|Bones [Indent level: 3],
            "Bones": {
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Driver_Heading|Draw [Indent level: 3],
            "Draw": {
                "color": [0.61,0.62,0],
                "alpha": 1,
                "condition": "on",
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Driver_Heading|Draw|Driver_Heading [Indent level: 4],
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
        # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Driver_Heading_text [Indent level: 2],
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
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Driver_Heading_text|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Driver_Heading_text|Bones [Indent level: 3],
            "Bones": {
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Driver_Heading_text|Draw [Indent level: 3],
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Driver_Heading_text|Draw|Driver_Heading [Indent level: 4],
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
        # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Driver_Heading_second [Indent level: 2],
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
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Driver_Heading_second|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Driver_Heading_second|Bones [Indent level: 3],
            "Bones": {
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Driver_Heading_second|Draw [Indent level: 3],
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Driver_Heading_second|Draw|Driver_Heading [Indent level: 4],
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
        # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_AmmoType [Indent level: 2],
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
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_AmmoType|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_AmmoType|Bones [Indent level: 3],
            "Bones": {
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_AmmoType|Draw [Indent level: 3],
            "Draw": {
                "color": [0.92,0.01,0],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_AmmoType|Draw|Gunner_AmmoType [Indent level: 4],
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
        # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_AmmoIndicator [Indent level: 2],
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
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_AmmoIndicator|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_AmmoIndicator|Bones [Indent level: 3],
            "Bones": {
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_AmmoIndicator|Draw [Indent level: 3],
            "Draw": {
                "color": [0.92,0.01,0],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_AmmoIndicator|Draw|Gunner_Text_1 [Indent level: 4],
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
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_AmmoIndicator|Draw|Gunner_Text_2 [Indent level: 4],
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
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_AmmoIndicator|Draw|Gunner_Text_3 [Indent level: 4],
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
        # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Ready_To_Fire [Indent level: 2],
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
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Ready_To_Fire|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Ready_To_Fire|Bones [Indent level: 3],
            "Bones": {
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Ready_To_Fire|Draw [Indent level: 3],
            "Draw": {
                "color": [0,0,0],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Ready_To_Fire|Draw|Top_text [Indent level: 4],
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
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Ready_To_Fire|Draw|Bottom_text [Indent level: 4],
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
        # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Display [Indent level: 2],
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
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Display|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Display|Bones [Indent level: 3],
            "Bones": {
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Display|Draw [Indent level: 3],
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Display|Draw|Main_armament [Indent level: 4],
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
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Display|Draw|Machinegun [Indent level: 4],
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
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Display|Draw|Main_armament_ammo_type [Indent level: 4],
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
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Display|Draw|Lased_distance_elevation [Indent level: 4],
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
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Display|Draw|Azimut [Indent level: 4],
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
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Display|Draw|Damage [Indent level: 4],
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
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Display|Draw|Heading [Indent level: 4],
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
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Display|Draw|Lased_Range [Indent level: 4],
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
        # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Main_Armament_Ammo_Type [Indent level: 2],
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
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Main_Armament_Ammo_Type|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Main_Armament_Ammo_Type|Bones [Indent level: 3],
            "Bones": {
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Main_Armament_Ammo_Type|Draw [Indent level: 3],
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Main_Armament_Ammo_Type|Draw|Gunner_AmmoType [Indent level: 4],
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
        # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Coax_Ammo [Indent level: 2],
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
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Coax_Ammo|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Coax_Ammo|Bones [Indent level: 3],
            "Bones": {
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Coax_Ammo|Draw [Indent level: 3],
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Coax_Ammo|Draw|Gunner_Text_1 [Indent level: 4],
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
        # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament [Indent level: 2],
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
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|Bones [Indent level: 3],
            "Bones": {
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|Draw [Indent level: 3],
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|Draw|Main_Armament_Ammo_Type_1 [Indent level: 4],
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
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|Draw|Gunner_Text_1 [Indent level: 4],
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
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|Draw|Main_Armament_Ammo_Type_2 [Indent level: 4],
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
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|Draw|Gunner_Text_2 [Indent level: 4],
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
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|Draw|Main_Armament_Ammo_Type_3 [Indent level: 4],
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
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|Draw|Gunner_Text_3 [Indent level: 4],
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
        # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Display [Indent level: 2],
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
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Display|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Display|Bones [Indent level: 3],
            "Bones": {
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Display|Draw [Indent level: 3],
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Display|Draw|Main_armament [Indent level: 4],
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
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Display|Draw|Machinegun [Indent level: 4],
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
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Display|Draw|Commander_machinegun [Indent level: 4],
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
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Display|Draw|Commander_armament [Indent level: 4],
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
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Display|Draw|Commander_armament_magazines [Indent level: 4],
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
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Display|Draw|Main_armament_ammo_type [Indent level: 4],
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
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Display|Draw|Lased_distance_elevation [Indent level: 4],
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
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Display|Draw|Azimut [Indent level: 4],
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
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Display|Draw|Damage [Indent level: 4],
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
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Display|Draw|Heading [Indent level: 4],
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
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Display|Draw|Lased_Range [Indent level: 4],
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
        # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Ready_To_Fire [Indent level: 2],
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
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Ready_To_Fire|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Ready_To_Fire|Bones [Indent level: 3],
            "Bones": {
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Ready_To_Fire|Draw [Indent level: 3],
            "Draw": {
                "color": [0,0,0],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Ready_To_Fire|Draw|Top_text [Indent level: 4],
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
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Ready_To_Fire|Draw|Bottom_text [Indent level: 4],
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
        # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Smoke_Indicator [Indent level: 2],
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
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Smoke_Indicator|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Smoke_Indicator|Bones [Indent level: 3],
            "Bones": {
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Smoke_Indicator|Draw [Indent level: 3],
            "Draw": {
                "color": [0,0,0],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Smoke_Indicator|Draw|Top_text [Indent level: 4],
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
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Smoke_Indicator|Draw|Bottom_text [Indent level: 4],
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
        # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Main_Armament_Ammo_Type [Indent level: 2],
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
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Main_Armament_Ammo_Type|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Main_Armament_Ammo_Type|Bones [Indent level: 3],
            "Bones": {
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Main_Armament_Ammo_Type|Draw [Indent level: 3],
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Main_Armament_Ammo_Type|Draw|Gunner_AmmoType [Indent level: 4],
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
        # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_AmmoIndicator_Main_Armament [Indent level: 2],
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
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_AmmoIndicator_Main_Armament|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_AmmoIndicator_Main_Armament|Bones [Indent level: 3],
            "Bones": {
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_AmmoIndicator_Main_Armament|Draw [Indent level: 3],
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_AmmoIndicator_Main_Armament|Draw|Main_Armament_Ammo_Type_1 [Indent level: 4],
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
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_AmmoIndicator_Main_Armament|Draw|Gunner_Text_1 [Indent level: 4],
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
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_AmmoIndicator_Main_Armament|Draw|Main_Armament_Ammo_Type_2 [Indent level: 4],
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
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_AmmoIndicator_Main_Armament|Draw|Gunner_Text_2 [Indent level: 4],
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
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_AmmoIndicator_Main_Armament|Draw|Main_Armament_Ammo_Type_3 [Indent level: 4],
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
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_AmmoIndicator_Main_Armament|Draw|Gunner_Text_3 [Indent level: 4],
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
        # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Coax_Ammo [Indent level: 2],
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
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Coax_Ammo|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Coax_Ammo|Bones [Indent level: 3],
            "Bones": {
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Coax_Ammo|Draw [Indent level: 3],
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Coax_Ammo|Draw|Gunner_Text_1 [Indent level: 4],
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
        # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Coax_Magazines [Indent level: 2],
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
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Coax_Magazines|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Coax_Magazines|Bones [Indent level: 3],
            "Bones": {
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Coax_Magazines|Draw [Indent level: 3],
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Coax_Magazines|Draw|Gunner_Text_1 [Indent level: 4],
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
        # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Second_Display [Indent level: 2],
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
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Second_Display|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Second_Display|Bones [Indent level: 3],
            "Bones": {
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Second_Display|Draw [Indent level: 3],
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Second_Display|Draw|Crosshair [Indent level: 4],
                "Crosshair": {
                    "type": "line",
                    "width": 3,
                    "points": [[[0.5,0.423413],1],[[0.5,0.346429],1],[],[[0.5,0.577381],1],[[0.5,0.654365],1],[],[[0.55,0.500397],1],[[0.6,0.500397],1],[],[[0.4,0.500397],1],[[0.45,0.500397],1],[],[[0.3,0.346429],1],[[0.3,0.269444],1],[],[[0.3,0.269444],1],[[0.35,0.269444],1],[],[[0.7,0.346429],1],[[0.7,0.269444],1],[],[[0.65,0.269444],1],[[0.7,0.269444],1],[],[[0.7,0.654365],1],[[0.7,0.731349],1],[],[[0.65,0.731349],1],[[0.7,0.731349],1],[],[[0.3,0.654365],1],[[0.3,0.731349],1],[],[[0.3,0.731349],1],[[0.35,0.731349],1],[]]
                },
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Second_Display|Draw|Heading [Indent level: 4],
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
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Second_Display|Draw|Lased_Range_Background [Indent level: 4],
                "Lased_Range_Background": {
                    "color": [0,0,0],
                    # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Second_Display|Draw|Lased_Range_Background|Background [Indent level: 5],
                    "Background": {
                        "type": "polygon",
                        "points": [[[[0.43,0.81],1],[[0.57,0.81],1],[[0.57,0.87],1],[[0.43,0.87],1]]]
                    }
                },
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Second_Display|Draw|Lased_Range [Indent level: 4],
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
    # Class: CfgVehicles|APC_Tracked_02_base_F|Library [Indent level: 1],
    "Library": {
        "libTextDesc": "The infantry fighting vehicle BTR-K Kamysh and its anti-aircraft cousin ZSU-39 Tigris share the same vehicle platform. Developed by Russia with a pinch of undeniable inspiration from Israeli IFVs, they serve in the OPFOR army as a prime example of a leveling of the technology field with the West. The Kamysh is equipped with a CTWS turret fitted with a 30 mm cannon, coaxial machinegun and 2 guided AT missiles, making the vehicle significant in the infantry support role. The Tigris is fitted with a 35 mm autocannon and 4 Titan AA missiles."
    },
    "editorSubcategory": "EdSubcat_APCs",
    "memoryPointTaskMarker": "TaskMarker_1_pos",
    "hideWeaponsDriver": 1,
    "hideWeaponsCargo": 1,
    "viewDriverShadowAmb": 0.5,
    "viewDriverShadowDiff": 0.05,
    "LODDriverOpticsIn": 1202,
    "driverInfoPanelCameraPos": "driverview_old",
    "driverLeftLegAnimName": "pedal_brake",
    "driverRightLegAnimName": "pedal_thrust",
    "crewExplosionProtection": 0.999,
    "threat": [0.8,0.6,0.6],
    "waterPPInVehicle": 0,
    "fireDustEffect": "emptyEffect",
    "animationSourceHatch": "",
    "soundLocked": ["|A3|Sounds_F|weapons|Rockets|locked_1",1,1],
    "soundIncommingMissile": ["|A3|Sounds_F|vehicles|air|noises|alarm_locked_by_missile_4",0.398107,1],
    # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights [Indent level: 1],
    "compartmentsLights": {
        # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights|Comp1 [Indent level: 2]
        "Comp1": {
            # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights|Comp1|Light1 [Indent level: 3]
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
                # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights|Comp1|Light1|Attenuation [Indent level: 4],
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
            # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights|Comp1|Light2 [Indent level: 3],
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
                # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights|Comp1|Light1|Attenuation [Indent level: 4],
                "Attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardLimitStart": 0.15,
                    "hardLimitEnd": 1.15
                }
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights|Comp1|Light3 [Indent level: 3],
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
                # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights|Comp1|Light1|Attenuation [Indent level: 4],
                "Attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardLimitStart": 0.15,
                    "hardLimitEnd": 1.15
                }
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights|Comp1|Light4 [Indent level: 3],
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
                # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights|Comp1|Light1|Attenuation [Indent level: 4],
                "Attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardLimitStart": 0.15,
                    "hardLimitEnd": 1.15
                }
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights|Comp1|Light5 [Indent level: 3],
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
                # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights|Comp1|Light1|Attenuation [Indent level: 4],
                "Attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardLimitStart": 0.15,
                    "hardLimitEnd": 1.15
                }
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights|Comp1|Light6 [Indent level: 3],
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
                # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights|Comp1|Light1|Attenuation [Indent level: 4],
                "Attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardLimitStart": 0.15,
                    "hardLimitEnd": 1.15
                }
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights|Comp1|Light7 [Indent level: 3],
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
                # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights|Comp1|Light1|Attenuation [Indent level: 4],
                "Attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardLimitStart": 0.15,
                    "hardLimitEnd": 1.15
                }
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights|Comp1|Light8 [Indent level: 3],
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
                # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights|Comp1|Light1|Attenuation [Indent level: 4],
                "Attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardLimitStart": 0.15,
                    "hardLimitEnd": 1.15
                }
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights|Comp1|Light9 [Indent level: 3],
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
                # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights|Comp1|Light1|Attenuation [Indent level: 4],
                "Attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardLimitStart": 0.15,
                    "hardLimitEnd": 1.15
                }
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights|Comp1|Light10 [Indent level: 3],
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
                # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights|Comp1|Light1|Attenuation [Indent level: 4],
                "Attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardLimitStart": 0.15,
                    "hardLimitEnd": 1.15
                }
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights|Comp1|Light11 [Indent level: 3],
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
                # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights|Comp1|Light1|Attenuation [Indent level: 4],
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
    "memoryPointCargoLight": "cargo light",
    "dampersBumpCoef": 4.5,
    "driveOnComponent": ["Track_L","Track_R","Slide"],
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
    # Class: CfgVehicles|Tank_F|CamShake [Indent level: 1],
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
    # Class: CfgVehicles|Tank_F|Components [Indent level: 1],
    "Components": {
        # Class: CfgVehicles|Tank_F|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 2]
        "VehicleSystemsDisplayManagerComponentLeft": {
            # Class: VehicleSystemsTemplateLeftDriver|Components [Indent level: 0]
            "Components": {
                # Class: VehicleSystemsTemplateLeftDriver|Components|VehiclePrimaryGunnerDisplay [Indent level: 1]
                "VehiclePrimaryGunnerDisplay": {
                    "componentType": "TransportFeedDisplayComponent",
                    "source": "PrimaryGunner"
                },
                # Class: VehicleSystemsTemplateLeftDriver|Components|VehicleCommanderDisplay [Indent level: 1],
                "VehicleCommanderDisplay": {
                    "componentType": "TransportFeedDisplayComponent",
                    "source": "Commander"
                },
                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|EmptyDisplay [Indent level: 1],
                "EmptyDisplay": {
                    "componentType": "EmptyDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|MinimapDisplay [Indent level: 1],
                "MinimapDisplay": {
                    "componentType": "MinimapDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|MineDetectorDisplay [Indent level: 1],
                "MineDetectorDisplay": {
                    "componentType": "MineDetectorDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|CrewDisplay [Indent level: 1],
                "CrewDisplay": {
                    "componentType": "CrewDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|UAVDisplay [Indent level: 1],
                "UAVDisplay": {
                    "componentType": "UAVFeedDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|SlingLoadDisplay [Indent level: 1],
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
        # Class: CfgVehicles|Tank_F|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 2],
        "VehicleSystemsDisplayManagerComponentRight": {
            # Class: VehicleSystemsTemplateRightDriver|Components [Indent level: 0]
            "Components": {
                # Class: VehicleSystemsTemplateRightDriver|Components|VehiclePrimaryGunnerDisplay [Indent level: 1]
                "VehiclePrimaryGunnerDisplay": {
                    "componentType": "TransportFeedDisplayComponent",
                    "source": "PrimaryGunner"
                },
                # Class: VehicleSystemsTemplateRightDriver|Components|VehicleCommanderDisplay [Indent level: 1],
                "VehicleCommanderDisplay": {
                    "componentType": "TransportFeedDisplayComponent",
                    "source": "Commander"
                },
                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|EmptyDisplay [Indent level: 1],
                "EmptyDisplay": {
                    "componentType": "EmptyDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|MinimapDisplay [Indent level: 1],
                "MinimapDisplay": {
                    "componentType": "MinimapDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|MineDetectorDisplay [Indent level: 1],
                "MineDetectorDisplay": {
                    "componentType": "MineDetectorDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|CrewDisplay [Indent level: 1],
                "CrewDisplay": {
                    "componentType": "CrewDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|UAVDisplay [Indent level: 1],
                "UAVDisplay": {
                    "componentType": "UAVFeedDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|SlingLoadDisplay [Indent level: 1],
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
        # Class: CfgVehicles|Tank_F|Components|AITankSteeringComponent [Indent level: 2],
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
        # Class: CfgVehicles|LandVehicle|Components|TransportCountermeasuresComponent [Indent level: 2],
        "TransportCountermeasuresComponent": {
        }
    },
    # Class: CfgVehicles|Tank_F|NVGMarkers [Indent level: 1],
    "NVGMarkers": {
        # Class: CfgVehicles|Tank_F|NVGMarkers|NVGMarker01 [Indent level: 2]
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
    "type": 1,
    "camouflage": 8,
    "driverOpticsColor": [1,1,1,1],
    # Class: CfgVehicles|Tank|CargoLight [Indent level: 1],
    "CargoLight": {
        "color": [0,0,0,0],
        "ambient": [0.6,0,0.15,1],
        "brightness": 0.007
    },
    "enableGPS": 1,
    "memoryPointTaskMarkerOffset": [0,0.3,0],
    "rightDustEffects": [["GdtKLDirt","RDustEffects"],["GdtKLGrass1","RDustEffects"],["GdtKLGrass1","RGrassEffects"],["GdtKLGrass2","RDustEffects"],["GdtKLGrass2","RGrassEffects"],["GdtKLForestCon","RDustEffects"],["GdtKLForestDec","RDustEffects"],["GdtKlMud","RDustEffects"],["GdtKlSoil","RDustEffects"],["GdtKlTarmac","RDustEffects"],["GdtKlStubble","RDustEffects"],["GdtKlStones","RStonesEffects"],["SurfRoadDirt_Enoch","RDustEffects"],["SurfTrailDirt_Enoch","RDustEffects"],["SurfRoadTarmac1_Enoch","RDustEffects"],["SurfRoadTarmac2_Enoch","RDustEffects"],["SurfRoadTarmac3_Enoch","RDustEffects"],["GdtGrassShort","RDustEffects"],["GdtGrassShort","RGrassEffectsBig"],["GdtGrassTall","RDustEffects"],["GdtGrassTall","RGrassEffectsBig"],["GdtRedDirt","RDustEffectsRed"],["GdtField","RDustEffects"],["GdtForest","RDustEffects"],["GdtVolcano","RDustEffects"],["GdtVolcano","RStonesEffectsBig"],["GdtCliff","RDustEffects"],["GdtVolcanoBeach","RDustEffects"],["SurfRoadDirt_exp","RDustEffectsRed"],["SurfRoadConcrete_exp","RDustEffects"],["SurfRoadTarmac_exp","RDustEffects"],["GdtStratisConcrete","RDustEffects"],["GdtStratisConcrete","RDirtEffectsBig"],["GdtStratisBeach","RDustEffects"],["GdtStratisBeach","RStonesEffectsBig"],["GdtStratisDirt","RDustEffects"],["GdtStratisDirt","RDirtEffectsBig"],["GdtStratisSeabedCluttered","RDustEffects"],["GdtStratisSeabed","RDustEffects"],["GdtStratisDryGrass","RDustEffects"],["GdtStratisDryGrass","RGrassEffectsDryBig"],["GdtStratisDryGrass","RDirtEffectsBig"],["GdtStratisGreenGrass","RDustEffects"],["GdtStratisGreenGrass","RGrassEffectsBig"],["GdtStratisGreenGrass","RDirtEffectsBig"],["GdtStratisRocky","RDustEffects"],["GdtStratisRocky","RGrassEffectsBig"],["GdtStratisRocky","RDirtEffectsBig"],["GdtStratisThistles","RDustEffects"],["GdtStratisThistles","RGrassEffectsBig"],["GdtStratisThistles","RDirtEffectsBig"],["GdtConcrete","RDustEffects"],["GdtConcrete","RDirtEffectsBig"],["GdtAsphalt","RDustEffects"],["GdtAsphalt","RDirtEffectsBig"],["GdtRubble","RDustEffects"],["GdtRubble","RDirtEffectsBig"],["GdtSoil","RDustEffects"],["GdtSoil","RDirtEffectsBig"],["GdtBeach","RDustEffects"],["GdtBeach","RStonesEffectsBig"],["GdtRock","RDustEffects"],["GdtRock","RDirtEffectsBig"],["GdtDead","RDustEffects"],["GdtDead","RDirtEffectsBig"],["Default","RDustEffects"],["GdtDesert","RDustEffects"],["GdtDesert","RDirtEffectsBig"],["GdtDesert","RStonesEffects"],["GdtDesert1","RDustEffects"],["GdtDesert1","RDirtEffectsBig"],["GdtDesert1","RStonesEffectsBig"],["GdtDesert2","RDustEffects"],["GdtDesert2","RGrassEffectsBig"],["GdtDesert2","RDirtEffectsBig"],["GdtDirt","RDustEffects"],["GdtDirt","RDirtEffectsBig"],["GdtGrassGreen","RDustEffects"],["GdtGrassGreen","RGrassEffectsBig"],["GdtGrassGreen","RDirtEffectsBig"],["GdtGrassDry","RDustEffects"],["GdtGrassDry","RGrassEffectsDryBig"],["GdtGrassDry","RDirtEffectsBig"],["GdtGrassWild","RDustEffects"],["GdtGrassWild","RGrassEffectsBig"],["GdtGrassWild","RDirtEffectsBig"],["GdtWildField","RDustEffects"],["GdtWildField","RGrassEffectsBig"],["GdtWildField","RDirtEffectsBig"],["GdtWeed1","RDustEffects"],["GdtWeed1","RGrassEffectsBig"],["GdtWeed1","RDirtEffectsBig"],["GdtWeed2","RDustEffects"],["GdtWeed2","RGrassEffectsBig"],["GdtWeed2","RDirtEffectsBig"],["GdtThorn","RDustEffects"],["GdtThorn","RGrassEffectsBig"],["GdtThorn","RDirtEffectsBig"],["GdtStony","RDustEffects"],["GdtStony","RGrassEffectsBig"],["GdtStony","RDirtEffectsBig"],["GdtStonyGreen","RDustEffects"],["GdtStonyGreen","RGrassEffectsBig"],["GdtStonyGreen","RDirtEffectsBig"],["GdtStonyThistle","RDustEffects"],["GdtStonyThistle","RGrassEffectsBig"],["GdtStonyThistle","RDirtEffectsBig"],["GdtSeabedDeep","RDustEffects"],["GdtSeabed","RDustEffects"],["SurfRoadDirt","RDustEffects"],["SurfRoadConcrete","RDustEffects"],["SurfRoadTarmac","RDustEffects"],["SurfWood","RDustEffects"],["SurfMetal","RDustEffects"],["SurfRoofTin","RDustEffects"],["SurfRoofTiles","RDustEffects"],["SurfIntWood","RDustEffects"],["SurfIntConcrete","RDustEffects"],["SurfIntTiles","RDustEffects"],["SurfIntMetal","RDustEffects"],["dirtrunway","RDustEffects"]],
    "leftDustEffects": [["GdtKLDirt","LDustEffects"],["GdtKLGrass1","LDustEffects"],["GdtKLGrass1","LGrassEffects"],["GdtKLGrass2","LDustEffects"],["GdtKLGrass2","LGrassEffects"],["GdtKLForestCon","LDustEffects"],["GdtKLForestDec","LDustEffects"],["GdtKlMud","LDustEffects"],["GdtKlSoil","LDustEffects"],["GdtKlTarmac","LDustEffects"],["GdtKlStubble","LDustEffects"],["GdtKlStones","LStonesEffects"],["SurfRoadDirt_Enoch","LDustEffects"],["SurfTrailDirt_Enoch","LDustEffects"],["SurfRoadTarmac1_Enoch","LDustEffects"],["SurfRoadTarmac2_Enoch","LDustEffects"],["SurfRoadTarmac3_Enoch","LDustEffects"],["GdtGrassShort","LDustEffects"],["GdtGrassShort","LGrassEffectsBig"],["GdtGrassTall","LDustEffects"],["GdtGrassTall","LGrassEffectsBig"],["GdtRedDirt","LDustEffectsRed"],["GdtField","LDustEffects"],["GdtForest","LDustEffects"],["GdtVolcano","LDustEffects"],["GdtVolcano","LStonesEffectsBig"],["GdtCliff","LDustEffects"],["GdtVolcanoBeach","LDustEffects"],["SurfRoadDirt_exp","LDustEffectsRed"],["SurfRoadConcrete_exp","LDustEffects"],["SurfRoadTarmac_exp","LDustEffects"],["GdtStratisConcrete","LDustEffects"],["GdtStratisConcrete","LDirtEffectsBig"],["GdtStratisBeach","LDustEffects"],["GdtStratisBeach","LStonesEffectsBig"],["GdtStratisDirt","LDustEffects"],["GdtStratisDirt","LDirtEffectsBig"],["GdtStratisSeabedCluttered","LDustEffects"],["GdtStratisSeabed","LDustEffects"],["GdtStratisDryGrass","LDustEffects"],["GdtStratisDryGrass","LGrassEffectsDryBig"],["GdtStratisDryGrass","LDirtEffectsBig"],["GdtStratisGreenGrass","LDustEffects"],["GdtStratisGreenGrass","LGrassEffectsBig"],["GdtStratisGreenGrass","LDirtEffectsBig"],["GdtStratisRocky","LDustEffects"],["GdtStratisRocky","LGrassEffectsBig"],["GdtStratisRocky","LDirtEffectsBig"],["GdtStratisThistles","LDustEffects"],["GdtStratisThistles","LGrassEffectsBig"],["GdtStratisThistles","LDirtEffectsBig"],["GdtConcrete","LDustEffects"],["GdtConcrete","LDirtEffectsBig"],["GdtAsphalt","LDustEffects"],["GdtAsphalt","LDirtEffectsBig"],["GdtRubble","LDustEffects"],["GdtRubble","LGrassEffectsBig"],["GdtRubble","LDirtEffectsBig"],["GdtSoil","LDustEffects"],["GdtSoil","LDirtEffectsBig"],["GdtBeach","LDustEffects"],["GdtBeach","LStonesEffectsBig"],["GdtRock","LDustEffects"],["GdtRock","LDirtEffectsBig"],["GdtDead","LDustEffects"],["GdtDead","LDirtEffectsBig"],["Default","LDustEffects"],["GdtDesert","LDustEffects"],["GdtDesert","LDirtEffectsBig"],["GdtDesert","LStonesEffects"],["GdtDesert1","LDustEffects"],["GdtDesert1","LDirtEffectsBig"],["GdtDesert1","LStonesEffectsBig"],["GdtDesert2","LDustEffects"],["GdtDesert2","LGrassEffectsBig"],["GdtDesert2","LDirtEffectsBig"],["GdtDirt","LDustEffects"],["GdtDirt","LDirtEffectsBig"],["GdtGrassGreen","LDustEffects"],["GdtGrassGreen","LGrassEffectsBig"],["GdtGrassGreen","LDirtEffectsBig"],["GdtGrassDry","LDustEffects"],["GdtGrassDry","LGrassEffectsDryBig"],["GdtGrassDry","LDirtEffectsBig"],["GdtGrassWild","LDustEffects"],["GdtGrassWild","LGrassEffectsBig"],["GdtGrassWild","LDirtEffectsBig"],["GdtWildField","LDustEffects"],["GdtWildField","LGrassEffectsBig"],["GdtWildField","LDirtEffectsBig"],["GdtWeed1","LDustEffects"],["GdtWeed1","LGrassEffectsBig"],["GdtWeed1","LDirtEffectsBig"],["GdtWeed2","LDustEffects"],["GdtWeed2","LGrassEffectsBig"],["GdtWeed2","LDirtEffectsBig"],["GdtThorn","LDustEffects"],["GdtThorn","LGrassEffectsBig"],["GdtThorn","LDirtEffectsBig"],["GdtStony","LDustEffects"],["GdtStony","LGrassEffectsBig"],["GdtStony","LDirtEffectsBig"],["GdtStonyGreen","LDustEffects"],["GdtStonyGreen","LGrassEffectsBig"],["GdtStonyGreen","LDirtEffectsBig"],["GdtStonyThistle","LDustEffects"],["GdtStonyThistle","LGrassEffectsBig"],["GdtStonyThistle","LDirtEffectsBig"],["GdtSeabedDeep","LDustEffects"],["GdtSeabed","LDustEffects"],["SurfRoadDirt","LDustEffects"],["SurfRoadConcrete","LDustEffects"],["SurfRoadTarmac","LDustEffects"],["SurfWood","LDustEffects"],["SurfMetal","LDustEffects"],["SurfRoofTin","LDustEffects"],["SurfRoofTiles","LDustEffects"],["SurfIntWood","LDustEffects"],["SurfIntConcrete","LDustEffects"],["SurfIntTiles","LDustEffects"],["SurfIntMetal","LDustEffects"],["dirtrunway","RDustEffects"]],
    # Class: CfgVehicles|Tank|DestructionEffects [Indent level: 1],
    "DestructionEffects": {
        # Class: CfgVehicles|Tank|DestructionEffects|LightBig1 [Indent level: 2]
        "LightBig1": {
            "simulation": "light",
            "type": "ObjectDestructionLight",
            "position": "destructionEffect1",
            "intensity": 0.001,
            "interval": 1,
            "lifeTime": 3,
            "enabled": "distToWater"
        },
        # Class: CfgVehicles|Tank|DestructionEffects|Sound [Indent level: 2],
        "Sound": {
            "simulation": "sound",
            "position": "destructionEffect1",
            "intensity": 1,
            "interval": 1,
            "lifeTime": 1,
            "type": "Fire"
        },
        # Class: CfgVehicles|Tank|DestructionEffects|FireBig1 [Indent level: 2],
        "FireBig1": {
            "simulation": "particles",
            "type": "ObjectDestructionFire1",
            "position": "destructionEffect1",
            "intensity": 0.15,
            "interval": 1,
            "lifeTime": 3
        },
        # Class: CfgVehicles|Tank|DestructionEffects|Refract1 [Indent level: 2],
        "Refract1": {
            "simulation": "particles",
            "type": "ObjectDestructionRefract",
            "position": "destructionEffect1",
            "intensity": 0.15,
            "interval": 1,
            "lifeTime": 3
        },
        # Class: CfgVehicles|Tank|DestructionEffects|SmokeBig1 [Indent level: 2],
        "SmokeBig1": {
            "simulation": "particles",
            "type": "ObjectDestructionSmoke",
            "position": "destructionEffect1",
            "intensity": 0.15,
            "interval": 1,
            "lifeTime": 3.5
        },
        # Class: CfgVehicles|Tank|DestructionEffects|SparksBig1 [Indent level: 2],
        "SparksBig1": {
            "simulation": "particles",
            "type": "ObjectDestructionSparks",
            "position": "destructionEffect1",
            "intensity": 0,
            "interval": 1,
            "lifeTime": 0
        },
        # Class: CfgVehicles|Tank|DestructionEffects|FireSparksBig1 [Indent level: 2],
        "FireSparksBig1": {
            "simulation": "particles",
            "type": "FireSparks",
            "position": "destructionEffect2",
            "intensity": 1,
            "interval": 1,
            "lifeTime": 2.8
        },
        # Class: CfgVehicles|Tank|DestructionEffects|FireBig2 [Indent level: 2],
        "FireBig2": {
            "simulation": "particles",
            "type": "ObjectDestructionFire2",
            "position": "destructionEffect2",
            "intensity": 0.15,
            "interval": 1,
            "lifeTime": 3
        },
        # Class: CfgVehicles|Tank|DestructionEffects|SmokeBig1_2 [Indent level: 2],
        "SmokeBig1_2": {
            "simulation": "particles",
            "type": "ObjectDestructionSmoke1_2",
            "position": "destructionEffect2",
            "intensity": 0.15,
            "interval": 1,
            "lifeTime": 3.5
        },
        # Class: CfgVehicles|Tank|DestructionEffects|SmokeBig2 [Indent level: 2],
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
                # Class: WeaponFireGun|Table|T0 [Indent level: 1]
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
                # Class: WeaponCloudsGun|Table|T0 [Indent level: 1]
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
                # Class: WeaponCloudsMGun|Table|T0 [Indent level: 1]
                "T0": {
                    "maxT": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|HitPoints [Indent level: 2],
        "HitPoints": {
            # Class: CfgVehicles|AllVehicles|NewTurret|HitPoints|HitTurret [Indent level: 3]
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
    "wheelDamageThreshold": 0.2,
    "wheelDestroyThreshold": 0.99,
    "wheelDamageRadiusCoef": 0.9,
    "wheelDestroyRadiusCoef": 0.4,
    "weaponsGroup1": 1,
    "weaponsGroup2": "2 + 		4",
    "weaponsGroup3": "8 + 	16 + 	32",
    "weaponsGroup4": "64 + 		128",
    # Class: CfgVehicles|AllVehicles|SquadTitles [Indent level: 1],
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
    # Class: CfgVehicles|AllVehicles|NewTurret [Indent level: 1],
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
                # Class: WeaponFireGun|Table|T0 [Indent level: 1]
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
                # Class: WeaponCloudsGun|Table|T0 [Indent level: 1]
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
                # Class: WeaponCloudsMGun|Table|T0 [Indent level: 1]
                "T0": {
                    "maxT": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|HitPoints [Indent level: 2],
        "HitPoints": {
            # Class: CfgVehicles|AllVehicles|NewTurret|HitPoints|HitTurret [Indent level: 3]
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
    # Class: CfgVehicles|AllVehicles|PilotSpec [Indent level: 1],
    "PilotSpec": {
        "showHeadPhones": 0
    },
    # Class: CfgVehicles|AllVehicles|CargoSpec [Indent level: 1],
    "CargoSpec": {
        # Class: CfgVehicles|AllVehicles|CargoSpec|Cargo1 [Indent level: 2]
        "Cargo1": {
            "showHeadPhones": 0
        }
    },
    # Class: CfgVehicles|AllVehicles|SoundEvents [Indent level: 1],
    "SoundEvents": {
    },
    "hasTerminal": 0,
    "getInOutOnProxy": 0,
    "preciseGetInOut": 0,
    "cargoPreciseGetInOut": [0],
    "availableForSupportTypes": [],
    "impactEffectsSea": "ImpactEffectsSea",
    "impactEffectSpeedLimit": 8,
    "showCrewAim": 0,
    # Class: CfgVehicles|AllVehicles|CargoTurret [Indent level: 1],
    "CargoTurret": {
        # Class: CfgVehicles|AllVehicles|CargoTurret|ViewGunner [Indent level: 2]
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
                # Class: WeaponFireGun|Table|T0 [Indent level: 1]
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
                # Class: WeaponCloudsGun|Table|T0 [Indent level: 1]
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
                # Class: WeaponCloudsMGun|Table|T0 [Indent level: 1]
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
    "irTarget": 1,
    "laserTarget": 0,
    "laserScanner": 0,
    "nvTarget": 0,
    "nvScanner": 0,
    "artilleryTarget": 0,
    "artilleryScanner": 0,
    "canUseScanners": 1,
    "preferRoads": 0,
    "unitInfoType": "RscUnitInfoTank",
    "unitInfoTypeLite": 0,
    "hideUnitInfo": 0,
    "radarType": 0,
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
    "soundEngine": ["",1,1],
    "soundEnviron": ["",1,1],
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
            # Class: WeaponFireGun|Table|T0 [Indent level: 1]
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
            # Class: WeaponCloudsGun|Table|T0 [Indent level: 1]
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
            # Class: WeaponCloudsMGun|Table|T0 [Indent level: 1]
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
    "slingLoadCargoMemoryPointsDir": [],
    "damageHalf": [],
    "damageFull": [],
    # Class: CfgVehicles|All|camShakeGForce [Indent level: 1],
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
    # Class: CfgVehicles|All|camShakeDamage [Indent level: 1],
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