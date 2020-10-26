rhs_t90a_tv = {
    "editorpreview": "rhsafrf|addons|rhs_editorPreviews|data|rhs_t90a_tv.paa",
    "displayname": "T-90A (obr. 2006g.)",
    "author": "Red Hammer Studios",
    "scope": 2,
    "model": "rhsafrf|addons|rhs_t72|rhs_t90a",
    "picture": "rhsafrf|addons|rhs_t72|icons|t90a_ca.paa",
    "normalspeedforwardcoef": 0.75,
    "slowspeedforwardcoef": 0.25,
    "fuelcapacity": 29.5,
    "rhs_fuelcapacity": 1200,
    "brakeidlespeed": 1.78,
    "maxspeed": 68,
    "torquecurve": [[0,0],[0.478261,0.853329],[0.521739,0.986803],[0.565217,1],[0.608696,1],[0.695652,0.980804],[0.869565,0.884823],[1.43478,0]],
    "enginemoi": 17,
    "enginepower": 736,
    "peaktorque": 3920,
    "minomega": 80,
    "maxomega": 240.86,
    "idlerpm": 800,
    "redrpm": 2300,
    "changegearomegaratios": [1,0.434783,0.434783,0,0.956522,0.434783,0.956522,0.782609,0.913043,0.782609,0.913043,0.782609,0.869565,0.73913,0.826087,0.695652,1,0.608696],
    # Class: CfgVehicles|rhs_t90a_tv|complexGearbox [Indent level: 1],
    "complexgearbox": {
        "gearboxratios": ["R1",-16.35,"N",0,"D1",8.173,"D2",4.4,"D3",3.485,"D4",2.787,"D5",2.027,"D6",1.467,"D7",1],
        "transmissionratios": ["High",9.05],
        "gearboxmode": "auto",
        "moveoffgear": 1,
        "drivestring": "D",
        "neutralstring": "N",
        "reversestring": "R",
        "transmissiondelay": 0.1
    },
    # Class: CfgVehicles|rhs_t90a_tv|Wheels [Indent level: 1],
    "wheels": {
        # Class: CfgVehicles|rhs_t90a_tv|Wheels|L2 [Indent level: 2]
        "l2": {
            "width": 0.504,
            "moi": 17.069,
            "sprungmass": -1,
            "dampingrate": 3143,
            "dampingrateinair": 3143,
            "side": "left",
            "susptraveldirection": [-0.125,-1,0],
            "bonename": "wheel_podkoloL1",
            "center": "wheel_1_2_axis",
            "boundary": "wheel_1_2_bound",
            "steering": 0,
            "mass": 193,
            "maxbraketorque": 20000,
            "springstrength": 484000,
            "springdamperrate": 11000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 1,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 72000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhs_t90a_tv|Wheels|L3 [Indent level: 2],
        "l3": {
            "bonename": "wheel_podkolol2",
            "center": "wheel_1_3_axis",
            "boundary": "wheel_1_3_bound",
            "width": 0.504,
            "moi": 17.069,
            "sprungmass": -1,
            "dampingrate": 3143,
            "dampingrateinair": 3143,
            "side": "left",
            "susptraveldirection": [-0.125,-1,0],
            "steering": 0,
            "mass": 193,
            "maxbraketorque": 20000,
            "springstrength": 484000,
            "springdamperrate": 11000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 1,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 72000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhs_t90a_tv|Wheels|L4 [Indent level: 2],
        "l4": {
            "bonename": "wheel_podkolol3",
            "center": "wheel_1_4_axis",
            "boundary": "wheel_1_4_bound",
            "width": 0.504,
            "moi": 17.069,
            "sprungmass": -1,
            "dampingrate": 3143,
            "dampingrateinair": 3143,
            "side": "left",
            "susptraveldirection": [-0.125,-1,0],
            "steering": 0,
            "mass": 193,
            "maxbraketorque": 20000,
            "springstrength": 484000,
            "springdamperrate": 11000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 1,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 72000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhs_t90a_tv|Wheels|L5 [Indent level: 2],
        "l5": {
            "bonename": "wheel_podkolol4",
            "center": "wheel_1_5_axis",
            "boundary": "wheel_1_5_bound",
            "width": 0.504,
            "moi": 17.069,
            "sprungmass": -1,
            "dampingrate": 3143,
            "dampingrateinair": 3143,
            "side": "left",
            "susptraveldirection": [-0.125,-1,0],
            "steering": 0,
            "mass": 193,
            "maxbraketorque": 20000,
            "springstrength": 484000,
            "springdamperrate": 11000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 1,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 72000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhs_t90a_tv|Wheels|L6 [Indent level: 2],
        "l6": {
            "bonename": "wheel_podkolol5",
            "center": "wheel_1_6_axis",
            "boundary": "wheel_1_6_bound",
            "width": 0.504,
            "moi": 17.069,
            "sprungmass": -1,
            "dampingrate": 3143,
            "dampingrateinair": 3143,
            "side": "left",
            "susptraveldirection": [-0.125,-1,0],
            "steering": 0,
            "mass": 193,
            "maxbraketorque": 20000,
            "springstrength": 484000,
            "springdamperrate": 11000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 1,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 72000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhs_t90a_tv|Wheels|L7 [Indent level: 2],
        "l7": {
            "bonename": "wheel_podkolol6",
            "center": "wheel_1_7_axis",
            "boundary": "wheel_1_7_bound",
            "width": 0.504,
            "moi": 17.069,
            "sprungmass": -1,
            "dampingrate": 3143,
            "dampingrateinair": 3143,
            "side": "left",
            "susptraveldirection": [-0.125,-1,0],
            "steering": 0,
            "mass": 193,
            "maxbraketorque": 20000,
            "springstrength": 484000,
            "springdamperrate": 11000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 1,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 72000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhs_t90a_tv|Wheels|L9 [Indent level: 2],
        "l9": {
            "bonename": "wheel_podkolol9",
            "center": "wheel_1_9_axis",
            "boundary": "wheel_1_9_bound",
            "maxdroop": 0,
            "maxcompression": 0,
            "width": 0.504,
            "moi": 17.069,
            "sprungmass": -1,
            "dampingrate": 3143,
            "dampingrateinair": 3143,
            "side": "left",
            "susptraveldirection": [-0.125,-1,0],
            "steering": 0,
            "mass": 193,
            "maxbraketorque": 20000,
            "springstrength": 484000,
            "springdamperrate": 11000,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 1,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 72000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhs_t90a_tv|Wheels|L1 [Indent level: 2],
        "l1": {
            "bonename": "",
            "center": "wheel_1_1_axis",
            "boundary": "wheel_1_1_bound",
            "maxdroop": 0,
            "maxcompression": 0,
            "width": 0.504,
            "moi": 17.069,
            "sprungmass": -1,
            "dampingrate": 3143,
            "dampingrateinair": 3143,
            "side": "left",
            "susptraveldirection": [-0.125,-1,0],
            "steering": 0,
            "mass": 193,
            "maxbraketorque": 20000,
            "springstrength": 484000,
            "springdamperrate": 11000,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 1,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 72000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhs_t90a_tv|Wheels|R2 [Indent level: 2],
        "r2": {
            "bonename": "wheel_podkolop1",
            "center": "wheel_2_2_axis",
            "boundary": "wheel_2_2_bound",
            "side": "right",
            "width": 0.504,
            "moi": 17.069,
            "sprungmass": -1,
            "dampingrate": 3143,
            "dampingrateinair": 3143,
            "susptraveldirection": [-0.125,-1,0],
            "steering": 0,
            "mass": 193,
            "maxbraketorque": 20000,
            "springstrength": 484000,
            "springdamperrate": 11000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 1,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 72000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhs_t90a_tv|Wheels|R3 [Indent level: 2],
        "r3": {
            "bonename": "wheel_podkolop2",
            "center": "wheel_2_3_axis",
            "boundary": "wheel_2_3_bound",
            "side": "right",
            "width": 0.504,
            "moi": 17.069,
            "sprungmass": -1,
            "dampingrate": 3143,
            "dampingrateinair": 3143,
            "susptraveldirection": [-0.125,-1,0],
            "steering": 0,
            "mass": 193,
            "maxbraketorque": 20000,
            "springstrength": 484000,
            "springdamperrate": 11000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 1,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 72000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhs_t90a_tv|Wheels|R4 [Indent level: 2],
        "r4": {
            "bonename": "wheel_podkolop3",
            "center": "wheel_2_4_axis",
            "boundary": "wheel_2_4_bound",
            "side": "right",
            "width": 0.504,
            "moi": 17.069,
            "sprungmass": -1,
            "dampingrate": 3143,
            "dampingrateinair": 3143,
            "susptraveldirection": [-0.125,-1,0],
            "steering": 0,
            "mass": 193,
            "maxbraketorque": 20000,
            "springstrength": 484000,
            "springdamperrate": 11000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 1,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 72000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhs_t90a_tv|Wheels|R5 [Indent level: 2],
        "r5": {
            "bonename": "wheel_podkolop4",
            "center": "wheel_2_5_axis",
            "boundary": "wheel_2_5_bound",
            "side": "right",
            "width": 0.504,
            "moi": 17.069,
            "sprungmass": -1,
            "dampingrate": 3143,
            "dampingrateinair": 3143,
            "susptraveldirection": [-0.125,-1,0],
            "steering": 0,
            "mass": 193,
            "maxbraketorque": 20000,
            "springstrength": 484000,
            "springdamperrate": 11000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 1,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 72000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhs_t90a_tv|Wheels|R6 [Indent level: 2],
        "r6": {
            "bonename": "wheel_podkolop5",
            "center": "wheel_2_6_axis",
            "boundary": "wheel_2_6_bound",
            "side": "right",
            "width": 0.504,
            "moi": 17.069,
            "sprungmass": -1,
            "dampingrate": 3143,
            "dampingrateinair": 3143,
            "susptraveldirection": [-0.125,-1,0],
            "steering": 0,
            "mass": 193,
            "maxbraketorque": 20000,
            "springstrength": 484000,
            "springdamperrate": 11000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 1,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 72000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhs_t90a_tv|Wheels|R7 [Indent level: 2],
        "r7": {
            "bonename": "wheel_podkolop6",
            "center": "wheel_2_7_axis",
            "boundary": "wheel_2_7_bound",
            "side": "right",
            "width": 0.504,
            "moi": 17.069,
            "sprungmass": -1,
            "dampingrate": 3143,
            "dampingrateinair": 3143,
            "susptraveldirection": [-0.125,-1,0],
            "steering": 0,
            "mass": 193,
            "maxbraketorque": 20000,
            "springstrength": 484000,
            "springdamperrate": 11000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 1,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 72000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhs_t90a_tv|Wheels|R9 [Indent level: 2],
        "r9": {
            "bonename": "wheel_podkolop9",
            "center": "wheel_2_9_axis",
            "boundary": "wheel_2_9_bound",
            "maxdroop": 0,
            "maxcompression": 0,
            "side": "right",
            "width": 0.504,
            "moi": 17.069,
            "sprungmass": -1,
            "dampingrate": 3143,
            "dampingrateinair": 3143,
            "susptraveldirection": [-0.125,-1,0],
            "steering": 0,
            "mass": 193,
            "maxbraketorque": 20000,
            "springstrength": 484000,
            "springdamperrate": 11000,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 1,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 72000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhs_t90a_tv|Wheels|R1 [Indent level: 2],
        "r1": {
            "bonename": "",
            "center": "wheel_2_1_axis",
            "boundary": "wheel_2_1_bound",
            "maxdroop": 0,
            "maxcompression": 0,
            "side": "right",
            "width": 0.504,
            "moi": 17.069,
            "sprungmass": -1,
            "dampingrate": 3143,
            "dampingrateinair": 3143,
            "susptraveldirection": [-0.125,-1,0],
            "steering": 0,
            "mass": 193,
            "maxbraketorque": 20000,
            "springstrength": 484000,
            "springdamperrate": 11000,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 1,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 72000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        }
    },
    "hiddenselectionstextures": ["rhsafrf|addons|rhs_t72|data|rhs_t72b3_01_co.paa","rhsafrf|addons|rhs_t72|data|rhs_t72b3_02_co.paa","rhsafrf|addons|rhs_t72|data|rhs_t72b_03_co.paa","rhsafrf|addons|rhs_t72|data|rhs_t72b_04_co.paa","rhsafrf|addons|rhs_t72|data|rhs_t72b_05_co.paa","rhsafrf|addons|rhs_t72|data|rhs_t90parts_co.paa","rhsafrf|addons|rhs_t72|data|rhs_t90a_02_co.paa","","rhsafrf|addons|rhs_t72|data|rhs_dazzler_co.paa","rhsafrf|addons|rhs_t72|data|rhs_dazzler_co.paa","rhsafrf|addons|rhs_decals|Data|Labels|Misc|no_ca.paa"],
    # Class: CfgVehicles|rhs_t90a_tv|textureSources [Indent level: 1],
    "texturesources": {
        # Class: CfgVehicles|rhs_t90a_tv|textureSources|standard [Indent level: 2]
        "standard": {
            "textures": ["rhsafrf|addons|rhs_t72|data|rhs_t72b3_01_co.paa","rhsafrf|addons|rhs_t72|data|rhs_t72b3_02_co.paa","rhsafrf|addons|rhs_t72|data|rhs_t72b_03_co.paa","rhsafrf|addons|rhs_t72|data|rhs_t72b_04_co.paa","rhsafrf|addons|rhs_t72|data|rhs_t72b_05_co.paa","rhsafrf|addons|rhs_t72|data|rhs_t90parts_co.paa","rhsafrf|addons|rhs_t72|data|rhs_t90a_02_co.paa","","rhsafrf|addons|rhs_t72|data|rhs_dazzler_co.paa","rhsafrf|addons|rhs_t72|data|rhs_dazzler_co.paa"],
            "displayname": "Standard",
            "author": "Red Hammer Studios",
            "factions": []
        },
        # Class: CfgVehicles|rhs_t90a_tv|textureSources|rhs_Sand [Indent level: 2],
        "rhs_sand": {
            "textures": ["rhsafrf|addons|rhs_t72_camo|data|rhs_t72b3_01_sand_co.paa","rhsafrf|addons|rhs_t72_camo|data|rhs_t72b3_02_sand_co.paa","rhsafrf|addons|rhs_t72_camo|data|rhs_t72b_03_sand_co.paa","rhsafrf|addons|rhs_t72_camo|data|rhs_t72b_04_sand_co.paa","rhsafrf|addons|rhs_t72_camo|data|rhs_t72b_05_sand_co.paa","rhsafrf|addons|rhs_t72_camo|data|rhs_t90parts_sand_co.paa","rhsafrf|addons|rhs_t72_camo|data|rhs_t90a_02_sand_co.paa","","rhsafrf|addons|rhs_t72_camo|data|rhs_dazzler_sand_co.paa","rhsafrf|addons|rhs_t72_camo|data|rhs_dazzler_sand_co.paa"],
            "displayname": "Sand",
            "author": "Red Hammer Studios",
            "factions": []
        },
        # Class: CfgVehicles|rhs_t90_tv|textureSources|RHS_CDF [Indent level: 2],
        "rhs_cdf": {
            "scope": 0,
            "displayname": ""
        },
        # Class: CfgVehicles|rhs_t72bd_tv|textureSources|rhs_chdkz [Indent level: 2],
        "rhs_chdkz": {
            "displayname": "",
            "textures": ["rhsafrf|addons|rhs_t72_camo|data|rhs_t72b_01a_chdkz_co.paa","rhsafrf|addons|rhs_t72_camo|data|rhs_t72b_02a_chdkz_co.paa","rhsafrf|addons|rhs_t72|data|rhs_t72b_03_co.paa","rhsafrf|addons|rhs_t72|data|rhs_t72b_04_co.paa"],
            "author": "Red Hammer Studios",
            "factions": []
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|textureSources|r1 [Indent level: 2],
        "r1": {
            "displayname": "#1",
            "author": "Red Hammer Studios",
            "textures": ["#(argb,8,8,3)color(0.92,0.87,0.92,1)","#(argb,8,8,3)color(0.92,0.87,0.92,1)","#(argb,8,8,3)color(0.92,0.87,0.92,1)","#(argb,8,8,3)color(0.92,0.87,0.92,1)","#(argb,8,8,3)color(0.92,0.87,0.92,1)","#(argb,8,8,3)color(0.92,0.87,0.92,1)","#(argb,8,8,3)color(0.92,0.87,0.92,1)","#(argb,8,8,3)color(0.92,0.87,0.92,1)"],
            "factions": []
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|textureSources|r2 [Indent level: 2],
        "r2": {
            "displayname": "#2",
            "author": "Red Hammer Studios",
            "textures": ["#(argb,8,8,3)color(0.07,0.98,0,1)","#(argb,8,8,3)color(0.07,0.98,0,1)","#(argb,8,8,3)color(0.07,0.98,0,1)","#(argb,8,8,3)color(0.07,0.98,0,1)","#(argb,8,8,3)color(0.07,0.98,0,1)","#(argb,8,8,3)color(0.07,0.98,0,1)","#(argb,8,8,3)color(0.07,0.98,0,1)","#(argb,8,8,3)color(0.07,0.98,0,1)"],
            "factions": []
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|textureSources|r3 [Indent level: 2],
        "r3": {
            "displayname": "#3",
            "author": "Red Hammer Studios",
            "textures": ["#(argb,8,8,3)color(0,0.11,0.67,1)","#(argb,8,8,3)color(0,0.11,0.67,1)","#(argb,8,8,3)color(0,0.11,0.67,1)","#(argb,8,8,3)color(0,0.11,0.67,1)","#(argb,8,8,3)color(0,0.11,0.67,1)","#(argb,8,8,3)color(0,0.11,0.67,1)","#(argb,8,8,3)color(0,0.11,0.67,1)","#(argb,8,8,3)color(0,0.11,0.67,1)"],
            "factions": []
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|textureSources|r4 [Indent level: 2],
        "r4": {
            "displayname": "#4",
            "author": "Red Hammer Studios",
            "textures": ["#(argb,8,8,3)color(0.99,0.27,0.25,1)","#(argb,8,8,3)color(0.99,0.27,0.25,1)","#(argb,8,8,3)color(0.99,0.27,0.25,1)","#(argb,8,8,3)color(0.99,0.27,0.25,1)","#(argb,8,8,3)color(0.99,0.27,0.25,1)","#(argb,8,8,3)color(0.99,0.27,0.25,1)","#(argb,8,8,3)color(0.99,0.27,0.25,1)","#(argb,8,8,3)color(0.99,0.27,0.25,1)"],
            "factions": []
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|textureSources|r5 [Indent level: 2],
        "r5": {
            "displayname": "#5",
            "author": "Red Hammer Studios",
            "textures": ["#(argb,8,8,3)color(00.41,0.4,0,1)","#(argb,8,8,3)color(00.41,0.4,0,1)","#(argb,8,8,3)color(00.41,0.4,0,1)","#(argb,8,8,3)color(00.41,0.4,0,1)","#(argb,8,8,3)color(00.41,0.4,0,1)","#(argb,8,8,3)color(00.41,0.4,0,1)","#(argb,8,8,3)color(00.41,0.4,0,1)","#(argb,8,8,3)color(00.41,0.4,0,1)"],
            "factions": []
        }
    },
    "receiveremotetargets": 1,
    "reportremotetargets": 1,
    "reportownposition": 1,
    "crew": "rhs_msv_emr_armoredcrew",
    "rhs_aps_shtora": 1,
    # Class: CfgVehicles|rhs_t90a_tv|Turrets [Indent level: 1],
    "turrets": {
        # Class: CfgVehicles|rhs_t90a_tv|Turrets|MainTurret [Indent level: 2]
        "mainturret": {
            "maxhorizontalrotspeed": 0.88,
            "weapons": ["rhs_weap_2a46m_5","rhs_weap_pkt","rhs_weap_902b","rhs_weap_fcs"],
            "magazines": ["rhs_mag_3bm46_8","rhs_mag_3bk31_3","rhs_mag_3of26_7","rhs_mag_9m119_4","rhs_mag_762x54mm_250","rhs_mag_762x54mm_250","rhs_mag_762x54mm_250","rhs_mag_762x54mm_250","rhs_mag_762x54mm_250","rhs_mag_762x54mm_250","rhs_mag_762x54mm_250","rhs_mag_762x54mm_250","rhs_mag_3d17_12","rhs_laserfcsmag","rhs_laserfcsmag"],
            "turretinfotype": "RHS_RscWeaponPlissa_T90_FCS",
            # Class: CfgVehicles|rhs_t90a_tv|Turrets|MainTurret|OpticsIn [Indent level: 3],
            "opticsin": {
                # Class: CfgVehicles|rhs_t90a_tv|Turrets|MainTurret|OpticsIn|Periscope [Indent level: 4]
                "periscope": {
                    "campos": "view_periscope",
                    "hitpoint": "Hit_Optic_Periscope",
                    "opticsdisplayname": "PERISCOPE",
                    "minfov": 0.466667,
                    "maxfov": 0.466667,
                    "initfov": 0.466667,
                    "visionmode": ["Normal"],
                    "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tvn5.p3d",
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
                # Class: CfgVehicles|rhs_t90a_tv|Turrets|MainTurret|OpticsIn|day1 [Indent level: 4],
                "day1": {
                    "campos": "view_1g46",
                    "hitpoint": "Hit_Optic_1G46",
                    "opticsdisplayname": "DAY",
                    "initfov": 0.175,
                    "minfov": 0.175,
                    "maxfov": 0.175,
                    "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_1g46.p3d",
                    "visionmode": ["Normal"],
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
                # Class: CfgVehicles|rhs_t90a_tv|Turrets|MainTurret|OpticsIn|day2 [Indent level: 4],
                "day2": {
                    "opticsdisplayname": "DAYZOOM",
                    "initfov": 0.0583333,
                    "minfov": 0.0583333,
                    "maxfov": 0.0583333,
                    "visionmode": ["Normal"],
                    "campos": "view_1g46",
                    "hitpoint": "Hit_Optic_1G46",
                    "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_1g46.p3d",
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
                # Class: CfgVehicles|rhs_t90a_tv|Turrets|MainTurret|OpticsIn|thermal1 [Indent level: 4],
                "thermal1": {
                    "campos": "gunnerview2",
                    "hitpoint": "Hit_Optic_ESSA",
                    "opticsdisplayname": "TI1",
                    "initfov": 0.466667,
                    "minfov": 0.466667,
                    "maxfov": 0.466667,
                    "visionmode": ["Ti"],
                    "thermalmode": [0,1],
                    "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_sosnau.p3d",
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
                # Class: CfgVehicles|rhs_t90a_tv|Turrets|MainTurret|OpticsIn|thermal2 [Indent level: 4],
                "thermal2": {
                    "opticsdisplayname": "TI2",
                    "initfov": 0.155556,
                    "minfov": 0.155556,
                    "maxfov": 0.155556,
                    "campos": "gunnerview2",
                    "hitpoint": "Hit_Optic_ESSA",
                    "visionmode": ["Ti"],
                    "thermalmode": [0,1],
                    "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_sosnau.p3d",
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
                # Class: CfgVehicles|rhs_t90a_tv|Turrets|MainTurret|OpticsIn|thermal3 [Indent level: 4],
                "thermal3": {
                    "opticsdisplayname": "TI3",
                    "initfov": 0.0388889,
                    "minfov": 0.0388889,
                    "maxfov": 0.0388889,
                    "campos": "gunnerview2",
                    "hitpoint": "Hit_Optic_ESSA",
                    "visionmode": ["Ti"],
                    "thermalmode": [0,1],
                    "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_sosnau.p3d",
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
                # Class: CfgVehicles|rhs_t90a_tv|Turrets|MainTurret|OpticsIn|thermal4 [Indent level: 4],
                "thermal4": {
                    "opticsdisplayname": "AUTOTRACK",
                    "directionstabilized": 1,
                    "initfov": 0.0388889,
                    "minfov": 0.0388889,
                    "maxfov": 0.0388889,
                    "campos": "gunnerview2",
                    "hitpoint": "Hit_Optic_ESSA",
                    "visionmode": ["Ti"],
                    "thermalmode": [0,1],
                    "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_sosnau.p3d",
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
            # Class: CfgVehicles|rhs_t90a_tv|Turrets|MainTurret|Turrets [Indent level: 3],
            "turrets": {
                # Class: CfgVehicles|rhs_t90a_tv|Turrets|MainTurret|Turrets|CommanderOptics [Indent level: 4]
                "commanderoptics": {
                    # Class: CfgVehicles|rhs_t90a_tv|Turrets|MainTurret|Turrets|CommanderOptics|Components [Indent level: 5]
                    "components": {
                        # Class: CfgVehicles|rhs_t90a_tv|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 6]
                        "vehiclesystemsdisplaymanagercomponentleft": {
                            # Class: CfgVehicles|rhs_t90a_tv|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentLeft|EmptyDisplay [Indent level: 7]
                            "emptydisplay": {
                                "componenttype": "EmptyDisplayComponent"
                            },
                            # Class: CfgVehicles|rhs_t90a_tv|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentLeft|CrewDisplay [Indent level: 7],
                            "crewdisplay": {
                                "componenttype": "CrewDisplayComponent",
                                "resource": "RscCustomInfoCrew"
                            },
                            # Class: CfgVehicles|rhs_t90a_tv|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentLeft|MinimapDisplay [Indent level: 7],
                            "minimapdisplay": {
                                "componenttype": "MinimapDisplayComponent",
                                "resource": "RscCustomInfoMiniMap"
                            },
                            # Class: CfgVehicles|rhs_t90a_tv|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentLeft|VehiclePrimaryGunnerDisplay [Indent level: 7],
                            "vehicleprimarygunnerdisplay": {
                                "componenttype": "TransportFeedDisplayComponent",
                                "source": "PrimaryGunner"
                            }
                        },
                        # Class: CfgVehicles|rhs_t90a_tv|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 6],
                        "vehiclesystemsdisplaymanagercomponentright": {
                            # Class: CfgVehicles|rhs_t90a_tv|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentRight|EmptyDisplay [Indent level: 7]
                            "emptydisplay": {
                                "componenttype": "EmptyDisplayComponent"
                            },
                            # Class: CfgVehicles|rhs_t90a_tv|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentRight|CrewDisplay [Indent level: 7],
                            "crewdisplay": {
                                "componenttype": "CrewDisplayComponent",
                                "resource": "RscCustomInfoCrew"
                            },
                            # Class: CfgVehicles|rhs_t90a_tv|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentRight|MinimapDisplay [Indent level: 7],
                            "minimapdisplay": {
                                "componenttype": "MinimapDisplayComponent",
                                "resource": "RscCustomInfoMiniMap"
                            },
                            # Class: CfgVehicles|rhs_t90a_tv|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentRight|VehiclePrimaryGunnerDisplay [Indent level: 7],
                            "vehicleprimarygunnerdisplay": {
                                "componenttype": "TransportFeedDisplayComponent",
                                "source": "PrimaryGunner"
                            }
                        }
                    },
                    "gun": "obsGun",
                    "animationsourcegun": "obsGun",
                    "weapons": ["rhs_weap_nsvt_t72"],
                    "magazines": ["rhs_mag_127x108mm_150","rhs_mag_127x108mm_150"],
                    "discretedistance": [100,200,300,400,500,600,800,900,1000,1100,1200,1400,1500,1800,1900,2000],
                    "discretedistanceinitindex": 2,
                    "memorypointgun": "mg_end",
                    "gunbeg": "mg_end",
                    "gunend": "mg_start",
                    "minelev": -7,
                    "maxelev": 60,
                    "minturn": -180,
                    "maxturn": 180,
                    "initelev": 0,
                    "lodturnedout": 0,
                    "turretinfotype": "rhs_gui_optic_TKN4S_rangefinder",
                    "gunneroutopticsmodel": "A3|weapons_f|reticle|optics_empty",
                    "gunneropticseffect": ["TankGunnerOptics1","BWTV","OpticsBlur2","OpticsCHAbera3"],
                    # Class: CfgVehicles|rhs_t90_tv|Turrets|MainTurret|Turrets|CommanderOptics|OpticsIn [Indent level: 5],
                    "opticsin": {
                        # Class: CfgVehicles|rhs_t90_tv|Turrets|MainTurret|Turrets|CommanderOptics|OpticsIn|day1aa [Indent level: 6]
                        "day1aa": {
                            "campos": "commanderview_aa",
                            "hitpoint": "Hit_Optic_NSVT",
                            "opticsdisplayname": "AA",
                            "initanglex": 0,
                            "minanglex": -30,
                            "maxanglex": 30,
                            "initangley": 0,
                            "minangley": -100,
                            "maxangley": 100,
                            "initfov": 0.291667,
                            "minfov": 0.291667,
                            "maxfov": 0.291667,
                            "visionmode": ["Normal"],
                            "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_pzu5.p3d",
                            "gunneropticseffect": ["OpticsBlur2","OpticsCHAbera3"]
                        },
                        # Class: CfgVehicles|rhs_t90_tv|Turrets|MainTurret|Turrets|CommanderOptics|OpticsIn|day1 [Indent level: 6],
                        "day1": {
                            "campos": "commanderview",
                            "hitpoint": "Hit_Optic_TKN4S",
                            "opticsdisplayname": "DAY",
                            "initfov": 0.7,
                            "minfov": 0.7,
                            "maxfov": 0.7,
                            "visionmode": ["Normal"],
                            "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tkn4s.p3d",
                            "gunneropticseffect": ["TankGunnerOptics1","BWTV","OpticsBlur2","OpticsCHAbera3"],
                            "initanglex": 0,
                            "minanglex": -30,
                            "maxanglex": 30,
                            "initangley": 0,
                            "minangley": -100,
                            "maxangley": 100
                        },
                        # Class: CfgVehicles|rhs_t90_tv|Turrets|MainTurret|Turrets|CommanderOptics|OpticsIn|day2 [Indent level: 6],
                        "day2": {
                            "opticsdisplayname": "DAYZOOM",
                            "initfov": 0.0875,
                            "minfov": 0.0875,
                            "maxfov": 0.0875,
                            "visionmode": ["Normal"],
                            "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tkn4s_zoom.p3d",
                            "gunneropticseffect": ["TankGunnerOptics1","OpticsBlur2","OpticsCHAbera3"],
                            "campos": "commanderview",
                            "hitpoint": "Hit_Optic_TKN4S",
                            "initanglex": 0,
                            "minanglex": -30,
                            "maxanglex": 30,
                            "initangley": 0,
                            "minangley": -100,
                            "maxangley": 100
                        },
                        # Class: CfgVehicles|rhs_t90_tv|Turrets|MainTurret|Turrets|CommanderOptics|OpticsIn|night3 [Indent level: 6],
                        "night3": {
                            "opticsdisplayname": "NIGHT",
                            "initfov": 0.1,
                            "minfov": 0.1,
                            "maxfov": 0.1,
                            "visionmode": ["NVG"],
                            "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_empty",
                            "gunneropticseffect": ["TankCommanderOptics1","OpticsBlur2","OpticsCHAbera3"],
                            "campos": "commanderview",
                            "hitpoint": "Hit_Optic_TKN4S",
                            "initanglex": 0,
                            "minanglex": -30,
                            "maxanglex": 30,
                            "initangley": 0,
                            "minangley": -100,
                            "maxangley": 100
                        }
                    },
                    "outgunnermayfire": 0,
                    "ingunnermayfire": 1,
                    "gunneraction": "passenger_inside_6",
                    "gunnerinaction": "rhs_t90_commander",
                    "personturretaction": "passenger_inside_6",
                    "selectionfireanim": "zasleh4",
                    "lockwhendriverout": 0,
                    "maxhorizontalrotspeed": 0.9,
                    "maxverticalrotspeed": 0.47,
                    "gunnertype": "rhs_msv_emr_crew_commander",
                    "body": "obsTurret",
                    "animationsourcebody": "obsTurret",
                    "stabilizedinaxes": 3,
                    "initturn": 0,
                    "canusescanners": 0,
                    "allowtablock": 0,
                    "memorypointgunneroutoptics": "commanderview",
                    "memorypointgunneroptics": "commanderview",
                    "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tkn3.p3d",
                    # Class: CfgVehicles|rhs_a3t72tank_base|Turrets|MainTurret|Turrets|CommanderOptics|ViewOptics [Indent level: 5],
                    "viewoptics": {
                        "initanglex": 0,
                        "minanglex": -30,
                        "maxanglex": 30,
                        "initangley": 0,
                        "minangley": -100,
                        "maxangley": 100,
                        "initfov": 0.101,
                        "minfov": 0.102,
                        "maxfov": 0.102,
                        "visionmode": ["Normal"],
                        "minmovex": 0,
                        "maxmovex": 0,
                        "minmovey": 0,
                        "maxmovey": 0,
                        "minmovez": 0,
                        "maxmovez": 0,
                        "speedzoommaxspeed": 1e+010,
                        "speedzoommaxfov": 0
                    },
                    "gunnergetinaction": "GetInMedium",
                    "gunnergetoutaction": "GetOutMedium",
                    "ispersonturret": 1,
                    "gunnerdoor": "hatchC",
                    "startengine": 0,
                    "viewgunnerinexternal": 1,
                    # Class: CfgVehicles|rhs_a3t72tank_base|Turrets|MainTurret|Turrets|CommanderOptics|HitPoints [Indent level: 5],
                    "hitpoints": {
                        # Class: CfgVehicles|rhs_a3t72tank_base|Turrets|MainTurret|Turrets|CommanderOptics|HitPoints|HitTurretCom [Indent level: 6]
                        "hitturretcom": {
                            "isturret": 1,
                            "armor": -999,
                            "material": -1,
                            "name": "vezVelitele",
                            "visual": "vezVelitele",
                            "passthrough": 0,
                            "minimalhit": 1,
                            "explosionshielding": 0.6,
                            "radius": 0.25
                        },
                        # Class: CfgVehicles|rhs_a3t72tank_base|Turrets|MainTurret|Turrets|CommanderOptics|HitPoints|HitGunCom [Indent level: 6],
                        "hitguncom": {
                            "isgun": 1,
                            "armor": -999,
                            "material": -1,
                            "name": "zbranVelitele",
                            "visual": "zbranVelitele",
                            "passthrough": 0,
                            "minimalhit": 1,
                            "explosionshielding": 0.6,
                            "radius": 0.25
                        }
                    },
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
                    "primaryobserver": 1,
                    "animationsourcehatch": "hatchCommander",
                    "animationsourcecamelev": "camElev",
                    "soundservo": ["A3|sounds_f|dummysound",0.01,1,10],
                    "commanding": 2,
                    "gunneroutopticscolor": [0,0,0,1],
                    "gunneroutforceoptics": 0,
                    "gunneroutopticsshowcursor": 0,
                    "gunneroutopticseffect": [],
                    "memorypointsgetingunner": "pos commander",
                    "memorypointsgetingunnerdir": "pos commander dir",
                    "soundelevation": ["",0.00316228,1],
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
                # Class: CfgVehicles|rhs_t72bd_tv|Turrets|MainTurret|Turrets|CommanderMG [Indent level: 4],
                "commandermg": {
                    "gunnername": "Commander HMG",
                    "proxyindex": 2,
                    "dontcreateai": 1,
                    "cantcreateai": 1,
                    "body": "mg_turret",
                    "gun": "mg_gun",
                    "animationsourcebody": "mg_turret",
                    "animationsourcegun": "mg_gun",
                    "gunnerdoor": "",
                    "memorypointgun": "mg_end",
                    "gunbeg": "mg_end",
                    "gunend": "mg_start",
                    "stabilizedinaxes": 0,
                    "gunneraction": "rhs_t72_commander_mg",
                    "gunnerinaction": "rhs_t72_commander_mg",
                    "canhidegunner": 0,
                    "ispersonturret": 0,
                    "memorypointgunneroutoptics": "commander_out_view",
                    "gunneroutopticsmodel": "A3|weapons_f|reticle|optics_empty",
                    "soundattenuationturret": "HeliAttenuationGunner",
                    "disablesoundattenuation": 1,
                    "animationsourcestickx": "mg_Turret_Inertia",
                    "animationsourcesticky": "mg_Gun_Inertia",
                    "gunnerlefthandanimname": "",
                    "gunnerrighthandanimname": "mg_handle2",
                    "turretinfotype": "RHS_RscWeaponZeroing",
                    "maxverticalrotspeed": 0.35,
                    "minelev": -6,
                    "maxelev": 45,
                    "initelev": 44,
                    "initturn": -180,
                    "lodopticsout": 1200,
                    "lodopticsin": 1200,
                    "discretedistance": [100,200,300,400,500,600,800,900,1000,1100,1200,1400,1500,1800,1900,2000],
                    "discretedistanceinitindex": 2,
                    "weapons": ["rhs_weap_nsvt_t72"],
                    "magazines": ["rhs_mag_127x108mm_50","rhs_mag_127x108mm_50","rhs_mag_127x108mm_50"],
                    "selectionfireanim": "zasleh4",
                    # Class: CfgVehicles|rhs_a3t72tank_base|Turrets|MainTurret|Turrets|CommanderMG|OpticsIn [Indent level: 5],
                    "opticsin": {
                        # Class: CfgVehicles|rhs_a3t72tank_base|Turrets|MainTurret|Turrets|CommanderMG|OpticsIn|Wide [Indent level: 6]
                        "wide": {
                            "visionmode": ["Normal"],
                            "initfov": 0.583333,
                            "minfov": 0.583333,
                            "maxfov": 0.583333,
                            "opticsdisplayname": "TKN3",
                            "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tkn3.p3d",
                            "gunneroutopticsmodel": "A3|weapons_f|reticle|optics_empty",
                            "hitpoint": "Hit_Optic_TKN3",
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
                        # Class: CfgVehicles|rhs_a3t72tank_base|Turrets|MainTurret|Turrets|CommanderOptics|OpticsIn|Night [Indent level: 6],
                        "night": {
                            "initfov": "0.7/4.2",
                            "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tkn3_night.p3d",
                            "visionmode": ["NVG"],
                            "opticsdisplayname": "TKN3",
                            "gunneroutopticsmodel": "A3|weapons_f|reticle|optics_empty",
                            "hitpoint": "Hit_Optic_TKN3",
                            "initanglex": 0,
                            "minanglex": -30,
                            "maxanglex": 30,
                            "initangley": 0,
                            "minangley": -100,
                            "maxangley": 100,
                            "minfov": 0.102,
                            "maxfov": 0.102,
                            "minmovex": 0,
                            "maxmovex": 0,
                            "minmovey": 0,
                            "maxmovey": 0,
                            "minmovez": 0,
                            "maxmovez": 0,
                            "speedzoommaxspeed": 1e+010,
                            "speedzoommaxfov": 0
                        },
                        # Class: CfgVehicles|rhs_a3t72tank_base|Turrets|MainTurret|Turrets|CommanderOptics|OpticsIn|Periscope [Indent level: 6],
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
                            "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tvn5.p3d",
                            "gunneropticseffect": ["TankGunnerOptics1","OpticsBlur2","OpticsCHAbera2"],
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
                    # Class: CfgVehicles|rhs_a3t72tank_base|Turrets|MainTurret|Turrets|CommanderMG|HitPoints [Indent level: 5],
                    "hitpoints": {
                        # Class: CfgVehicles|rhs_a3t72tank_base|Turrets|MainTurret|Turrets|CommanderMG|HitPoints|HitTurretNSVT [Indent level: 6]
                        "hitturretnsvt": {
                            "isturret": 1,
                            "armor": 0.3,
                            "material": -1,
                            "name": "nsvt_turret",
                            "armorcomponent": "Hit_NSVT_Turret",
                            "visual": "-",
                            "passthrough": 0,
                            "minimalhit": 0.03,
                            "explosionshielding": 0.6,
                            "radius": 0.25
                        },
                        # Class: CfgVehicles|rhs_a3t72tank_base|Turrets|MainTurret|Turrets|CommanderMG|HitPoints|HitGunNSVT [Indent level: 6],
                        "hitgunnsvt": {
                            "isgun": 1,
                            "armor": 0.3,
                            "material": -1,
                            "name": "nsvt_gun",
                            "armorcomponent": "Hit_NSVT_Gun",
                            "visual": "-",
                            "passthrough": 0,
                            "minimalhit": 0.03,
                            "explosionshielding": 0.6,
                            "radius": 0.25
                        }
                    },
                    "gunnercompartments": "Compartment5",
                    "lodturnedout": 1200,
                    "maxhorizontalrotspeed": 1.8,
                    "minturn": -360,
                    "maxturn": 360,
                    "canusescanners": 0,
                    "allowtablock": 0,
                    "memorypointgunneroptics": "commanderview",
                    "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tkn3.p3d",
                    "gunneropticseffect": ["TankGunnerOptics1","OpticsBlur2","OpticsCHAbera3"],
                    # Class: CfgVehicles|rhs_a3t72tank_base|Turrets|MainTurret|Turrets|CommanderOptics|ViewOptics [Indent level: 5],
                    "viewoptics": {
                        "initanglex": 0,
                        "minanglex": -30,
                        "maxanglex": 30,
                        "initangley": 0,
                        "minangley": -100,
                        "maxangley": 100,
                        "initfov": 0.101,
                        "minfov": 0.102,
                        "maxfov": 0.102,
                        "visionmode": ["Normal"],
                        "minmovex": 0,
                        "maxmovex": 0,
                        "minmovey": 0,
                        "maxmovey": 0,
                        "minmovez": 0,
                        "maxmovez": 0,
                        "speedzoommaxspeed": 1e+010,
                        "speedzoommaxfov": 0
                    },
                    "gunnergetinaction": "GetInMedium",
                    "gunnergetoutaction": "GetOutMedium",
                    "personturretaction": "RHS_passenger_inside_6",
                    "gunnertype": "rhs_msv_crew_commander",
                    "startengine": 0,
                    "viewgunnerinexternal": 1,
                    "outgunnermayfire": 1,
                    "ingunnermayfire": 1,
                    # Class: CfgVehicles|rhs_a3t72tank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components [Indent level: 5],
                    "components": {
                        # Class: CfgVehicles|rhs_a3t72tank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 6]
                        "vehiclesystemsdisplaymanagercomponentleft": {
                            # Class: CfgVehicles|rhs_a3t72tank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentLeft|EmptyDisplay [Indent level: 7]
                            "emptydisplay": {
                                "componenttype": "EmptyDisplayComponent"
                            },
                            # Class: CfgVehicles|rhs_a3t72tank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentLeft|CrewDisplay [Indent level: 7],
                            "crewdisplay": {
                                "componenttype": "CrewDisplayComponent",
                                "resource": "RscCustomInfoCrew"
                            }
                        },
                        # Class: CfgVehicles|rhs_a3t72tank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 6],
                        "vehiclesystemsdisplaymanagercomponentright": {
                            # Class: CfgVehicles|rhs_a3t72tank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentRight|EmptyDisplay [Indent level: 7]
                            "emptydisplay": {
                                "componenttype": "EmptyDisplayComponent"
                            },
                            # Class: CfgVehicles|rhs_a3t72tank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentRight|CrewDisplay [Indent level: 7],
                            "crewdisplay": {
                                "componenttype": "CrewDisplayComponent",
                                "resource": "RscCustomInfoCrew"
                            }
                        }
                    },
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
                    "primarygunner": 0,
                    "primaryobserver": 1,
                    "animationsourcehatch": "hatchCommander",
                    "animationsourcecamelev": "camElev",
                    "soundservo": ["A3|sounds_f|dummysound",0.01,1,10],
                    "commanding": 2,
                    "gunneroutopticscolor": [0,0,0,1],
                    "gunneroutforceoptics": 0,
                    "gunneroutopticsshowcursor": 0,
                    "gunneroutopticseffect": [],
                    "memorypointsgetingunner": "pos commander",
                    "memorypointsgetingunnerdir": "pos commander dir",
                    "soundelevation": ["",0.00316228,1],
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
                    "forcehidegunner": 0,
                    "showhmd": 0,
                    "lockwhendriverout": 0,
                    "lockwhenvehiclespeed": -1,
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
                    "gunnerleftleganimname": "",
                    "gunnerrightleganimname": "",
                    "precisegetinout": 0,
                    "turretfollowfreelook": 0,
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
                    "showcrewaim": 0
                }
            },
            "memorypointgunneroptics": "gunnerview2",
            "lodturnedout": 0,
            "memorypointgun": "usti hlavne2",
            "selectionfireanim": "zaslehCoax",
            "gunbeg": "usti hlavne",
            "gunend": "konec hlavne",
            "startengine": 0,
            "maxverticalrotspeed": 0.07,
            "minelev": -5,
            "maxelev": 14,
            "initelev": 10,
            "initturn": -13,
            "soundservo": ["rhsafrf|addons|rhs_t72|sounds|traverse",7,1,30],
            # Class: CfgVehicles|rhs_a3t72tank_base|Turrets|MainTurret|TurnIn [Indent level: 3],
            "turnin": {
                "limitsarraytop": [[14,-180],[14,180]],
                "limitsarraybottom": [[-1.9,-180],[-1.9,-134.687],[-4.7683,-133.687],[-5,0],[-4.7173,133.637],[-1.9,134.687],[-1.9,180]]
            },
            "discretedistance": [100],
            "discretedistanceinitindex": 0,
            "canusescanners": 0,
            "allowtablock": 0,
            "enablemanualfire": 0,
            "gunneroutopticsmodel": "",
            "gunneroutopticseffect": [],
            "gunneropticseffect": [],
            "gunnerforceoptics": 1,
            "lockwhendriverout": 1,
            "gunneraction": "rhs_t80a_gunner_out",
            "gunnerinaction": "rhs_t80a_gunner_in",
            "gunnergetinaction": "GetInMedium",
            "gunnergetoutaction": "GetOutMedium",
            "gunnerdoor": "hatchG",
            "forcehidegunner": 0,
            "ingunnermayfire": 1,
            "viewgunnerinexternal": 1,
            # Class: CfgVehicles|rhs_a3t72tank_base|Turrets|MainTurret|HitPoints [Indent level: 3],
            "hitpoints": {
                # Class: CfgVehicles|rhs_a3t72tank_base|Turrets|MainTurret|HitPoints|HitTurret [Indent level: 4]
                "hitturret": {
                    "armor": -150,
                    "material": -1,
                    "name": "vez",
                    "armorcomponent": "Hit_Turret",
                    "visual": "vez",
                    "passthrough": 0,
                    "minimalhit": -0.2,
                    "explosionshielding": 0.0009,
                    "radius": 0.1
                },
                # Class: CfgVehicles|rhs_a3t72tank_base|Turrets|MainTurret|HitPoints|HitGun [Indent level: 4],
                "hitgun": {
                    "armor": -150,
                    "material": -1,
                    "name": "zbran",
                    "armorcomponent": "Hit_Gun",
                    "visual": "-",
                    "passthrough": 0,
                    "minimalhit": -0.2,
                    "explosionshielding": 0.0001,
                    "radius": 0.1
                }
            },
            # Class: CfgVehicles|rhs_a3t72tank_base|Turrets|MainTurret|Reflectors [Indent level: 3],
            "reflectors": {
                # Class: CfgVehicles|rhs_a3t72tank_base|Turrets|MainTurret|Reflectors|Searchlight_FG125 [Indent level: 4]
                "searchlight_fg125": {
                    "color": [1900,1300,950],
                    "ambient": [5,5,5],
                    "position": "Light_FG125",
                    "direction": "Light_FG125_end",
                    "hitpoint": "Light_FG125",
                    "selection": "Light_FG125",
                    "size": 1,
                    "innerangle": 8,
                    "outerangle": 15,
                    "conefadecoef": 1,
                    "intensity": 45,
                    "useflare": 1,
                    "daylight": 1,
                    "flaresize": 0.85,
                    # Class: CfgVehicles|rhs_a3t72tank_base|Turrets|MainTurret|Reflectors|Searchlight_FG125|Attenuation [Indent level: 5],
                    "attenuation": {
                        "start": 1,
                        "constant": 0,
                        "linear": 0,
                        "quadratic": 0.02,
                        "hardlimitstart": 630,
                        "hardlimitend": 660
                    }
                },
                # Class: CfgVehicles|rhs_a3t72tank_base|Turrets|MainTurret|Reflectors|Searchlight_FG125_Flare [Indent level: 4],
                "searchlight_fg125_flare": {
                    "color": [7,6,6.5],
                    "ambient": [22,22,22],
                    "position": "Light_FG125",
                    "direction": "Light_FG125_end",
                    "hitpoint": "Light_FG125",
                    "selection": "Light_FG125",
                    "size": 1,
                    "innerangle": 30,
                    "outerangle": 175,
                    "conefadecoef": 10,
                    "intensity": 100,
                    "useflare": 1,
                    "daylight": 0,
                    "flaresize": 1.85,
                    # Class: CfgVehicles|rhs_a3t72tank_base|Turrets|MainTurret|Reflectors|Searchlight_FG125_Flare|Attenuation [Indent level: 5],
                    "attenuation": {
                        "start": 0,
                        "constant": 0,
                        "linear": 0,
                        "quadratic": 10,
                        "hardlimitstart": 0,
                        "hardlimitend": 0.9
                    }
                }
            },
            "armorlights": 0.1,
            # Class: CfgVehicles|rhs_a3t72tank_base|Turrets|MainTurret|Components [Indent level: 3],
            "components": {
                # Class: CfgVehicles|rhs_a3t72tank_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 4]
                "vehiclesystemsdisplaymanagercomponentleft": {
                    # Class: CfgVehicles|rhs_a3t72tank_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft|EmptyDisplay [Indent level: 5]
                    "emptydisplay": {
                        "componenttype": "EmptyDisplayComponent"
                    },
                    # Class: CfgVehicles|rhs_a3t72tank_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft|CrewDisplay [Indent level: 5],
                    "crewdisplay": {
                        "componenttype": "CrewDisplayComponent",
                        "resource": "RscCustomInfoCrew"
                    }
                },
                # Class: CfgVehicles|rhs_a3t72tank_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 4],
                "vehiclesystemsdisplaymanagercomponentright": {
                    # Class: CfgVehicles|rhs_a3t72tank_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight|EmptyDisplay [Indent level: 5]
                    "emptydisplay": {
                        "componenttype": "EmptyDisplayComponent"
                    },
                    # Class: CfgVehicles|rhs_a3t72tank_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight|CrewDisplay [Indent level: 5],
                    "crewdisplay": {
                        "componenttype": "CrewDisplayComponent",
                        "resource": "RscCustomInfoCrew"
                    }
                }
            },
            "commanding": 1,
            "gunneropticsmodel": "A3|weapons_f|reticle|optics_empty",
            "memorypointsgetingunner": "pos gunner",
            "memorypointsgetingunnerdir": "pos gunner dir",
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
            # Class: CfgVehicles|AllVehicles|NewTurret|TurnOut [Indent level: 2],
            "turnout": {
                "turnoffset": 0
            },
            "showcrewaim": 0
        }
    },
    # Class: CfgVehicles|rhs_t90a_tv|AnimationSources [Indent level: 1],
    "animationsources": {
        # Class: CfgVehicles|rhs_t90a_tv|AnimationSources|reload_source [Indent level: 2]
        "reload_source": {
            "weapon": "rhs_weap_2a46m_5",
            "source": "reload"
        },
        # Class: CfgVehicles|rhs_t90a_tv|AnimationSources|reload_magazine_source [Indent level: 2],
        "reload_magazine_source": {
            "source": "reloadMagazine",
            "weapon": "rhs_weap_2a46m_5"
        },
        # Class: CfgVehicles|rhs_t90a_tv|AnimationSources|muzzle_rot_cannon [Indent level: 2],
        "muzzle_rot_cannon": {
            "source": "ammorandom",
            "weapon": "rhs_weap_2a46m_5"
        },
        # Class: CfgVehicles|rhs_t90_tv|AnimationSources|smokecap_revolving_source [Indent level: 2],
        "smokecap_revolving_source": {
            "source": "revolving",
            "weapon": "rhs_weap_902b"
        },
        # Class: CfgVehicles|rhs_t90_tv|AnimationSources|ShtoraTurn [Indent level: 2],
        "shtoraturn": {
            "source": "user",
            "animperiod": 2
        },
        # Class: CfgVehicles|rhs_t90_tv|AnimationSources|Unhide_vis_optic_d_driver [Indent level: 2],
        "unhide_vis_optic_d_driver": {
            "source": "hit",
            "hitpoint": "Hit_Optic_Driver"
        },
        # Class: CfgVehicles|rhs_t90_tv|AnimationSources|Unhide_vis_optic_d_gunperiscope [Indent level: 2],
        "unhide_vis_optic_d_gunperiscope": {
            "source": "hit",
            "hitpoint": "Hit_Optic_Periscope"
        },
        # Class: CfgVehicles|rhs_t90_tv|AnimationSources|Unhide_vis_optic_d_sosnau [Indent level: 2],
        "unhide_vis_optic_d_sosnau": {
            "source": "hit",
            "hitpoint": "Hit_Optic_ESSA"
        },
        # Class: CfgVehicles|rhs_t90_tv|AnimationSources|Unhide_vis_optic_d_1g46 [Indent level: 2],
        "unhide_vis_optic_d_1g46": {
            "source": "hit",
            "hitpoint": "Hit_Optic_1G46"
        },
        # Class: CfgVehicles|rhs_t90_tv|AnimationSources|Unhide_vis_optic_d_tkn4 [Indent level: 2],
        "unhide_vis_optic_d_tkn4": {
            "source": "hit",
            "hitpoint": "Hit_Optic_TKN4S"
        },
        # Class: CfgVehicles|rhs_t90_tv|AnimationSources|Unhide_vis_optic_d_1pz3 [Indent level: 2],
        "unhide_vis_optic_d_1pz3": {
            "source": "hit",
            "hitpoint": "Hit_Optic_NSVT"
        },
        # Class: CfgVehicles|rhs_t90_tv|AnimationSources|Unhide_vis_optic_d_periscope1 [Indent level: 2],
        "unhide_vis_optic_d_periscope1": {
            "source": "hit",
            "hitpoint": "Hit_Optic_Periscope1"
        },
        # Class: CfgVehicles|rhs_t90_tv|AnimationSources|Unhide_vis_optic_d_periscope2 [Indent level: 2],
        "unhide_vis_optic_d_periscope2": {
            "source": "hit",
            "hitpoint": "Hit_Optic_Periscope1"
        },
        # Class: CfgVehicles|rhs_t90_tv|AnimationSources|Unhide_vis_optic_d_periscope3 [Indent level: 2],
        "unhide_vis_optic_d_periscope3": {
            "source": "hit",
            "hitpoint": "Hit_Optic_Periscope1"
        },
        # Class: CfgVehicles|rhs_t90_tv|AnimationSources|Unhide_vis_optic_d_periscope4 [Indent level: 2],
        "unhide_vis_optic_d_periscope4": {
            "source": "hit",
            "hitpoint": "Hit_Optic_Periscope1"
        },
        # Class: CfgVehicles|rhs_t90_tv|AnimationSources|Unhide_vis_lwr_d_1 [Indent level: 2],
        "unhide_vis_lwr_d_1": {
            "source": "hit",
            "hitpoint": "Hit_LWR_1"
        },
        # Class: CfgVehicles|rhs_t90_tv|AnimationSources|Unhide_vis_lwr_d_2 [Indent level: 2],
        "unhide_vis_lwr_d_2": {
            "source": "hit",
            "hitpoint": "Hit_LWR_2"
        },
        # Class: CfgVehicles|rhs_t90_tv|AnimationSources|Unhide_vis_lwr_d_3 [Indent level: 2],
        "unhide_vis_lwr_d_3": {
            "source": "hit",
            "hitpoint": "Hit_LWR_3"
        },
        # Class: CfgVehicles|rhs_t90_tv|AnimationSources|Unhide_vis_lwr_d_4 [Indent level: 2],
        "unhide_vis_lwr_d_4": {
            "source": "hit",
            "hitpoint": "Hit_LWR_4"
        },
        # Class: CfgVehicles|rhs_t90_tv|AnimationSources|Unhide_vis_lwr_d_5 [Indent level: 2],
        "unhide_vis_lwr_d_5": {
            "source": "hit",
            "hitpoint": "Hit_LWR_5"
        },
        # Class: CfgVehicles|rhs_t90_tv|AnimationSources|Unhide_vis_lwr_d_6 [Indent level: 2],
        "unhide_vis_lwr_d_6": {
            "source": "hit",
            "hitpoint": "Hit_LWR_6"
        },
        # Class: CfgVehicles|rhs_t72bd_tv|AnimationSources|hide_com_shield [Indent level: 2],
        "hide_com_shield": {
            "source": "user",
            "animperiod": 3.25,
            "initphase": 0
        },
        # Class: CfgVehicles|rhs_t72bd_tv|AnimationSources|era_1_source [Indent level: 2],
        "era_1_source": {
            "source": "Hit",
            "hitpoint": "era_1_hitpoint"
        },
        # Class: CfgVehicles|rhs_t72bd_tv|AnimationSources|era_2_source [Indent level: 2],
        "era_2_source": {
            "source": "Hit",
            "hitpoint": "era_2_hitpoint"
        },
        # Class: CfgVehicles|rhs_t72bd_tv|AnimationSources|era_3_source [Indent level: 2],
        "era_3_source": {
            "source": "Hit",
            "hitpoint": "era_3_hitpoint"
        },
        # Class: CfgVehicles|rhs_t72bd_tv|AnimationSources|era_4_source [Indent level: 2],
        "era_4_source": {
            "source": "Hit",
            "hitpoint": "era_4_hitpoint"
        },
        # Class: CfgVehicles|rhs_t72bd_tv|AnimationSources|era_5_source [Indent level: 2],
        "era_5_source": {
            "source": "Hit",
            "hitpoint": "era_5_hitpoint"
        },
        # Class: CfgVehicles|rhs_t72bd_tv|AnimationSources|era_6_source [Indent level: 2],
        "era_6_source": {
            "source": "Hit",
            "hitpoint": "era_6_hitpoint"
        },
        # Class: CfgVehicles|rhs_t72bd_tv|AnimationSources|era_7_source [Indent level: 2],
        "era_7_source": {
            "source": "Hit",
            "hitpoint": "era_7_hitpoint"
        },
        # Class: CfgVehicles|rhs_t72bd_tv|AnimationSources|era_8_source [Indent level: 2],
        "era_8_source": {
            "source": "Hit",
            "hitpoint": "era_8_hitpoint"
        },
        # Class: CfgVehicles|rhs_t72bd_tv|AnimationSources|era_9_source [Indent level: 2],
        "era_9_source": {
            "source": "Hit",
            "hitpoint": "era_9_hitpoint"
        },
        # Class: CfgVehicles|rhs_t72bd_tv|AnimationSources|era_10_source [Indent level: 2],
        "era_10_source": {
            "source": "Hit",
            "hitpoint": "era_10_hitpoint"
        },
        # Class: CfgVehicles|rhs_t72bd_tv|AnimationSources|era_11_source [Indent level: 2],
        "era_11_source": {
            "source": "Hit",
            "hitpoint": "era_11_hitpoint"
        },
        # Class: CfgVehicles|rhs_t72bd_tv|AnimationSources|era_12_source [Indent level: 2],
        "era_12_source": {
            "source": "Hit",
            "hitpoint": "era_12_hitpoint"
        },
        # Class: CfgVehicles|rhs_t72bd_tv|AnimationSources|era_13_source [Indent level: 2],
        "era_13_source": {
            "source": "Hit",
            "hitpoint": "era_13_hitpoint"
        },
        # Class: CfgVehicles|rhs_t72bd_tv|AnimationSources|era_14_source [Indent level: 2],
        "era_14_source": {
            "source": "Hit",
            "hitpoint": "era_14_hitpoint"
        },
        # Class: CfgVehicles|rhs_t72bd_tv|AnimationSources|era_15_source [Indent level: 2],
        "era_15_source": {
            "source": "Hit",
            "hitpoint": "era_15_hitpoint"
        },
        # Class: CfgVehicles|rhs_t72bd_tv|AnimationSources|era_16_source [Indent level: 2],
        "era_16_source": {
            "source": "Hit",
            "hitpoint": "era_16_hitpoint"
        },
        # Class: CfgVehicles|rhs_t72bd_tv|AnimationSources|era_17_source [Indent level: 2],
        "era_17_source": {
            "source": "Hit",
            "hitpoint": "era_17_hitpoint"
        },
        # Class: CfgVehicles|rhs_t72bd_tv|AnimationSources|era_18_source [Indent level: 2],
        "era_18_source": {
            "source": "Hit",
            "hitpoint": "era_18_hitpoint"
        },
        # Class: CfgVehicles|rhs_t72bd_tv|AnimationSources|era_19_source [Indent level: 2],
        "era_19_source": {
            "source": "Hit",
            "hitpoint": "era_19_hitpoint"
        },
        # Class: CfgVehicles|rhs_t72bd_tv|AnimationSources|era_20_source [Indent level: 2],
        "era_20_source": {
            "source": "Hit",
            "hitpoint": "era_20_hitpoint"
        },
        # Class: CfgVehicles|rhs_t72bd_tv|AnimationSources|era_21_source [Indent level: 2],
        "era_21_source": {
            "source": "Hit",
            "hitpoint": "era_21_hitpoint"
        },
        # Class: CfgVehicles|rhs_t72bd_tv|AnimationSources|era_22_source [Indent level: 2],
        "era_22_source": {
            "source": "Hit",
            "hitpoint": "era_22_hitpoint"
        },
        # Class: CfgVehicles|rhs_t72bd_tv|AnimationSources|era_23_source [Indent level: 2],
        "era_23_source": {
            "source": "Hit",
            "hitpoint": "era_23_hitpoint"
        },
        # Class: CfgVehicles|rhs_t72bd_tv|AnimationSources|era_24_source [Indent level: 2],
        "era_24_source": {
            "source": "Hit",
            "hitpoint": "era_24_hitpoint"
        },
        # Class: CfgVehicles|rhs_t72bd_tv|AnimationSources|era_25_source [Indent level: 2],
        "era_25_source": {
            "source": "Hit",
            "hitpoint": "era_25_hitpoint"
        },
        # Class: CfgVehicles|rhs_t72bd_tv|AnimationSources|era_26_source [Indent level: 2],
        "era_26_source": {
            "source": "Hit",
            "hitpoint": "era_26_hitpoint"
        },
        # Class: CfgVehicles|rhs_t72bd_tv|AnimationSources|era_27_source [Indent level: 2],
        "era_27_source": {
            "source": "Hit",
            "hitpoint": "era_27_hitpoint"
        },
        # Class: CfgVehicles|rhs_t72bd_tv|AnimationSources|era_28_source [Indent level: 2],
        "era_28_source": {
            "source": "Hit",
            "hitpoint": "era_28_hitpoint"
        },
        # Class: CfgVehicles|rhs_t72bd_tv|AnimationSources|era_29_source [Indent level: 2],
        "era_29_source": {
            "source": "Hit",
            "hitpoint": "era_29_hitpoint"
        },
        # Class: CfgVehicles|rhs_t72bd_tv|AnimationSources|era_30_source [Indent level: 2],
        "era_30_source": {
            "source": "Hit",
            "hitpoint": "era_30_hitpoint"
        },
        # Class: CfgVehicles|rhs_t72bd_tv|AnimationSources|era_31_source [Indent level: 2],
        "era_31_source": {
            "source": "Hit",
            "hitpoint": "era_31_hitpoint"
        },
        # Class: CfgVehicles|rhs_t72bd_tv|AnimationSources|era_32_source [Indent level: 2],
        "era_32_source": {
            "source": "Hit",
            "hitpoint": "era_32_hitpoint"
        },
        # Class: CfgVehicles|rhs_t72bd_tv|AnimationSources|elev [Indent level: 2],
        "elev": {
            "source": "user",
            "animperiod": 0.0016
        },
        # Class: CfgVehicles|rhs_t72bd_tv|AnimationSources|elev_bank [Indent level: 2],
        "elev_bank": {
            "source": "user",
            "animperiod": 0.0016
        },
        # Class: CfgVehicles|rhs_t72bd_tv|AnimationSources|lead [Indent level: 2],
        "lead": {
            "source": "user",
            "animperiod": 0.001
        },
        # Class: CfgVehicles|rhs_t72bd_tv|AnimationSources|offset [Indent level: 2],
        "offset": {
            "source": "user",
            "animperiod": 0.0002
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|AnimationSources|recoil_source [Indent level: 2],
        "recoil_source": {
            "source": "door",
            "animperiod": 6,
            "initphase": 0
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|AnimationSources|muzzle_rot_mg1 [Indent level: 2],
        "muzzle_rot_mg1": {
            "weapon": "rhs_weap_pkt",
            "source": "ammorandom"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|AnimationSources|autoloader [Indent level: 2],
        "autoloader": {
            "source": "user",
            "animperiod": 3.25,
            "initphase": 0
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|AnimationSources|turretHide [Indent level: 2],
        "turrethide": {
            "animperiod": 1e-010,
            "source": "user",
            "initphase": 0
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|AnimationSources|hide_sideskirts [Indent level: 2],
        "hide_sideskirts": {
            "displayname": "hide side skirts",
            "usesource": 1,
            "mass": 0,
            "animperiod": 0.01,
            "source": "user",
            "initphase": 0
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|AnimationSources|TCOverrideTurret [Indent level: 2],
        "tcoverrideturret": {
            "source": "user",
            "animperiod": 4,
            "initphase": 0
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|AnimationSources|sightHide [Indent level: 2],
        "sighthide": {
            "animperiod": 1e-010,
            "source": "user",
            "initphase": 0
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|AnimationSources|sightRange [Indent level: 2],
        "sightrange": {
            "source": "user",
            "animperiod": 0.0005,
            "initphase": 0
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|AnimationSources|sightElevationAPFSDS [Indent level: 2],
        "sightelevationapfsds": {
            "animperiod": 0.4,
            "initphase": 7.46,
            "source": "user"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|AnimationSources|sightElevationHEAT [Indent level: 2],
        "sightelevationheat": {
            "animperiod": 0.065,
            "source": "user",
            "initphase": 0
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|AnimationSources|sightElevationHEF [Indent level: 2],
        "sightelevationhef": {
            "animperiod": 0.08,
            "source": "user",
            "initphase": 0
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|AnimationSources|HatchC [Indent level: 2],
        "hatchc": {
            "source": "door",
            "animperiod": 2.1
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|AnimationSources|HatchG [Indent level: 2],
        "hatchg": {
            "source": "door",
            "animperiod": 2.1
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|AnimationSources|HatchD [Indent level: 2],
        "hatchd": {
            "source": "door",
            "animperiod": 2.1
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|AnimationSources|muzzle_rot_hmg [Indent level: 2],
        "muzzle_rot_hmg": {
            "weapon": "rhs_weap_nsvt_t72",
            "source": "ammorandom"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|AnimationSources|ReloadAnim [Indent level: 2],
        "reloadanim": {
            "source": "reload",
            "weapon": "rhs_weap_nsvt_t72"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|AnimationSources|ReloadMagazine [Indent level: 2],
        "reloadmagazine": {
            "source": "reloadmagazine",
            "weapon": "rhs_weap_nsvt_t72"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|AnimationSources|Revolving [Indent level: 2],
        "revolving": {
            "source": "revolving",
            "weapon": "rhs_weap_nsvt_t72"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|AnimationSources|skirt_1_source [Indent level: 2],
        "skirt_1_source": {
            "source": "Hit",
            "hitpoint": "sideskirt_1_hitpoint"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|AnimationSources|skirt_2_source [Indent level: 2],
        "skirt_2_source": {
            "source": "Hit",
            "hitpoint": "sideskirt_2_hitpoint"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|AnimationSources|skirt_3_source [Indent level: 2],
        "skirt_3_source": {
            "source": "Hit",
            "hitpoint": "sideskirt_3_hitpoint"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|AnimationSources|skirt_4_source [Indent level: 2],
        "skirt_4_source": {
            "source": "Hit",
            "hitpoint": "sideskirt_4_hitpoint"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|AnimationSources|skirt_5_source [Indent level: 2],
        "skirt_5_source": {
            "source": "Hit",
            "hitpoint": "sideskirt_5_hitpoint"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|AnimationSources|skirt_6_source [Indent level: 2],
        "skirt_6_source": {
            "source": "Hit",
            "hitpoint": "sideskirt_6_hitpoint"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|AnimationSources|skirt_7_source [Indent level: 2],
        "skirt_7_source": {
            "source": "Hit",
            "hitpoint": "sideskirt_7_hitpoint"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|AnimationSources|skirt_8_source [Indent level: 2],
        "skirt_8_source": {
            "source": "Hit",
            "hitpoint": "sideskirt_8_hitpoint"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|AnimationSources|skirt_9_source [Indent level: 2],
        "skirt_9_source": {
            "source": "Hit",
            "hitpoint": "sideskirt_9_hitpoint"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|AnimationSources|skirt_10_source [Indent level: 2],
        "skirt_10_source": {
            "source": "Hit",
            "hitpoint": "sideskirt_10_hitpoint"
        }
    },
    # Class: CfgVehicles|rhs_t90a_tv|EventHandlers [Indent level: 1],
    "eventhandlers": {
        # Class: CfgVehicles|rhs_t90a_tv|EventHandlers|RHS_EventHandlers [Indent level: 2]
        "rhs_eventhandlers": {
            "killed": "[_this select 0,'rhs_Wreck_T90a_turret_F'] call rhs_fnc_turretBlow",
            "init": "_this call RHS_fnc_T72_init;",
            "fired": "_this call RHS_fnc_T72_autoloader;",
            "hitpart": "_this call rhs_fnc_hitSpall",
            "getout": "_this call rhs_fnc_t72_hatch;_this call rhs_fnc_hatchAbandon",
            "engine": "[_this select 0,_this select 1,2.7] call rhs_fnc_engineStartupDelay"
        },
        "init": "",
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');",
        # Class: DefaultEventHandlers|RHS_DefaultEventhandlers [Indent level: 0],
        "rhs_defaulteventhandlers": {
            "hitpart": "_this call rhs_fnc_hitPart"
        }
    },
    "simulation": "tankX",
    "maxfordingdepth": 0,
    "waterresistance": 0,
    "waterdamageengine": 0.2,
    "waterleakiness": 10,
    "thrustdelay": 0,
    "enginebrakecoef": 0.9,
    "tankturnforce": 950000,
    "tankturnforceangminspd": 0.7,
    "tankturnforceangspd": 0.92,
    "accelaidforcecoef": 2.5,
    "accelaidforceyoffset": -5.5,
    "accelaidforcespd": 2.23,
    "antirollbarforcecoef": 24,
    "antirollbarforcelimit": 42,
    "antirollbarspeedmin": 30,
    "antirollbarspeedmax": 75,
    "enginelosses": 35,
    "transmissionlosses": 45,
    "clutchstrength": 40,
    "latency": 1.3,
    "switchtime": 0,
    "changegeartype": "rpmratio",
    "gunnerhasflares": 0,
    "enablegps": 1,
    "hiddenselections": ["camo1","camo2","camo3","camo4","camo5","camo6","camo7","camo8","dazzler","dazzlerlight","camo11","n1","n2","n3","i1","dazzlerglass"],
    "unitinfotype": "RHS_RscInfoT90",
    "lockdetectionsystem": 4,
    # Class: CfgVehicles|rhs_t90_tv|Hitpoints [Indent level: 1],
    "hitpoints": {
        # Class: CfgVehicles|rhs_t90_tv|Hitpoints|Hit_Optic_Driver [Indent level: 2]
        "hit_optic_driver": {
            "armor": -40,
            "explosionshielding": 0,
            "name": "",
            "visual": "vis_optic_driver",
            "armorcomponent": "Hit_Optic_Driver",
            "passthrough": 0
        },
        # Class: CfgVehicles|rhs_t90_tv|Hitpoints|Hit_Optic_Periscope [Indent level: 2],
        "hit_optic_periscope": {
            "armor": -40,
            "explosionshielding": 0,
            "name": "",
            "visual": "vis_optic_gunperiscope",
            "armorcomponent": "Hit_Optic_Periscope",
            "passthrough": 0
        },
        # Class: CfgVehicles|rhs_t90_tv|Hitpoints|Hit_Optic_1G46 [Indent level: 2],
        "hit_optic_1g46": {
            "armor": -40,
            "explosionshielding": 0,
            "name": "",
            "visual": "vis_optic_1g46",
            "armorcomponent": "Hit_Optic_1G46",
            "passthrough": 0
        },
        # Class: CfgVehicles|rhs_t90_tv|Hitpoints|Hit_Optic_TPN4 [Indent level: 2],
        "hit_optic_tpn4": {
            "armor": -40,
            "explosionshielding": 0,
            "name": "",
            "visual": "vis_optic_TPN4",
            "armorcomponent": "Hit_Optic_ESSA",
            "passthrough": 0
        },
        # Class: CfgVehicles|rhs_t90_tv|Hitpoints|Hit_Optic_ESSA [Indent level: 2],
        "hit_optic_essa": {
            "armor": -40,
            "explosionshielding": 0,
            "name": "",
            "visual": "vis_optic_essa",
            "armorcomponent": "Hit_Optic_ESSA",
            "passthrough": 0
        },
        # Class: CfgVehicles|rhs_t90_tv|Hitpoints|Hit_Optic_NSVT [Indent level: 2],
        "hit_optic_nsvt": {
            "armor": -40,
            "explosionshielding": 0,
            "name": "",
            "visual": "vis_optic_1pz3",
            "armorcomponent": "Hit_Optic_NSVT",
            "passthrough": 0
        },
        # Class: CfgVehicles|rhs_t90_tv|Hitpoints|Hit_Optic_TKN4S [Indent level: 2],
        "hit_optic_tkn4s": {
            "armor": -40,
            "explosionshielding": 0,
            "name": "",
            "visual": "vis_optic_tkn4s",
            "armorcomponent": "Hit_Optic_TKN4S",
            "passthrough": 0
        },
        # Class: CfgVehicles|rhs_t90_tv|Hitpoints|Hit_Optic_Periscope1 [Indent level: 2],
        "hit_optic_periscope1": {
            "armor": -40,
            "explosionshielding": 0,
            "name": "",
            "visual": "vis_optic_periscope1",
            "armorcomponent": "Hit_Optic_Periscope1",
            "passthrough": 0
        },
        # Class: CfgVehicles|rhs_t90_tv|Hitpoints|Hit_Optic_Periscope2 [Indent level: 2],
        "hit_optic_periscope2": {
            "armor": -40,
            "explosionshielding": 0,
            "name": "",
            "visual": "vis_optic_periscope2",
            "armorcomponent": "Hit_Optic_Periscope2",
            "passthrough": 0
        },
        # Class: CfgVehicles|rhs_t90_tv|Hitpoints|Hit_Optic_Periscope3 [Indent level: 2],
        "hit_optic_periscope3": {
            "armor": -40,
            "explosionshielding": 0,
            "name": "",
            "visual": "vis_optic_periscope3",
            "armorcomponent": "Hit_Optic_Periscope3",
            "passthrough": 0
        },
        # Class: CfgVehicles|rhs_t90_tv|Hitpoints|Hit_Optic_Periscope4 [Indent level: 2],
        "hit_optic_periscope4": {
            "armor": -40,
            "explosionshielding": 0,
            "name": "",
            "visual": "vis_optic_periscope4",
            "armorcomponent": "Hit_Optic_Periscope4",
            "passthrough": 0
        },
        # Class: CfgVehicles|rhs_t90_tv|Hitpoints|Hit_Shtora_L [Indent level: 2],
        "hit_shtora_l": {
            "armor": -40,
            "explosionshielding": 0,
            "name": "",
            "visual": "vis_shtora_l",
            "armorcomponent": "Hit_Shtora_L",
            "passthrough": 0
        },
        # Class: CfgVehicles|rhs_t90_tv|Hitpoints|Hit_Shtora_R [Indent level: 2],
        "hit_shtora_r": {
            "armor": -40,
            "explosionshielding": 0,
            "name": "",
            "visual": "vis_shtora_r",
            "armorcomponent": "Hit_Shtora_R",
            "passthrough": 0
        },
        # Class: CfgVehicles|rhs_t90_tv|Hitpoints|Hit_LWR_1 [Indent level: 2],
        "hit_lwr_1": {
            "armor": -20,
            "explosionshielding": 0,
            "name": "",
            "visual": "vis_lwr_1",
            "armorcomponent": "aps_s1",
            "passthrough": 0
        },
        # Class: CfgVehicles|rhs_t90_tv|Hitpoints|Hit_LWR_2 [Indent level: 2],
        "hit_lwr_2": {
            "armor": -20,
            "explosionshielding": 0,
            "name": "",
            "visual": "vis_lwr_2",
            "armorcomponent": "aps_s2",
            "passthrough": 0
        },
        # Class: CfgVehicles|rhs_t90_tv|Hitpoints|Hit_LWR_3 [Indent level: 2],
        "hit_lwr_3": {
            "armor": -20,
            "explosionshielding": 0,
            "name": "",
            "visual": "vis_lwr_3",
            "armorcomponent": "aps_s3",
            "passthrough": 0
        },
        # Class: CfgVehicles|rhs_t90_tv|Hitpoints|Hit_LWR_4 [Indent level: 2],
        "hit_lwr_4": {
            "armor": -20,
            "explosionshielding": 0,
            "name": "",
            "visual": "vis_lwr_4",
            "armorcomponent": "aps_s4",
            "passthrough": 0
        },
        # Class: CfgVehicles|rhs_t90_tv|Hitpoints|Hit_LWR_5 [Indent level: 2],
        "hit_lwr_5": {
            "armor": -20,
            "explosionshielding": 0,
            "name": "",
            "visual": "vis_lwr_5",
            "armorcomponent": "aps_s5",
            "passthrough": 0
        },
        # Class: CfgVehicles|rhs_t90_tv|Hitpoints|Hit_LWR_6 [Indent level: 2],
        "hit_lwr_6": {
            "armor": -20,
            "explosionshielding": 0,
            "name": "",
            "visual": "vis_lwr_6",
            "armorcomponent": "aps_s6",
            "passthrough": 0
        },
        # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|Hit_Optic_SosnaU [Indent level: 2],
        "hit_optic_sosnau": {
            "armor": -40,
            "explosionshielding": 0,
            "name": "",
            "visual": "vis_optic_essa",
            "armorcomponent": "Hit_Optic_ESSA",
            "passthrough": 0
        },
        # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_1_hitpoint [Indent level: 2],
        "era_1_hitpoint": {
            "simulation": "RHS_ERA_K5",
            "armor": -100,
            "material": -1,
            "name": "e1",
            "armorcomponent": "e1",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_1_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_1_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_1_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e1",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_1_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e1",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_1_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
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
        # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_2_hitpoint [Indent level: 2],
        "era_2_hitpoint": {
            "simulation": "RHS_ERA_K5",
            "armor": -100,
            "material": -1,
            "name": "e2",
            "armorcomponent": "e2",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_2_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_2_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e2",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_2_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e2",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_2_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e2",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_2_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
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
        # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_3_hitpoint [Indent level: 2],
        "era_3_hitpoint": {
            "simulation": "RHS_ERA_K5",
            "armor": -100,
            "material": -1,
            "name": "e3",
            "armorcomponent": "e3",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_3_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_3_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e3",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_3_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e3",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_3_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e3",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_3_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
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
        # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_4_hitpoint [Indent level: 2],
        "era_4_hitpoint": {
            "simulation": "RHS_ERA_K5",
            "armor": -100,
            "material": -1,
            "name": "e4",
            "armorcomponent": "e4",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_4_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_4_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e4",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_4_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e4",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_4_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e4",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_4_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
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
        # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_5_hitpoint [Indent level: 2],
        "era_5_hitpoint": {
            "simulation": "RHS_ERA_K5",
            "armor": -100,
            "material": -1,
            "name": "e5",
            "armorcomponent": "e5",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_5_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_5_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e5",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_5_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e5",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_5_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e5",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_5_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
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
        # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_6_hitpoint [Indent level: 2],
        "era_6_hitpoint": {
            "simulation": "RHS_ERA_K5",
            "armor": -100,
            "material": -1,
            "name": "e6",
            "armorcomponent": "e6",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_6_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_6_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e6",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_6_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e6",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_6_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e6",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_6_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
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
        # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_7_hitpoint [Indent level: 2],
        "era_7_hitpoint": {
            "simulation": "RHS_ERA_K5",
            "armor": -100,
            "material": -1,
            "name": "e7",
            "armorcomponent": "e7",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_7_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_7_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e7",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_7_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e7",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_7_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e7",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_7_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
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
        # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_8_hitpoint [Indent level: 2],
        "era_8_hitpoint": {
            "simulation": "RHS_ERA_K5",
            "armor": -100,
            "material": -1,
            "name": "e8",
            "armorcomponent": "e8",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_8_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_8_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e8",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_8_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e8",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_8_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e8",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_8_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
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
        # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_9_hitpoint [Indent level: 2],
        "era_9_hitpoint": {
            "simulation": "RHS_ERA_K5",
            "armor": -100,
            "material": -1,
            "name": "e9",
            "armorcomponent": "e9",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_9_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_9_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e9",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_9_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e9",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_9_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e9",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_9_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
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
        # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_10_hitpoint [Indent level: 2],
        "era_10_hitpoint": {
            "simulation": "RHS_ERA_K5",
            "armor": -100,
            "material": -1,
            "name": "e10",
            "armorcomponent": "e10",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_10_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_10_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e10",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_10_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e10",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_10_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e10",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_10_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
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
        # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_11_hitpoint [Indent level: 2],
        "era_11_hitpoint": {
            "simulation": "RHS_ERA_K5",
            "armor": -100,
            "material": -1,
            "name": "e11",
            "armorcomponent": "e11",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_11_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_11_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e11",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_11_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e11",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_11_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e11",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_11_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
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
        # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_12_hitpoint [Indent level: 2],
        "era_12_hitpoint": {
            "simulation": "RHS_ERA_K5",
            "armor": -100,
            "material": -1,
            "name": "e12",
            "armorcomponent": "e12",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_12_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_12_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e12",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_12_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e12",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_12_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e12",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_12_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
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
        # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_13_hitpoint [Indent level: 2],
        "era_13_hitpoint": {
            "simulation": "RHS_ERA_K5",
            "armor": -100,
            "material": -1,
            "name": "e13",
            "armorcomponent": "e13",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_13_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_13_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e13",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_13_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e13",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_13_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e13",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_13_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
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
        # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_14_hitpoint [Indent level: 2],
        "era_14_hitpoint": {
            "simulation": "RHS_ERA_K5",
            "armor": -100,
            "material": -1,
            "name": "e14",
            "armorcomponent": "e14",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_14_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_14_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e14",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_14_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e14",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_14_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e14",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_14_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
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
        # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_15_hitpoint [Indent level: 2],
        "era_15_hitpoint": {
            "simulation": "RHS_ERA_K5",
            "armor": -100,
            "material": -1,
            "name": "e15",
            "armorcomponent": "e15",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_15_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_15_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e15",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_15_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e15",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_15_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e15",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_15_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
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
        # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_16_hitpoint [Indent level: 2],
        "era_16_hitpoint": {
            "simulation": "RHS_ERA_K5",
            "armor": -100,
            "material": -1,
            "name": "e16",
            "armorcomponent": "e16",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_16_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_16_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e16",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_16_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e16",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_16_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e16",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_16_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
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
        # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_17_hitpoint [Indent level: 2],
        "era_17_hitpoint": {
            "simulation": "RHS_ERA_K5",
            "armor": -100,
            "material": -1,
            "name": "e17",
            "armorcomponent": "e17",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_17_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_17_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e17",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_17_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e17",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_17_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e17",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_17_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
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
        # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_18_hitpoint [Indent level: 2],
        "era_18_hitpoint": {
            "simulation": "RHS_ERA_K5",
            "armor": -100,
            "material": -1,
            "name": "e18",
            "armorcomponent": "e18",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_18_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_18_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e18",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_18_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e18",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_18_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e18",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_18_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
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
        # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_19_hitpoint [Indent level: 2],
        "era_19_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e19",
            "armorcomponent": "e19",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_19_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_19_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e19",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_19_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e19",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_19_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e19",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_19_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
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
        # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_20_hitpoint [Indent level: 2],
        "era_20_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e20",
            "armorcomponent": "e20",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_20_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_20_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e20",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_20_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e20",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_20_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e20",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_20_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
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
        # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_21_hitpoint [Indent level: 2],
        "era_21_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e21",
            "armorcomponent": "e21",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_21_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_21_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e21",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_21_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e21",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_21_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e21",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_21_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
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
        # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_22_hitpoint [Indent level: 2],
        "era_22_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e22",
            "armorcomponent": "e22",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_22_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_22_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e22",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_22_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e22",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_22_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e22",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_22_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
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
        # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_23_hitpoint [Indent level: 2],
        "era_23_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e23",
            "armorcomponent": "e23",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_23_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_23_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e23",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_23_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e23",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_23_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e23",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_23_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
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
        # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_24_hitpoint [Indent level: 2],
        "era_24_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e24",
            "armorcomponent": "e24",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_24_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_24_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e24",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_24_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e24",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_24_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e24",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_24_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
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
        # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_25_hitpoint [Indent level: 2],
        "era_25_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e25",
            "armorcomponent": "e25",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_25_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_25_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e25",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_25_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e25",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_25_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e25",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_25_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
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
        # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_26_hitpoint [Indent level: 2],
        "era_26_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e26",
            "armorcomponent": "e26",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_26_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_26_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e26",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_26_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e26",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_26_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e26",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_26_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
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
        # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_27_hitpoint [Indent level: 2],
        "era_27_hitpoint": {
            "simulation": "RHS_ERA_K5",
            "armor": -100,
            "material": -1,
            "name": "e27",
            "armorcomponent": "e27",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_27_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_27_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e27",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_27_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e27",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_27_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e27",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_27_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
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
        # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_28_hitpoint [Indent level: 2],
        "era_28_hitpoint": {
            "simulation": "RHS_ERA_K5",
            "armor": -100,
            "material": -1,
            "name": "e28",
            "armorcomponent": "e28",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_28_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_28_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e28",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_28_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e28",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_28_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e28",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_28_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
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
        # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_29_hitpoint [Indent level: 2],
        "era_29_hitpoint": {
            "simulation": "RHS_ERA_K5",
            "armor": -100,
            "material": -1,
            "name": "e29",
            "armorcomponent": "e29",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_29_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_29_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e29",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_29_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e29",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_29_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e29",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_29_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
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
        # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_30_hitpoint [Indent level: 2],
        "era_30_hitpoint": {
            "simulation": "RHS_ERA_K5",
            "armor": -100,
            "material": -1,
            "name": "e30",
            "armorcomponent": "e30",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_30_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_30_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e30",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_30_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e30",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_30_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e30",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_30_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
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
        # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_31_hitpoint [Indent level: 2],
        "era_31_hitpoint": {
            "simulation": "RHS_ERA_K5",
            "armor": -100,
            "material": -1,
            "name": "e31",
            "armorcomponent": "e31",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_31_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_31_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e31",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_31_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e31",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_31_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e31",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_31_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
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
        # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_32_hitpoint [Indent level: 2],
        "era_32_hitpoint": {
            "simulation": "RHS_ERA_K5",
            "armor": -100,
            "material": -1,
            "name": "e32",
            "armorcomponent": "e32",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_32_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_32_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e32",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_32_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e32",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_32_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e32",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t72bd_tv|HitPoints|era_32_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
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
        # Class: CfgVehicles|rhs_a3t72tank_base|HitPoints|Armor_Composite_75 [Indent level: 2],
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
        # Class: CfgVehicles|rhs_a3t72tank_base|HitPoints|Armor_Composite_80 [Indent level: 2],
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
        # Class: CfgVehicles|rhs_a3t72tank_base|HitPoints|Armor_Composite_85 [Indent level: 2],
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
        # Class: CfgVehicles|rhs_a3t72tank_base|HitPoints|Armor_Composite_95 [Indent level: 2],
        "armor_composite_95": {
            "armor": 999,
            "material": -1,
            "name": "Armor_CE_95_Hit",
            "armorcomponent": "Armor_CE_95",
            "simulation": "RHS_Composite_95",
            "passthrough": 0,
            "minimalhit": 1,
            "explosionshielding": 0,
            "radius": 0.001,
            "visual": "-"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|HitPoints|Sideskirt_1_hitpoint [Indent level: 2],
        "sideskirt_1_hitpoint": {
            "simulation": "RHS_Sideskirt_Rubber",
            "armor": -80,
            "material": -1,
            "name": "Skirt_1",
            "armorcomponent": "Skirt_1",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.2,
            "radius": 0.16,
            "visual": "-"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|HitPoints|Sideskirt_2_hitpoint [Indent level: 2],
        "sideskirt_2_hitpoint": {
            "simulation": "RHS_Sideskirt_Rubber",
            "armor": -80,
            "material": -1,
            "name": "Skirt_2",
            "armorcomponent": "Skirt_2",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.2,
            "radius": 0.16,
            "visual": "-"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|HitPoints|Sideskirt_3_hitpoint [Indent level: 2],
        "sideskirt_3_hitpoint": {
            "simulation": "RHS_Sideskirt_Rubber",
            "armor": -80,
            "material": -1,
            "name": "Skirt_3",
            "armorcomponent": "Skirt_3",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.2,
            "radius": 0.16,
            "visual": "-"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|HitPoints|Sideskirt_4_hitpoint [Indent level: 2],
        "sideskirt_4_hitpoint": {
            "simulation": "RHS_Sideskirt_Rubber",
            "armor": -80,
            "material": -1,
            "name": "Skirt_4",
            "armorcomponent": "Skirt_4",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.2,
            "radius": 0.16,
            "visual": "-"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|HitPoints|Sideskirt_5_hitpoint [Indent level: 2],
        "sideskirt_5_hitpoint": {
            "simulation": "RHS_Sideskirt_Rubber",
            "armor": -80,
            "material": -1,
            "name": "Skirt_5",
            "armorcomponent": "Skirt_5",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.2,
            "radius": 0.16,
            "visual": "-"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|HitPoints|Sideskirt_6_hitpoint [Indent level: 2],
        "sideskirt_6_hitpoint": {
            "simulation": "RHS_Sideskirt_Rubber",
            "armor": -80,
            "material": -1,
            "name": "Skirt_6",
            "armorcomponent": "Skirt_6",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.2,
            "radius": 0.16,
            "visual": "-"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|HitPoints|Sideskirt_7_hitpoint [Indent level: 2],
        "sideskirt_7_hitpoint": {
            "simulation": "RHS_Sideskirt_Rubber",
            "armor": -80,
            "material": -1,
            "name": "Skirt_7",
            "armorcomponent": "Skirt_7",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.2,
            "radius": 0.16,
            "visual": "-"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|HitPoints|Sideskirt_8_hitpoint [Indent level: 2],
        "sideskirt_8_hitpoint": {
            "simulation": "RHS_Sideskirt_Rubber",
            "armor": -80,
            "material": -1,
            "name": "Skirt_8",
            "armorcomponent": "Skirt_8",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.2,
            "radius": 0.16,
            "visual": "-"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|HitPoints|Sideskirt_9_hitpoint [Indent level: 2],
        "sideskirt_9_hitpoint": {
            "simulation": "RHS_Sideskirt_Rubber",
            "armor": -80,
            "material": -1,
            "name": "Skirt_9",
            "armorcomponent": "Skirt_9",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.2,
            "radius": 0.16,
            "visual": "-"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|HitPoints|Sideskirt_10_hitpoint [Indent level: 2],
        "sideskirt_10_hitpoint": {
            "simulation": "RHS_Sideskirt_Rubber",
            "armor": -80,
            "material": -1,
            "name": "Skirt_10",
            "armorcomponent": "Skirt_10",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.2,
            "radius": 0.16,
            "visual": "-"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|HitPoints|HitFuelTank_Left [Indent level: 2],
        "hitfueltank_left": {
            "armor": -80,
            "material": -1,
            "name": "Hit_FuelTank_Left",
            "armorcomponent": "Hit_FuelTank_Left",
            "visual": "-",
            "passthrough": 0,
            "minimalhit": 0.3,
            "explosionshielding": 0,
            "radius": 0.1
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|HitPoints|HitFuelTank_Right [Indent level: 2],
        "hitfueltank_right": {
            "name": "Hit_FuelTank_Right",
            "armorcomponent": "Hit_FuelTank_Right",
            "armor": -80,
            "material": -1,
            "visual": "-",
            "passthrough": 0,
            "minimalhit": 0.3,
            "explosionshielding": 0,
            "radius": 0.1
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|HitPoints|HitFuel [Indent level: 2],
        "hitfuel": {
            "armor": 999,
            "name": "Hit_Fuel",
            "armorcomponent": "Hit_Fuel",
            "visual": "-",
            "passthrough": 0,
            "minimalhit": 1,
            "explosionshielding": 0,
            "radius": 0.01,
            "depends": "(HitFuelTank_Left+HitFuelTank_Right)*0.5"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|HitPoints|HitHull [Indent level: 2],
        "hithull": {
            "armor": -100,
            "name": "Hit_Hull",
            "armorcomponent": "Hit_Carousel",
            "visual": "zbytek",
            "passthrough": 0,
            "minimalhit": 0.04,
            "explosionshielding": 0.01,
            "radius": 0.1,
            "material": -1
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|HitPoints|HitEngine [Indent level: 2],
        "hitengine": {
            "armor": -150,
            "material": -1,
            "name": "Hit_Engine",
            "armorcomponent": "Hit_Engine",
            "visual": "zbytek",
            "passthrough": 0,
            "minimalhit": 0.14,
            "explosionshielding": 0.009,
            "radius": 0.18,
            # Class: CfgVehicles|rhs_a3t72tank_base|HitPoints|HitEngine|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_a3t72tank_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Smoke [Indent level: 4],
                "rhs_engine_smoke": {
                    "simulation": "particles",
                    "type": "SmallWreckSmoke",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "enabled": "engineDamage"
                },
                # Class: CfgVehicles|rhs_a3t72tank_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Fire [Indent level: 4],
                "rhs_engine_fire": {
                    "type": "SmallFireFPlace",
                    "simulation": "particles",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "enabled": "engineDamage"
                },
                # Class: CfgVehicles|rhs_a3t72tank_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Sparks [Indent level: 4],
                "rhs_engine_sparks": {
                    "type": "RHS_FireSparks",
                    "simulation": "particles",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "enabled": "engineDamage"
                },
                # Class: CfgVehicles|rhs_a3t72tank_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Sounds [Indent level: 4],
                "rhs_engine_sounds": {
                    "simulation": "sound",
                    "type": "Fire",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "enabled": "engineDamage"
                },
                # Class: CfgVehicles|rhs_a3t72tank_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Smoke_small1 [Indent level: 4],
                "rhs_engine_smoke_small1": {
                    "type": "WeaponWreckSmoke",
                    "position": "engine_smoke2",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "enabled": "engineDamage"
                },
                # Class: CfgVehicles|rhs_a3t72tank_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Smoke_small2 [Indent level: 4],
                "rhs_engine_smoke_small2": {
                    "position": "engine_smoke3",
                    "type": "WeaponWreckSmoke",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "enabled": "engineDamage"
                }
            }
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|HitPoints|HitLTrack [Indent level: 2],
        "hitltrack": {
            "armor": -150,
            "armorcomponent": "Hit_TrackL",
            "name": "Hit_TrackL",
            "passthrough": 0,
            "material": -1,
            "minimalhit": -0.25,
            "explosionshielding": 0.5,
            "radius": 0.3,
            "visual": "pas_L"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|HitPoints|HitRTrack [Indent level: 2],
        "hitrtrack": {
            "armor": -150,
            "armorcomponent": "Hit_TrackR",
            "name": "Hit_TrackR",
            "material": -1,
            "passthrough": 0,
            "minimalhit": -0.25,
            "explosionshielding": 0.5,
            "radius": 0.3,
            "visual": "pas_P"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|HitPoints|Hit_Optic_TPD1K [Indent level: 2],
        "hit_optic_tpd1k": {
            "armor": -40,
            "explosionshielding": 0,
            "name": "",
            "visual": "vis_optic_tpd1k",
            "armorcomponent": "Hit_Optic_TPD1K",
            "passthrough": 0
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|HitPoints|Hit_Optic_1K13 [Indent level: 2],
        "hit_optic_1k13": {
            "armor": -40,
            "explosionshielding": 0,
            "name": "",
            "visual": "vis_optic_1K13",
            "armorcomponent": "Hit_Optic_1K13",
            "passthrough": 0
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|HitPoints|Hit_Optic_TKN3 [Indent level: 2],
        "hit_optic_tkn3": {
            "armor": -40,
            "explosionshielding": 0,
            "name": "",
            "visual": "vis_optic_TKN3",
            "armorcomponent": "Hit_Optic_TKN3",
            "passthrough": 0
        }
    },
    # Class: CfgVehicles|rhs_t90_tv|Damage [Indent level: 1],
    "damage": {
        "tex": [],
        "mat": ["rhsafrf|addons|rhs_t72|data|periscope.rvmat","rhsafrf|addons|rhs_t72|data|periscope_damage.rvmat","rhsafrf|addons|rhs_t72|data|periscope_destroyed.rvmat","rhsafrf|addons|rhs_t72|data|rhs_t90a_02.rvmat","rhsafrf|addons|rhs_t72|data|rhs_dam_t90a_02.rvmat","rhsafrf|addons|rhs_t72|data|rhs_destr_t90a_02.rvmat","rhsafrf|addons|rhs_t72|data|rhs_t90parts.rvmat","rhsafrf|addons|rhs_t72|data|rhs_dam_t90parts.rvmat","rhsafrf|addons|rhs_t72|data|rhs_destr_t90parts.rvmat","rhsafrf|addons|rhs_t72|data|rhs_dazzler.rvmat","rhsafrf|addons|rhs_t72|data|rhs_dam_dazzler.rvmat","rhsafrf|addons|rhs_t72|data|rhs_destr_dazzler.rvmat","rhsafrf|addons|rhs_t72|data|rhs_t72b_01.rvmat","rhsafrf|addons|rhs_t72|data|rhs_dam_t72b_01.rvmat","rhsafrf|addons|rhs_t72|data|rhs_destr_t72b_01.rvmat","rhsafrf|addons|rhs_t72|data|rhs_t72b_02.rvmat","rhsafrf|addons|rhs_t72|data|rhs_dam_t72b_02.rvmat","rhsafrf|addons|rhs_t72|data|rhs_destr_t72b_02.rvmat","rhsafrf|addons|rhs_t72|data|rhs_t72b_03.rvmat","rhsafrf|addons|rhs_t72|data|rhs_dam_t72b_03.rvmat","rhsafrf|addons|rhs_t72|data|rhs_destr_t72b_03.rvmat","rhsafrf|addons|rhs_t72|data|rhs_t72b_04.rvmat","rhsafrf|addons|rhs_t72|data|rhs_dam_t72b_04.rvmat","rhsafrf|addons|rhs_t72|data|rhs_destr_t72b_04.rvmat","rhsafrf|addons|rhs_t72|data|rhs_t72b_05.rvmat","rhsafrf|addons|rhs_t72|data|rhs_dam_t72b_05.rvmat","rhsafrf|addons|rhs_t72|data|rhs_destr_t72b_05.rvmat","rhsafrf|addons|rhs_t72|data|rhs_t72c_tracks.rvmat","rhsafrf|addons|rhs_t72|data|rhs_dam_t72c_tracks.rvmat","rhsafrf|addons|rhs_t72|data|rhs_destr_t72c_tracks.rvmat","rhsafrf|addons|rhs_t72|data|rhs_t72b3_01.rvmat","rhsafrf|addons|rhs_t72|data|rhs_dam_t72b3_01.rvmat","rhsafrf|addons|rhs_t72|data|rhs_destr_t72b3_01.rvmat","rhsafrf|addons|rhs_t72|data|rhs_t72b3_02.rvmat","rhsafrf|addons|rhs_t72|data|rhs_dam_t72b3_02.rvmat","rhsafrf|addons|rhs_t72|data|rhs_destr_t72b3_02.rvmat","rhsafrf|addons|rhs_t72|data|rhs_t72b3_turret.rvmat","rhsafrf|addons|rhs_t72|data|rhs_dam_t72b3_turret.rvmat","rhsafrf|addons|rhs_t72|data|rhs_destr_t72b3_turret.rvmat","rhsafrf|addons|rhs_t80|data|materials|turret_A.rvmat","rhsafrf|addons|rhs_t80|data|materials|turret_A.rvmat","rhsafrf|addons|rhs_t80|data|materials|turret_destroy.rvmat","rhsafrf|addons|rhs_bmd_34|data|rhs_bmd4_02.rvmat","rhsafrf|addons|rhs_bmd_34|data|rhs_dam_bmd4_02.rvmat","rhsafrf|addons|rhs_bmd_34|data|rhs_destr_bmd4_02.rvmat","a3|data_f|default.rvmat","a3|data_f|default.rvmat","a3|data_f|default_destruct.rvmat"]
    },
    # Class: CfgVehicles|rhs_t90_tv|UserActions [Indent level: 1],
    "useractions": {
    },
    "enablemanualfire": 1,
    # Class: CfgVehicles|rhs_t72bd_tv|Attributes [Indent level: 1],
    "attributes": {
        # Class: CfgVehicles|rhs_t72bd_tv|Attributes|ObjectTexture [Indent level: 2]
        "objecttexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayname": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        # Class: CfgVehicles|rhs_t72bd_tv|Attributes|rhs_decalNumber_type [Indent level: 2],
        "rhs_decalnumber_type": {
            "displayname": "Define font type of plate number",
            "tooltip": "Define kind of font that will be drawn on vehicle.",
            "property": "rhs_decalNumber_type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];[_this,[['Number', cRHST72NumberPlaces, _value]]] call rhs_fnc_decalsInit",
            "defaultvalue": 0,
            "typename": "STRING",
            # Class: CfgVehicles|rhs_a3t72tank_base|Attributes|rhs_decalNumber_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_a3t72tank_base|Attributes|rhs_decalNumber_type|values|Default [Indent level: 4]
                "default": {
                    "name": "Default",
                    "value": "Default",
                    "defaultvalue": "Default"
                },
                # Class: CfgVehicles|rhs_a3t72tank_base|Attributes|rhs_decalNumber_type|values|DefaultRed [Indent level: 4],
                "defaultred": {
                    "name": "Default (Red)",
                    "value": "DefaultRed"
                },
                # Class: CfgVehicles|rhs_a3t72tank_base|Attributes|rhs_decalNumber_type|values|BoldRed [Indent level: 4],
                "boldred": {
                    "name": "Bold Red",
                    "value": "BoldRed"
                },
                # Class: CfgVehicles|rhs_a3t72tank_base|Attributes|rhs_decalNumber_type|values|CDF [Indent level: 4],
                "cdf": {
                    "name": "CDF",
                    "value": "CDF"
                },
                # Class: CfgVehicles|rhs_a3t72tank_base|Attributes|rhs_decalNumber_type|values|Handpaint [Indent level: 4],
                "handpaint": {
                    "name": "Handpaint",
                    "value": "Handpaint"
                },
                # Class: CfgVehicles|rhs_a3t72tank_base|Attributes|rhs_decalNumber_type|values|HandpaintBlack [Indent level: 4],
                "handpaintblack": {
                    "name": "Handpaint Black",
                    "value": "HandpaintBlack"
                },
                # Class: CfgVehicles|rhs_a3t72tank_base|Attributes|rhs_decalNumber_type|values|Iraqi [Indent level: 4],
                "iraqi": {
                    "name": "Iraqi",
                    "value": "Iraqi"
                },
                # Class: CfgVehicles|rhs_a3t72tank_base|Attributes|rhs_decalNumber_type|values|LicensePlate [Indent level: 4],
                "licenseplate": {
                    "name": "License Plate",
                    "value": "LicensePlate"
                }
            }
        },
        # Class: CfgVehicles|rhs_t72bd_tv|Attributes|rhs_decalNumber [Indent level: 2],
        "rhs_decalnumber": {
            "collapsed": 1,
            "displayname": "Set side number",
            "tooltip": "Set side number. 3 numbers are required. Type 0 to hide numbers complety & leave at -1 to get random number",
            "property": "rhs_decalNumber",
            "control": "Edit",
            "validate": "Number",
            "typename": "Number",
            "defaultvalue": "-1",
            "expression": "if( _value >= 0)then{if( _value == 0)then{{[_this setobjectTexture [_x,'a3|data_f|clear_empty.paa']]}foreach cRHST72NumberPlaces}else{[_this, [['Number', cRHST72NumberPlaces, _this getVariable ['rhs_decalNumber_type','Default'], _value] ] ] call rhs_fnc_decalsInit}};"
        },
        # Class: CfgVehicles|rhs_t72bd_tv|Attributes|rhs_decalPlatoon_type [Indent level: 2],
        "rhs_decalplatoon_type": {
            "displayname": "Define platoon symbol type",
            "tooltip": "Decal type",
            "property": "rhs_decalPlatoon_type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": "0",
            "typename": "STRING",
            # Class: CfgVehicles|rhs_a3t72tank_base|Attributes|rhs_decalPlatoon_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_a3t72tank_base|Attributes|rhs_decalPlatoon_type|values|Platoon [Indent level: 4]
                "platoon": {
                    "name": "Platoon",
                    "value": "Platoon"
                },
                # Class: CfgVehicles|rhs_a3t72tank_base|Attributes|rhs_decalPlatoon_type|values|PlatoonGDR [Indent level: 4],
                "platoongdr": {
                    "name": "Platoon GDR",
                    "value": "PlatoonGDR"
                },
                # Class: CfgVehicles|rhs_a3t72tank_base|Attributes|rhs_decalPlatoon_type|values|PlatoonVDV [Indent level: 4],
                "platoonvdv": {
                    "name": "Platoon VDV",
                    "value": "PlatoonVDV"
                },
                # Class: CfgVehicles|rhs_a3t72tank_base|Attributes|rhs_decalPlatoon_type|values|Army [Indent level: 4],
                "army": {
                    "name": "Army",
                    "value": "Army",
                    "defaultvalue": "1"
                },
                # Class: CfgVehicles|rhs_a3t72tank_base|Attributes|rhs_decalPlatoon_type|values|Honor [Indent level: 4],
                "honor": {
                    "name": "Honor",
                    "value": "Honor",
                    "defaultvalue": "0"
                },
                # Class: CfgVehicles|rhs_a3t72tank_base|Attributes|rhs_decalPlatoon_type|values|HonorGDR [Indent level: 4],
                "honorgdr": {
                    "name": "Honor GDR",
                    "value": "HonorGDR"
                }
            }
        },
        # Class: CfgVehicles|rhs_t72bd_tv|Attributes|rhs_decalPlatoon [Indent level: 2],
        "rhs_decalplatoon": {
            "displayname": "Set platoon symbol",
            "tooltip": "Set platoon symbol located on turret. Usually used for platoon symbols. -1 leaves current symbol & 0 clears decal.",
            "property": "rhs_decalPlatoon",
            "control": "Edit",
            "validate": "none",
            "defaultvalue": "-1",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', cRHST72PlnSymPlaces,  _this getVariable ['rhs_decalPlatoon_type','Platoon'],call compile _value] ] ] call rhs_fnc_decalsInit};"
        },
        # Class: CfgVehicles|rhs_t72bd_tv|Attributes|rhs_ammoslot_1_type [Indent level: 2],
        "rhs_ammoslot_1_type": {
            # Class: CfgVehicles|rhs_t72bd_tv|Attributes|rhs_ammoslot_1_type|values [Indent level: 3]
            "values": {
                # Class: CfgVehicles|rhs_t72bd_tv|Attributes|rhs_ammoslot_1_type|values|rhs_mag_3bm46_10 [Indent level: 4]
                "rhs_mag_3bm46_10": {
                    "name": "APFSDS-T 3BM46",
                    "value": "rhs_mag_3bm46",
                    "defaultvalue": "rhs_mag_3bm46"
                },
                # Class: CfgVehicles|rhs_t72bd_tv|Attributes|rhs_ammoslot_1_type|values|rhs_mag_3bm9_10 [Indent level: 4],
                "rhs_mag_3bm9_10": {
                    "name": "APFSDS-T 3BM9",
                    "value": "rhs_mag_3bm9",
                    "defaultvalue": "rhs_mag_3bm9"
                },
                # Class: CfgVehicles|rhs_t72bd_tv|Attributes|rhs_ammoslot_1_type|values|rhs_mag_3bm12_10 [Indent level: 4],
                "rhs_mag_3bm12_10": {
                    "name": "APFSDS-T 3BM12",
                    "value": "rhs_mag_3bm12",
                    "defaultvalue": "rhs_mag_3bm12"
                },
                # Class: CfgVehicles|rhs_t72bd_tv|Attributes|rhs_ammoslot_1_type|values|rhs_mag_3bm15_10 [Indent level: 4],
                "rhs_mag_3bm15_10": {
                    "name": "APFSDS-T 3BM15",
                    "value": "rhs_mag_3bm15",
                    "defaultvalue": "rhs_mag_3bm15"
                },
                # Class: CfgVehicles|rhs_t72bd_tv|Attributes|rhs_ammoslot_1_type|values|rhs_mag_3bm17_10 [Indent level: 4],
                "rhs_mag_3bm17_10": {
                    "name": "APFSDS-T 3BM17",
                    "value": "rhs_mag_3bm17",
                    "defaultvalue": "rhs_mag_3bm17"
                },
                # Class: CfgVehicles|rhs_t72bd_tv|Attributes|rhs_ammoslot_1_type|values|rhs_mag_3bm22_10 [Indent level: 4],
                "rhs_mag_3bm22_10": {
                    "name": "APFSDS-T 3BM22",
                    "value": "rhs_mag_3bm22",
                    "defaultvalue": "rhs_mag_3bm22"
                },
                # Class: CfgVehicles|rhs_t72bd_tv|Attributes|rhs_ammoslot_1_type|values|rhs_mag_3bm29_10 [Indent level: 4],
                "rhs_mag_3bm29_10": {
                    "name": "APFSDS-T 3BM29",
                    "value": "rhs_mag_3bm29",
                    "defaultvalue": "rhs_mag_3bm29"
                },
                # Class: CfgVehicles|rhs_t72bd_tv|Attributes|rhs_ammoslot_1_type|values|rhs_mag_3bm26_10 [Indent level: 4],
                "rhs_mag_3bm26_10": {
                    "name": "APFSDS-T 3BM26",
                    "value": "rhs_mag_3bm26",
                    "defaultvalue": "rhs_mag_3bm26"
                },
                # Class: CfgVehicles|rhs_t72bd_tv|Attributes|rhs_ammoslot_1_type|values|rhs_mag_3bm32_10 [Indent level: 4],
                "rhs_mag_3bm32_10": {
                    "name": "APFSDS-T 3BM32",
                    "value": "rhs_mag_3bm32",
                    "defaultvalue": "rhs_mag_3bm32"
                },
                # Class: CfgVehicles|rhs_t72bd_tv|Attributes|rhs_ammoslot_1_type|values|rhs_mag_3bm42_10 [Indent level: 4],
                "rhs_mag_3bm42_10": {
                    "name": "APFSDS-T 3BM42",
                    "value": "rhs_mag_3bm42",
                    "defaultvalue": "rhs_mag_3bm42"
                },
                # Class: CfgVehicles|rhs_t72bd_tv|Attributes|rhs_ammoslot_1_type|values|rhs_mag_3bm42m_10 [Indent level: 4],
                "rhs_mag_3bm42m_10": {
                    "name": "APFSDS-T 3BM42M",
                    "value": "rhs_mag_3bm42m",
                    "defaultvalue": "rhs_mag_3bm42m"
                }
            },
            "displayname": "Ammo slot #1 type",
            "tooltip": "Define type of shell for #1 slot [AP rounds]",
            "property": "rhs_ammoslot_1_type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": 0,
            "typename": "STRING"
        },
        # Class: CfgVehicles|rhs_t72bd_tv|Attributes|rhs_ammoslot_1 [Indent level: 2],
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
        # Class: CfgVehicles|rhs_t72bd_tv|Attributes|rhs_ammoslot_2_type [Indent level: 2],
        "rhs_ammoslot_2_type": {
            # Class: CfgVehicles|rhs_t72bd_tv|Attributes|rhs_ammoslot_2_type|values [Indent level: 3]
            "values": {
                # Class: CfgVehicles|rhs_t72bd_tv|Attributes|rhs_ammoslot_2_type|values|rhs_mag_3bk31_8 [Indent level: 4]
                "rhs_mag_3bk31_8": {
                    "name": "HEAT-FS 3BK31",
                    "value": "rhs_mag_3bk31",
                    "defaultvalue": "rhs_mag_3bk31"
                },
                # Class: CfgVehicles|rhs_t72bd_tv|Attributes|rhs_ammoslot_2_type|values|rhs_mag_3bk12_8 [Indent level: 4],
                "rhs_mag_3bk12_8": {
                    "name": "HEAT-FS 3BK12",
                    "value": "rhs_mag_3bk12",
                    "defaultvalue": "rhs_mag_3bk12"
                },
                # Class: CfgVehicles|rhs_t72bd_tv|Attributes|rhs_ammoslot_2_type|values|rhs_mag_3bk14_8 [Indent level: 4],
                "rhs_mag_3bk14_8": {
                    "name": "HEAT-FS 3BK14",
                    "value": "rhs_mag_3bk14",
                    "defaultvalue": "rhs_mag_3bk14"
                },
                # Class: CfgVehicles|rhs_t72bd_tv|Attributes|rhs_ammoslot_2_type|values|rhs_mag_3bk18_8 [Indent level: 4],
                "rhs_mag_3bk18_8": {
                    "name": "HEAT-FS 3BK18",
                    "value": "rhs_mag_3bk18",
                    "defaultvalue": "rhs_mag_3bk18"
                },
                # Class: CfgVehicles|rhs_t72bd_tv|Attributes|rhs_ammoslot_2_type|values|rhs_mag_3bk18m_8 [Indent level: 4],
                "rhs_mag_3bk18m_8": {
                    "name": "HEAT-FS 3BK18M",
                    "value": "rhs_mag_3bk18m",
                    "defaultvalue": "rhs_mag_3bk18m"
                },
                # Class: CfgVehicles|rhs_t72bd_tv|Attributes|rhs_ammoslot_2_type|values|rhs_mag_3bk21_8 [Indent level: 4],
                "rhs_mag_3bk21_8": {
                    "name": "HEAT-FS 3BK21",
                    "value": "rhs_mag_3bk21",
                    "defaultvalue": "rhs_mag_3bk21"
                },
                # Class: CfgVehicles|rhs_t72bd_tv|Attributes|rhs_ammoslot_2_type|values|rhs_mag_3bk29_8 [Indent level: 4],
                "rhs_mag_3bk29_8": {
                    "name": "HEAT-FS 3BK29",
                    "value": "rhs_mag_3bk29",
                    "defaultvalue": "rhs_mag_3bk29"
                }
            },
            "displayname": "Ammo slot #2 type",
            "tooltip": "Define type of shell for #2 slot [HEAT rounds]",
            "property": "rhs_ammoslot_2_type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": 0,
            "typename": "STRING"
        },
        # Class: CfgVehicles|rhs_t72bd_tv|Attributes|rhs_ammoslot_2 [Indent level: 2],
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
        # Class: CfgVehicles|rhs_t72bd_tv|Attributes|rhs_ammoslot_3_type [Indent level: 2],
        "rhs_ammoslot_3_type": {
            # Class: CfgVehicles|rhs_t72bd_tv|Attributes|rhs_ammoslot_3_type|values [Indent level: 3]
            "values": {
                # Class: CfgVehicles|rhs_t72bd_tv|Attributes|rhs_ammoslot_3_type|values|rhs_mag_3of26_6 [Indent level: 4]
                "rhs_mag_3of26_6": {
                    "name": "HE-FRAG-FS 3OF26",
                    "value": "rhs_mag_3of26",
                    "defaultvalue": "rhs_mag_3of26"
                },
                # Class: CfgVehicles|rhs_t72bd_tv|Attributes|rhs_ammoslot_3_type|values|rhs_mag_3of11_6 [Indent level: 4],
                "rhs_mag_3of11_6": {
                    "name": "HE-FRAG-FS 3OF11",
                    "value": "rhs_mag_3of11",
                    "defaultvalue": "rhs_mag_3of11"
                }
            },
            "displayname": "Ammo slot #3 type",
            "tooltip": "Define type of shell for #3 slot [HE rounds]",
            "property": "rhs_ammoslot_3_type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": 0,
            "typename": "STRING"
        },
        # Class: CfgVehicles|rhs_t72bd_tv|Attributes|rhs_ammoslot_3 [Indent level: 2],
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
        # Class: CfgVehicles|rhs_t72bd_tv|Attributes|rhs_ammoslot_4_type [Indent level: 2],
        "rhs_ammoslot_4_type": {
            # Class: CfgVehicles|rhs_t72bd_tv|Attributes|rhs_ammoslot_4_type|values [Indent level: 3]
            "values": {
                # Class: CfgVehicles|rhs_t72bd_tv|Attributes|rhs_ammoslot_4_type|values|rhs_mag_9m119m_6 [Indent level: 4]
                "rhs_mag_9m119m_6": {
                    "name": "ATGM 9M119M",
                    "value": "rhs_mag_9m119m",
                    "defaultvalue": "rhs_mag_9m119m"
                },
                # Class: CfgVehicles|rhs_t72bd_tv|Attributes|rhs_ammoslot_4_type|values|rhs_mag_9m119_6 [Indent level: 4],
                "rhs_mag_9m119_6": {
                    "name": "ATGM 9M119",
                    "value": "rhs_mag_9m119",
                    "defaultvalue": "rhs_mag_9m119"
                },
                # Class: CfgVehicles|rhs_t72bd_tv|Attributes|rhs_ammoslot_4_type|values|rhs_mag_9m119f_6 [Indent level: 4],
                "rhs_mag_9m119f_6": {
                    "name": "ATGM 9M119F",
                    "value": "rhs_mag_9m119f",
                    "defaultvalue": "rhs_mag_9m119f"
                }
            },
            "displayname": "Ammo slot #4 type",
            "tooltip": "Define type of shell for #4 slot [ATGM rounds]",
            "property": "rhs_ammoslot4_type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": 0,
            "typename": "STRING"
        },
        # Class: CfgVehicles|rhs_t72bd_tv|Attributes|rhs_ammoslot_4 [Indent level: 2],
        "rhs_ammoslot_4": {
            "displayname": "Ammo slot #4 count",
            "tooltip": "Define number of rounds stored inside of type #4. Max 22. Leave -1 for default loadout",
            "property": "rhs_ammoslot_4",
            "control": "Edit",
            "expression": "if(_value >= 0)then{ [_this,_value,'%s',22] spawn rhs_fnc_TTanks_DefineLoadout};",
            "defaultvalue": "-1",
            "validate": "NUMBER",
            "typename": "NUMBER"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Attributes|rhs_decalHonor_type [Indent level: 2],
        "rhs_decalhonor_type": {
            "displayname": "Define honor symbol type",
            "property": "rhs_decalHonor_type",
            # Class: CfgVehicles|rhs_a3t72tank_base|Attributes|rhs_decalHonor_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_a3t72tank_base|Attributes|rhs_decalHonor_type|values|Honor [Indent level: 4]
                "honor": {
                    "name": "Honor",
                    "value": "Honor",
                    "defaultvalue": "0"
                },
                # Class: CfgVehicles|rhs_a3t72tank_base|Attributes|rhs_decalHonor_type|values|HonorGDR [Indent level: 4],
                "honorgdr": {
                    "name": "Honor GDR",
                    "value": "HonorGDR"
                },
                # Class: CfgVehicles|rhs_a3t72tank_base|Attributes|rhs_decalHonor_type|values|Platoon [Indent level: 4],
                "platoon": {
                    "name": "Platoon",
                    "value": "Platoon"
                },
                # Class: CfgVehicles|rhs_a3t72tank_base|Attributes|rhs_decalHonor_type|values|PlatoonGDR [Indent level: 4],
                "platoongdr": {
                    "name": "Platoon GDR",
                    "value": "PlatoonGDR"
                },
                # Class: CfgVehicles|rhs_a3t72tank_base|Attributes|rhs_decalHonor_type|values|PlatoonVDV [Indent level: 4],
                "platoonvdv": {
                    "name": "Platoon VDV",
                    "value": "PlatoonVDV"
                },
                # Class: CfgVehicles|rhs_a3t72tank_base|Attributes|rhs_decalHonor_type|values|Army [Indent level: 4],
                "army": {
                    "name": "Army",
                    "value": "Army",
                    "defaultvalue": "1"
                }
            },
            "tooltip": "Decal type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": "0",
            "typename": "STRING"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Attributes|rhs_decalHonor [Indent level: 2],
        "rhs_decalhonor": {
            "displayname": "Set honor symbol",
            "tooltip": "Define symbol located on IR Lamp ('84-'89 type tanks only). Usually used for honor symbols. -1 leaves current symbol & 0 clears decal.",
            "property": "rhs_decalHonor",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', cRHST72HnrSymPlaces,  _this getVariable ['rhs_decalHonor_type','Honor'],call compile _value] ] ] call rhs_fnc_decalsInit};",
            "control": "Edit",
            "validate": "none",
            "defaultvalue": "-1"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Attributes|rhs_hide_com_shield [Indent level: 2],
        "rhs_hide_com_shield": {
            "displayname": "Remove commander shield",
            "property": "rhs_hide_com_shield",
            "control": "CheckboxNumber",
            "expression": "_this animate ['hide_com_shield',_value,true]",
            "defaultvalue": "0"
        }
    },
    "dlc": "RHS_AFRF",
    "rhs_decalparameters": ["['Number',cRHST72NumberPlaces,'Default']","['Label',cRHST72PlnSymPlaces, 'Platoon',8]"],
    "category": "Armored",
    "allowtablock": 0,
    "destrtype": "DestructDefault",
    "driveoncomponent": ["Track_L","Track_R","Slide"],
    "vehicleclass": "rhs_vehclass_tank",
    "editorsubcategory": "rhs_EdSubcat_tank",
    "accuracy": 0.3,
    "supplyradius": 1,
    "memorypointsupply": "pos driver",
    "icon": "rhsafrf|addons|rhs_t72|data|icomap_t72_CA.paa",
    "mapsize": 9.5,
    "tf_range_api": 45000,
    "irtarget": 1,
    "irtargetsize": 1,
    "visualtarget": 1,
    "visualtargetsize": 0.7,
    "radartarget": 1,
    "radartargetsize": 1.1,
    "precision": 1,
    "typicalcargo": [],
    "side": 0,
    "faction": "rhs_faction_tv",
    "drivercansee": "2+4+8",
    "gunnercansee": "2+4+8",
    "commandercansee": "2+4+8",
    "incomingmissiledetectionsystem": 0,
    "getinaction": "GetInLow",
    "getoutaction": "GetOutLow",
    "driveraction": "driver_apcwheeled2_out",
    "driverinaction": "rhs_t72_driver",
    "driverdoor": "hatchD",
    "driveropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tvn5.p3d",
    "loddriverturnedin": 0,
    "loddriverturnedout": 0,
    "loddriveropticsin": 0,
    # Class: CfgVehicles|rhs_a3t72tank_base|DriverOpticsIn [Indent level: 1],
    "driveropticsin": {
        # Class: CfgVehicles|rhs_a3t72tank_base|DriverOpticsIn|OpticView [Indent level: 2]
        "opticview": {
            "opticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tvn5",
            "hitpoint": "Hit_Optic_Driver",
            "initfov": 0.7,
            "minfov": 0.7,
            "maxfov": 0.7,
            "initanglex": 7,
            "initangley": 0,
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
        }
    },
    "weapons": ["rhs_weap_smokegen"],
    "magazines": ["rhs_mag_smokegen"],
    "soundgetin": ["A3|Sounds_F_EPB|Tracked|noises|get_in_out",0.562341,1],
    "soundgetout": ["A3|Sounds_F_EPB|Tracked|noises|get_in_out",0.562341,1,20],
    "sounddammage": ["",0.562341,1],
    "soundengineonint": ["rhsafrf|addons|rhs_vehiclesounds|sounds|armor|t72|t72_engine_ext_startup",0.562341,1],
    "soundengineonext": ["rhsafrf|addons|rhs_vehiclesounds|sounds|armor|t72|t72_engine_ext_shutdown",6.30957,1,100],
    "soundengineoffint": ["rhsafrf|addons|rhs_vehiclesounds|sounds|armor|t72|t72_engine_ext_shutdown",0.562341,1],
    "soundengineoffext": ["rhsafrf|addons|rhs_vehiclesounds|sounds|armor|t72|t72_engine_ext_startup",6.30957,1,100],
    "buildcrash0": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_01",3.16228,1,200],
    "buildcrash1": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_02",3.16228,1,200],
    "buildcrash2": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_03",3.16228,1,200],
    "buildcrash3": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_04",3.16228,1,200],
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
    "soundarmorcrash": ["ArmorCrash0",0.166,"ArmorCrash1",0.166,"ArmorCrash2",0.166,"ArmorCrash3",0.166,"ArmorCrash4",0.166,"ArmorCrash5",0.166],
    # Class: CfgVehicles|rhs_a3t72tank_base|Sounds [Indent level: 1],
    "sounds": {
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|Idle_ext [Indent level: 2]
        "idle_ext": {
            "sound": ["rhsafrf|addons|rhs_t72|sounds|T72_outside-d_idle1","3.5*0.79432821",1,200],
            "frequency": "0.95	+	((rpm/	2340) factor[(400*1.57/	2340),(900*1.57/	2340)])*0.15",
            "volume": "engineOn*camPos*(((rpm/	2340) factor[(100*1.57/	2340),(200*1.57/	2340)])	*	((rpm/	2340) factor[(900*1.57/	2340),(700*1.57/	2340)]))"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|Engine [Indent level: 2],
        "engine": {
            "sound": ["rhsafrf|addons|rhs_t72|sounds|T72_outside-m_low1","3.5*0.89125091",1,340],
            "frequency": "0.8	+	((rpm/	2340) factor[(700*1.57/	2340),(1100*1.57/	2340)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	2340) factor[(705*1.57/	2340),(850*1.57/	2340)])	*	((rpm/	2340) factor[(1100 *1.57/	2340),(950*1.57/	2340)]))"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|Engine1_ext [Indent level: 2],
        "engine1_ext": {
            "sound": ["rhsafrf|addons|rhs_t72|sounds|T72_outside-m_low1","3.5*1.1220185",1,380],
            "frequency": "0.8	+	((rpm/	2340) factor[(950*1.57/	2340),(1400*1.57/	2340)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	2340) factor[(900*1.57/	2340),(1050*1.57/	2340)])	*	((rpm/	2340) factor[(1400*1.57/	2340),(1200*1.57/	2340)]))"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|Engine2_ext [Indent level: 2],
        "engine2_ext": {
            "sound": ["rhsafrf|addons|rhs_t72|sounds|T72_outside-m_low1","3.5*1.2589254",1,420],
            "frequency": "0.8	+	((rpm/	2340) factor[(1200*1.57/	2340),(1700*1.57/	2340)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	2340) factor[(1170*1.57/	2340),(1380*1.57/	2340)])	*	((rpm/	2340) factor[(1700*1.57/	2340),(1500*1.57/	2340)]))"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|Engine3_ext [Indent level: 2],
        "engine3_ext": {
            "sound": ["rhsafrf|addons|rhs_t72|sounds|T72_outside-m_high1","3.5*1.4125376",1,460],
            "frequency": "0.8	+	((rpm/	2340) factor[(1500*1.57/	2340),(2100*1.57/	2340)])*0.1",
            "volume": "engineOn*camPos*(((rpm/	2340) factor[(1500*1.57/	2340),(1670*1.57/	2340)])	*	((rpm/	2340) factor[(2100*1.57/	2340),(1800*1.57/	2340)]))"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|Engine4_ext [Indent level: 2],
        "engine4_ext": {
            "sound": ["rhsafrf|addons|rhs_t72|sounds|T72_outside-m_high1","3.5*1.5848932",1,500],
            "frequency": "0.8	+	((rpm/	2340) factor[(1800*1.57/	2340),(2300*1.57/	2340)])*0.1",
            "volume": "engineOn*camPos*(((rpm/	2340) factor[(1780*1.57/	2340),(2060*1.57/	2340)])	*	((rpm/	2340) factor[(2450*1.57/	2340),(2200*1.57/	2340)]))"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|Engine5_ext [Indent level: 2],
        "engine5_ext": {
            "sound": ["rhsafrf|addons|rhs_t72|sounds|T72_outside-m_high1","3.5*1.7782794",1,540],
            "frequency": "0.8	+	((rpm/	2340) factor[(2100*1.57/	2340),(2340*1.57/	2340)])*0.1",
            "volume": "engineOn*camPos*((rpm/	2340) factor[(2150*1.57/	2340),(2500*1.57/	2340)])"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|IdleThrust [Indent level: 2],
        "idlethrust": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_01|MBT1_exhaust_ext_rpm1","3.5*1.1220185",1,200],
            "frequency": "0.8	+	((rpm/	2340) factor[(400*1.57/	2340),(900*1.57/	2340)])*0.15",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	2340) factor[(100*1.57/	2340),(200*1.57/	2340)])	*	((rpm/	2340) factor[(900*1.57/	2340),(700*1.57/	2340)]))"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|EngineThrust [Indent level: 2],
        "enginethrust": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_01|MBT1_exhaust_ext_rpm2","3*1.4125376",1,200],
            "frequency": "0.8	+	((rpm/	2340) factor[(700*1.57/	2340),(1100*1.57/	2340)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	2340) factor[(705*1.57/	2340),(850*1.57/	2340)])	*	((rpm/	2340) factor[(1100 *1.57/	2340),(950*1.57/	2340)]))"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|Engine1_Thrust_ext [Indent level: 2],
        "engine1_thrust_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_01|MBT1_exhaust_ext_rpm3","3*1.7782794",1,230],
            "frequency": "0.8	+	((rpm/	2340) factor[(950*1.57/	2340),(1400*1.57/	2340)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	2340) factor[(900*1.57/	2340),(1050*1.57/	2340)])	*	((rpm/	2340) factor[(1400*1.57/	2340),(1200*1.57/	2340)]))"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|Engine2_Thrust_ext [Indent level: 2],
        "engine2_thrust_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_01|MBT1_exhaust_ext_rpm4","3*1.9952624",1,290],
            "frequency": "0.8	+	((rpm/	2340) factor[(1200*1.57/	2340),(1700*1.57/	2340)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	2340) factor[(1170*1.57/	2340),(1380*1.57/	2340)])	*	((rpm/	2340) factor[(1700*1.57/	2340),(1500*1.57/	2340)]))"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|Engine3_Thrust_ext [Indent level: 2],
        "engine3_thrust_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_01|MBT1_exhaust_ext_rpm5","3*1.7782794",1,350],
            "frequency": "0.8	+	((rpm/	2340) factor[(1500*1.57/	2340),(2100*1.57/	2340)])*0.1",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	2340) factor[(1500*1.57/	2340),(1670*1.57/	2340)])	*	((rpm/	2340) factor[(2100*1.57/	2340),(1800*1.57/	2340)]))"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|Engine4_Thrust_ext [Indent level: 2],
        "engine4_thrust_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_01|MBT1_exhaust_ext_rpm6","3*2.2387211",1,400],
            "frequency": "0.8	+	((rpm/	2340) factor[(1800*1.57/	2340),(2300*1.57/	2340)])*0.1",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	2340) factor[(1780*1.57/	2340),(2060*1.57/	2340)])	*	((rpm/	2340) factor[(2450*1.57/	2340),(2200*1.57/	2340)]))"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|Engine5_Thrust_ext [Indent level: 2],
        "engine5_thrust_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_01|MBT1_exhaust_ext_rpm7","3*2.5118864",1,450],
            "frequency": "0.8	+	((rpm/	2340) factor[(2100*1.57/	2340),(2340*1.57/	2340)])*0.1",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*((rpm/	2340) factor[(2150*1.57/	2340),(2500*1.57/	2340)])"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|Idle_int [Indent level: 2],
        "idle_int": {
            "sound": ["rhsafrf|addons|rhs_t72|sounds|T72_inside_idle1","3*0.50118721",1],
            "frequency": "0.8	+	((rpm/	2340) factor[(400*1.57/	2340),(900*1.57/	2340)])*0.15",
            "volume": "engineOn*(1-camPos)*(((rpm/	2340) factor[(100*1.57/	2340),(200*1.57/	2340)])	*	((rpm/	2340) factor[(900*1.57/	2340),(700*1.57/	2340)]))"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|Engine_int [Indent level: 2],
        "engine_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_01|MBT1_engine_int_rpm2",0.354813,1],
            "frequency": "0.8	+	((rpm/	2340) factor[(700*1.57/	2340),(1100*1.57/	2340)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	2340) factor[(705*1.57/	2340),(850*1.57/	2340)])	*	((rpm/	2340) factor[(1100 *1.57/	2340),(950*1.57/	2340)]))"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|Engine1_int [Indent level: 2],
        "engine1_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_01|MBT1_engine_int_rpm3",0.398107,1],
            "frequency": "0.8	+	((rpm/	2340) factor[(950*1.57/	2340),(1400*1.57/	2340)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	2340) factor[(900*1.57/	2340),(1050*1.57/	2340)])	*	((rpm/	2340) factor[(1400*1.57/	2340),(1200*1.57/	2340)]))"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|Engine2_int [Indent level: 2],
        "engine2_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_01|MBT1_engine_int_rpm4",0.446684,1],
            "frequency": "0.8	+	((rpm/	2340) factor[(1200*1.57/	2340),(1700*1.57/	2340)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	2340) factor[(1170*1.57/	2340),(1380*1.57/	2340)])	*	((rpm/	2340) factor[(1700*1.57/	2340),(1500*1.57/	2340)]))"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|Engine3_int [Indent level: 2],
        "engine3_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_01|MBT1_engine_int_rpm5",0.501187,1],
            "frequency": "0.8	+	((rpm/	2340) factor[(1500*1.57/	2340),(2100*1.57/	2340)])*0.1",
            "volume": "engineOn*(1-camPos)*(((rpm/	2340) factor[(1500*1.57/	2340),(1670*1.57/	2340)])	*	((rpm/	2340) factor[(2100*1.57/	2340),(1800*1.57/	2340)]))"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|Engine4_int [Indent level: 2],
        "engine4_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_01|MBT1_engine_int_rpm6",0.562341,1],
            "frequency": "0.8	+	((rpm/	2340) factor[(1800*1.57/	2340),(2300*1.57/	2340)])*0.1",
            "volume": "engineOn*(1-camPos)*(((rpm/	2340) factor[(1780*1.57/	2340),(2060*1.57/	2340)])	*	((rpm/	2340) factor[(2450*1.57/	2340),(2200*1.57/	2340)]))"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|Engine5_int [Indent level: 2],
        "engine5_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_01|MBT1_engine_int_rpm7",0.630957,1],
            "frequency": "0.8	+	((rpm/	2340) factor[(2100*1.57/	2340),(2340*1.57/	2340)])*0.1",
            "volume": "engineOn*(1-camPos)*((rpm/	2340) factor[(2150*1.57/	2340),(2500*1.57/	2340)])"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|IdleThrust_int [Indent level: 2],
        "idlethrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_01|MBT1_exhaust_int_rpm1",0.630957,1],
            "frequency": "0.8	+	((rpm/	2340) factor[(400*1.57/	2340),(900*1.57/	2340)])*0.15",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	2340) factor[(100*1.57/	2340),(200*1.57/	2340)])	*	((rpm/	2340) factor[(900*1.57/	2340),(700*1.57/	2340)]))"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|EngineThrust_int [Indent level: 2],
        "enginethrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_01|MBT1_exhaust_int_rpm2",0.398107,1],
            "frequency": "0.8	+	((rpm/	2340) factor[(700*1.57/	2340),(1100*1.57/	2340)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	2340) factor[(705*1.57/	2340),(850*1.57/	2340)])	*	((rpm/	2340) factor[(1100 *1.57/	2340),(950*1.57/	2340)]))"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|Engine1_Thrust_int [Indent level: 2],
        "engine1_thrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_01|MBT1_exhaust_int_rpm3",0.446684,1],
            "frequency": "0.8	+	((rpm/	2340) factor[(950*1.57/	2340),(1400*1.57/	2340)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	2340) factor[(900*1.57/	2340),(1050*1.57/	2340)])	*	((rpm/	2340) factor[(1400*1.57/	2340),(1200*1.57/	2340)]))"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|Engine2_Thrust_int [Indent level: 2],
        "engine2_thrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_01|MBT1_exhaust_int_rpm4",0.446684,1],
            "frequency": "0.8	+	((rpm/	2340) factor[(1200*1.57/	2340),(1700*1.57/	2340)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	2340) factor[(1170*1.57/	2340),(1380*1.57/	2340)])	*	((rpm/	2340) factor[(1700*1.57/	2340),(1500*1.57/	2340)]))"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|Engine3_Thrust_int [Indent level: 2],
        "engine3_thrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_01|MBT1_exhaust_int_rpm5",0.501187,1],
            "frequency": "0.8	+	((rpm/	2340) factor[(1500*1.57/	2340),(2100*1.57/	2340)])*0.1",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	2340) factor[(1500*1.57/	2340),(1670*1.57/	2340)])	*	((rpm/	2340) factor[(2100*1.57/	2340),(1800*1.57/	2340)]))"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|Engine4_Thrust_int [Indent level: 2],
        "engine4_thrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_01|MBT1_exhaust_int_rpm6",0.562341,1],
            "frequency": "0.8	+	((rpm/	2340) factor[(1800*1.57/	2340),(2300*1.57/	2340)])*0.1",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	2340) factor[(1780*1.57/	2340),(2060*1.57/	2340)])	*	((rpm/	2340) factor[(2450*1.57/	2340),(2200*1.57/	2340)]))"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|Engine5_Thrust_int [Indent level: 2],
        "engine5_thrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_01|MBT1_exhaust_int_rpm7",0.630957,1],
            "frequency": "0.8	+	((rpm/	2340) factor[(2100*1.57/	2340),(2340*1.57/	2340)])*0.1",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*((rpm/	2340) factor[(2150*1.57/	2340),(2500*1.57/	2340)])"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|NoiseInt [Indent level: 2],
        "noiseint": {
            "sound": ["A3|sounds_f|vehicles|armor|noises|noise_tank_int_1",0.501187,1],
            "frequency": "1",
            "volume": "(1-camPos)*(angVelocity max 0.04)*(speed factor[4, 15])"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|NoiseExt [Indent level: 2],
        "noiseext": {
            "sound": ["A3|sounds_f|vehicles|armor|noises|noise_tank_ext_1",0.891251,1,50],
            "frequency": "1",
            "volume": "camPos*(angVelocity max 0.04)*(speed factor[4, 15])"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|ThreadsOutH0 [Indent level: 2],
        "threadsouth0": {
            "sound": ["rhsafrf|addons|rhs_t72|sounds|ext_treads_hard_01","3*0.39810717",1,140],
            "frequency": "1",
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-0) max 0)*1.57/	60),(((-5) max 5)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-15) max 15)*1.57/	60),(((-10) max 10)*1.57/	60)]))"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|ThreadsOutH1 [Indent level: 2],
        "threadsouth1": {
            "sound": ["rhsafrf|addons|rhs_t72|sounds|ext_treads_hard_02","3*0.44668359",1,160],
            "frequency": "1",
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-10) max 10)*1.57/	60),(((-15) max 15)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-30) max 30)*1.57/	60),(((-25) max 25)*1.57/	60)]))"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|ThreadsOutH2 [Indent level: 2],
        "threadsouth2": {
            "sound": ["rhsafrf|addons|rhs_t72|sounds|ext_treads_hard_03","3*0.50118721",1,180],
            "frequency": "1",
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-25) max 25)*1.57/	60),(((-30) max 30)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-45) max 45)*1.57/	60),(((-40) max 40)*1.57/	60)]))"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|ThreadsOutH3 [Indent level: 2],
        "threadsouth3": {
            "sound": ["rhsafrf|addons|rhs_t72|sounds|ext_treads_hard_04","3*0.56234133",1,200],
            "frequency": "1",
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-40) max 40)*1.57/	60),(((-45) max 45)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-55) max 55)*1.57/	60),(((-50) max 50)*1.57/	60)]))"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|ThreadsOutH4 [Indent level: 2],
        "threadsouth4": {
            "sound": ["rhsafrf|addons|rhs_t72|sounds|ext_treads_hard_05","3*0.56234133",1,220],
            "frequency": "1",
            "volume": "engineOn*camPos*(1-grass)*((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-49) max 49)*1.57/	60),(((-53) max 53)*1.57/	60)])"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|ThreadsOutS0 [Indent level: 2],
        "threadsouts0": {
            "sound": ["rhsafrf|addons|rhs_t72|sounds|ext_treads_soft_01","3*0.31622776",1,120],
            "frequency": "1",
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-0) max 0)*1.57/	60),(((-5) max 5)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-15) max 15)*1.57/	60),(((-10) max 10)*1.57/	60)]))"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|ThreadsOutS1 [Indent level: 2],
        "threadsouts1": {
            "sound": ["rhsafrf|addons|rhs_t72|sounds|ext_treads_soft_02","3*0.35481337",1,140],
            "frequency": "1",
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-10) max 10)*1.57/	60),(((-15) max 15)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-30) max 30)*1.57/	60),(((-25) max 25)*1.57/	60)]))"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|ThreadsOutS2 [Indent level: 2],
        "threadsouts2": {
            "sound": ["rhsafrf|addons|rhs_t72|sounds|ext_treads_soft_03","3*0.39810717",1,160],
            "frequency": "1",
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-25) max 25)*1.57/	60),(((-30) max 30)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-45) max 45)*1.57/	60),(((-40) max 40)*1.57/	60)]))"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|ThreadsOutS3 [Indent level: 2],
        "threadsouts3": {
            "sound": ["rhsafrf|addons|rhs_t72|sounds|ext_treads_soft_04","3*0.44668359",1,180],
            "frequency": "1",
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-40) max 40)*1.57/	60),(((-45) max 45)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-55) max 55)*1.57/	60),(((-50) max 50)*1.57/	60)]))"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|ThreadsOutS4 [Indent level: 2],
        "threadsouts4": {
            "sound": ["rhsafrf|addons|rhs_t72|sounds|ext_treads_soft_05","3*0.50118721",1,200],
            "frequency": "1",
            "volume": "engineOn*(camPos)*(grass)*((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-49) max 49)*1.57/	60),(((-53) max 53)*1.57/	60)])"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|ThreadsInH0 [Indent level: 2],
        "threadsinh0": {
            "sound": ["rhsafrf|addons|rhs_t72|sounds|int_treads_hard_01","2*0.25118864",1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*(1-grass)*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-0) max 0)*1.57/	60),(((-5) max 5)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-15) max 15)*1.57/	60),(((-10) max 10)*1.57/	60)]))"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|ThreadsInH1 [Indent level: 2],
        "threadsinh1": {
            "sound": ["rhsafrf|addons|rhs_t72|sounds|int_treads_hard_02","2*0.2818383",1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*(1-grass)*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-10) max 10)*1.57/	60),(((-15) max 15)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-30) max 30)*1.57/	60),(((-25) max 25)*1.57/	60)]))"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|ThreadsInH2 [Indent level: 2],
        "threadsinh2": {
            "sound": ["rhsafrf|addons|rhs_t72|sounds|int_treads_hard_03","2*0.31622776",1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*(1-grass)*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-25) max 25)*1.57/	60),(((-30) max 30)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-45) max 45)*1.57/	60),(((-40) max 40)*1.57/	60)]))"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|ThreadsInH3 [Indent level: 2],
        "threadsinh3": {
            "sound": ["rhsafrf|addons|rhs_t72|sounds|int_treads_hard_04","2*0.35481337",1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*(1-grass)*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-40) max 40)*1.57/	60),(((-45) max 45)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-55) max 55)*1.57/	60),(((-50) max 50)*1.57/	60)]))"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|ThreadsInH4 [Indent level: 2],
        "threadsinh4": {
            "sound": ["rhsafrf|addons|rhs_t72|sounds|int_treads_hard_05","2*0.39810717",1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*(1-grass)*((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-49) max 49)*1.57/	60),(((-53) max 53)*1.57/	60)])"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|ThreadsInS0 [Indent level: 2],
        "threadsins0": {
            "sound": ["rhsafrf|addons|rhs_t72|sounds|int_treads_soft_01","2*0.31622776",1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*grass*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-0) max 0)*1.57/	60),(((-5) max 5)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-15) max 15)*1.57/	60),(((-10) max 10)*1.57/	60)]))"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|ThreadsInS1 [Indent level: 2],
        "threadsins1": {
            "sound": ["rhsafrf|addons|rhs_t72|sounds|int_treads_soft_02","2*0.31622776",1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*grass*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-10) max 10)*1.57/	60),(((-15) max 15)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-30) max 30)*1.57/	60),(((-25) max 25)*1.57/	60)]))"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|ThreadsInS2 [Indent level: 2],
        "threadsins2": {
            "sound": ["rhsafrf|addons|rhs_t72|sounds|int_treads_soft_03","2*0.35481337",1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*grass*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-25) max 25)*1.57/	60),(((-30) max 30)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-45) max 45)*1.57/	60),(((-40) max 40)*1.57/	60)]))"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|ThreadsInS3 [Indent level: 2],
        "threadsins3": {
            "sound": ["rhsafrf|addons|rhs_t72|sounds|int_treads_soft_04","2*0.35481337",1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*grass*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-40) max 40)*1.57/	60),(((-45) max 45)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-55) max 55)*1.57/	60),(((-50) max 50)*1.57/	60)]))"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Sounds|ThreadsInS4 [Indent level: 2],
        "threadsins4": {
            "sound": ["rhsafrf|addons|rhs_t72|sounds|int_treads_soft_05","2*0.39810717",1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*grass*((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-49) max 49)*1.57/	60),(((-53) max 53)*1.57/	60)])"
        },
        "soundsetsint": ["RHS_T72_Engine_RPM0_INT_SoundSet","RHS_T72_Engine_RPM1_INT_SoundSet","RHS_T72_Engine_RPM2_INT_SoundSet","RHS_T72_Engine_INT_Burst_SoundSet","RHS_T72_Tracks_01_INT_SoundSet","RHS_T72_Tracks_02_INT_SoundSet","RHS_T72_Tracks_03_INT_SoundSet","RHS_T72_Tracks_04_INT_SoundSet","RHS_T72_Tracks_05_INT_SoundSet","RHS_T72_Tracks_06_INT_SoundSet","T72_Interior_Tone_Engine_Off_SoundSet","T72_Interior_Tone_Engine_On_SoundSet","T72_Rattling_INT_SoundSet","T72_Rain_INT_SoundSet","RHS_T72_Tracks_Brake_Hard_INT_SoundSet","RHS_T72_Tracks_Brake_Soft_INT_SoundSet","RHS_T72_Tracks_Turn_Hard_INT_SoundSet","RHS_T72_Tracks_Turn_Soft_INT_SoundSet","RHS_T72_Drive_Water_INT_SoundSet","RHS_T72_Drive_Dirt_INT_SoundSet","","Tracks_Movement_Dirt_Int_01_SoundSet","Tracks_Surface_Soft_Int_SoundSet","Tracks_Surface_Sand_Int_SoundSet","Tracks_Surface_Squeaks_Soft_Int_SoundSet","Tracks_Surface_Squeaks_Hard_Int_SoundSet","Tanks_Material_Strain_Int_SoundSet","Tank_General_Collision_Int_SoundSet","rhs_tank_t72_int_autoloader_SoundSet"],
        "soundsetsext": ["RHS_T72_Engine_RPM0_EXT_SoundSet","RHS_T72_Engine_RPM1_EXT_SoundSet","RHS_T72_Engine_RPM2_EXT_SoundSet","RHS_T72_Engine_EXT_Burst_SoundSet","RHS_T72_Tracks_01_EXT_SoundSet","RHS_T72_Tracks_02_EXT_SoundSet","RHS_T72_Tracks_03_EXT_SoundSet","RHS_T72_Tracks_04_EXT_SoundSet","RHS_T72_Tracks_05_EXT_SoundSet","RHS_T72_Tracks_06_EXT_SoundSet","T72_Rain_EXT_SoundSet","RHS_T72_Tracks_Brake_Hard_EXT_SoundSet","RHS_T72_Tracks_Brake_Soft_EXT_SoundSet","RHS_T72_Tracks_Turn_Hard_EXT_SoundSet","RHS_T72_Tracks_Turn_Soft_EXT_SoundSet","RHS_T72_Drive_Water_EXT_SoundSet","RHS_T72_Drive_Dirt_EXT_SoundSet","","Tracks_Movement_Dirt_Ext_01_SoundSet","Tracks_Surface_Soft_Ext_SoundSet","Tracks_Surface_Sand_Ext_SoundSet","Tracks_Surface_Squeaks_Soft_Ext_SoundSet","Tracks_Surface_Squeaks_Hard_Ext_SoundSet","Tank_General_Collision_SoundShader","rhs_tank_t72_ext_autoloader_SoundSet"]
    },
    "tracksspeed": -1,
    "wheelcircumference": 2.51,
    "extcameraposition": [0,2.2,-11],
    "viewdriverinexternal": 1,
    "viewcargoshadow": 1,
    "viewcargoshadowdiff": 1,
    "viewcargoshadowamb": 1,
    "cost": 1.5e+006,
    # Class: CfgVehicles|rhs_a3t72tank_base|TransportMagazines [Indent level: 1],
    "transportmagazines": {
        # Class: CfgVehicles|rhs_a3t72tank_base|TransportMagazines|_xx_rhs_30Rnd_545x39_7N10_AK [Indent level: 2]
        "_xx_rhs_30rnd_545x39_7n10_ak": {
            "magazine": "rhs_30Rnd_545x39_7N10_AK",
            "count": 10
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|TransportMagazines|_xx_rhs_mag_rgd5 [Indent level: 2],
        "_xx_rhs_mag_rgd5": {
            "magazine": "rhs_mag_rgd5",
            "count": 10
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|TransportMagazines|_xx_rhs_mag_nspn_red [Indent level: 2],
        "_xx_rhs_mag_nspn_red": {
            "magazine": "rhs_mag_nspn_red",
            "count": 10
        }
    },
    # Class: CfgVehicles|rhs_a3t72tank_base|TransportItems [Indent level: 1],
    "transportitems": {
        # Class: CfgVehicles|rhs_a3t72tank_base|TransportItems|_xx_FirstAidKit [Indent level: 2]
        "_xx_firstaidkit": {
            "name": "FirstAidKit",
            "count": 10
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|TransportItems|_xx_Medikit [Indent level: 2],
        "_xx_medikit": {
            "name": "Medikit",
            "count": 1
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|TransportItems|_xx_Toolkit [Indent level: 2],
        "_xx_toolkit": {
            "name": "Toolkit",
            "count": 1
        }
    },
    "armor": 450,
    "armorstructural": 220,
    "explosionshielding": 100,
    "crewexplosionprotection": 1,
    "mintotaldamagethreshold": 0.5,
    "fireresistance": -1,
    "crewvulnerable": 0,
    "texturelist": [],
    # Class: CfgVehicles|rhs_a3t72tank_base|ViewOptics [Indent level: 1],
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
    # Class: CfgVehicles|rhs_a3t72tank_base|Exhausts [Indent level: 1],
    "exhausts": {
        # Class: CfgVehicles|rhs_a3t72tank_base|Exhausts|Exhaust1 [Indent level: 2]
        "exhaust1": {
            "position": "exhaustl",
            "direction": "exhaustl_dir",
            "effect": "ExhaustEffectTankSide"
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Exhausts|Exhaust2 [Indent level: 2],
        "exhaust2": {
            "position": "exhaustr",
            "direction": "exhaustr_dir",
            "effect": "ExhaustEffectTankSide"
        }
    },
    # Class: CfgVehicles|rhs_a3t72tank_base|Reflectors [Indent level: 1],
    "reflectors": {
        # Class: CfgVehicles|rhs_a3t72tank_base|Reflectors|Driver_FG125_Cover [Indent level: 2]
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
            # Class: CfgVehicles|rhs_a3t72tank_base|Reflectors|Driver_FG125_Cover|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.2,
                "hardlimitstart": 130,
                "hardlimitend": 160
            }
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Reflectors|Driver_FG125_Cover_Flare [Indent level: 2],
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
            # Class: CfgVehicles|rhs_a3t72tank_base|Reflectors|Driver_FG125_Cover|Attenuation [Indent level: 3],
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
    # Class: CfgVehicles|rhs_a3t72tank_base|Components [Indent level: 1],
    "components": {
        # Class: CfgVehicles|rhs_a3t72tank_base|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 2]
        "vehiclesystemsdisplaymanagercomponentleft": {
            # Class: CfgVehicles|rhs_a3t72tank_base|Components|VehicleSystemsDisplayManagerComponentLeft|EmptyDisplay [Indent level: 3]
            "emptydisplay": {
                "componenttype": "EmptyDisplayComponent"
            },
            # Class: CfgVehicles|rhs_a3t72tank_base|Components|VehicleSystemsDisplayManagerComponentLeft|CrewDisplay [Indent level: 3],
            "crewdisplay": {
                "componenttype": "CrewDisplayComponent",
                "resource": "RscCustomInfoCrew"
            }
        },
        # Class: CfgVehicles|rhs_a3t72tank_base|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 2],
        "vehiclesystemsdisplaymanagercomponentright": {
            # Class: CfgVehicles|rhs_a3t72tank_base|Components|VehicleSystemsDisplayManagerComponentRight|EmptyDisplay [Indent level: 3]
            "emptydisplay": {
                "componenttype": "EmptyDisplayComponent"
            },
            # Class: CfgVehicles|rhs_a3t72tank_base|Components|VehicleSystemsDisplayManagerComponentRight|CrewDisplay [Indent level: 3],
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
    "_generalmacro": "Tank_F",
    "occludesoundswhenin": 0,
    "obstructsoundswhenin": 0,
    "cargogetinaction": ["GetInLow"],
    "cargogetoutaction": ["GetOutLow"],
    "sensorposition": "gunnerView",
    "audible": 18,
    "sensitivityear": "0.0075 /3",
    "turncoef": 5,
    "steeraheadsimul": 0.3,
    "steeraheadplan": 0.4,
    "brakedistance": 5,
    "hideproxyincombat": 1,
    "irscanground": 2,
    "irscanrangemax": 0,
    "irscanrangemin": 0,
    "irscantoeyefactor": 1,
    "enableradio": 1,
    "countermeasureactivationradius": 2000,
    "soundincommingmissile": ["|A3|Sounds_F|vehicles|air|noises|alarm_locked_by_missile_3",0.316228,1],
    "memorypointcargolight": "cargo light",
    "dampersbumpcoef": 4.5,
    "crewcrashprotection": 0.25,
    "secondaryexplosion": -1,
    "fuelexplosionpower": 1,
    "transportmaxweapons": 12,
    "transportmaxmagazines": 128,
    "transportmaxbackpacks": 12,
    "maximumload": 3000,
    # Class: CfgVehicles|Tank_F|TransportBackpacks [Indent level: 1],
    "transportbackpacks": {
    },
    # Class: CfgVehicles|Tank_F|TransportWeapons [Indent level: 1],
    "transportweapons": {
    },
    # Class: CfgVehicles|Tank_F|CamShake [Indent level: 1],
    "camshake": {
        "power": 5,
        "frequency": 20,
        "distance": 20,
        "minspeed": 5
    },
    "camshakecoef": 0,
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
    "canfloat": 0,
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
    "unloadincombat": 0,
    "epeimpulsedamagecoef": 30,
    "sensitivity": 2.5,
    "portrait": "",
    "ghostpreview": "",
    "damageresistance": 0.004,
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
    "radartype": 0,
    "limitedspeedcoef": 0.22,
    "hasdriver": 1,
    "hideweaponsdriver": 1,
    "hideweaponscargo": 0,
    "enablewatch": 0,
    "useprecisegetinaction": 0,
    "showalltargets": 0,
    "dustfrontleftpos": "dustFrontLeft",
    "dustfrontrightpos": "dustFrontRight",
    "dustbackleftpos": "dustBackLeft",
    "dustbackrightpos": "dustBackRight",
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
    "transportsoldier": 0,
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
    "soundlocked": ["",1,1],
    "cargoaction": [],
    "cargoiscodriver": [0],
    "drivercompartments": "Compartment1",
    "cargocompartments": ["Compartment1"],
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