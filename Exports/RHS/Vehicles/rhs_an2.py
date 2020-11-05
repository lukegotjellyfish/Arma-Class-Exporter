rhs_an2 = {
    "editorpreview": "rhsgref|addons|rhsgref_editorPreviews|data|RHS_AN2.paa",
    "accuracy": 0.5,
    "author": "Red Hammer Studios",
    "scope": 2,
    "side": 2,
    "faction": "rhsgref_faction_cdf_air",
    "crew": "rhsgref_cdf_air_pilot",
    "typicalcargo": ["rhsgref_cdf_air_pilot"],
    "displayname": "Antonov An-2",
    "rhs_decalparameters": ["['Number',[3,4],'AviaCDF']","['Label',[5],'Aviation', 4]","['Label',[6],'AviationSquadronsCDF']"],
    "cabinopening": 0,
    "dlc": "RHS_GREF",
    "simulation": "airplaneX",
    "destrtype": "DestructWreck",
    "vehicleclass": "rhs_vehclass_aircraft",
    "model": "rhsgref|addons|rhsgref_air|AN2|AN2.p3d",
    "picture": "rhsgref|addons|rhsgref_air|AN2|data|UI|picture_an2_CA.paa",
    "icon": "rhsgref|addons|rhsgref_air|AN2|data|UI|icon_an2_CA.paa",
    "mapsize": 20,
    "memorypointsgetincargo": ["pos cargo"],
    "memorypointsgetincargodir": ["pos cargo dir"],
    "memorypointsgetindriver": "pos cargo",
    "memorypointsgetindriverdir": "pos cargo dir",
    "getinaction": "GetInHigh",
    "getoutaction": "GetOutHigh",
    "cargogetinaction": ["GetInHigh"],
    "cargogetoutaction": ["GetOutHigh"],
    "cost": 20000,
    "gearretracting": 0,
    "driveraction": "RHS_AN2_Pilot",
    "cargoaction": ["RHS_AN2_Cargo01","RHS_AN2_Cargo02","RHS_AN2_Cargo01","RHS_AN2_Cargo03","RHS_AN2_Cargo02","RHS_AN2_Cargo01","RHS_AN2_Cargo03","RHS_AN2_Cargo01","RHS_AN2_Cargo03","RHS_AN2_Cargo02","RHS_AN2_Cargo01","RHS_AN2_Cargo02","RHS_AN2_Cargo02","RHS_AN2_Cargo03"],
    "cargoiscodriver": [1,0],
    "transportsoldier": 12,
    "drivercompartments": "Compartment1",
    "cargocompartments": ["Compartment1"],
    "insidesoundcoef": 0.2,
    "attenuationeffecttype": "HeliAttenuation",
    "soundgetin": ["rhsgref|addons|rhsgref_air|AN2|data|sound|close",0.316228,1],
    "soundgetout": ["rhsgref|addons|rhsgref_air|AN2|data|sound|open",0.316228,1,40],
    "sounddammage": ["",0.562341,1],
    "soundengineonint": ["rhsgref|addons|rhsgref_air|AN2|data|sound|AN2_engine_start_int",0.177828,1],
    "soundengineonext": ["rhsgref|addons|rhsgref_air|AN2|data|sound|AN2_engine_start_ext",0.398107,1,700],
    "soundengineoffint": ["rhsgref|addons|rhsgref_air|AN2|data|sound|AN2_engine_stop_int",0.177828,1],
    "soundengineoffext": ["rhsgref|addons|rhsgref_air|AN2|data|sound|AN2_engine_stop_ext",0.398107,1,700],
    "soundlocked": ["|A3|Sounds_F|weapons|Rockets|locked_1",0.1,1],
    "soundincommingmissile": ["|A3|Sounds_F|weapons|Rockets|locked_3",0.1,1.5],
    # Class: CfgVehicles|RHS_AN2_Base|Sounds [Indent level: 1],
    "sounds": {
        # Class: CfgVehicles|RHS_AN2_Base|Sounds|EngineLowOut [Indent level: 2]
        "enginelowout": {
            "sound": ["rhsgref|addons|rhsgref_air|AN2|data|sound|AN2_engine_low_ext",1.77828,1,900],
            "frequency": "1.0 min (rpm + 0.5)",
            "volume": "camPos*engineOn*(rpm factor[0.85, 0])"
        },
        # Class: CfgVehicles|RHS_AN2_Base|Sounds|EngineHighOut [Indent level: 2],
        "enginehighout": {
            "sound": ["rhsgref|addons|rhsgref_air|AN2|data|sound|AN2_engine_high_ext",1.77828,1,1100],
            "frequency": "1",
            "volume": "camPos*engineOn*(rpm factor[0.55, 1.0])"
        },
        # Class: CfgVehicles|RHS_AN2_Base|Sounds|ForsageOut [Indent level: 2],
        "forsageout": {
            "sound": ["rhsgref|addons|rhsgref_air|AN2|data|sound|AN2_engine_high_ext",1.41254,1,1500],
            "frequency": "1",
            "volume": "camPos*engineOn*(thrust factor[0.5, 1.0])",
            "cone": [1.14,3.92,2,0.4]
        },
        # Class: CfgVehicles|RHS_AN2_Base|Sounds|WindNoiseOut [Indent level: 2],
        "windnoiseout": {
            "sound": ["rhsgref|addons|rhsgref_air|AN2|data|sound|ext-wind",0.001,0.6,150],
            "frequency": "(0.1+(1.2*(speed factor[1, 100])))",
            "volume": "camPos*(speed factor[1, 100])"
        },
        # Class: CfgVehicles|RHS_AN2_Base|Sounds|EngineLowIn [Indent level: 2],
        "enginelowin": {
            "sound": ["rhsgref|addons|rhsgref_air|AN2|data|sound|AN2_engine_low_int",1,1],
            "frequency": "1.0 min (rpm + 0.5)",
            "volume": "(1-camPos)*(engineOn*(rpm factor[0.85, 0]))"
        },
        # Class: CfgVehicles|RHS_AN2_Base|Sounds|EngineHighIn [Indent level: 2],
        "enginehighin": {
            "sound": ["rhsgref|addons|rhsgref_air|AN2|data|sound|AN2_engine_high_int",1,1],
            "frequency": "1",
            "volume": "(1-camPos)*(engineOn*(rpm factor[0.55, 1.0]))"
        },
        # Class: CfgVehicles|RHS_AN2_Base|Sounds|ForsageIn [Indent level: 2],
        "forsagein": {
            "sound": ["rhsgref|addons|rhsgref_air|AN2|data|sound|AN2_engine_high_int",1.41254,1.1],
            "frequency": "1",
            "volume": "(1-camPos)*(engineOn*(thrust factor[0.5, 1.0]))"
        },
        # Class: CfgVehicles|RHS_AN2_Base|Sounds|WindNoiseIn [Indent level: 2],
        "windnoisein": {
            "sound": ["rhsgref|addons|rhsgref_air|AN2|data|sound|int-wind",0.001,0.6],
            "frequency": "(0.1+(1.2*(speed factor[1, 100])))",
            "volume": "(1-camPos)*(speed factor[1, 100])"
        }
    },
    "weapons": [],
    "magazines": [],
    "threat": [0,0,0],
    "airbrake": 0,
    "maxspeed": 258,
    "landingspeed": 85,
    "takeoffspeed": 90,
    "landingaoa": "rad(10)",
    "flapsfrictioncoef": 0.95,
    "rudderinfluence": 0.5,
    "aileronsensitivity": 0.4,
    "elevatorsensitivity": 0.4,
    "envelope": [0,0,0.43,1.2,2.3,2.42,3.53,7.12,8.56,11.05,9.39,7.94,5.2,2.82,0],
    "angleofindicence": 0,
    "draconicforcexcoef": 3.15,
    "draconicforceycoef": 0.5,
    "draconicforcezcoef": 0.5,
    "draconictorquexcoef": 0.15,
    "draconictorqueycoef": 3.15,
    "thrustcoef": [1.4,1.3,1.2,1.2,1.1,1.1,1,1,0.9,0.7,0.5,0.3,0.1,0,0,0],
    "maxomega": 2000,
    "turncoef": 1.5,
    # Class: CfgVehicles|RHS_AN2_Base|Wheels [Indent level: 1],
    "wheels": {
        # Class: CfgVehicles|RHS_AN2_Base|Wheels|Wheel_1 [Indent level: 2]
        "wheel_1": {
            "steering": 1,
            "side": "left",
            "bonename": "Wheel_1_1",
            "center": "wheel_1_1_center",
            "boundary": "wheel_1_1_bound",
            "suspforceapppointoffset": "Wheel_1_1_center",
            "tireforceapppointoffset": "Wheel_1_1_center",
            "width": 0.3,
            "mass": 50,
            "moi": 8,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 10,
            "maxhandbraketorque": 0,
            "susptraveldirection": [0,-1,0],
            "maxcompression": 0.1,
            "maxdroop": 0.1,
            "sprungmass": 2400,
            "springstrength": 100000,
            "springdamperrate": 128000,
            "longitudinalstiffnessperunitgravity": 90,
            "latstiffx": 15,
            "latstiffy": 120,
            "frictionvsslipgraph": [[0,2],[0.5,1],[1,1]]
        },
        # Class: CfgVehicles|RHS_AN2_Base|Wheels|Wheel_2 [Indent level: 2],
        "wheel_2": {
            "bonename": "wheel_1_2",
            "center": "wheel_1_2_center",
            "boundary": "wheel_1_2_bound",
            "suspforceapppointoffset": "Wheel_1_2_center",
            "tireforceapppointoffset": "Wheel_1_2_center",
            "steering": 1,
            "side": "left",
            "width": 0.3,
            "mass": 50,
            "moi": 8,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 10,
            "maxhandbraketorque": 0,
            "susptraveldirection": [0,-1,0],
            "maxcompression": 0.1,
            "maxdroop": 0.1,
            "sprungmass": 2400,
            "springstrength": 100000,
            "springdamperrate": 128000,
            "longitudinalstiffnessperunitgravity": 90,
            "latstiffx": 15,
            "latstiffy": 120,
            "frictionvsslipgraph": [[0,2],[0.5,1],[1,1]]
        },
        # Class: CfgVehicles|RHS_AN2_Base|Wheels|Wheel_3 [Indent level: 2],
        "wheel_3": {
            "steering": 0,
            "side": "left",
            "bonename": "Wheel_2_1",
            "center": "wheel_2_1_center",
            "boundary": "wheel_2_1_bound",
            "suspforceapppointoffset": "Wheel_2_1_center",
            "tireforceapppointoffset": "Wheel_2_1_center",
            "width": 0.16,
            "maxcompression": 0.1,
            "maxdroop": 0.1,
            "sprungmass": 700,
            "springstrength": 1.58e+006,
            "springdamperrate": 12000,
            "mass": 50,
            "moi": 8,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 10,
            "maxhandbraketorque": 0,
            "susptraveldirection": [0,-1,0],
            "longitudinalstiffnessperunitgravity": 90,
            "latstiffx": 15,
            "latstiffy": 120,
            "frictionvsslipgraph": [[0,2],[0.5,1],[1,1]]
        }
    },
    "wheelsteeringsensitivity": 2,
    "ejectspeed": [0,0,0],
    "extcameraposition": [0,5,-20],
    "lightongear": 0,
    "driverlefthandanimname": "left_stick_aileron",
    "driverrighthandanimname": "left_stick_aileron",
    "armor": 25,
    "damageresistance": 0.00278,
    # Class: CfgVehicles|RHS_AN2_Base|HitPoints [Indent level: 1],
    "hitpoints": {
        # Class: CfgVehicles|RHS_AN2_Base|HitPoints|HitHull [Indent level: 2]
        "hithull": {
            "armor": 1.5,
            "explosionshielding": 1,
            "passthrough": 0.5,
            "minimalhit": 0,
            "material": -1,
            "radius": 0.3,
            "name": "HitHull",
            "visual": "vis_hull",
            "depends": "Total"
        },
        # Class: CfgVehicles|RHS_AN2_Base|HitPoints|HitEngine [Indent level: 2],
        "hitengine": {
            "armor": 0.5,
            "explosionshielding": 1,
            "passthrough": 0.2,
            "minimalhit": 0.1,
            "material": -1,
            "radius": 0.15,
            "name": "hit_engine",
            "visual": "vis_engine",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_AN2_Base|HitPoints|HitFuel [Indent level: 2],
        "hitfuel": {
            "armor": 1.5,
            "explosionshielding": 2,
            "passthrough": 0.2,
            "minimalhit": 0,
            "material": -1,
            "radius": 0.1,
            "name": "hit_fuel_l",
            "visual": "vis_wing_lh",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_AN2_Base|HitPoints|HitFuel2 [Indent level: 2],
        "hitfuel2": {
            "armor": 1.5,
            "explosionshielding": 2,
            "passthrough": 0.2,
            "minimalhit": 0,
            "material": -1,
            "radius": 0.1,
            "name": "hit_fuel_r",
            "visual": "vis_wing_rh",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_AN2_Base|HitPoints|HitLAileron_link [Indent level: 2],
        "hitlaileron_link": {
            "armor": 0.3,
            "explosionshielding": 0.9,
            "passthrough": 0.01,
            "minimalhit": 0.03,
            "material": -1,
            "radius": 0.1,
            "name": "hit_aileron_link_l",
            "visual": "",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_AN2_Base|HitPoints|HitLAileron_1 [Indent level: 2],
        "hitlaileron_1": {
            "armor": 1.5,
            "explosionshielding": 3,
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "material": -1,
            "radius": 0.12,
            "name": "hit_aileron_lh",
            "visual": "vis_wing_lh",
            "depends": "HitLAileron_link*0.7"
        },
        # Class: CfgVehicles|RHS_AN2_Base|HitPoints|HitLAileron_2 [Indent level: 2],
        "hitlaileron_2": {
            "armor": 1.5,
            "explosionshielding": 3,
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "material": -1,
            "radius": 0.1,
            "name": "hit_aileron_ld",
            "visual": "vis_wing_ld",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_AN2_Base|HitPoints|HitLAileron [Indent level: 2],
        "hitlaileron": {
            "armor": 1.5,
            "explosionshielding": 3,
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "material": -1,
            "radius": 0.12,
            "name": "hit_aileron_lh",
            "visual": "vis_wing_lh",
            "depends": "(HitLAileron_1 + HitLAileron_2)*0.5"
        },
        # Class: CfgVehicles|RHS_AN2_Base|HitPoints|HitRAileron_link [Indent level: 2],
        "hitraileron_link": {
            "armor": 0.3,
            "explosionshielding": 0.9,
            "passthrough": 0.01,
            "minimalhit": 0.03,
            "material": -1,
            "radius": 0.1,
            "name": "hit_aileron_link_r",
            "visual": "",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_AN2_Base|HitPoints|HitRAileron_1 [Indent level: 2],
        "hitraileron_1": {
            "armor": 1.5,
            "explosionshielding": 3,
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "material": -1,
            "radius": 0.12,
            "name": "hit_aileron_rh",
            "visual": "vis_wing_rh",
            "depends": "HitRAileron_link*0.7"
        },
        # Class: CfgVehicles|RHS_AN2_Base|HitPoints|HitRAileron_2 [Indent level: 2],
        "hitraileron_2": {
            "armor": 1.5,
            "explosionshielding": 3,
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "material": -1,
            "radius": 0.1,
            "name": "hit_aileron_rd",
            "visual": "vis_wing_rd",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_AN2_Base|HitPoints|HitRAileron [Indent level: 2],
        "hitraileron": {
            "armor": 1.5,
            "explosionshielding": 3,
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "material": -1,
            "radius": 0.12,
            "name": "hit_aileron_rh",
            "visual": "vis_wing_rh",
            "depends": "(HitRAileron_1 + HitRAileron_2)*0.5"
        },
        # Class: CfgVehicles|RHS_AN2_Base|HitPoints|HitControlRear [Indent level: 2],
        "hitcontrolrear": {
            "armor": 0.6,
            "explosionshielding": 0.1,
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "radius": 0.04,
            "material": -1,
            "name": "hit_control_rear",
            "visual": "-",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_AN2_Base|HitPoints|HitLCRudder [Indent level: 2],
        "hitlcrudder": {
            "armor": 1.5,
            "explosionshielding": 3,
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "material": -1,
            "radius": 0.15,
            "name": "hit_rudder",
            "visual": "vis_rudder",
            "depends": "HitControlRear"
        },
        # Class: CfgVehicles|RHS_AN2_Base|HitPoints|HitLCElevator [Indent level: 2],
        "hitlcelevator": {
            "armor": 1.5,
            "explosionshielding": 3,
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "material": -1,
            "radius": 0.11,
            "name": "hit_elevator_l",
            "visual": "vis_elevator_l",
            "depends": "HitControlRear"
        },
        # Class: CfgVehicles|RHS_AN2_Base|HitPoints|HitRElevator [Indent level: 2],
        "hitrelevator": {
            "armor": 1.5,
            "explosionshielding": 3,
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "material": -1,
            "radius": 0.11,
            "name": "hit_elevator_r",
            "visual": "vis_elevator_r",
            "depends": "HitControlRear"
        },
        # Class: CfgVehicles|RHS_AN2_Base|HitPoints|HitGlass1 [Indent level: 2],
        "hitglass1": {
            "armor": 0.1,
            "material": -1,
            "name": "glass1",
            "visual": "glass1",
            "passthrough": 0
        },
        # Class: CfgVehicles|RHS_AN2_Base|HitPoints|HitGlass2 [Indent level: 2],
        "hitglass2": {
            "armor": 0.1,
            "material": -1,
            "name": "glass2",
            "visual": "glass2",
            "passthrough": 0
        },
        # Class: CfgVehicles|RHS_AN2_Base|HitPoints|HitGlass3 [Indent level: 2],
        "hitglass3": {
            "armor": 0.1,
            "material": -1,
            "name": "glass3",
            "visual": "glass3",
            "passthrough": 0
        },
        # Class: CfgVehicles|RHS_AN2_Base|HitPoints|HitGlass4 [Indent level: 2],
        "hitglass4": {
            "armor": 0.1,
            "material": -1,
            "name": "glass4",
            "visual": "glass4",
            "passthrough": 0
        }
    },
    # Class: CfgVehicles|RHS_AN2_Base|AnimationSources [Indent level: 1],
    "animationsources": {
        # Class: CfgVehicles|RHS_AN2_Base|AnimationSources|HitGlass1 [Indent level: 2]
        "hitglass1": {
            "source": "Hit",
            "hitpoint": "HitGlass1",
            "raw": 1
        },
        # Class: CfgVehicles|RHS_AN2_Base|AnimationSources|HitGlass2 [Indent level: 2],
        "hitglass2": {
            "hitpoint": "HitGlass2",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|RHS_AN2_Base|AnimationSources|HitGlass3 [Indent level: 2],
        "hitglass3": {
            "hitpoint": "HitGlass3",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|RHS_AN2_Base|AnimationSources|HitGlass4 [Indent level: 2],
        "hitglass4": {
            "hitpoint": "HitGlass4",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|RHS_AN2_Base|AnimationSources|hideDoor [Indent level: 2],
        "hidedoor": {
            "displayname": "Hide Door...",
            "author": "Community Upgrade Project",
            "source": "user",
            "animperiod": 1e-006,
            "initphase": 0,
            "forceanimatephase": 0,
            "forceanimate": [],
            "mass": 20
        },
        # Class: CfgVehicles|RHS_AN2_Base|AnimationSources|door [Indent level: 2],
        "door": {
            "source": "user",
            "animperiod": 2.5,
            "sound": "ServoRampSound_2"
        }
    },
    # Class: CfgVehicles|RHS_AN2_Base|Damage [Indent level: 1],
    "damage": {
        "tex": [],
        "mat": ["rhsgref|addons|rhsgref_air|AN2|Data|an2_1.rvmat","rhsgref|addons|rhsgref_air|AN2|Data|an2_1_damage.rvmat","rhsgref|addons|rhsgref_air|AN2|Data|an2_1_destruct.rvmat","rhsgref|addons|rhsgref_air|AN2|Data|an2_2.rvmat","rhsgref|addons|rhsgref_air|AN2|Data|an2_2_damage.rvmat","rhsgref|addons|rhsgref_air|AN2|Data|an2_2_destruct.rvmat","rhsgref|addons|rhsgref_air|AN2|Data|an2_interier.rvmat","rhsgref|addons|rhsgref_air|AN2|Data|an2_interier_damage.rvmat","rhsgref|addons|rhsgref_air|AN2|Data|an2_interier_destruct.rvmat","rhsgref|addons|rhsgref_air|AN2|Data|an2_cockpit.rvmat","rhsgref|addons|rhsgref_air|AN2|Data|an2_cockpit_damage.rvmat","rhsgref|addons|rhsgref_air|AN2|Data|an2_cockpit_destruct.rvmat","rhsgref|addons|rhsgref_air|AN2|Data|an2_wings.rvmat","rhsgref|addons|rhsgref_air|AN2|Data|an2_wings_damage.rvmat","rhsgref|addons|rhsgref_air|AN2|Data|an2_wings_destruct.rvmat","rhsgref|addons|rhsgref_air|AN2|Data|an2_window.rvmat","rhsgref|addons|rhsgref_air|AN2|Data|an2_window_damage.rvmat","rhsgref|addons|rhsgref_air|AN2|Data|an2_window_destruct.rvmat","a3|data_f|default.rvmat","a3|data_f|default.rvmat","a3|data_f|default_destruct.rvmat"]
    },
    "driveoncomponent": [],
    "driverleftleganimname": "pedal_l",
    "driverrightleganimname": "pedal_r",
    # Class: CfgVehicles|RHS_AN2_Base|Turrets [Indent level: 1],
    "turrets": {
        # Class: CfgVehicles|RHS_AN2_Base|Turrets|MainTurret [Indent level: 2]
        "mainturret": {
            "startengine": 0,
            "outgunnermayfire": 1,
            "commanding": -1,
            "weapons": [],
            "magazines": [],
            "body": "",
            "gun": "",
            "animationsourcebody": "",
            "animationsourcegun": "",
            "memorypointsgetingunner": "pos driver",
            "memorypointsgetingunnerdir": "pos driver dir",
            "gunnergetinaction": "GetInLow",
            "gunnergetoutaction": "GetOutLow",
            "memorypointgun": "machinegun",
            "memorypointgunneroptics": "gunnerview",
            "gunnername": "Copilot",
            "selectionfireanim": "zasleh",
            "castgunnershadow": 1,
            "viewgunnershadow": 1,
            "minelev": -50,
            "maxelev": 30,
            "initelev": 11,
            "minturn": -170,
            "maxturn": 170,
            "initturn": 0,
            "gunneraction": "RHS_AN2_Cargo",
            "gunnerinaction": "RHS_AN2_Cargo",
            "gunneropticsmodel": "A3|Weapons_F|empty.p3d",
            "gunnerforceoptics": 0,
            "enablemanualfire": 0,
            "lodturnedin": 1100,
            "lodturnedout": 1100,
            # Class: CfgVehicles|RHS_AN2_Base|Turrets|MainTurret|ViewPilot [Indent level: 3],
            "viewpilot": {
                "minanglex": -65,
                "maxanglex": 85,
                "initanglex": 0,
                "minangley": -150,
                "maxangley": 150,
                "initangley": 0,
                "minfov": 0.3,
                "maxfov": 1.2,
                "initfov": 1,
                "minmovex": -0.2,
                "maxmovex": 0.2,
                "minmovey": -0.1,
                "maxmovey": 0.1,
                "minmovez": -0.1,
                "maxmovez": 0.2,
                "speedzoommaxspeed": 1e+010,
                "speedzoommaxfov": 0
            },
            "iscopilot": 1,
            "primarygunner": 0,
            "caneject": 0,
            "gunnernotspawned": 0,
            "gunnerusepilotview": 1,
            # Class: CfgVehicles|RHS_AN2_Base|Turrets|MainTurret|HitPoints [Indent level: 3],
            "hitpoints": {
            },
            "gunnerlefthandanimname": "yoke_copilot",
            "gunnerrighthandanimname": "right_stick_aileron",
            "gunnerleftleganimname": "pedal_l_copilot",
            "gunnerrightleganimname": "pedal_r_copilot",
            "turretcansee": 15,
            # Class: CfgVehicles|RHS_AN2_Base|Turrets|MainTurret|Components [Indent level: 3],
            "components": {
                # Class: CfgVehicles|RHS_AN2_Base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 4]
                "vehiclesystemsdisplaymanagercomponentleft": {
                    # Class: CfgVehicles|RHS_AN2_Base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft|Components [Indent level: 5]
                    "components": {
                        # Class: CfgVehicles|RHS_AN2_Base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft|Components|CrewDisplay [Indent level: 6]
                        "crewdisplay": {
                            "componenttype": "CrewDisplayComponent",
                            "resource": "RscCustomInfoCrew"
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
                # Class: CfgVehicles|RHS_AN2_Base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 4],
                "vehiclesystemsdisplaymanagercomponentright": {
                    "defaultdisplay": "",
                    # Class: CfgVehicles|RHS_AN2_Base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight|Components [Indent level: 5],
                    "components": {
                        # Class: CfgVehicles|RHS_AN2_Base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight|Components|CrewDisplay [Indent level: 6]
                        "crewdisplay": {
                            "componenttype": "CrewDisplayComponent",
                            "resource": "RscCustomInfoCrew"
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
                    "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,	((safezoneX + safezoneW) - (		(10 * 			(			((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40)))])",
                    "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                }
            },
            "animationsourcehatch": "hatchGunner",
            "animationsourcecamelev": "camElev",
            "proxytype": "CPGunner",
            "proxyindex": 1,
            "gunnertype": "",
            "primaryobserver": 0,
            "soundservo": ["",0.00316228,1],
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
            "stabilizedinaxes": 3,
            "primary": 1,
            "hasgunner": 1,
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
            "gunneropticscolor": [0,0,0,1],
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
            "viewgunnershadowdiff": 1,
            "viewgunnershadowamb": 1,
            "ejectdeadgunner": 0,
            "hideweaponsgunner": 1,
            "canhidegunner": -1,
            "forcehidegunner": 0,
            "ingunnermayfire": 1,
            "showhmd": 0,
            "viewgunnerinexternal": 0,
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
            "gunbeg": "usti hlavne",
            "gunend": "konec hlavne",
            "showcrewaim": 0
        },
        # Class: CfgVehicles|Plane_Base_F|Turrets|CopilotTurret [Indent level: 2],
        "copilotturret": {
            "primarygunner": 0,
            "gunnerforceoptics": 0,
            "body": "",
            "gun": "",
            "animationsourcebody": "",
            "animationsourcegun": "",
            "weapons": [],
            "magazines": [],
            "gunnergetinaction": "GetInHigh",
            "gunnergetoutaction": "GetOutHigh",
            "gunnername": "Copilot",
            "gunnernotspawned": 1,
            "memorypointsgetingunner": "pos codriver",
            "memorypointsgetingunnerdir": "pos codriver dir",
            "minelev": -50,
            "maxelev": 30,
            "initelev": 11,
            "minturn": -170,
            "maxturn": 170,
            "initturn": 0,
            "maxhorizontalrotspeed": 3,
            "maxverticalrotspeed": 3,
            "startengine": 0,
            "gunnerusespilotview": 1,
            # Class: CfgVehicles|Plane_Base_F|Turrets|CopilotTurret|ViewGunner [Indent level: 3],
            "viewgunner": {
                "initfov": 0.75,
                "minfov": 0.25,
                "maxfov": 1.25,
                "initanglex": 0,
                "initangley": 0,
                "minanglex": -65,
                "maxanglex": 85,
                "minangley": -150,
                "maxangley": 150,
                "minmovex": -0.2,
                "maxmovex": 0.2,
                "minmovey": -0.1,
                "maxmovey": 0.1,
                "minmovez": -0.1,
                "maxmovez": 0.2,
                "speedzoommaxspeed": 1e+010,
                "speedzoommaxfov": 0
            },
            "commanding": -1,
            "turretcansee": "1 + 2 + 4 + 8 + 32",
            "animationsourcehatch": "hatchGunner",
            "animationsourcecamelev": "camElev",
            "proxytype": "CPGunner",
            "proxyindex": 1,
            "gunnertype": "",
            "primaryobserver": 0,
            "soundservo": ["",0.00316228,1],
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
            "stabilizedinaxes": 3,
            "primary": 1,
            "hasgunner": 1,
            "canusescanners": 1,
            # Class: CfgVehicles|AllVehicles|NewTurret|TurretSpec [Indent level: 2],
            "turretspec": {
                "showheadphones": 0
            },
            "gunneropticsmodel": "",
            "gunneropticscolor": [0,0,0,1],
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
            "memorypointgun": "kulas",
            "selectionfireanim": "zasleh",
            "showcrewaim": 0
        }
    },
    # Class: CfgVehicles|RHS_AN2_Base|Components [Indent level: 1],
    "components": {
        # Class: CfgVehicles|RHS_AN2_Base|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 2]
        "vehiclesystemsdisplaymanagercomponentleft": {
            # Class: CfgVehicles|RHS_AN2_Base|Components|VehicleSystemsDisplayManagerComponentLeft|Components [Indent level: 3]
            "components": {
                # Class: CfgVehicles|RHS_AN2_Base|Components|VehicleSystemsDisplayManagerComponentLeft|Components|CrewDisplay [Indent level: 4]
                "crewdisplay": {
                    "componenttype": "CrewDisplayComponent",
                    "resource": "RscCustomInfoCrew"
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
        # Class: CfgVehicles|RHS_AN2_Base|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 2],
        "vehiclesystemsdisplaymanagercomponentright": {
            "defaultdisplay": "",
            # Class: CfgVehicles|RHS_AN2_Base|Components|VehicleSystemsDisplayManagerComponentRight|Components [Indent level: 3],
            "components": {
                # Class: CfgVehicles|RHS_AN2_Base|Components|VehicleSystemsDisplayManagerComponentRight|Components|CrewDisplay [Indent level: 4]
                "crewdisplay": {
                    "componenttype": "CrewDisplayComponent",
                    "resource": "RscCustomInfoCrew"
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
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,	((safezoneX + safezoneW) - (		(10 * 			(			((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40)))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
        }
    },
    # Class: CfgVehicles|RHS_AN2_Base|Reflectors [Indent level: 1],
    "reflectors": {
        # Class: CfgVehicles|RHS_AN2_Base|Reflectors|Left [Indent level: 2]
        "left": {
            "color": [7000,7500,10000,1],
            "ambient": [100,100,100,0],
            "position": "light_l",
            "direction": "light_l_dir",
            "hitpoint": "light_l",
            "selection": "light_l",
            "size": 1,
            "innerangle": 20,
            "outerangle": 60,
            "conefadecoef": 10,
            "intensity": 50,
            "useflare": 1,
            "daylight": 0,
            "flaresize": 6,
            # Class: CfgVehicles|RHS_AN2_Base|Reflectors|Left|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 4
            }
        },
        # Class: CfgVehicles|RHS_AN2_Base|Reflectors|Right [Indent level: 2],
        "right": {
            "position": "light_r",
            "direction": "light_r_dir",
            "hitpoint": "light_r",
            "selection": "light_r",
            "color": [7000,7500,10000,1],
            "ambient": [100,100,100,0],
            "size": 1,
            "innerangle": 20,
            "outerangle": 60,
            "conefadecoef": 10,
            "intensity": 50,
            "useflare": 1,
            "daylight": 0,
            "flaresize": 6,
            # Class: CfgVehicles|RHS_AN2_Base|Reflectors|Left|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 4
            }
        }
    },
    # Class: CfgVehicles|RHS_AN2_Base|Exhausts [Indent level: 1],
    "exhausts": {
        # Class: CfgVehicles|RHS_AN2_Base|Exhausts|Exhaust1 [Indent level: 2]
        "exhaust1": {
            "direction": "exhaust1_dir",
            "effect": "ExhaustsEffectPlane",
            "position": "exhaust1"
        }
    },
    "hiddenselections": ["Camo1","Camo2","Camo3","n1","n2","i1","i2"],
    "hiddenselectionstextures": ["rhsgref|addons|rhsgref_air|an2|data|an2_1_co.paa","rhsgref|addons|rhsgref_air|an2|data|an2_2_co.paa","rhsgref|addons|rhsgref_air|an2|data|an2_wings_co.paa"],
    # Class: CfgVehicles|RHS_AN2_Base|textureSources [Indent level: 1],
    "texturesources": {
        # Class: CfgVehicles|RHS_AN2_Base|textureSources|standardCDF [Indent level: 2]
        "standardcdf": {
            "displayname": "CDF",
            "author": "Red Hammer Studios",
            "textures": ["rhsgref|addons|rhsgref_air|an2|data|an2_1_co.paa","rhsgref|addons|rhsgref_air|an2|data|an2_2_co.paa","rhsgref|addons|rhsgref_air|an2|data|an2_wings_co.paa"],
            "factions": ["rhsgref_faction_cdf_air"]
        },
        # Class: CfgVehicles|RHS_AN2_Base|textureSources|aeroschrot [Indent level: 2],
        "aeroschrot": {
            "displayname": "АэроШрот",
            "author": "Bohemia Interactive",
            "textures": ["rhsgref|addons|rhsgref_air|AN2|data|an2_1_A_CO","rhsgref|addons|rhsgref_air|AN2|data|an2_2_A_CO","rhsgref|addons|rhsgref_air|AN2|data|an2_wings_A_CO"],
            "factions": []
        },
        # Class: CfgVehicles|RHS_AN2_Base|textureSources|airtak [Indent level: 2],
        "airtak": {
            "displayname": "AirTak",
            "author": "Bohemia Interactive",
            "textures": ["rhsgref|addons|rhsgref_air|AN2|data|an2_1_B_CO","rhsgref|addons|rhsgref_air|AN2|data|an2_2_B_CO","rhsgref|addons|rhsgref_air|AN2|data|an2_wings_B_CO"],
            "factions": []
        },
        # Class: CfgVehicles|RHS_AN2_Base|textureSources|military [Indent level: 2],
        "military": {
            "displayname": "Military",
            "author": "Bohemia Interactive",
            "textures": ["rhsgref|addons|rhsgref_air|AN2|data|an2_1_CO","rhsgref|addons|rhsgref_air|AN2|data|an2_2_CO","rhsgref|addons|rhsgref_air|AN2|data|an2_wings_CO"],
            "factions": []
        }
    },
    "texturelist": [],
    # Class: CfgVehicles|RHS_AN2_Base|Attributes [Indent level: 1],
    "attributes": {
        # Class: CfgVehicles|RHS_AN2_Base|Attributes|ObjectTexture [Indent level: 2]
        "objecttexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayname": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        # Class: CfgVehicles|RHS_AN2_Base|Attributes|rhs_decalNumber_type [Indent level: 2],
        "rhs_decalnumber_type": {
            "displayname": "Define font type of side number",
            "tooltip": "Define kind of font that will be drawn on vehicle",
            "property": "rhs_decalNumber_type",
            "control": "Combo",
            "expression": "if(_value != 'NoChange')then{ _this setVariable ['%s', _value];[_this,[['Number', [3,4], _value]]] call rhs_fnc_decalsInit}",
            "defaultvalue": 0,
            "typename": "STRING",
            # Class: CfgVehicles|RHS_AN2_Base|Attributes|rhs_decalNumber_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|RHS_AN2_Base|Attributes|rhs_decalNumber_type|values|NoChange [Indent level: 4]
                "nochange": {
                    "name": "Default",
                    "value": "NoChange"
                },
                # Class: CfgVehicles|RHS_AN2_Base|Attributes|rhs_decalNumber_type|values|AviaYellow [Indent level: 4],
                "aviayellow": {
                    "name": "Aviation Yellow",
                    "value": "AviaYellow"
                },
                # Class: CfgVehicles|RHS_AN2_Base|Attributes|rhs_decalNumber_type|values|AviaBlue [Indent level: 4],
                "aviablue": {
                    "name": "Aviation Blue",
                    "value": "AviaBlue"
                },
                # Class: CfgVehicles|RHS_AN2_Base|Attributes|rhs_decalNumber_type|values|AviaRed [Indent level: 4],
                "aviared": {
                    "name": "Aviation Red",
                    "value": "AviaRed"
                },
                # Class: CfgVehicles|RHS_AN2_Base|Attributes|rhs_decalNumber_type|values|AviaWhiteOut [Indent level: 4],
                "aviawhiteout": {
                    "name": "Aviation White Out",
                    "value": "AviaWhiteOut"
                },
                # Class: CfgVehicles|RHS_AN2_Base|Attributes|rhs_decalNumber_type|values|AviaCDF [Indent level: 4],
                "aviacdf": {
                    "name": "Aviation CDF",
                    "value": "AviaCDF",
                    "defaultvalue": "AviaCDF"
                },
                # Class: CfgVehicles|RHS_AN2_Base|Attributes|rhs_decalNumber_type|values|Default [Indent level: 4],
                "default": {
                    "name": "Default (White)",
                    "value": "Default"
                },
                # Class: CfgVehicles|RHS_AN2_Base|Attributes|rhs_decalNumber_type|values|DefaultRed [Indent level: 4],
                "defaultred": {
                    "name": "Default (Red)",
                    "value": "DefaultRed"
                },
                # Class: CfgVehicles|RHS_AN2_Base|Attributes|rhs_decalNumber_type|values|BoldRed [Indent level: 4],
                "boldred": {
                    "name": "Bold Red",
                    "value": "BoldRed"
                },
                # Class: CfgVehicles|RHS_AN2_Base|Attributes|rhs_decalNumber_type|values|CDF [Indent level: 4],
                "cdf": {
                    "name": "CDF",
                    "value": "CDF"
                },
                # Class: CfgVehicles|RHS_AN2_Base|Attributes|rhs_decalNumber_type|values|Handpaint [Indent level: 4],
                "handpaint": {
                    "name": "Handpaint",
                    "value": "Handpaint"
                },
                # Class: CfgVehicles|RHS_AN2_Base|Attributes|rhs_decalNumber_type|values|HandpaintBlack [Indent level: 4],
                "handpaintblack": {
                    "name": "Handpaint Black",
                    "value": "HandpaintBlack"
                },
                # Class: CfgVehicles|RHS_AN2_Base|Attributes|rhs_decalNumber_type|values|Iraqi [Indent level: 4],
                "iraqi": {
                    "name": "Iraqi",
                    "value": "Iraqi"
                }
            }
        },
        # Class: CfgVehicles|RHS_AN2_Base|Attributes|rhs_decalNumber [Indent level: 2],
        "rhs_decalnumber": {
            "displayname": "Set side number",
            "tooltip": "Set side number. 2 numbers are required. Type 0 to hide numbers completly",
            "property": "rhs_decalNumber",
            "control": "Edit",
            "validate": "Number",
            "defaultvalue": "-1",
            "typename": "Number",
            "expression": "if( _value >= 0)then{if(_value == 0)then{{[_this setobjectTexture [_x,'a3|data_f|clear_empty.paa']]}foreach [3,4]}else{[_this, [['Number', [3,4], _this getVariable ['rhs_decalNumber_type','AviaCDF'], _value] ] ] call rhs_fnc_decalsInit}};"
        },
        # Class: CfgVehicles|RHS_AN2_Base|Attributes|rhs_decalTail [Indent level: 2],
        "rhs_decaltail": {
            "displayname": "Define tail decal",
            "tooltip": "Define tail decal that will be drawn on vehicle",
            "property": "rhs_decalTail",
            "control": "Combo",
            "expression": "[_this,[['Label', [5], 'Aviation',_value]]] call rhs_fnc_decalsInit",
            "defaultvalue": -1,
            "typename": "Number",
            # Class: CfgVehicles|RHS_AN2_Base|Attributes|rhs_decalTail|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|RHS_AN2_Base|Attributes|rhs_decalTail|values|Default [Indent level: 4]
                "default": {
                    "name": "Default",
                    "value": -1
                },
                # Class: CfgVehicles|RHS_AN2_Base|Attributes|rhs_decalTail|values|Empty [Indent level: 4],
                "empty": {
                    "name": "Empty",
                    "value": 0
                },
                # Class: CfgVehicles|RHS_AN2_Base|Attributes|rhs_decalTail|values|Star [Indent level: 4],
                "star": {
                    "name": "Red Star",
                    "value": 2
                },
                # Class: CfgVehicles|RHS_AN2_Base|Attributes|rhs_decalTail|values|CDF [Indent level: 4],
                "cdf": {
                    "name": "CDF",
                    "value": 4,
                    "defaultvalue": 4
                }
            }
        },
        # Class: CfgVehicles|RHS_AN2_Base|Attributes|door [Indent level: 2],
        "door": {
            "displayname": "Open Door",
            "property": "door",
            "control": "slider",
            "expression": "_this animate ['door',_value];",
            "defaultvalue": "0"
        }
    },
    # Class: CfgVehicles|RHS_AN2_Base|MarkerLights [Indent level: 1],
    "markerlights": {
        # Class: CfgVehicles|RHS_AN2_Base|MarkerLights|WhiteStill [Indent level: 2]
        "whitestill": {
            "name": "pos_light_still_white",
            "color": [1,1,1],
            "ambient": [0.1,0.1,0.1],
            "intensity": 75,
            "drawlight": 1,
            "drawlightsize": 0.25,
            "drawlightcentersize": 0.04,
            "activelight": 0,
            "blinking": 0,
            "daylight": 0,
            "useflare": 1
        },
        # Class: CfgVehicles|RHS_AN2_Base|MarkerLights|RedStill [Indent level: 2],
        "redstill": {
            "name": "pos_light_still_red",
            "color": [0.8,0,0],
            "ambient": [0.08,0,0],
            "intensity": 75,
            "drawlight": 1,
            "drawlightsize": 0.25,
            "drawlightcentersize": 0.04,
            "activelight": 0,
            "blinking": 0,
            "daylight": 0,
            "useflare": 1
        },
        # Class: CfgVehicles|RHS_AN2_Base|MarkerLights|GreenStill [Indent level: 2],
        "greenstill": {
            "name": "pos_light_still_green",
            "color": [0,0.8,0],
            "ambient": [0,0.08,0],
            "intensity": 75,
            "drawlight": 1,
            "drawlightsize": 0.25,
            "drawlightcentersize": 0.04,
            "activelight": 0,
            "blinking": 0,
            "daylight": 0,
            "useflare": 1
        },
        # Class: CfgVehicles|RHS_AN2_Base|MarkerLights|RedBlinking [Indent level: 2],
        "redblinking": {
            "name": "pos_light_blink_red",
            "color": [0.9,0.15,0.1],
            "ambient": [0.09,0.015,0.01],
            "intensity": 75,
            "blinking": 1,
            "blinkingstartson": 0,
            "blinkingpattern": [2.9,0.1],
            "blinkingpatternguarantee": 0,
            "drawlightsize": 0.2,
            "drawlightcentersize": 0.04
        },
        # Class: CfgVehicles|RHS_AN2_Base|MarkerLights|WhiteBlinking1 [Indent level: 2],
        "whiteblinking1": {
            "name": "pos_light_blink1_white",
            "color": [1,1,1],
            "ambient": [0.1,0.1,0.1],
            "intensity": 100,
            "blinking": 1,
            "blinkingpattern": [0.1,2.9],
            "blinkingpatternguarantee": 0,
            "drawlightsize": 0.35,
            "drawlightcentersize": 0.08
        },
        # Class: CfgVehicles|RHS_AN2_Base|MarkerLights|WhiteBlinking2 [Indent level: 2],
        "whiteblinking2": {
            "name": "pos_light_blink2_white",
            "color": [1,1,1],
            "ambient": [0.1,0.1,0.1],
            "intensity": 100,
            "blinking": 1,
            "blinkingpattern": [0.1,2.9],
            "blinkingpatternguarantee": 0,
            "drawlightsize": 0.35,
            "drawlightcentersize": 0.08
        },
        # Class: CfgVehicles|RHS_AN2_Base|MarkerLights|WhiteBlinking3 [Indent level: 2],
        "whiteblinking3": {
            "name": "pos_light_blink3_white",
            "color": [1,1,1],
            "ambient": [0.1,0.1,0.1],
            "intensity": 100,
            "blinking": 1,
            "blinkingpattern": [0.1,2.9],
            "blinkingpatternguarantee": 0,
            "drawlightsize": 0.35,
            "drawlightcentersize": 0.08
        }
    },
    # Class: CfgVehicles|RHS_AN2_Base|WingVortices [Indent level: 1],
    "wingvortices": {
        # Class: CfgVehicles|RHS_AN2_Base|WingVortices|WingTipLeft [Indent level: 2]
        "wingtipleft": {
            "effectname": "WingVortices",
            "position": "body_vapour_L_E"
        },
        # Class: CfgVehicles|RHS_AN2_Base|WingVortices|WingTipRight [Indent level: 2],
        "wingtipright": {
            "effectname": "WingVortices",
            "position": "body_vapour_R_E"
        },
        # Class: CfgVehicles|RHS_AN2_Base|WingVortices|BodyLeft [Indent level: 2],
        "bodyleft": {
            "effectname": "BodyVortices",
            "position": "body_vapour_L_S"
        },
        # Class: CfgVehicles|RHS_AN2_Base|WingVortices|BodyRight [Indent level: 2],
        "bodyright": {
            "effectname": "BodyVortices",
            "position": "body_vapour_R_S"
        },
        # Class: CfgVehicles|RHS_AN2_Base|WingVortices|WingTipLeftTop [Indent level: 2],
        "wingtiplefttop": {
            "effectname": "WingVortices",
            "position": "body_vapour_L_E_T"
        },
        # Class: CfgVehicles|RHS_AN2_Base|WingVortices|WingTipRightTop [Indent level: 2],
        "wingtiprighttop": {
            "effectname": "WingVortices",
            "position": "body_vapour_R_E_T"
        },
        # Class: CfgVehicles|RHS_AN2_Base|WingVortices|BodyLeftTop [Indent level: 2],
        "bodylefttop": {
            "effectname": "BodyVortices",
            "position": "body_vapour_L_S_T"
        },
        # Class: CfgVehicles|RHS_AN2_Base|WingVortices|BodyRightTop [Indent level: 2],
        "bodyrighttop": {
            "effectname": "BodyVortices",
            "position": "body_vapour_R_S_T"
        }
    },
    # Class: CfgVehicles|RHS_AN2_Base|TransportBackpacks [Indent level: 1],
    "transportbackpacks": {
        # Class: CfgVehicles|RHS_AN2_Base|TransportBackpacks|_xx_B_Parachute [Indent level: 2]
        "_xx_b_parachute": {
            "backpack": "B_Parachute",
            "count": 16
        }
    },
    # Class: CfgVehicles|RHS_AN2_Base|TransportItems [Indent level: 1],
    "transportitems": {
        # Class: CfgVehicles|RHS_AN2_Base|TransportItems|_xx_FirstAidKit [Indent level: 2]
        "_xx_firstaidkit": {
            "name": "FirstAidKit",
            "count": 20
        },
        # Class: CfgVehicles|RHS_AN2_Base|TransportItems|_xx_Medikit [Indent level: 2],
        "_xx_medikit": {
            "name": "Medikit",
            "count": 5
        }
    },
    # Class: CfgVehicles|RHS_AN2_Base|UserActions [Indent level: 1],
    "useractions": {
        # Class: CfgVehicles|RHS_AN2_Base|UserActions|DoorOpen [Indent level: 2]
        "dooropen": {
            "displayname": "Open Doors",
            "displaynamedefault": "Open doors",
            "position": "cargo_door_handle",
            "radius": 2,
            "showwindow": 0,
            "onlyforplayer": 1,
            "condition": "this animationPhase 'door' == 0 && (alive this) && (player in crew this) && (this animationPhase 'hideDoor' < 0.5);",
            "statement": "this animate ['door',1, false];"
        },
        # Class: CfgVehicles|RHS_AN2_Base|UserActions|DoorClose [Indent level: 2],
        "doorclose": {
            "displayname": "Close Doors",
            "displaynamedefault": "Close doors",
            "position": "cargo_door_handle",
            "radius": 2,
            "showwindow": 0,
            "onlyforplayer": 1,
            "condition": "this animationPhase 'door' == 1 && (alive this) && (player in crew this) && (this animationPhase 'hideDoor' < 0.5);",
            "statement": "this animate ['door',0, false];"
        }
    },
    # Class: CfgVehicles|RHS_AN2_Base|EventHandlers [Indent level: 1],
    "eventhandlers": {
        # Class: CfgVehicles|RHS_AN2_Base|EventHandlers|RHS_EventHandlers [Indent level: 2]
        "rhs_eventhandlers": {
            "init": "_this call rhs_fnc_air_init"
        },
        "init": "",
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');",
        # Class: DefaultEventHandlers|RHS_DefaultEventhandlers [Indent level: 0],
        "rhs_defaulteventhandlers": {
            "hitpart": "_this call rhs_fnc_hitPart"
        }
    },
    "_generalmacro": "Plane_Base_F",
    "drivercansee": "1 + 2 + 4 + 8 + 32",
    "gunnercansee": "1 + 2 + 4 + 8 + 32",
    "commandercansee": "1 + 2 + 4 + 8 + 32",
    "waterleakiness": 150,
    "waterlineardampingcoefy": 0,
    "waterlineardampingcoefx": 5,
    "waterresistancecoef": 0.04,
    "transportmaxweapons": 6,
    "transportmaxmagazines": 24,
    "transportmaxbackpacks": 6,
    "maximumload": 500,
    "supplyradius": 2,
    "memorypointsupply": "doplnovani",
    # Class: CfgVehicles|Plane_Base_F|TransportMagazines [Indent level: 1],
    "transportmagazines": {
    },
    # Class: CfgVehicles|Plane_Base_F|TransportWeapons [Indent level: 1],
    "transportweapons": {
    },
    # Class: CfgVehicles|Plane_Base_F|camShakeGForce [Indent level: 1],
    "camshakegforce": {
        "power": 1,
        "frequency": 20,
        "distance": 0,
        "minspeed": 1
    },
    "mingforce": 0.3,
    "maxgforce": 3,
    "gforceshakeattenuation": 0.5,
    # Class: CfgVehicles|Plane_Base_F|NewTurret [Indent level: 1],
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
    "formationx": 200,
    "formationz": 300,
    "precision": 200,
    "brakedistance": 500,
    "steeraheadsimul": 1,
    "steeraheadplan": 2,
    "durationgetin": 0.99,
    "durationgetout": 0.99,
    "flaps": 1,
    "vtol": 0,
    "tailhook": 0,
    "gearuptime": 3.33,
    "geardowntime": 2,
    "ejectdamagelimit": 0.45,
    "minfiretime": 60,
    "mingunelev": 0,
    "maxgunelev": 0,
    "mingunturn": 0,
    "maxgunturn": 0,
    "gunaimdown": 0,
    "elevatorcoef": [],
    "aileroncoef": [],
    "ruddercoef": [],
    "elevatorcontrolssensitivitycoef": 4,
    "aileroncontrolssensitivitycoef": 4,
    "ruddercontrolssensitivitycoef": 4,
    "vtolyawinfluence": 2,
    "vtolpitchinfluence": 2,
    "vtolrollinfluence": 2,
    "stallwarningtreshold": 0.2,
    # Class: CfgVehicles|Plane|ViewPilot [Indent level: 1],
    "viewpilot": {
        "initfov": 0.75,
        "minfov": 0.25,
        "maxfov": 1.25,
        "initanglex": 0,
        "initangley": 0,
        "minanglex": -65,
        "maxanglex": 85,
        "minangley": -150,
        "maxangley": 150,
        "minmovex": -0.2,
        "maxmovex": 0.2,
        "minmovey": -0.1,
        "maxmovey": 0.1,
        "minmovez": -0.1,
        "maxmovez": 0.2,
        "speedzoommaxspeed": 1e+010,
        "speedzoommaxfov": 0
    },
    # Class: CfgVehicles|Plane|ViewOptics [Indent level: 1],
    "viewoptics": {
        "initanglex": 0,
        "minanglex": 0,
        "maxanglex": 0,
        "initangley": 0,
        "minangley": 0,
        "maxangley": 0,
        "initfov": 0.5,
        "minfov": 0.5,
        "maxfov": 0.5,
        "minmovex": 0,
        "maxmovex": 0,
        "minmovey": 0,
        "maxmovey": 0,
        "minmovez": 0,
        "maxmovez": 0,
        "speedzoommaxspeed": 1e+010,
        "speedzoommaxfov": 0
    },
    "selectionrotorstill": "vrtule staticka",
    "selectionrotormove": "vrtule blur",
    "memorypointlrocket": "L raketa",
    "memorypointrrocket": "P raketa",
    "memorypointldust": "levy prach",
    "memorypointrdust": "pravy prach",
    "selectionfireanim": "zasleh",
    "leftdusteffect": "LDustEffects",
    "rightdusteffect": "RDustEffects",
    "dusteffect": "HeliDust",
    "watereffect": "HeliWater",
    # Class: CfgVehicles|Plane|MFD [Indent level: 1],
    "mfd": {
        # Class: CfgVehicles|Plane|MFD|HUD [Indent level: 2]
        "hud": {
            "borderleft": 0.09,
            "borderright": 0.02,
            "bordertop": 0.02,
            "borderbottom": 0.1,
            "helmetmounteddisplay": 1,
            "helmetposition": [-0.025,0.025,0.1],
            "helmetright": [0.05,0,0],
            "helmetdown": [-0,-0.05,0],
            # Class: CfgVehicles|Plane|MFD|HUD|pos10vector [Indent level: 3],
            "pos10vector": {
                "type": "vector",
                "pos0": [0.5,0.27],
                "pos10": ["0.5+0.9","0.27+0.7"]
            },
            # Class: CfgVehicles|Plane|MFD|HUD|bones [Indent level: 3],
            "bones": {
                # Class: AirplaneHUD|Bones|AGLMove1 [Indent level: 1]
                "aglmove1": {
                    "type": "linear",
                    "source": "altitudeAGL",
                    "min": 0,
                    "max": 100,
                    "minpos": [0.05,0.1],
                    "maxpos": [0.05,0.8]
                },
                # Class: AirplaneHUD|Bones|AGLMove2 [Indent level: 1],
                "aglmove2": {
                    "type": "fixed",
                    "pos": [0.05,0.8]
                },
                # Class: AirplaneHUD|Bones|ASLMove1 [Indent level: 1],
                "aslmove1": {
                    "type": "linear",
                    "source": "altitudeASL",
                    "min": 0,
                    "max": 500,
                    "minpos": [0.1,0.1],
                    "maxpos": [0.1,0.8]
                },
                # Class: AirplaneHUD|Bones|ASLMove2 [Indent level: 1],
                "aslmove2": {
                    "type": "fixed",
                    "pos": [0.1,0.8]
                },
                # Class: AirplaneHUD|Bones|VertSpeed [Indent level: 1],
                "vertspeed": {
                    "type": "linear",
                    "source": "vSpeed",
                    "min": -25,
                    "max": 25,
                    "minpos": [0,-0.4],
                    "maxpos": [0,0.4]
                },
                # Class: AirplaneHUD|Bones|SpdMove2 [Indent level: 1],
                "spdmove2": {
                    "source": "speed",
                    "min": 33,
                    "max": 200,
                    "type": "linear",
                    "minpos": [0.94,0.1],
                    "maxpos": [0.94,0.87]
                },
                # Class: AirplaneHUD|Bones|ILS [Indent level: 1],
                "ils": {
                    "type": "ils",
                    "pos0": [0.5,0.4],
                    "pos3": [0.7,0.6]
                },
                # Class: AirplaneHUD|Bones|WeaponAim [Indent level: 1],
                "weaponaim": {
                    "source": "weapon",
                    "type": "vector",
                    "pos0": [0.5,0.27],
                    "pos10": ["0.5+0.9","0.27+0.7"]
                },
                # Class: AirplaneHUD|Bones|Target [Indent level: 1],
                "target": {
                    "source": "target",
                    "type": "vector",
                    "pos0": [0.5,0.27],
                    "pos10": ["0.5+0.9","0.27+0.7"]
                },
                # Class: AirplaneHUD|Bones|TargetDistanceMissile [Indent level: 1],
                "targetdistancemissile": {
                    "type": "rotational",
                    "source": "targetDist",
                    "center": [0,0],
                    "min": 100,
                    "max": 3000,
                    "minangle": -120,
                    "maxangle": 120
                },
                # Class: AirplaneHUD|Bones|TargetDistanceMGun [Indent level: 1],
                "targetdistancemgun": {
                    "type": "rotational",
                    "source": "targetDist",
                    "center": [0,0],
                    "min": 100,
                    "max": 1000,
                    "minangle": -180,
                    "maxangle": 90
                },
                # Class: AirplaneHUD|Bones|Level0 [Indent level: 1],
                "level0": {
                    "type": "horizon",
                    "angle": 0,
                    "pos0": [0.5,0.27],
                    "pos10": ["0.5+0.9","0.27+0.7"]
                },
                # Class: AirplaneHUD|Bones|LevelP5 [Indent level: 1],
                "levelp5": {
                    "angle": 5,
                    "type": "horizon",
                    "pos0": [0.5,0.27],
                    "pos10": ["0.5+0.9","0.27+0.7"]
                },
                # Class: AirplaneHUD|Bones|LevelM5 [Indent level: 1],
                "levelm5": {
                    "angle": -5,
                    "type": "horizon",
                    "pos0": [0.5,0.27],
                    "pos10": ["0.5+0.9","0.27+0.7"]
                },
                # Class: AirplaneHUD|Bones|LevelP10 [Indent level: 1],
                "levelp10": {
                    "angle": 10,
                    "type": "horizon",
                    "pos0": [0.5,0.27],
                    "pos10": ["0.5+0.9","0.27+0.7"]
                },
                # Class: AirplaneHUD|Bones|LevelM10 [Indent level: 1],
                "levelm10": {
                    "angle": -10,
                    "type": "horizon",
                    "pos0": [0.5,0.27],
                    "pos10": ["0.5+0.9","0.27+0.7"]
                },
                # Class: AirplaneHUD|Bones|LevelP15 [Indent level: 1],
                "levelp15": {
                    "angle": 15,
                    "type": "horizon",
                    "pos0": [0.5,0.27],
                    "pos10": ["0.5+0.9","0.27+0.7"]
                },
                # Class: AirplaneHUD|Bones|LevelM15 [Indent level: 1],
                "levelm15": {
                    "angle": -15,
                    "type": "horizon",
                    "pos0": [0.5,0.27],
                    "pos10": ["0.5+0.9","0.27+0.7"]
                },
                # Class: AirplaneHUD|Bones|Velocity [Indent level: 1],
                "velocity": {
                    "type": "vector",
                    "source": "velocity",
                    "pos0": [0.5,0.27],
                    "pos10": ["0.5+0.9","0.27+0.7"]
                },
                # Class: AirplaneHUD|Bones|PlaneW [Indent level: 1],
                "planew": {
                    "type": "fixed",
                    "pos": [0.5,0.27]
                }
            },
            # Class: CfgVehicles|Plane|MFD|HUD|Draw [Indent level: 3],
            "draw": {
                # Class: CfgVehicles|Plane|MFD|HUD|Draw|DimmedBase [Indent level: 4]
                "dimmedbase": {
                    "alpha": 0.3,
                    # Class: AirplaneHUD|Draw|DimmedBase|AltitudeBase [Indent level: 2],
                    "altitudebase": {
                        "type": "line",
                        "points": [["AGLMove2",1],["ASLMove2",1]]
                    }
                },
                # Class: CfgVehicles|Plane|MFD|HUD|Draw|PlaneW [Indent level: 4],
                "planew": {
                    "cliptl": [0,0.1],
                    "clipbr": [1,0.9],
                    # Class: AirplaneHUD|Draw|PlaneW|LineHL [Indent level: 2],
                    "linehl": {
                        "type": "line",
                        "points": [["PlaneW",[-0.07,0],1],["PlaneW",[-0.02,0],1],["PlaneW",[0,-0.02],1],["PlaneW",[0.02,0],1],["PlaneW",[0,0.02],1],["PlaneW",[-0.02,0],1],[],["PlaneW",[0.02,0],1],["PlaneW",[0.07,0],1]]
                    },
                    # Class: AirplaneHUD|Draw|PlaneW|Velocity [Indent level: 2],
                    "velocity": {
                        "type": "line",
                        "points": [["Velocity",[0,-0.02],1],["Velocity",[0.02,0],1],["Velocity",[0,0.02],1],["Velocity",[-0.02,0],1],["Velocity",[0,-0.02],1]]
                    }
                },
                # Class: CfgVehicles|Plane|MFD|HUD|Draw|MGun [Indent level: 4],
                "mgun": {
                    "condition": "mgun",
                    # Class: AirplaneHUD|Draw|MGun|Circle [Indent level: 2],
                    "circle": {
                        "type": "line",
                        "points": [["WeaponAim",[0,-0.07],1],["WeaponAim",["+0.7*0.07","-0.7*0.07"],1],["WeaponAim",[0.07,0],1],["WeaponAim",["+0.7*0.07","+0.7*0.07"],1],["WeaponAim",[0,0.07],1],["WeaponAim",["-0.7*0.07","+0.7*0.07"],1],["WeaponAim",[-0.07,0],1],["WeaponAim",["-0.7*0.07","-0.7*0.07"],1],["WeaponAim",[0,-0.07],1],[],["WeaponAim",[0,-0.01],1],["WeaponAim",["+0.7*0.01","-0.7*0.01"],1],["WeaponAim",[0.01,0],1],["WeaponAim",["+0.7*0.01","+0.7*0.01"],1],["WeaponAim",[0,0.01],1],["WeaponAim",["-0.7*0.01","+0.7*0.01"],1],["WeaponAim",[-0.01,0],1],["WeaponAim",["-0.7*0.01","-0.7*0.01"],1],["WeaponAim",[0,-0.01],1],[],["WeaponAim",["0.03*sin(-180)","-0.03*cos(-180)"],1],["WeaponAim",["0.07*sin(-180)","-0.07*cos(-180)"],1],[],["WeaponAim",["0.03*sin(+90)","-0.03*cos(+90)"],1],["WeaponAim",["0.07*sin(+90)","-0.07*cos(+90)"],1],[],["WeaponAim",1,"TargetDistanceMGun",[0,0.04],1],["WeaponAim",1,"TargetDistanceMGun",[0,0.07],1]]
                    }
                },
                # Class: CfgVehicles|Plane|MFD|HUD|Draw|Missile [Indent level: 4],
                "missile": {
                    "condition": "missile",
                    # Class: AirplaneHUD|Draw|Missile|Circle [Indent level: 2],
                    "circle": {
                        "type": "line",
                        "points": [["WeaponAim",[0,-0.1],1],["WeaponAim",["+0.7*0.1","-0.7*0.1"],1],["WeaponAim",[0.1,0],1],["WeaponAim",["+0.7*0.1","+0.7*0.1"],1],["WeaponAim",[0,0.1],1],["WeaponAim",["-0.7*0.1","+0.7*0.1"],1],["WeaponAim",[-0.1,0],1],["WeaponAim",["-0.7*0.1","-0.7*0.1"],1],["WeaponAim",[0,-0.1],1],[],["WeaponAim",["0.1*0.8*sin(-120)","-0.1*0.8*cos(-120)"],1],["WeaponAim",["0.1*1.2*sin(-120)","-0.1*1.2*cos(-120)"],1],[],["WeaponAim",["0.1*0.8*sin(+120)","-0.1*0.8*cos(+120)"],1],["WeaponAim",["0.1*1.2*sin(+120)","-0.1*1.2*cos(+120)"],1],[],["WeaponAim",1,"TargetDistanceMissile",[0,"0.1*0.8"],1],["WeaponAim",1,"TargetDistanceMissile",[0,"0.1*1.2"],1]]
                    },
                    # Class: AirplaneHUD|Draw|Missile|Target [Indent level: 2],
                    "target": {
                        "type": "line",
                        "points": [["Target",[-0.05,-0.05],1],["Target",[0.05,-0.05],1],["Target",[0.05,0.05],1],["Target",[-0.05,0.05],1],["Target",[-0.05,-0.05],1]]
                    }
                },
                # Class: CfgVehicles|Plane|MFD|HUD|Draw|Horizont [Indent level: 4],
                "horizont": {
                    # Class: CfgVehicles|Plane|MFD|HUD|Draw|Horizont|Dimmed [Indent level: 5]
                    "dimmed": {
                        "alpha": 0.6,
                        # Class: AirplaneHUD|Draw|Horizont|Dimmed|Level0 [Indent level: 3],
                        "level0": {
                            "type": "line",
                            "points": [["Level0",[-0.4,0],1],["Level0",[-0.13,0],1],[],["Level0",[0.13,0],1],["Level0",[0.4,0],1]]
                        }
                    },
                    "cliptl": [0.2,0.1],
                    "clipbr": [0.8,0.9],
                    # Class: AirplaneHUD|Draw|Horizont|LevelP5 [Indent level: 2],
                    "levelp5": {
                        "type": "line",
                        "points": [["LevelP5",[-0.15,0.03],1],["LevelP5",[-0.15,0],1],["LevelP5",[0.15,0],1],["LevelP5",[0.15,0.03],1]]
                    },
                    # Class: AirplaneHUD|Draw|Horizont|LevelM5 [Indent level: 2],
                    "levelm5": {
                        "type": "line",
                        "points": [["LevelM5",[-0.15,-0.03],1],["LevelM5",[-0.15,0],1],["LevelM5",[0.15,0],1],["LevelM5",[0.15,-0.03],1]]
                    },
                    # Class: AirplaneHUD|Draw|Horizont|LevelP10 [Indent level: 2],
                    "levelp10": {
                        "type": "line",
                        "points": [["LevelP10",[-0.2,0.05],1],["LevelP10",[-0.2,0],1],["LevelP10",[0.2,0],1],["LevelP10",[0.2,0.05],1]]
                    },
                    # Class: AirplaneHUD|Draw|Horizont|LevelM10 [Indent level: 2],
                    "levelm10": {
                        "type": "line",
                        "points": [["LevelM10",[-0.2,-0.05],1],["LevelM10",[-0.2,0],1],["LevelM10",[0.2,0],1],["LevelM10",[0.2,-0.05],1]]
                    },
                    # Class: AirplaneHUD|Draw|Horizont|LevelP15 [Indent level: 2],
                    "levelp15": {
                        "type": "line",
                        "points": [["LevelP15",[-0.2,0.07],1],["LevelP15",[-0.2,0],1],["LevelP15",[0.2,0],1],["LevelP15",[0.2,0.07],1]]
                    },
                    # Class: AirplaneHUD|Draw|Horizont|LevelM15 [Indent level: 2],
                    "levelm15": {
                        "type": "line",
                        "points": [["LevelM15",[-0.2,-0.07],1],["LevelM15",[-0.2,0],1],["LevelM15",[0.2,0],1],["LevelM15",[0.2,-0.07],1]]
                    }
                },
                # Class: CfgVehicles|Plane|MFD|HUD|Draw|ILS [Indent level: 4],
                "ils": {
                    # Class: CfgVehicles|Plane|MFD|HUD|Draw|ILS|Glideslope [Indent level: 5]
                    "glideslope": {
                        "cliptl": [0.29,0.29],
                        "clipbr": [0.71,0.71],
                        # Class: AirplaneHUD|Draw|ILS|Glideslope|ILS [Indent level: 3],
                        "ils": {
                            "type": "line",
                            "points": [["ILS",[-10,0],1],["ILS",[10,0],1],[],["ILS",[0,-10],1],["ILS",[0,10],1]]
                        }
                    },
                    "condition": "ils",
                    # Class: AirplaneHUD|Draw|ILS|AOABracket [Indent level: 2],
                    "aoabracket": {
                        "type": "line",
                        "points": [[[0.42,0.78],1],[[0.4,0.78],1],[[0.4,0.88],1],[[0.42,0.88],1]]
                    }
                },
                "alpha": 0.8,
                "color": [0.1,0.5,0.05],
                "cliptl": [0,0.05],
                "clipbr": [1,0.9],
                "condition": "on",
                # Class: AirplaneHUD|Draw|Altitude [Indent level: 1],
                "altitude": {
                    "type": "line",
                    "points": [["AGLMove1",1],["AGLMove2",1],[],["ASLMove2",1],["ASLMove1",1],["ASLMove1",[0.02,0],1],["ASLMove1",[0.02,0],1,"VertSpeed",1]]
                },
                # Class: AirplaneHUD|Draw|Speed [Indent level: 1],
                "speed": {
                    "type": "line",
                    "points": [[[0.95,0.87],1],[[0.95,0.1],1],[],["SpdMove2",[-0.05,0],1],["SpdMove2",1]]
                },
                # Class: AirplaneHUD|Draw|SpeedNumber [Indent level: 1],
                "speednumber": {
                    "type": "text",
                    "align": "left",
                    "scale": 1,
                    "source": "speed",
                    "sourcescale": 3.6,
                    "pos": ["SpdMove2",[-0.05,-0.03],1],
                    "right": ["SpdMove2",[0.01,-0.03],1],
                    "down": ["SpdMove2",[-0.05,0.03],1]
                }
            },
            "topleft": "HUD LH",
            "topright": "HUD PH",
            "bottomleft": "HUD LD",
            "color": [0,1,0,0.1]
        }
    },
    # Class: CfgVehicles|Plane|GunFire [Indent level: 1],
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
    # Class: CfgVehicles|Plane|GunClouds [Indent level: 1],
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
    # Class: CfgVehicles|Plane|MGunFire [Indent level: 1],
    "mgunfire": {
        "cloudletduration": 0,
        "cloudletgrowup": 0.06,
        "cloudletfadein": 0,
        "cloudletfadeout": 0.12,
        "interval": 0.005,
        "size": 0.12,
        "sourcesize": 0.01,
        "initt": 3200,
        "deltat": -4000,
        "access": 0,
        "cloudletanimperiod": 1,
        "cloudletsize": 1,
        "cloudletalpha": 1,
        "cloudletaccy": 0,
        "cloudletminyspeed": -100,
        "cloudletmaxyspeed": 100,
        "cloudletshape": "cloudletFire",
        "cloudletcolor": [1,1,1,0],
        "timetolive": 0,
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
    # Class: CfgVehicles|Plane|MGunClouds [Indent level: 1],
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
    "numberphysicalwheels": 3,
    # Class: CfgVehicles|Plane|SpeechVariants [Indent level: 1],
    "speechvariants": {
        # Class: CfgVehicles|Plane|SpeechVariants|Default [Indent level: 2]
        "default": {
            "speechsingular": ["veh_air_plane_s"],
            "speechplural": ["veh_air_plane_p"]
        }
    },
    "textsingular": "fast mover",
    "textplural": "fast movers",
    "namesound": "veh_air_plane_s",
    "type": 2,
    "memorypointgun": "kulomet",
    "fuelexplosionpower": 10,
    "epeimpulsedamagecoef": 10,
    "crewcrashprotection": 0.15,
    "unitinfotype": "RscUnitInfoAirPlane",
    "damageeffect": "AirDestructionEffects",
    "gunnergetinaction": "GetInHigh",
    "gunnergetoutaction": "GetOutHigh",
    "getinradius": 1.2,
    "camouflage": 100,
    "audible": 60,
    # Class: CfgVehicles|Plane|CamShake [Indent level: 1],
    "camshake": {
        "power": 50,
        "frequency": 20,
        "distance": 50,
        "minspeed": 200
    },
    "camshakecoef": 0,
    "headgforceleaningfactor": [0.005,0.001,0.025],
    "armorstructural": 1,
    "explosionshielding": 2,
    "mintotaldamagethreshold": 0.005,
    # Class: CfgVehicles|Plane|DestructionEffects [Indent level: 1],
    "destructioneffects": {
    },
    "formationtime": 10,
    "gearsupfrictioncoef": 0.5,
    "airbrakefrictioncoef": 3,
    "airfrictioncoefs2": [0.001,0.0005,6e-005],
    "airfrictioncoefs1": [0.1,0.05,0.006],
    "airfrictioncoefs0": [0,0,0],
    "altfullforce": 2000,
    "altnoforce": 6000,
    "fuelcapacity": 1000,
    "outsidesoundfilter": 1,
    "occludesoundswhenin": 0.316228,
    "obstructsoundswhenin": 0.316228,
    "irscanrangemin": 2000,
    "irscanrangemax": 10000,
    "irscantoeyefactor": 2,
    "nightvision": 0,
    "enablegps": 1,
    "weaponsgroup1": "1 + 		2",
    "weaponsgroup2": 4,
    "weaponsgroup3": "8 + 	16 + 	32",
    "weaponsgroup4": "64 + 		128",
    "editorsubcategory": "EdSubcat_Planes",
    "memorypointtaskmarkeroffset": [0,0.3,0],
    "rightdusteffects": [["GdtKLDirt","RDustEffectsAir"],["GdtKLGrass1","RDustEffectsAir"],["GdtKLGrass1","RGrassEffects"],["GdtKLGrass2","RDustEffectsAir"],["GdtKLGrass2","RGrassEffects"],["GdtKLForestCon","RDustEffectsAir"],["GdtKLForestDec","RDustEffectsAir"],["GdtKlMud","RDustEffectsAir"],["GdtKlSoil","RDustEffectsAir"],["GdtKlTarmac","RDustEffectsAir"],["GdtKlStubble","RDustEffectsAir"],["GdtKlStones","RDustEffectsAir"],["SurfRoadDirt_Enoch","RDustEffectsAir"],["SurfTrailDirt_Enoch","RDustEffectsAir"],["SurfRoadTarmac1_Enoch","RDustEffectsAir"],["SurfRoadTarmac2_Enoch","RDustEffectsAir"],["SurfRoadTarmac3_Enoch","RDustEffectsAir"],["GdtGrassShort","RDustEffectsAir"],["GdtGrassShort","RGrassEffects"],["GdtGrassTall","RDustEffectsAir"],["GdtGrassTall","RGrassEffects"],["GdtRedDirt","RDustEffectsAirRed"],["GdtField","RDustEffectsAir"],["GdtForest","RDustEffectsAir"],["GdtVolcano","RDustEffectsAir"],["GdtVolcano","RStonesEffects"],["GdtCliff","RDustEffectsAir"],["GdtVolcanoBeach","RDustEffectsAir"],["SurfRoadDirt_exp","RDustEffectsAirRed"],["SurfRoadConcrete_exp","RDustEffectsAir"],["SurfRoadTarmac_exp","RDustEffectsAir"],["GdtStratisConcrete","RDustEffectsAir"],["GdtStratisConcrete","RDirtEffects"],["GdtStratisBeach","RDustEffectsAir"],["GdtStratisBeach","RStonesEffects"],["GdtStratisDirt","RDustEffectsAir"],["GdtStratisDirt","RDirtEffects"],["GdtStratisSeabedCluttered","RDustEffectsAir"],["GdtStratisSeabed","RDustEffectsAir"],["GdtStratisDryGrass","RDustEffectsAir"],["GdtStratisDryGrass","RGrassDryEffects"],["GdtStratisDryGrass","RDirtEffects"],["GdtStratisGreenGrass","RDustEffectsAir"],["GdtStratisGreenGrass","RGrassEffects"],["GdtStratisGreenGrass","RDirtEffects"],["GdtStratisRocky","RDustEffectsAir"],["GdtStratisRocky","RGrassEffects"],["GdtStratisRocky","RDirtEffects"],["GdtStratisThistles","RDustEffectsAir"],["GdtStratisThistles","RGrassEffects"],["GdtStratisThistles","RDirtEffects"],["GdtConcrete","RDustEffectsAir"],["GdtConcrete","RDirtEffects"],["GdtAsphalt","RDustEffectsAir"],["GdtAsphalt","RDirtEffects"],["GdtRubble","RDustEffectsAir"],["GdtRubble","RDirtEffects"],["GdtSoil","RDustEffectsAir"],["GdtSoil","RDirtEffects"],["GdtBeach","RDustEffectsAir"],["GdtBeach","RStonesEffects"],["GdtRock","RDustEffectsAir"],["GdtRock","RDirtEffects"],["GdtDead","RDustEffectsAir"],["GdtDead","RDirtEffects"],["Default","RDustEffectsAir"],["GdtDesert1","RDustEffectsAir"],["GdtDesert1","RSandEffects"],["GdtDesert1","RDirtEffects"],["GdtDesert1","RStonesEffects"],["GdtDesert2","RDustEffectsAir"],["GdtDesert2","RSandEffects"],["GdtDesert2","RGrassEffects"],["GdtDesert2","RDirtEffects"],["GdtDirt","RDustEffectsAir"],["GdtDirt","RDirtEffects"],["GdtGrassGreen","RDustEffectsAir"],["GdtGrassGreen","RGrassEffects"],["GdtGrassGreen","RDirtEffects"],["GdtGrassDry","RDustEffectsAir"],["GdtGrassDry","RGrassDryEffects"],["GdtGrassDry","RDirtEffects"],["GdtGrassWild","RDustEffectsAir"],["GdtGrassWild","RGrassEffects"],["GdtGrassWild","RDirtEffects"],["GdtWildField","RDustEffectsAir"],["GdtWildField","RGrassEffects"],["GdtWildField","RDirtEffects"],["GdtWeed1","RDustEffectsAir"],["GdtWeed1","RGrassEffects"],["GdtWeed1","RDirtEffects"],["GdtWeed2","RDustEffectsAir"],["GdtWeed2","RGrassEffects"],["GdtWeed2","RDirtEffects"],["GdtThorn","RDustEffectsAir"],["GdtThorn","RGrassEffects"],["GdtThorn","RDirtEffects"],["GdtStony","RDustEffectsAir"],["GdtStony","RGrassEffects"],["GdtStony","RDirtEffects"],["GdtStonyGreen","RDustEffectsAir"],["GdtStonyGreen","RGrassEffects"],["GdtStonyGreen","RDirtEffects"],["GdtStonyThistle","RDustEffectsAir"],["GdtStonyThistle","RGrassEffects"],["GdtStonyThistle","RDirtEffects"],["GdtSeabedDeep","RDustEffectsAir"],["GdtSeabed","RDustEffectsAir"],["SurfRoadDirt","RDustEffectsAir"],["SurfRoadConcrete","RDustEffectsAir"],["SurfRoadTarmac","RDustEffectsAir"],["SurfWood","RDustEffectsAir"],["SurfMetal","RDustEffectsAir"],["SurfRoofTin","RDustEffectsAir"],["SurfRoofTiles","RDustEffectsAir"],["SurfIntWood","RDustEffectsAir"],["SurfIntConcrete","RDustEffectsAir"],["SurfIntTiles","RDustEffectsAir"],["SurfIntMetal","RDustEffectsAir"]],
    "leftdusteffects": [["GdtKLDirt","LDustEffectsAir"],["GdtKLGrass1","LDustEffectsAir"],["GdtKLGrass1","LGrassEffects"],["GdtKLGrass2","LDustEffectsAir"],["GdtKLGrass2","LGrassEffects"],["GdtKLForestCon","LDustEffectsAir"],["GdtKLForestDec","LDustEffectsAir"],["GdtKlMud","LDustEffectsAir"],["GdtKlSoil","LDustEffectsAir"],["GdtKlTarmac","LDustEffectsAir"],["GdtKlStubble","LDustEffectsAir"],["GdtKlStones","LDustEffectsAir"],["SurfRoadDirt_Enoch","LDustEffectsAir"],["SurfTrailDirt_Enoch","LDustEffectsAir"],["SurfRoadTarmac1_Enoch","LDustEffectsAir"],["SurfRoadTarmac2_Enoch","LDustEffectsAir"],["SurfRoadTarmac3_Enoch","LDustEffectsAir"],["GdtGrassShort","LDustEffectsAir"],["GdtGrassShort","LGrassEffects"],["GdtGrassTall","LDustEffectsAir"],["GdtGrassTall","LGrassEffects"],["GdtRedDirt","LDustEffectsAirRed"],["GdtField","LDustEffectsAir"],["GdtForest","LDustEffectsAir"],["GdtVolcano","LDustEffectsAir"],["GdtVolcano","LStonesEffects"],["GdtCliff","LDustEffectsAir"],["GdtVolcanoBeach","LDustEffectsAir"],["SurfRoadDirt_exp","LDustEffectsAirRed"],["SurfRoadConcrete_exp","LDustEffectsAir"],["SurfRoadTarmac_exp","LDustEffectsAir"],["GdtStratisConcrete","LDustEffectsAir"],["GdtStratisConcrete","LDirtEffects"],["GdtStratisBeach","LDustEffectsAir"],["GdtStratisBeach","LStonesEffects"],["GdtStratisDirt","LDustEffectsAir"],["GdtStratisDirt","LDirtEffects"],["GdtStratisSeabedCluttered","LDustEffectsAir"],["GdtStratisSeabed","LDustEffectsAir"],["GdtStratisDryGrass","LDustEffectsAir"],["GdtStratisDryGrass","LGrassDryEffects"],["GdtStratisDryGrass","LDirtEffects"],["GdtStratisGreenGrass","LDustEffectsAir"],["GdtStratisGreenGrass","LGrassEffects"],["GdtStratisGreenGrass","LDirtEffects"],["GdtStratisRocky","LDustEffectsAir"],["GdtStratisRocky","LGrassEffects"],["GdtStratisRocky","LDirtEffects"],["GdtStratisThistles","LDustEffectsAir"],["GdtStratisThistles","LGrassEffects"],["GdtStratisThistles","LDirtEffects"],["GdtConcrete","LDustEffectsAir"],["GdtConcrete","LDirtEffects"],["GdtAsphalt","LDustEffectsAir"],["GdtAsphalt","LDirtEffects"],["GdtRubble","LDustEffectsAir"],["GdtRubble","LDirtEffects"],["GdtSoil","LDustEffectsAir"],["GdtSoil","LDirtEffects"],["GdtBeach","LDustEffectsAir"],["GdtBeach","LStonesEffects"],["GdtRock","LDustEffectsAir"],["GdtRock","LDirtEffects"],["GdtDead","LDustEffectsAir"],["GdtDead","LDirtEffects"],["Default","LDustEffectsAir"],["GdtDesert1","LDustEffectsAir"],["GdtDesert1","LSandEffects"],["GdtDesert1","LDirtEffects"],["GdtDesert1","LStonesEffects"],["GdtDesert2","LDustEffectsAir"],["GdtDesert2","LSandEffects"],["GdtDesert2","LGrassEffects"],["GdtDesert2","LDirtEffects"],["GdtDirt","LDustEffectsAir"],["GdtDirt","LDirtEffects"],["GdtGrassGreen","LDustEffectsAir"],["GdtGrassGreen","LGrassEffects"],["GdtGrassGreen","LDirtEffects"],["GdtGrassDry","LDustEffectsAir"],["GdtGrassDry","LGrassDryEffects"],["GdtGrassDry","LDirtEffects"],["GdtGrassWild","LDustEffectsAir"],["GdtGrassWild","LGrassEffects"],["GdtGrassWild","LDirtEffects"],["GdtWildField","LDustEffectsAir"],["GdtWildField","LGrassEffects"],["GdtWildField","LDirtEffects"],["GdtWeed1","LDustEffectsAir"],["GdtWeed1","LGrassEffects"],["GdtWeed1","LDirtEffects"],["GdtWeed2","LDustEffectsAir"],["GdtWeed2","LGrassEffects"],["GdtWeed2","LDirtEffects"],["GdtThorn","LDustEffectsAir"],["GdtThorn","LGrassEffects"],["GdtThorn","LDirtEffects"],["GdtStony","LDustEffectsAir"],["GdtStony","LGrassEffects"],["GdtStony","LDirtEffects"],["GdtStonyGreen","LDustEffectsAir"],["GdtStonyGreen","LGrassEffects"],["GdtStonyGreen","LDirtEffects"],["GdtStonyThistle","LDustEffectsAir"],["GdtStonyThistle","LGrassEffects"],["GdtStonyThistle","LDirtEffects"],["GdtSeabedDeep","LDustEffectsAir"],["GdtSeabed","LDustEffectsAir"],["SurfRoadDirt","LDustEffectsAir"],["SurfRoadConcrete","LDustEffectsAir"],["SurfRoadTarmac","LDustEffectsAir"],["SurfWood","LDustEffectsAir"],["SurfMetal","LDustEffectsAir"],["SurfRoofTin","LDustEffectsAir"],["SurfRoofTiles","LDustEffectsAir"],["SurfIntWood","LDustEffectsAir"],["SurfIntConcrete","LDustEffectsAir"],["SurfIntTiles","LDustEffectsAir"],["SurfIntMetal","LDustEffectsAir"]],
    # Class: CfgVehicles|Air|DustEffects [Indent level: 1],
    "dusteffects": {
        # Class: CfgDustEffectsAir|Both [Indent level: 0]
        "both": {
        },
        # Class: CfgDustEffectsAir|Left [Indent level: 0],
        "left": {
            "default": ["LDustEffectsAir"],
            "gdtstratisconcrete": ["LDustEffectsAir","LDirtEffects"],
            "gdtstratisbeach": ["LDustEffectsAir","LStonesEffects"],
            "gdtstratisdirt": ["LDustEffectsAir","LDirtEffects"],
            "gdtstratisseabedcluttered": ["LDustEffectsAir"],
            "gdtstratisseabed": ["LDustEffectsAir"],
            "gdtstratisdrygrass": ["LDustEffectsAir","LGrassDryEffects","LDirtEffects"],
            "gdtstratisgreengrass": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtstratisrocky": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtstratisthistles": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtconcrete": ["LDustEffectsAir","LDirtEffects"],
            "gdtasphalt": ["LDustEffectsAir","LDirtEffects"],
            "gdtrubble": ["LDustEffectsAir","LDirtEffects"],
            "gdtsoil": ["LDustEffectsAir","LDirtEffects"],
            "gdtbeach": ["LDustEffectsAir","LStonesEffects"],
            "gdtrock": ["LDustEffectsAir","LDirtEffects"],
            "gdtdead": ["LDustEffectsAir","LDirtEffects"],
            "gdtdesert1": ["LDustEffectsAir","LSandEffects","LDirtEffects","LStonesEffects"],
            "gdtdesert2": ["LDustEffectsAir","LSandEffects","LGrassEffects","LDirtEffects"],
            "gdtdirt": ["LDustEffectsAir","LDirtEffects"],
            "gdtgrassgreen": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtgrassdry": ["LDustEffectsAir","LGrassDryEffects","LDirtEffects"],
            "gdtgrasswild": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtwildfield": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtweed1": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtweed2": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtthorn": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtstony": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtstonygreen": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtstonythistle": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtseabeddeep": ["LDustEffectsAir"],
            "gdtseabed": ["LDustEffectsAir"],
            "surfroaddirt": ["LDustEffectsAir"],
            "surfroadconcrete": ["LDustEffectsAir"],
            "surfroadtarmac": ["LDustEffectsAir"],
            "surfwood": ["LDustEffectsAir"],
            "surfmetal": ["LDustEffectsAir"],
            "surfrooftin": ["LDustEffectsAir"],
            "surfrooftiles": ["LDustEffectsAir"],
            "surfintwood": ["LDustEffectsAir"],
            "surfintconcrete": ["LDustEffectsAir"],
            "surfinttiles": ["LDustEffectsAir"],
            "surfintmetal": ["LDustEffectsAir"],
            "gdtgrassshort": ["LDustEffectsAir","LGrassEffects"],
            "gdtgrasstall": ["LDustEffectsAir","LGrassEffects"],
            "gdtreddirt": ["LDustEffectsAirRed"],
            "gdtfield": ["LDustEffectsAir"],
            "gdtforest": ["LDustEffectsAir"],
            "gdtvolcano": ["LDustEffectsAir","LStonesEffects"],
            "gdtcliff": ["LDustEffectsAir"],
            "gdtvolcanobeach": ["LDustEffectsAir"],
            "surfroaddirt_exp": ["LDustEffectsAirRed"],
            "surfroadconcrete_exp": ["LDustEffectsAir"],
            "surfroadtarmac_exp": ["LDustEffectsAir"],
            "gdtkldirt": ["LDustEffectsAir"],
            "gdtklgrass1": ["LDustEffectsAir","LGrassEffects"],
            "gdtklgrass2": ["LDustEffectsAir","LGrassEffects"],
            "gdtklforestcon": ["LDustEffectsAir"],
            "gdtklforestdec": ["LDustEffectsAir"],
            "gdtklmud": ["LDustEffectsAir"],
            "gdtklsoil": ["LDustEffectsAir"],
            "gdtkltarmac": ["LDustEffectsAir"],
            "gdtklstubble": ["LDustEffectsAir"],
            "gdtklstones": ["LDustEffectsAir"],
            "surfroaddirt_enoch": ["LDustEffectsAir"],
            "surftraildirt_enoch": ["LDustEffectsAir"],
            "surfroadtarmac1_enoch": ["LDustEffectsAir"],
            "surfroadtarmac2_enoch": ["LDustEffectsAir"],
            "surfroadtarmac3_enoch": ["LDustEffectsAir"]
        },
        # Class: CfgDustEffectsAir|Right [Indent level: 0],
        "right": {
            "default": ["RDustEffectsAir"],
            "gdtstratisconcrete": ["RDustEffectsAir","RDirtEffects"],
            "gdtstratisbeach": ["RDustEffectsAir","RStonesEffects"],
            "gdtstratisdirt": ["RDustEffectsAir","RDirtEffects"],
            "gdtstratisseabedcluttered": ["RDustEffectsAir"],
            "gdtstratisseabed": ["RDustEffectsAir"],
            "gdtstratisdrygrass": ["RDustEffectsAir","RGrassDryEffects","RDirtEffects"],
            "gdtstratisgreengrass": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtstratisrocky": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtstratisthistles": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtconcrete": ["RDustEffectsAir","RDirtEffects"],
            "gdtasphalt": ["RDustEffectsAir","RDirtEffects"],
            "gdtrubble": ["RDustEffectsAir","RDirtEffects"],
            "gdtsoil": ["RDustEffectsAir","RDirtEffects"],
            "gdtbeach": ["RDustEffectsAir","RStonesEffects"],
            "gdtrock": ["RDustEffectsAir","RDirtEffects"],
            "gdtdead": ["RDustEffectsAir","RDirtEffects"],
            "gdtdesert1": ["RDustEffectsAir","RSandEffects","RDirtEffects","RStonesEffects"],
            "gdtdesert2": ["RDustEffectsAir","RSandEffects","RGrassEffects","RDirtEffects"],
            "gdtdirt": ["RDustEffectsAir","RDirtEffects"],
            "gdtgrassgreen": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtgrassdry": ["RDustEffectsAir","RGrassDryEffects","RDirtEffects"],
            "gdtgrasswild": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtwildfield": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtweed1": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtweed2": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtthorn": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtstony": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtstonygreen": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtstonythistle": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtseabeddeep": ["RDustEffectsAir"],
            "gdtseabed": ["RDustEffectsAir"],
            "surfroaddirt": ["RDustEffectsAir"],
            "surfroadconcrete": ["RDustEffectsAir"],
            "surfroadtarmac": ["RDustEffectsAir"],
            "surfwood": ["RDustEffectsAir"],
            "surfmetal": ["RDustEffectsAir"],
            "surfrooftin": ["RDustEffectsAir"],
            "surfrooftiles": ["RDustEffectsAir"],
            "surfintwood": ["RDustEffectsAir"],
            "surfintconcrete": ["RDustEffectsAir"],
            "surfinttiles": ["RDustEffectsAir"],
            "surfintmetal": ["RDustEffectsAir"],
            "gdtgrassshort": ["RDustEffectsAir","RGrassEffects"],
            "gdtgrasstall": ["RDustEffectsAir","RGrassEffects"],
            "gdtreddirt": ["RDustEffectsAirRed"],
            "gdtfield": ["RDustEffectsAir"],
            "gdtforest": ["RDustEffectsAir"],
            "gdtvolcano": ["RDustEffectsAir","RStonesEffects"],
            "gdtcliff": ["RDustEffectsAir"],
            "gdtvolcanobeach": ["RDustEffectsAir"],
            "surfroaddirt_exp": ["RDustEffectsAirRed"],
            "surfroadconcrete_exp": ["RDustEffectsAir"],
            "surfroadtarmac_exp": ["RDustEffectsAir"],
            "gdtkldirt": ["RDustEffectsAir"],
            "gdtklgrass1": ["RDustEffectsAir","RGrassEffects"],
            "gdtklgrass2": ["RDustEffectsAir","RGrassEffects"],
            "gdtklforestcon": ["RDustEffectsAir"],
            "gdtklforestdec": ["RDustEffectsAir"],
            "gdtklmud": ["RDustEffectsAir"],
            "gdtklsoil": ["RDustEffectsAir"],
            "gdtkltarmac": ["RDustEffectsAir"],
            "gdtklstubble": ["RDustEffectsAir"],
            "gdtklstones": ["RDustEffectsAir"],
            "surfroaddirt_enoch": ["RDustEffectsAir"],
            "surftraildirt_enoch": ["RDustEffectsAir"],
            "surfroadtarmac1_enoch": ["RDustEffectsAir"],
            "surfroadtarmac2_enoch": ["RDustEffectsAir"],
            "surfroadtarmac3_enoch": ["RDustEffectsAir"]
        }
    },
    "maxfordingdepth": 0.001,
    "waterresistance": 1,
    "impacteffectssea": "ImpactEffectsAir",
    "flarevelocity": 100,
    "enableradio": 1,
    "memorypointcm": ["flare_launcher1","flare_launcher2"],
    "memorypointcmdir": ["flare_launcher1_dir","flare_launcher2_dir"],
    "radartype": 4,
    "radartarget": 1,
    "radartargetsize": 1,
    "visualtarget": 1,
    "visualtargetsize": 1,
    "irtargetsize": 1,
    "lockdetectionsystem": "8 + 4",
    "incomingmissiledetectionsystem": "8 + 16",
    "countermeasureactivationradius": 10000,
    # Class: CfgVehicles|Air|camShakeDamage [Indent level: 1],
    "camshakedamage": {
        "power": 0.5,
        "frequency": 60,
        "distance": -1,
        "minspeed": 1,
        "attenuation": 0.5,
        "duration": 3
    },
    "secondaryexplosion": -1,
    # Class: CfgVehicles|AllVehicles|SquadTitles [Indent level: 1],
    "squadtitles": {
        "name": "clan_sign",
        "color": [0,0,0,0.75]
    },
    "memorypointdriveroptics": ["driverview","pilot"],
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
    "tracksspeed": 0,
    "selectionleftoffset": "",
    "selectionrightoffset": "",
    # Class: CfgVehicles|AllVehicles|RenderTargets [Indent level: 1],
    "rendertargets": {
    },
    "cargoproxyindexes": [],
    "driverdoor": "",
    "cargodoors": [],
    "hasterminal": 0,
    "getinoutonproxy": 0,
    "precisegetinout": 0,
    "cargoprecisegetinout": [0],
    "availableforsupporttypes": [],
    "waterppinvehicle": 1,
    "htmin": 60,
    "htmax": 1800,
    "afmax": 200,
    "mfmax": 100,
    "mfact": 0.2,
    "tbody": 150,
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
    "antirollbarforcecoef": 0,
    "antirollbarforcelimit": 5,
    "antirollbarspeedmin": 20,
    "antirollbarspeedmax": 60,
    "slowspeedforwardcoef": 0.3,
    "normalspeedforwardcoef": 0.85,
    "gunnerhasflares": 1,
    "enablemanualfire": 1,
    "sensitivity": 2.5,
    "sensitivityear": 0.0075,
    "portrait": "",
    "ghostpreview": "",
    "armorlights": 0.4,
    "crewvulnerable": 1,
    "replacedamaged": "",
    "replacedamagedlimit": 0.9,
    "replacedamagedhitpoints": [],
    "keepinepesceneafterdeath": 0,
    "fuelconsumptionrate": 0.01,
    "groupcameraposition": [0,5,-30],
    "extcameraparams": [1],
    "camerasmoothspeed": 5,
    "predictturnsimul": 1.2,
    "predictturnplan": 1,
    "indirecthitenemycoefai": 10,
    "indirecthitfriendlycoefai": -20,
    "indirecthitciviliancoefai": -20,
    "indirecthitunknowncoefai": -0.5,
    "alwaystarget": 0,
    "irtarget": 1,
    "irscanground": 1,
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
    "driverforceoptics": 0,
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
    "wheelcircumference": 1,
    "waterangulardampingcoef": 0,
    "shownvgdriver": 0,
    "shownvgcommander": 0,
    "shownvggunner": 0,
    "shownvgcargo": [0],
    "soundattenuationcargo": [1],
    "countsforscoreboard": 1,
    "hulldamagecauseexplosion": 0,
    # Class: CfgVehicles|All|NVGMarkers [Indent level: 1],
    "nvgmarkers": {
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
    # Class: CfgVehicles|All|SoundGear [Indent level: 1],
    "soundgear": {
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
    "soundwoodcrash": ["emptySound",0],
    "soundbushcrash": ["emptySound",0],
    "soundbuildingcrash": ["emptySound",0],
    "soundarmorcrash": ["emptySound",0],
    "aggregatereflectors": [],
    "driverinaction": "",
    "driveropticsmodel": "",
    "driveropticseffect": [],
    "driveropticscolor": [1,1,1,1],
    "hideproxyincombat": 0,
    "forcehidedriver": 0,
    "canhidedriver": -1,
    "castdrivershadow": 0,
    "castcargoshadow": 0,
    "viewdrivershadow": 1,
    "viewdrivershadowdiff": 1,
    "viewdrivershadowamb": 1,
    "viewcargoshadow": 1,
    "viewcargoshadowdiff": 1,
    "viewcargoshadowamb": 1,
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
    "selectiondamage": "zbytek",
    "headaimdown": 0,
    "cargocaneject": 1,
    "drivercaneject": 1,
    "fireresistance": 10,
    "aircapacity": 10,
    "waterdamageengine": 0.2,
    "damagetexdelay": 0,
    "coefinside": 2,
    "coefinsideheur": 2,
    "coefspeedinside": 2,
    "windsockexist": 0,
    "slingloadcargomemorypoints": [],
    "slingloadcargomemorypointsdir": [],
    "damagehalf": [],
    "damagefull": [],
    "soundturnin": ["",0.000316228,1],
    "soundturnout": ["",0.000316228,1],
    "soundturnininternal": ["",0.000316228,1],
    "soundturnoutinternal": ["",0.000316228,1],
    "features": "",
    "insidedetectcoef": 0.05,
}