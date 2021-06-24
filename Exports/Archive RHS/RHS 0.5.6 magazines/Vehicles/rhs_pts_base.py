rhs_pts_base = {
    "dlc": "RHS_AFRF",
    "rhs_decalparameters": ["['Number',cRHSPTSNumberPlaces,'Default']","['Label',cRHSPTSPlnSymPlaces, 'Platoon',12]"],
    "category": "Armored",
    "destrtype": "DestructDefault",
    "author": "Red Hammer Studios",
    "enablegps": 0,
    "incomingmissiledetectionsystem": 0,
    "weapons": [],
    "magazines": [],
    # Class: CfgVehicles|rhs_pts_base|UserActions [Indent level: 1],
    "useractions": {
        # Class: CfgVehicles|rhs_pts_base|UserActions|OpenRamp [Indent level: 2]
        "openramp": {
            "displayname": "Open Cargo Ramp",
            "position": "ramp",
            "onlyforplayer": 1,
            "radius": 6,
            "showwindow": 0,
            "condition": "(this doorPhase 'ramp' == 0) AND {Alive(this)} AND {(call RHS_fnc_findPlayer) in this} AND {((getPosASLW this) select 2) > -1}",
            "statement": "this animateDoor ['ramp',1];this engineOn false;[this] call rhs_fnc_pts_cargoDetach",
            "shortcut": "user12"
        },
        # Class: CfgVehicles|rhs_pts_base|UserActions|CloseRamp [Indent level: 2],
        "closeramp": {
            "displayname": "Close Cargo Ramp",
            "condition": "(this doorPhase 'ramp' == 1) AND {Alive(this)} AND {(call RHS_fnc_findPlayer) in this}",
            "statement": "this animateDoor ['ramp',0];[this] call rhs_fnc_pts_cargoAttach",
            "position": "ramp",
            "onlyforplayer": 1,
            "radius": 6,
            "showwindow": 0,
            "shortcut": "user12"
        }
    },
    "rhs_maxcargomasscoeff": 5e-008,
    "vehicleclass": "rhs_vehclass_apc",
    "editorsubcategory": "rhs_EdSubcat_apc",
    "displayname": "PTS-M",
    "faction": "rhs_faction_vmf",
    "crew": "rhs_vmf_flora_crew",
    "accuracy": 0.3,
    "side": 0,
    # Class: CfgVehicles|rhs_pts_base|RenderTargets [Indent level: 1],
    "rendertargets": {
    },
    "model": "rhsafrf|addons|rhs_pts|rhs_pts",
    "picture": "rhsafrf|addons|rhs_pts|ui|pts_ca.paa",
    "icon": "rhsafrf|addons|rhs_c_pts|ptsm_map_ca.paa",
    "driveropticsmodel": "",
    "mapsize": 11,
    "forcehidedriver": 0,
    "hideproxyincombat": 0,
    "cargoiscodriver": [1],
    "driveriscommander": 1,
    "viewcargoshadow": 1,
    "typicalcargo": ["rhs_vmf_flora_crew_commander","rhs_vmf_flora_crew","rhs_vmf_flora_crew",""],
    "getinaction": "GetInLow",
    "getoutaction": "GetOutLow",
    "cargogetinaction": ["GetInLow"],
    "cargogetoutaction": ["GetOutLow"],
    "transportsoldier": 1,
    "unloadincombat": 1,
    "tf_range_api": 35000,
    "cargoaction": ["RHS_BMP3_Cargo"],
    "driveoncomponent": ["Track_L","Track_R","Slide"],
    "driverdoor": "hatchD",
    "driveraction": "RHS_BMP3_driverout",
    "driverinaction": "RHS_BMP3_driver",
    "driverlefthandanimname": "steering",
    "driverrighthandanimname": "steering",
    "driverforceoptics": 0,
    "simulation": "tankX",
    "normalspeedforwardcoef": 0.85,
    "slowspeedforwardcoef": 0.5,
    "fuelcapacity": 672,
    "rhs_fuelcapacity": 672,
    "maxspeed": 46,
    "tankturnforce": 200000,
    "tankturnforceangminspd": 0.7,
    "tankturnforceangspd": 0.82,
    "accelaidforcecoef": 4,
    "accelaidforceyoffset": -4.1,
    "accelaidforcespd": 2.23,
    "canfloat": 1,
    "waterleakiness": 250,
    "maxfordingdepth": 0.1,
    "waterresistance": 1,
    "waterdamageengine": 0.9,
    "engineshifty": 0.1,
    "waterlineardampingcoefy": 2,
    "waterlineardampingcoefx": 2,
    "waterangulardampingcoef": 1.2,
    "waterresistancecoef": 0.175,
    "watereffectspeed": 5,
    "engineeffectspeed": 5,
    "waterfasteffectspeed": 28,
    "memorypointsleftengineeffect": "EngineEffectL",
    "memorypointsrightengineeffect": "EngineEffectR",
    "torquecurve": [[0,0],[0.478261,0.866667],[0.521739,0.984848],[0.565217,1],[0.608696,0.987879],[0.695652,0.909091],[0.869565,0.8],[1.13217,0]],
    "enginemoi": 10,
    "enginepower": 261,
    "peaktorque": 1650,
    "minomega": 85,
    "maxomega": 240.86,
    "idlerpm": 800,
    "redrpm": 2300,
    "thrustdelay": 0.3,
    "dampingratefullthrottle": 0.3,
    "dampingratezerothrottleclutchengaged": 3,
    "dampingratezerothrottleclutchdisengaged": 0.25,
    "enginelosses": 25,
    "transmissionlosses": 15,
    "clutchstrength": 18,
    "latency": 0.7,
    "switchtime": 0,
    "changegeartype": "rpmratio",
    "changegearomegaratios": [1,0.434783,0.434783,0,0.913043,0.608696,0.934783,0.652174,0.934783,0.652174,1,0.73913],
    # Class: CfgVehicles|rhs_pts_base|complexGearbox [Indent level: 1],
    "complexgearbox": {
        "gearboxratios": ["R1",-3.31,"N",0,"D1",3.31,"D2",1.934,"D3",1.132,"D4",0.662],
        "amphibiousratios": ["R1",-9.5,"N",0,"D1",9.5],
        "transmissionratios": ["High",18.5],
        "gearboxmode": "auto",
        "moveoffgear": 1,
        "drivestring": "D",
        "neutralstring": "N",
        "reversestring": "R",
        "transmissiondelay": 0.1
    },
    # Class: CfgVehicles|rhs_pts_base|Wheels [Indent level: 1],
    "wheels": {
        # Class: CfgVehicles|rhs_pts_base|Wheels|L2 [Indent level: 2]
        "l2": {
            "susptraveldirection": [-0.125,-1,0],
            "bonename": "wheel_podkoloL1",
            "center": "wheel_1_2_axis",
            "boundary": "wheel_1_2_bound",
            "side": "left",
            "width": 0.2,
            "steering": 0,
            "mass": 93,
            "moi": 10.3595,
            "maxbraketorque": 25000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "sprungmass": 1306,
            "springstrength": 92969,
            "springdamperrate": 7663,
            "dampingrate": 955,
            "dampingrateinair": 955,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.55],[0.18,1],[0.65,0.7]]
        },
        # Class: CfgVehicles|rhs_pts_base|Wheels|L3 [Indent level: 2],
        "l3": {
            "bonename": "wheel_podkolol2",
            "center": "wheel_1_3_axis",
            "boundary": "wheel_1_3_bound",
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "width": 0.2,
            "steering": 0,
            "mass": 93,
            "moi": 10.3595,
            "maxbraketorque": 25000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "sprungmass": 1306,
            "springstrength": 92969,
            "springdamperrate": 7663,
            "dampingrate": 955,
            "dampingrateinair": 955,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.55],[0.18,1],[0.65,0.7]]
        },
        # Class: CfgVehicles|rhs_pts_base|Wheels|L4 [Indent level: 2],
        "l4": {
            "bonename": "wheel_podkolol3",
            "center": "wheel_1_4_axis",
            "boundary": "wheel_1_4_bound",
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "width": 0.2,
            "steering": 0,
            "mass": 93,
            "moi": 10.3595,
            "maxbraketorque": 25000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "sprungmass": 1306,
            "springstrength": 92969,
            "springdamperrate": 7663,
            "dampingrate": 955,
            "dampingrateinair": 955,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.55],[0.18,1],[0.65,0.7]]
        },
        # Class: CfgVehicles|rhs_pts_base|Wheels|L5 [Indent level: 2],
        "l5": {
            "bonename": "wheel_podkolol4",
            "center": "wheel_1_5_axis",
            "boundary": "wheel_1_5_bound",
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "width": 0.2,
            "steering": 0,
            "mass": 93,
            "moi": 10.3595,
            "maxbraketorque": 25000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "sprungmass": 1306,
            "springstrength": 92969,
            "springdamperrate": 7663,
            "dampingrate": 955,
            "dampingrateinair": 955,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.55],[0.18,1],[0.65,0.7]]
        },
        # Class: CfgVehicles|rhs_pts_base|Wheels|L6 [Indent level: 2],
        "l6": {
            "bonename": "wheel_podkolol5",
            "center": "wheel_1_6_axis",
            "boundary": "wheel_1_6_bound",
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "width": 0.2,
            "steering": 0,
            "mass": 93,
            "moi": 10.3595,
            "maxbraketorque": 25000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "sprungmass": 1306,
            "springstrength": 92969,
            "springdamperrate": 7663,
            "dampingrate": 955,
            "dampingrateinair": 955,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.55],[0.18,1],[0.65,0.7]]
        },
        # Class: CfgVehicles|rhs_pts_base|Wheels|L7 [Indent level: 2],
        "l7": {
            "bonename": "wheel_podkolol6",
            "center": "wheel_1_7_axis",
            "boundary": "wheel_1_7_bound",
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "width": 0.2,
            "steering": 0,
            "mass": 93,
            "moi": 10.3595,
            "maxbraketorque": 25000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "sprungmass": 1306,
            "springstrength": 92969,
            "springdamperrate": 7663,
            "dampingrate": 955,
            "dampingrateinair": 955,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.55],[0.18,1],[0.65,0.7]]
        },
        # Class: CfgVehicles|rhs_pts_base|Wheels|L9 [Indent level: 2],
        "l9": {
            "bonename": "wheel_podkolol9",
            "center": "wheel_1_9_axis",
            "boundary": "wheel_1_9_bound",
            "maxdroop": 0,
            "maxcompression": 0,
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "width": 0.2,
            "steering": 0,
            "mass": 93,
            "moi": 10.3595,
            "maxbraketorque": 25000,
            "sprungmass": 1306,
            "springstrength": 92969,
            "springdamperrate": 7663,
            "dampingrate": 955,
            "dampingrateinair": 955,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.55],[0.18,1],[0.65,0.7]]
        },
        # Class: CfgVehicles|rhs_pts_base|Wheels|L1 [Indent level: 2],
        "l1": {
            "bonename": "",
            "center": "wheel_1_1_axis",
            "boundary": "wheel_1_1_bound",
            "maxdroop": 0,
            "maxcompression": 0,
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "width": 0.2,
            "steering": 0,
            "mass": 93,
            "moi": 10.3595,
            "maxbraketorque": 25000,
            "sprungmass": 1306,
            "springstrength": 92969,
            "springdamperrate": 7663,
            "dampingrate": 955,
            "dampingrateinair": 955,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.55],[0.18,1],[0.65,0.7]]
        },
        # Class: CfgVehicles|rhs_pts_base|Wheels|R2 [Indent level: 2],
        "r2": {
            "susptraveldirection": [0.125,-1,0],
            "bonename": "wheel_podkolop1",
            "center": "wheel_2_2_axis",
            "boundary": "wheel_2_2_bound",
            "side": "right",
            "width": 0.2,
            "steering": 0,
            "mass": 93,
            "moi": 10.3595,
            "maxbraketorque": 25000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "sprungmass": 1306,
            "springstrength": 92969,
            "springdamperrate": 7663,
            "dampingrate": 955,
            "dampingrateinair": 955,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.55],[0.18,1],[0.65,0.7]]
        },
        # Class: CfgVehicles|rhs_pts_base|Wheels|R3 [Indent level: 2],
        "r3": {
            "bonename": "wheel_podkolop2",
            "center": "wheel_2_3_axis",
            "boundary": "wheel_2_3_bound",
            "susptraveldirection": [0.125,-1,0],
            "side": "right",
            "width": 0.2,
            "steering": 0,
            "mass": 93,
            "moi": 10.3595,
            "maxbraketorque": 25000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "sprungmass": 1306,
            "springstrength": 92969,
            "springdamperrate": 7663,
            "dampingrate": 955,
            "dampingrateinair": 955,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.55],[0.18,1],[0.65,0.7]]
        },
        # Class: CfgVehicles|rhs_pts_base|Wheels|R4 [Indent level: 2],
        "r4": {
            "bonename": "wheel_podkolop3",
            "center": "wheel_2_4_axis",
            "boundary": "wheel_2_4_bound",
            "susptraveldirection": [0.125,-1,0],
            "side": "right",
            "width": 0.2,
            "steering": 0,
            "mass": 93,
            "moi": 10.3595,
            "maxbraketorque": 25000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "sprungmass": 1306,
            "springstrength": 92969,
            "springdamperrate": 7663,
            "dampingrate": 955,
            "dampingrateinair": 955,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.55],[0.18,1],[0.65,0.7]]
        },
        # Class: CfgVehicles|rhs_pts_base|Wheels|R5 [Indent level: 2],
        "r5": {
            "bonename": "wheel_podkolop4",
            "center": "wheel_2_5_axis",
            "boundary": "wheel_2_5_bound",
            "susptraveldirection": [0.125,-1,0],
            "side": "right",
            "width": 0.2,
            "steering": 0,
            "mass": 93,
            "moi": 10.3595,
            "maxbraketorque": 25000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "sprungmass": 1306,
            "springstrength": 92969,
            "springdamperrate": 7663,
            "dampingrate": 955,
            "dampingrateinair": 955,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.55],[0.18,1],[0.65,0.7]]
        },
        # Class: CfgVehicles|rhs_pts_base|Wheels|R6 [Indent level: 2],
        "r6": {
            "bonename": "wheel_podkolop5",
            "center": "wheel_2_6_axis",
            "boundary": "wheel_2_6_bound",
            "susptraveldirection": [0.125,-1,0],
            "side": "right",
            "width": 0.2,
            "steering": 0,
            "mass": 93,
            "moi": 10.3595,
            "maxbraketorque": 25000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "sprungmass": 1306,
            "springstrength": 92969,
            "springdamperrate": 7663,
            "dampingrate": 955,
            "dampingrateinair": 955,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.55],[0.18,1],[0.65,0.7]]
        },
        # Class: CfgVehicles|rhs_pts_base|Wheels|R7 [Indent level: 2],
        "r7": {
            "bonename": "wheel_podkolop6",
            "center": "wheel_2_7_axis",
            "boundary": "wheel_2_7_bound",
            "susptraveldirection": [0.125,-1,0],
            "side": "right",
            "width": 0.2,
            "steering": 0,
            "mass": 93,
            "moi": 10.3595,
            "maxbraketorque": 25000,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "sprungmass": 1306,
            "springstrength": 92969,
            "springdamperrate": 7663,
            "dampingrate": 955,
            "dampingrateinair": 955,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.55],[0.18,1],[0.65,0.7]]
        },
        # Class: CfgVehicles|rhs_pts_base|Wheels|R9 [Indent level: 2],
        "r9": {
            "bonename": "wheel_podkolop9",
            "center": "wheel_2_9_axis",
            "boundary": "wheel_2_9_bound",
            "maxdroop": 0,
            "maxcompression": 0,
            "susptraveldirection": [0.125,-1,0],
            "side": "right",
            "width": 0.2,
            "steering": 0,
            "mass": 93,
            "moi": 10.3595,
            "maxbraketorque": 25000,
            "sprungmass": 1306,
            "springstrength": 92969,
            "springdamperrate": 7663,
            "dampingrate": 955,
            "dampingrateinair": 955,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.55],[0.18,1],[0.65,0.7]]
        },
        # Class: CfgVehicles|rhs_pts_base|Wheels|R1 [Indent level: 2],
        "r1": {
            "bonename": "",
            "center": "wheel_2_1_axis",
            "boundary": "wheel_2_1_bound",
            "maxdroop": 0,
            "maxcompression": 0,
            "susptraveldirection": [0.125,-1,0],
            "side": "right",
            "width": 0.2,
            "steering": 0,
            "mass": 93,
            "moi": 10.3595,
            "maxbraketorque": 25000,
            "sprungmass": 1306,
            "springstrength": 92969,
            "springdamperrate": 7663,
            "dampingrate": 955,
            "dampingrateinair": 955,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3.5,
            "latstiffy": 35,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.55],[0.18,1],[0.65,0.7]]
        }
    },
    "soundgetin": ["A3|sounds_f|vehicles|armor|noises|get_in_out",0.562341,1],
    "soundgetout": ["A3|sounds_f|vehicles|armor|noises|get_in_out",0.562341,1,20],
    "sounddammage": ["",0.562341,1],
    "soundengineonint": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_int_start",0.707946,1],
    "soundengineonext": ["|rhsafrf|addons|rhs_bmp|sounds|utd20_start.wss",0.630957,1,200],
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
    # Class: CfgVehicles|rhs_pts_base|Sounds [Indent level: 1],
    "sounds": {
        # Class: CfgVehicles|rhs_pts_base|Sounds|Idle_ext [Indent level: 2]
        "idle_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_ext_idle",0.707946,1,200],
            "frequency": "0.95	+	((rpm/	5200) factor[(400/	5200),(900/	5200)])*0.15",
            "volume": "engineOn*camPos*(((rpm/	5200) factor[(100/	5200),(200/	5200)])	*	((rpm/	5200) factor[(900/	5200),(700/	5200)]))"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|Engine [Indent level: 2],
        "engine": {
            "sound": ["|rhsafrf|addons|rhs_bmp|sounds|UTD20.ogg",0.794328,1,200],
            "frequency": "0.8	+	((rpm/	5200) factor[(700/	5200),(1100/	5200)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	5200) factor[(705/	5200),(850/	5200)])	*	((rpm/	5200) factor[(1100 /	5200),(950/	5200)]))"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|Engine1_ext [Indent level: 2],
        "engine1_ext": {
            "sound": ["|rhsafrf|addons|rhs_bmp|sounds|UTD20.ogg",0.794328,1,200],
            "frequency": "0.8	+	((rpm/	5200) factor[(950/	5200),(1400/	5200)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	5200) factor[(900/	5200),(1050/	5200)])	*	((rpm/	5200) factor[(1400/	5200),(1200/	5200)]))"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|Engine2_ext [Indent level: 2],
        "engine2_ext": {
            "sound": ["|rhsafrf|addons|rhs_bmp|sounds|UTD20.ogg",0.891251,1,250],
            "frequency": "0.8	+	((rpm/	5200) factor[(1200/	5200),(1700/	5200)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	5200) factor[(1170/	5200),(1380/	5200)])	*	((rpm/	5200) factor[(1700/	5200),(1500/	5200)]))"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|Engine3_ext [Indent level: 2],
        "engine3_ext": {
            "sound": ["|rhsafrf|addons|rhs_bmp|sounds|UTD20.ogg",1,1,300],
            "frequency": "0.8	+	((rpm/	5200) factor[(1500/	5200),(2100/	5200)])*0.1",
            "volume": "engineOn*camPos*(((rpm/	5200) factor[(1500/	5200),(1670/	5200)])	*	((rpm/	5200) factor[(2100/	5200),(1800/	5200)]))"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|Engine4_ext [Indent level: 2],
        "engine4_ext": {
            "sound": ["|rhsafrf|addons|rhs_bmp|sounds|UTD20.ogg",1.12202,1,340],
            "frequency": "0.8	+	((rpm/	5200) factor[(1800/	5200),(2300/	5200)])*0.1",
            "volume": "engineOn*camPos*(((rpm/	5200) factor[(1780/	5200),(2060/	5200)])	*	((rpm/	5200) factor[(2450/	5200),(2200/	5200)]))"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|Engine5_ext [Indent level: 2],
        "engine5_ext": {
            "sound": ["|rhsafrf|addons|rhs_bmp|sounds|UTD20.ogg",1.41254,1,400],
            "frequency": "0.8	+	((rpm/	5200) factor[(2100/	5200),(2640/	5200)])*0.1",
            "volume": "engineOn*camPos*((rpm/	5200) factor[(2150/	5200),(2500/	5200)])"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|IdleThrust [Indent level: 2],
        "idlethrust": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_ext_idle",0.891251,1,200],
            "frequency": "0.8	+	((rpm/	5200) factor[(400/	5200),(900/	5200)])*0.15",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(100/	5200),(200/	5200)])	*	((rpm/	5200) factor[(900/	5200),(700/	5200)]))"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|EngineThrust [Indent level: 2],
        "enginethrust": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_ext_rpm1",1.12202,1,200],
            "frequency": "0.8	+	((rpm/	5200) factor[(700/	5200),(1100/	5200)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(705/	5200),(850/	5200)])	*	((rpm/	5200) factor[(1100 /	5200),(950/	5200)]))"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|Engine1_Thrust_ext [Indent level: 2],
        "engine1_thrust_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_ext_rpm2",1.25893,1,200],
            "frequency": "0.8	+	((rpm/	5200) factor[(950/	5200),(1400/	5200)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(900/	5200),(1050/	5200)])	*	((rpm/	5200) factor[(1400/	5200),(1200/	5200)]))"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|Engine2_Thrust_ext [Indent level: 2],
        "engine2_thrust_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_ext_rpm3",1.41254,1,250],
            "frequency": "0.8	+	((rpm/	5200) factor[(1200/	5200),(1700/	5200)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(1170/	5200),(1380/	5200)])	*	((rpm/	5200) factor[(1700/	5200),(1500/	5200)]))"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|Engine3_Thrust_ext [Indent level: 2],
        "engine3_thrust_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_ext_rpm4",1.58489,1,350],
            "frequency": "0.8	+	((rpm/	5200) factor[(1500/	5200),(2100/	5200)])*0.1",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(1500/	5200),(1670/	5200)])	*	((rpm/	5200) factor[(2100/	5200),(1800/	5200)]))"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|Engine4_Thrust_ext [Indent level: 2],
        "engine4_thrust_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_ext_rpm5",1.77828,1,400],
            "frequency": "0.8	+	((rpm/	5200) factor[(1800/	5200),(2300/	5200)])*0.1",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(1780/	5200),(2060/	5200)])	*	((rpm/	5200) factor[(2450/	5200),(2200/	5200)]))"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|Engine5_Thrust_ext [Indent level: 2],
        "engine5_thrust_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_ext_rpm6",1.99526,1,450],
            "frequency": "0.8	+	((rpm/	5200) factor[(2100/	5200),(2640/	5200)])*0.1",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*((rpm/	5200) factor[(2150/	5200),(2500/	5200)])"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|Idle_int [Indent level: 2],
        "idle_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_int_idle",0.316228,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(400/	5200),(900/	5200)])*0.15",
            "volume": "engineOn*(1-camPos)*(((rpm/	5200) factor[(100/	5200),(200/	5200)])	*	((rpm/	5200) factor[(900/	5200),(700/	5200)]))"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|Engine_int [Indent level: 2],
        "engine_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_int_rpm1",0.354813,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(700/	5200),(1100/	5200)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	5200) factor[(705/	5200),(850/	5200)])	*	((rpm/	5200) factor[(1100 /	5200),(950/	5200)]))"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|Engine1_int [Indent level: 2],
        "engine1_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_int_rpm2",0.398107,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(950/	5200),(1400/	5200)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	5200) factor[(900/	5200),(1050/	5200)])	*	((rpm/	5200) factor[(1400/	5200),(1200/	5200)]))"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|Engine2_int [Indent level: 2],
        "engine2_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_int_rpm3",0.446684,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(1200/	5200),(1700/	5200)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	5200) factor[(1170/	5200),(1380/	5200)])	*	((rpm/	5200) factor[(1700/	5200),(1500/	5200)]))"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|Engine3_int [Indent level: 2],
        "engine3_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_int_rpm4",0.501187,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(1500/	5200),(2100/	5200)])*0.1",
            "volume": "engineOn*(1-camPos)*(((rpm/	5200) factor[(1500/	5200),(1670/	5200)])	*	((rpm/	5200) factor[(2100/	5200),(1800/	5200)]))"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|Engine4_int [Indent level: 2],
        "engine4_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_int_rpm5",0.562341,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(1800/	5200),(2300/	5200)])*0.1",
            "volume": "engineOn*(1-camPos)*(((rpm/	5200) factor[(1780/	5200),(2060/	5200)])	*	((rpm/	5200) factor[(2450/	5200),(2200/	5200)]))"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|Engine5_int [Indent level: 2],
        "engine5_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_int_rpm6",0.630957,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(2100/	5200),(2640/	5200)])*0.1",
            "volume": "engineOn*(1-camPos)*((rpm/	5200) factor[(2150/	5200),(2500/	5200)])"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|IdleThrust_int [Indent level: 2],
        "idlethrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_int_idle",0.354813,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(400/	5200),(900/	5200)])*0.15",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(100/	5200),(200/	5200)])	*	((rpm/	5200) factor[(900/	5200),(700/	5200)]))"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|EngineThrust_int [Indent level: 2],
        "enginethrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_int_rpm1",0.398107,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(700/	5200),(1100/	5200)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(705/	5200),(850/	5200)])	*	((rpm/	5200) factor[(1100 /	5200),(950/	5200)]))"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|Engine1_Thrust_int [Indent level: 2],
        "engine1_thrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_int_rpm2",0.446684,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(950/	5200),(1400/	5200)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(900/	5200),(1050/	5200)])	*	((rpm/	5200) factor[(1400/	5200),(1200/	5200)]))"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|Engine2_Thrust_int [Indent level: 2],
        "engine2_thrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_int_rpm3",0.446684,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(1200/	5200),(1700/	5200)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(1170/	5200),(1380/	5200)])	*	((rpm/	5200) factor[(1700/	5200),(1500/	5200)]))"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|Engine3_Thrust_int [Indent level: 2],
        "engine3_thrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_int_rpm4",0.501187,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(1500/	5200),(2100/	5200)])*0.1",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(1500/	5200),(1670/	5200)])	*	((rpm/	5200) factor[(2100/	5200),(1800/	5200)]))"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|Engine4_Thrust_int [Indent level: 2],
        "engine4_thrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_int_rpm5",0.562341,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(1800/	5200),(2300/	5200)])*0.1",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(1780/	5200),(2060/	5200)])	*	((rpm/	5200) factor[(2450/	5200),(2200/	5200)]))"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|Engine5_Thrust_int [Indent level: 2],
        "engine5_thrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_int_rpm6",0.630957,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(2100/	5200),(2640/	5200)])*0.1",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*((rpm/	5200) factor[(2150/	5200),(2500/	5200)])"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|NoiseInt [Indent level: 2],
        "noiseint": {
            "sound": ["A3|sounds_f|vehicles|armor|noises|noise_tank_int_1",0.562341,1],
            "frequency": "1",
            "volume": "(1-camPos)*(angVelocity max 0.04)*(speed factor[4, 25])"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|NoiseExt [Indent level: 2],
        "noiseext": {
            "sound": ["A3|sounds_f|vehicles|armor|noises|noise_tank_ext_1",0.794328,1,150],
            "frequency": "1",
            "volume": "camPos*(angVelocity max 0.04)*(speed factor[4, 25])"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|ThreadsOutH0 [Indent level: 2],
        "threadsouth0": {
            "sound": ["|rhsafrf|addons|rhs_bmp|sounds|lanc_2.ogg",0.398107,1,140],
            "frequency": "1",
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-0) max 0)/	60),(((-5) max 5)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-15) max 15)/	60),(((-10) max 10)/	60)]))"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|ThreadsOutH1 [Indent level: 2],
        "threadsouth1": {
            "sound": ["|rhsafrf|addons|rhs_bmp|sounds|lanc_2.ogg",0.446684,1,160],
            "frequency": "1",
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-10) max 10)/	60),(((-15) max 15)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-30) max 30)/	60),(((-25) max 25)/	60)]))"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|ThreadsOutH2 [Indent level: 2],
        "threadsouth2": {
            "sound": ["|rhsafrf|addons|rhs_bmp|sounds|lanc_3.ogg",0.501187,1,180],
            "frequency": "1",
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-25) max 25)/	60),(((-30) max 30)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-45) max 45)/	60),(((-40) max 40)/	60)]))"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|ThreadsOutH3 [Indent level: 2],
        "threadsouth3": {
            "sound": ["|rhsafrf|addons|rhs_bmp|sounds|lanc_4.ogg",0.562341,1,200],
            "frequency": "1",
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-40) max 40)/	60),(((-45) max 45)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-55) max 55)/	60),(((-50) max 50)/	60)]))"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|ThreadsOutH4 [Indent level: 2],
        "threadsouth4": {
            "sound": ["|rhsafrf|addons|rhs_bmp|sounds|lanc_5.ogg",0.562341,1,220],
            "frequency": "1",
            "volume": "engineOn*camPos*(1-grass)*((((-speed*3.6) max speed*3.6)/	60) factor[(((-49) max 49)/	60),(((-53) max 53)/	60)])"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|ThreadsOutS0 [Indent level: 2],
        "threadsouts0": {
            "sound": ["|rhsafrf|addons|rhs_bmp|sounds|lanc_2.ogg",0.316228,1,120],
            "frequency": "1",
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-0) max 0)/	60),(((-5) max 5)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-15) max 15)/	60),(((-10) max 10)/	60)]))"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|ThreadsOutS1 [Indent level: 2],
        "threadsouts1": {
            "sound": ["|rhsafrf|addons|rhs_bmp|sounds|lanc_2.ogg",0.354813,1,140],
            "frequency": "1",
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-10) max 10)/	60),(((-15) max 15)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-30) max 30)/	60),(((-25) max 25)/	60)]))"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|ThreadsOutS2 [Indent level: 2],
        "threadsouts2": {
            "sound": ["|rhsafrf|addons|rhs_bmp|sounds|lanc_3.ogg",0.398107,1,160],
            "frequency": "1",
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-25) max 25)/	60),(((-30) max 30)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-45) max 45)/	60),(((-40) max 40)/	60)]))"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|ThreadsOutS3 [Indent level: 2],
        "threadsouts3": {
            "sound": ["|rhsafrf|addons|rhs_bmp|sounds|lanc_4.ogg",0.446684,1,180],
            "frequency": "1",
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-40) max 40)/	60),(((-45) max 45)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-55) max 55)/	60),(((-50) max 50)/	60)]))"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|ThreadsOutS4 [Indent level: 2],
        "threadsouts4": {
            "sound": ["|rhsafrf|addons|rhs_bmp|sounds|lanc_5.ogg",0.501187,1,200],
            "frequency": "1",
            "volume": "engineOn*(camPos)*(grass)*((((-speed*3.6) max speed*3.6)/	60) factor[(((-49) max 49)/	60),(((-53) max 53)/	60)])"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|ThreadsInH0 [Indent level: 2],
        "threadsinh0": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_hard_01",0.446684,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*(1-grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-0) max 0)/	60),(((-5) max 5)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-15) max 15)/	60),(((-10) max 10)/	60)]))"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|ThreadsInH1 [Indent level: 2],
        "threadsinh1": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_hard_02",0.446684,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*(1-grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-10) max 10)/	60),(((-15) max 15)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-30) max 30)/	60),(((-25) max 25)/	60)]))"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|ThreadsInH2 [Indent level: 2],
        "threadsinh2": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_hard_03",0.446684,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*(1-grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-25) max 25)/	60),(((-30) max 30)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-45) max 45)/	60),(((-40) max 40)/	60)]))"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|ThreadsInH3 [Indent level: 2],
        "threadsinh3": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_hard_04",0.501187,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*(1-grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-40) max 40)/	60),(((-45) max 45)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-55) max 55)/	60),(((-50) max 50)/	60)]))"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|ThreadsInH4 [Indent level: 2],
        "threadsinh4": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_hard_05",0.562341,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*(1-grass)*((((-speed*3.6) max speed*3.6)/	60) factor[(((-49) max 49)/	60),(((-53) max 53)/	60)])"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|ThreadsInS0 [Indent level: 2],
        "threadsins0": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_soft_01",0.354813,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*grass*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-0) max 0)/	60),(((-5) max 5)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-15) max 15)/	60),(((-10) max 10)/	60)]))"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|ThreadsInS1 [Indent level: 2],
        "threadsins1": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_soft_02",0.354813,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*grass*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-10) max 10)/	60),(((-15) max 15)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-30) max 30)/	60),(((-25) max 25)/	60)]))"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|ThreadsInS2 [Indent level: 2],
        "threadsins2": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_soft_03",0.398107,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*grass*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-25) max 25)/	60),(((-30) max 30)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-45) max 45)/	60),(((-40) max 40)/	60)]))"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|ThreadsInS3 [Indent level: 2],
        "threadsins3": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_soft_04",0.398107,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*grass*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-40) max 40)/	60),(((-45) max 45)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-55) max 55)/	60),(((-50) max 50)/	60)]))"
        },
        # Class: CfgVehicles|rhs_pts_base|Sounds|ThreadsInS4 [Indent level: 2],
        "threadsins4": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_soft_05",0.446684,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*grass*((((-speed*3.6) max speed*3.6)/	60) factor[(((-49) max 49)/	60),(((-53) max 53)/	60)])"
        }
    },
    "drivercansee": "2+4+8",
    "gunnercansee": "2+4+8",
    "commandercansee": "2+4+8",
    "tracksspeed": 1.35,
    "wheelcircumference": 1.922,
    "attenuationeffecttype": "TankAttenuation",
    "textsingular": "PTS",
    "textplural": "PTS",
    "namesound": "veh_vehicle_APC_s",
    "extcameraposition": [0,2,-15],
    "cost": 1.5e+006,
    "damageresistance": 0.00845,
    "crewvulnerable": 1,
    "armor": 50,
    "armorstructural": 500,
    # Class: CfgVehicles|rhs_pts_base|TransportMagazines [Indent level: 1],
    "transportmagazines": {
    },
    # Class: CfgVehicles|rhs_pts_base|TransportWeapons [Indent level: 1],
    "transportweapons": {
    },
    # Class: CfgVehicles|rhs_pts_base|TransportItems [Indent level: 1],
    "transportitems": {
        # Class: CfgVehicles|rhs_pts_base|TransportItems|_xx_FirstAidKit [Indent level: 2]
        "_xx_firstaidkit": {
            "name": "FirstAidKit",
            "count": 4
        },
        # Class: CfgVehicles|rhs_pts_base|TransportItems|_xx_Medikit [Indent level: 2],
        "_xx_medikit": {
            "name": "Medikit",
            "count": 1
        }
    },
    # Class: CfgVehicles|rhs_pts_base|TransportBackpacks [Indent level: 1],
    "transportbackpacks": {
        # Class: CfgVehicles|rhs_pts_base|TransportBackpacks|_xx_rhs_sidor [Indent level: 2]
        "_xx_rhs_sidor": {
            "backpack": "rhs_sidor",
            "count": 7
        }
    },
    # Class: CfgVehicles|rhs_pts_base|HitPoints [Indent level: 1],
    "hitpoints": {
        # Class: CfgVehicles|rhs_pts_base|HitPoints|HitHull [Indent level: 2]
        "hithull": {
            "armor": 0.4,
            "material": -1,
            "name": "telo",
            "visual": "zbytek",
            "passthrough": 0,
            "minimalhit": 0.44,
            "explosionshielding": 0.5,
            "radius": 0.25,
            "armorcomponent": "hit_hull"
        },
        # Class: CfgVehicles|rhs_pts_base|HitPoints|HitEngine [Indent level: 2],
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
        # Class: CfgVehicles|rhs_pts_base|HitPoints|HitLTrack [Indent level: 2],
        "hitltrack": {
            "armor": -150,
            "material": -1,
            "name": "pas_L",
            "passthrough": 0,
            "minimalhit": -0.25,
            "explosionshielding": 0.15,
            "radius": 0.3,
            "armorcomponent": "hit_trackL",
            "visual": "pas_L"
        },
        # Class: CfgVehicles|rhs_pts_base|HitPoints|HitRTrack [Indent level: 2],
        "hitrtrack": {
            "armor": -150,
            "material": -1,
            "name": "pas_P",
            "passthrough": 0,
            "minimalhit": -0.25,
            "explosionshielding": 0.15,
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
    # Class: CfgVehicles|rhs_pts_base|Turrets [Indent level: 1],
    "turrets": {
        # Class: CfgVehicles|APC_Tracked_02_base_F|Turrets|MainTurret [Indent level: 2]
        "mainturret": {
            # Class: CfgVehicles|APC_Tracked_02_base_F|Turrets|MainTurret|Turrets [Indent level: 3]
            "turrets": {
                # Class: CfgVehicles|APC_Tracked_02_base_F|Turrets|MainTurret|Turrets|CommanderOptics [Indent level: 4]
                "commanderoptics": {
                    "memorypointgunneroutoptics": "commanderview",
                    "memorypointgunneroptics": "commanderview",
                    "minelev": -25,
                    "maxelev": 60,
                    "initelev": 0,
                    "minturn": -360,
                    "maxturn": 360,
                    "initturn": 0,
                    "mincamelev": -90,
                    "maxcamelev": 90,
                    "weapons": ["SmokeLauncher"],
                    "magazines": ["SmokeLauncherMag"],
                    "soundservo": ["A3|Sounds_F|vehicles|armor|APC|noises|servo_APC_comm",0.562341,1,30],
                    "soundservovertical": ["A3|Sounds_F|vehicles|armor|APC|noises|servo_APC_comm",0.562341,1,30],
                    "outgunnermayfire": 0,
                    "ingunnermayfire": 1,
                    "gunneraction": "Commander_APC_tracked_02_cannon_F_out",
                    "gunnerinaction": "Commander_APC_tracked_02_cannon_F_in",
                    "gunnergetinaction": "GetInAMV_cargo",
                    "gunnergetoutaction": "GetOutLow",
                    "gunneropticsmodel": "A3|weapons_f|reticle|Optics_Commander_OPFOR_F",
                    "gunneroutopticsmodel": "",
                    "gunneropticseffect": [],
                    "gunnerforceoptics": 0,
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
                    # Class: CfgVehicles|APC_Tracked_02_base_F|Turrets|MainTurret|Turrets|CommanderOptics|ViewOptics [Indent level: 5],
                    "viewoptics": {
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
                    },
                    # Class: CfgVehicles|APC_Tracked_02_base_F|Turrets|MainTurret|Turrets|CommanderOptics|OpticsIn [Indent level: 5],
                    "opticsin": {
                        # Class: CfgVehicles|APC_Tracked_02_base_F|Turrets|MainTurret|Turrets|CommanderOptics|OpticsIn|Wide [Indent level: 6]
                        "wide": {
                            "thermalmode": [0,1],
                            "gunneropticsmodel": "A3|Weapons_F|Reticle|Optics_Commander_02_w_F.p3d",
                            "initfov": "(36 / 120)",
                            "minfov": "(36 / 120)",
                            "maxfov": "(36 / 120)",
                            "visionmode": ["Normal","NVG","TI"],
                            "gunneropticseffect": [],
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
                            "maxmovez": 0
                        },
                        # Class: CfgVehicles|APC_Tracked_02_base_F|Turrets|MainTurret|Turrets|CommanderOptics|OpticsIn|Medium [Indent level: 6],
                        "medium": {
                            "thermalmode": [0,1],
                            "gunneropticsmodel": "A3|Weapons_F|Reticle|Optics_Commander_02_m_F.p3d",
                            "initfov": "(150 * 0.05625 / 120)",
                            "minfov": "(150 * 0.05625 / 120)",
                            "maxfov": "(150 * 0.05625 / 120)",
                            "visionmode": ["Normal","NVG","TI"],
                            "gunneropticseffect": [],
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
                            "maxmovez": 0
                        },
                        # Class: CfgVehicles|APC_Tracked_02_base_F|Turrets|MainTurret|Turrets|CommanderOptics|OpticsIn|Narrow [Indent level: 6],
                        "narrow": {
                            "thermalmode": [0,1],
                            "gunneropticsmodel": "A3|Weapons_F|Reticle|Optics_Commander_02_n_F.p3d",
                            "initfov": "(60 * 0.05625 / 120)",
                            "minfov": "(60 * 0.05625 / 120)",
                            "maxfov": "(60 * 0.05625 / 120)",
                            "visionmode": ["Normal","NVG","TI"],
                            "gunneropticseffect": [],
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
                            "maxmovez": 0
                        }
                    },
                    "turretinfotype": "RscOptics_MBT_02_commander",
                    "showcrewaim": 1,
                    "startengine": 0,
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
                    "maxhorizontalrotspeed": 1.8,
                    "maxverticalrotspeed": 1.8,
                    "viewgunnerinexternal": 1,
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
                    "body": "obsTurret",
                    "gun": "obsGun",
                    "animationsourcebody": "obsTurret",
                    "animationsourcegun": "obsGun",
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
                    "gunnerrighthandanimname": "",
                    "gunnerleftleganimname": "",
                    "gunnerrightleganimname": "",
                    "gunnerdoor": "",
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
            "body": "mainTurret",
            "gun": "mainGun",
            "weapons": ["LMG_M200"],
            "magazines": ["2000Rnd_65x39_belt","2000Rnd_65x39_belt"],
            "soundservo": ["A3|Sounds_F|vehicles|armor|APC|noises|servo_APC_gunner",0.562341,1,10],
            "soundservovertical": ["A3|Sounds_F|vehicles|armor|APC|noises|servo_APC_gunner_vertical",0.562341,1,30],
            "initelev": 1,
            "minelev": -16,
            "maxelev": 36,
            "mincamelev": -90,
            "maxcamelev": 90,
            "gunneraction": "Gunner_APC_tracked_02_cannon_F_out",
            "gunnerinaction": "Gunner_APC_tracked_02_cannon_F_in",
            "gunnergetinaction": "GetInAMV_cargo",
            "gunnergetoutaction": "GetOutLow",
            "viewgunnerinexternal": 1,
            "castgunnershadow": 1,
            "startengine": 0,
            "stabilizedinaxes": 3,
            "gunneropticsmodel": "A3|weapons_f|reticle|Optics_Gunner_02_F",
            "gunneroutopticsmodel": "",
            "gunnerforceoptics": 0,
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
            "discretedistance": [100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000,2100,2200,2300,2400,2500,2600,2700,2800,2900,3000],
            "discretedistanceinitindex": 2,
            "memorypointgunneroptics": "gunnerview",
            "selectionfireanim": "zasleh2",
            "memorypointgun": ["usti hlavne3"],
            # Class: CfgVehicles|APC_Tracked_02_base_F|Turrets|MainTurret|ViewOptics [Indent level: 3],
            "viewoptics": {
                "visionmode": ["Normal","TI"],
                "initanglex": 0,
                "minanglex": -30,
                "maxanglex": 30,
                "initangley": 0,
                "minangley": -100,
                "maxangley": 100,
                "initfov": 0.4375,
                "minfov": 0.03482,
                "maxfov": 0.4375,
                "thermalmode": [0,1],
                "minmovex": 0,
                "maxmovex": 0,
                "minmovey": 0,
                "maxmovey": 0,
                "minmovez": 0,
                "maxmovez": 0
            },
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
            # Class: CfgVehicles|APC_Tracked_02_base_F|Turrets|MainTurret|OpticsIn [Indent level: 3],
            "opticsin": {
                # Class: CfgVehicles|APC_Tracked_02_base_F|Turrets|MainTurret|OpticsIn|Wide [Indent level: 4]
                "wide": {
                    "thermalmode": [0,1],
                    "gunneropticsmodel": "A3|Weapons_F|Reticle|Optics_Gunner_MBT_02_w_F.p3d",
                    "initfov": "(36 / 120)",
                    "minfov": "(36 / 120)",
                    "maxfov": "(36 / 120)",
                    "visionmode": ["Normal","NVG","TI"],
                    "gunneropticseffect": [],
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
                    "maxmovez": 0
                },
                # Class: CfgVehicles|APC_Tracked_02_base_F|Turrets|MainTurret|OpticsIn|Medium [Indent level: 4],
                "medium": {
                    "thermalmode": [0,1],
                    "gunneropticsmodel": "A3|Weapons_F|Reticle|Optics_Gunner_MBT_02_m_F.p3d",
                    "initfov": "(150 * 0.05625 / 120)",
                    "minfov": "(150 * 0.05625 / 120)",
                    "maxfov": "(150 * 0.05625 / 120)",
                    "visionmode": ["Normal","NVG","TI"],
                    "gunneropticseffect": [],
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
                    "maxmovez": 0
                },
                # Class: CfgVehicles|APC_Tracked_02_base_F|Turrets|MainTurret|OpticsIn|Narrow [Indent level: 4],
                "narrow": {
                    "thermalmode": [0,1],
                    "gunneropticsmodel": "A3|Weapons_F|Reticle|Optics_Gunner_MBT_02_n_F.p3d",
                    "initfov": "(60 * 0.05625 / 120)",
                    "minfov": "(60 * 0.05625 / 120)",
                    "maxfov": "(60 * 0.05625 / 120)",
                    "visionmode": ["Normal","NVG","TI"],
                    "gunneropticseffect": [],
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
                    "maxmovez": 0
                }
            },
            "turretinfotype": "RscOptics_MBT_02_gunner",
            "showcrewaim": 2,
            # Class: CfgVehicles|APC_Tracked_02_base_F|Turrets|MainTurret|HitPoints [Indent level: 3],
            "hitpoints": {
                # Class: CfgVehicles|APC_Tracked_02_base_F|Turrets|MainTurret|HitPoints|HitTurret [Indent level: 4]
                "hitturret": {
                    "armor": 0.8,
                    "material": -1,
                    "armorcomponent": "hit_main_turret",
                    "name": "hit_main_turret_point",
                    "visual": "vez",
                    "passthrough": 0,
                    "minimalhit": 0.1,
                    "explosionshielding": 0.2,
                    "radius": 0.25,
                    "isturret": 1
                },
                # Class: CfgVehicles|APC_Tracked_02_base_F|Turrets|MainTurret|HitPoints|HitGun [Indent level: 4],
                "hitgun": {
                    "armor": 0.6,
                    "material": -1,
                    "armorcomponent": "hit_main_gun",
                    "name": "hit_main_gun_point",
                    "visual": "zbran",
                    "passthrough": 0,
                    "minimalhit": 0.1,
                    "explosionshielding": 0.4,
                    "radius": 0.2,
                    "isgun": 1
                }
            },
            "commanding": 1,
            "gunbeg": "usti hlavne",
            "gunend": "konec hlavne",
            "memorypointsgetingunner": "pos gunner",
            "memorypointsgetingunnerdir": "pos gunner dir",
            "primarygunner": 1,
            "gunneroutopticseffect": [],
            "gunneropticseffect": ["TankGunnerOptics2","OpticsBlur1","OpticsCHAbera1"],
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
            "maxhorizontalrotspeed": 1.2,
            "maxverticalrotspeed": 1.2,
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
            "forcehidegunner": 0,
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
            }
        }
    },
    "hiddenselections": ["n1","n2","n3"],
    "hiddenselectionstextures": ["rhsafrf|addons|rhs_decals|Data|Labels|Misc|no_ca.paa","rhsafrf|addons|rhs_decals|Data|Labels|Misc|no_ca.paa","rhsafrf|addons|rhs_decals|Data|Labels|Misc|no_ca.paa"],
    # Class: CfgVehicles|rhs_pts_base|Attributes [Indent level: 1],
    "attributes": {
        # Class: CfgVehicles|rhs_pts_base|Attributes|ObjectTexture [Indent level: 2]
        "objecttexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayname": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        # Class: CfgVehicles|rhs_pts_base|Attributes|rhs_decalNumber_type [Indent level: 2],
        "rhs_decalnumber_type": {
            "displayname": "Define font type of plate number",
            "tooltip": "Define kind of font that will be drawn on vehicle.",
            "property": "rhs_decalNumber_type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];[_this,[['Number', cRHSPTSNumberPlaces, _value]]] call rhs_fnc_decalsInit",
            "defaultvalue": 0,
            "typename": "STRING",
            # Class: CfgVehicles|rhs_pts_base|Attributes|rhs_decalNumber_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_pts_base|Attributes|rhs_decalNumber_type|values|Default [Indent level: 4]
                "default": {
                    "name": "Default",
                    "value": "Default",
                    "defaultvalue": "Default"
                },
                # Class: CfgVehicles|rhs_pts_base|Attributes|rhs_decalNumber_type|values|DefaultRed [Indent level: 4],
                "defaultred": {
                    "name": "Default (Red)",
                    "value": "DefaultRed"
                },
                # Class: CfgVehicles|rhs_pts_base|Attributes|rhs_decalNumber_type|values|BoldRed [Indent level: 4],
                "boldred": {
                    "name": "Bold Red",
                    "value": "BoldRed"
                },
                # Class: CfgVehicles|rhs_pts_base|Attributes|rhs_decalNumber_type|values|CDF [Indent level: 4],
                "cdf": {
                    "name": "CDF",
                    "value": "CDF"
                },
                # Class: CfgVehicles|rhs_pts_base|Attributes|rhs_decalNumber_type|values|Handpaint [Indent level: 4],
                "handpaint": {
                    "name": "Handpaint",
                    "value": "Handpaint"
                },
                # Class: CfgVehicles|rhs_pts_base|Attributes|rhs_decalNumber_type|values|HandpaintBlack [Indent level: 4],
                "handpaintblack": {
                    "name": "Handpaint Black",
                    "value": "HandpaintBlack"
                },
                # Class: CfgVehicles|rhs_pts_base|Attributes|rhs_decalNumber_type|values|Iraqi [Indent level: 4],
                "iraqi": {
                    "name": "Iraqi",
                    "value": "Iraqi"
                },
                # Class: CfgVehicles|rhs_pts_base|Attributes|rhs_decalNumber_type|values|LicensePlate [Indent level: 4],
                "licenseplate": {
                    "name": "License Plate",
                    "value": "LicensePlate"
                }
            }
        },
        # Class: CfgVehicles|rhs_pts_base|Attributes|rhs_decalNumber [Indent level: 2],
        "rhs_decalnumber": {
            "collapsed": 1,
            "displayname": "Set side number",
            "tooltip": "Set side number. 3 numbers are required. Type 0 to hide numbers complety & leave at -1 to get random number",
            "property": "rhs_decalNumber",
            "control": "Edit",
            "validate": "Number",
            "typename": "Number",
            "defaultvalue": "-1",
            "expression": "if( _value >= 0)then{if( _value == 0)then{{[_this setobjectTexture [_x,'a3|data_f|clear_empty.paa']]}foreach cRHSPTSNumberPlaces}else{[_this, [['Number', cRHSPTSNumberPlaces, _this getVariable ['rhs_decalNumber_type','Default'], _value] ] ] call rhs_fnc_decalsInit}};"
        },
        # Class: CfgVehicles|rhs_pts_base|Attributes|rhs_openramp [Indent level: 2],
        "rhs_openramp": {
            "displayname": "Open ramp",
            "property": "rhs_opendoors",
            "control": "CheckboxNumber",
            "expression": "_this animateDoor ['ramp',_value];",
            "defaultvalue": "0"
        },
        # Class: CfgVehicles|rhs_pts_base|Attributes|rhs_attachCargo [Indent level: 2],
        "rhs_attachcargo": {
            "displayname": "Attach cargo",
            "tooltip": "Attaching cargo (using attachTo command) just like when you use ramp action",
            "property": "rhs_attachCargo",
            "expression": "if(_value == 1)then{[_this] spawn rhs_fnc_pts_cargoAttach}else{[_this] call rhs_fnc_pts_cargoDetach};",
            "control": "CheckboxNumber",
            "defaultvalue": "0"
        }
    },
    # Class: CfgVehicles|rhs_pts_base|Damage [Indent level: 1],
    "damage": {
        "tex": [],
        "mat": ["rhsafrf|addons|rhs_pts|data|rhs_pts.rvmat","rhsafrf|addons|rhs_pts|data|rhs_dam_pts.rvmat","rhsafrf|addons|rhs_pts|data|rhs_destr_pts.rvmat"]
    },
    # Class: CfgVehicles|rhs_pts_base|Exhausts [Indent level: 1],
    "exhausts": {
        # Class: CfgVehicles|rhs_pts_base|Exhausts|Exhaust1 [Indent level: 2]
        "exhaust1": {
            "position": "exhaustl",
            "direction": "exhaustl_dir",
            "effect": "ExhaustEffectTankSide"
        },
        # Class: CfgVehicles|rhs_pts_base|Exhausts|Exhaust2 [Indent level: 2],
        "exhaust2": {
            "position": "exhaustr",
            "direction": "exhaustr_dir",
            "effect": "ExhaustEffectTankSide"
        }
    },
    # Class: CfgVehicles|rhs_pts_base|AnimationSources [Indent level: 1],
    "animationsources": {
        # Class: CfgVehicles|rhs_pts_base|AnimationSources|ramp [Indent level: 2]
        "ramp": {
            "source": "door",
            "initphase": 0,
            "animperiod": 5,
            "sound": "ServoRampSound_2",
            "soundposition": "Ramp_01_axis"
        }
    },
    # Class: CfgVehicles|rhs_pts_base|VehicleTransport [Indent level: 1],
    "vehicletransport": {
        # Class: CfgVehicles|rhs_pts_base|VehicleTransport|Cargo [Indent level: 2]
        "cargo": {
            "parachuteclass": "O_Parachute_02_F",
            "parachuteheightlimit": 5,
            "canbetransported": 1,
            "dimensions": ["BBox_1_1_pos","BBox_1_2_pos"]
        },
        # Class: CfgVehicles|rhs_pts_base|VehicleTransport|Carrier [Indent level: 2],
        "carrier": {
            "cargobaydimensions": ["VVT_cargo_1","VVT_cargo_2"],
            "disableheightlimit": 1,
            "maxloadmass": 25000,
            "cargoalignment": ["center","front"],
            "cargospacing": [0,0,0],
            "exits": ["VVT_exit"],
            "unloadinginterval": 2,
            "loadingdistance": 5,
            "loadingangle": 60,
            "parachuteclassdefault": "O_Parachute_02_F",
            "parachuteheightlimitdefault": 5
        }
    },
    # Class: CfgVehicles|rhs_pts_base|Reflectors [Indent level: 1],
    "reflectors": {
        # Class: CfgVehicles|rhs_pts_base|Reflectors|Left [Indent level: 2]
        "left": {
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "position": "l svetlo",
            "direction": "konec l svetla",
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
            # Class: CfgVehicles|rhs_pts_base|Reflectors|Left|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardlimitstart": 30,
                "hardlimitend": 60
            }
        },
        # Class: CfgVehicles|rhs_pts_base|Reflectors|Left2 [Indent level: 2],
        "left2": {
            "direction": "konec l svetla",
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
            # Class: CfgVehicles|rhs_pts_base|Reflectors|Left|Attenuation [Indent level: 3],
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
    "aggregatereflectors": [["Left","Left2"]],
    "armorlights": 0.1,
    # Class: CfgVehicles|rhs_pts_base|ViewPilot [Indent level: 1],
    "viewpilot": {
        "initanglex": -12,
        "minanglex": -35,
        "maxanglex": 25,
        "initangley": 0,
        "minangley": -135,
        "maxangley": 135,
        "initfov": 0.7,
        "minfov": 0.3,
        "maxfov": 1,
        "minmovex": -0.075,
        "maxmovex": 0.075,
        "minmovey": -0.075,
        "maxmovey": 0.075,
        "minmovez": -0.075,
        "maxmovez": 0.1,
        "speedzoommaxspeed": 1e+010,
        "speedzoommaxfov": 0
    },
    # Class: CfgVehicles|rhs_pts_base|EventHandlers [Indent level: 1],
    "eventhandlers": {
        # Class: CfgVehicles|rhs_pts_base|EventHandlers|RHS_EventHandlers [Indent level: 2]
        "rhs_eventhandlers": {
            "init": "_this call rhs_fnc_pts_init",
            "postinit": "_this call rhs_fnc_reapplyTextures",
            "engine": "if((_this select 0) doorPhase 'ramp'> 0)then{_this select 0 engineOn false}else{[_this select 0,_this select 1,2] call rhs_fnc_engineStartupDelay};"
        },
        "init": "if (local (_this select 0)) then {[(_this select 0), `, [], false] call bis_fnc_initVehicle;};",
        "fired": "[_this select 0,_this select 6,'missile_move','MissileBase'] call BIS_fnc_missileLaunchPositionFix; _this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');"
    },
    # Class: CfgVehicles|rhs_pts_base|Components [Indent level: 1],
    "components": {
        # Class: CfgVehicles|rhs_pts_base|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 2]
        "vehiclesystemsdisplaymanagercomponentleft": {
            # Class: CfgVehicles|rhs_pts_base|Components|VehicleSystemsDisplayManagerComponentLeft|EmptyDisplay [Indent level: 3]
            "emptydisplay": {
                "componenttype": "EmptyDisplayComponent"
            },
            # Class: CfgVehicles|rhs_pts_base|Components|VehicleSystemsDisplayManagerComponentLeft|CrewDisplay [Indent level: 3],
            "crewdisplay": {
                "componenttype": "CrewDisplayComponent",
                "resource": "RscCustomInfoCrew"
            }
        },
        # Class: CfgVehicles|rhs_pts_base|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 2],
        "vehiclesystemsdisplaymanagercomponentright": {
            # Class: CfgVehicles|rhs_pts_base|Components|VehicleSystemsDisplayManagerComponentRight|EmptyDisplay [Indent level: 3]
            "emptydisplay": {
                "componenttype": "EmptyDisplayComponent"
            },
            # Class: CfgVehicles|rhs_pts_base|Components|VehicleSystemsDisplayManagerComponentRight|CrewDisplay [Indent level: 3],
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
    "_generalmacro": "APC_Tracked_02_base_F",
    "brakeidlespeed": 0.1,
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
    "scope": 0,
    # Class: CfgVehicles|APC_Tracked_02_base_F|Library [Indent level: 1],
    "library": {
        "libtextdesc": "The infantry fighting vehicle BTR-K Kamysh and its anti-aircraft cousin ZSU-39 Tigris share the same vehicle platform. Developed by Russia with a pinch of undeniable inspiration from Israeli IFVs, they serve in the OPFOR army as a prime example of a leveling of the technology field with the West. The Kamysh is equipped with a CTWS turret fitted with a 30 mm cannon, coaxial machinegun and 2 guided AT missiles, making the vehicle significant in the infantry support role. The Tigris is fitted with a 35 mm autocannon and 4 Titan AA missiles."
    },
    "memorypointtaskmarker": "TaskMarker_1_pos",
    "hideweaponsdriver": 1,
    "hideweaponscargo": 1,
    "viewdriverinexternal": 1,
    "viewdrivershadowamb": 0.5,
    "viewdrivershadowdiff": 0.05,
    "loddriverturnedout": 0,
    "loddriveropticsin": 1202,
    "driverinfopanelcamerapos": "driverview_old",
    "driverleftleganimname": "pedal_brake",
    "driverrightleganimname": "pedal_thrust",
    # Class: CfgVehicles|APC_Tracked_02_base_F|ViewOptics [Indent level: 1],
    "viewoptics": {
        "visionmode": ["Normal","NVG"],
        "initfov": 0.25,
        "minfov": 0.13,
        "maxfov": 0.25,
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
    "crewexplosionprotection": 0.999,
    "threat": [0.8,0.6,0.6],
    "waterppinvehicle": 0,
    "firedusteffect": "emptyEffect",
    "animationsourcehatch": "",
    "insidesoundcoef": 0.9,
    "soundlocked": ["|A3|Sounds_F|weapons|Rockets|locked_1",1,1],
    "soundincommingmissile": ["|A3|Sounds_F|vehicles|air|noises|alarm_locked_by_missile_4",0.398107,1],
    "smokelaunchergrenadecount": 8,
    "smokelaunchervelocity": 14,
    "smokelauncheronturret": 0,
    "smokelauncherangle": 120,
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
    "sensorposition": "gunnerView",
    "audible": 18,
    "sensitivityear": "0.0075 /3",
    "turncoef": 5,
    "steeraheadsimul": 0.3,
    "steeraheadplan": 0.4,
    "brakedistance": 5,
    "precision": 10,
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
    "type": 1,
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
    "unitinfotype": "RscUnitInfoTank",
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
    "features": "",
    "insidedetectcoef": 0.05,
}