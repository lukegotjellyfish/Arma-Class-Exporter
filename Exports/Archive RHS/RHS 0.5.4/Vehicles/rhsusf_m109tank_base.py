rhsusf_m109tank_base = {
    "dlc": "RHS_USAF",
    "editorsubcategory": "rhs_EdSubcat_artillery",
    "vehicleclass": "rhs_vehclass_artillery",
    "category": "Armored",
    "destrtype": "DestructDefault",
    "driveoncomponent": ["slide"],
    "displayname": "M109A6",
    "accuracy": 0.3,
    "icon": "rhsusf|addons|rhsusf_m109|data|sa_m109a6_icon_ca.paa",
    "picture": "rhsusf|addons|rhsusf_m109|UI|m109a6_ca",
    "model": "rhsusf|addons|rhsusf_m109|rhsusf_m109a6",
    # Class: CfgVehicles|rhsusf_m109tank_base|RenderTargets [Indent level: 1],
    "rendertargets": {
    },
    "typicalcargo": [],
    "side": 1,
    "unitinfotype": "RscUnitInfoArtillery",
    "driverforceoptics": 1,
    "driveropticsmodel": "rhsusf|addons|rhsusf_optics|data|rhsusf_vision_block",
    "simulation": "tankX",
    "normalspeedforwardcoef": 0.8,
    "slowspeedforwardcoef": 0.65,
    "maxspeed": 56,
    "fuelcapacity": 19.5,
    "rhs_fuelcapacity": 1885,
    "tankturnforce": 450000,
    "tankturnforceangminspd": 0.5,
    "tankturnforceangspd": 0.72,
    "accelaidforcecoef": 2,
    "accelaidforceyoffset": -2.3,
    "accelaidforcespd": 2.73,
    "maxfordingdepth": 0,
    "waterresistance": 0,
    "waterdamageengine": 0.2,
    "waterleakiness": 10,
    "torquecurve": [[0.282609,0.55016],[0.434783,0.811502],[0.521739,0.952077],[0.608696,1],[0.695652,0.977636],[0.782609,0.948882],[0.869565,0.907348],[1.34174,0]],
    "enginemoi": 19,
    "enginepower": 328,
    "peaktorque": 1565,
    "minomega": 68,
    "maxomega": 240.86,
    "idlerpm": 650,
    "redrpm": 2300,
    "antirollbarforcecoef": 24,
    "antirollbarforcelimit": 42,
    "antirollbarspeedmin": 30,
    "antirollbarspeedmax": 75,
    "thrustdelay": 0.3,
    "dampingratefullthrottle": 0.3,
    "dampingratezerothrottleclutchengaged": 3,
    "dampingratezerothrottleclutchdisengaged": 0.25,
    "enginelosses": 25,
    "transmissionlosses": 15,
    "clutchstrength": 15,
    "switchtime": 0,
    "latency": 1.1,
    "changegeartype": "rpmratio",
    "changegearomegaratios": [1,0.434783,0.434783,0,0.826087,0.608696,0.891304,0.608696,0.978261,0.608696,1,0.652174],
    # Class: CfgVehicles|rhsusf_m109tank_base|complexGearbox [Indent level: 1],
    "complexgearbox": {
        "gearboxratios": ["R1",-2.235,"N",0,"D1",4.69,"D2",3.17,"D3",1.58,"D4",0.79],
        "transmissionratios": ["High",10.7],
        "gearboxmode": "auto",
        "moveoffgear": 1,
        "drivestring": "D",
        "neutralstring": "N",
        "reversestring": "R",
        "transmissiondelay": 0.1
    },
    # Class: CfgVehicles|rhsusf_m109tank_base|Wheels [Indent level: 1],
    "wheels": {
        # Class: CfgVehicles|rhsusf_m109tank_base|Wheels|L2 [Indent level: 2]
        "l2": {
            "bonename": "wheel_podkoloL1",
            "center": "wheel_1_2_axis",
            "boundary": "wheel_1_2_bound",
            "side": "left",
            "width": 0.39,
            "steering": 0,
            "mass": 150,
            "moi": 8.2668,
            "maxbraketorque": 10000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "sprungmass": 2857,
            "springstrength": 85000,
            "springdamperrate": 18428,
            "dampingrate": 727,
            "dampingrateinair": 727,
            "dampingratedamaged": 10,
            "dampingradtedestroyed": 10000,
            "latstiffx": 1,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 32000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|Wheels|L3 [Indent level: 2],
        "l3": {
            "bonename": "wheel_podkolol2",
            "center": "wheel_1_3_axis",
            "boundary": "wheel_1_3_bound",
            "side": "left",
            "width": 0.39,
            "steering": 0,
            "mass": 150,
            "moi": 8.2668,
            "maxbraketorque": 10000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "sprungmass": 2857,
            "springstrength": 85000,
            "springdamperrate": 18428,
            "dampingrate": 727,
            "dampingrateinair": 727,
            "dampingratedamaged": 10,
            "dampingradtedestroyed": 10000,
            "latstiffx": 1,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 32000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|Wheels|L4 [Indent level: 2],
        "l4": {
            "bonename": "wheel_podkolol3",
            "center": "wheel_1_4_axis",
            "boundary": "wheel_1_4_bound",
            "side": "left",
            "width": 0.39,
            "steering": 0,
            "mass": 150,
            "moi": 8.2668,
            "maxbraketorque": 10000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "sprungmass": 2857,
            "springstrength": 85000,
            "springdamperrate": 18428,
            "dampingrate": 727,
            "dampingrateinair": 727,
            "dampingratedamaged": 10,
            "dampingradtedestroyed": 10000,
            "latstiffx": 1,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 32000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|Wheels|L5 [Indent level: 2],
        "l5": {
            "bonename": "wheel_podkolol4",
            "center": "wheel_1_5_axis",
            "boundary": "wheel_1_5_bound",
            "side": "left",
            "width": 0.39,
            "steering": 0,
            "mass": 150,
            "moi": 8.2668,
            "maxbraketorque": 10000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "sprungmass": 2857,
            "springstrength": 85000,
            "springdamperrate": 18428,
            "dampingrate": 727,
            "dampingrateinair": 727,
            "dampingratedamaged": 10,
            "dampingradtedestroyed": 10000,
            "latstiffx": 1,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 32000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|Wheels|L6 [Indent level: 2],
        "l6": {
            "bonename": "wheel_podkolol5",
            "center": "wheel_1_6_axis",
            "boundary": "wheel_1_6_bound",
            "side": "left",
            "width": 0.39,
            "steering": 0,
            "mass": 150,
            "moi": 8.2668,
            "maxbraketorque": 10000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "sprungmass": 2857,
            "springstrength": 85000,
            "springdamperrate": 18428,
            "dampingrate": 727,
            "dampingrateinair": 727,
            "dampingratedamaged": 10,
            "dampingradtedestroyed": 10000,
            "latstiffx": 1,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 32000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|Wheels|L7 [Indent level: 2],
        "l7": {
            "bonename": "wheel_podkolol6",
            "center": "wheel_1_7_axis",
            "boundary": "wheel_1_7_bound",
            "side": "left",
            "width": 0.39,
            "steering": 0,
            "mass": 150,
            "moi": 8.2668,
            "maxbraketorque": 10000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "sprungmass": 2857,
            "springstrength": 85000,
            "springdamperrate": 18428,
            "dampingrate": 727,
            "dampingrateinair": 727,
            "dampingratedamaged": 10,
            "dampingradtedestroyed": 10000,
            "latstiffx": 1,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 32000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|Wheels|L8 [Indent level: 2],
        "l8": {
            "bonename": "wheel_podkolol7",
            "center": "wheel_1_8_axis",
            "boundary": "wheel_1_8_bound",
            "side": "left",
            "width": 0.39,
            "steering": 0,
            "mass": 150,
            "moi": 8.2668,
            "maxbraketorque": 10000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "sprungmass": 2857,
            "springstrength": 85000,
            "springdamperrate": 18428,
            "dampingrate": 727,
            "dampingrateinair": 727,
            "dampingratedamaged": 10,
            "dampingradtedestroyed": 10000,
            "latstiffx": 1,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 32000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|Wheels|L9 [Indent level: 2],
        "l9": {
            "bonename": "",
            "center": "wheel_1_9_axis",
            "boundary": "wheel_1_9_bound",
            "maxdroop": 0,
            "maxcompression": 0,
            "side": "left",
            "width": 0.39,
            "steering": 0,
            "mass": 150,
            "moi": 8.2668,
            "maxbraketorque": 10000,
            "sprungmass": 2857,
            "springstrength": 85000,
            "springdamperrate": 18428,
            "dampingrate": 727,
            "dampingrateinair": 727,
            "dampingratedamaged": 10,
            "dampingradtedestroyed": 10000,
            "latstiffx": 1,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 32000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|Wheels|L1 [Indent level: 2],
        "l1": {
            "bonename": "",
            "center": "wheel_1_1_axis",
            "boundary": "wheel_1_1_bound",
            "maxdroop": 0,
            "maxcompression": 0,
            "side": "left",
            "width": 0.39,
            "steering": 0,
            "mass": 150,
            "moi": 8.2668,
            "maxbraketorque": 10000,
            "sprungmass": 2857,
            "springstrength": 85000,
            "springdamperrate": 18428,
            "dampingrate": 727,
            "dampingrateinair": 727,
            "dampingratedamaged": 10,
            "dampingradtedestroyed": 10000,
            "latstiffx": 1,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 32000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|Wheels|R2 [Indent level: 2],
        "r2": {
            "bonename": "wheel_podkolop1",
            "center": "wheel_2_2_axis",
            "boundary": "wheel_2_2_bound",
            "side": "right",
            "width": 0.39,
            "steering": 0,
            "mass": 150,
            "moi": 8.2668,
            "maxbraketorque": 10000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "sprungmass": 2857,
            "springstrength": 85000,
            "springdamperrate": 18428,
            "dampingrate": 727,
            "dampingrateinair": 727,
            "dampingratedamaged": 10,
            "dampingradtedestroyed": 10000,
            "latstiffx": 1,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 32000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|Wheels|R3 [Indent level: 2],
        "r3": {
            "bonename": "wheel_podkolop2",
            "center": "wheel_2_3_axis",
            "boundary": "wheel_2_3_bound",
            "side": "right",
            "width": 0.39,
            "steering": 0,
            "mass": 150,
            "moi": 8.2668,
            "maxbraketorque": 10000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "sprungmass": 2857,
            "springstrength": 85000,
            "springdamperrate": 18428,
            "dampingrate": 727,
            "dampingrateinair": 727,
            "dampingratedamaged": 10,
            "dampingradtedestroyed": 10000,
            "latstiffx": 1,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 32000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|Wheels|R4 [Indent level: 2],
        "r4": {
            "bonename": "wheel_podkolop3",
            "center": "wheel_2_4_axis",
            "boundary": "wheel_2_4_bound",
            "side": "right",
            "width": 0.39,
            "steering": 0,
            "mass": 150,
            "moi": 8.2668,
            "maxbraketorque": 10000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "sprungmass": 2857,
            "springstrength": 85000,
            "springdamperrate": 18428,
            "dampingrate": 727,
            "dampingrateinair": 727,
            "dampingratedamaged": 10,
            "dampingradtedestroyed": 10000,
            "latstiffx": 1,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 32000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|Wheels|R5 [Indent level: 2],
        "r5": {
            "bonename": "wheel_podkolop4",
            "center": "wheel_2_5_axis",
            "boundary": "wheel_2_5_bound",
            "side": "right",
            "width": 0.39,
            "steering": 0,
            "mass": 150,
            "moi": 8.2668,
            "maxbraketorque": 10000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "sprungmass": 2857,
            "springstrength": 85000,
            "springdamperrate": 18428,
            "dampingrate": 727,
            "dampingrateinair": 727,
            "dampingratedamaged": 10,
            "dampingradtedestroyed": 10000,
            "latstiffx": 1,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 32000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|Wheels|R6 [Indent level: 2],
        "r6": {
            "bonename": "wheel_podkolop5",
            "center": "wheel_2_6_axis",
            "boundary": "wheel_2_6_bound",
            "side": "right",
            "width": 0.39,
            "steering": 0,
            "mass": 150,
            "moi": 8.2668,
            "maxbraketorque": 10000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "sprungmass": 2857,
            "springstrength": 85000,
            "springdamperrate": 18428,
            "dampingrate": 727,
            "dampingrateinair": 727,
            "dampingratedamaged": 10,
            "dampingradtedestroyed": 10000,
            "latstiffx": 1,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 32000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|Wheels|R7 [Indent level: 2],
        "r7": {
            "bonename": "wheel_podkolop6",
            "center": "wheel_2_7_axis",
            "boundary": "wheel_2_7_bound",
            "side": "right",
            "width": 0.39,
            "steering": 0,
            "mass": 150,
            "moi": 8.2668,
            "maxbraketorque": 10000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "sprungmass": 2857,
            "springstrength": 85000,
            "springdamperrate": 18428,
            "dampingrate": 727,
            "dampingrateinair": 727,
            "dampingratedamaged": 10,
            "dampingradtedestroyed": 10000,
            "latstiffx": 1,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 32000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|Wheels|R8 [Indent level: 2],
        "r8": {
            "bonename": "wheel_podkolop7",
            "center": "wheel_2_8_axis",
            "boundary": "wheel_2_8_bound",
            "side": "right",
            "width": 0.39,
            "steering": 0,
            "mass": 150,
            "moi": 8.2668,
            "maxbraketorque": 10000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "sprungmass": 2857,
            "springstrength": 85000,
            "springdamperrate": 18428,
            "dampingrate": 727,
            "dampingrateinair": 727,
            "dampingratedamaged": 10,
            "dampingradtedestroyed": 10000,
            "latstiffx": 1,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 32000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|Wheels|R9 [Indent level: 2],
        "r9": {
            "bonename": "",
            "center": "wheel_2_9_axis",
            "boundary": "wheel_2_9_bound",
            "maxdroop": 0,
            "maxcompression": 0,
            "side": "right",
            "width": 0.39,
            "steering": 0,
            "mass": 150,
            "moi": 8.2668,
            "maxbraketorque": 10000,
            "sprungmass": 2857,
            "springstrength": 85000,
            "springdamperrate": 18428,
            "dampingrate": 727,
            "dampingrateinair": 727,
            "dampingratedamaged": 10,
            "dampingradtedestroyed": 10000,
            "latstiffx": 1,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 32000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|Wheels|R1 [Indent level: 2],
        "r1": {
            "bonename": "",
            "center": "wheel_2_1_axis",
            "boundary": "wheel_2_1_bound",
            "maxdroop": 0,
            "maxcompression": 0,
            "side": "right",
            "width": 0.39,
            "steering": 0,
            "mass": 150,
            "moi": 8.2668,
            "maxbraketorque": 10000,
            "sprungmass": 2857,
            "springstrength": 85000,
            "springdamperrate": 18428,
            "dampingrate": 727,
            "dampingrateinair": 727,
            "dampingratedamaged": 10,
            "dampingradtedestroyed": 10000,
            "latstiffx": 1,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 32000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        }
    },
    "tracksspeed": 1.35,
    "wheelcircumference": 2.375,
    "attenuationeffecttype": "TankAttenuation",
    "extcameraposition": [0,2,-15],
    "weapons": ["rhs_weap_smokegen"],
    "magazines": ["rhs_mag_smokegen"],
    "driverdoor": "HatchD",
    "driveraction": "RHS_M109_DriverOut",
    "driverinaction": "RHS_M109_DriverIn",
    "cost": 1.5e+006,
    "damageresistance": 0.02,
    "crewvulnerable": 0,
    "incomingmissiledetectionsystem": 0,
    "armor": 200,
    "armorstructural": 600,
    # Class: CfgVehicles|rhsusf_m109tank_base|HitPoints [Indent level: 1],
    "hitpoints": {
        # Class: CfgVehicles|rhsusf_m109tank_base|HitPoints|HitHull [Indent level: 2]
        "hithull": {
            "armor": 0.4,
            "material": -1,
            "name": "telo",
            "visual": "zbytek",
            "passthrough": 0,
            "minimalhit": 0.08,
            "explosionshielding": 0,
            "radius": 0.25,
            "armorcomponent": "hit_hull"
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|HitPoints|HitEngine [Indent level: 2],
        "hitengine": {
            "armor": 0.45,
            "material": -1,
            "name": "motor",
            "passthrough": 0,
            "minimalhit": 0.139,
            "explosionshielding": 0.009,
            "radius": 0.27,
            "armorcomponent": "hit_engine",
            "visual": "-"
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|HitPoints|HitLTrack [Indent level: 2],
        "hitltrack": {
            "armor": -150,
            "material": -1,
            "name": "pas_L",
            "passthrough": 0,
            "minimalhit": -0.25,
            "explosionshielding": 0.5,
            "radius": 0.3,
            "armorcomponent": "hit_trackL",
            "visual": "-"
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|HitPoints|HitRTrack [Indent level: 2],
        "hitrtrack": {
            "armor": -150,
            "material": -1,
            "name": "pas_P",
            "passthrough": 0,
            "minimalhit": -0.25,
            "explosionshielding": 0.5,
            "radius": 0.3,
            "armorcomponent": "hit_trackR",
            "visual": "-"
        },
        # Class: CfgVehicles|MBT_01_base_F|HitPoints|HitFuel [Indent level: 2],
        "hitfuel": {
            "armor": 0.3,
            "material": -1,
            "armorcomponent": "hit_fuel",
            "name": "hit_fuel_point",
            "visual": "-",
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "explosionshielding": 0.6,
            "radius": 0.3
        }
    },
    # Class: CfgVehicles|rhsusf_m109tank_base|TransportBackpacks [Indent level: 1],
    "transportbackpacks": {
        # Class: CfgVehicles|rhsusf_m109tank_base|TransportBackpacks|_xx_rhsusf_falconii [Indent level: 2]
        "_xx_rhsusf_falconii": {
            "backpack": "rhsusf_falconii",
            "count": 2
        }
    },
    # Class: CfgVehicles|rhsusf_m109tank_base|TransportMagazines [Indent level: 1],
    "transportmagazines": {
        # Class: CfgVehicles|rhsusf_m109tank_base|TransportMagazines|_xx_rhs_mag_30Rnd_556x45_M855A1_Stanag [Indent level: 2]
        "_xx_rhs_mag_30rnd_556x45_m855a1_stanag": {
            "count": 20,
            "magazine": "rhs_mag_30Rnd_556x45_M855A1_Stanag"
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|TransportMagazines|_xx_rhs_mag_m67 [Indent level: 2],
        "_xx_rhs_mag_m67": {
            "count": 10,
            "magazine": "rhs_mag_m67"
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|TransportMagazines|_xx_rhs_mag_m18_green [Indent level: 2],
        "_xx_rhs_mag_m18_green": {
            "count": 2,
            "magazine": "rhs_mag_m18_green"
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|TransportMagazines|_xx_rhs_mag_m18_red [Indent level: 2],
        "_xx_rhs_mag_m18_red": {
            "count": 2,
            "magazine": "rhs_mag_m18_red"
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|TransportMagazines|_xx_rhs_mag_m18_yellow [Indent level: 2],
        "_xx_rhs_mag_m18_yellow": {
            "count": 2,
            "magazine": "rhs_mag_m18_yellow"
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|TransportMagazines|_xx_rhs_mag_m18_purple [Indent level: 2],
        "_xx_rhs_mag_m18_purple": {
            "count": 2,
            "magazine": "rhs_mag_m18_purple"
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|TransportMagazines|_xx_rhs_mag_an_m8hc [Indent level: 2],
        "_xx_rhs_mag_an_m8hc": {
            "count": 4,
            "magazine": "rhs_mag_an_m8hc"
        }
    },
    # Class: CfgVehicles|rhsusf_m109tank_base|TransportItems [Indent level: 1],
    "transportitems": {
        # Class: CfgVehicles|rhsusf_m109tank_base|TransportItems|_xx_FirstAidKit [Indent level: 2]
        "_xx_firstaidkit": {
            "name": "FirstAidKit",
            "count": 8
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|TransportItems|_xx_Medikit [Indent level: 2],
        "_xx_medikit": {
            "name": "Medikit",
            "count": 1
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|TransportItems|_xx_Toolkit [Indent level: 2],
        "_xx_toolkit": {
            "name": "Toolkit",
            "count": 1
        }
    },
    # Class: CfgVehicles|rhsusf_m109tank_base|TransportWeapons [Indent level: 1],
    "transportweapons": {
        # Class: CfgVehicles|rhsusf_m109tank_base|TransportWeapons|_xx_weap [Indent level: 2]
        "_xx_weap": {
            "count": 2,
            "weapon": "rhs_weap_m4_carryhandle"
        }
    },
    # Class: CfgVehicles|rhsusf_m109tank_base|Turrets [Indent level: 1],
    "turrets": {
        # Class: CfgVehicles|rhsusf_m109tank_base|Turrets|MainTurret [Indent level: 2]
        "mainturret": {
            # Class: CfgVehicles|rhsusf_m109tank_base|Turrets|MainTurret|Turrets [Indent level: 3]
            "turrets": {
                # Class: CfgVehicles|rhsusf_m109tank_base|Turrets|MainTurret|Turrets|CommanderOptics [Indent level: 4]
                "commanderoptics": {
                    "body": "obsTurret",
                    "gun": "obsGun",
                    "gunbeg": "com_pos",
                    "gunend": "com_dir",
                    "animationsourcebody": "obsTurret",
                    "animationsourcegun": "obsGun",
                    "maxhorizontalrotspeed": 1.8,
                    "maxverticalrotspeed": 1.8,
                    "stabilizedinaxes": 3,
                    "soundservo": ["A3|Sounds_F|vehicles|armor|noises|servo_best",0.01,1,50],
                    "minelev": -5,
                    "maxelev": 60,
                    "initelev": 0,
                    "minturn": -360,
                    "maxturn": 360,
                    "initturn": 0,
                    "maxoutelev": 40,
                    "maxoutturn": 115,
                    "minoutturn": -115,
                    "weapons": [],
                    "magazines": [],
                    "lodturnedout": 0,
                    "gunnerforceoptics": 1,
                    "memorypointgunneroutoptics": "commanderview",
                    "memorypointgunneroptics": "commanderview",
                    "gunneropticsmodel": "A3|weapons_f|reticle|Optics_Commander_02_F",
                    "gunneroutopticsmodel": "",
                    "gunneropticseffect": [],
                    "gunnerhasflares": 1,
                    # Class: CfgVehicles|rhsusf_m109tank_base|Turrets|MainTurret|Turrets|CommanderOptics|ViewOptics [Indent level: 5],
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
                        "maxmovez": 0
                    },
                    "gunneraction": "mbt2_slot2b_out",
                    "gunnerinaction": "mbt2_slot2b_in",
                    "gunnergetinaction": "GetInHigh",
                    "gunnergetoutaction": "GetOutHigh",
                    "gunnerdoor": "HatchC",
                    "startengine": 0,
                    "viewgunnerinexternal": 1,
                    "outgunnermayfire": 1,
                    "ingunnermayfire": 1,
                    # Class: CfgVehicles|rhsusf_m109tank_base|Turrets|MainTurret|Turrets|CommanderOptics|HitPoints [Indent level: 5],
                    "hitpoints": {
                        # Class: CfgVehicles|rhsusf_m109tank_base|Turrets|MainTurret|Turrets|CommanderOptics|HitPoints|HitTurretCom [Indent level: 6]
                        "hitturretcom": {
                            "armor": 0.3,
                            "material": -1,
                            "name": "vezVelitele",
                            "visual": "vezVelitele",
                            "passthrough": 0,
                            "minimalhit": 0.03,
                            "explosionshielding": 0.6,
                            "radius": 0.25,
                            "isturret": 1
                        },
                        # Class: CfgVehicles|rhsusf_m109tank_base|Turrets|MainTurret|Turrets|CommanderOptics|HitPoints|HitGunCom [Indent level: 6],
                        "hitguncom": {
                            "armor": 0.3,
                            "material": -1,
                            "name": "zbranVelitele",
                            "visual": "zbranVelitele",
                            "passthrough": 0,
                            "minimalhit": 0.03,
                            "explosionshielding": 0.6,
                            "radius": 0.25,
                            "isgun": 1
                        }
                    },
                    "selectionfireanim": "zasleh3",
                    "memorypointgun": "usti hlavne2",
                    "discretedistance": [100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000],
                    "discretedistanceinitindex": 2,
                    "usepip": 2,
                    "forcehidegunner": 1,
                    "ispersonturret": 0,
                    "animationsourcestickx": "com_turret_control_x",
                    "animationsourcesticky": "com_turret_control_y",
                    "gunnerlefthandanimname": "com_turret_control_y",
                    "gunnerrighthandanimname": "com_turret_control_y",
                    "lodturnedin": 1000,
                    "lodopticsin": 0,
                    "minoutelev": -10,
                    "initoutelev": 0,
                    "initoutturn": 0,
                    # Class: CfgVehicles|MBT_01_arty_base_F|Turrets|MainTurret|Turrets|CommanderOptics|OpticsIn [Indent level: 5],
                    "opticsin": {
                        # Class: CfgVehicles|MBT_01_arty_base_F|Turrets|MainTurret|Turrets|CommanderOptics|OpticsIn|Wide [Indent level: 6]
                        "wide": {
                            "gunneropticsmodel": "A3|weapons_f|reticle|Optics_Gunner_02_F",
                            "initanglex": 0,
                            "minanglex": -30,
                            "maxanglex": 30,
                            "initangley": 0,
                            "minangley": -100,
                            "maxangley": 100,
                            "initfov": 0.4375,
                            "minfov": 0.03482,
                            "maxfov": 0.4375,
                            "visionmode": ["Normal","NVG","Ti"],
                            "thermalmode": [0,1],
                            "minmovex": 0,
                            "maxmovex": 0,
                            "minmovey": 0,
                            "maxmovey": 0,
                            "minmovez": 0,
                            "maxmovez": 0
                        }
                    },
                    "soundservovertical": ["A3|Sounds_F|vehicles|armor|noises|servo_armor_comm",0.562341,1,30],
                    "turretfollowfreelook": 2,
                    "viewgunnershadowamb": 0.5,
                    "viewgunnershadowdiff": 0.05,
                    "personturretaction": "vehicle_turnout_2",
                    # Class: CfgVehicles|MBT_01_base_F|Turrets|MainTurret|Turrets|CommanderOptics|ViewGunner [Indent level: 5],
                    "viewgunner": {
                        "initanglex": -10,
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
                    "turretinfotype": "RscOptics_MBT_01_commander",
                    "showcrewaim": 1,
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
                    "commanding": 2,
                    "gunneroutopticscolor": [0,0,0,1],
                    "gunneroutforceoptics": 0,
                    "gunneroutopticsshowcursor": 0,
                    "gunneroutopticseffect": [],
                    "memorypointsgetingunner": "pos commander",
                    "memorypointsgetingunnerdir": "pos commander dir",
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
                    "hideweaponsgunner": 1,
                    "canhidegunner": -1,
                    "showhmd": 0,
                    "lockwhendriverout": 0,
                    "lockwhenvehiclespeed": -1,
                    "gunnercompartments": "Compartment1",
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
            "weapons": ["rhs_weap_m284"],
            "magazines": ["rhs_mag_155mm_m795_28","rhs_mag_155mm_m825a1_2","rhs_mag_155mm_485_2","rhs_mag_155mm_m712_2","rhs_mag_155mm_m731_1","rhs_mag_155mm_raams_1","rhs_mag_155mm_m864_3"],
            "memorypointgun": "usti hlavne2",
            "selectionfireanim": "zasleh2",
            "gunbeg": "usti hlavne3",
            "gunend": "konec hlavne3",
            "minelev": -5,
            "maxelev": 80,
            "initelev": 10,
            "maxhorizontalrotspeed": 0.365,
            "soundservo": ["A3|Sounds_F|vehicles|armor|noises|servo_best",0.316228,1,50],
            "lockwhenvehiclespeed": 3,
            "memorypointgunneroptics": "gunnerview",
            "gunneroutopticsmodel": "",
            "gunneroutopticseffect": [],
            "gunneropticseffect": [],
            "gunnerforceoptics": 1,
            # Class: CfgVehicles|rhsusf_m109tank_base|Turrets|MainTurret|OpticsIn [Indent level: 3],
            "opticsin": {
                # Class: CfgVehicles|rhsusf_m109tank_base|Turrets|MainTurret|OpticsIn|Wide [Indent level: 4]
                "wide": {
                    "initanglex": 0,
                    "minanglex": -30,
                    "maxanglex": 30,
                    "initangley": 0,
                    "minangley": -100,
                    "maxangley": 100,
                    "initfov": 0.3,
                    "minfov": 0.3,
                    "maxfov": 0.3,
                    "visionmode": ["Normal","Ti"],
                    "thermalmode": [4,5],
                    "gunneropticsmodel": "A3|Weapons_F|Reticle|Optics_Gunner_MTB_02_w_F.p3d",
                    "gunneropticseffect": [],
                    "minmovex": 0,
                    "maxmovex": 0,
                    "minmovey": 0,
                    "maxmovey": 0,
                    "minmovez": 0,
                    "maxmovez": 0,
                    "speedzoommaxspeed": 1e+010,
                    "speedzoommaxfov": 0
                },
                # Class: CfgVehicles|rhsusf_m109tank_base|Turrets|MainTurret|OpticsIn|Medium [Indent level: 4],
                "medium": {
                    "gunneropticsmodel": "A3|Weapons_F|Reticle|Optics_Gunner_MTB_02_m_F.p3d",
                    "initfov": 0.07,
                    "minfov": 0.07,
                    "maxfov": 0.07,
                    "initanglex": 0,
                    "minanglex": -30,
                    "maxanglex": 30,
                    "initangley": 0,
                    "minangley": -100,
                    "maxangley": 100,
                    "visionmode": ["Normal","Ti"],
                    "thermalmode": [4,5],
                    "gunneropticseffect": [],
                    "minmovex": 0,
                    "maxmovex": 0,
                    "minmovey": 0,
                    "maxmovey": 0,
                    "minmovez": 0,
                    "maxmovez": 0,
                    "speedzoommaxspeed": 1e+010,
                    "speedzoommaxfov": 0
                },
                # Class: CfgVehicles|rhsusf_m109tank_base|Turrets|MainTurret|OpticsIn|Narrow [Indent level: 4],
                "narrow": {
                    "gunneropticsmodel": "A3|Weapons_F|Reticle|Optics_Gunner_MTB_02_n_F.p3d",
                    "initfov": 0.028,
                    "minfov": 0.028,
                    "maxfov": 0.028,
                    "initanglex": 0,
                    "minanglex": -30,
                    "maxanglex": 30,
                    "initangley": 0,
                    "minangley": -100,
                    "maxangley": 100,
                    "visionmode": ["Normal","Ti"],
                    "thermalmode": [4,5],
                    "gunneropticseffect": [],
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
            "gunnerinaction": "mbt2_slot2a_in",
            "gunnerdoor": "HatchC",
            "forcehidegunner": 1,
            "ingunnermayfire": 1,
            "viewgunnerinexternal": 1,
            # Class: CfgVehicles|rhsusf_m109tank_base|Turrets|MainTurret|HitPoints [Indent level: 3],
            "hitpoints": {
                # Class: CfgVehicles|rhsusf_m109tank_base|Turrets|MainTurret|HitPoints|HitTurret [Indent level: 4]
                "hitturret": {
                    "armor": 0.5,
                    "material": -1,
                    "name": "vez",
                    "visual": "zbytek",
                    "passthrough": 0,
                    "minimalhit": 0.14,
                    "explosionshielding": 0.001,
                    "radius": 0.08
                },
                # Class: CfgVehicles|rhsusf_m109tank_base|Turrets|MainTurret|HitPoints|HitGun [Indent level: 4],
                "hitgun": {
                    "armor": 0.6,
                    "material": -1,
                    "name": "zbran",
                    "visual": "zbytek",
                    "passthrough": 0,
                    "minimalhit": 0.13,
                    "explosionshielding": 0.001,
                    "radius": 0.25
                }
            },
            "animationsourcehatch": "hatchCommander",
            "usepip": 2,
            "gunnergetinaction": "GetInHigh",
            "gunnergetoutaction": "GetOutHigh",
            "animationsourcestickx": "turret_control_x",
            "animationsourcesticky": "turret_control_y",
            "gunnerlefthandanimname": "turret_control_y",
            "gunnerrighthandanimname": "turret_control_y",
            "lodturnedin": 1000,
            "lodopticsin": 0,
            "soundservovertical": ["A3|Sounds_F|vehicles|armor|noises|servo_armor_gunner_vertical",0.158489,1,30],
            "elevationmode": 3,
            "maxverticalrotspeed": 0.26,
            "cameradir": "look",
            "turretinfotype": "RscWeaponRangeArtilleryAuto",
            # Class: CfgVehicles|MBT_01_base_F|Turrets|MainTurret|ViewGunner [Indent level: 3],
            "viewgunner": {
                "initanglex": -17,
                "initangley": 0,
                "initfov": 0.9,
                "minfov": 0.25,
                "maxfov": 1.25,
                "minanglex": -65,
                "maxanglex": 85,
                "minangley": -150,
                "maxangley": 150,
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
            "viewgunnershadowamb": 0.5,
            "viewgunnershadowdiff": 0.05,
            "discretedistance": [100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000,2100,2200,2300,2400,2500,2600,2700,2800,2900,3000,3100,3200,3300,3400,3500,3600,3700,3800,3900,4000],
            "discretedistanceinitindex": 5,
            "startengine": 0,
            "showcrewaim": 2,
            "commanding": 1,
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
            "stabilizedinaxes": 3,
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
            "hideweaponsgunner": 1,
            "canhidegunner": -1,
            "outgunnermayfire": 0,
            "showhmd": 0,
            "lockwhendriverout": 0,
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
    "hiddenselections": ["camo1","camo2","camo3","camo4","camo5"],
    # Class: CfgVehicles|rhsusf_m109tank_base|textureSources [Indent level: 1],
    "texturesources": {
        # Class: CfgVehicles|rhsusf_m109tank_base|textureSources|standard [Indent level: 2]
        "standard": {
            "displayname": "Woodland",
            "author": "Red Hammer Studios",
            "textures": ["rhsusf|addons|rhsusf_m109|data|rhsusf_m109a6_01_wd_co.paa","rhsusf|addons|rhsusf_m109|data|rhsusf_m109a6_02_wd_co.paa","rhsusf|addons|rhsusf_m109|data|rhsusf_m109a6_03_wd_co.paa","rhsusf|addons|rhsusf_m109|data|rhsusf_m109a6_mesh_wd_ca.paa","rhsusf|addons|rhsusf_m109|data|rhsusf_m109a6_wheels_wd_co.paa"],
            "factions": ["rhs_faction_usarmy_wd"]
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|textureSources|Desert [Indent level: 2],
        "desert": {
            "displayname": "Desert",
            "author": "Red Hammer Studios",
            "textures": ["rhsusf|addons|rhsusf_m109|data|rhsusf_m109a6_01_d_co.paa","rhsusf|addons|rhsusf_m109|data|rhsusf_m109a6_02_d_co.paa","rhsusf|addons|rhsusf_m109|data|rhsusf_m109a6_03_d_co.paa","rhsusf|addons|rhsusf_m109|data|rhsusf_m109a6_mesh_d_ca.paa","rhsusf|addons|rhsusf_m109|data|rhsusf_m109a6_wheels_d_co.paa"],
            "factions": ["rhs_faction_usarmy_d"]
        }
    },
    "texturelist": [],
    "availableforsupporttypes": ["Artillery"],
    # Class: CfgVehicles|rhsusf_m109tank_base|Damage [Indent level: 1],
    "damage": {
        "tex": [],
        "mat": ["rhsusf|addons|rhsusf_m109|data|rhsusf_m109a6_01_d.rvmat","rhsusf|addons|rhsusf_m109|data|rhsusf_dam_m109a6_01_d.rvmat","rhsusf|addons|rhsusf_m109|data|rhsusf_destr_m109.rvmat","rhsusf|addons|rhsusf_m109|data|rhsusf_m109a6_02_d.rvmat","rhsusf|addons|rhsusf_m109|data|rhsusf_dam_m109a6_02_d.rvmat","rhsusf|addons|rhsusf_m109|data|rhsusf_destr_m109.rvmat","rhsusf|addons|rhsusf_m109|data|rhsusf_m109a6_03_d.rvmat","rhsusf|addons|rhsusf_m109|data|rhsusf_dam_m109a6_03_d.rvmat","rhsusf|addons|rhsusf_m109|data|rhsusf_destr_m109.rvmat","rhsusf|addons|rhsusf_m109|data|rhsusf_m109a6_mesh_d.rvmat","rhsusf|addons|rhsusf_m109|data|rhsusf_dam_m109a6_mesh_d.rvmat","rhsusf|addons|rhsusf_m109|data|rhsusf_destr_m109.rvmat","rhsusf|addons|rhsusf_m109|data|rhsusf_m109a6_tracks.rvmat","rhsusf|addons|rhsusf_m109|data|rhsusf_dam_m109a6_tracks.rvmat","rhsusf|addons|rhsusf_m109|data|rhsusf_destr_m109.rvmat","rhsusf|addons|rhsusf_m109|data|rhsusf_m109a6_wheels_d.rvmat","rhsusf|addons|rhsusf_m109|data|rhsusf_dam_m109a6_wheels_d.rvmat","rhsusf|addons|rhsusf_m109|data|rhsusf_destr_m109.rvmat","a3|data_f|default.rvmat","a3|data_f|default.rvmat","a3|data_f|default_destruct.rvmat"]
    },
    # Class: CfgVehicles|rhsusf_m109tank_base|ViewOptics [Indent level: 1],
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
    # Class: CfgVehicles|rhsusf_m109tank_base|Exhausts [Indent level: 1],
    "exhausts": {
        # Class: CfgVehicles|rhsusf_m109tank_base|Exhausts|Exhaust1 [Indent level: 2]
        "exhaust1": {
            "position": "exhaustr",
            "direction": "exhaustr_dir",
            "effect": "ExhaustEffectTankSide"
        }
    },
    # Class: CfgVehicles|rhsusf_m109tank_base|Reflectors [Indent level: 1],
    "reflectors": {
        # Class: CfgVehicles|rhsusf_m109tank_base|Reflectors|Left [Indent level: 2]
        "left": {
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "position": "l svetlo",
            "direction": "konec l svetlo",
            "hitpoint": "l svetlo",
            "selection": "L svetlo",
            "size": 1,
            "innerangle": 100,
            "outerangle": 179,
            "conefadecoef": 10,
            "intensity": 1,
            "useflare": 0,
            "daylight": 0,
            "flaresize": 1,
            # Class: CfgVehicles|rhsusf_m109tank_base|Reflectors|Left|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardlimitstart": 30,
                "hardlimitend": 60
            }
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|Reflectors|Right [Indent level: 2],
        "right": {
            "position": "P svetlo",
            "direction": "konec P svetlo",
            "hitpoint": "P svetlo",
            "selection": "P svetlo",
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "size": 1,
            "innerangle": 100,
            "outerangle": 179,
            "conefadecoef": 10,
            "intensity": 1,
            "useflare": 0,
            "daylight": 0,
            "flaresize": 1,
            # Class: CfgVehicles|rhsusf_m109tank_base|Reflectors|Left|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardlimitstart": 30,
                "hardlimitend": 60
            }
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|Reflectors|Right2 [Indent level: 2],
        "right2": {
            "direction": "konec P svetlo",
            "useflare": 1,
            "position": "P svetlo",
            "hitpoint": "P svetlo",
            "selection": "P svetlo",
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "size": 1,
            "innerangle": 100,
            "outerangle": 179,
            "conefadecoef": 10,
            "intensity": 1,
            "daylight": 0,
            "flaresize": 1,
            # Class: CfgVehicles|rhsusf_m109tank_base|Reflectors|Left|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardlimitstart": 30,
                "hardlimitend": 60
            }
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|Reflectors|Left2 [Indent level: 2],
        "left2": {
            "direction": "konec l svetlo",
            "useflare": 1,
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "position": "l svetlo",
            "hitpoint": "l svetlo",
            "selection": "L svetlo",
            "size": 1,
            "innerangle": 100,
            "outerangle": 179,
            "conefadecoef": 10,
            "intensity": 1,
            "daylight": 0,
            "flaresize": 1,
            # Class: CfgVehicles|rhsusf_m109tank_base|Reflectors|Left|Attenuation [Indent level: 3],
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
    # Class: CfgVehicles|rhsusf_m109tank_base|AnimationSources [Indent level: 1],
    "animationsources": {
        # Class: CfgVehicles|rhsusf_m109tank_base|AnimationSources|IFF_Panels_Hide [Indent level: 2]
        "iff_panels_hide": {
            "source": "user",
            "mass": -20,
            "displayname": "hide IFF Panels",
            "author": "Red Hammer Studios",
            "animperiod": 1e-005,
            "initphase": 0
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|AnimationSources|recoil_source [Indent level: 2],
        "recoil_source": {
            "source": "reload",
            "weapon": "rhs_weap_m284"
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|AnimationSources|muzzle_hide_arty [Indent level: 2],
        "muzzle_hide_arty": {
            "source": "reload",
            "weapon": "rhs_weap_m284"
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|AnimationSources|HatchC [Indent level: 2],
        "hatchc": {
            "source": "door",
            "animperiod": 2.1
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|AnimationSources|HatchD [Indent level: 2],
        "hatchd": {
            "source": "door",
            "animperiod": 2.1
        },
        # Class: CfgVehicles|MBT_01_arty_base_F|AnimationSources|muzzle_rot_HMG [Indent level: 2],
        "muzzle_rot_hmg": {
            "source": "ammorandom",
            "weapon": "HMG_127_APC"
        },
        # Class: CfgVehicles|MBT_01_arty_base_F|AnimationSources|muzzle_hide_HMG [Indent level: 2],
        "muzzle_hide_hmg": {
            "source": "reload",
            "weapon": "HMG_127_APC"
        },
        # Class: CfgVehicles|MBT_01_arty_base_F|AnimationSources|muzzle_rot_GMG [Indent level: 2],
        "muzzle_rot_gmg": {
            "source": "ammorandom",
            "weapon": "GMG_40mm"
        },
        # Class: CfgVehicles|MBT_01_arty_base_F|AnimationSources|muzzle_hide_GMG [Indent level: 2],
        "muzzle_hide_gmg": {
            "source": "reload",
            "weapon": "GMG_40mm"
        },
        # Class: CfgVehicles|MBT_01_arty_base_F|AnimationSources|HitComTurret_src [Indent level: 2],
        "hitcomturret_src": {
            "source": "Hit",
            "hitpoint": "HitComTurret",
            "raw": 1
        },
        # Class: CfgVehicles|MBT_01_arty_base_F|AnimationSources|showCanisters [Indent level: 2],
        "showcanisters": {
            "displayname": "Show Canisters",
            "author": "Bohemia Interactive",
            "source": "user",
            "animperiod": 0.001,
            "forceanimatephase": 0,
            "forceanimate": ["showCamonetTurret",0],
            "initphase": 0,
            "mass": -50
        },
        # Class: CfgVehicles|MBT_01_arty_base_F|AnimationSources|showCamonetTurret [Indent level: 2],
        "showcamonetturret": {
            "displayname": "Show Camo Net (Turret)",
            "author": "Bohemia Interactive",
            "source": "user",
            "animperiod": 0.001,
            "initphase": 0,
            "forceanimatephase": 1,
            "forceanimate": ["showCanisters",1,"showAmmobox",1],
            "forceanimate2": ["showCanisters",0,"showAmmobox",0],
            "mass": -50
        },
        # Class: CfgVehicles|MBT_01_arty_base_F|AnimationSources|showAmmobox [Indent level: 2],
        "showammobox": {
            "displayname": "Show Ammo Boxes",
            "author": "Bohemia Interactive",
            "source": "user",
            "animperiod": 0.001,
            "forceanimatephase": 0,
            "forceanimate": ["showCamonetTurret",0],
            "initphase": 0,
            "mass": -50
        },
        # Class: CfgVehicles|MBT_01_base_F|AnimationSources|muzzle_rot_cannon [Indent level: 2],
        "muzzle_rot_cannon": {
            "source": "ammorandom",
            "weapon": "cannon_120mm"
        },
        # Class: CfgVehicles|MBT_01_base_F|AnimationSources|muzzle_rot_coax [Indent level: 2],
        "muzzle_rot_coax": {
            "source": "ammorandom",
            "weapon": "LMG_M200"
        },
        # Class: CfgVehicles|MBT_01_base_F|AnimationSources|muzzle_hide_coax [Indent level: 2],
        "muzzle_hide_coax": {
            "source": "reload",
            "weapon": "LMG_M200"
        },
        # Class: CfgVehicles|MBT_01_base_F|AnimationSources|Smoke_source [Indent level: 2],
        "smoke_source": {
            "source": "revolving",
            "weapon": "SmokeLauncher"
        },
        # Class: CfgVehicles|MBT_01_base_F|AnimationSources|HitEngine_src [Indent level: 2],
        "hitengine_src": {
            "source": "Hit",
            "hitpoint": "HitEngine",
            "raw": 1
        },
        # Class: CfgVehicles|MBT_01_base_F|AnimationSources|HitFuel_src [Indent level: 2],
        "hitfuel_src": {
            "source": "Hit",
            "hitpoint": "HitFuel",
            "raw": 1
        },
        # Class: CfgVehicles|MBT_01_base_F|AnimationSources|HitHull_src [Indent level: 2],
        "hithull_src": {
            "source": "Hit",
            "hitpoint": "HitHull",
            "raw": 1
        },
        # Class: CfgVehicles|MBT_01_base_F|AnimationSources|HitMainGun_src [Indent level: 2],
        "hitmaingun_src": {
            "source": "Hit",
            "hitpoint": "HitGun",
            "raw": 1
        },
        # Class: CfgVehicles|MBT_01_base_F|AnimationSources|HitTurret_src [Indent level: 2],
        "hitturret_src": {
            "source": "Hit",
            "hitpoint": "HitTurret",
            "raw": 1
        },
        # Class: CfgVehicles|MBT_01_base_F|AnimationSources|showCamonetCannon [Indent level: 2],
        "showcamonetcannon": {
            "source": "user",
            "animperiod": 0.001,
            "initphase": 0
        },
        # Class: CfgVehicles|MBT_01_base_F|AnimationSources|showCamonetPlates1 [Indent level: 2],
        "showcamonetplates1": {
            "source": "user",
            "animperiod": 0.001,
            "initphase": 0
        },
        # Class: CfgVehicles|MBT_01_base_F|AnimationSources|showCamonetPlates2 [Indent level: 2],
        "showcamonetplates2": {
            "source": "user",
            "animperiod": 0.001,
            "initphase": 0
        },
        # Class: CfgVehicles|MBT_01_base_F|AnimationSources|showCamonetHull [Indent level: 2],
        "showcamonethull": {
            "displayname": "Show Camo Net (Hull)",
            "author": "Bohemia Interactive",
            "source": "user",
            "animperiod": 0.001,
            "initphase": 0,
            "forceanimatephase": 1,
            "forceanimate": ["showCamonetPlates1",1,"showCamonetPlates2",1],
            "forceanimate2": ["showCamonetPlates1",0,"showCamonetPlates2",0],
            "mass": -50
        }
    },
    # Class: CfgVehicles|rhsusf_m109tank_base|Attributes [Indent level: 1],
    "attributes": {
        # Class: CfgVehicles|rhsusf_m109tank_base|Attributes|ObjectTexture [Indent level: 2]
        "objecttexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayname": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|Attributes|rhs_hideIFFPanel [Indent level: 2],
        "rhs_hideiffpanel": {
            "displayname": "Hide IFF Panel",
            "property": "rhs_hideIFFPanel",
            "control": "CheckboxNumber",
            "expression": "_this animate ['IFF_Panels_Hide',_value,true]",
            "defaultvalue": "0"
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|Attributes|rhs_ammoslot_1_type [Indent level: 2],
        "rhs_ammoslot_1_type": {
            "displayname": "Ammo slot #1 type",
            "tooltip": "Define type of shell for #1 slot [HE rounds]",
            "property": "rhs_ammoslot_1_type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": 0,
            "typename": "STRING",
            # Class: CfgVehicles|rhsusf_m109tank_base|Attributes|rhs_ammoslot_1_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhsusf_m109tank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_155mm_m795_28 [Indent level: 4]
                "rhs_mag_155mm_m795_28": {
                    "name": "M795 HE round",
                    "value": "rhs_mag_155mm_m795_28",
                    "defaultvalue": "rhs_mag_155mm_m795_28"
                }
            }
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|Attributes|rhs_ammoslot_1 [Indent level: 2],
        "rhs_ammoslot_1": {
            "displayname": "Ammo slot #1 count",
            "tooltip": "Define number of rounds stored inside of type #1. Max 46. Leave -1 for default loadout",
            "property": "rhs_ammoslot_1",
            "control": "Edit",
            "expression": "if(_value >= 0)then{ [_this,_value,'%s',46,['rhs_ammoslot_1','rhs_ammoslot_2','rhs_ammoslot_3','rhs_ammoslot_4','rhs_ammoslot_5']] spawn rhs_fnc_Eden_DefineLoadout};",
            "defaultvalue": "-1",
            "validate": "NUMBER",
            "typename": "NUMBER"
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|Attributes|rhs_ammoslot_2_type [Indent level: 2],
        "rhs_ammoslot_2_type": {
            "displayname": "Ammo slot #2 type",
            "tooltip": "Define type of shell for #2 slot [Smoke rounds]",
            "property": "rhs_ammoslot_2_type",
            # Class: CfgVehicles|rhsusf_m109tank_base|Attributes|rhs_ammoslot_2_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhsusf_m109tank_base|Attributes|rhs_ammoslot_2_type|values|6Rnd_155mm_Mo_smoke [Indent level: 4]
                "6rnd_155mm_mo_smoke": {
                    "name": "M825A1 Smoke round",
                    "value": "6Rnd_155mm_Mo_smoke",
                    "defaultvalue": "6Rnd_155mm_Mo_smoke"
                }
            },
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": 0,
            "typename": "STRING"
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|Attributes|rhs_ammoslot_2 [Indent level: 2],
        "rhs_ammoslot_2": {
            "displayname": "Ammo slot #2 count",
            "tooltip": "Define number of rounds stored inside of type #2. Max 46. Leave -1 for default loadout",
            "property": "rhs_ammoslot_2",
            "control": "Edit",
            "expression": "if(_value >= 0)then{ [_this,_value,'%s',46,['rhs_ammoslot_1','rhs_ammoslot_2','rhs_ammoslot_3','rhs_ammoslot_4','rhs_ammoslot_5']] spawn rhs_fnc_Eden_DefineLoadout};",
            "defaultvalue": "-1",
            "validate": "NUMBER",
            "typename": "NUMBER"
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|Attributes|rhs_ammoslot_3_type [Indent level: 2],
        "rhs_ammoslot_3_type": {
            "displayname": "Ammo slot #3 type",
            "tooltip": "Define type of shell for #3 slot [Cluster rounds]",
            "property": "rhs_ammoslot_3_type",
            # Class: CfgVehicles|rhsusf_m109tank_base|Attributes|rhs_ammoslot_3_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhsusf_m109tank_base|Attributes|rhs_ammoslot_3_type|values|rhs_mag_155mm_m864_3 [Indent level: 4]
                "rhs_mag_155mm_m864_3": {
                    "name": "M864 Cluster round",
                    "value": "rhs_mag_155mm_m864_3",
                    "defaultvalue": "rhs_mag_155mm_m864_3"
                }
            },
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": 0,
            "typename": "STRING"
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|Attributes|rhs_ammoslot_3 [Indent level: 2],
        "rhs_ammoslot_3": {
            "displayname": "Ammo slot #3 count",
            "tooltip": "Define number of rounds stored inside of type #3. Max 46. Leave -1 for default loadout",
            "property": "rhs_ammoslot_3",
            "control": "Edit",
            "expression": "if(_value >= 0)then{ [_this,_value,'%s',46,['rhs_ammoslot_1','rhs_ammoslot_2','rhs_ammoslot_3','rhs_ammoslot_4','rhs_ammoslot_5']] spawn rhs_fnc_Eden_DefineLoadout};",
            "defaultvalue": "-1",
            "validate": "NUMBER",
            "typename": "NUMBER"
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|Attributes|rhs_ammoslot_4_type [Indent level: 2],
        "rhs_ammoslot_4_type": {
            "displayname": "Ammo slot #4 type",
            "tooltip": "Define type of shell for #4 slot [Laser guided rounds]",
            "property": "rhs_ammoslot_4_type",
            # Class: CfgVehicles|rhsusf_m109tank_base|Attributes|rhs_ammoslot_4_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhsusf_m109tank_base|Attributes|rhs_ammoslot_4_type|values|rhs_mag_155mm_m712_2 [Indent level: 4]
                "rhs_mag_155mm_m712_2": {
                    "name": "M712 LG round",
                    "value": "rhs_mag_155mm_m712_2",
                    "defaultvalue": "rhs_mag_155mm_m712_2"
                }
            },
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": 0,
            "typename": "STRING"
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|Attributes|rhs_ammoslot_4 [Indent level: 2],
        "rhs_ammoslot_4": {
            "displayname": "Ammo slot #4 count",
            "tooltip": "Define number of rounds stored inside of type #4. Max 46. Leave -1 for default loadout",
            "property": "rhs_ammoslot_4",
            "control": "Edit",
            "expression": "if(_value >= 0)then{ [_this,_value,'%s',46,['rhs_ammoslot_1','rhs_ammoslot_2','rhs_ammoslot_3','rhs_ammoslot_4','rhs_ammoslot_5']] spawn rhs_fnc_Eden_DefineLoadout};",
            "defaultvalue": "-1",
            "validate": "NUMBER",
            "typename": "NUMBER"
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|Attributes|rhs_ammoslot_5_type [Indent level: 2],
        "rhs_ammoslot_5_type": {
            "displayname": "Ammo slot #5 type",
            "tooltip": "Define type of shell for #5 slot [Special rounds]",
            "property": "rhs_ammoslot_5_type",
            # Class: CfgVehicles|rhsusf_m109tank_base|Attributes|rhs_ammoslot_5_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhsusf_m109tank_base|Attributes|rhs_ammoslot_5_type|values|rhs_mag_155mm_raams_1 [Indent level: 4]
                "rhs_mag_155mm_raams_1": {
                    "name": "RAAMS AT mine round",
                    "value": "rhs_mag_155mm_raams_1",
                    "defaultvalue": "rhs_mag_155mm_raams_1"
                },
                # Class: CfgVehicles|rhsusf_m109tank_base|Attributes|rhs_ammoslot_5_type|values|rhs_mag_155mm_m731_1 [Indent level: 4],
                "rhs_mag_155mm_m731_1": {
                    "name": "M731 AP mine round",
                    "value": "rhs_mag_155mm_m731_1",
                    "defaultvalue": "rhs_mag_155mm_m731_1"
                }
            },
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": 0,
            "typename": "STRING"
        },
        # Class: CfgVehicles|rhsusf_m109tank_base|Attributes|rhs_ammoslot_5 [Indent level: 2],
        "rhs_ammoslot_5": {
            "displayname": "Ammo slot #5 count",
            "tooltip": "Define number of rounds stored inside of type #5. Max 40. Leave -1 for default loadout",
            "property": "rhs_ammoslot_5",
            "control": "Edit",
            "expression": "if(_value >= 0)then{ [_this,_value,'%s',46,['rhs_ammoslot_1','rhs_ammoslot_2','rhs_ammoslot_3','rhs_ammoslot_4','rhs_ammoslot_5']] spawn rhs_fnc_Eden_DefineLoadout};",
            "defaultvalue": "-1",
            "validate": "NUMBER",
            "typename": "NUMBER"
        }
    },
    # Class: CfgVehicles|rhsusf_m109tank_base|EventHandlers [Indent level: 1],
    "eventhandlers": {
        # Class: CfgVehicles|rhsusf_m109tank_base|EventHandlers|RHSUSF_EventHandlers [Indent level: 2]
        "rhsusf_eventhandlers": {
            "engine": "[_this select 0,_this select 1,2] call rhs_fnc_engineStartupDelay"
        },
        "init": "",
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');",
        # Class: DefaultEventHandlers|RHS_DefaultEventhandlers [Indent level: 0],
        "rhs_defaulteventhandlers": {
            "hitpart": "_this call rhs_fnc_hitPart"
        }
    },
    "features": "Randomization: No						<br />Camo selections: 3 - hull, main turret, RCWS turret						<br />Script door sources: None						<br />Script animations: None						<br />Executed scripts: None						<br />Firing from vehicles: No						<br />Slingload: No						<br />Cargo proxy indexes: None",
    "author": "Bohemia Interactive",
    "mapsize": 11.37,
    "_generalmacro": "MBT_01_arty_base_F",
    "weaponsgroup1": 2,
    "weaponsgroup2": "1 + 		4",
    "weaponsgroup3": "8 + 	16 + 	32",
    "weaponsgroup4": "64 + 		128",
    # Class: CfgVehicles|MBT_01_arty_base_F|Library [Indent level: 1],
    "library": {
        "libtextdesc": "Based on the licensed version of an Israeli tank chassis, The Scorcher M4 is a 155 mm self-propelled artillery at the end of its lifetime cycle. It has modules allowing indirect fire, advanced artillery computer and is able to fire guided cannon ammunition. The rear of the tank was changed from a passenger transport space to ammunition storage. Scorcher is also equipped with a Remotely Controlled Weapon Systems turret fitted with 12.7 mm HMG and 40 mm GMG."
    },
    "forcehidedriver": 0,
    "transportsoldier": 0,
    # Class: CfgVehicles|MBT_01_arty_base_F|MFD [Indent level: 1],
    "mfd": {
        # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_AmmoType [Indent level: 2]
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
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_AmmoType|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_AmmoType|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_AmmoType|Draw|Gunner_AmmoType [Indent level: 4],
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
        # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_Heading [Indent level: 2],
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
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_Heading|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_Heading|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_Heading|Draw|Heading [Indent level: 4],
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
        },
        # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Com_AmmoType [Indent level: 2],
        "mfd_com_ammotype": {
            "topleft": "MFD_9_TL",
            "topright": "MFD_9_TR",
            "bottomleft": "MFD_9_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "turret": [0],
            "enableparallax": 0,
            "font": "LCD14",
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Com_AmmoType|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Com_AmmoType|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Com_AmmoType|Draw|Gunner_AmmoType [Indent level: 4],
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
        # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Com_Heading [Indent level: 2],
        "mfd_com_heading": {
            "topleft": "MFD_2_TL",
            "topright": "MFD_2_TR",
            "bottomleft": "MFD_2_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [1,1,1],
            "alpha": 0.5,
            "enableparallax": 0,
            "font": "LCD14",
            "turret": [0],
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Com_Heading|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Com_Heading|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Com_Heading|Draw|Heading [Indent level: 4],
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
        },
        # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Driver_Heading [Indent level: 2],
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
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Driver_Heading|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Driver_Heading|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Driver_Heading|Draw [Indent level: 3],
            "draw": {
                "color": [0.61,0.62,0],
                "alpha": 1,
                "condition": "on",
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Driver_Heading|Draw|Driver_Heading [Indent level: 4],
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
        # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Driver_Speed [Indent level: 2],
        "mfd_driver_speed": {
            "topleft": "MFD_6_TL",
            "topright": "MFD_6_TR",
            "bottomleft": "MFD_6_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "enableparallax": 0,
            "font": "LCD14",
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Driver_Speed|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Driver_Speed|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Driver_Speed|Draw [Indent level: 3],
            "draw": {
                "color": [0.61,0.62,0],
                "alpha": 1,
                "condition": "on",
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Driver_Speed|Draw|Driver_Speed [Indent level: 4],
                "driver_speed": {
                    "type": "text",
                    "source": "speed",
                    "sourcescale": 3.6,
                    "sourcelength": 2,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.5,0],1],
                    "right": [[1,0],1],
                    "down": [[0.5,0.81],1]
                }
            }
        },
        # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Driver_Heading_text [Indent level: 2],
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
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Driver_Heading_text|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Driver_Heading_text|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Driver_Heading_text|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Driver_Heading_text|Draw|Driver_Heading [Indent level: 4],
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
        # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Driver_Heading_second [Indent level: 2],
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
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Driver_Heading_second|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Driver_Heading_second|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Driver_Heading_second|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Driver_Heading_second|Draw|Driver_Heading [Indent level: 4],
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
        # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_Ready_To_Fire [Indent level: 2],
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
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_Ready_To_Fire|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_Ready_To_Fire|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_Ready_To_Fire|Draw [Indent level: 3],
            "draw": {
                "color": [0,0,0],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_Ready_To_Fire|Draw|Top_text [Indent level: 4],
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
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_Ready_To_Fire|Draw|Bottom_text [Indent level: 4],
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
        # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_Display [Indent level: 2],
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
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_Display|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_Display|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_Display|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_Display|Draw|Main_armament [Indent level: 4],
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
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_Display|Draw|Machinegun [Indent level: 4],
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
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_Display|Draw|Main_armament_ammo_type [Indent level: 4],
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
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_Display|Draw|Lased_distance_elevation [Indent level: 4],
                "lased_distance_elevation": {
                    "type": "text",
                    "source": "static",
                    "text": "LASED DIST",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshrate": 0.1,
                    "pos": [[0.015,0.84],1],
                    "right": [[0.067,0.84],1],
                    "down": [[0.015,0.918],1]
                },
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_Display|Draw|Azimut [Indent level: 4],
                "azimut": {
                    "type": "text",
                    "source": "static",
                    "text": "AZIMUTH",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshrate": 0.1,
                    "pos": [[0.015,0.915],1],
                    "right": [[0.075,0.915],1],
                    "down": [[0.015,0.993],1]
                },
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_Display|Draw|Damage [Indent level: 4],
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
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_Display|Draw|Heading [Indent level: 4],
                "heading": {
                    "type": "text",
                    "source": "[x]turretworld",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "sourceoffset": 180,
                    "scale": 0.2,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.34,0.915],1],
                    "right": [[0.4,0.915],1],
                    "down": [[0.34,0.993],1]
                },
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_Display|Draw|Lased_Range [Indent level: 4],
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
        # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_Main_Armament_Ammo_Type [Indent level: 2],
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
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_Main_Armament_Ammo_Type|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_Main_Armament_Ammo_Type|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_Main_Armament_Ammo_Type|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_Main_Armament_Ammo_Type|Draw|Gunner_AmmoType [Indent level: 4],
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
        # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_Coax_Ammo [Indent level: 2],
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
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_Coax_Ammo|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_Coax_Ammo|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_Coax_Ammo|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_Coax_Ammo|Draw|Gunner_Text_1 [Indent level: 4],
                "gunner_text_1": {
                    "type": "text",
                    "source": "ammo",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "sourceindex": 1,
                    "align": "left",
                    "refreshrate": 0.1,
                    "pos": [[0.37,0.31],1],
                    "right": [[0.43,0.31],1],
                    "down": [[0.37,0.388],1]
                }
            }
        },
        # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament [Indent level: 2],
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
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|Draw|Main_Armament_Ammo_Type_1 [Indent level: 4],
                "main_armament_ammo_type_1": {
                    "type": "text",
                    "source": "static",
                    "text": "HE",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshrate": 0.1,
                    "pos": [[0.015,0.065],1],
                    "right": [[0.06,0.065],1],
                    "down": [[0.015,0.145],1]
                },
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|Draw|Gunner_Text_1 [Indent level: 4],
                "gunner_text_1": {
                    "type": "text",
                    "source": "ammo",
                    "sourcescale": 1,
                    "sourcelength": 2,
                    "sourceindex": 1000,
                    "scale": 1,
                    "align": "left",
                    "refreshrate": 0.1,
                    "pos": [[0.195,0.065],1],
                    "right": [[0.24,0.065],1],
                    "down": [[0.195,0.145],1]
                },
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|Draw|Main_Armament_Ammo_Type_2 [Indent level: 4],
                "main_armament_ammo_type_2": {
                    "type": "text",
                    "source": "static",
                    "text": "GUIDED",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshrate": 0.1,
                    "pos": [[0.015,0.12],1],
                    "right": [[0.06,0.12],1],
                    "down": [[0.015,0.2],1]
                },
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|Draw|Gunner_Text_2 [Indent level: 4],
                "gunner_text_2": {
                    "type": "text",
                    "source": "ammo",
                    "sourcescale": 1,
                    "sourcelength": 2,
                    "sourceindex": 1001,
                    "scale": 1,
                    "align": "left",
                    "refreshrate": 0.1,
                    "pos": [[0.195,0.12],1],
                    "right": [[0.24,0.12],1],
                    "down": [[0.195,0.2],1]
                },
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|Draw|Main_Armament_Ammo_Type_3 [Indent level: 4],
                "main_armament_ammo_type_3": {
                    "type": "text",
                    "source": "static",
                    "text": "MINE",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshrate": 0.1,
                    "pos": [[0.015,0.175],1],
                    "right": [[0.06,0.175],1],
                    "down": [[0.015,0.255],1]
                },
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|Draw|Gunner_Text_3 [Indent level: 4],
                "gunner_text_3": {
                    "type": "text",
                    "source": "ammo",
                    "sourcescale": 1,
                    "sourcelength": 2,
                    "sourceindex": 1002,
                    "scale": 1,
                    "align": "left",
                    "refreshrate": 0.1,
                    "pos": [[0.195,0.175],1],
                    "right": [[0.24,0.175],1],
                    "down": [[0.195,0.255],1]
                },
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|Draw|Main_Armament_Ammo_Type_4 [Indent level: 4],
                "main_armament_ammo_type_4": {
                    "type": "text",
                    "source": "static",
                    "text": "CLUSTER",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshrate": 0.1,
                    "pos": [[0.015,0.23],1],
                    "right": [[0.06,0.23],1],
                    "down": [[0.015,0.31],1]
                },
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|Draw|Gunner_Text_4 [Indent level: 4],
                "gunner_text_4": {
                    "type": "text",
                    "source": "ammo",
                    "sourcescale": 1,
                    "sourcelength": 2,
                    "sourceindex": 1003,
                    "scale": 1,
                    "align": "left",
                    "refreshrate": 0.1,
                    "pos": [[0.195,0.23],1],
                    "right": [[0.24,0.23],1],
                    "down": [[0.195,0.31],1]
                },
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|Draw|Main_Armament_Ammo_Type_5 [Indent level: 4],
                "main_armament_ammo_type_5": {
                    "type": "text",
                    "source": "static",
                    "text": "SMOKE",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshrate": 0.1,
                    "pos": [[0.215,0.065],1],
                    "right": [[0.26,0.065],1],
                    "down": [[0.215,0.145],1]
                },
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|Draw|Gunner_Text_5 [Indent level: 4],
                "gunner_text_5": {
                    "type": "text",
                    "source": "ammo",
                    "sourcescale": 1,
                    "sourcelength": 2,
                    "sourceindex": 1004,
                    "scale": 1,
                    "align": "left",
                    "refreshrate": 0.1,
                    "pos": [[0.395,0.065],1],
                    "right": [[0.44,0.065],1],
                    "down": [[0.395,0.145],1]
                },
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|Draw|Main_Armament_Ammo_Type_6 [Indent level: 4],
                "main_armament_ammo_type_6": {
                    "type": "text",
                    "source": "static",
                    "text": "LASER",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshrate": 0.1,
                    "pos": [[0.215,0.12],1],
                    "right": [[0.26,0.12],1],
                    "down": [[0.215,0.2],1]
                },
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|Draw|Gunner_Text_6 [Indent level: 4],
                "gunner_text_6": {
                    "type": "text",
                    "source": "ammo",
                    "sourcescale": 1,
                    "sourcelength": 2,
                    "sourceindex": 1005,
                    "scale": 1,
                    "align": "left",
                    "refreshrate": 0.1,
                    "pos": [[0.395,0.12],1],
                    "right": [[0.44,0.12],1],
                    "down": [[0.395,0.2],1]
                },
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|Draw|Main_Armament_Ammo_Type_7 [Indent level: 4],
                "main_armament_ammo_type_7": {
                    "type": "text",
                    "source": "static",
                    "text": "AT MINE",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshrate": 0.1,
                    "pos": [[0.215,0.175],1],
                    "right": [[0.26,0.175],1],
                    "down": [[0.215,0.255],1]
                },
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|Draw|Gunner_Text_7 [Indent level: 4],
                "gunner_text_7": {
                    "type": "text",
                    "source": "ammo",
                    "sourcescale": 1,
                    "sourcelength": 2,
                    "sourceindex": 1006,
                    "scale": 1,
                    "align": "left",
                    "refreshrate": 0.1,
                    "pos": [[0.395,0.175],1],
                    "right": [[0.44,0.175],1],
                    "down": [[0.395,0.255],1]
                }
            }
        },
        # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_Heading1 [Indent level: 2],
        "mfd_gunner_heading1": {
            "topleft": "mfd_gun_dir_TL",
            "topright": "mfd_gun_dir_TR",
            "bottomleft": "mfd_gun_dir_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "enableparallax": 0,
            "turret": [0],
            "font": "LCD14",
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_Heading1|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_Heading1|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_Heading1|Draw [Indent level: 3],
            "draw": {
                "color": [0.61,0.62,0],
                "alpha": 1,
                "condition": "on",
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_Heading1|Draw|Gunner_Heading [Indent level: 4],
                "gunner_heading": {
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
        # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_Range [Indent level: 2],
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
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_Range|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_Range|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Gunner_Range|Draw|Gunner_Range [Indent level: 4],
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
        # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_Display_Damage [Indent level: 2],
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
            "font": "PuristaBold",
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_Display_Damage|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_Display_Damage|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_Display_Damage|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_Display_Damage|Draw|Damage_Hull [Indent level: 4],
                "damage_hull": {
                    "type": "text",
                    "source": "static",
                    "text": "HULL",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": [[0.04,0.18],1],
                    "right": [[0.065,0.18],1],
                    "down": [[0.04,0.44],1]
                },
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_Display_Damage|Draw|Damage_Engine [Indent level: 4],
                "damage_engine": {
                    "type": "text",
                    "source": "static",
                    "text": "ENG",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": [[0.11,0.18],1],
                    "right": [[0.135,0.18],1],
                    "down": [[0.11,0.44],1]
                },
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_Display_Damage|Draw|Damage_Fuel [Indent level: 4],
                "damage_fuel": {
                    "type": "text",
                    "source": "static",
                    "text": "FUEL",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": [[0.178,0.18],1],
                    "right": [[0.203,0.18],1],
                    "down": [[0.178,0.44],1]
                },
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_Display_Damage|Draw|Damage_Wheels [Indent level: 4],
                "damage_wheels": {
                    "type": "text",
                    "source": "static",
                    "text": "TRKS",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": [[0.04,0.55],1],
                    "right": [[0.065,0.55],1],
                    "down": [[0.04,0.81],1]
                },
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_Display_Damage|Draw|Damage_Gun [Indent level: 4],
                "damage_gun": {
                    "type": "text",
                    "source": "static",
                    "text": "GUN",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": [[0.11,0.55],1],
                    "right": [[0.135,0.55],1],
                    "down": [[0.11,0.81],1]
                },
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_Display_Damage|Draw|Damage_Turret [Indent level: 4],
                "damage_turret": {
                    "type": "text",
                    "source": "static",
                    "text": "TRT",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": [[0.178,0.55],1],
                    "right": [[0.203,0.55],1],
                    "down": [[0.178,0.81],1]
                }
            }
        },
        # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_Display [Indent level: 2],
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
            "font": "PuristaBold",
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_Display|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_Display|Bones [Indent level: 3],
            "bones": {
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_Display|Bones|FuelScale [Indent level: 4]
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
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_Display|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_Display|Draw|Main_Gun [Indent level: 4],
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
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_Display|Draw|Main_Gun_Ammo_count [Indent level: 4],
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
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_Display|Draw|Main_Gun_Ammo_Type_text [Indent level: 4],
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
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_Display|Draw|Main_Gun_Ammo_Type [Indent level: 4],
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
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_Display|Draw|Coax [Indent level: 4],
                "coax": {
                    "type": "text",
                    "source": "static",
                    "text": "COM GUN",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.498,0.18],1],
                    "right": [[0.523,0.18],1],
                    "down": [[0.498,0.44],1]
                },
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_Display|Draw|Azimuth [Indent level: 4],
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
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_Display|Draw|Smoke [Indent level: 4],
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
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_Display|Draw|Fuel_background_white [Indent level: 4],
                "fuel_background_white": {
                    "color": [0.2,0.2,0.2],
                    "alpha": 0.1,
                    "condition": "1",
                    # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_Display|Draw|Fuel_background_white|Background [Indent level: 5],
                    "background": {
                        "type": "polygon",
                        "points": [[[[0.787,0.7],1],[[0.877,0.7],1],[[0.877,0.9],1],[[0.787,0.9],1]]]
                    }
                },
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_Display|Draw|Fuel_background_green [Indent level: 4],
                "fuel_background_green": {
                    "color": [0,0.7,0],
                    "condition": "fuel>=0.5",
                    # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_Display|Draw|Fuel_background_green|Background [Indent level: 5],
                    "background": {
                        "type": "polygon",
                        "points": [[[[0.787,0.7],1],["FuelScale",[0.877,0.7],1],["FuelScale",[0.877,0.9],1],[[0.787,0.9],1]]]
                    }
                },
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_Display|Draw|Fuel_background_yellow [Indent level: 4],
                "fuel_background_yellow": {
                    "color": [0.9,0.7,0],
                    "condition": "fuel<0.5",
                    # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_Display|Draw|Fuel_background_yellow|Background [Indent level: 5],
                    "background": {
                        "type": "polygon",
                        "points": [[[[0.787,0.7],1],["FuelScale",[0.877,0.7],1],["FuelScale",[0.877,0.9],1],[[0.787,0.9],1]]]
                    }
                },
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_Display|Draw|Fuel_background_red [Indent level: 4],
                "fuel_background_red": {
                    "color": [0.7,0,0],
                    "condition": "fuel<0.3",
                    # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_Display|Draw|Fuel_background_red|Background [Indent level: 5],
                    "background": {
                        "type": "polygon",
                        "points": [[[[0.787,0.7],1],["FuelScale",[0.877,0.7],1],["FuelScale",[0.877,0.9],1],[[0.787,0.9],1]]]
                    }
                },
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_Display|Draw|Fuel [Indent level: 4],
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
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_Display|Draw|Fuel_number [Indent level: 4],
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
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_Display|Draw|Fuel_percent_sign [Indent level: 4],
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
        # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_OnScreen [Indent level: 2],
        "mfd_commander_onscreen": {
            "topleft": "PIP_COM_TL",
            "topright": "PIP_COM_TR",
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
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_OnScreen|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_OnScreen|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_OnScreen|Draw [Indent level: 3],
            "draw": {
                "color": [0.15,1,0.05],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_OnScreen|Draw|Azimuth_number [Indent level: 4],
                "azimuth_number": {
                    "type": "text",
                    "source": "[x]turretworld",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.5,0.235],1],
                    "right": [[0.525,0.235],1],
                    "down": [[0.5,0.272],1]
                },
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_OnScreen|Draw|Elevation_Text [Indent level: 4],
                "elevation_text": {
                    "type": "text",
                    "source": "static",
                    "text": "E: ",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.23,0.3],1],
                    "right": [[0.255,0.3],1],
                    "down": [[0.23,0.337],1]
                },
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_OnScreen|Draw|Elevation_Number [Indent level: 4],
                "elevation_number": {
                    "type": "text",
                    "source": "[y]turretworld",
                    "sourcescale": 1,
                    "sourcelength": 4,
                    "sourceprecision": 1,
                    "refreshrate": 0,
                    "align": "center",
                    "scale": 1,
                    "pos": [[0.26,0.3],1],
                    "right": [[0.285,0.3],1],
                    "down": [[0.26,0.337],1]
                },
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_OnScreen|Draw|Lased_Range [Indent level: 4],
                "lased_range": {
                    "type": "text",
                    "source": "laserDist",
                    "sourcescale": 1,
                    "sourcelength": 4,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.5,0.65],1],
                    "right": [[0.525,0.65],1],
                    "down": [[0.5,0.687],1]
                },
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_OnScreen|Draw|VisionMode_Text [Indent level: 4],
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
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_OnScreen|Draw|VisionMode_String [Indent level: 4],
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
        # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_Display_MainTurret [Indent level: 2],
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
            "font": "PuristaBold",
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_Display_MainTurret|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_Display_MainTurret|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_Display_MainTurret|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_Display_MainTurret|Draw|Smoke_ammo [Indent level: 4],
                "smoke_ammo": {
                    "type": "text",
                    "source": "ammo",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "sourceindex": 2,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.72,0.55],1],
                    "right": [[0.745,0.55],1],
                    "down": [[0.72,0.81],1]
                },
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_Display_MainTurret|Draw|Coax_Ammo_count [Indent level: 4],
                "coax_ammo_count": {
                    "type": "text",
                    "source": "ammo",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.498,0.55],1],
                    "right": [[0.523,0.55],1],
                    "down": [[0.498,0.81],1]
                },
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Commander_Display_MainTurret|Draw|Azimuth_number [Indent level: 4],
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
                }
            }
        },
        # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Com_Range [Indent level: 2],
        "mfd_com_range": {
            "topleft": "MFD_10_TL",
            "topright": "MFD_10_TR",
            "bottomleft": "MFD_10_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "enableparallax": 0,
            "turret": [0],
            "font": "LCD14",
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Com_Range|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Com_Range|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|MBT_01_arty_base_F|MFD|MFD_Com_Range|Draw|Gunner_Range [Indent level: 4],
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
        }
    },
    # Class: CfgVehicles|MBT_01_arty_base_F|compartmentsLights [Indent level: 1],
    "compartmentslights": {
        # Class: CfgVehicles|MBT_01_arty_base_F|compartmentsLights|Comp1 [Indent level: 2]
        "comp1": {
            # Class: CfgVehicles|MBT_01_arty_base_F|compartmentsLights|Comp1|Light1 [Indent level: 3]
            "light1": {
                "color": [10,15,15],
                "ambient": [0,0,0],
                "intensity": 2,
                "size": 0,
                "useflare": 0,
                "flaresize": 0,
                "flaremaxdistance": 0,
                "daylight": 0,
                "blinking": 0,
                # Class: CfgVehicles|MBT_01_arty_base_F|compartmentsLights|Comp1|Light1|Attenuation [Indent level: 4],
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
            # Class: CfgVehicles|MBT_01_arty_base_F|compartmentsLights|Comp1|Light2 [Indent level: 3],
            "light2": {
                "point": "light_interior2",
                "color": [10,15,15],
                "ambient": [0,0,0],
                "intensity": 2,
                "size": 0,
                "useflare": 0,
                "flaresize": 0,
                "flaremaxdistance": 0,
                "daylight": 0,
                "blinking": 0,
                # Class: CfgVehicles|MBT_01_arty_base_F|compartmentsLights|Comp1|Light1|Attenuation [Indent level: 4],
                "attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardlimitstart": 0.15,
                    "hardlimitend": 1.15
                }
            },
            # Class: CfgVehicles|MBT_01_arty_base_F|compartmentsLights|Comp1|Light3 [Indent level: 3],
            "light3": {
                "point": "light_interior3",
                "color": [10,15,15],
                "ambient": [0,0,0],
                "intensity": 0.85,
                "size": 0,
                "useflare": 0,
                "flaresize": 0,
                "flaremaxdistance": 0,
                "daylight": 0,
                "blinking": 0,
                # Class: CfgVehicles|MBT_01_arty_base_F|compartmentsLights|Comp1|Light1|Attenuation [Indent level: 4],
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
    "artilleryscanner": 1,
    "selectionfireanim": "",
    "soundgetin": ["A3|Sounds_F_EPB|Tracked|noises|get_in_out",0.562341,1],
    "soundgetout": ["A3|Sounds_F_EPB|Tracked|noises|get_in_out",0.562341,1,20],
    "soundturnin": ["A3|Sounds_F|vehicles|noises|Turn_in_out",1.77828,1,20],
    "soundturnout": ["A3|Sounds_F|vehicles|noises|Turn_in_out",1.77828,1,20],
    "soundturnininternal": ["A3|Sounds_F|vehicles|noises|Turn_in_out",1.77828,1,20],
    "soundturnoutinternal": ["A3|Sounds_F|vehicles|noises|Turn_in_out",1.77828,1,20],
    "sounddammage": ["",0.562341,1],
    "soundengineonint": ["A3|Sounds_F|vehicles2|armor|MBT_01|MBT_01_Engine_Int_Start",0.562341,1],
    "soundengineoffint": ["A3|Sounds_F|vehicles2|armor|MBT_01|MBT_01_Engine_Int_Stop",0.562341,1],
    "soundengineoffext": ["A3|Sounds_F|vehicles2|armor|MBT_01|MBT_01_Engine_Ext_Stop",6.30957,1,100],
    "soundengineonext": ["A3|Sounds_F|vehicles2|armor|MBT_01|MBT_01_Engine_Ext_Start",6.30957,1,100],
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
    # Class: CfgVehicles|MBT_01_base_F|Sounds [Indent level: 1],
    "sounds": {
        "soundsetsint": ["MBT_01_Engine_RPM0_INT_SoundSet","MBT_01_Engine_RPM1_INT_SoundSet","MBT_01_Engine_RPM2_INT_SoundSet","MBT_01_Engine_RPM3_INT_SoundSet","MBT_01_Engine_RPM4_INT_SoundSet","MBT_01_Engine_RPM5_INT_SoundSet","MBT_01_Engine_RPM6_INT_SoundSet","MBT_01_Engine_INT_Burst_SoundSet","MBT_01_Tracks_01_INT_SoundSet","MBT_01_Tracks_02_INT_SoundSet","MBT_01_Tracks_03_INT_SoundSet","MBT_01_Tracks_04_INT_SoundSet","MBT_01_Tracks_05_INT_SoundSet","MBT_01_Tracks_06_INT_SoundSet","MBT_01_Interior_Tone_Engine_Off_SoundSet","MBT_01_Interior_Tone_Engine_On_SoundSet","MBT_01_Rattling_INT_SoundSet","MBT_01_Rain_INT_SoundSet","MBT_01_Tracks_Brake_Hard_INT_SoundSet","MBT_01_Tracks_Brake_Soft_INT_SoundSet","MBT_01_Tracks_Turn_Hard_INT_SoundSet","MBT_01_Tracks_Turn_Soft_INT_SoundSet","MBT_01_Drive_Water_INT_SoundSet","MBT_01_Drive_Dirt_INT_SoundSet","","Tracks_Movement_Dirt_Int_01_SoundSet","Tracks_Surface_Soft_Int_SoundSet","Tracks_Surface_Sand_Int_SoundSet","Tracks_Surface_Squeaks_Soft_Int_SoundSet","Tracks_Surface_Squeaks_Hard_Int_SoundSet","Tanks_Material_Strain_Int_SoundSet","Tank_General_Collision_Int_SoundSet"],
        "soundsetsext": ["MBT_01_Engine_RPM0_EXT_SoundSet","MBT_01_Engine_RPM1_EXT_SoundSet","MBT_01_Engine_RPM2_EXT_SoundSet","MBT_01_Engine_RPM3_EXT_SoundSet","MBT_01_Engine_RPM4_EXT_SoundSet","MBT_01_Engine_RPM5_EXT_SoundSet","MBT_01_Engine_RPM6_EXT_SoundSet","MBT_01_Engine_EXT_Burst_SoundSet","MBT_01_Tracks_01_EXT_SoundSet","MBT_01_Tracks_02_EXT_SoundSet","MBT_01_Tracks_03_EXT_SoundSet","MBT_01_Tracks_04_EXT_SoundSet","MBT_01_Tracks_05_EXT_SoundSet","MBT_01_Tracks_06_EXT_SoundSet","MBT_01_Rain_EXT_SoundSet","MBT_01_Tracks_Brake_Hard_EXT_SoundSet","MBT_01_Tracks_Brake_Soft_EXT_SoundSet","MBT_01_Tracks_Turn_Hard_EXT_SoundSet","MBT_01_Tracks_Turn_Soft_EXT_SoundSet","MBT_01_Drive_Water_EXT_SoundSet","MBT_01_Drive_Dirt_EXT_SoundSet","","Tracks_Movement_Dirt_Ext_01_SoundSet","Tracks_Surface_Soft_Ext_SoundSet","Tracks_Surface_Sand_Ext_SoundSet","Tracks_Surface_Squeaks_Soft_Ext_SoundSet","Tracks_Surface_Squeaks_Hard_Ext_SoundSet","Tank_General_Collision_SoundShader"]
    },
    "brakeidlespeed": 0.1,
    "waterresistancecoef": 0.25,
    "scope": 0,
    "driverinfopanelcamerapos": "driverview_old",
    "driverlefthandanimname": "drivewheel",
    "driverrighthandanimname": "drivewheel",
    "driverleftleganimname": "pedal_brake",
    "driverrightleganimname": "pedal_thrust",
    "viewdrivershadowamb": 0.5,
    "viewdrivershadowdiff": 0.05,
    "getinaction": "GetInLow",
    "getoutaction": "GetOutLow",
    "cargogetinaction": ["GetInLow"],
    "cargogetoutaction": ["GetOutLow"],
    "cargoaction": ["passenger_flatground_leanleft","passenger_flatground_generic01","passenger_flatground_generic02","passenger_flatground_generic03","passenger_flatground_generic04","passenger_flatground_generic05"],
    "loddriverturnedin": 1100,
    "loddriverturnedout": 0,
    "loddriveropticsin": 1202,
    "viewdriverinexternal": 1,
    # Class: CfgVehicles|MBT_01_base_F|ViewPilot [Indent level: 1],
    "viewpilot": {
        "initanglex": -3,
        "initangley": 0,
        "initfov": 0.9,
        "minfov": 0.25,
        "maxfov": 1.25,
        "minanglex": -65,
        "maxanglex": 85,
        "minangley": -150,
        "maxangley": 150,
        "minmovex": 0,
        "maxmovex": 0,
        "minmovey": -0.075,
        "maxmovey": 0.075,
        "minmovez": -0.075,
        "maxmovez": 0.1,
        "speedzoommaxspeed": 1e+010,
        "speedzoommaxfov": 0
    },
    "crewexplosionprotection": 0.9999,
    "epeimpulsedamagecoef": 18,
    "waterppinvehicle": 0,
    "memorypointtaskmarker": "TaskMarker_1_pos",
    "hideweaponsdriver": 1,
    "hideweaponscargo": 1,
    "animationsourcehatch": "",
    "insidesoundcoef": 0.9,
    "threat": [0.8,1,0.3],
    "soundlocked": ["|A3|Sounds_F|weapons|Rockets|opfor_lock_1",1,1],
    "soundincommingmissile": ["|A3|Sounds_F|vehicles|air|noises|alarm_locked_by_missile_1",0.316228,1],
    "smokelaunchergrenadecount": 8,
    "smokelaunchervelocity": 14,
    "smokelauncheronturret": 1,
    "smokelauncherangle": 120,
    "animationlist": ["showCamonetCannon",0,"showCamonetPlates1",0,"showCamonetPlates2",0,"showCamonetTurret",0,"showCamonetHull",0],
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
    "irscanground": 2,
    "irscanrangemax": 0,
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
    "faction": "Default",
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
    "canusescanners": 1,
    "preferroads": 0,
    "unitinfotypelite": 0,
    "hideunitinfo": 0,
    "radartype": 0,
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
    "drivercompartments": "Compartment1",
    "cargocompartments": ["Compartment1"],
    "driveropticseffect": [],
    "canhidedriver": -1,
    "castdrivershadow": 0,
    "castcargoshadow": 0,
    "viewdrivershadow": 1,
    "ejectdeaddriver": 0,
    "ejectdeadcargo": 0,
    "crew": "Civilian",
    "hiddenselectionstextures": [],
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