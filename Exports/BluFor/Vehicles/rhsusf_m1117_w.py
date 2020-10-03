rhsusf_m1117_w = {
    "editorPreview": "rhsusf|addons|rhsusf_editorPreviews|data|rhsusf_M1117_W.paa",
    "author": "Cleggy",
    "dlc": "RHS_USAF",
    "category": "Car",
    "faction": "rhs_faction_usarmy_wd",
    "hiddenSelectionsTextures": ["rhsusf|addons|rhsusf_m1117|data|m1117_tex1_green_co.paa","rhsusf|addons|rhsusf_m1117|data|m1117_armour_green_co.paa","rhsusf|addons|rhsusf_m1117|data|m1117_turret_green_co.paa","rhsusf|addons|rhsusf_m1117|data|m1117_wheel_green_co.paa","rhsusf|addons|rhsusf_hmmwv|textures|A2_parts_g_co.paa","rhsusf|addons|rhsusf_m1a1|duke|data|duke_antennae_wd_co.paa"],
    "scope": 2,
    "scopeCurator": 2,
    "side": 1,
    "crew": "rhsusf_army_ucp_rifleman_m4",
    "typicalCargo": ["rhsusf_army_ucp_rifleman_m4"],
    "hiddenSelections": ["camo1","camo2","camo3","camo4","camo5","camo6"],
    "rhs_duke_type": "rhsusf_duke",
    "vehicleClass": "rhs_vehclass_MRAP",
    "editorSubcategory": "rhs_EdSubcat_mrap",
    # Class: CfgVehicles\rhsusf_M1117_base\SpeechVariants,
    "SpeechVariants": {
        # Class: CfgVehicles\rhsusf_M1117_base\SpeechVariants\Default
        "Default": {
            "speechSingular": ["veh_vehicle_MRAP_s"],
            "speechPlural": ["veh_vehicle_MRAP_p"]
        }
    },
    "textSingular": "MRAP",
    "textPlural": "MRAPs",
    "nameSound": "veh_vehicle_MRAP_s",
    "displayName": "M1117 ASV",
    "model": "rhsusf|addons|rhsusf_m1117|blx_M1117",
    "picture": "rhsusf|addons|rhsusf_m1117|data|UI|picture_m1117_ca.paa",
    "Icon": "rhsusf|addons|rhsusf_m1117|data|UI|icon_m1117_ca.paa",
    "mapSize": 6,
    "unitInfoType": "RHS_RscUnitInfoM1117",
    "radarType": 8,
    "driverCanSee": "2+4+16",
    "gunnerCanSee": "2+4+16",
    "commanderCanSee": "2+4+16",
    "enableManualFire": 0,
    "transportSoldier": 4,
    "cargoProxyIndexes": [1],
    "cost": 600000,
    "threat": [1,0.8,0.3],
    "incomingMissileDetectionSystem": 0,
    "normalSpeedForwardCoef": 0.7,
    "slownSpeedForwardCoef": 0.55,
    "turnCoef": 3,
    "terrainCoef": 2,
    "simulation": "carx",
    "dampersBumpCoef": 0,
    "maxSpeed": 100,
    "fuelCapacity": 35,
    "wheelCircumference": 3.65671,
    "brakeIdleSpeed": 2,
    "canFloat": 0,
    "maxFordingDepth": 0,
    "waterSpeedFactor": 0.1,
    "waterResistance": 1,
    "waterResistanceCoef": 0.3,
    "waterLeakiness": 20,
    # Class: CfgVehicles\rhsusf_M1117_base\complexGearbox,
    "complexGearbox": {
        "GearboxRatios": ["R1",-5.03,"N",0,"D1",3.49,"D2",1.86,"D3",1.41,"D4",1,"D5",0.75,"D6",0.6],
        "TransmissionRatios": ["High",6.9],
        "gearBoxMode": "auto",
        "moveOffGear": 1,
        "driveString": "D",
        "neutralString": "N",
        "reverseString": "R"
    },
    "changeGearMinEffectivity": [0.95,0,0.95,0.95,0.95,0.9,0.9,0.45],
    "switchTime": 0.5,
    "latency": 1,
    "differentialType": "all_limited",
    "frontRearSplit": 0.5,
    "frontBias": 1.3,
    "rearBias": 1.3,
    "centreBias": 1.3,
    "clutchStrength": 55,
    "dampingRateFullThrottle": 0.15,
    "dampingRateZeroThrottleClutchEngaged": 0.8,
    "dampingRateZeroThrottleClutchDisengaged": 0.35,
    "torqueCurve": [[0.454545,0.63348],[0.5,0.856388],[0.590909,0.987665],[0.681818,1],[0.772727,0.959471],[0.863636,0.864317],[0.954545,0.781498],[1.05409,0]],
    "engineMOI": 5,
    "enginePower": 194,
    "peakTorque": 1135,
    "minOmega": 66,
    "maxOmega": 230.38,
    "idleRPM": 1000,
    "redRPM": 2200,
    "thrustDelay": 0.8,
    "engineLosses": 15,
    "engineBrakeCoef": 0.8,
    "antiRollbarForceCoef": 0.5,
    "antiRollbarForceLimit": 0.5,
    "antiRollbarSpeedMin": 10,
    "antiRollbarSpeedMax": 50,
    "accelAidForceSpd": 2.23,
    "accelAidForceCoef": 3,
    "accelAidForceYOffset": -1.3,
    # Class: CfgVehicles\rhsusf_M1117_base\Wheels,
    "Wheels": {
        # Class: CfgVehicles\rhsusf_M1117_base\Wheels\LF
        "LF": {
            "side": "left",
            "boneName": "wheel_1_1",
            "center": "wheel_1_1_axis",
            "boundary": "wheel_1_1_bound",
            "suspForceAppPointOffset": "wheel_1_1_axis",
            "tireForceAppPointOffset": "wheel_1_1_axis",
            "suspTravelDirection": [-0.125,-1,0],
            "steering": 1,
            "width": 0.35,
            "mass": 80,
            "MOI": 14.4,
            "dampingRate": 1,
            "dampingRateInAir": 1,
            "dampingRateDamaged": 1.5,
            "dampingRateDestroyed": 1000,
            "maxBrakeTorque": 26000,
            "maxHandBrakeTorque": 0,
            "maxCompression": 0.2,
            "maxDroop": 0.2,
            "sprungMass": -1,
            "springStrength": 178578,
            "springDamperRate": 17000,
            "longitudinalStiffnessPerUnitGravity": 13000,
            "latStiffX": 35,
            "latStiffY": 180,
            "frictionVsSlipGraph": [[0,1],[0.5,1],[1,1]]
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Wheels\LR,
        "LR": {
            "boneName": "wheel_1_2",
            "center": "wheel_1_2_axis",
            "boundary": "wheel_1_2_bound",
            "suspForceAppPointOffset": "wheel_1_2_axis",
            "tireForceAppPointOffset": "wheel_1_2_axis",
            "maxHandBrakeTorque": 40000,
            "steering": 0,
            "side": "left",
            "suspTravelDirection": [-0.125,-1,0],
            "width": 0.35,
            "mass": 80,
            "MOI": 14.4,
            "dampingRate": 1,
            "dampingRateInAir": 1,
            "dampingRateDamaged": 1.5,
            "dampingRateDestroyed": 1000,
            "maxBrakeTorque": 26000,
            "maxCompression": 0.2,
            "maxDroop": 0.2,
            "sprungMass": -1,
            "springStrength": 178578,
            "springDamperRate": 17000,
            "longitudinalStiffnessPerUnitGravity": 13000,
            "latStiffX": 35,
            "latStiffY": 180,
            "frictionVsSlipGraph": [[0,1],[0.5,1],[1,1]]
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Wheels\RF,
        "RF": {
            "side": "right",
            "boneName": "wheel_2_1",
            "center": "wheel_2_1_axis",
            "boundary": "wheel_2_1_bound",
            "suspForceAppPointOffset": "wheel_2_1_axis",
            "tireForceAppPointOffset": "wheel_2_1_axis",
            "suspTravelDirection": [0.125,-1,0],
            "steering": 1,
            "width": 0.35,
            "mass": 80,
            "MOI": 14.4,
            "dampingRate": 1,
            "dampingRateInAir": 1,
            "dampingRateDamaged": 1.5,
            "dampingRateDestroyed": 1000,
            "maxBrakeTorque": 26000,
            "maxHandBrakeTorque": 0,
            "maxCompression": 0.2,
            "maxDroop": 0.2,
            "sprungMass": -1,
            "springStrength": 178578,
            "springDamperRate": 17000,
            "longitudinalStiffnessPerUnitGravity": 13000,
            "latStiffX": 35,
            "latStiffY": 180,
            "frictionVsSlipGraph": [[0,1],[0.5,1],[1,1]]
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Wheels\RR,
        "RR": {
            "boneName": "wheel_2_2",
            "center": "wheel_2_2_axis",
            "boundary": "wheel_2_2_bound",
            "suspForceAppPointOffset": "wheel_2_2_axis",
            "tireForceAppPointOffset": "wheel_2_2_axis",
            "maxHandBrakeTorque": 40000,
            "steering": 0,
            "side": "right",
            "suspTravelDirection": [0.125,-1,0],
            "width": 0.35,
            "mass": 80,
            "MOI": 14.4,
            "dampingRate": 1,
            "dampingRateInAir": 1,
            "dampingRateDamaged": 1.5,
            "dampingRateDestroyed": 1000,
            "maxBrakeTorque": 26000,
            "maxCompression": 0.2,
            "maxDroop": 0.2,
            "sprungMass": -1,
            "springStrength": 178578,
            "springDamperRate": 17000,
            "longitudinalStiffnessPerUnitGravity": 13000,
            "latStiffX": 35,
            "latStiffY": 180,
            "frictionVsSlipGraph": [[0,1],[0.5,1],[1,1]]
        }
    },
    "tf_RadioType_api": "tf_rt1523g",
    "tf_hasLRradio_api": 1,
    "tf_isolatedAmount_api": 0.2,
    "rhs_hasSmokeCap": 1,
    "htMin": 60,
    "htMax": 600,
    "afMax": 200,
    "mfMax": 100,
    "mFact": 1,
    "tBody": 150,
    "damperSize": 0.1,
    "damperForce": 0.1,
    "damperDamping": 0.1,
    "steerAheadSimul": 0.55,
    "steerAheadPlan": 0.2,
    "predictTurnSimul": 4.4,
    "predictTurnPlan": 0.5,
    "precision": 15,
    "crewVulnerable": 1,
    "crewCrashProtection": 0.15,
    # Class: CfgVehicles\rhsusf_M1117_base\Library,
    "Library": {
        "libTextDesc": "M1117_Guardian ASV"
    },
    "armor": 150,
    "armorStructural": 8,
    "weapons": ["TruckHorn"],
    "magazines": [],
    "damageResistance": 0.03099,
    "destrType": "DestructWreck",
    "selectionDamage": "zbytek",
    "enableGPS": 1,
    # Class: CfgVehicles\rhsusf_M1117_base\Damage,
    "Damage": {
        "tex": [],
        "mat": ["rhsusf|addons|rhsusf_m1117|data|m1117_tex1.rvmat","rhsusf|addons|rhsusf_m1117|data|m1117_tex1_damage.rvmat","rhsusf|addons|rhsusf_m1117|data|m1117_tex1_damage.rvmat","rhsusf|addons|rhsusf_m1117|data|m1117_armour.rvmat","rhsusf|addons|rhsusf_m1117|data|m1117_armour_damage.rvmat","rhsusf|addons|rhsusf_m1117|data|m1117_armour_damage.rvmat","rhsusf|addons|rhsusf_m1117|data|m1117_turret.rvmat","rhsusf|addons|rhsusf_m1117|data|m1117_turret_damage.rvmat","rhsusf|addons|rhsusf_m1117|data|m1117_turret_damage.rvmat","rhsusf|addons|rhsusf_m1117|data|m1117_wheel.rvmat","rhsusf|addons|rhsusf_m1117|data|m1117_wheel_damage.rvmat","rhsusf|addons|rhsusf_m1117|data|m1117_wheel_damage.rvmat","rhsusf|addons|rhsusf_m1117|data|periscope_int_damage.rvmat","rhsusf|addons|rhsusf_m1117|data|periscope_int_destroyed.rvmat","rhsusf|addons|rhsusf_m1117|data|periscope_int_destroyed.rvmat","rhsusf|addons|rhsusf_m1117|data|glassz.rvmat","a3|data_f|glass_veh_armored_damage.rvmat","a3|data_f|glass_veh_armored_damage.rvmat","a3|data_f|glass_veh_int.rvmat","a3|data_f|glass_veh_armored_damage.rvmat","a3|data_f|glass_veh_armored_damage.rvmat"]
    },
    "forceHideDriver": 0,
    "hideProxyInCombat": 0,
    "driverCompartments": "Compartment1",
    "cargoCompartments": ["Compartment1"],
    "driverAction": "rhs_M1117_Driver",
    "driverInAction": "rhs_M1117_Driver",
    "cargoAction": ["rhs_M1117_passenger","passenger_flatground_generic01","passenger_low01","passenger_flatground_crosslegs"],
    "getInAction": "GetInAMV_cargo",
    "getOutAction": "GetOutLow",
    "cargoGetInAction": ["GetInAMV_cargo"],
    "cargoGetOutAction": ["GetOutLow"],
    "driverDoor": "door_l",
    "cargoDoors": ["door_r","door_b","door_l","door_r"],
    "memoryPointsGetInCargo": ["pos gunner","pos cargo b","pos cargo","pos gunner"],
    "memoryPointsGetInCargoDir": ["pos gunner dir","pos cargo b dir","pos cargo dir","pos gunner dir"],
    "hideWeaponsDriver": 1,
    "hideWeaponsGunner": 1,
    "hideWeaponsCargo": 1,
    "extCameraPosition": [0,2,-9],
    "driverForceOptics": 0,
    "castDriverShadow": 0,
    "viewDriverShadow": 1,
    "viewCargoShadow": 1,
    "viewGunnerShadow": 1,
    "driveropticsmodel": "rhsusf|addons|rhsusf_m1117|optics|driver_optic",
    "memoryPointDriverOptics": "driverview",
    "slingLoadCargoMemoryPoints": ["SlingLoadCargo1","SlingLoadCargo2","SlingLoadCargo3","SlingLoadCargo4"],
    # Class: CfgVehicles\rhsusf_M1117_base\ViewPilot,
    "ViewPilot": {
        "initAngleX": -4.5,
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
    # Class: CfgVehicles\rhsusf_M1117_base\ViewOptics,
    "ViewOptics": {
        "initFov": 0.8,
        "minFov": 0.8,
        "maxFov": 0.8,
        "initAngleX": 0,
        "minAngleX": -45,
        "maxAngleX": 30,
        "initAngleY": 0,
        "minAngleY": -90,
        "maxAngleY": 90,
        "visionMode": ["Normal"],
        "thermalMode": [0,1],
        "minMoveX": 0,
        "maxMoveX": 0,
        "minMoveY": 0,
        "maxMoveY": 0,
        "minMoveZ": 0,
        "maxMoveZ": 0,
        "speedZoomMaxSpeed": 1e+010,
        "speedZoomMaxFOV": 0
    },
    # Class: CfgVehicles\rhsusf_M1117_base\Turrets,
    "Turrets": {
        # Class: CfgVehicles\rhsusf_M1117_base\Turrets\MainTurret
        "MainTurret": {
            "gunnerType": "rhsusf_army_ucp_grenadier",
            "proxyType": "CPGunner",
            "proxyIndex": 1,
            "commanding": -1,
            "primaryGunner": 1,
            "primaryObserver": 0,
            "gunnerName": "Gunner",
            "gunnerCompartments": "Compartment1",
            "gunnerDoor": "door_r",
            "hasGunner": 1,
            "gunnerGetInAction": "GetInAMV_cargo",
            "gunnerGetOutAction": "GetOutLow",
            "memoryPointsGetInGunner": "pos gunner",
            "memoryPointsGetInGunnerDir": "pos gunner dir",
            "weapons": ["RHS_M2_M1117","RHS_MK19","rhsusf_weap_M257_8"],
            "magazines": ["rhs_mag_200rnd_127x99_mag_Tracer_Red","rhs_mag_200rnd_127x99_mag_Tracer_Red","rhs_mag_200rnd_127x99_mag_Tracer_Red","rhs_mag_200rnd_127x99_mag_Tracer_Red","rhs_mag_200rnd_127x99_mag_Tracer_Red","RHS_96Rnd_40mm_MK19_M430A1","RHS_96Rnd_40mm_MK19_M430A1","RHS_96Rnd_40mm_MK19_M430A1","RHS_96Rnd_40mm_MK19_M430A1","RHS_96Rnd_40mm_MK19_M430A1","RHS_96Rnd_40mm_MK19_M430A1","RHS_96Rnd_40mm_MK19_M1001","rhsusf_mag_L8A3_8"],
            "soundServo": ["A3|sounds_f|dummysound","db-35",1,15],
            "minElev": -5,
            "maxElev": 60,
            "initElev": 0,
            "minTurn": -360,
            "maxTurn": 360,
            "initTurn": 0,
            "gunnerAction": "rhs_M1117_Gunner",
            "gunnerInAction": "rhs_M1117_Gunner",
            "canHideGunner": 0,
            "forceHideGunner": 0,
            "gunnerOpticsModel": "A3|weapons_f|reticle|Optics_Gunner_02_F",
            "gunnerOutOpticsModel": "",
            "memoryPointGunnerOptics": "gunnerview",
            "memoryPointGunnerOutOptics": "gunnerview",
            "discreteDistance": [],
            "discreteDistanceInitIndex": 0,
            "turretInfoType": "RscWeaponZeroing",
            "canUseScanners": 0,
            "allowTabLock": 0,
            "memoryPointGun": "kulas",
            "selectionFireAnim": "zasleh",
            "gunBeg": "usti hlavne",
            "gunEnd": "konec hlavne",
            "body": "MainTurret",
            "gun": "MainGun",
            "animationSourceBody": "MainTurret",
            "animationSourceGun": "MainGun",
            "gunnerForceOptics": 0,
            "outGunnerMayFire": 1,
            "inGunnerMayFire": 1,
            "gunnerFireAlsoInInternalCamera": 1,
            "viewGunnerInExternal": 1,
            "startEngine": 0,
            "stabilizedInAxes": 3,
            # Class: CfgVehicles\rhsusf_M1117_base\Turrets\MainTurret\ViewOptics,
            "ViewOptics": {
                "visionMode": ["Normal","TI"],
                "thermalMode": [2,3],
                "initAngleX": 0,
                "minAngleX": -30,
                "maxAngleX": "+30",
                "initAngleY": 0,
                "minAngleY": -100,
                "maxAngleY": "+100",
                "initFov": 0.4,
                "minFov": 0.2,
                "maxFov": 0.4,
                "minMoveX": 0,
                "maxMoveX": 0,
                "minMoveY": 0,
                "maxMoveY": 0,
                "minMoveZ": 0,
                "maxMoveZ": 0
            },
            # Class: CfgVehicles\rhsusf_M1117_base\Turrets\MainTurret\OpticsIn,
            "OpticsIn": {
                # Class: CfgVehicles\rhsusf_M1117_base\Turrets\MainTurret\OpticsIn\Periscope
                "Periscope": {
                    "initFov": 0.466667,
                    "minFov": 0.466667,
                    "maxFov": 0.466667,
                    "gunnerOpticsModel": "rhsusf|addons|rhsusf_optics|data|rhs_periscope_BISType",
                    "visionMode": ["Normal"],
                    "thermalMode": [2,3],
                    "initAngleX": 0,
                    "minAngleX": -30,
                    "maxAngleX": "+30",
                    "initAngleY": 0,
                    "minAngleY": -100,
                    "maxAngleY": "+100",
                    "minMoveX": 0,
                    "maxMoveX": 0,
                    "minMoveY": 0,
                    "maxMoveY": 0,
                    "minMoveZ": 0,
                    "maxMoveZ": 0
                },
                # Class: CfgVehicles\rhsusf_M1117_base\Turrets\MainTurret\OpticsIn\Wide,
                "Wide": {
                    "initFov": 0.233333,
                    "minFov": 0.233333,
                    "maxFov": 0.233333,
                    "gunnerOpticsModel": "rhsusf|addons|rhsusf_m1117|optics|rhs_m36_wide",
                    "visionMode": ["Normal","TI"],
                    "thermalMode": [2,3],
                    "initAngleX": 0,
                    "minAngleX": -30,
                    "maxAngleX": "+30",
                    "initAngleY": 0,
                    "minAngleY": -100,
                    "maxAngleY": "+100",
                    "minMoveX": 0,
                    "maxMoveX": 0,
                    "minMoveY": 0,
                    "maxMoveY": 0,
                    "minMoveZ": 0,
                    "maxMoveZ": 0
                },
                # Class: CfgVehicles\rhsusf_M1117_base\Turrets\MainTurret\OpticsIn\Narrow,
                "Narrow": {
                    "initFov": 0.1,
                    "minFov": 0.1,
                    "maxFov": 0.1,
                    "gunnerOpticsModel": "rhsusf|addons|rhsusf_m1117|optics|rhs_m36_narrow",
                    "visionMode": ["Normal","TI"],
                    "thermalMode": [2,3],
                    "initAngleX": 0,
                    "minAngleX": -30,
                    "maxAngleX": "+30",
                    "initAngleY": 0,
                    "minAngleY": -100,
                    "maxAngleY": "+100",
                    "minMoveX": 0,
                    "maxMoveX": 0,
                    "minMoveY": 0,
                    "maxMoveY": 0,
                    "minMoveZ": 0,
                    "maxMoveZ": 0
                }
            },
            # Class: CfgVehicles\rhsusf_M1117_base\Turrets\MainTurret\HitPoints,
            "HitPoints": {
                # Class: CfgVehicles\rhsusf_M1117_base\Turrets\MainTurret\HitPoints\HitTurret
                "HitTurret": {
                    "armor": 1.5,
                    "material": -1,
                    "name": "vez",
                    "visual": "otocvez",
                    "passThrough": 0,
                    "explosionShielding": 0.5,
                    "radius": 0.15
                },
                # Class: CfgVehicles\rhsusf_M1117_base\Turrets\MainTurret\HitPoints\HitGun,
                "HitGun": {
                    "armor": 1.3,
                    "material": -1,
                    "name": "zbran",
                    "visual": "-",
                    "passThrough": 0,
                    "explosionShielding": 0.5,
                    "radius": 0.15
                }
            },
            # Class: CfgVehicles\rhsusf_M1117_base\Turrets\MainTurret\ViewGunner,
            "ViewGunner": {
                "initAngleX": 5,
                "minAngleX": -60,
                "maxAngleX": "+85",
                "initAngleY": 0,
                "minAngleY": -150,
                "maxAngleY": "+150",
                "initFov": 0.7,
                "minFov": 0.25,
                "maxFov": 0.7
            },
            # Class: CfgVehicles\rhsusf_M1117_base\Turrets\MainTurret\Reflectors,
            "Reflectors": {
                # Class: CfgVehicles\rhsusf_M1117_base\Turrets\MainTurret\Reflectors\gunlight
                "gunlight": {
                    "color": [1900,1300,950],
                    "ambient": [5,5,5],
                    "position": "t svetlo",
                    "direction": "konec t svetla",
                    "hitpoint": "t svetlo",
                    "selection": "t svetlo",
                    "size": 0.1,
                    "innerAngle": 10,
                    "outerAngle": 12,
                    "coneFadeCoef": 10,
                    "intensity": 1,
                    "useFlare": 1,
                    "dayLight": 1,
                    "flareSize": 0.25,
                    # Class: CfgVehicles\rhsusf_M1117_base\Turrets\MainTurret\Reflectors\gunlight\Attenuation,
                    "Attenuation": {
                        "start": 1,
                        "constant": 0,
                        "linear": 0,
                        "quadratic": 0.25,
                        "hardLimitStart": 50,
                        "hardLimitEnd": 150
                    }
                },
                # Class: CfgVehicles\rhsusf_M1117_base\Turrets\MainTurret\Reflectors\gunlight_flare,
                "gunlight_flare": {
                    "innerAngle": 10,
                    "outerAngle": 160,
                    "coneFadeCoef": 10,
                    "intensity": 1,
                    "flareSize": 1.25,
                    # Class: CfgVehicles\rhsusf_M1117_base\Turrets\MainTurret\Reflectors\gunlight_flare\Attenuation,
                    "Attenuation": {
                        "start": 1,
                        "constant": 0,
                        "linear": 0,
                        "quadratic": 0.25,
                        "hardLimitStart": 0.5,
                        "hardLimitEnd": 0.15
                    },
                    "color": [1900,1300,950],
                    "ambient": [5,5,5],
                    "position": "t svetlo",
                    "direction": "konec t svetla",
                    "hitpoint": "t svetlo",
                    "selection": "t svetlo",
                    "size": 0.1,
                    "useFlare": 1,
                    "dayLight": 1
                }
            },
            "armorLights": 0.1,
            # Class: CfgVehicles\rhsusf_M1117_base\Turrets\MainTurret\Turrets,
            "Turrets": {
                # Class: CfgVehicles\rhsusf_M1117_base\Turrets\MainTurret\Turrets\commanderOptics
                "commanderOptics": {
                    "body": "obsTurret",
                    "gun": "",
                    "animationSourceBody": "obsTurret",
                    "animationSourceGun": "",
                    "animationSourceHatch": "",
                    "animationSourceCamElev": "",
                    "gunBeg": "",
                    "gunEnd": "",
                    "gunnerOpticsModel": "",
                    "gunnerOutOpticsModel": "",
                    "gunnerDoor": "door_r",
                    "commanding": 2,
                    "weapons": ["rhsusf_weap_duke"],
                    "magazines": ["rhsusf_mag_duke"],
                    "soundServo": ["A3|sounds_f|dummysound",0.01,1,10],
                    "minElev": -4,
                    "maxElev": 20,
                    "initElev": 0,
                    "minTurn": -10,
                    "maxTurn": 10,
                    "initTurn": 0,
                    "maxHorizontalRotSpeed": 0.5,
                    "maxVerticalRotSpeed": 0.5,
                    "stabilizedInAxes": 0,
                    "gunnerGetInAction": "GetInAMV_cargo",
                    "gunnerGetOutAction": "GetOutLow",
                    "gunnerCompartments": "Compartment1",
                    "LODTurnedIn": 1100,
                    "LODTurnedOut": 1100,
                    "startEngine": 0,
                    "armorLights": 0.4,
                    "canEject": 1,
                    "preciseGetInOut": 0,
                    "turretFollowFreeLook": 0,
                    "allowTabLock": 0,
                    "showAllTargets": 0,
                    "disableSoundAttenuation": 0,
                    "gunnerInAction": "rhs_M1117_Commander",
                    "gunnerAction": "rhs_M1117_Commander",
                    "gunnerForceOptics": 0,
                    "memoryPointGunnerOptics": "gunnerview",
                    "memoryPointGunnerOutOptics": "gunnerview",
                    "memoryPointsGetInGunner": "pos commander",
                    "memoryPointsGetInGunnerDir": "pos commander dir",
                    "memoryPointGun": "",
                    "selectionFireAnim": "",
                    "turretInfoType": "RHS_RscM1117_Commander",
                    # Class: CfgVehicles\rhsusf_M1117_base\Turrets\MainTurret\Turrets\commanderOptics\ViewOptics,
                    "ViewOptics": {
                        "visionMode": ["Normal","TI"],
                        "thermalMode": [2,3],
                        "initAngleX": 0,
                        "minAngleX": -30,
                        "maxAngleX": "+30",
                        "initAngleY": 0,
                        "minAngleY": -100,
                        "maxAngleY": "+100",
                        "initFov": 0.4,
                        "minFov": 0.2,
                        "maxFov": 0.4,
                        "minMoveX": 0,
                        "maxMoveX": 0,
                        "minMoveY": 0,
                        "maxMoveY": 0,
                        "minMoveZ": 0,
                        "maxMoveZ": 0
                    },
                    # Class: CfgVehicles\rhsusf_M1117_base\Turrets\MainTurret\Turrets\commanderOptics\HitPoints,
                    "HitPoints": {
                    },
                    # Class: CfgVehicles\rhsusf_M1117_base\Turrets\MainTurret\Turrets\commanderOptics\OpticsIn,
                    "OpticsIn": {
                        # Class: CfgVehicles\rhsusf_M1117_base\Turrets\MainTurret\Turrets\commanderOptics\OpticsIn\Wide
                        "Wide": {
                            "initFov": 0.233333,
                            "minFov": 0.233333,
                            "maxFov": 0.233333,
                            "gunnerOpticsModel": "rhsusf|addons|rhsusf_m1117|optics|rhs_m36_wide_com",
                            "visionMode": ["Normal","TI"],
                            "thermalMode": [2,3],
                            "initAngleX": 0,
                            "minAngleX": -30,
                            "maxAngleX": "+30",
                            "initAngleY": 0,
                            "minAngleY": -100,
                            "maxAngleY": "+100",
                            "minMoveX": 0,
                            "maxMoveX": 0,
                            "minMoveY": 0,
                            "maxMoveY": 0,
                            "minMoveZ": 0,
                            "maxMoveZ": 0
                        },
                        # Class: CfgVehicles\rhsusf_M1117_base\Turrets\MainTurret\Turrets\commanderOptics\OpticsIn\Narrow,
                        "Narrow": {
                            "initFov": 0.1,
                            "minFov": 0.1,
                            "maxFov": 0.1,
                            "gunnerOpticsModel": "rhsusf|addons|rhsusf_m1117|optics|rhs_m36_narrow_com",
                            "visionMode": ["Normal","TI"],
                            "thermalMode": [2,3],
                            "initAngleX": 0,
                            "minAngleX": -30,
                            "maxAngleX": "+30",
                            "initAngleY": 0,
                            "minAngleY": -100,
                            "maxAngleY": "+100",
                            "minMoveX": 0,
                            "maxMoveX": 0,
                            "minMoveY": 0,
                            "maxMoveY": 0,
                            "minMoveZ": 0,
                            "maxMoveZ": 0
                        }
                    },
                    "proxyType": "CPCommander",
                    "proxyIndex": 1,
                    "gunnerName": "Commander",
                    "primaryGunner": 0,
                    "primaryObserver": 1,
                    "outGunnerMayFire": 1,
                    "inGunnerMayFire": 1,
                    "viewGunnerInExternal": 0,
                    "gunnerOutOpticsColor": [0,0,0,1],
                    "gunnerOutForceOptics": 0,
                    "gunnerOutOpticsShowCursor": 0,
                    "gunnerOpticsEffect": [],
                    "gunnerOutOpticsEffect": [],
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
                    "viewGunnerShadowDiff": 1,
                    "viewGunnerShadowAmb": 1,
                    "ejectDeadGunner": 0,
                    "hideWeaponsGunner": 1,
                    "canHideGunner": -1,
                    "forceHideGunner": 0,
                    "showHMD": 0,
                    "lockWhenDriverOut": 0,
                    "lockWhenVehicleSpeed": -1,
                    "memoryPointsGetInGunnerPrecise": "",
                    "missileBeg": "spice rakety",
                    "missileEnd": "konec rakety",
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
                    "gunnerLeftHandAnimName": "",
                    "gunnerRightHandAnimName": "",
                    "gunnerLeftLegAnimName": "",
                    "gunnerRightLegAnimName": "",
                    "dontCreateAI": 0,
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
            # Class: CfgVehicles\Wheeled_APC_F\Turrets\MainTurret\Components,
            "Components": {
                # Class: CfgVehicles\Wheeled_APC_F\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentLeft
                "VehicleSystemsDisplayManagerComponentLeft": {
                    # Class: VehicleSystemsTemplateLeftGunner\Components
                    "Components": {
                        # Class: VehicleSystemsTemplateLeftGunner\Components\VehicleDriverDisplay
                        "VehicleDriverDisplay": {
                            "componentType": "TransportFeedDisplayComponent",
                            "source": "Driver"
                        },
                        # Class: VehicleSystemsTemplateLeftGunner\Components\VehicleCommanderDisplay,
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
                # Class: CfgVehicles\Wheeled_APC_F\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentRight,
                "VehicleSystemsDisplayManagerComponentRight": {
                    # Class: VehicleSystemsTemplateRightGunner\Components
                    "Components": {
                        # Class: VehicleSystemsTemplateRightGunner\Components\VehicleDriverDisplay
                        "VehicleDriverDisplay": {
                            "componentType": "TransportFeedDisplayComponent",
                            "source": "Driver"
                        },
                        # Class: VehicleSystemsTemplateRightGunner\Components\VehicleCommanderDisplay,
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
                }
            },
            "animationSourceHatch": "hatchGunner",
            "animationSourceCamElev": "camElev",
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
            "turretCanSee": 0,
            # Class: CfgVehicles\AllVehicles\NewTurret\TurretSpec,
            "TurretSpec": {
                "showHeadPhones": 0
            },
            "gunnerOpticsColor": [0,0,0,1],
            "gunnerOpticsShowCursor": 0,
            "gunnerOutOpticsColor": [0,0,0,1],
            "gunnerOpticsEffect": [],
            "gunnerOutOpticsEffect": [],
            "gunnerOutForceOptics": 0,
            "gunnerOutOpticsShowCursor": 0,
            "gunnerOutFireAlsoInInternalCamera": 1,
            "gunnerUsesPilotView": 0,
            "castGunnerShadow": 0,
            "viewGunnerShadow": 1,
            "viewGunnerShadowDiff": 1,
            "viewGunnerShadowAmb": 1,
            "ejectDeadGunner": 0,
            "hideWeaponsGunner": 1,
            "showHMD": 0,
            "lockWhenDriverOut": 0,
            "lockWhenVehicleSpeed": -1,
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
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Turrets\MainTurret_Out,
        "MainTurret_Out": {
            "gunnerCompartments": "Compartment3",
            "gunnerName": "Gunner",
            "proxyType": "CPGunner",
            "LODTurnedIn": 0,
            "LODTurnedOut": 0,
            "proxyIndex": 2,
            "gunnerAction": "vehicle_turnout_2",
            "gunnerInAction": "vehicle_turnout_2",
            "personTurretAction": "vehicle_turnout_2",
            # Class: CfgVehicles\AllVehicles\CargoTurret\ViewGunner,
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
            "hideWeaponsGunner": 0,
            "isCopilot": 0,
            "memoryPointsGetInGunner": "pos cargo",
            "memoryPointsGetInGunnerDir": "pos cargo dir",
            "primaryGunner": 0,
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
            "gunBeg": "usti hlavne",
            "gunEnd": "konec hlavne",
            "memoryPointGunnerOptics": "gunnerview",
            "memoryPointGun": "kulas",
            "selectionFireAnim": "zasleh",
            "showCrewAim": 0
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Turrets\MainTurret2_Out,
        "MainTurret2_Out": {
            "gunnerName": "Commander",
            "proxyIndex": 3,
            "gunnerAction": "vehicle_turnout_1",
            "gunnerInAction": "vehicle_turnout_1",
            "personTurretAction": "vehicle_turnout_1",
            "gunnerCompartments": "Compartment3",
            "proxyType": "CPGunner",
            "LODTurnedIn": 0,
            "LODTurnedOut": 0,
            # Class: CfgVehicles\AllVehicles\CargoTurret\ViewGunner,
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
            "hideWeaponsGunner": 0,
            "isCopilot": 0,
            "memoryPointsGetInGunner": "pos cargo",
            "memoryPointsGetInGunnerDir": "pos cargo dir",
            "primaryGunner": 0,
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
            "gunBeg": "usti hlavne",
            "gunEnd": "konec hlavne",
            "memoryPointGunnerOptics": "gunnerview",
            "memoryPointGun": "kulas",
            "selectionFireAnim": "zasleh",
            "showCrewAim": 0
        }
    },
    # Class: CfgVehicles\rhsusf_M1117_base\Attributes,
    "Attributes": {
        # Class: CfgVehicles\rhsusf_M1117_base\Attributes\ObjectTexture
        "ObjectTexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayName": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Attributes\rhs_hideDUKE,
        "rhs_hideDUKE": {
            "displayName": "hide DUKE antennas",
            "property": "rhs_hideDUKE",
            "expression": "_this animate ['DUKE_Hide',_value,true]",
            "control": "CheckboxNumber",
            "defaultValue": "0"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Attributes\door_l,
        "door_l": {
            "displayName": "Open left door",
            "property": "door_l",
            "control": "CheckboxNumber",
            "defaultValue": "0",
            "expression": "_this animateDoor ['%s',_value,true]"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Attributes\door_r,
        "door_r": {
            "displayName": "Open right door",
            "property": "door_r",
            "control": "CheckboxNumber",
            "defaultValue": "0",
            "expression": "_this animateDoor ['%s',_value,true]"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Attributes\door_b,
        "door_b": {
            "displayName": "Open back doors",
            "property": "door_b",
            "control": "CheckboxNumber",
            "defaultValue": "0",
            "expression": "_this animateDoor ['%s',_value,true]"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Attributes\hatch_commander,
        "hatch_commander": {
            "displayName": "Open commander hatch",
            "property": "hatch_commander",
            "control": "CheckboxNumber",
            "defaultValue": "0",
            "expression": "_this animateDoor ['%s',_value,true]"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Attributes\hatch_driver,
        "hatch_driver": {
            "displayName": "Open driver hatch",
            "property": "hatch_driver",
            "control": "CheckboxNumber",
            "defaultValue": "0",
            "expression": "_this animateDoor ['%s',_value,true]"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Attributes\hatch_gunner,
        "hatch_gunner": {
            "displayName": "Open gunner hatch",
            "property": "hatch_gunner",
            "control": "CheckboxNumber",
            "defaultValue": "0",
            "expression": "_this animateDoor ['%s',_value,true]"
        }
    },
    # Class: CfgVehicles\rhsusf_M1117_base\AnimationSources,
    "AnimationSources": {
        # Class: CfgVehicles\rhsusf_M1117_base\AnimationSources\smoke_revolving_source
        "smoke_revolving_source": {
            "source": "revolving",
            "weapon": "rhsusf_weap_M257_8"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\AnimationSources\longlights_hide,
        "longlights_hide": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 1
        },
        # Class: CfgVehicles\rhsusf_M1117_base\AnimationSources\shortlights_hide,
        "shortlights_hide": {
            "initPhase": 0,
            "source": "user",
            "animPeriod": 1e-006
        },
        # Class: CfgVehicles\rhsusf_M1117_base\AnimationSources\lights_hide,
        "lights_hide": {
            "initPhase": 0,
            "source": "user",
            "animPeriod": 1e-006
        },
        # Class: CfgVehicles\rhsusf_M1117_base\AnimationSources\cabinlights_hide,
        "cabinlights_hide": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 1
        },
        # Class: CfgVehicles\rhsusf_M1117_base\AnimationSources\door_l,
        "door_l": {
            "source": "door",
            "animperiod": 1,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhsusf_M1117_base\AnimationSources\door_r,
        "door_r": {
            "source": "door",
            "animperiod": 1,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhsusf_M1117_base\AnimationSources\door_b,
        "door_b": {
            "source": "door",
            "animperiod": 1,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhsusf_M1117_base\AnimationSources\zoom_handler,
        "zoom_handler": {
            "source": "door",
            "animperiod": 1,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhsusf_M1117_base\AnimationSources\DUKE_Hide,
        "DUKE_Hide": {
            "source": "user",
            "mass": -20,
            "displayName": "hide DUKE antennas",
            "animPeriod": 1e-005,
            "initPhase": 0,
            "onPhaseChanged": "_this + ([[0,0]]) call rhs_fnc_duke_vg;"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\AnimationSources\ReloadAnim,
        "ReloadAnim": {
            "source": "reload",
            "weapon": "RHS_M2_M1117"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\AnimationSources\muzzle_flash_gl,
        "muzzle_flash_gl": {
            "source": "reload",
            "weapon": "RHS_MK19"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\AnimationSources\muzzle_rot_MG,
        "muzzle_rot_MG": {
            "source": "ammorandom",
            "weapon": "RHS_M2_M1117"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\AnimationSources\muzzle_rot_GL,
        "muzzle_rot_GL": {
            "source": "ammorandom",
            "weapon": "RHS_MK19"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\AnimationSources\Revolving,
        "Revolving": {
            "source": "revolving",
            "weapon": "RHS_M2_M1117"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\AnimationSources\hatch_commander,
        "hatch_commander": {
            "source": "door",
            "animperiod": 1,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhsusf_M1117_base\AnimationSources\hatch_driver,
        "hatch_driver": {
            "source": "door",
            "animperiod": 1,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhsusf_M1117_base\AnimationSources\hatch_gunner,
        "hatch_gunner": {
            "source": "door",
            "animperiod": 1,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhsusf_M1117_base\AnimationSources\HitLFWheel,
        "HitLFWheel": {
            "source": "Hit",
            "hitpoint": "HitLFWheel",
            "raw": 1
        },
        # Class: CfgVehicles\rhsusf_M1117_base\AnimationSources\HitRFWheel,
        "HitRFWheel": {
            "hitpoint": "HitRFWheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\rhsusf_M1117_base\AnimationSources\HitLBWheel,
        "HitLBWheel": {
            "hitpoint": "HitLF2Wheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\rhsusf_M1117_base\AnimationSources\HitRBWheel,
        "HitRBWheel": {
            "hitpoint": "HitRF2Wheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\rhsusf_M1117_base\AnimationSources\HitGlass1,
        "HitGlass1": {
            "source": "Hit",
            "hitpoint": "HitGlass1"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\AnimationSources\HitGlass2,
        "HitGlass2": {
            "hitpoint": "HitGlass2",
            "source": "Hit"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\AnimationSources\HitGlass3,
        "HitGlass3": {
            "hitpoint": "HitGlass3",
            "source": "Hit"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\AnimationSources\HitGlass4,
        "HitGlass4": {
            "hitpoint": "HitGlass4",
            "source": "Hit"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\AnimationSources\HitGlass5,
        "HitGlass5": {
            "hitpoint": "HitGlass5",
            "source": "Hit"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\AnimationSources\HitGlass6,
        "HitGlass6": {
            "hitpoint": "HitGlass6",
            "source": "Hit"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\AnimationSources\HitPeriscope1,
        "HitPeriscope1": {
            "source": "Hit",
            "hitpoint": "HitPeriscope1"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\AnimationSources\HitPeriscope2,
        "HitPeriscope2": {
            "hitpoint": "HitPeriscope2",
            "source": "Hit"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\AnimationSources\HitPeriscope3,
        "HitPeriscope3": {
            "hitpoint": "HitPeriscope3",
            "source": "Hit"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\AnimationSources\HitPeriscope4,
        "HitPeriscope4": {
            "hitpoint": "HitPeriscope4",
            "source": "Hit"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\AnimationSources\HitPeriscope5,
        "HitPeriscope5": {
            "hitpoint": "HitPeriscope5",
            "source": "Hit"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\AnimationSources\HitPeriscope6,
        "HitPeriscope6": {
            "hitpoint": "HitPeriscope6",
            "source": "Hit"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\AnimationSources\HitPeriscope7,
        "HitPeriscope7": {
            "hitpoint": "HitPeriscope7",
            "source": "Hit"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\AnimationSources\HitMainSight,
        "HitMainSight": {
            "hitpoint": "HitMainSight",
            "source": "Hit"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\AnimationSources\HitHull,
        "HitHull": {
            "source": "Hit",
            "hitpoint": "HitHull"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\AnimationSources\HitDuke1,
        "HitDuke1": {
            "source": "Hit",
            "hitpoint": "HitDuke1"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\AnimationSources\HitDuke2,
        "HitDuke2": {
            "hitpoint": "HitDuke2",
            "source": "Hit"
        },
        # Class: CfgVehicles\Wheeled_APC_F\AnimationSources\HitLF2Wheel,
        "HitLF2Wheel": {
            "hitpoint": "HitLBWheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\Wheeled_APC_F\AnimationSources\HitRF2Wheel,
        "HitRF2Wheel": {
            "hitpoint": "HitRBWheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\Wheeled_APC_F\AnimationSources\HitLMWheel,
        "HitLMWheel": {
            "hitpoint": "HitLMWheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\Wheeled_APC_F\AnimationSources\HitRMWheel,
        "HitRMWheel": {
            "hitpoint": "HitRMWheel",
            "source": "Hit",
            "raw": 1
        }
    },
    # Class: CfgVehicles\rhsusf_M1117_base\HitPoints,
    "HitPoints": {
        # Class: CfgVehicles\rhsusf_M1117_base\HitPoints\HitLFWheel
        "HitLFWheel": {
            "radius": 0.3,
            "visual": "wheel_1_1_damage",
            "armorComponent": "wheel_1_1_damper",
            "armor": -250,
            "minimalHit": -0.025,
            "explosionShielding": 1,
            "passThrough": 0,
            "material": -1,
            "name": "wheel_1_1_steering"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\HitPoints\HitLF2Wheel,
        "HitLF2Wheel": {
            "radius": 0.3,
            "visual": "wheel_1_2_damage",
            "armorComponent": "wheel_1_2_damper",
            "armor": -250,
            "minimalHit": -0.025,
            "explosionShielding": 1,
            "passThrough": 0,
            "material": -1,
            "name": "wheel_1_2_steering"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\HitPoints\HitRFWheel,
        "HitRFWheel": {
            "radius": 0.3,
            "visual": "wheel_2_1_damage",
            "armorComponent": "wheel_2_1_damper",
            "armor": -250,
            "minimalHit": -0.025,
            "explosionShielding": 1,
            "passThrough": 0,
            "material": -1,
            "name": "wheel_2_1_steering"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\HitPoints\HitRF2Wheel,
        "HitRF2Wheel": {
            "radius": 0.3,
            "visual": "wheel_2_2_damage",
            "armorComponent": "wheel_2_2_damper",
            "armor": -250,
            "minimalHit": -0.025,
            "explosionShielding": 1,
            "passThrough": 0,
            "material": -1,
            "name": "wheel_2_2_steering"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\HitPoints\HitBody,
        "HitBody": {
            "armor": 0.8,
            "material": -1,
            "name": "karoserie",
            "visual": "zbytek",
            "passThrough": 0,
            "minimalHit": 0.15,
            "explosionShielding": 0.8,
            "radius": 0.05
        },
        # Class: CfgVehicles\rhsusf_M1117_base\HitPoints\HitFuel,
        "HitFuel": {
            "armor": 4,
            "material": -1,
            "name": "palivo",
            "visual": "",
            "passThrough": 0,
            "MinimalHit": 0.05,
            "explosionShielding": 0.01,
            "radius": 0.09
        },
        # Class: CfgVehicles\rhsusf_M1117_base\HitPoints\HitHull,
        "HitHull": {
            "armor": -350,
            "passThrough": 8,
            "name": "karoserie",
            "visual": "zbytek",
            "minimalhit": -0.25,
            "explosionShielding": 0.01,
            "radius": 0.22
        },
        # Class: CfgVehicles\rhsusf_M1117_base\HitPoints\HitDuke1,
        "HitDuke1": {
            "armor": 1,
            "material": -1,
            "name": "duke1",
            "visual": "",
            "passThrough": 0,
            "MinimalHit": 0.15,
            "explosionShielding": 0.01,
            "radius": 0.15
        },
        # Class: CfgVehicles\rhsusf_M1117_base\HitPoints\HitDuke2,
        "HitDuke2": {
            "name": "duke2",
            "visual": "",
            "armor": 1,
            "material": -1,
            "passThrough": 0,
            "MinimalHit": 0.15,
            "explosionShielding": 0.01,
            "radius": 0.15
        },
        # Class: CfgVehicles\rhsusf_M1117_base\HitPoints\HitEngine,
        "HitEngine": {
            "armor": 1.8,
            "material": -1,
            "name": "engine",
            "visual": "zbytek",
            "passThrough": 0,
            "MinimalHit": 0.01,
            "explosionShielding": 0.01,
            "radius": 0.15,
            # Class: CfgVehicles\rhsusf_M1117_base\HitPoints\HitEngine\DestructionEffects,
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\rhsusf_M1117_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Smoke,
                "RHS_Engine_Smoke": {
                    "simulation": "particles",
                    "type": "SmallWreckSmoke",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\rhsusf_M1117_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Fire,
                "RHS_Engine_Fire": {
                    "type": "SmallFireFPlace",
                    "simulation": "particles",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\rhsusf_M1117_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Sparks,
                "RHS_Engine_Sparks": {
                    "type": "RHS_FireSparks",
                    "simulation": "particles",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\rhsusf_M1117_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Sounds,
                "RHS_Engine_Sounds": {
                    "simulation": "sound",
                    "type": "Fire",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\rhsusf_M1117_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Smoke_small1,
                "RHS_Engine_Smoke_small1": {
                    "type": "WeaponWreckSmoke",
                    "position": "engine_smoke2",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\rhsusf_M1117_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Smoke_small2,
                "RHS_Engine_Smoke_small2": {
                    "position": "engine_smoke3",
                    "type": "WeaponWreckSmoke",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\rhsusf_M1117_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Smoke_small3,
                "RHS_Engine_Smoke_small3": {
                    "position": "engine_smoke4",
                    "type": "WeaponWreckSmoke",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                }
            }
        },
        # Class: CfgVehicles\rhsusf_M1117_base\HitPoints\HitGlass1,
        "HitGlass1": {
            "armor": 2.4,
            "explosionShielding": 1,
            "radius": 0.25,
            "material": -1,
            "name": "glass1",
            "visual": "glass1",
            "passThrough": 0
        },
        # Class: CfgVehicles\rhsusf_M1117_base\HitPoints\HitGlass2,
        "HitGlass2": {
            "armor": 2.4,
            "explosionShielding": 1,
            "radius": 0.25,
            "material": -1,
            "name": "glass2",
            "visual": "glass2",
            "passThrough": 0
        },
        # Class: CfgVehicles\rhsusf_M1117_base\HitPoints\HitGlass3,
        "HitGlass3": {
            "armor": 2.4,
            "explosionShielding": 1,
            "radius": 0.25,
            "material": -1,
            "name": "glass3",
            "visual": "glass3",
            "passThrough": 0
        },
        # Class: CfgVehicles\rhsusf_M1117_base\HitPoints\HitGlass4,
        "HitGlass4": {
            "armor": 2.4,
            "explosionShielding": 1,
            "radius": 0.25,
            "material": -1,
            "name": "glass4",
            "visual": "glass4",
            "passThrough": 0
        },
        # Class: CfgVehicles\rhsusf_M1117_base\HitPoints\HitGlass5,
        "HitGlass5": {
            "armor": 2.4,
            "explosionShielding": 1,
            "radius": 0.15,
            "material": -1,
            "name": "glass5",
            "visual": "glass5",
            "passThrough": 0
        },
        # Class: CfgVehicles\rhsusf_M1117_base\HitPoints\HitGlass6,
        "HitGlass6": {
            "armor": 2.4,
            "explosionShielding": 1,
            "radius": 0.15,
            "material": -1,
            "name": "glass6",
            "visual": "glass6",
            "passThrough": 0
        },
        # Class: CfgVehicles\rhsusf_M1117_base\HitPoints\HitPeriscope1,
        "HitPeriscope1": {
            "armor": 0.8,
            "name": "periscope1",
            "visual": "periscope1",
            "explosionShielding": 0.5,
            "radius": 0.05,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles\rhsusf_M1117_base\HitPoints\HitPeriscope2,
        "HitPeriscope2": {
            "armor": 0.8,
            "name": "periscope2",
            "visual": "periscope2",
            "explosionShielding": 0.5,
            "radius": 0.05,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles\rhsusf_M1117_base\HitPoints\HitPeriscope3,
        "HitPeriscope3": {
            "armor": 0.8,
            "name": "periscope3",
            "visual": "periscope3",
            "explosionShielding": 0.5,
            "radius": 0.05,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles\rhsusf_M1117_base\HitPoints\HitPeriscope4,
        "HitPeriscope4": {
            "armor": 0.8,
            "name": "periscope4",
            "visual": "periscope4",
            "explosionShielding": 0.5,
            "radius": 0.05,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles\rhsusf_M1117_base\HitPoints\HitPeriscope5,
        "HitPeriscope5": {
            "armor": 0.8,
            "name": "periscope5",
            "visual": "periscope5",
            "explosionShielding": 0.5,
            "radius": 0.05,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles\rhsusf_M1117_base\HitPoints\HitPeriscope6,
        "HitPeriscope6": {
            "armor": 0.8,
            "name": "periscope6",
            "visual": "periscope6",
            "explosionShielding": 0.5,
            "radius": 0.05,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles\rhsusf_M1117_base\HitPoints\HitPeriscope7,
        "HitPeriscope7": {
            "armor": 0.8,
            "name": "periscope7",
            "visual": "periscope7",
            "explosionShielding": 0.5,
            "radius": 0.05,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles\rhsusf_M1117_base\HitPoints\HitMainSight,
        "HitMainSight": {
            "armor": 1.2,
            "explosionShielding": 0.3,
            "name": "mainSight",
            "visual": "mainSight",
            "radius": 0.05,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles\Car_F\HitPoints\HitRGlass,
        "HitRGlass": {
            "armor": 0.2,
            "material": -1,
            "name": "sklo predni P",
            "passThrough": 0,
            "explosionShielding": 2
        },
        # Class: CfgVehicles\Car_F\HitPoints\HitLGlass,
        "HitLGlass": {
            "armor": 0.2,
            "material": -1,
            "name": "sklo predni L",
            "passThrough": 0,
            "explosionShielding": 2
        },
        # Class: CfgVehicles\Car_F\HitPoints\HitLBWheel,
        "HitLBWheel": {
            "armor": 0.2,
            "material": -1,
            "name": "wheel_1_4_steering",
            "visual": "-",
            "passThrough": 0.3,
            "explosionShielding": 4
        },
        # Class: CfgVehicles\Car_F\HitPoints\HitLMWheel,
        "HitLMWheel": {
            "armor": 0.2,
            "material": -1,
            "name": "wheel_1_3_steering",
            "visual": "-",
            "passThrough": 0.3,
            "explosionShielding": 4
        },
        # Class: CfgVehicles\Car_F\HitPoints\HitRBWheel,
        "HitRBWheel": {
            "armor": 0.2,
            "material": -1,
            "name": "wheel_2_4_steering",
            "visual": "-",
            "passThrough": 0.3,
            "explosionShielding": 4
        },
        # Class: CfgVehicles\Car_F\HitPoints\HitRMWheel,
        "HitRMWheel": {
            "armor": 0.2,
            "material": -1,
            "name": "wheel_2_3_steering",
            "visual": "-",
            "passThrough": 0.3,
            "explosionShielding": 4
        }
    },
    # Class: CfgVehicles\rhsusf_M1117_base\UserActions,
    "UserActions": {
        # Class: CfgVehicles\rhsusf_M1117_base\UserActions\hatch_gunner
        "hatch_gunner": {
            "OnlyForPlayer": 1,
            "position": "",
            "radius": 20,
            "showWindow": 0,
            "default": 1,
            "displayname": "Turn Out",
            "shortcut": "turnOut",
            "condition": "(player == gunner this)",
            "statement": "[this,'hatch_gunner',[[0],[1]],0] spawn rhs_fnc_m1117_turnOut"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\UserActions\hatch_gunner_in,
        "hatch_gunner_in": {
            "displayname": "Turn In",
            "shortcut": "turnIn",
            "condition": "this turretUnit [1] isEqualTo (call rhsusf_fnc_findPlayer)",
            "statement": "[this,'hatch_gunner',[[0],[1]],1] spawn rhs_fnc_m1117_turnOut",
            "OnlyForPlayer": 1,
            "position": "",
            "radius": 20,
            "showWindow": 0,
            "default": 1
        },
        # Class: CfgVehicles\rhsusf_M1117_base\UserActions\hatch_commander,
        "hatch_commander": {
            "condition": "(player == commander this)",
            "statement": "[this,'hatch_commander',[[0,0],[2]],0] spawn rhs_fnc_m1117_turnOut",
            "OnlyForPlayer": 1,
            "position": "",
            "radius": 20,
            "showWindow": 0,
            "default": 1,
            "displayname": "Turn Out",
            "shortcut": "turnOut"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\UserActions\hatch_commander_in,
        "hatch_commander_in": {
            "condition": "this turretUnit [2] isEqualTo (call rhsusf_fnc_findPlayer)",
            "statement": "[this,'hatch_commander',[[0,0],[2]],1] spawn rhs_fnc_m1117_turnOut",
            "displayname": "Turn In",
            "shortcut": "turnIn",
            "OnlyForPlayer": 1,
            "position": "",
            "radius": 20,
            "showWindow": 0,
            "default": 1
        },
        # Class: CfgVehicles\rhsusf_M1117_base\UserActions\hatch_driver,
        "hatch_driver": {
            "displayname": "Open/Close roof hatch",
            "condition": "(player == driver this)",
            "shortcut": "turnOut",
            "statement": "this animateDoor ['hatch_driver',abs((this doorPhase 'hatch_driver')-1)]",
            "OnlyForPlayer": 1,
            "position": "",
            "radius": 20,
            "showWindow": 0,
            "default": 1
        },
        # Class: CfgVehicles\rhsusf_M1117_base\UserActions\lights_toggle,
        "lights_toggle": {
            "displayName": "Toggle short/long lights",
            "position": "",
            "shortcut": "vehLockTargets",
            "radius": 12,
            "priority": 1.5,
            "showWindow": 0,
            "onlyForplayer": 1,
            "condition": "(player == driver this) AND (isLightOn this)",
            "statement": "[this,0] call rhsusf_fnc_carLightToggle"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\UserActions\cabinlights_toggle,
        "cabinlights_toggle": {
            "shortcut": "lockTarget",
            "displayName": "Toggle cabin lights",
            "statement": "[this,1] call rhsusf_fnc_carLightToggle",
            "position": "",
            "radius": 12,
            "priority": 1.5,
            "showWindow": 0,
            "onlyForplayer": 1,
            "condition": "(player == driver this) AND (isLightOn this)"
        }
    },
    # Class: CfgVehicles\rhsusf_M1117_base\TransportBackpacks,
    "TransportBackpacks": {
        # Class: CfgVehicles\rhsusf_M1117_base\TransportBackpacks\_xx_rhsusf_falconii
        "_xx_rhsusf_falconii": {
            "backpack": "rhsusf_falconii",
            "count": 2
        }
    },
    # Class: CfgVehicles\rhsusf_M1117_base\TransportMagazines,
    "TransportMagazines": {
        # Class: CfgVehicles\rhsusf_M1117_base\TransportMagazines\_xx_rhs_mag_30Rnd_556x45_M855A1_Stanag
        "_xx_rhs_mag_30Rnd_556x45_M855A1_Stanag": {
            "count": 12,
            "magazine": "rhs_mag_30Rnd_556x45_M855A1_Stanag"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\TransportMagazines\_xx_rhsusf_100Rnd_556x45_soft_pouch,
        "_xx_rhsusf_100Rnd_556x45_soft_pouch": {
            "count": 8,
            "magazine": "rhsusf_100Rnd_556x45_soft_pouch"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\TransportMagazines\_xx_rhsusf_8Rnd_00Buck,
        "_xx_rhsusf_8Rnd_00Buck": {
            "count": 8,
            "magazine": "rhsusf_8Rnd_00Buck"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\TransportMagazines\_xx_rhs_mag_M433_HEDP,
        "_xx_rhs_mag_M433_HEDP": {
            "count": 12,
            "magazine": "rhs_mag_M433_HEDP"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\TransportMagazines\_xx_rhs_mag_M662_red,
        "_xx_rhs_mag_M662_red": {
            "count": 4,
            "magazine": "rhs_mag_M662_red"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\TransportMagazines\_xx_rhs_mag_m67,
        "_xx_rhs_mag_m67": {
            "count": 8,
            "magazine": "rhs_mag_m67"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\TransportMagazines\_xx_rhs_mag_m18_green,
        "_xx_rhs_mag_m18_green": {
            "count": 4,
            "magazine": "rhs_mag_m18_green"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\TransportMagazines\_xx_rhs_mag_m18_red,
        "_xx_rhs_mag_m18_red": {
            "count": 4,
            "magazine": "rhs_mag_m18_red"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\TransportMagazines\_xx_rhs_mag_an_m8hc,
        "_xx_rhs_mag_an_m8hc": {
            "count": 4,
            "magazine": "rhs_mag_an_m8hc"
        }
    },
    # Class: CfgVehicles\rhsusf_M1117_base\TransportItems,
    "TransportItems": {
        # Class: CfgVehicles\rhsusf_M1117_base\TransportItems\_xx_FirstAidKit
        "_xx_FirstAidKit": {
            "name": "FirstAidKit",
            "count": 6
        },
        # Class: CfgVehicles\rhsusf_M1117_base\TransportItems\_xx_Medikit,
        "_xx_Medikit": {
            "name": "Medikit",
            "count": 1
        },
        # Class: CfgVehicles\rhsusf_M1117_base\TransportItems\_xx_binoculars,
        "_xx_binoculars": {
            "count": 1,
            "name": "Binocular"
        }
    },
    # Class: CfgVehicles\rhsusf_M1117_base\TransportWeapons,
    "TransportWeapons": {
        # Class: CfgVehicles\rhsusf_M1117_base\TransportWeapons\_xx_weap
        "_xx_weap": {
            "count": 1,
            "weapon": "rhs_weap_m4_carryhandle"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\TransportWeapons\_xx_rhs_weap_M590_8RD,
        "_xx_rhs_weap_M590_8RD": {
            "count": 1,
            "weapon": "rhs_weap_M590_8RD"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\TransportWeapons\_xx_rhs_weap_M136_hedp,
        "_xx_rhs_weap_M136_hedp": {
            "count": 2,
            "weapon": "rhs_weap_M136_hedp"
        }
    },
    "transportMaxBackpacks": 2,
    "transportMaxMagazines": 90,
    "wheelDamageThreshold": 0.7,
    "wheelDestroyThreshold": 0.99,
    "wheelDamageRadiusCoef": 0.95,
    "wheelDestroyRadiusCoef": 0.45,
    "smokeLauncherGrenadeCount": 4,
    "smokeLauncherVelocity": 14,
    "smokeLauncherOnTurret": 1,
    "smokeLauncherAngle": 160,
    "attenuationEffectType": "CarAttenuation",
    "soundGetIn": ["A3|Sounds_F|vehicles|soft|MRAP_03|getin",0.562341,1],
    "soundGetOut": ["A3|Sounds_F|vehicles|soft|MRAP_03|getout",0.562341,1,40],
    "soundDammage": ["",1,1],
    "soundEngineOnInt": ["A3|Sounds_F|vehicles|soft|Truck_02|int_start",0.707946,1],
    "soundEngineOnExt": ["A3|Sounds_F|vehicles|soft|Truck_02|ext_start",0.707946,1,200],
    "soundEngineOffInt": ["A3|Sounds_F|vehicles|soft|Truck_02|int_stop",0.707946,1],
    "soundEngineOffExt": ["A3|Sounds_F|vehicles|soft|Truck_02|ext_stop",0.707946,1,200],
    "buildCrash0": ["A3|sounds_f|Vehicles|soft|noises|crash_building_01",1,1,200],
    "buildCrash1": ["A3|sounds_f|Vehicles|soft|noises|crash_building_02",1,1,200],
    "buildCrash2": ["A3|sounds_f|Vehicles|soft|noises|crash_building_03",1,1,200],
    "buildCrash3": ["A3|sounds_f|Vehicles|soft|noises|crash_building_04",1,1,200],
    "soundBuildingCrash": ["buildCrash0",0.25,"buildCrash1",0.25,"buildCrash2",0.25,"buildCrash3",0.25],
    "WoodCrash0": ["A3|sounds_f|Vehicles|soft|noises|crash_mix_wood_01",1,1,200],
    "WoodCrash1": ["A3|sounds_f|Vehicles|soft|noises|crash_mix_wood_02",1,1,200],
    "WoodCrash2": ["A3|sounds_f|Vehicles|soft|noises|crash_mix_wood_03",1,1,200],
    "WoodCrash3": ["A3|sounds_f|Vehicles|soft|noises|crash_mix_wood_04",1,1,200],
    "WoodCrash4": ["A3|sounds_f|Vehicles|soft|noises|crash_mix_wood_05",1,1,200],
    "WoodCrash5": ["A3|sounds_f|Vehicles|soft|noises|crash_mix_wood_06",1,1,200],
    "soundWoodCrash": ["woodCrash0",0.166,"woodCrash1",0.166,"woodCrash2",0.166,"woodCrash3",0.166,"woodCrash4",0.166,"woodCrash5",0.166],
    "ArmorCrash0": ["A3|sounds_f|Vehicles|soft|noises|crash_vehicle_01",1,1,200],
    "ArmorCrash1": ["A3|sounds_f|Vehicles|soft|noises|crash_vehicle_02",1,1,200],
    "ArmorCrash2": ["A3|sounds_f|Vehicles|soft|noises|crash_vehicle_03",1,1,200],
    "ArmorCrash3": ["A3|sounds_f|Vehicles|soft|noises|crash_vehicle_04",1,1,200],
    "soundArmorCrash": ["ArmorCrash0",0.25,"ArmorCrash1",0.25,"ArmorCrash2",0.25,"ArmorCrash3",0.25],
    # Class: CfgVehicles\rhsusf_M1117_base\Sounds,
    "Sounds": {
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\Idle_ext
        "Idle_ext": {
            "sound": ["A3|Sounds_F|vehicles|soft|Truck_02|ext_engine_00",0.562341,1,200],
            "frequency": "0.95	+	((rpm/	3000) factor[(100/	3000),(800/	3000)])*0.15",
            "volume": "engineOn*camPos*(((rpm/	3000) factor[(10/	3000),(50/	3000)])	*	((rpm/	3000) factor[(800/	3000),(600/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\Engine,
        "Engine": {
            "sound": ["A3|Sounds_F|vehicles|soft|Truck_02|ext_engine_01",0.630957,1,200],
            "frequency": "0.8	+	((rpm/	3000) factor[(610/	3000),(1200/	3000)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	3000) factor[(620/	3000),(820/	3000)])	*	((rpm/	3000) factor[(1200/	3000),(1000/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\Engine1_ext,
        "Engine1_ext": {
            "sound": ["A3|Sounds_F|vehicles|soft|Truck_02|ext_engine_02",0.707946,1,200],
            "frequency": "0.8	+	((rpm/	3000) factor[(1000/	3000),(1500/	3000)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	3000) factor[(950/	3000),(1150/	3000)])	*	((rpm/	3000) factor[(1500/	3000),(1300/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\Engine2_ext,
        "Engine2_ext": {
            "sound": ["A3|Sounds_F|vehicles|soft|Truck_02|ext_engine_03",0.794328,1,250],
            "frequency": "0.8	+	((rpm/	3000) factor[(1300/	3000),(1850/	3000)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	3000) factor[(1260/	3000),(1500/	3000)])	*	((rpm/	3000) factor[(1850/	3000),(1600/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\Engine3_ext,
        "Engine3_ext": {
            "sound": ["A3|Sounds_F|vehicles|soft|Truck_02|ext_engine_04",1.12202,1,300],
            "frequency": "0.8	+	((rpm/	3000) factor[(1600/	3000),(2200/	3000)])*0.1",
            "volume": "engineOn*camPos*(((rpm/	3000) factor[(1550/	3000),(1800/	3000)])	*	((rpm/	3000) factor[(2200/	3000),(1950/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\Engine4_ext,
        "Engine4_ext": {
            "sound": ["A3|Sounds_F|vehicles|soft|Truck_02|ext_engine_05",1.41254,1,350],
            "frequency": "0.8	+	((rpm/	3000) factor[(2000/	3000),(2600/	3000)])*0.1",
            "volume": "engineOn*camPos*(((rpm/	3000) factor[(1900/	3000),(2150/	3000)])	*	((rpm/	3000) factor[(2600/	3000),(2300/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\Engine5_ext,
        "Engine5_ext": {
            "sound": ["A3|Sounds_F|vehicles|soft|Truck_02|ext_engine_06",1.77828,1,400],
            "frequency": "0.8	+	((rpm/	3000) factor[(2300/	3000),(3000/	3000)])*0.1",
            "volume": "engineOn*camPos*((rpm/	3000) factor[(2300/	3000),(2700/	3000)])"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\IdleThrust,
        "IdleThrust": {
            "sound": ["A3|Sounds_F|vehicles|soft|Truck_02|ext_exhaust_00",1,1,250],
            "frequency": "0.8	+	((rpm/	3000) factor[(100/	3000),(800/	3000)])*0.15",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	3000) factor[(10/	3000),(50/	3000)])	*	((rpm/	3000) factor[(800/	3000),(600/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\EngineThrust,
        "EngineThrust": {
            "sound": ["A3|Sounds_F|vehicles|soft|Truck_02|ext_exhaust_01",1.25893,1,300],
            "frequency": "0.8	+	((rpm/	3000) factor[(610/	3000),(1200/	3000)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	3000) factor[(620/	3000),(820/	3000)])	*	((rpm/	3000) factor[(1200/	3000),(1000/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\Engine1_Thrust_ext,
        "Engine1_Thrust_ext": {
            "sound": ["A3|Sounds_F|vehicles|soft|Truck_02|ext_exhaust_02",1.41254,1,350],
            "frequency": "0.8	+	((rpm/	3000) factor[(1000/	3000),(1500/	3000)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	3000) factor[(950/	3000),(1150/	3000)])	*	((rpm/	3000) factor[(1500/	3000),(1300/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\Engine2_Thrust_ext,
        "Engine2_Thrust_ext": {
            "sound": ["A3|Sounds_F|vehicles|soft|Truck_02|ext_exhaust_03",1.58489,1,400],
            "frequency": "0.8	+	((rpm/	3000) factor[(1300/	3000),(1850/	3000)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	3000) factor[(1260/	3000),(1500/	3000)])	*	((rpm/	3000) factor[(1850/	3000),(1600/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\Engine3_Thrust_ext,
        "Engine3_Thrust_ext": {
            "sound": ["A3|Sounds_F|vehicles|soft|Truck_02|ext_exhaust_04",1.99526,1,450],
            "frequency": "0.8	+	((rpm/	3000) factor[(1600/	3000),(2200/	3000)])*0.1",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	3000) factor[(1550/	3000),(1800/	3000)])	*	((rpm/	3000) factor[(2200/	3000),(1950/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\Engine4_Thrust_ext,
        "Engine4_Thrust_ext": {
            "sound": ["A3|Sounds_F|vehicles|soft|Truck_02|ext_exhaust_05",1.99526,1,450],
            "frequency": "0.8	+	((rpm/	3000) factor[(2000/	3000),(2600/	3000)])*0.1",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	3000) factor[(1900/	3000),(2150/	3000)])	*	((rpm/	3000) factor[(2600/	3000),(2300/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\Engine5_Thrust_ext,
        "Engine5_Thrust_ext": {
            "sound": ["A3|Sounds_F|vehicles|soft|Truck_02|ext_exhaust_06",2.23872,1,500],
            "frequency": "0.8	+	((rpm/	3000) factor[(2300/	3000),(3000/	3000)])*0.1",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*((rpm/	3000) factor[(2300/	3000),(2700/	3000)])"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\Idle_int,
        "Idle_int": {
            "sound": ["A3|Sounds_F|vehicles|soft|Truck_02|int_engine_00",0.398107,1],
            "frequency": "0.8	+	((rpm/	3000) factor[(100/	3000),(800/	3000)])*0.15",
            "volume": "engineOn*(1-camPos)*(((rpm/	3000) factor[(10/	3000),(50/	3000)])	*	((rpm/	3000) factor[(800/	3000),(600/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\Engine_int,
        "Engine_int": {
            "sound": ["A3|Sounds_F|vehicles|soft|Truck_02|int_engine_01",0.446684,1],
            "frequency": "0.8	+	((rpm/	3000) factor[(610/	3000),(1200/	3000)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	3000) factor[(620/	3000),(820/	3000)])	*	((rpm/	3000) factor[(1200/	3000),(1000/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\Engine1_int,
        "Engine1_int": {
            "sound": ["A3|Sounds_F|vehicles|soft|Truck_02|int_engine_02",0.501187,1],
            "frequency": "0.8	+	((rpm/	3000) factor[(1000/	3000),(1500/	3000)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	3000) factor[(950/	3000),(1150/	3000)])	*	((rpm/	3000) factor[(1500/	3000),(1300/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\Engine2_int,
        "Engine2_int": {
            "sound": ["A3|Sounds_F|vehicles|soft|Truck_02|int_engine_03",0.501187,1],
            "frequency": "0.8	+	((rpm/	3000) factor[(1300/	3000),(1850/	3000)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	3000) factor[(1260/	3000),(1500/	3000)])	*	((rpm/	3000) factor[(1850/	3000),(1600/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\Engine3_int,
        "Engine3_int": {
            "sound": ["A3|Sounds_F|vehicles|soft|Truck_02|int_engine_04",0.562341,1],
            "frequency": "0.8	+	((rpm/	3000) factor[(1600/	3000),(2200/	3000)])*0.1",
            "volume": "engineOn*(1-camPos)*(((rpm/	3000) factor[(1550/	3000),(1800/	3000)])	*	((rpm/	3000) factor[(2200/	3000),(1950/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\Engine4_int,
        "Engine4_int": {
            "sound": ["A3|Sounds_F|vehicles|soft|Truck_02|int_engine_05",0.562341,1],
            "frequency": "0.8	+	((rpm/	3000) factor[(2000/	3000),(2600/	3000)])*0.1",
            "volume": "engineOn*(1-camPos)*(((rpm/	3000) factor[(1900/	3000),(2150/	3000)])	*	((rpm/	3000) factor[(2600/	3000),(2300/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\Engine5_int,
        "Engine5_int": {
            "sound": ["A3|Sounds_F|vehicles|soft|Truck_02|int_engine_06",0.630957,1],
            "frequency": "0.8	+	((rpm/	3000) factor[(2300/	3000),(3000/	3000)])*0.1",
            "volume": "engineOn*(1-camPos)*((rpm/	3000) factor[(2300/	3000),(2700/	3000)])"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\IdleThrust_int,
        "IdleThrust_int": {
            "sound": ["A3|Sounds_F|vehicles|soft|Truck_02|int_exhaust_00",0.501187,1],
            "frequency": "0.8	+	((rpm/	3000) factor[(100/	3000),(800/	3000)])*0.15",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	3000) factor[(10/	3000),(50/	3000)])	*	((rpm/	3000) factor[(800/	3000),(600/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\EngineThrust_int,
        "EngineThrust_int": {
            "sound": ["A3|Sounds_F|vehicles|soft|Truck_02|int_exhaust_01",0.562341,1],
            "frequency": "0.8	+	((rpm/	3000) factor[(610/	3000),(1200/	3000)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	3000) factor[(620/	3000),(820/	3000)])	*	((rpm/	3000) factor[(1200/	3000),(1000/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\Engine1_Thrust_int,
        "Engine1_Thrust_int": {
            "sound": ["A3|Sounds_F|vehicles|soft|Truck_02|int_exhaust_02",0.630957,1],
            "frequency": "0.8	+	((rpm/	3000) factor[(1000/	3000),(1500/	3000)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	3000) factor[(950/	3000),(1150/	3000)])	*	((rpm/	3000) factor[(1500/	3000),(1300/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\Engine2_Thrust_int,
        "Engine2_Thrust_int": {
            "sound": ["A3|Sounds_F|vehicles|soft|Truck_02|int_exhaust_03",0.630957,1],
            "frequency": "0.8	+	((rpm/	3000) factor[(1300/	3000),(1850/	3000)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	3000) factor[(1260/	3000),(1500/	3000)])	*	((rpm/	3000) factor[(1850/	3000),(1600/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\Engine3_Thrust_int,
        "Engine3_Thrust_int": {
            "sound": ["A3|Sounds_F|vehicles|soft|Truck_02|int_exhaust_04",0.707946,1],
            "frequency": "0.8	+	((rpm/	3000) factor[(1600/	3000),(2200/	3000)])*0.1",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	3000) factor[(1550/	3000),(1800/	3000)])	*	((rpm/	3000) factor[(2200/	3000),(1950/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\Engine4_Thrust_int,
        "Engine4_Thrust_int": {
            "sound": ["A3|Sounds_F|vehicles|soft|Truck_02|int_exhaust_05",0.794328,1],
            "frequency": "0.8	+	((rpm/	3000) factor[(2000/	3000),(2600/	3000)])*0.1",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	3000) factor[(1900/	3000),(2150/	3000)])	*	((rpm/	3000) factor[(2600/	3000),(2300/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\Engine5_Thrust_int,
        "Engine5_Thrust_int": {
            "sound": ["A3|Sounds_F|vehicles|soft|Truck_02|int_exhaust_06",1,1],
            "frequency": "0.8	+	((rpm/	3000) factor[(2300/	3000),(3000/	3000)])*0.1",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*((rpm/	3000) factor[(2300/	3000),(2700/	3000)])"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\Movement,
        "Movement": {
            "sound": "soundEnviron",
            "frequency": "1",
            "volume": "0"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\TiresRockOut,
        "TiresRockOut": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|ext_tires_dirt_soft_1",1,1,60],
            "frequency": "1",
            "volume": "camPos*rock*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\TiresSandOut,
        "TiresSandOut": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|ext-tires-sand1",1,1,60],
            "frequency": "1",
            "volume": "camPos*sand*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\TiresGrassOut,
        "TiresGrassOut": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|ext_tires_dirt_soft_2",1,1,60],
            "frequency": "1",
            "volume": "camPos*grass*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\TiresMudOut,
        "TiresMudOut": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|ext-tires-mud2",1,1,60],
            "frequency": "1",
            "volume": "camPos*mud*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\TiresGravelOut,
        "TiresGravelOut": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|ext_tires_gravel_1",1,1,60],
            "frequency": "1",
            "volume": "camPos*gravel*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\TiresAsphaltOut,
        "TiresAsphaltOut": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|ext_tires_asfalt_2",1,1,60],
            "frequency": "1",
            "volume": "camPos*asphalt*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\NoiseOut,
        "NoiseOut": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|noise_int_car_3",1,1,90],
            "frequency": "1",
            "volume": "camPos*(damper0 max 0.02)*(speed factor[0, 8])"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\TiresRockIn,
        "TiresRockIn": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|int_tires_dirt_soft_1",0.707946,1],
            "frequency": "1",
            "volume": "(1-camPos)*rock*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\TiresSandIn,
        "TiresSandIn": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|int-tires-sand2",0.707946,1],
            "frequency": "1",
            "volume": "(1-camPos)*sand*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\TiresGrassIn,
        "TiresGrassIn": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|int_tires_dirt_soft_2",0.707946,1],
            "frequency": "1",
            "volume": "(1-camPos)*grass*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\TiresMudIn,
        "TiresMudIn": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|int-tires-mud2",0.707946,1],
            "frequency": "1",
            "volume": "(1-camPos)*mud*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\TiresGravelIn,
        "TiresGravelIn": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|int_tires_gravel_1",0.707946,1],
            "frequency": "1",
            "volume": "(1-camPos)*gravel*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\TiresAsphaltIn,
        "TiresAsphaltIn": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|int_tires_asfalt_2",0.707946,1],
            "frequency": "1",
            "volume": "(1-camPos)*asphalt*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\NoiseIn,
        "NoiseIn": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|noise_int_car_3",0.707946,1],
            "frequency": "1",
            "volume": "(damper0 max 0.1)*(speed factor[0, 8])*(1-camPos)"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\breaking_ext_road,
        "breaking_ext_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_04",0.707946,1,80],
            "frequency": 1,
            "volume": "engineOn*camPos*asphalt*(LongSlipDrive Factor[-0.15, -0.3])*(Speed Factor[2, 10])"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\acceleration_ext_road,
        "acceleration_ext_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_02",0.707946,1,80],
            "frequency": 1,
            "volume": "engineOn*camPos*asphalt*(LongSlipDrive Factor[0.15, 0.3])*(Speed Factor[10, 0])"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\turn_left_ext_road,
        "turn_left_ext_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_02",0.707946,1,80],
            "frequency": 1,
            "volume": "engineOn*camPos*asphalt*(latSlipDrive Factor[0.15, 0.3])*(Speed Factor[0, 10])"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\turn_right_ext_road,
        "turn_right_ext_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_02",0.707946,1,80],
            "frequency": 1,
            "volume": "engineOn*camPos*asphalt*(latSlipDrive Factor[-0.15, -0.3])*(Speed Factor[0, 10])"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\breaking_ext_dirt,
        "breaking_ext_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_14_dirt_breaking",0.707946,1,60],
            "frequency": 1,
            "volume": "engineOn*camPos*(1-asphalt)*(LongSlipDrive Factor[-0.15, -0.3])*(Speed Factor[2, 10])"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\acceleration_ext_dirt,
        "acceleration_ext_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|acceleration_dirt_ext_1",0.707946,1,60],
            "frequency": 1,
            "volume": "engineOn*camPos*(1-asphalt)*(LongSlipDrive Factor[0.15, 0.3])*(Speed Factor[10, 0])"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\turn_left_ext_dirt,
        "turn_left_ext_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_18_dirt",0.707946,1,60],
            "frequency": 1,
            "volume": "engineOn*camPos*(1-asphalt)*(latSlipDrive Factor[0.15, 0.3])*(Speed Factor[0, 10])"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\turn_right_ext_dirt,
        "turn_right_ext_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_18_dirt",0.707946,1,60],
            "frequency": 1,
            "volume": "engineOn*camPos*(1-asphalt)*(latSlipDrive Factor[-0.15, -0.3])*(Speed Factor[0, 10])"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\breaking_int_road,
        "breaking_int_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_04_int",0.630957,1],
            "frequency": 1,
            "volume": "engineOn*asphalt*(1-camPos)*(LongSlipDrive Factor[-0.15, -0.3])*(Speed Factor[2, 6])"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\acceleration_int_road,
        "acceleration_int_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_02_int",0.630957,1],
            "frequency": 1,
            "volume": "engineOn*asphalt*(1-camPos)*(LongSlipDrive Factor[0.15, 0.3])*(Speed Factor[10, 0])"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\turn_left_int_road,
        "turn_left_int_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_02_int",0.630957,1],
            "frequency": 1,
            "volume": "engineOn*asphalt*(1-camPos)*(latSlipDrive Factor[0.15, 0.3])*(Speed Factor[0, 10])"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\turn_right_int_road,
        "turn_right_int_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_02_int",0.630957,1],
            "frequency": 1,
            "volume": "engineOn*asphalt*(1-camPos)*(latSlipDrive Factor[-0.15, -0.3])*(Speed Factor[0, 10])"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\breaking_int_dirt,
        "breaking_int_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_14_dirt_breaking_int",0.630957,1],
            "frequency": 1,
            "volume": "engineOn*(1-asphalt)*(1-camPos)*(LongSlipDrive Factor[-0.15, -0.3])*(Speed Factor[2, 6])"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\acceleration_int_dirt,
        "acceleration_int_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|acceleration_dirt_int_1",0.630957,1],
            "frequency": 1,
            "volume": "engineOn*(1-asphalt)*(1-camPos)*(LongSlipDrive Factor[0.15, 0.3])*(Speed Factor[10, 0])"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\turn_left_int_dirt,
        "turn_left_int_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_18_dirt_int",0.630957,1],
            "frequency": 1,
            "volume": "engineOn*(1-asphalt)*(1-camPos)*(latSlipDrive Factor[0.15, 0.3])*(Speed Factor[0, 10])"
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Sounds\turn_right_int_dirt,
        "turn_right_int_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_18_dirt_int",0.630957,1],
            "frequency": 1,
            "volume": "engineOn*(1-asphalt)*(1-camPos)*(latSlipDrive Factor[-0.15, -0.3])*(Speed Factor[0, 10])"
        }
    },
    # Class: CfgVehicles\rhsusf_M1117_base\RenderTargets,
    "RenderTargets": {
        # Class: CfgVehicles\rhsusf_M1117_base\RenderTargets\mirrorL
        "mirrorL": {
            "renderTarget": "rendertarget0",
            # Class: CfgVehicles\rhsusf_M1117_base\RenderTargets\mirrorL\CameraView1,
            "CameraView1": {
                "pointPosition": "PIP0_pos",
                "pointDirection": "PIP0_dir",
                "renderVisionMode": 4,
                "renderQuality": 2,
                "fov": 0.35
            },
            "BBoxes": ["PIP_1_TL","PIP_1_TR","PIP_1_BL","PIP_1_BR"]
        },
        # Class: CfgVehicles\rhsusf_M1117_base\RenderTargets\mirrorR,
        "mirrorR": {
            "renderTarget": "rendertarget1",
            # Class: CfgVehicles\rhsusf_M1117_base\RenderTargets\mirrorR\CameraView1,
            "CameraView1": {
                "pointPosition": "PIP1_pos",
                "pointDirection": "PIP1_dir",
                "renderVisionMode": 4,
                "renderQuality": 2,
                "fov": 0.35
            },
            "BBoxes": ["PIP_2_TL","PIP_2_TR","PIP_2_BL","PIP_2_BR"]
        }
    },
    # Class: CfgVehicles\rhsusf_M1117_base\Reflectors,
    "Reflectors": {
        # Class: CfgVehicles\rhsusf_M1117_base\Reflectors\Left
        "Left": {
            "color": [1900,1300,950],
            "ambient": [5,5,5],
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
            # Class: CfgVehicles\rhsusf_M1117_base\Reflectors\Left\Attenuation,
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardLimitStart": 30,
                "hardLimitEnd": 60
            }
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Reflectors\Right,
        "Right": {
            "position": "P svetlo",
            "direction": "konec P svetla",
            "hitpoint": "P svetlo",
            "selection": "P svetlo",
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "size": 1,
            "innerAngle": 100,
            "outerAngle": 179,
            "coneFadeCoef": 10,
            "intensity": 1,
            "useFlare": 0,
            "dayLight": 0,
            "flareSize": 1,
            # Class: CfgVehicles\rhsusf_M1117_base\Reflectors\Left\Attenuation,
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardLimitStart": 30,
                "hardLimitEnd": 60
            }
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Reflectors\Right2,
        "Right2": {
            "useFlare": 1,
            "position": "P svetlo",
            "direction": "konec P svetla",
            "hitpoint": "P svetlo",
            "selection": "P svetlo",
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "size": 1,
            "innerAngle": 100,
            "outerAngle": 179,
            "coneFadeCoef": 10,
            "intensity": 1,
            "dayLight": 0,
            "flareSize": 1,
            # Class: CfgVehicles\rhsusf_M1117_base\Reflectors\Left\Attenuation,
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardLimitStart": 30,
                "hardLimitEnd": 60
            }
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Reflectors\Left2,
        "Left2": {
            "useFlare": 1,
            "position": "L svetlo",
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "direction": "konec L svetla",
            "hitpoint": "L svetlo",
            "selection": "L svetlo",
            "size": 1,
            "innerAngle": 100,
            "outerAngle": 179,
            "coneFadeCoef": 10,
            "intensity": 1,
            "dayLight": 0,
            "flareSize": 1,
            # Class: CfgVehicles\rhsusf_M1117_base\Reflectors\Left\Attenuation,
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardLimitStart": 30,
                "hardLimitEnd": 60
            }
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Reflectors\Long_Left,
        "Long_Left": {
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "position": "Light_L_Long",
            "direction": "Light_L_Long_end",
            "hitpoint": "L svetlo",
            "selection": "L svetlo",
            "size": 1,
            "innerAngle": 22,
            "outerAngle": 29,
            "coneFadeCoef": 1,
            "intensity": 100,
            "useFlare": 0,
            "dayLight": 0,
            "flareSize": 1.5,
            "flareMaxDistance": 750,
            # Class: CfgVehicles\rhsusf_M1117_base\Reflectors\Long_Left\Attenuation,
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0.1,
                "quadratic": 0,
                "hardLimitStart": 500,
                "hardLimitEnd": 750
            }
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Reflectors\Long_Right,
        "Long_Right": {
            "position": "Light_R_Long",
            "direction": "Light_R_Long_end",
            "hitpoint": "P svetlo",
            "selection": "P svetlo",
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "size": 1,
            "innerAngle": 22,
            "outerAngle": 29,
            "coneFadeCoef": 1,
            "intensity": 100,
            "useFlare": 0,
            "dayLight": 0,
            "flareSize": 1.5,
            "flareMaxDistance": 750,
            # Class: CfgVehicles\rhsusf_M1117_base\Reflectors\Long_Left\Attenuation,
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0.1,
                "quadratic": 0,
                "hardLimitStart": 500,
                "hardLimitEnd": 750
            }
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Reflectors\Long_Right2,
        "Long_Right2": {
            "useFlare": 1,
            "position": "light_R_Long_flare",
            "innerAngle": 50,
            "outerAngle": 179,
            "coneFadeCoef": 51,
            "intensity": 1,
            # Class: CfgVehicles\rhsusf_M1117_base\Reflectors\Long_Right2\Attenuation,
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 50,
                "hardLimitStart": 0,
                "hardLimitEnd": 3
            },
            "direction": "Light_R_Long_end",
            "hitpoint": "P svetlo",
            "selection": "P svetlo",
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "size": 1,
            "dayLight": 0,
            "flareSize": 1.5,
            "flareMaxDistance": 750
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Reflectors\Long_Left2,
        "Long_Left2": {
            "useFlare": 1,
            "position": "light_L_Long_flare",
            "innerAngle": 50,
            "outerAngle": 179,
            "coneFadeCoef": 51,
            "intensity": 1,
            # Class: CfgVehicles\rhsusf_M1117_base\Reflectors\Long_Left2\Attenuation,
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 50,
                "hardLimitStart": 0,
                "hardLimitEnd": 3
            },
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "direction": "Light_L_Long_end",
            "hitpoint": "L svetlo",
            "selection": "L svetlo",
            "size": 1,
            "dayLight": 0,
            "flareSize": 1.5,
            "flareMaxDistance": 750
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Reflectors\interior_light_1,
        "interior_light_1": {
            "color": [800,900,650],
            "ambient": [5,0,0],
            "intensity": 4,
            "size": 1,
            "innerAngle": 90,
            "outerAngle": 165,
            "coneFadeCoef": 1,
            "position": "interior_light_1",
            "direction": "interior_light_1_dir",
            "hitpoint": "cabin_light",
            "selection": "cabin_light",
            "useFlare": 1,
            "flareSize": 1,
            "flareMaxDistance": 5,
            "dayLight": 0,
            "blinking": 0,
            # Class: CfgVehicles\rhsusf_M1117_base\Reflectors\interior_light_1\Attenuation,
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 70,
                "hardLimitStart": 1,
                "hardLimitEnd": 1.5
            }
        },
        # Class: CfgVehicles\rhsusf_M1117_base\Reflectors\interior_light_2,
        "interior_light_2": {
            "position": "interior_light_2",
            "direction": "interior_light_2_dir",
            # Class: CfgVehicles\rhsusf_M1117_base\Reflectors\interior_light_2\Attenuation,
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 70,
                "hardLimitStart": 1,
                "hardLimitEnd": 1.5
            },
            "color": [800,900,650],
            "ambient": [5,0,0],
            "intensity": 4,
            "size": 1,
            "innerAngle": 90,
            "outerAngle": 165,
            "coneFadeCoef": 1,
            "hitpoint": "cabin_light",
            "selection": "cabin_light",
            "useFlare": 1,
            "flareSize": 1,
            "flareMaxDistance": 5,
            "dayLight": 0,
            "blinking": 0
        }
    },
    "aggregateReflectors": [["Left","Left2"],["Right","Right2"]],
    # Class: CfgVehicles\rhsusf_M1117_base\Exhausts,
    "Exhausts": {
        # Class: CfgVehicles\rhsusf_M1117_base\Exhausts\Exhaust
        "Exhaust": {
            "position": "exhaust_pos",
            "direction": "exhaust_dir",
            "effect": "ExhaustEffectMRAP_03"
        }
    },
    # Class: CfgVehicles\rhsusf_M1117_base\textureSources,
    "textureSources": {
        # Class: CfgVehicles\rhsusf_M1117_base\textureSources\standard
        "standard": {
            "displayName": "Woodland",
            "textures": ["rhsusf|addons|rhsusf_m1117|data|m1117_tex1_green_co.paa","rhsusf|addons|rhsusf_m1117|data|m1117_armour_green_co.paa","rhsusf|addons|rhsusf_m1117|data|m1117_turret_green_co.paa","rhsusf|addons|rhsusf_m1117|data|m1117_wheel_green_co.paa","rhsusf|addons|rhsusf_hmmwv|textures|A2_parts_g_co.paa","rhsusf|addons|rhsusf_m1a1|duke|data|duke_antennae_wd_co.paa"],
            "factions": ["rhs_faction_usarmy_wd","rhs_faction_usarmy_d"]
        },
        # Class: CfgVehicles\rhsusf_M1117_base\textureSources\desert,
        "desert": {
            "displayName": "Desert",
            "textures": ["rhsusf|addons|rhsusf_m1117|data|m1117_tex1_co.paa","rhsusf|addons|rhsusf_m1117|data|m1117_armour_co.paa","rhsusf|addons|rhsusf_m1117|data|m1117_turret_co.paa","rhsusf|addons|rhsusf_m1117|data|m1117_wheel_co.paa","rhsusf|addons|rhsusf_hmmwv|textures|A2_parts_D_co.paa","rhsusf|addons|rhsusf_m1a1|duke|data|duke_antennae_d_co.paa"],
            "factions": ["rhs_faction_usarmy_wd","rhs_faction_usarmy_d"]
        },
        # Class: CfgVehicles\rhsusf_M1117_base\textureSources\olive,
        "olive": {
            "displayName": "OD",
            "textures": ["rhsusf|addons|rhsusf_m1117|data|M1117_tex1_OD_co.paa","rhsusf|addons|rhsusf_m1117|data|M1117_armour_od_co.paa","rhsusf|addons|rhsusf_m1117|data|M1117_turret_od_co.paa","rhsusf|addons|rhsusf_m1117|data|m1117_wheel_green_co.paa","rhsusf|addons|rhsusf_hmmwv|textures|A2_parts_g_co.paa","rhsusf|addons|rhsusf_m1a1|duke|data|duke_antennae_wd_co.paa"],
            "factions": ["rhs_faction_usarmy_wd","rhs_faction_usarmy_d"]
        },
        # Class: CfgVehicles\rhsusf_M1117_base\textureSources\un,
        "un": {
            "displayName": "UN",
            "textures": ["rhsusf|addons|rhsusf_m1117|data|m1117_tex1_un_co.paa","rhsusf|addons|rhsusf_m1117|data|m1117_armour_un_co.paa","rhsusf|addons|rhsusf_m1117|data|m1117_turret_un_co.paa","rhsusf|addons|rhsusf_m1117|data|m1117_wheel_un_co.paa","rhsusf|addons|rhsusf_hmmwv|textures|A2_parts_D_co.paa","rhsusf|addons|rhsusf_m1a1|duke|data|duke_antennae_d_co.paa"],
            "factions": ["rhs_faction_usarmy_wd","rhs_faction_usarmy_d"]
        }
    },
    "textureList": [],
    # Class: CfgVehicles\rhsusf_M1117_base\PlayerSteeringCoefficients,
    "PlayerSteeringCoefficients": {
        "turnIncreaseConst": 0.1,
        "turnIncreaseLinear": 1,
        "turnIncreaseTime": 1,
        "turnDecreaseConst": 5,
        "turnDecreaseLinear": 3,
        "turnDecreaseTime": 0,
        "maxTurnHundred": 0.7
    },
    # Class: CfgVehicles\rhsusf_M1117_base\EventHandlers,
    "EventHandlers": {
        # Class: CfgVehicles\rhsusf_M1117_base\EventHandlers\rhs_m1117_EH
        "rhs_m1117_EH": {
            "init": "(_this select 0) lockTurret [[1],true];(_this select 0) lockTurret [[2],true]",
            "handleDamage": "_this call rhs_fnc_duke_destruction",
            "hitpart": "_this call rhsusf_fnc_hitSpall",
            "getOut": "_this call rhs_fnc_m1117_hatch"
        },
        "init": "",
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');",
        # Class: DefaultEventHandlers\RHS_DefaultEventhandlers,
        "RHS_DefaultEventhandlers": {
            "hitpart": "_this call rhs_fnc_hitPart"
        }
    },
    "_generalMacro": "Wheeled_APC_F",
    "preferRoads": 0,
    "brakeDistance": 5,
    "driveOnComponent": ["Slide"],
    "sensorPosition": "gunnerView",
    "audible": 14,
    "type": 1,
    "radarTarget": 1,
    "radarTargetSize": 1.2,
    "visualTarget": 1,
    "visualTargetSize": 1,
    "irTargetSize": 1.2,
    "enableRadio": 1,
    "lockDetectionSystem": 0,
    "countermeasureActivationRadius": 2000,
    "soundIncommingMissile": ["|A3|Sounds_F|vehicles|air|noises|alarm_locked_by_missile_3",0.316228,1],
    "epeImpulseDamageCoef": 20,
    "crewExplosionProtection": 0.999,
    "fuelExplosionPower": 1,
    # Class: CfgVehicles\Wheeled_APC_F\Components,
    "Components": {
        # Class: CfgVehicles\Wheeled_APC_F\Components\VehicleSystemsDisplayManagerComponentLeft
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
        # Class: CfgVehicles\Wheeled_APC_F\Components\VehicleSystemsDisplayManagerComponentRight,
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
        # Class: CfgVehicles\Car\Components\AICarSteeringComponent,
        "AICarSteeringComponent": {
            "steeringPIDWeights": [2.9,0.1,0.2],
            "speedPIDWeights": [0.7,0.2,0],
            "convoyPIDWeights": [1,0.01,0.01],
            "doRemapSpeed": 1,
            "remapSpeedRange": [30,70],
            "remapSpeedScalar": [1,0.35],
            "doPredictForward": 1,
            "predictForwardRange": [1,20],
            "steerAheadSaturation": [0.01,0.4],
            "speedPredictionMethod": 2,
            "wheelAngleCoef": 0.7,
            "forwardAngleCoef": 0.7,
            "steeringAngleCoef": 1,
            "differenceAngleCoef": 0.4,
            "stuckMaxTime": 3,
            "allowOvertaking": 1,
            "allowDrifting": 0,
            "allowCollisionAvoidance": 1,
            "maxWheelAngleDiff": 0.2616,
            "minSpeedToKeep": 0.1,
            "commandTurnFactor": 1
        },
        # Class: CfgVehicles\LandVehicle\Components\TransportCountermeasuresComponent,
        "TransportCountermeasuresComponent": {
        }
    },
    "headGforceLeaningFactor": [0.0075,0.005,0.0075],
    "camShakeCoef": 0.05,
    "maximumLoad": 3000,
    "transportMaxWeapons": 12,
    "supplyRadius": -1,
    "memoryPointSupply": "doplnovani",
    # Class: CfgVehicles\Wheeled_APC_F\NewTurret,
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
    "occludeSoundsWhenIn": 0,
    "obstructSoundsWhenIn": 0,
    "secondaryExplosion": -10,
    "dammageHalf": [],
    "dammageFull": [],
    "explosionShielding": 1,
    "minTotalDamageThreshold": 0.01,
    "gunnerHasFlares": 0,
    "driverLeftHandAnimName": "drivewheel",
    "driverRightHandAnimName": "drivewheel",
    "driverLeftLegAnimName": "",
    "driverRightLegAnimName": "pedal_thrust",
    "holdOffroadFormation": 1,
    # Class: CfgVehicles\Car_F\NVGMarkers,
    "NVGMarkers": {
        # Class: CfgVehicles\Car_F\NVGMarkers\NVGMarker01
        "NVGMarker01": {
            "name": "nvg_marker",
            "color": [0.03,0.003,0.003,1],
            "ambient": [0.003,0.0003,0.0003,1],
            "brightness": 0.001,
            "blinking": 1
        }
    },
    "viewCargoShadowDiff": 1,
    "viewCargoShadowAmb": 1,
    "accuracy": 0.25,
    "insideSoundCoef": 0.9,
    "soundEnviron": ["",0.000562341,1],
    "soundCrash": ["A3|sounds_f|dummysound",1,1],
    "soundGear": ["",1e-005,1],
    "collisionEffect": "collisionEffect",
    "hideUnitInfo": 0,
    "brakeTorque": 6000,
    "longStiff": 15000,
    "latStiffX": 2000,
    "latStiffY": 18000,
    "wheelMask": "wheel_X_X",
    "numberPhysicalWheels": 4,
    "maxGForce": 3,
    # Class: CfgVehicles\Car_F\camShakeGForce,
    "camShakeGForce": {
        "power": 2,
        "frequency": 60,
        "distance": 0,
        "minSpeed": 60
    },
    "unloadInCombat": 1,
    "limitedSpeedCoef": 0.5,
    "hullDamageCauseExplosion": 1,
    # Class: CfgVehicles\Car\PlateInfos,
    "PlateInfos": {
        "name": "spz",
        "color": [0,0,0,0.75]
    },
    "selectionFireAnim": "zasleh",
    "alphaTracks": 0.2,
    "memoryPointTrackFLL": "Stopa PLL",
    "memoryPointTrackFLR": "Stopa PLP",
    "memoryPointTrackBLL": "Stopa ZLL",
    "memoryPointTrackBLR": "Stopa ZLP",
    "memoryPointTrackFRL": "Stopa PPL",
    "memoryPointTrackFRR": "Stopa PPP",
    "memoryPointTrackBRL": "Stopa ZPL",
    "memoryPointTrackBRR": "Stopa ZPP",
    "memoryPointCirculumReference": "circulumReference",
    "gearBox": [-8,0,10,6.15,4.44,3.33],
    "Scudeffect": "ScudEffect",
    "armorLights": 0.4,
    "formationX": 20,
    "formationZ": 20,
    "scudModel": "",
    "inputTurnCurve": [[0,[0,0,1,1]],[30,[0,0,0.2,0.008,0.4,0.032,0.6,0.216,0.8,0.512,1,1]]],
    "soundEngine": ["",1.77828,0.9],
    "memoryPointTaskMarkerOffset": [0,0.3,0],
    "rightDustEffects": [["GdtKLDirt","RDustEffects"],["GdtKLGrass1","RDustEffects"],["GdtKLGrass1","RGrassEffects"],["GdtKLGrass2","RDustEffects"],["GdtKLGrass2","RGrassEffects"],["GdtKLForestCon","RDustEffects"],["GdtKLForestDec","RDustEffects"],["GdtKlMud","RDustEffects"],["GdtKlSoil","RDustEffects"],["GdtKlTarmac","RDustEffects"],["GdtKlStubble","RDustEffects"],["GdtKlStones","RStonesEffects"],["SurfRoadDirt_Enoch","RDustEffects"],["SurfTrailDirt_Enoch","RDustEffects"],["SurfRoadTarmac1_Enoch","RDustEffects"],["SurfRoadTarmac2_Enoch","RDustEffects"],["SurfRoadTarmac3_Enoch","RDustEffects"],["GdtGrassShort","RDustEffects"],["GdtGrassShort","RGrassEffects"],["GdtGrassTall","RDustEffects"],["GdtGrassTall","RGrassEffects"],["GdtRedDirt","RDustEffectsRed"],["GdtField","RDustEffects"],["GdtForest","RDustEffects"],["GdtVolcano","RDustEffects"],["GdtVolcano","RStonesEffects"],["GdtCliff","RDustEffects"],["GdtVolcanoBeach","RDustEffects"],["SurfRoadDirt_exp","RDustEffectsRed"],["SurfRoadConcrete_exp","RDustEffects"],["SurfRoadTarmac_exp","RDustEffects"],["GdtStratisConcrete","RDustEffects"],["GdtStratisConcrete","RDirtEffects"],["GdtStratisBeach","RDustEffects"],["GdtStratisBeach","RStonesEffects"],["GdtStratisDirt","RDustEffects"],["GdtStratisDirt","RDirtEffects"],["GdtStratisSeabedCluttered","RDustEffects"],["GdtStratisSeabed","RDustEffects"],["GdtStratisDryGrass","RDustEffects"],["GdtStratisDryGrass","RGrassDryEffects"],["GdtStratisDryGrass","RDirtEffects"],["GdtStratisGreenGrass","RDustEffects"],["GdtStratisGreenGrass","RGrassEffects"],["GdtStratisGreenGrass","RDirtEffects"],["GdtStratisRocky","RDustEffects"],["GdtStratisRocky","RGrassEffects"],["GdtStratisRocky","RDirtEffects"],["GdtStratisThistles","RDustEffects"],["GdtStratisThistles","RGrassEffects"],["GdtStratisThistles","RDirtEffects"],["GdtConcrete","RDustEffects"],["GdtConcrete","RDirtEffects"],["GdtAsphalt","RDustEffects"],["GdtAsphalt","RDirtEffects"],["GdtRubble","RDustEffects"],["GdtRubble","RDirtEffects"],["GdtSoil","RDustEffects"],["GdtSoil","RDirtEffects"],["GdtBeach","RDustEffects"],["GdtBeach","RStonesEffects"],["GdtRock","RDustEffects"],["GdtRock","RDirtEffects"],["GdtDead","RDustEffects"],["GdtDead","RDirtEffects"],["Default","RDustEffects"],["GdtDesert","RDustEffects"],["GdtDesert","RStonesEffects"],["GdtDesert1","RDustEffects"],["GdtDesert1","RSandEffects"],["GdtDesert1","RDirtEffects"],["GdtDesert1","RStonesEffects"],["GdtDesert2","RDustEffects"],["GdtDesert2","RSandEffects"],["GdtDesert2","RGrassEffects"],["GdtDesert2","RDirtEffects"],["GdtDirt","RDustEffects"],["GdtDirt","RDirtEffects"],["GdtGrassGreen","RDustEffects"],["GdtGrassGreen","RGrassEffects"],["GdtGrassGreen","RDirtEffects"],["GdtGrassDry","RDustEffects"],["GdtGrassDry","RGrassDryEffects"],["GdtGrassDry","RDirtEffects"],["GdtGrassWild","RDustEffects"],["GdtGrassWild","RGrassEffects"],["GdtGrassWild","RDirtEffects"],["GdtWildField","RDustEffects"],["GdtWildField","RGrassEffects"],["GdtWildField","RDirtEffects"],["GdtWeed1","RDustEffects"],["GdtWeed1","RGrassEffects"],["GdtWeed1","RDirtEffects"],["GdtWeed2","RDustEffects"],["GdtWeed2","RGrassEffects"],["GdtWeed2","RDirtEffects"],["GdtThorn","RDustEffects"],["GdtThorn","RGrassEffects"],["GdtThorn","RDirtEffects"],["GdtStony","RDustEffects"],["GdtStony","RGrassEffects"],["GdtStony","RDirtEffects"],["GdtStonyGreen","RDustEffects"],["GdtStonyGreen","RGrassEffects"],["GdtStonyGreen","RDirtEffects"],["GdtStonyThistle","RDustEffects"],["GdtStonyThistle","RGrassEffects"],["GdtStonyThistle","RDirtEffects"],["GdtSeabedDeep","RDustEffects"],["GdtSeabed","RDustEffects"],["SurfRoadDirt","RDustEffects"],["SurfRoadConcrete","RDustEffects"],["SurfRoadTarmac","RDustEffects"],["SurfWood","RDustEffects"],["SurfMetal","RDustEffects"],["SurfRoofTin","RDustEffects"],["SurfRoofTiles","RDustEffects"],["SurfIntWood","RDustEffects"],["SurfIntConcrete","RDustEffects"],["SurfIntTiles","RDustEffects"],["SurfIntMetal","RDustEffects"],["dirtrunway","RDustEffects"]],
    "leftDustEffects": [["GdtKLDirt","LDustEffects"],["GdtKLGrass1","LDustEffects"],["GdtKLGrass1","LGrassEffects"],["GdtKLGrass2","LDustEffects"],["GdtKLGrass2","LGrassEffects"],["GdtKLForestCon","LDustEffects"],["GdtKLForestDec","LDustEffects"],["GdtKlMud","LDustEffects"],["GdtKlSoil","LDustEffects"],["GdtKlTarmac","LDustEffects"],["GdtKlStubble","LDustEffects"],["GdtKlStones","LStonesEffects"],["SurfRoadDirt_Enoch","LDustEffects"],["SurfTrailDirt_Enoch","LDustEffects"],["SurfRoadTarmac1_Enoch","LDustEffects"],["SurfRoadTarmac2_Enoch","LDustEffects"],["SurfRoadTarmac3_Enoch","LDustEffects"],["GdtGrassShort","LDustEffects"],["GdtGrassShort","LGrassEffects"],["GdtGrassTall","LDustEffects"],["GdtGrassTall","LGrassEffects"],["GdtRedDirt","LDustEffectsRed"],["GdtField","LDustEffects"],["GdtForest","LDustEffects"],["GdtVolcano","LDustEffects"],["GdtVolcano","LStonesEffects"],["GdtCliff","LDustEffects"],["GdtVolcanoBeach","LDustEffects"],["SurfRoadDirt_exp","LDustEffectsRed"],["SurfRoadConcrete_exp","LDustEffects"],["SurfRoadTarmac_exp","LDustEffects"],["GdtStratisConcrete","LDustEffects"],["GdtStratisConcrete","LDirtEffects"],["GdtStratisBeach","LDustEffects"],["GdtStratisBeach","LStonesEffects"],["GdtStratisDirt","LDustEffects"],["GdtStratisDirt","LDirtEffects"],["GdtStratisSeabedCluttered","LDustEffects"],["GdtStratisSeabed","LDustEffects"],["GdtStratisDryGrass","LDustEffects"],["GdtStratisDryGrass","LGrassDryEffects"],["GdtStratisDryGrass","LDirtEffects"],["GdtStratisGreenGrass","LDustEffects"],["GdtStratisGreenGrass","LGrassEffects"],["GdtStratisGreenGrass","LDirtEffects"],["GdtStratisRocky","LDustEffects"],["GdtStratisRocky","LGrassEffects"],["GdtStratisRocky","LDirtEffects"],["GdtStratisThistles","LDustEffects"],["GdtStratisThistles","LGrassEffects"],["GdtStratisThistles","LDirtEffects"],["GdtConcrete","LDustEffects"],["GdtConcrete","LDirtEffects"],["GdtAsphalt","LDustEffects"],["GdtAsphalt","LDirtEffects"],["GdtRubble","LDustEffects"],["GdtRubble","LGrassEffects"],["GdtRubble","LDirtEffects"],["GdtSoil","LDustEffects"],["GdtSoil","LDirtEffects"],["GdtBeach","LDustEffects"],["GdtBeach","LStonesEffects"],["GdtRock","LDustEffects"],["GdtRock","LDirtEffects"],["GdtDead","LDustEffects"],["GdtDead","LDirtEffects"],["Default","LDustEffects"],["GdtDesert","LDustEffects"],["GdtDesert","LStonesEffects"],["GdtDesert1","LDustEffects"],["GdtDesert1","LSandEffects"],["GdtDesert1","LDirtEffects"],["GdtDesert1","LStonesEffects"],["GdtDesert2","LDustEffects"],["GdtDesert2","LSandEffects"],["GdtDesert2","LGrassEffects"],["GdtDesert2","LDirtEffects"],["GdtDirt","LDustEffects"],["GdtDirt","LDirtEffects"],["GdtGrassGreen","LDustEffects"],["GdtGrassGreen","LGrassEffects"],["GdtGrassGreen","LDirtEffects"],["GdtGrassDry","LDustEffects"],["GdtGrassDry","LGrassDryEffects"],["GdtGrassDry","LDirtEffects"],["GdtGrassWild","LDustEffects"],["GdtGrassWild","LGrassEffects"],["GdtGrassWild","LDirtEffects"],["GdtWildField","LDustEffects"],["GdtWildField","LGrassEffects"],["GdtWildField","LDirtEffects"],["GdtWeed1","LDustEffects"],["GdtWeed1","LGrassEffects"],["GdtWeed1","LDirtEffects"],["GdtWeed2","LDustEffects"],["GdtWeed2","LGrassEffects"],["GdtWeed2","LDirtEffects"],["GdtThorn","LDustEffects"],["GdtThorn","LGrassEffects"],["GdtThorn","LDirtEffects"],["GdtStony","LDustEffects"],["GdtStony","LGrassEffects"],["GdtStony","LDirtEffects"],["GdtStonyGreen","LDustEffects"],["GdtStonyGreen","LGrassEffects"],["GdtStonyGreen","LDirtEffects"],["GdtStonyThistle","LDustEffects"],["GdtStonyThistle","LGrassEffects"],["GdtStonyThistle","LDirtEffects"],["GdtSeabedDeep","LDustEffects"],["GdtSeabed","LDustEffects"],["SurfRoadDirt","LDustEffects"],["SurfRoadConcrete","LDustEffects"],["SurfRoadTarmac","LDustEffects"],["SurfWood","LDustEffects"],["SurfMetal","LDustEffects"],["SurfRoofTin","LDustEffects"],["SurfRoofTiles","LDustEffects"],["SurfIntWood","LDustEffects"],["SurfIntConcrete","LDustEffects"],["SurfIntTiles","LDustEffects"],["SurfIntMetal","LDustEffects"],["dirtrunway","LDustEffects"]],
    # Class: CfgVehicles\Car\DestructionEffects,
    "DestructionEffects": {
        # Class: CfgVehicles\Car\DestructionEffects\Light1
        "Light1": {
            "simulation": "light",
            "type": "ObjectDestructionLight",
            "position": "destructionEffect1",
            "intensity": 0.001,
            "interval": 1,
            "lifeTime": 3,
            "enabled": "distToWater"
        },
        # Class: CfgVehicles\Car\DestructionEffects\Sound,
        "Sound": {
            "simulation": "sound",
            "position": "destructionEffect1",
            "intensity": 1,
            "interval": 1,
            "lifeTime": 1,
            "type": "Fire"
        },
        # Class: CfgVehicles\Car\DestructionEffects\Fire1,
        "Fire1": {
            "simulation": "particles",
            "type": "ObjectDestructionFire1Small",
            "position": "destructionEffect1",
            "intensity": 0.15,
            "interval": 1,
            "lifeTime": 3
        },
        # Class: CfgVehicles\Car\DestructionEffects\Refract1,
        "Refract1": {
            "simulation": "particles",
            "type": "ObjectDestructionRefractSmall",
            "position": "destructionEffect1",
            "intensity": 0.15,
            "interval": 1,
            "lifeTime": 3
        },
        # Class: CfgVehicles\Car\DestructionEffects\Smoke1,
        "Smoke1": {
            "simulation": "particles",
            "type": "ObjectDestructionSmokeSmall",
            "position": "destructionEffect1",
            "intensity": 0.15,
            "interval": 1,
            "lifeTime": 3.5
        },
        # Class: CfgVehicles\Car\DestructionEffects\Sparks1,
        "Sparks1": {
            "simulation": "particles",
            "type": "ObjectDestructionSparks",
            "position": "destructionEffect1",
            "intensity": 0,
            "interval": 1,
            "lifeTime": 0
        },
        # Class: CfgVehicles\Car\DestructionEffects\FireSparks1,
        "FireSparks1": {
            "simulation": "particles",
            "type": "FireSparks",
            "position": "destructionEffect2",
            "intensity": 1,
            "interval": 1,
            "lifeTime": 2.8
        },
        # Class: CfgVehicles\Car\DestructionEffects\Fire2,
        "Fire2": {
            "simulation": "particles",
            "type": "ObjectDestructionFire2Small",
            "position": "destructionEffect2",
            "intensity": 0.15,
            "interval": 1,
            "lifeTime": 3
        },
        # Class: CfgVehicles\Car\DestructionEffects\Smoke1_2,
        "Smoke1_2": {
            "simulation": "particles",
            "type": "ObjectDestructionSmoke1_2Small",
            "position": "destructionEffect2",
            "intensity": 0.15,
            "interval": 1,
            "lifeTime": 3.5
        },
        # Class: CfgVehicles\Car\DestructionEffects\Smoke2,
        "Smoke2": {
            "simulation": "particles",
            "type": "ObjectDestructionSmoke2",
            "position": "destructionEffect2",
            "intensity": 1,
            "interval": 1,
            "lifeTime": 3.2
        }
    },
    "sensitivityEar": 0.125,
    "sensitivity": 1.75,
    "selectionBrakeLights": "brzdove svetlo",
    "memoryPointMissile": ["spice rakety","usti hlavne"],
    "memoryPointMissileDir": ["konec rakety","konec hlavne"],
    "engineStartSpeed": 1.5,
    "leftDustEffect": "LDustEffects",
    "rightDustEffect": "RDustEffects",
    "leftWaterEffect": "LWaterEffects",
    "rightWaterEffect": "RWaterEffects",
    "leftFastWaterEffect": "LWaterEffects",
    "rightFastWaterEffect": "RWaterEffects",
    "tracksSpeed": 0,
    "selectionLeftOffset": "PasOffsetL",
    "selectionRightOffset": "PasOffsetP",
    "explosionEffect": "FuelExplosion",
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
    # Class: CfgVehicles\AllVehicles\MFD,
    "MFD": {
    },
    # Class: CfgVehicles\AllVehicles\SoundEvents,
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
    "camouflage": 2,
    "spotableDarkNightLightsOff": 0.001,
    "spotableNightLightsOff": 0.02,
    "spotableNightLightsOn": 4,
    "accuracyDarkNightLightsOff": 0.001,
    "accuracyNightLightsOff": 0.006,
    "accuracyNightLightsOn": 0.1,
    "outsideSoundFilter": 0,
    "obstructSoundLFRatio": 0,
    "occludeSoundLFRatio": 0.25,
    "slowSpeedForwardCoef": 0.3,
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
    "irScanRangeMin": 0,
    "irScanRangeMax": 0,
    "irScanToEyeFactor": 1,
    "irScanGround": 1,
    "laserTarget": 0,
    "laserScanner": 0,
    "nvTarget": 0,
    "nvScanner": 0,
    "artilleryTarget": 0,
    "artilleryScanner": 0,
    "canUseScanners": 1,
    "unitInfoTypeLite": 0,
    "nightVision": 0,
    "hasDriver": 1,
    "getInRadius": 2.5,
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
    "driverOpticsEffect": [],
    "driverOpticsColor": [1,1,1,1],
    "canHideDriver": -1,
    "castCargoShadow": 0,
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
    "HeadAimDown": 0,
    "cargoCanEject": 1,
    "driverCanEject": 1,
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
    "minGForce": 0.2,
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