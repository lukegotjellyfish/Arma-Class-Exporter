rhs_zsu234_aa = {
    "editorpreview": "rhsafrf|addons|rhs_editorPreviews|data|rhs_zsu234_aa.paa",
    "author": "RHS",
    "scope": 2,
    "displayname": "ZSU-23-4V",
    "faction": "rhs_faction_vpvo",
    "vehicleclass": "rhs_vehclass_aa",
    "editorsubcategory": "rhs_EdSubcat_aa",
    "dlc": "RHS_AFRF",
    "rhs_decalparameters": ["['Number',cRHSZSUNumberPlaces,'Default']"],
    "category": "Armored",
    "driveoncomponent": ["Slide"],
    "simulation": "tankX",
    "maxfordingdepth": 0,
    "waterresistance": 0,
    "waterdamageengine": 0.2,
    "waterleakiness": 10,
    "enginepower": 209,
    "peaktorque": 1176,
    "minomega": 61,
    "maxomega": 209.44,
    "idlerpm": 600,
    "redrpm": 2000,
    "torquecurve": [[0,0],[0.3,0.757238],[0.4,0.868597],[0.6,0.957684],[0.7,1],[0.8,0.746102],[1,0.534521],[1.5,0]],
    "thrustdelay": 0.6,
    "clutchstrength": 80,
    "fuelcapacity": 30,
    "rhs_fuelcapacity": 520,
    "brakeidlespeed": 1.78,
    "latency": 1.1,
    "tankturnforce": 330000,
    "tankturnforceangminspd": 0.6,
    "tankturnforceangspd": 0.91,
    "accelaidforceyoffset": -3.5,
    "accelaidforcecoef": 4,
    "accelaidforcespd": 1.9,
    "enginelosses": 25,
    "transmissionlosses": 15,
    "normalspeedforwardcoef": 0.7,
    "changegeartype": "rpmratio",
    "changegearomegaratios": [1,0.7,0.75,0.55,0.65,0.5,0.75,0.7,0.75,0.7,0.75,0.55,1,0.5],
    # Class: CfgVehicles|rhs_zsutank_base|complexGearbox [Indent level: 1],
    "complexgearbox": {
        "gearboxratios": ["R2",-7,"N",0,"D1",1.25,"D2",1.2,"D3",1.15,"D4",1.05,"D5",0.95],
        "transmissionratios": ["High",15.8],
        "gearboxmode": "auto",
        "moveoffgear": 1,
        "drivestring": "D",
        "neutralstring": "N",
        "reversestring": "R",
        "transmissiondelay": 0.6
    },
    # Class: CfgVehicles|rhs_zsutank_base|Wheels [Indent level: 1],
    "wheels": {
        # Class: CfgVehicles|rhs_zsutank_base|Wheels|L2 [Indent level: 2]
        "l2": {
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "bonename": "wheel_podkoloL1",
            "center": "wheel_1_2_axis",
            "boundary": "wheel_1_2_bound",
            "steering": 0,
            "width": 0.33,
            "mass": 150,
            "moi": 10,
            "maxbraketorque": 8000,
            "sprungmass": -1,
            "springstrength": 150000,
            "springdamperrate": 11000,
            "dampingrate": 2174,
            "dampingrateinair": 2174,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.45],[0.18,1],[0.6,0.6]]
        },
        # Class: CfgVehicles|rhs_zsutank_base|Wheels|L3 [Indent level: 2],
        "l3": {
            "bonename": "wheel_podkolol2",
            "center": "wheel_1_3_axis",
            "boundary": "wheel_1_3_bound",
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.33,
            "mass": 150,
            "moi": 10,
            "maxbraketorque": 8000,
            "sprungmass": -1,
            "springstrength": 150000,
            "springdamperrate": 11000,
            "dampingrate": 2174,
            "dampingrateinair": 2174,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.45],[0.18,1],[0.6,0.6]]
        },
        # Class: CfgVehicles|rhs_zsutank_base|Wheels|L4 [Indent level: 2],
        "l4": {
            "bonename": "wheel_podkolol3",
            "center": "wheel_1_4_axis",
            "boundary": "wheel_1_4_bound",
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.33,
            "mass": 150,
            "moi": 10,
            "maxbraketorque": 8000,
            "sprungmass": -1,
            "springstrength": 150000,
            "springdamperrate": 11000,
            "dampingrate": 2174,
            "dampingrateinair": 2174,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.45],[0.18,1],[0.6,0.6]]
        },
        # Class: CfgVehicles|rhs_zsutank_base|Wheels|L5 [Indent level: 2],
        "l5": {
            "bonename": "wheel_podkolol4",
            "center": "wheel_1_5_axis",
            "boundary": "wheel_1_5_bound",
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.33,
            "mass": 150,
            "moi": 10,
            "maxbraketorque": 8000,
            "sprungmass": -1,
            "springstrength": 150000,
            "springdamperrate": 11000,
            "dampingrate": 2174,
            "dampingrateinair": 2174,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.45],[0.18,1],[0.6,0.6]]
        },
        # Class: CfgVehicles|rhs_zsutank_base|Wheels|L6 [Indent level: 2],
        "l6": {
            "bonename": "wheel_podkolol5",
            "center": "wheel_1_6_axis",
            "boundary": "wheel_1_6_bound",
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.33,
            "mass": 150,
            "moi": 10,
            "maxbraketorque": 8000,
            "sprungmass": -1,
            "springstrength": 150000,
            "springdamperrate": 11000,
            "dampingrate": 2174,
            "dampingrateinair": 2174,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.45],[0.18,1],[0.6,0.6]]
        },
        # Class: CfgVehicles|rhs_zsutank_base|Wheels|L7 [Indent level: 2],
        "l7": {
            "bonename": "wheel_podkolol6",
            "center": "wheel_1_7_axis",
            "boundary": "wheel_1_7_bound",
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.33,
            "mass": 150,
            "moi": 10,
            "maxbraketorque": 8000,
            "sprungmass": -1,
            "springstrength": 150000,
            "springdamperrate": 11000,
            "dampingrate": 2174,
            "dampingrateinair": 2174,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.45],[0.18,1],[0.6,0.6]]
        },
        # Class: CfgVehicles|rhs_zsutank_base|Wheels|L9 [Indent level: 2],
        "l9": {
            "bonename": "wheel_podkolol9",
            "center": "wheel_1_9_axis",
            "boundary": "wheel_1_9_bound",
            "maxdroop": 0,
            "maxcompression": 0,
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.33,
            "mass": 150,
            "moi": 10,
            "maxbraketorque": 8000,
            "sprungmass": -1,
            "springstrength": 150000,
            "springdamperrate": 11000,
            "dampingrate": 2174,
            "dampingrateinair": 2174,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.45],[0.18,1],[0.6,0.6]]
        },
        # Class: CfgVehicles|rhs_zsutank_base|Wheels|L1 [Indent level: 2],
        "l1": {
            "bonename": "",
            "center": "wheel_1_1_axis",
            "boundary": "wheel_1_1_bound",
            "maxdroop": 0,
            "maxcompression": 0,
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.33,
            "mass": 150,
            "moi": 10,
            "maxbraketorque": 8000,
            "sprungmass": -1,
            "springstrength": 150000,
            "springdamperrate": 11000,
            "dampingrate": 2174,
            "dampingrateinair": 2174,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.45],[0.18,1],[0.6,0.6]]
        },
        # Class: CfgVehicles|rhs_zsutank_base|Wheels|R2 [Indent level: 2],
        "r2": {
            "bonename": "wheel_podkolop1",
            "center": "wheel_2_2_axis",
            "boundary": "wheel_2_2_bound",
            "side": "right",
            "susptraveldirection": [0.125,-1,0],
            "steering": 0,
            "width": 0.33,
            "mass": 150,
            "moi": 10,
            "maxbraketorque": 8000,
            "sprungmass": -1,
            "springstrength": 150000,
            "springdamperrate": 11000,
            "dampingrate": 2174,
            "dampingrateinair": 2174,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.45],[0.18,1],[0.6,0.6]]
        },
        # Class: CfgVehicles|rhs_zsutank_base|Wheels|R3 [Indent level: 2],
        "r3": {
            "bonename": "wheel_podkolop2",
            "center": "wheel_2_3_axis",
            "boundary": "wheel_2_3_bound",
            "side": "right",
            "susptraveldirection": [0.125,-1,0],
            "steering": 0,
            "width": 0.33,
            "mass": 150,
            "moi": 10,
            "maxbraketorque": 8000,
            "sprungmass": -1,
            "springstrength": 150000,
            "springdamperrate": 11000,
            "dampingrate": 2174,
            "dampingrateinair": 2174,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.45],[0.18,1],[0.6,0.6]]
        },
        # Class: CfgVehicles|rhs_zsutank_base|Wheels|R4 [Indent level: 2],
        "r4": {
            "bonename": "wheel_podkolop3",
            "center": "wheel_2_4_axis",
            "boundary": "wheel_2_4_bound",
            "side": "right",
            "susptraveldirection": [0.125,-1,0],
            "steering": 0,
            "width": 0.33,
            "mass": 150,
            "moi": 10,
            "maxbraketorque": 8000,
            "sprungmass": -1,
            "springstrength": 150000,
            "springdamperrate": 11000,
            "dampingrate": 2174,
            "dampingrateinair": 2174,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.45],[0.18,1],[0.6,0.6]]
        },
        # Class: CfgVehicles|rhs_zsutank_base|Wheels|R5 [Indent level: 2],
        "r5": {
            "bonename": "wheel_podkolop4",
            "center": "wheel_2_5_axis",
            "boundary": "wheel_2_5_bound",
            "side": "right",
            "susptraveldirection": [0.125,-1,0],
            "steering": 0,
            "width": 0.33,
            "mass": 150,
            "moi": 10,
            "maxbraketorque": 8000,
            "sprungmass": -1,
            "springstrength": 150000,
            "springdamperrate": 11000,
            "dampingrate": 2174,
            "dampingrateinair": 2174,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.45],[0.18,1],[0.6,0.6]]
        },
        # Class: CfgVehicles|rhs_zsutank_base|Wheels|R6 [Indent level: 2],
        "r6": {
            "bonename": "wheel_podkolop5",
            "center": "wheel_2_6_axis",
            "boundary": "wheel_2_6_bound",
            "side": "right",
            "susptraveldirection": [0.125,-1,0],
            "steering": 0,
            "width": 0.33,
            "mass": 150,
            "moi": 10,
            "maxbraketorque": 8000,
            "sprungmass": -1,
            "springstrength": 150000,
            "springdamperrate": 11000,
            "dampingrate": 2174,
            "dampingrateinair": 2174,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.45],[0.18,1],[0.6,0.6]]
        },
        # Class: CfgVehicles|rhs_zsutank_base|Wheels|R7 [Indent level: 2],
        "r7": {
            "bonename": "wheel_podkolop6",
            "center": "wheel_2_7_axis",
            "boundary": "wheel_2_7_bound",
            "side": "right",
            "susptraveldirection": [0.125,-1,0],
            "steering": 0,
            "width": 0.33,
            "mass": 150,
            "moi": 10,
            "maxbraketorque": 8000,
            "sprungmass": -1,
            "springstrength": 150000,
            "springdamperrate": 11000,
            "dampingrate": 2174,
            "dampingrateinair": 2174,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.45],[0.18,1],[0.6,0.6]]
        },
        # Class: CfgVehicles|rhs_zsutank_base|Wheels|R9 [Indent level: 2],
        "r9": {
            "bonename": "wheel_podkolop9",
            "center": "wheel_2_9_axis",
            "boundary": "wheel_2_9_bound",
            "maxdroop": 0,
            "maxcompression": 0,
            "side": "right",
            "susptraveldirection": [0.125,-1,0],
            "steering": 0,
            "width": 0.33,
            "mass": 150,
            "moi": 10,
            "maxbraketorque": 8000,
            "sprungmass": -1,
            "springstrength": 150000,
            "springdamperrate": 11000,
            "dampingrate": 2174,
            "dampingrateinair": 2174,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.45],[0.18,1],[0.6,0.6]]
        },
        # Class: CfgVehicles|rhs_zsutank_base|Wheels|R1 [Indent level: 2],
        "r1": {
            "bonename": "",
            "center": "wheel_2_1_axis",
            "boundary": "wheel_2_1_bound",
            "maxdroop": 0,
            "maxcompression": 0,
            "side": "right",
            "susptraveldirection": [0.125,-1,0],
            "steering": 0,
            "width": 0.33,
            "mass": 150,
            "moi": 10,
            "maxbraketorque": 8000,
            "sprungmass": -1,
            "springstrength": 150000,
            "springdamperrate": 11000,
            "dampingrate": 2174,
            "dampingrateinair": 2174,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.45],[0.18,1],[0.6,0.6]]
        }
    },
    "accuracy": 0.3,
    "destrtype": "DestructDefault",
    "model": "rhsafrf|addons|rhs_a2port_armor|rhs_zsu",
    "picture": "rhsafrf|addons|rhs_a2port_armor|pictures|rhs_zsu23_pic_ca.paa",
    "icon": "rhsafrf|addons|rhs_a2port_armor|data|icomap_zsu_CA.paa",
    "crew": "rhs_msv_crew",
    "typicalcargo": [],
    "side": 0,
    "tracksspeed": 1,
    "irtarget": 1,
    "irtargetsize": 1,
    "visualtarget": 1,
    "visualtargetsize": 1,
    "radartarget": 1,
    "radartargetsize": 1.2,
    "receiveremotetargets": 1,
    "cost": 1.5e+006,
    "damageresistance": 0.02,
    "crewvulnerable": 1,
    "drivercompartments": "Compartment1",
    "getinaction": "GetInLow",
    "getoutaction": "GetOutLow",
    "driveraction": "RHS_ZSU_Driver",
    "driverinaction": "RHS_ZSU_Driver",
    "driverdoor": "hatchD",
    "forcehidedriver": 0,
    "driverforceoptics": 1,
    "viewdriverinexternal": 1,
    "loddriveropticsin": 0,
    "loddriveropticsout": 0,
    "loddriverturnedin": 0,
    "loddriverturnedout": 0,
    "unitinfotype": "RHS_RscUnitInfoEastTank",
    "mapsize": 6.5,
    "commandercansee": 31,
    "gunnercansee": "1+16+4+8",
    "threat": [0.5,0.5,1],
    "irscanground": 0,
    "irscanrangemax": 19000,
    "radartype": 4,
    "incomingmissiledetectionsystem": 0,
    "driveropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tnpo170a",
    "armor": 200,
    "armorstructural": 600,
    # Class: CfgVehicles|rhs_zsutank_base|ViewOptics [Indent level: 1],
    "viewoptics": {
        "initfov": 0.7,
        "minfov": 0.7,
        "maxfov": 0.7,
        "visionmode": ["Normal","NVG"],
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
    # Class: CfgVehicles|rhs_zsutank_base|HitPoints [Indent level: 1],
    "hitpoints": {
        # Class: CfgVehicles|rhs_zsutank_base|HitPoints|HitHull [Indent level: 2]
        "hithull": {
            "armor": 0.45,
            "material": -1,
            "name": "telo",
            "visual": "zbytek",
            "passthrough": 0,
            "minimalhit": 0.14,
            "explosionshielding": 0.5,
            "radius": 0.25,
            "armorcomponent": "hit_hull"
        },
        # Class: CfgVehicles|rhs_zsutank_base|HitPoints|HitEngine [Indent level: 2],
        "hitengine": {
            "armor": 0.45,
            "material": -1,
            "name": "motor",
            "visual": "zbytek",
            "passthrough": 0.01,
            "minimalhit": 0.03,
            "explosionshielding": 0.05,
            "radius": 0.2,
            # Class: CfgVehicles|rhs_zsutank_base|HitPoints|HitEngine|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_zsutank_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Smoke [Indent level: 4],
                "rhs_engine_smoke": {
                    "simulation": "particles",
                    "type": "SmallWreckSmoke",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|rhs_zsutank_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Fire [Indent level: 4],
                "rhs_engine_fire": {
                    "type": "SmallFireFPlace",
                    "simulation": "particles",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|rhs_zsutank_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Sparks [Indent level: 4],
                "rhs_engine_sparks": {
                    "type": "RHS_FireSparks",
                    "simulation": "particles",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|rhs_zsutank_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Sounds [Indent level: 4],
                "rhs_engine_sounds": {
                    "simulation": "sound",
                    "type": "Fire",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|rhs_zsutank_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Smoke_small1 [Indent level: 4],
                "rhs_engine_smoke_small1": {
                    "type": "WeaponWreckSmoke",
                    "position": "engine_smoke2",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|rhs_zsutank_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Smoke_small2 [Indent level: 4],
                "rhs_engine_smoke_small2": {
                    "position": "engine_smoke3",
                    "type": "WeaponWreckSmoke",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|rhs_zsutank_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Smoke_small3 [Indent level: 4],
                "rhs_engine_smoke_small3": {
                    "position": "engine_smoke4",
                    "simulation": "particles",
                    "type": "SmallWreckSmoke",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|rhs_zsutank_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Fire2 [Indent level: 4],
                "rhs_engine_fire2": {
                    "type": "SmallFireFPlace",
                    "position": "engine_smoke4",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|rhs_zsutank_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Sparks2 [Indent level: 4],
                "rhs_engine_sparks2": {
                    "type": "RHS_FireSparks",
                    "position": "engine_smoke4",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                }
            }
        },
        # Class: CfgVehicles|rhs_zsutank_base|HitPoints|HitLTrack [Indent level: 2],
        "hitltrack": {
            "armor": 0.5,
            "material": -1,
            "name": "pas_L",
            "passthrough": 0,
            "minimalhit": 0.15,
            "explosionshielding": 0.5,
            "radius": 0.3,
            "armorcomponent": "hit_trackL",
            "visual": "pas_L"
        },
        # Class: CfgVehicles|rhs_zsutank_base|HitPoints|HitRTrack [Indent level: 2],
        "hitrtrack": {
            "armor": 0.5,
            "material": -1,
            "name": "pas_P",
            "passthrough": 0,
            "minimalhit": 0.15,
            "explosionshielding": 0.5,
            "radius": 0.3,
            "armorcomponent": "hit_trackR",
            "visual": "pas_P"
        },
        # Class: CfgVehicles|APC_Tracked_02_base_F|HitPoints|HitFuel [Indent level: 2],
        "hitfuel": {
            "armor": 0.5,
            "material": -1,
            "armorcomponent": "hit_fuel",
            "name": "hit_fuel_point",
            "visual": "-",
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "explosionshielding": 0.6,
            "radius": 0.3
        },
        # Class: CfgVehicles|APC_Tracked_02_base_F|HitPoints|HitSLAT_Left_1 [Indent level: 2],
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
        # Class: CfgVehicles|APC_Tracked_02_base_F|HitPoints|HitSLAT_Left_2 [Indent level: 2],
        "hitslat_left_2": {
            "armorcomponent": "cage_left_2_geo",
            "name": "cage_left_2_point",
            "visual": "-",
            "simulation": "Armor_SLAT",
            "armor": -200,
            "minimalhit": 0.3,
            "passthrough": 0,
            "explosionshielding": 2,
            "radius": 0.25
        },
        # Class: CfgVehicles|APC_Tracked_02_base_F|HitPoints|HitSLAT_Left_3 [Indent level: 2],
        "hitslat_left_3": {
            "armorcomponent": "cage_left_3_geo",
            "name": "cage_left_3_point",
            "visual": "-",
            "simulation": "Armor_SLAT",
            "armor": -200,
            "minimalhit": 0.3,
            "passthrough": 0,
            "explosionshielding": 2,
            "radius": 0.25
        },
        # Class: CfgVehicles|APC_Tracked_02_base_F|HitPoints|HitSLAT_Right_1 [Indent level: 2],
        "hitslat_right_1": {
            "armorcomponent": "cage_right_1_geo",
            "name": "cage_right_1_point",
            "visual": "-",
            "simulation": "Armor_SLAT",
            "armor": -200,
            "minimalhit": 0.3,
            "passthrough": 0,
            "explosionshielding": 2,
            "radius": 0.25
        },
        # Class: CfgVehicles|APC_Tracked_02_base_F|HitPoints|HitSLAT_Right_2 [Indent level: 2],
        "hitslat_right_2": {
            "armorcomponent": "cage_right_2_geo",
            "name": "cage_right_2_point",
            "visual": "-",
            "simulation": "Armor_SLAT",
            "armor": -200,
            "minimalhit": 0.3,
            "passthrough": 0,
            "explosionshielding": 2,
            "radius": 0.25
        },
        # Class: CfgVehicles|APC_Tracked_02_base_F|HitPoints|HitSLAT_Right_3 [Indent level: 2],
        "hitslat_right_3": {
            "armorcomponent": "cage_right_3_geo",
            "name": "cage_right_3_point",
            "visual": "-",
            "simulation": "Armor_SLAT",
            "armor": -200,
            "minimalhit": 0.3,
            "passthrough": 0,
            "explosionshielding": 2,
            "radius": 0.25
        },
        # Class: CfgVehicles|APC_Tracked_02_base_F|HitPoints|HitSLAT_back [Indent level: 2],
        "hitslat_back": {
            "armorcomponent": "cage_back_geo",
            "name": "cage_back_point",
            "visual": "-",
            "simulation": "Armor_SLAT",
            "armor": -200,
            "minimalhit": 0.3,
            "passthrough": 0,
            "explosionshielding": 2,
            "radius": 0.25
        },
        # Class: CfgVehicles|APC_Tracked_02_base_F|HitPoints|HitSLAT_front [Indent level: 2],
        "hitslat_front": {
            "armorcomponent": "cage_front_geo",
            "name": "cage_front_point",
            "visual": "-",
            "simulation": "Armor_SLAT",
            "armor": -200,
            "minimalhit": 0.3,
            "passthrough": 0,
            "explosionshielding": 2,
            "radius": 0.25
        }
    },
    # Class: CfgVehicles|rhs_zsutank_base|RenderTargets [Indent level: 1],
    "rendertargets": {
    },
    # Class: CfgVehicles|rhs_zsutank_base|TransportMagazines [Indent level: 1],
    "transportmagazines": {
        # Class: CfgVehicles|rhs_zsutank_base|TransportMagazines|_xx_30Rnd_545x39_AK [Indent level: 2]
        "_xx_30rnd_545x39_ak": {
            "magazine": "rhs_30Rnd_545x39_7N10_AK",
            "count": "10"
        },
        # Class: CfgVehicles|rhs_zsutank_base|TransportMagazines|_xx_HandGrenade_East [Indent level: 2],
        "_xx_handgrenade_east": {
            "magazine": "rhs_mag_rgd5",
            "count": "10"
        },
        # Class: CfgVehicles|rhs_zsutank_base|TransportMagazines|_xx_signal_rounds [Indent level: 2],
        "_xx_signal_rounds": {
            "magazine": "rhs_mag_nspn_red",
            "count": "10"
        }
    },
    # Class: CfgVehicles|rhs_zsutank_base|TransportWeapons [Indent level: 1],
    "transportweapons": {
        # Class: CfgVehicles|rhs_zsutank_base|TransportWeapons|_xx_AK74M [Indent level: 2]
        "_xx_ak74m": {
            "weapon": "rhs_weap_ak74m",
            "count": 1
        }
    },
    # Class: CfgVehicles|rhs_zsutank_base|TransportItems [Indent level: 1],
    "transportitems": {
        # Class: CfgVehicles|rhs_zsutank_base|TransportItems|_xx_FirstAidKit [Indent level: 2]
        "_xx_firstaidkit": {
            "name": "FirstAidKit",
            "count": 4
        }
    },
    "hiddenselections": ["camo1","camo2","camo3","n1","n2","n3"],
    "hiddenselectionstextures": ["|rhsafrf|addons|rhs_a2port_armor|data|zsu_01_co.paa","|rhsafrf|addons|rhs_a2port_armor|data|zsu_02_co.paa","|rhsafrf|addons|rhs_a2port_armor|data|zsu_03_co.paa","rhsafrf|addons|rhs_decals|Data|Labels|Misc|no_ca.paa","rhsafrf|addons|rhs_decals|Data|Labels|Misc|no_ca.paa","rhsafrf|addons|rhs_decals|Data|Labels|Misc|no_ca.paa"],
    # Class: CfgVehicles|rhs_zsutank_base|textureSources [Indent level: 1],
    "texturesources": {
        # Class: CfgVehicles|rhs_zsutank_base|textureSources|standard [Indent level: 2]
        "standard": {
            "displayname": "Standard",
            "textures": ["|rhsafrf|addons|rhs_a2port_armor|data|zsu_01_co.paa","|rhsafrf|addons|rhs_a2port_armor|data|zsu_02_co.paa","|rhsafrf|addons|rhs_a2port_armor|data|zsu_03_co.paa"],
            "factions": ["rhs_faction_vpvo"]
        },
        # Class: CfgVehicles|rhs_zsutank_base|textureSources|Chdkz [Indent level: 2],
        "chdkz": {
            "displayname": "Chedaki",
            "textures": ["|rhsafrf|addons|rhs_a2port_armor|data|zsu_01_gue_co.paa","|rhsafrf|addons|rhs_a2port_armor|data|zsu_02_gue_co.paa","|rhsafrf|addons|rhs_a2port_armor|data|zsu_03_gue_co.paa"],
            "factions": []
        },
        # Class: CfgVehicles|rhs_zsutank_base|textureSources|rhs_sand [Indent level: 2],
        "rhs_sand": {
            "displayname": "Sand",
            "author": "beaar",
            "textures": ["|rhsafrf|addons|rhs_a2port_armor_camo|data|zsu_01_des_co.paa","|rhsafrf|addons|rhs_a2port_armor_camo|data|zsu_02_des_co.paa","|rhsafrf|addons|rhs_a2port_armor_camo|data|zsu_03_des_co.paa"],
            "factions": []
        },
        # Class: CfgVehicles|rhs_zsutank_base|textureSources|CDF [Indent level: 2],
        "cdf": {
            "displayname": "CDF",
            "author": "Red Hammer Studios",
            "textures": ["|rhsgref|addons|rhsgref_vehicles_ret|data|cdf|zsu_01_cdf_co.paa","|rhsgref|addons|rhsgref_vehicles_ret|data|cdf|zsu_02_cdf_co.paa","|rhsgref|addons|rhsgref_vehicles_ret|data|cdf|zsu_03_cdf_co.paa"],
            "factions": []
        },
        # Class: CfgVehicles|rhs_zsutank_base|textureSources|Takistan [Indent level: 2],
        "takistan": {
            "displayname": "Takistan",
            "author": "Red Hammer Studios",
            "textures": ["|rhsgref|addons|rhsgref_vehicles_ret|data|tak|zsu_01_tk_co.paa","|rhsgref|addons|rhsgref_vehicles_ret|data|tak|zsu_02_tk_co.paa","|rhsgref|addons|rhsgref_vehicles_ret|data|tak|zsu_03_tk_co.paa"],
            "factions": []
        }
    },
    "texturelist": [],
    # Class: CfgVehicles|rhs_zsutank_base|Attributes [Indent level: 1],
    "attributes": {
        # Class: CfgVehicles|rhs_zsutank_base|Attributes|ObjectTexture [Indent level: 2]
        "objecttexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayname": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        # Class: CfgVehicles|rhs_zsutank_base|Attributes|rhs_decalNumber_type [Indent level: 2],
        "rhs_decalnumber_type": {
            "displayname": "Define font type of plate number",
            "tooltip": "Define kind of font that will be drawn on vehicle.",
            "property": "rhs_decalNumber_type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value,true];[_this,[['Number', cRHSZSUNumberPlaces, _value]]] call rhs_fnc_decalsInit",
            "defaultvalue": 0,
            "typename": "STRING",
            # Class: CfgVehicles|rhs_zsutank_base|Attributes|rhs_decalNumber_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_zsutank_base|Attributes|rhs_decalNumber_type|values|Default [Indent level: 4]
                "default": {
                    "name": "Default",
                    "value": "Default",
                    "defaultvalue": "Default"
                },
                # Class: CfgVehicles|rhs_zsutank_base|Attributes|rhs_decalNumber_type|values|DefaultRed [Indent level: 4],
                "defaultred": {
                    "name": "Default (Red)",
                    "value": "DefaultRed"
                },
                # Class: CfgVehicles|rhs_zsutank_base|Attributes|rhs_decalNumber_type|values|BoldRed [Indent level: 4],
                "boldred": {
                    "name": "Bold Red",
                    "value": "BoldRed"
                },
                # Class: CfgVehicles|rhs_zsutank_base|Attributes|rhs_decalNumber_type|values|CDF [Indent level: 4],
                "cdf": {
                    "name": "CDF",
                    "value": "CDF"
                },
                # Class: CfgVehicles|rhs_zsutank_base|Attributes|rhs_decalNumber_type|values|Handpaint [Indent level: 4],
                "handpaint": {
                    "name": "Handpaint",
                    "value": "Handpaint"
                },
                # Class: CfgVehicles|rhs_zsutank_base|Attributes|rhs_decalNumber_type|values|HandpaintBlack [Indent level: 4],
                "handpaintblack": {
                    "name": "Handpaint Black",
                    "value": "HandpaintBlack"
                },
                # Class: CfgVehicles|rhs_zsutank_base|Attributes|rhs_decalNumber_type|values|Iraqi [Indent level: 4],
                "iraqi": {
                    "name": "Iraqi",
                    "value": "Iraqi"
                },
                # Class: CfgVehicles|rhs_zsutank_base|Attributes|rhs_decalNumber_type|values|LicensePlate [Indent level: 4],
                "licenseplate": {
                    "name": "License Plate",
                    "value": "LicensePlate"
                }
            }
        },
        # Class: CfgVehicles|rhs_zsutank_base|Attributes|rhs_decalNumber [Indent level: 2],
        "rhs_decalnumber": {
            "collapsed": 1,
            "displayname": "Set side number",
            "tooltip": "Set side number. 4 numbers are required. Type 0 to hide numbers complety & leave at -1 to get random number",
            "property": "rhs_decalNumber",
            "control": "Edit",
            "validate": "Number",
            "typename": "Number",
            "defaultvalue": "-1",
            "expression": "if( _value >= 0)then{if( _value == 0)then{{[_this setobjectTexture [_x,'a3|data_f|clear_empty.paa']]}foreach cRHSZSUNumberPlaces}else{[_this, [['Number', cRHSZSUNumberPlaces, _this getVariable ['rhs_decalNumber_type','Default'], _value] ] ] call rhs_fnc_decalsInit}};"
        }
    },
    # Class: CfgVehicles|rhs_zsutank_base|Turrets [Indent level: 1],
    "turrets": {
        # Class: CfgVehicles|rhs_zsutank_base|Turrets|MainTurret [Indent level: 2]
        "mainturret": {
            # Class: CfgVehicles|rhs_zsutank_base|Turrets|MainTurret|Turrets [Indent level: 3]
            "turrets": {
                # Class: CfgVehicles|rhs_zsutank_base|Turrets|MainTurret|Turrets|CommanderOptics [Indent level: 4]
                "commanderoptics": {
                    "gunbeg": "gun_muzzle",
                    "gunend": "gun_chamber",
                    "body": "ObsTurret",
                    "gun": "ObsGun",
                    "gunneroutopticsmodel": "",
                    "memorypointgunneroutoptics": "commanderview",
                    "memorypointgunneroptics": "commanderview",
                    "lodturnedout": 1100,
                    "gunneropticseffect": ["TankCommanderOptics1"],
                    "weapons": [],
                    "magazines": [],
                    "turretinfotype": "RscWeaponEmpty",
                    "forcehidegunner": 0,
                    "gunnerinaction": "RHS_ZSU_Commander",
                    "gunneraction": "RHS_ZSU_CommanderOut",
                    "gunnerdoor": "hatchC",
                    "gunnerforceoptics": 1,
                    "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tkn3.p3d",
                    "minelev": -10,
                    "maxelev": 60,
                    "initelev": 0,
                    "minturn": -360,
                    "maxturn": 360,
                    "initturn": 0,
                    # Class: CfgVehicles|rhs_zsutank_base|Turrets|MainTurret|Turrets|CommanderOptics|ViewOptics [Indent level: 5],
                    "viewoptics": {
                        "initfov": 0.111,
                        "minfov": 0.111,
                        "maxfov": 0.111,
                        "visionmode": ["Normal","NVG"],
                        "initanglex": 0,
                        "minanglex": -30,
                        "maxanglex": 30,
                        "initangley": 0,
                        "minangley": -100,
                        "maxangley": 100,
                        "thermalmode": [0,1],
                        "minmovex": 0,
                        "maxmovex": 0,
                        "minmovey": 0,
                        "maxmovey": 0,
                        "minmovez": 0,
                        "maxmovez": 0
                    },
                    "startengine": 0,
                    "outgunnermayfire": 0,
                    "maxhorizontalrotspeed": 2,
                    "maxverticalrotspeed": 2,
                    "ingunnermayfire": 1,
                    "viewgunnerinexternal": 1,
                    # Class: CfgVehicles|rhs_zsutank_base|Turrets|MainTurret|Turrets|CommanderOptics|OpticsIn [Indent level: 5],
                    "opticsin": {
                        # Class: CfgVehicles|rhs_zsutank_base|Turrets|MainTurret|Turrets|CommanderOptics|OpticsIn|Wide [Indent level: 6]
                        "wide": {
                            "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tkn3.p3d",
                            "gunneroutopticsmodel": "",
                            "initfov": 0.111,
                            "minfov": 0.111,
                            "maxfov": 0.111,
                            "visionmode": ["Normal","NVG"],
                            "initanglex": 0,
                            "minanglex": -30,
                            "maxanglex": 30,
                            "initangley": 0,
                            "minangley": -100,
                            "maxangley": 100,
                            "thermalmode": [0,1],
                            "minmovex": 0,
                            "maxmovex": 0,
                            "minmovey": 0,
                            "maxmovey": 0,
                            "minmovez": 0,
                            "maxmovez": 0
                        },
                        # Class: CfgVehicles|rhs_zsutank_base|Turrets|MainTurret|Turrets|CommanderOptics|OpticsIn|Periscope [Indent level: 6],
                        "periscope": {
                            "initanglex": 0,
                            "minanglex": -30,
                            "maxanglex": 30,
                            "initangley": 0,
                            "minangley": -100,
                            "maxangley": 100,
                            "initfov": 0.26,
                            "minfov": 0.26,
                            "maxfov": 0.26,
                            "visionmode": ["Normal"],
                            "gunneropticsmodel": "a3|weapons_f|reticle|Optics_Driver_01_f",
                            "gunneropticseffect": ["TankGunnerOptics1","OpticsBlur2","OpticsCHAbera2"],
                            "thermalmode": [0,1],
                            "minmovex": 0,
                            "maxmovex": 0,
                            "minmovey": 0,
                            "maxmovey": 0,
                            "minmovez": 0,
                            "maxmovez": 0
                        }
                    },
                    # Class: CfgVehicles|rhs_zsutank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components [Indent level: 5],
                    "components": {
                        # Class: CfgVehicles|rhs_zsutank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components|AICarSteeringComponent [Indent level: 6]
                        "aicarsteeringcomponent": {
                            "steeringpidweights": [1.2,0.1,0.2],
                            "speedpidweights": [1.7,1.3,1.1],
                            "doremapspeed": 1,
                            "remapspeedrange": [40,50],
                            "remapspeedscalar": [1,0.35],
                            "dopredictforward": 1,
                            "predictforwardrange": [0.1,20],
                            "steeraheadsaturation": [0.01,0.4],
                            "speedpredictionmethod": 1,
                            "wheelanglecoef": 0.7,
                            "forwardanglecoef": 0.7,
                            "steeringanglecoef": 1,
                            "differenceanglecoef": 1,
                            "stuckmaxtime": 3,
                            "allowovertaking": 1,
                            "allowcollisionavoidance": 1,
                            "allowdrifting": 0,
                            "maxwheelanglediff": 0.2616,
                            "minspeedtokeep": 0.1,
                            "commandturnfactor": 1
                        },
                        # Class: CfgVehicles|rhs_zsutank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 6],
                        "vehiclesystemsdisplaymanagercomponentleft": {
                            # Class: CfgVehicles|rhs_zsutank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentLeft|Components [Indent level: 7]
                            "components": {
                                # Class: CfgVehicles|rhs_zsutank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentLeft|Components|EmptyDisplay [Indent level: 8]
                                "emptydisplay": {
                                    "componenttype": "EmptyDisplayComponent"
                                },
                                # Class: CfgVehicles|rhs_zsutank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentLeft|Components|CrewDisplay [Indent level: 8],
                                "crewdisplay": {
                                    "componenttype": "CrewDisplayComponent",
                                    "resource": "RscCustomInfoCrew"
                                },
                                # Class: CfgVehicles|rhs_zsutank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentLeft|Components|SensorDisplay [Indent level: 8],
                                "sensordisplay": {
                                    "componenttype": "SensorsDisplayComponent",
                                    "range": [2000,4000,8000,14000],
                                    "resource": "RscCustomInfoSensors"
                                }
                            },
                            "componenttype": "VehicleSystemsDisplayManager",
                            "left": 1,
                            "defaultdisplay": "EmptyDisplay",
                            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,	(safezoneX + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40))])",
                            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                        },
                        # Class: CfgVehicles|rhs_zsutank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 6],
                        "vehiclesystemsdisplaymanagercomponentright": {
                            "defaultdisplay": "SensorDisplay",
                            # Class: CfgVehicles|rhs_zsutank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentRight|Components [Indent level: 7],
                            "components": {
                                # Class: CfgVehicles|rhs_zsutank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentRight|Components|EmptyDisplay [Indent level: 8]
                                "emptydisplay": {
                                    "componenttype": "EmptyDisplayComponent"
                                },
                                # Class: CfgVehicles|rhs_zsutank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentRight|Components|CrewDisplay [Indent level: 8],
                                "crewdisplay": {
                                    "componenttype": "CrewDisplayComponent",
                                    "resource": "RscCustomInfoCrew"
                                },
                                # Class: CfgVehicles|rhs_zsutank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentRight|Components|SensorDisplay [Indent level: 8],
                                "sensordisplay": {
                                    "componenttype": "SensorsDisplayComponent",
                                    "range": [2000,4000,8000,14000],
                                    "resource": "RscCustomInfoSensors"
                                }
                            },
                            "componenttype": "VehicleSystemsDisplayManager",
                            "right": 1,
                            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,	((safezoneX + safezoneW) - (		(10 * 			(			((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40)))])",
                            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                        }
                    },
                    "mincamelev": -90,
                    "maxcamelev": 90,
                    "soundservo": ["A3|Sounds_F|vehicles|armor|APC|noises|servo_APC_comm",0.562341,1,30],
                    "soundservovertical": ["A3|Sounds_F|vehicles|armor|APC|noises|servo_APC_comm",0.562341,1,30],
                    "gunnergetinaction": "GetInAMV_cargo",
                    "gunnergetoutaction": "GetOutLow",
                    "usepip": 2,
                    "turretfollowfreelook": 2,
                    "lodopticsin": 0,
                    "ispersonturret": 1,
                    "personturretaction": "vehicle_turnout_1",
                    "minoutelev": -20,
                    "maxoutelev": 40,
                    "initoutelev": 0,
                    "minoutturn": -150,
                    "maxoutturn": 120,
                    "initoutturn": 0,
                    "animationsourcestickx": "com_turret_control_x",
                    "animationsourcesticky": "com_turret_control_y",
                    "gunnerlefthandanimname": "com_turret_control",
                    "viewgunnershadowamb": 0.5,
                    "viewgunnershadowdiff": 0.05,
                    # Class: CfgVehicles|APC_Tracked_02_base_F|Turrets|MainTurret|Turrets|CommanderOptics|ViewGunner [Indent level: 5],
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
                    "showcrewaim": 1,
                    # Class: CfgVehicles|APC_Tracked_02_base_F|Turrets|MainTurret|Turrets|CommanderOptics|HitPoints [Indent level: 5],
                    "hitpoints": {
                        # Class: CfgVehicles|APC_Tracked_02_base_F|Turrets|MainTurret|Turrets|CommanderOptics|HitPoints|HitComTurret [Indent level: 6]
                        "hitcomturret": {
                            "armor": 0.08,
                            "material": -1,
                            "armorcomponent": "hit_com_turret",
                            "name": "hit_com_turret_point",
                            "visual": "vezVelitele",
                            "passthrough": 0.4,
                            "minimalhit": 0.1,
                            "explosionshielding": 1,
                            "radius": 0.15,
                            "isturret": 1
                        },
                        # Class: CfgVehicles|APC_Tracked_02_base_F|Turrets|MainTurret|Turrets|CommanderOptics|HitPoints|HitComGun [Indent level: 6],
                        "hitcomgun": {
                            "armor": 0.04,
                            "material": -1,
                            "armorcomponent": "hit_com_gun",
                            "name": "hit_com_gun_point",
                            "visual": "zbranVelitele",
                            "passthrough": 0,
                            "minimalhit": 0.1,
                            "explosionshielding": 1,
                            "radius": 0.15,
                            "isgun": 1
                        }
                    },
                    "stabilizedinaxes": 3,
                    "gunnerhasflares": 1,
                    "proxytype": "CPCommander",
                    "proxyindex": 1,
                    "gunnername": "Commander",
                    "primarygunner": 0,
                    "primaryobserver": 1,
                    "animationsourcebody": "obsTurret",
                    "animationsourcegun": "obsGun",
                    "animationsourcehatch": "hatchCommander",
                    "animationsourcecamelev": "camElev",
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
                    "hideweaponsgunner": 1,
                    "canhidegunner": -1,
                    "showhmd": 0,
                    "lockwhendriverout": 0,
                    "lockwhenvehiclespeed": -1,
                    "gunnercompartments": "Compartment1",
                    "lodturnedin": -1,
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
                    "gunnerrighthandanimname": "",
                    "gunnerleftleganimname": "",
                    "gunnerrightleganimname": "",
                    "precisegetinout": 0,
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
                    }
                }
            },
            # Class: CfgVehicles|rhs_zsutank_base|Turrets|MainTurret|Components [Indent level: 3],
            "components": {
                # Class: CfgVehicles|rhs_zsutank_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 4]
                "vehiclesystemsdisplaymanagercomponentleft": {
                    # Class: CfgVehicles|rhs_zsutank_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft|Components [Indent level: 5]
                    "components": {
                        # Class: CfgVehicles|rhs_zsutank_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft|Components|EmptyDisplay [Indent level: 6]
                        "emptydisplay": {
                            "componenttype": "EmptyDisplayComponent"
                        },
                        # Class: CfgVehicles|rhs_zsutank_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft|Components|CrewDisplay [Indent level: 6],
                        "crewdisplay": {
                            "componenttype": "CrewDisplayComponent",
                            "resource": "RscCustomInfoCrew"
                        },
                        # Class: CfgVehicles|rhs_zsutank_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft|Components|SensorDisplay [Indent level: 6],
                        "sensordisplay": {
                            "componenttype": "SensorsDisplayComponent",
                            "range": [2000,4000,8000,16000],
                            "resource": "RscCustomInfoSensors"
                        }
                    },
                    "componenttype": "VehicleSystemsDisplayManager",
                    "left": 1,
                    "defaultdisplay": "EmptyDisplay",
                    "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,	(safezoneX + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40))])",
                    "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                },
                # Class: CfgVehicles|rhs_zsutank_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 4],
                "vehiclesystemsdisplaymanagercomponentright": {
                    "defaultdisplay": "SensorDisplay",
                    # Class: CfgVehicles|rhs_zsutank_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight|Components [Indent level: 5],
                    "components": {
                        # Class: CfgVehicles|rhs_zsutank_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight|Components|EmptyDisplay [Indent level: 6]
                        "emptydisplay": {
                            "componenttype": "EmptyDisplayComponent"
                        },
                        # Class: CfgVehicles|rhs_zsutank_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight|Components|CrewDisplay [Indent level: 6],
                        "crewdisplay": {
                            "componenttype": "CrewDisplayComponent",
                            "resource": "RscCustomInfoCrew"
                        },
                        # Class: CfgVehicles|rhs_zsutank_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight|Components|SensorDisplay [Indent level: 6],
                        "sensordisplay": {
                            "componenttype": "SensorsDisplayComponent",
                            "range": [2000,4000,8000,16000],
                            "resource": "RscCustomInfoSensors"
                        }
                    },
                    "componenttype": "VehicleSystemsDisplayManager",
                    "right": 1,
                    "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,	((safezoneX + safezoneW) - (		(10 * 			(			((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40)))])",
                    "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                }
            },
            "lodturnedout": 1100,
            "weapons": ["RHS_weap_AZP23"],
            "magazines": ["rhs_mag_AZP23_2000"],
            "forcehidegunner": 0,
            "minelev": -4.5,
            "maxelev": 85,
            "minturn": -360,
            "maxturn": 360,
            "maxhorizontalrotspeed": 0.94,
            "maxverticalrotspeed": 0.6,
            # Class: CfgVehicles|rhs_zsutank_base|Turrets|MainTurret|OpticsIn [Indent level: 3],
            "opticsin": {
                # Class: CfgVehicles|rhs_zsutank_base|Turrets|MainTurret|OpticsIn|Wide [Indent level: 4]
                "wide": {
                    "initfov": 0.35,
                    "minfov": 0.35,
                    "maxfov": 0.35,
                    "gunneropticsmodel": "rhsafrf|addons|rhs_a2port_armor|2Dscope_RUAA8",
                    "gunneroutopticsmodel": "",
                    "visionmode": ["Normal"],
                    "gunneropticseffect": ["TankGunnerOptics1","OpticsBlur2","OpticsCHAbera2"],
                    "initanglex": 0,
                    "minanglex": -30,
                    "maxanglex": 30,
                    "initangley": 0,
                    "minangley": -100,
                    "maxangley": 100,
                    "thermalmode": [0,1],
                    "minmovex": 0,
                    "maxmovex": 0,
                    "minmovey": 0,
                    "maxmovey": 0,
                    "minmovez": 0,
                    "maxmovez": 0
                },
                # Class: CfgVehicles|rhs_zsutank_base|Turrets|MainTurret|OpticsIn|Auto [Indent level: 4],
                "auto": {
                    "initfov": 0.175,
                    "minfov": 0.175,
                    "maxfov": 0.175,
                    "directionstabilized": 1,
                    "gunneropticsmodel": "rhsafrf|addons|rhs_a2port_armor|2Dscope_RUAA8",
                    "gunneroutopticsmodel": "",
                    "visionmode": ["Normal"],
                    "gunneropticseffect": ["TankGunnerOptics1","OpticsBlur2","OpticsCHAbera2"],
                    "initanglex": 0,
                    "minanglex": -30,
                    "maxanglex": 30,
                    "initangley": 0,
                    "minangley": -100,
                    "maxangley": 100,
                    "thermalmode": [0,1],
                    "minmovex": 0,
                    "maxmovex": 0,
                    "minmovey": 0,
                    "maxmovey": 0,
                    "minmovez": 0,
                    "maxmovez": 0
                }
            },
            "gunneraction": "RHS_ZSU_GunnerOut",
            "gunnerinaction": "RHS_ZSU_Gunner",
            "gunnerforceoptics": 1,
            # Class: CfgVehicles|rhs_zsutank_base|Turrets|MainTurret|ViewOptics [Indent level: 3],
            "viewoptics": {
                "initanglex": 0,
                "minanglex": -30,
                "maxanglex": 30,
                "initangley": 0,
                "minangley": -100,
                "maxangley": 100,
                "initfov": 0.2,
                "minfov": 0.058,
                "maxfov": 0.2,
                "visionmode": ["Normal","NVG"]
            },
            "gunnerdoor": "hatchG",
            "memorypointgun": ["chase01","chase02","chase03","chase04"],
            "turretinfotype": "RscWeaponZeroing",
            "discretedistance": [100,200,300,400,500,600,700,800,900,1000],
            "discretedistanceinitindex": 5,
            "selectionfireanim": "zasleh",
            "viewgunnerinexternal": 1,
            # Class: CfgVehicles|rhs_zsutank_base|Turrets|MainTurret|HitPoints [Indent level: 3],
            "hitpoints": {
                # Class: CfgVehicles|rhs_zsutank_base|Turrets|MainTurret|HitPoints|HitTurret [Indent level: 4]
                "hitturret": {
                    "armor": 0.5,
                    "material": -1,
                    "name": "vez",
                    "visual": "vez",
                    "passthrough": 0,
                    "minimalhit": 0.14,
                    "explosionshielding": 0.001,
                    "radius": 0.2
                },
                # Class: CfgVehicles|rhs_zsutank_base|Turrets|MainTurret|HitPoints|HitGun [Indent level: 4],
                "hitgun": {
                    "armor": 0.6,
                    "material": -1,
                    "name": "zbran",
                    "visual": "-",
                    "passthrough": 0,
                    "minimalhit": 0.13,
                    "explosionshielding": 0.001,
                    "radius": 0.2
                }
            },
            "body": "mainTurret",
            "gun": "mainGun",
            "soundservo": ["A3|Sounds_F|vehicles|armor|APC|noises|servo_APC_gunner",0.562341,1,10],
            "soundservovertical": ["A3|Sounds_F|vehicles|armor|APC|noises|servo_APC_gunner_vertical",0.562341,1,30],
            "initelev": 1,
            "mincamelev": -90,
            "maxcamelev": 90,
            "gunnergetinaction": "GetInAMV_cargo",
            "gunnergetoutaction": "GetOutLow",
            "castgunnershadow": 1,
            "startengine": 0,
            "stabilizedinaxes": 3,
            "gunneropticsmodel": "A3|weapons_f|reticle|Optics_Gunner_02_F",
            "gunneroutopticsmodel": "",
            "usepip": 1,
            "lodopticsin": 0,
            "ispersonturret": 1,
            "personturretaction": "vehicle_turnout_2",
            "minoutelev": -20,
            "maxoutelev": 40,
            "initoutelev": 0,
            "minoutturn": -120,
            "maxoutturn": 150,
            "initoutturn": 0,
            "animationsourcestickx": "turret_control_x",
            "animationsourcesticky": "turret_control_y",
            "gunnerlefthandanimname": "turret_control",
            "viewgunnershadowamb": 0.5,
            "viewgunnershadowdiff": 0.05,
            "memorypointgunneroptics": "gunnerview",
            # Class: CfgVehicles|APC_Tracked_02_base_F|Turrets|MainTurret|ViewGunner [Indent level: 3],
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
            "showcrewaim": 2,
            "commanding": 1,
            "gunbeg": "usti hlavne",
            "gunend": "konec hlavne",
            "memorypointsgetingunner": "pos gunner",
            "memorypointsgetingunnerdir": "pos gunner dir",
            "primarygunner": 1,
            "gunneroutopticseffect": [],
            "gunneropticseffect": ["TankGunnerOptics2","OpticsBlur1","OpticsCHAbera1"],
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
            "initturn": 0,
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
            "viewgunnershadow": 1,
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
            "gunnerrighthandanimname": "",
            "gunnerleftleganimname": "",
            "gunnerrightleganimname": "",
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
            }
        }
    },
    # Class: CfgVehicles|rhs_zsutank_base|Damage [Indent level: 1],
    "damage": {
        "tex": [],
        "mat": ["rhsafrf|addons|rhs_a2port_armor|data|ZSU_01.rvmat","rhsafrf|addons|rhs_a2port_armor|data|ZSU_01_damage.rvmat","rhsafrf|addons|rhs_a2port_armor|data|ZSU_01_destruct.rvmat","rhsafrf|addons|rhs_a2port_armor|data|ZSU_02.rvmat","rhsafrf|addons|rhs_a2port_armor|data|ZSU_02_damage.rvmat","rhsafrf|addons|rhs_a2port_armor|data|ZSU_02_destruct.rvmat","rhsafrf|addons|rhs_a2port_armor|data|ZSU_03.rvmat","rhsafrf|addons|rhs_a2port_armor|data|ZSU_03_damage.rvmat","rhsafrf|addons|rhs_a2port_armor|data|ZSU_03_destruct.rvmat","rhsafrf|addons|rhs_a2port_armor|data|ZSU_track.rvmat","rhsafrf|addons|rhs_a2port_armor|data|ZSU_track_damage.rvmat","rhsafrf|addons|rhs_a2port_armor|data|ZSU_track_destruct.rvmat","a3|data_f|default.rvmat","a3|data_f|default.rvmat","a3|data_f|default_destruct.rvmat"]
    },
    # Class: CfgVehicles|rhs_zsutank_base|AnimationSources [Indent level: 1],
    "animationsources": {
        # Class: CfgVehicles|rhs_zsutank_base|AnimationSources|HatchC [Indent level: 2]
        "hatchc": {
            "source": "door",
            "animperiod": 2.1
        },
        # Class: CfgVehicles|rhs_zsutank_base|AnimationSources|HatchG [Indent level: 2],
        "hatchg": {
            "source": "door",
            "animperiod": 2.1
        },
        # Class: CfgVehicles|rhs_zsutank_base|AnimationSources|HatchD [Indent level: 2],
        "hatchd": {
            "source": "door",
            "animperiod": 2.1
        },
        # Class: CfgVehicles|rhs_zsutank_base|AnimationSources|muzzle_rot1 [Indent level: 2],
        "muzzle_rot1": {
            "weapon": "RHS_weap_AZP23",
            "source": "ammorandom"
        }
    },
    # Class: CfgVehicles|rhs_zsutank_base|Reflectors [Indent level: 1],
    "reflectors": {
        # Class: CfgVehicles|rhs_zsutank_base|Reflectors|Left [Indent level: 2]
        "left": {
            "color": [190,130,95],
            "ambient": [0.1,0.1,0.1,1],
            "position": "L svetlo",
            "direction": "konec L svetla",
            "hitpoint": "L svetlo",
            "selection": "L svetlo",
            "size": 1,
            "innerangle": 100,
            "outerangle": 179,
            "conefadecoef": 10,
            "intensity": 1,
            "useflare": 0,
            "daylight": 0,
            "flaresize": 1,
            # Class: CfgVehicles|rhs_zsutank_base|Reflectors|Left|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardlimitstart": 30,
                "hardlimitend": 60
            }
        },
        # Class: CfgVehicles|rhs_zsutank_base|Reflectors|Right [Indent level: 2],
        "right": {
            "position": "P svetlo",
            "direction": "konec P svetla",
            "hitpoint": "P svetlo",
            "selection": "P svetlo",
            "color": [190,130,95],
            "ambient": [0.1,0.1,0.1,1],
            "size": 1,
            "innerangle": 100,
            "outerangle": 179,
            "conefadecoef": 10,
            "intensity": 1,
            "useflare": 0,
            "daylight": 0,
            "flaresize": 1,
            # Class: CfgVehicles|rhs_zsutank_base|Reflectors|Left|Attenuation [Indent level: 3],
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
    "aggregatereflectors": [["Left","Right"]],
    # Class: CfgVehicles|rhs_zsutank_base|Exhausts [Indent level: 1],
    "exhausts": {
        # Class: CfgVehicles|rhs_zsutank_base|Exhausts|Exhaust1 [Indent level: 2]
        "exhaust1": {
            "position": "exhaust",
            "direction": "exhaust_dir",
            "effect": "ExhaustEffectTankBack"
        }
    },
    # Class: CfgVehicles|rhs_zsutank_base|Components [Indent level: 1],
    "components": {
        # Class: CfgVehicles|rhs_zsutank_base|Components|SensorsManagerComponent [Indent level: 2]
        "sensorsmanagercomponent": {
            # Class: CfgVehicles|rhs_zsutank_base|Components|SensorsManagerComponent|Components [Indent level: 3]
            "components": {
                # Class: CfgVehicles|rhs_zsutank_base|Components|SensorsManagerComponent|Components|ActiveRadarSensorComponent [Indent level: 4]
                "activeradarsensorcomponent": {
                    # Class: CfgVehicles|rhs_zsutank_base|Components|SensorsManagerComponent|Components|ActiveRadarSensorComponent|AirTarget [Indent level: 5]
                    "airtarget": {
                        "minrange": 14000,
                        "maxrange": 14000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    # Class: CfgVehicles|rhs_zsutank_base|Components|SensorsManagerComponent|Components|ActiveRadarSensorComponent|GroundTarget [Indent level: 5],
                    "groundtarget": {
                        "minrange": -1,
                        "maxrange": -1,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    "anglerangehorizontal": 360,
                    "anglerangevertical": 100,
                    "typerecognitiondistance": 4000,
                    "groundnoisedistancecoef": 0.05,
                    "maxgroundnoisedistance": 60,
                    "minspeedthreshold": 20,
                    "maxspeedthreshold": 90,
                    "maxfogseethrough": 1,
                    "aimdown": -35,
                    "mintrackablespeed": 25,
                    "maxtrackablespeed": 555,
                    "mintrackableatl": 50,
                    "componenttype": "ActiveRadarSensorComponent",
                    "color": [0,1,1,1],
                    "allowsmarking": 1,
                    "animdirection": "",
                    "maxtrackableatl": 1e+010
                }
            }
        },
        # Class: CfgVehicles|Tank_F|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 2],
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
    # Class: CfgVehicles|rhs_zsutank_base|EventHandlers [Indent level: 1],
    "eventhandlers": {
        # Class: CfgVehicles|rhs_zsutank_base|EventHandlers|RHS_EventHandlers [Indent level: 2]
        "rhs_eventhandlers": {
            "init": "_this call rhs_fnc_bmp3_init",
            "getout": "_this call rhs_fnc_hatchAbandon"
        },
        "init": "if (local (_this select 0)) then {[(_this select 0), `, [], false] call bis_fnc_initVehicle;};",
        "fired": "[_this select 0,_this select 6,'missile_move','MissileBase'] call BIS_fnc_missileLaunchPositionFix; _this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');",
        # Class: DefaultEventHandlers|RHS_DefaultEventhandlers [Indent level: 0],
        "rhs_defaulteventhandlers": {
            "hitpart": "_this call rhs_fnc_hitPart"
        }
    },
    "attenuationeffecttype": "TankAttenuation",
    "soundgetin": ["A3|Sounds_F_EPB|Tracked|noises|get_in_out",0.562341,1],
    "soundgetout": ["A3|Sounds_F_EPB|Tracked|noises|get_in_out",0.562341,1,20],
    "soundturnin": ["A3|Sounds_F|vehicles|noises|Turn_in_out",1.77828,1,20],
    "soundturnout": ["A3|Sounds_F|vehicles|noises|Turn_in_out",1.77828,1,20],
    "soundturnininternal": ["A3|Sounds_F|vehicles|noises|Turn_in_out",1.77828,1,20],
    "soundturnoutinternal": ["A3|Sounds_F|vehicles|noises|Turn_in_out",1.77828,1,20],
    "sounddammage": ["",0.562341,1],
    "soundengineonint": ["A3|Sounds_F|vehicles2|armor|MBT_03|MBT_03_Engine_Int_Start",0.501187,1],
    "soundengineoffint": ["A3|Sounds_F|vehicles2|armor|MBT_03|MBT_03_Engine_Int_Stop",0.707946,1],
    "soundengineonext": ["A3|Sounds_F|vehicles2|armor|MBT_03|MBT_03_Engine_Ext_Start",1.99526,1,70],
    "soundengineoffext": ["A3|Sounds_F|vehicles2|armor|MBT_03|MBT_03_Engine_Ext_Stop",1.99526,1,70],
    "bushcrash1": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_Collision_Light_Bush_01",0.630957,1,100],
    "bushcrash2": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_Collision_Light_Bush_02",0.630957,1,100],
    "bushcrash3": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_Collision_Light_Bush_03",0.630957,1,100],
    "soundbushcrash": ["BushCrash1",0.33,"BushCrash2",0.33,"BushCrash3",0.33],
    "buildcrash0": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_01",3.16228,1,200],
    "buildcrash1": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_02",3.16228,1,200],
    "buildcrash2": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_03",3.16228,1,200],
    "buildcrash3": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_04",3.16228,1,200],
    "buildcrash4": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_05",3.16228,1,200],
    "buildcrash5": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_06",3.16228,1,200],
    "soundbuildingcrash": ["buildCrash0",0.166,"buildCrash1",0.166,"buildCrash2",0.166,"buildCrash3",0.166,"buildCrash4",0.166,"buildCrash5",0.166],
    "woodcrash0": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_01",3.16228,1,200],
    "woodcrash1": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_02",3.16228,1,200],
    "woodcrash2": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_03",3.16228,1,200],
    "woodcrash3": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_04",3.16228,1,200],
    "woodcrash4": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_05",3.16228,1,200],
    "woodcrash5": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_06",3.16228,1,200],
    "soundwoodcrash": ["woodCrash0",0.166,"woodCrash1",0.166,"woodCrash2",0.166,"woodCrash3",0.166,"woodCrash4",0.166,"woodCrash5",0.166],
    "armorcrash0": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_01",3.16228,1,200],
    "armorcrash1": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_02",3.16228,1,200],
    "armorcrash2": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_03",3.16228,1,200],
    "armorcrash3": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_04",3.16228,1,200],
    "armorcrash4": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_05",3.16228,1,200],
    "armorcrash5": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_06",3.16228,1,200],
    "soundarmorcrash": ["ArmorCrash0",0.166,"ArmorCrash1",0.166,"ArmorCrash2",0.166,"ArmorCrash3",0.166,"ArmorCrash4",0.166,"ArmorCrash5",0.166],
    # Class: CfgVehicles|APC_Tracked_02_base_F|Sounds [Indent level: 1],
    "sounds": {
        "soundsetsint": ["APC_Tracked_02_Engine_RPM0_INT_SoundSet","APC_Tracked_02_Engine_RPM1_INT_SoundSet","APC_Tracked_02_Engine_RPM2_INT_SoundSet","APC_Tracked_02_Engine_RPM3_INT_SoundSet","APC_Tracked_02_Engine_RPM4_INT_SoundSet","APC_Tracked_02_Tracks_01_INT_SoundSet","APC_Tracked_02_Tracks_02_INT_SoundSet","APC_Tracked_02_Tracks_03_INT_SoundSet","APC_Tracked_02_Tracks_04_INT_SoundSet","APC_Tracked_02_Tracks_05_INT_SoundSet","APC_Tracked_02_Tracks_06_INT_SoundSet","APC_Tracked_02_Interior_Tone_Engine_Off_SoundSet","APC_Tracked_02_Interior_Tone_Engine_On_SoundSet","APC_Tracked_02_Rattling_INT_SoundSet","APC_Tracked_02_Stress_INT_SoundSet","APC_Tracked_02_Rain_INT_SoundSet","APC_Tracked_02_Tracks_Brake_Hard_INT_SoundSet","APC_Tracked_02_Tracks_Brake_Soft_INT_SoundSet","APC_Tracked_02_Tracks_Turn_Hard_INT_SoundSet","APC_Tracked_02_Tracks_Turn_Soft_INT_SoundSet","APC_Tracked_02_Drive_Water_INT_SoundSet","APC_Tracked_02_Drive_Dirt_INT_SoundSet","Tracks_Movement_Dirt_Int_01_SoundSet","Tracks_Surface_Soft_Int_SoundSet","Tracks_Surface_Sand_Int_SoundSet","Tracks_Surface_Squeaks_Soft_Int_SoundSet","Tracks_Surface_Squeaks_Hard_Int_SoundSet","Tanks_Material_Strain_Int_SoundSet"],
        "soundsetsext": ["APC_Tracked_02_Engine_RPM0_EXT_SoundSet","APC_Tracked_02_Engine_RPM1_EXT_SoundSet","APC_Tracked_02_Engine_RPM2_EXT_SoundSet","APC_Tracked_02_Engine_RPM3_EXT_SoundSet","APC_Tracked_02_Engine_RPM4_EXT_SoundSet","APC_Tracked_02_Tracks_01_EXT_SoundSet","APC_Tracked_02_Tracks_02_EXT_SoundSet","APC_Tracked_02_Tracks_03_EXT_SoundSet","APC_Tracked_02_Tracks_04_EXT_SoundSet","APC_Tracked_02_Tracks_05_EXT_SoundSet","APC_Tracked_02_Tracks_06_EXT_SoundSet","APC_Tracked_02_Rattling_EXT_SoundSet","APC_Tracked_02_Rain_EXT_SoundSet","APC_Tracked_02_Tracks_Brake_Hard_EXT_SoundSet","APC_Tracked_02_Tracks_Brake_Soft_EXT_SoundSet","APC_Tracked_02_Tracks_Turn_Hard_EXT_SoundSet","APC_Tracked_02_Tracks_Turn_Soft_EXT_SoundSet","APC_Tracked_02_Drive_Water_EXT_SoundSet","APC_Tracked_02_Drive_Dirt_EXT_SoundSet","Tracks_Movement_Dirt_Ext_01_SoundSet","Tracks_Surface_Soft_Ext_SoundSet","Tracks_Surface_Sand_Ext_SoundSet","Tracks_Surface_Squeaks_Soft_Ext_SoundSet","Tracks_Surface_Squeaks_Hard_Ext_SoundSet"]
    },
    "_generalmacro": "APC_Tracked_02_base_F",
    "maxspeed": 87,
    "slowspeedforwardcoef": 0.6435,
    "waterresistancecoef": 0.25,
    "enginemoi": 7,
    "dampingratefullthrottle": 0.8,
    "dampingratezerothrottleclutchengaged": 4,
    "dampingratezerothrottleclutchdisengaged": 0.5,
    "switchtime": 0,
    "antirollbarforcecoef": 20,
    "antirollbarforcelimit": 10,
    "antirollbarspeedmin": 10,
    "antirollbarspeedmax": 55,
    # Class: CfgVehicles|APC_Tracked_02_base_F|MFD [Indent level: 1],
    "mfd": {
        # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Driver_Heading [Indent level: 2]
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
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Driver_Heading|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Driver_Heading|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Driver_Heading|Draw [Indent level: 3],
            "draw": {
                "color": [0.61,0.62,0],
                "alpha": 1,
                "condition": "on",
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Driver_Heading|Draw|Driver_Heading [Indent level: 4],
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
        # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Driver_Heading_text [Indent level: 2],
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
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Driver_Heading_text|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Driver_Heading_text|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Driver_Heading_text|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Driver_Heading_text|Draw|Driver_Heading [Indent level: 4],
                "driver_heading": {
                    "type": "text",
                    "source": "static",
                    "text": "АЗИМУТ",
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
        # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Driver_Heading_second [Indent level: 2],
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
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Driver_Heading_second|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Driver_Heading_second|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Driver_Heading_second|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Driver_Heading_second|Draw|Driver_Heading [Indent level: 4],
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
        # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_AmmoType [Indent level: 2],
        "mfd_gunner_ammotype": {
            "topleft": "MFD_5_TL",
            "topright": "MFD_5_TR",
            "bottomleft": "MFD_5_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "turret": [0],
            "enableparallax": 0,
            "font": "LCD14",
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_AmmoType|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_AmmoType|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_AmmoType|Draw [Indent level: 3],
            "draw": {
                "color": [0.92,0.01,0],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_AmmoType|Draw|Gunner_AmmoType [Indent level: 4],
                "gunner_ammotype": {
                    "type": "text",
                    "source": "ammoFormat",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.455,0.05],1],
                    "right": [[1.355,0.05],1],
                    "down": [[0.455,0.76],1]
                }
            }
        },
        # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_AmmoIndicator [Indent level: 2],
        "mfd_gunner_ammoindicator": {
            "topleft": "MFD_3_TL",
            "topright": "MFD_3_TR",
            "bottomleft": "MFD_3_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "enableparallax": 0,
            "turret": [0],
            "font": "LCD14",
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_AmmoIndicator|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_AmmoIndicator|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_AmmoIndicator|Draw [Indent level: 3],
            "draw": {
                "color": [0.92,0.01,0],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_AmmoIndicator|Draw|Gunner_Text_1 [Indent level: 4],
                "gunner_text_1": {
                    "type": "text",
                    "source": "ammo",
                    "sourcescale": 1,
                    "sourcelength": 2,
                    "sourceindex": 1000,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.5,0],1],
                    "right": [[1.3,0],1],
                    "down": [[0.5,0.3],1]
                },
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_AmmoIndicator|Draw|Gunner_Text_2 [Indent level: 4],
                "gunner_text_2": {
                    "type": "text",
                    "source": "ammo",
                    "sourcescale": 1,
                    "sourcelength": 2,
                    "sourceindex": 1001,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.5,0.3],1],
                    "right": [[1.3,0.3],1],
                    "down": [[0.5,0.6],1]
                },
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_AmmoIndicator|Draw|Gunner_Text_3 [Indent level: 4],
                "gunner_text_3": {
                    "type": "text",
                    "source": "ammo",
                    "sourcescale": 1,
                    "sourcelength": 2,
                    "sourceindex": 1002,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.5,0.6],1],
                    "right": [[1.3,0.6],1],
                    "down": [[0.5,0.9],1]
                }
            }
        },
        # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Ready_To_Fire [Indent level: 2],
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
            "font": "RobotoCondensedLight",
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Ready_To_Fire|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Ready_To_Fire|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Ready_To_Fire|Draw [Indent level: 3],
            "draw": {
                "color": [0,0,0],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Ready_To_Fire|Draw|Top_text [Indent level: 4],
                "top_text": {
                    "type": "text",
                    "source": "static",
                    "text": "К СТРЕЛЬБЕ",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.45,0.05],1],
                    "right": [[0.67,0.05],1],
                    "down": [[0.45,0.55],1]
                },
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Ready_To_Fire|Draw|Bottom_text [Indent level: 4],
                "bottom_text": {
                    "type": "text",
                    "source": "static",
                    "text": "ГОТОВ",
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
        # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Display [Indent level: 2],
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
            "font": "RobotoCondensedLight",
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Display|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Display|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Display|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Display|Draw|Main_armament [Indent level: 4],
                "main_armament": {
                    "type": "text",
                    "source": "static",
                    "text": "ГЛАВНОЕ ОРУДИЕ",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshrate": 0.1,
                    "pos": [[0.015,-0.005],1],
                    "right": [[0.075,-0.005],1],
                    "down": [[0.015,0.073],1]
                },
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Display|Draw|Machinegun [Indent level: 4],
                "machinegun": {
                    "type": "text",
                    "source": "static",
                    "text": "ПУЛЕМЕТ",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshrate": 0.1,
                    "pos": [[0.015,0.31],1],
                    "right": [[0.075,0.31],1],
                    "down": [[0.015,0.388],1]
                },
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Display|Draw|Main_armament_ammo_type [Indent level: 4],
                "main_armament_ammo_type": {
                    "type": "text",
                    "source": "static",
                    "text": "ТИП АМУНИЦИИ",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.55,-0.005],1],
                    "right": [[0.61,-0.005],1],
                    "down": [[0.55,0.073],1]
                },
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Display|Draw|Lased_distance_elevation [Indent level: 4],
                "lased_distance_elevation": {
                    "type": "text",
                    "source": "static",
                    "text": "ДАЛЬНОСТЬ",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshrate": 0.1,
                    "pos": [[0.015,0.84],1],
                    "right": [[0.075,0.84],1],
                    "down": [[0.015,0.918],1]
                },
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Display|Draw|Azimut [Indent level: 4],
                "azimut": {
                    "type": "text",
                    "source": "static",
                    "text": "АЗИМУТ",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshrate": 0.1,
                    "pos": [[0.015,0.915],1],
                    "right": [[0.075,0.915],1],
                    "down": [[0.015,0.993],1]
                },
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Display|Draw|Damage [Indent level: 4],
                "damage": {
                    "type": "text",
                    "source": "static",
                    "text": "ПОВРЕЖДЕНИЯ",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshrate": 0.1,
                    "pos": [[0.015,0.39],1],
                    "right": [[0.075,0.39],1],
                    "down": [[0.015,0.468],1]
                },
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Display|Draw|Heading [Indent level: 4],
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
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Display|Draw|Lased_Range [Indent level: 4],
                "lased_range": {
                    "type": "text",
                    "source": "laserDist",
                    "sourcescale": 1,
                    "sourcelength": 4,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.34,0.84],1],
                    "right": [[0.4,0.84],1],
                    "down": [[0.34,0.918],1]
                }
            }
        },
        # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Main_Armament_Ammo_Type [Indent level: 2],
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
            "font": "RobotoCondensedLight",
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Main_Armament_Ammo_Type|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Main_Armament_Ammo_Type|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Main_Armament_Ammo_Type|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Main_Armament_Ammo_Type|Draw|Gunner_AmmoType [Indent level: 4],
                "gunner_ammotype": {
                    "type": "text",
                    "source": "ammoFormat",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.555,0.065],1],
                    "right": [[0.635,0.065],1],
                    "down": [[0.555,0.185],1]
                }
            }
        },
        # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Coax_Ammo [Indent level: 2],
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
            "font": "RobotoCondensedLight",
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Coax_Ammo|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Coax_Ammo|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Coax_Ammo|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_Coax_Ammo|Draw|Gunner_Text_1 [Indent level: 4],
                "gunner_text_1": {
                    "type": "text",
                    "source": "ammo",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "sourceindex": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.31,0.31],1],
                    "right": [[0.37,0.31],1],
                    "down": [[0.31,0.388],1]
                }
            }
        },
        # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament [Indent level: 2],
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
            "font": "RobotoCondensedLight",
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|Draw|Main_Armament_Ammo_Type_1 [Indent level: 4],
                "main_armament_ammo_type_1": {
                    "type": "text",
                    "source": "static",
                    "text": "БР",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshrate": 0.1,
                    "pos": [[0.015,0.065],1],
                    "right": [[0.075,0.065],1],
                    "down": [[0.015,0.143],1]
                },
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|Draw|Gunner_Text_1 [Indent level: 4],
                "gunner_text_1": {
                    "type": "text",
                    "source": "ammo",
                    "sourcescale": 1,
                    "sourcelength": 2,
                    "sourceindex": 0,
                    "sourceprecision": 1,
                    "scale": 1,
                    "align": "left",
                    "refreshrate": 0.1,
                    "pos": [[0.395,0.065],1],
                    "right": [[0.455,0.065],1],
                    "down": [[0.395,0.143],1]
                },
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|Draw|Main_Armament_Ammo_Type_2 [Indent level: 4],
                "main_armament_ammo_type_2": {
                    "type": "text",
                    "source": "static",
                    "text": "ОФ",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshrate": 0.1,
                    "pos": [[0.015,0.125],1],
                    "right": [[0.075,0.125],1],
                    "down": [[0.015,0.203],1]
                },
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|Draw|Gunner_Text_2 [Indent level: 4],
                "gunner_text_2": {
                    "type": "text",
                    "source": "ammo",
                    "sourcescale": 1,
                    "sourcelength": 2,
                    "sourceindex": 0,
                    "scale": 1,
                    "align": "left",
                    "refreshrate": 0.1,
                    "pos": [[0.395,0.125],1],
                    "right": [[0.455,0.125],1],
                    "down": [[0.395,0.203],1]
                },
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|Draw|Main_Armament_Ammo_Type_3 [Indent level: 4],
                "main_armament_ammo_type_3": {
                    "type": "text",
                    "source": "static",
                    "text": "Р",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshrate": 0.1,
                    "pos": [[0.015,0.185],1],
                    "right": [[0.075,0.185],1],
                    "down": [[0.015,0.263],1]
                },
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|Draw|Gunner_Text_3 [Indent level: 4],
                "gunner_text_3": {
                    "type": "text",
                    "source": "ammo",
                    "sourcescale": 1,
                    "sourcelength": 2,
                    "sourceindex": 2,
                    "scale": 1,
                    "align": "left",
                    "refreshrate": 0.1,
                    "pos": [[0.395,0.185],1],
                    "right": [[0.455,0.185],1],
                    "down": [[0.395,0.263],1]
                }
            }
        },
        # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Display [Indent level: 2],
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
            "turret": [0,0],
            "font": "RobotoCondensedLight",
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Display|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Display|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Display|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Display|Draw|Main_armament [Indent level: 4],
                "main_armament": {
                    "type": "text",
                    "source": "static",
                    "text": "ГЛАВНОЕ ОРУДИЕ",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshrate": 0.1,
                    "pos": [[0.015,-0.005],1],
                    "right": [[0.075,-0.005],1],
                    "down": [[0.015,0.145],1]
                },
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Display|Draw|Machinegun [Indent level: 4],
                "machinegun": {
                    "type": "text",
                    "source": "static",
                    "text": "ПУЛЕМЕТ",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.51,-0.005],1],
                    "right": [[0.57,-0.005],1],
                    "down": [[0.51,0.145],1]
                },
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Display|Draw|Commander_machinegun [Indent level: 4],
                "commander_machinegun": {
                    "type": "text",
                    "source": "static",
                    "text": "----",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.81,0.19],1],
                    "right": [[0.87,0.19],1],
                    "down": [[0.81,0.34],1]
                },
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Display|Draw|Commander_armament [Indent level: 4],
                "commander_armament": {
                    "type": "text",
                    "source": "static",
                    "text": "ОРУДИЕ КОМАНДИРА",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.795,0.005],1],
                    "right": [[0.845,0.005],1],
                    "down": [[0.795,0.125],1]
                },
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Display|Draw|Commander_armament_magazines [Indent level: 4],
                "commander_armament_magazines": {
                    "type": "text",
                    "source": "static",
                    "text": "МАГ.",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.47,0.4],1],
                    "right": [[0.53,0.4],1],
                    "down": [[0.47,0.55],1]
                },
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Display|Draw|Main_armament_ammo_type [Indent level: 4],
                "main_armament_ammo_type": {
                    "type": "text",
                    "source": "static",
                    "text": "ТИП АМУНИЦИИ",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshrate": 0.1,
                    "pos": [[0.015,0.61],1],
                    "right": [[0.075,0.61],1],
                    "down": [[0.015,0.76],1]
                },
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Display|Draw|Lased_distance_elevation [Indent level: 4],
                "lased_distance_elevation": {
                    "type": "text",
                    "source": "static",
                    "text": "ДАЛЬНОСТЬ",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.73,0.61],1],
                    "right": [[0.785,0.61],1],
                    "down": [[0.73,0.75],1]
                },
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Display|Draw|Azimut [Indent level: 4],
                "azimut": {
                    "type": "text",
                    "source": "static",
                    "text": "АЗИМУТ",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.71,0.8],1],
                    "right": [[0.77,0.8],1],
                    "down": [[0.71,0.95],1]
                },
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Display|Draw|Damage [Indent level: 4],
                "damage": {
                    "type": "text",
                    "source": "static",
                    "text": "ПОВРЕЖДЕНИЯ",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshrate": 0.1,
                    "pos": [[0.015,0.82],1],
                    "right": [[0.075,0.82],1],
                    "down": [[0.015,0.97],1]
                },
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Display|Draw|Heading [Indent level: 4],
                "heading": {
                    "type": "text",
                    "source": "[x]turretworld",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 0.2,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.925,0.8],1],
                    "right": [[0.985,0.8],1],
                    "down": [[0.925,0.95],1]
                },
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Display|Draw|Lased_Range [Indent level: 4],
                "lased_range": {
                    "type": "text",
                    "source": "laserDist",
                    "sourcescale": 1,
                    "sourcelength": 4,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.925,0.61],1],
                    "right": [[0.985,0.61],1],
                    "down": [[0.925,0.76],1]
                }
            }
        },
        # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Ready_To_Fire [Indent level: 2],
        "mfd_commander_ready_to_fire": {
            "topleft": "mfd_com_cli_TL",
            "topright": "mfd_com_cli_TR",
            "bottomleft": "mfd_com_cli_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0,0,0],
            "alpha": 0.5,
            "enableparallax": 0,
            "font": "RobotoCondensedLight",
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Ready_To_Fire|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Ready_To_Fire|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Ready_To_Fire|Draw [Indent level: 3],
            "draw": {
                "color": [0,0,0],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Ready_To_Fire|Draw|Top_text [Indent level: 4],
                "top_text": {
                    "type": "text",
                    "source": "static",
                    "text": "К СТРЕЛЬБЕ",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": [[0.48,0.05],1],
                    "right": [[0.68,0.05],1],
                    "down": [[0.48,0.56],1]
                },
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Ready_To_Fire|Draw|Bottom_text [Indent level: 4],
                "bottom_text": {
                    "type": "text",
                    "source": "static",
                    "text": "ГОТОВ",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": [[0.5,0.41],1],
                    "right": [[0.7,0.41],1],
                    "down": [[0.5,0.92],1]
                }
            }
        },
        # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Smoke_Indicator [Indent level: 2],
        "mfd_commander_smoke_indicator": {
            "topleft": "mfd_com_smoke_TL",
            "topright": "mfd_com_smoke_TR",
            "bottomleft": "mfd_com_smoke_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0,0,0],
            "alpha": 0.5,
            "enableparallax": 0,
            "font": "RobotoCondensedLight",
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Smoke_Indicator|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Smoke_Indicator|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Smoke_Indicator|Draw [Indent level: 3],
            "draw": {
                "color": [0,0,0],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Smoke_Indicator|Draw|Top_text [Indent level: 4],
                "top_text": {
                    "type": "text",
                    "source": "static",
                    "text": "ДЫМОВАЯ",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": [[0.47,0],1],
                    "right": [[0.67,0],1],
                    "down": [[0.47,0.5],1]
                },
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Smoke_Indicator|Draw|Bottom_text [Indent level: 4],
                "bottom_text": {
                    "type": "text",
                    "source": "static",
                    "text": "ЗАВЕСА",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": [[0.5,0.4],1],
                    "right": [[0.7,0.4],1],
                    "down": [[0.5,0.9],1]
                }
            }
        },
        # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Main_Armament_Ammo_Type [Indent level: 2],
        "mfd_commander_main_armament_ammo_type": {
            "topleft": "mfd_com_TL",
            "topright": "mfd_com_TR",
            "bottomleft": "mfd_com_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "turret": [0],
            "enableparallax": 0,
            "font": "RobotoCondensedLight",
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Main_Armament_Ammo_Type|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Main_Armament_Ammo_Type|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Main_Armament_Ammo_Type|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Main_Armament_Ammo_Type|Draw|Gunner_AmmoType [Indent level: 4],
                "gunner_ammotype": {
                    "type": "text",
                    "source": "ammoFormat",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.36,0.61],1],
                    "right": [[0.42,0.61],1],
                    "down": [[0.36,0.76],1]
                }
            }
        },
        # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_AmmoIndicator_Main_Armament [Indent level: 2],
        "mfd_commander_ammoindicator_main_armament": {
            "topleft": "mfd_com_TL",
            "topright": "mfd_com_TR",
            "bottomleft": "mfd_com_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "enableparallax": 0,
            "turret": [0],
            "font": "RobotoCondensedLight",
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_AmmoIndicator_Main_Armament|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_AmmoIndicator_Main_Armament|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_AmmoIndicator_Main_Armament|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_AmmoIndicator_Main_Armament|Draw|Main_Armament_Ammo_Type_1 [Indent level: 4],
                "main_armament_ammo_type_1": {
                    "type": "text",
                    "source": "static",
                    "text": "БР",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshrate": 0.1,
                    "pos": [[0.015,0.13],1],
                    "right": [[0.075,0.13],1],
                    "down": [[0.015,0.28],1]
                },
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_AmmoIndicator_Main_Armament|Draw|Gunner_Text_1 [Indent level: 4],
                "gunner_text_1": {
                    "type": "text",
                    "source": "ammo",
                    "sourcescale": 1,
                    "sourcelength": 2,
                    "sourceindex": 0,
                    "sourceprecision": 1,
                    "scale": 1,
                    "align": "left",
                    "refreshrate": 0.1,
                    "pos": [[0.39,0.13],1],
                    "right": [[0.45,0.13],1],
                    "down": [[0.39,0.28],1]
                },
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_AmmoIndicator_Main_Armament|Draw|Main_Armament_Ammo_Type_2 [Indent level: 4],
                "main_armament_ammo_type_2": {
                    "type": "text",
                    "source": "static",
                    "text": "ОФ",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshrate": 0.1,
                    "pos": [[0.015,0.23],1],
                    "right": [[0.075,0.23],1],
                    "down": [[0.015,0.38],1]
                },
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_AmmoIndicator_Main_Armament|Draw|Gunner_Text_2 [Indent level: 4],
                "gunner_text_2": {
                    "type": "text",
                    "source": "ammo",
                    "sourcescale": 1,
                    "sourcelength": 2,
                    "sourceindex": 0,
                    "scale": 1,
                    "align": "left",
                    "refreshrate": 0.1,
                    "pos": [[0.39,0.23],1],
                    "right": [[0.45,0.23],1],
                    "down": [[0.39,0.38],1]
                },
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_AmmoIndicator_Main_Armament|Draw|Main_Armament_Ammo_Type_3 [Indent level: 4],
                "main_armament_ammo_type_3": {
                    "type": "text",
                    "source": "static",
                    "text": "Р",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshrate": 0.1,
                    "pos": [[0.015,0.33],1],
                    "right": [[0.075,0.33],1],
                    "down": [[0.015,0.48],1]
                },
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_AmmoIndicator_Main_Armament|Draw|Gunner_Text_3 [Indent level: 4],
                "gunner_text_3": {
                    "type": "text",
                    "source": "ammo",
                    "sourcescale": 1,
                    "sourcelength": 2,
                    "sourceindex": 2,
                    "scale": 1,
                    "align": "left",
                    "refreshrate": 0.1,
                    "pos": [[0.39,0.33],1],
                    "right": [[0.45,0.33],1],
                    "down": [[0.39,0.48],1]
                }
            }
        },
        # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Coax_Ammo [Indent level: 2],
        "mfd_commander_coax_ammo": {
            "topleft": "mfd_com_ammo_count_TL",
            "topright": "mfd_com_ammo_count_TR",
            "bottomleft": "mfd_com_ammo_count_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "enableparallax": 0,
            "turret": [0],
            "font": "RobotoCondensedLight",
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Coax_Ammo|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Coax_Ammo|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Coax_Ammo|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Coax_Ammo|Draw|Gunner_Text_1 [Indent level: 4],
                "gunner_text_1": {
                    "type": "text",
                    "source": "ammo",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "sourceindex": 1,
                    "align": "left",
                    "refreshrate": 0.1,
                    "pos": [[1.32,0.2],1],
                    "right": [[1.97,0.2],1],
                    "down": [[1.32,1],1]
                }
            }
        },
        # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Coax_Magazines [Indent level: 2],
        "mfd_commander_coax_magazines": {
            "topleft": "mfd_com_mag_count_TL",
            "topright": "mfd_com_mag_count_TR",
            "bottomleft": "mfd_com_mag_count_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "enableparallax": 0,
            "turret": [0],
            "font": "RobotoCondensedLight",
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Coax_Magazines|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Coax_Magazines|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Coax_Magazines|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Coax_Magazines|Draw|Gunner_Text_1 [Indent level: 4],
                "gunner_text_1": {
                    "type": "text",
                    "source": "ammo",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "sourceindex": 1,
                    "align": "left",
                    "refreshrate": 0.1,
                    "pos": [[0.1,0.11],1],
                    "right": [[0.85,0.11],1],
                    "down": [[0.1,0.81],1]
                }
            }
        },
        # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Second_Display [Indent level: 2],
        "mfd_commander_second_display": {
            "topleft": "MFD_7_TL",
            "topright": "MFD_7_TR",
            "bottomleft": "MFD_7_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [1,1,1],
            "alpha": 0.5,
            "enableparallax": 0,
            "font": "EtelkaMonospacePro",
            "turret": [0,0],
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Second_Display|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Second_Display|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Second_Display|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Second_Display|Draw|Crosshair [Indent level: 4],
                "crosshair": {
                    "type": "line",
                    "width": 3,
                    "points": [[[0.5,0.423413],1],[[0.5,0.346429],1],[],[[0.5,0.577381],1],[[0.5,0.654365],1],[],[[0.55,0.500397],1],[[0.6,0.500397],1],[],[[0.4,0.500397],1],[[0.45,0.500397],1],[],[[0.3,0.346429],1],[[0.3,0.269444],1],[],[[0.3,0.269444],1],[[0.35,0.269444],1],[],[[0.7,0.346429],1],[[0.7,0.269444],1],[],[[0.65,0.269444],1],[[0.7,0.269444],1],[],[[0.7,0.654365],1],[[0.7,0.731349],1],[],[[0.65,0.731349],1],[[0.7,0.731349],1],[],[[0.3,0.654365],1],[[0.3,0.731349],1],[],[[0.3,0.731349],1],[[0.35,0.731349],1],[]]
                },
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Second_Display|Draw|Heading [Indent level: 4],
                "heading": {
                    "type": "text",
                    "source": "[x]turretworld",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 0.2,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.83,0.25],1],
                    "right": [[0.88,0.25],1],
                    "down": [[0.83,0.33],1]
                },
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Second_Display|Draw|Lased_Range_Background [Indent level: 4],
                "lased_range_background": {
                    "color": [0,0,0],
                    # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Second_Display|Draw|Lased_Range_Background|Background [Indent level: 5],
                    "background": {
                        "type": "polygon",
                        "points": [[[[0.43,0.81],1],[[0.57,0.81],1],[[0.57,0.87],1],[[0.43,0.87],1]]]
                    }
                },
                # Class: CfgVehicles|APC_Tracked_02_base_F|MFD|MFD_Commander_Second_Display|Draw|Lased_Range [Indent level: 4],
                "lased_range": {
                    "type": "text",
                    "source": "laserDist",
                    "sourcescale": 1,
                    "sourcelength": 4,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.494,0.8],1],
                    "right": [[0.544,0.8],1],
                    "down": [[0.494,0.88],1]
                }
            }
        }
    },
    # Class: CfgVehicles|APC_Tracked_02_base_F|Library [Indent level: 1],
    "library": {
        "libtextdesc": "The infantry fighting vehicle BTR-K Kamysh and its anti-aircraft cousin ZSU-39 Tigris share the same vehicle platform. Developed by Russia with a pinch of undeniable inspiration from Israeli IFVs, they serve in the OPFOR army as a prime example of a leveling of the technology field with the West. The Kamysh is equipped with a CTWS turret fitted with a 30 mm cannon, coaxial machinegun and 2 guided AT missiles, making the vehicle significant in the infantry support role. The Tigris is fitted with a 35 mm autocannon and 4 Titan AA missiles."
    },
    "memorypointtaskmarker": "TaskMarker_1_pos",
    "transportsoldier": 0,
    "cargogetinaction": ["GetInAMV_cargo"],
    "cargogetoutaction": ["GetOutLow"],
    "cargoaction": ["passenger_apc_narrow_generic02","passenger_apc_narrow_generic03","passenger_apc_generic02","passenger_apc_generic04","passenger_apc_narrow_generic01","passenger_generic01_foldhands","passenger_generic01_leanleft","passenger_generic01_leanright"],
    "hideproxyincombat": 1,
    "hideweaponsdriver": 1,
    "hideweaponscargo": 1,
    "viewdrivershadowamb": 0.5,
    "viewdrivershadowdiff": 0.05,
    "driverinfopanelcamerapos": "driverview_old",
    "driverlefthandanimname": "drivingstick_left",
    "driverrighthandanimname": "drivingstick_right",
    "driverleftleganimname": "pedal_brake",
    "driverrightleganimname": "pedal_thrust",
    # Class: CfgVehicles|APC_Tracked_02_base_F|ViewPilot [Indent level: 1],
    "viewpilot": {
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
    "armorlights": 0.1,
    "crewexplosionprotection": 0.999,
    "waterppinvehicle": 0,
    "firedusteffect": "emptyEffect",
    "wheelcircumference": 2.18,
    "animationsourcehatch": "",
    "insidesoundcoef": 0.9,
    "soundlocked": ["|A3|Sounds_F|weapons|Rockets|locked_1",1,1],
    "soundincommingmissile": ["|A3|Sounds_F|vehicles|air|noises|alarm_locked_by_missile_4",0.398107,1],
    "smokelaunchergrenadecount": 8,
    "smokelaunchervelocity": 14,
    "smokelauncheronturret": 0,
    "smokelauncherangle": 120,
    "extcameraposition": [0,2.75,-9.5],
    # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights [Indent level: 1],
    "compartmentslights": {
        # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights|Comp1 [Indent level: 2]
        "comp1": {
            # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights|Comp1|Light1 [Indent level: 3]
            "light1": {
                "color": [10,15,17],
                "ambient": [0,0,0],
                "intensity": 1,
                "size": 0,
                "useflare": 0,
                "flaresize": 0,
                "flaremaxdistance": 0,
                "daylight": 0,
                "blinking": 0,
                # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights|Comp1|Light1|Attenuation [Indent level: 4],
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
            # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights|Comp1|Light2 [Indent level: 3],
            "light2": {
                "point": "light_interior2",
                "color": [10,15,17],
                "ambient": [0,0,0],
                "intensity": 0.3,
                "size": 0,
                "useflare": 0,
                "flaresize": 0,
                "flaremaxdistance": 0,
                "daylight": 0,
                "blinking": 0,
                # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights|Comp1|Light1|Attenuation [Indent level: 4],
                "attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardlimitstart": 0.15,
                    "hardlimitend": 1.15
                }
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights|Comp1|Light3 [Indent level: 3],
            "light3": {
                "point": "light_interior3",
                "color": [10,15,17],
                "ambient": [0,0,0],
                "intensity": 0.4,
                "size": 0,
                "useflare": 0,
                "flaresize": 0,
                "flaremaxdistance": 0,
                "daylight": 0,
                "blinking": 0,
                # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights|Comp1|Light1|Attenuation [Indent level: 4],
                "attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardlimitstart": 0.15,
                    "hardlimitend": 1.15
                }
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights|Comp1|Light4 [Indent level: 3],
            "light4": {
                "point": "light_interior4",
                "color": [10,15,17],
                "ambient": [0,0,0],
                "intensity": 0.5,
                "size": 0,
                "useflare": 0,
                "flaresize": 0,
                "flaremaxdistance": 0,
                "daylight": 0,
                "blinking": 0,
                # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights|Comp1|Light1|Attenuation [Indent level: 4],
                "attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardlimitstart": 0.15,
                    "hardlimitend": 1.15
                }
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights|Comp1|Light5 [Indent level: 3],
            "light5": {
                "point": "light_interior5",
                "color": [10,15,17],
                "ambient": [0,0,0],
                "intensity": 0.3,
                "size": 0,
                "useflare": 0,
                "flaresize": 0,
                "flaremaxdistance": 0,
                "daylight": 0,
                "blinking": 0,
                # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights|Comp1|Light1|Attenuation [Indent level: 4],
                "attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardlimitstart": 0.15,
                    "hardlimitend": 1.15
                }
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights|Comp1|Light6 [Indent level: 3],
            "light6": {
                "point": "light_interior6",
                "color": [12,12,12],
                "ambient": [0,0,0],
                "intensity": 3,
                "size": 0,
                "useflare": 0,
                "flaresize": 0,
                "flaremaxdistance": 0,
                "daylight": 0,
                "blinking": 0,
                # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights|Comp1|Light1|Attenuation [Indent level: 4],
                "attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardlimitstart": 0.15,
                    "hardlimitend": 1.15
                }
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights|Comp1|Light7 [Indent level: 3],
            "light7": {
                "point": "light_interior7",
                "color": [12,12,12],
                "ambient": [0,0,0],
                "intensity": 3,
                "size": 0,
                "useflare": 0,
                "flaresize": 0,
                "flaremaxdistance": 0,
                "daylight": 0,
                "blinking": 0,
                # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights|Comp1|Light1|Attenuation [Indent level: 4],
                "attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardlimitstart": 0.15,
                    "hardlimitend": 1.15
                }
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights|Comp1|Light8 [Indent level: 3],
            "light8": {
                "point": "light_interior8",
                "color": [12,12,12],
                "ambient": [0,0,0],
                "intensity": 3,
                "size": 0,
                "useflare": 0,
                "flaresize": 0,
                "flaremaxdistance": 0,
                "daylight": 0,
                "blinking": 0,
                # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights|Comp1|Light1|Attenuation [Indent level: 4],
                "attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardlimitstart": 0.15,
                    "hardlimitend": 1.15
                }
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights|Comp1|Light9 [Indent level: 3],
            "light9": {
                "point": "light_interior9",
                "color": [12,12,12],
                "ambient": [0,0,0],
                "intensity": 3,
                "size": 0,
                "useflare": 0,
                "flaresize": 0,
                "flaremaxdistance": 0,
                "daylight": 0,
                "blinking": 0,
                # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights|Comp1|Light1|Attenuation [Indent level: 4],
                "attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardlimitstart": 0.15,
                    "hardlimitend": 1.15
                }
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights|Comp1|Light10 [Indent level: 3],
            "light10": {
                "point": "light_interior10",
                "color": [20,20,20],
                "ambient": [0,0,0],
                "intensity": 5,
                "size": 0,
                "useflare": 0,
                "flaresize": 0,
                "flaremaxdistance": 0,
                "daylight": 0,
                "blinking": 0,
                # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights|Comp1|Light1|Attenuation [Indent level: 4],
                "attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardlimitstart": 0.15,
                    "hardlimitend": 1.15
                }
            },
            # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights|Comp1|Light11 [Indent level: 3],
            "light11": {
                "point": "light_interior11",
                "color": [20,20,20],
                "ambient": [0,0,0],
                "intensity": 5,
                "size": 0,
                "useflare": 0,
                "flaresize": 0,
                "flaremaxdistance": 0,
                "daylight": 0,
                "blinking": 0,
                # Class: CfgVehicles|APC_Tracked_02_base_F|compartmentsLights|Comp1|Light1|Attenuation [Indent level: 4],
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
    "occludesoundswhenin": 0,
    "obstructsoundswhenin": 0,
    "drivercansee": "1 + 2 + 4 + 8 + 32",
    "sensorposition": "gunnerView",
    "audible": 18,
    "sensitivityear": "0.0075 /3",
    "turncoef": 5,
    "steeraheadsimul": 0.3,
    "steeraheadplan": 0.4,
    "brakedistance": 5,
    "precision": 10,
    "irscanrangemin": 0,
    "irscantoeyefactor": 1,
    "enableradio": 1,
    "lockdetectionsystem": 0,
    "countermeasureactivationradius": 2000,
    "memorypointcargolight": "cargo light",
    "dampersbumpcoef": 4.5,
    "explosionshielding": 1,
    "mintotaldamagethreshold": 0.005,
    "crewcrashprotection": 0.25,
    "secondaryexplosion": -1,
    "fuelexplosionpower": 1,
    "weapons": [],
    "magazines": [],
    "transportmaxweapons": 12,
    "transportmaxmagazines": 128,
    "transportmaxbackpacks": 12,
    "maximumload": 3000,
    "supplyradius": -1,
    "memorypointsupply": "doplnovani",
    # Class: CfgVehicles|Tank_F|TransportBackpacks [Indent level: 1],
    "transportbackpacks": {
    },
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
    # Class: CfgVehicles|Tank|SpeechVariants [Indent level: 1],
    "speechvariants": {
        # Class: CfgVehicles|Tank|SpeechVariants|Default [Indent level: 2]
        "default": {
            "speechsingular": ["veh_vehicle_tank_s"],
            "speechplural": ["veh_vehicle_tank_p"]
        }
    },
    "textsingular": "tank",
    "textplural": "tanks",
    "namesound": "veh_vehicle_tank_s",
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
    "memorypointsgetincargo": "pos cargo",
    "memorypointsgetincargodir": "pos cargo dir",
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
    "cargoproxyindexes": [],
    "cargodoors": [],
    "hasterminal": 0,
    "getinoutonproxy": 0,
    "precisegetinout": 0,
    "cargoprecisegetinout": [0],
    "availableforsupporttypes": [],
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
    "dustfrontleftpos": "dustFrontLeft",
    "dustfrontrightpos": "dustFrontRight",
    "dustbackleftpos": "dustBackLeft",
    "dustbackrightpos": "dustBackRight",
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
    "cargoiscodriver": [0],
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
    "features": "",
    "insidedetectcoef": 0.05,
}