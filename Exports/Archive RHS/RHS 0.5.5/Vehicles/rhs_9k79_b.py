rhs_9k79_b = {
    "editorpreview": "rhsafrf|addons|rhs_editorPreviews|data|rhs_9k79_B.paa",
    "author": "Red Hammer Studios",
    "displayname": "9P129-1M (9M79B)",
    # Class: CfgVehicles|rhs_9k79_B|Turrets [Indent level: 1],
    "turrets": {
        # Class: CfgVehicles|rhs_9k79_B|Turrets|MainTurret [Indent level: 2]
        "mainturret": {
            "magazines": ["1_Rnd_RHS_9M79B"],
            "commanding": 0,
            "gun": "RHS_SS21_missile_rise",
            "gunbeg": "usti hlavne",
            "gunend": "konec hlavne",
            "usepip": 1,
            "minelev": 74,
            "maxelev": 78,
            "initelev": 75,
            "minturn": -0.01,
            "maxturn": 0.01,
            "weapons": ["RHS_ss21_dummy_launcher"],
            "weaponsonundeploy": ["RHS_ss21_dummy_launcher"],
            "weaponsondeploy": ["RHS_9M79_1Launcher"],
            "gunnerinaction": "BAZ_oper",
            "gunneraction": "BAZ_oper",
            "soundservo": ["",0,1],
            "gunneropticsmodel": "",
            "gunnergetinaction": "GetInHigh",
            "stabilizedinaxes": 0,
            "gunnertype": "rhs_rva_crew_officer",
            "forcehidegunner": 1,
            "forcehidecommander": 1,
            "viewgunnerinexternal": 1,
            # Class: CfgVehicles|OTR21_Base|Turrets|MainTurret|ViewOptics [Indent level: 3],
            "viewoptics": {
                "initanglex": 0,
                "minanglex": -30,
                "maxanglex": 30,
                "initangley": 0,
                "minangley": -100,
                "maxangley": 100,
                "initfov": 0.093,
                "minfov": 0.093,
                "maxfov": 0.093
            },
            "lockwhenvehiclespeed": 1,
            # Class: CfgVehicles|OTR21_Base|Turrets|MainTurret|ViewCargo [Indent level: 3],
            "viewcargo": {
                "initanglex": 5,
                "minanglex": -75,
                "maxanglex": 85,
                "initangley": 0,
                "minangley": -150,
                "maxangley": 150,
                "initfov": 0.7,
                "minfov": 0.42,
                "maxfov": 0.85,
                "minmovex": 0,
                "maxmovex": 0,
                "minmovey": 0,
                "maxmovey": 0,
                "minmovez": 0,
                "maxmovez": 0
            },
            # Class: CfgVehicles|OTR21_Base|Turrets|MainTurret|ViewGunner [Indent level: 3],
            "viewgunner": {
                "initanglex": 5,
                "minanglex": -75,
                "maxanglex": 85,
                "initangley": 0,
                "minangley": -150,
                "maxangley": 150,
                "initfov": 0.7,
                "minfov": 0.42,
                "maxfov": 0.85,
                "minmovex": 0,
                "maxmovex": 0,
                "minmovey": 0,
                "maxmovey": 0,
                "minmovez": 0,
                "maxmovez": 0
            },
            "outgunnermayfire": 1,
            "memorypointgun": "machinegun",
            "body": "",
            "gunnergetoutaction": "GetOutLow",
            "primarygunner": 1,
            "enablemanualfire": 0,
            "gunnerforceoptics": 0,
            "startengine": 0,
            # Class: CfgVehicles|Car_F|Turrets|MainTurret|HitPoints [Indent level: 3],
            "hitpoints": {
                # Class: CfgVehicles|Car_F|Turrets|MainTurret|HitPoints|HitTurret [Indent level: 4]
                "hitturret": {
                    "armor": 0.8,
                    "material": -1,
                    "name": "vez",
                    "visual": "vez",
                    "passthrough": 0.5,
                    "explosionshielding": 0.4
                },
                # Class: CfgVehicles|Car_F|Turrets|MainTurret|HitPoints|HitGun [Indent level: 4],
                "hitgun": {
                    "armor": 0.4,
                    "material": -1,
                    "name": "zbran",
                    "visual": "zbran",
                    "passthrough": 0,
                    "explosionshielding": 0.2
                }
            },
            # Class: CfgVehicles|Car_F|Turrets|MainTurret|Components [Indent level: 3],
            "components": {
            },
            "disablesoundattenuation": 0,
            "animationsourcebody": "mainTurret",
            "animationsourcegun": "mainGun",
            "animationsourcehatch": "hatchGunner",
            "animationsourcecamelev": "camElev",
            "proxytype": "CPGunner",
            "proxyindex": 1,
            "gunnername": "Gunner",
            "primaryobserver": 0,
            "soundelevation": ["",0.00316228,1],
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
            "ingunnermayfire": 1,
            "showhmd": 0,
            "lockwhendriverout": 0,
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
            "gunnerdoor": "",
            "precisegetinout": 0,
            "turretfollowfreelook": 0,
            "allowtablock": 1,
            "showalltargets": 0,
            "dontcreateai": 0,
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
            "memorypointgunneroptics": "gunnerview",
            "memorypointsgetingunner": "pos gunner",
            "memorypointsgetingunnerdir": "pos gunner dir",
            "selectionfireanim": "zasleh",
            "showcrewaim": 0
        },
        # Class: CfgVehicles|Truck_F|Turrets|ViewGunner [Indent level: 2],
        "viewgunner": {
        }
    },
    "scope": 2,
    "dlc": "RHS_AFRF",
    "rhs_decalparameters": ["['Number', SS21NumberPlaces, 'Default']"],
    "category": "Car",
    "normalspeedforwardcoef": 0.6,
    "slowspeedforwardcoef": 0.45,
    "turncoef": 3.5,
    "terraincoef": 1.5,
    "simulation": "carx",
    "dampersbumpcoef": 6,
    "precision": 10,
    "brakedistance": 3,
    "acceleration": 15,
    "fireresistance": 5,
    "maxspeed": 60,
    "fuelcapacity": 20,
    "rhs_fuelcapacity": 300,
    "wheelcircumference": 3.769,
    "brakeidlespeed": 0,
    "canfloat": 1,
    "waterleakiness": 250,
    "waterspeedfactor": 0.133,
    "maxfordingdepth": 0.4,
    "waterresistance": 1,
    "waterdamageengine": 0.9,
    "waterangulardampingcoef": 10,
    "waterlineardampingcoefy": 2,
    "waterlineardampingcoefx": 2,
    "waterppinvehicle": 0,
    "waterresistancecoef": 0.4,
    "engineshifty": 0.3,
    "engineshiftz": -3,
    "rudderforcecoef": 1.5,
    "rudderforcecoefatmaxspeed": 0.3,
    # Class: CfgVehicles|OTR21_Base|complexGearbox [Indent level: 1],
    "complexgearbox": {
        "gearboxratios": ["R1",-5.3,"N",0,"D1",5.62,"D2",2.89,"D3",1.64,"D4",1,"D5",0.724],
        "transmissionratios": ["High",10.62],
        "gearboxmode": "auto",
        "moveoffgear": 1,
        "drivestring": "D",
        "neutralstring": "N",
        "reversestring": "R"
    },
    "changegearmineffectivity": [0.95,0,0.95,0.95,0.95,0.85,0.85],
    "switchtime": 0.81,
    "latency": 1.5,
    "differentialtype": "all_limited",
    "frontrearsplit": 0.5,
    "frontbias": 3.3,
    "rearbias": 3.6,
    "centrebias": 1,
    "clutchstrength": 175,
    "transmissionlosses": 12,
    "dampingratefullthrottle": 0.08,
    "dampingratezerothrottleclutchengaged": 1.35,
    "dampingratezerothrottleclutchdisengaged": 0.35,
    "torquecurve": [[0.245614,0],[0.421053,0.953109],[0.526316,1],[0.561404,1],[0.631579,0.953109],[0.77193,0.897044],[0.912281,0.826707],[1.08807,0]],
    "maxomega": 298.45,
    "minomega": 60,
    "enginepower": 280,
    "peaktorque": 1226.25,
    "idlerpm": 700,
    "redrpm": 2850,
    "enginelosses": 14,
    "thrustdelay": 2.4,
    "enginebrakecoef": 0.3,
    "antirollbarforcecoef": 25,
    "antirollbarforcelimit": 45.5,
    "antirollbarspeedmin": 30,
    "antirollbarspeedmax": 60,
    # Class: CfgVehicles|OTR21_Base|Wheels [Indent level: 1],
    "wheels": {
        # Class: CfgVehicles|OTR21_Base|Wheels|LF [Indent level: 2]
        "lf": {
            "side": "left",
            "bonename": "wheel_1_1_damper",
            "center": "wheel_1_1_axis",
            "boundary": "wheel_1_1_bound",
            "suspforceapppointoffset": "wheel_1_1_axis",
            "tireforceapppointoffset": "wheel_1_1_axis",
            "susptraveldirection": [-0.125,-1,0],
            "steering": 1,
            "width": 0.4,
            "mass": 90,
            "moi": 14,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 12500,
            "maxhandbraketorque": 0,
            "maxcompression": 0.25,
            "maxdroop": 0.25,
            "sprungmass": 3000,
            "springstrength": 111813,
            "springdamperrate": 15872,
            "longitudinalstiffnessperunitgravity": 54582,
            "latstiffx": 3.5,
            "latstiffy": 18,
            "frictionvsslipgraph": [[0,1.2],[0.5,1.13],[1,1]]
        },
        # Class: CfgVehicles|OTR21_Base|Wheels|LR [Indent level: 2],
        "lr": {
            "bonename": "wheel_1_2_damper",
            "center": "wheel_1_2_axis",
            "boundary": "wheel_1_2_bound",
            "suspforceapppointoffset": "wheel_1_2_axis",
            "tireforceapppointoffset": "wheel_1_2_axis",
            "steering": 0,
            "maxhandbraketorque": 20000,
            "side": "left",
            "susptraveldirection": [-0.125,-1,0],
            "width": 0.4,
            "mass": 90,
            "moi": 14,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 12500,
            "maxcompression": 0.25,
            "maxdroop": 0.25,
            "sprungmass": 3000,
            "springstrength": 111813,
            "springdamperrate": 15872,
            "longitudinalstiffnessperunitgravity": 54582,
            "latstiffx": 3.5,
            "latstiffy": 18,
            "frictionvsslipgraph": [[0,1.2],[0.5,1.13],[1,1]]
        },
        # Class: CfgVehicles|OTR21_Base|Wheels|LR2 [Indent level: 2],
        "lr2": {
            "bonename": "wheel_1_3_damper",
            "center": "wheel_1_3_axis",
            "boundary": "wheel_1_3_bound",
            "suspforceapppointoffset": "wheel_1_3_axis",
            "tireforceapppointoffset": "wheel_1_3_axis",
            "steering": 0,
            "maxhandbraketorque": 20000,
            "side": "left",
            "susptraveldirection": [-0.125,-1,0],
            "width": 0.4,
            "mass": 90,
            "moi": 14,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 12500,
            "maxcompression": 0.25,
            "maxdroop": 0.25,
            "sprungmass": 3000,
            "springstrength": 111813,
            "springdamperrate": 15872,
            "longitudinalstiffnessperunitgravity": 54582,
            "latstiffx": 3.5,
            "latstiffy": 18,
            "frictionvsslipgraph": [[0,1.2],[0.5,1.13],[1,1]]
        },
        # Class: CfgVehicles|OTR21_Base|Wheels|RF [Indent level: 2],
        "rf": {
            "bonename": "wheel_2_1_damper",
            "center": "wheel_2_1_axis",
            "boundary": "wheel_2_1_bound",
            "suspforceapppointoffset": "wheel_2_1_axis",
            "tireforceapppointoffset": "wheel_2_1_axis",
            "side": "right",
            "susptraveldirection": [-0.125,-1,0],
            "steering": 1,
            "width": 0.4,
            "mass": 90,
            "moi": 14,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 12500,
            "maxhandbraketorque": 0,
            "maxcompression": 0.25,
            "maxdroop": 0.25,
            "sprungmass": 3000,
            "springstrength": 111813,
            "springdamperrate": 15872,
            "longitudinalstiffnessperunitgravity": 54582,
            "latstiffx": 3.5,
            "latstiffy": 18,
            "frictionvsslipgraph": [[0,1.2],[0.5,1.13],[1,1]]
        },
        # Class: CfgVehicles|OTR21_Base|Wheels|RR [Indent level: 2],
        "rr": {
            "bonename": "wheel_2_2_damper",
            "center": "wheel_2_2_axis",
            "boundary": "wheel_2_2_bound",
            "suspforceapppointoffset": "wheel_2_2_axis",
            "tireforceapppointoffset": "wheel_2_2_axis",
            "maxhandbraketorque": 20000,
            "side": "right",
            "susptraveldirection": [-0.125,-1,0],
            "steering": 1,
            "width": 0.4,
            "mass": 90,
            "moi": 14,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 12500,
            "maxcompression": 0.25,
            "maxdroop": 0.25,
            "sprungmass": 3000,
            "springstrength": 111813,
            "springdamperrate": 15872,
            "longitudinalstiffnessperunitgravity": 54582,
            "latstiffx": 3.5,
            "latstiffy": 18,
            "frictionvsslipgraph": [[0,1.2],[0.5,1.13],[1,1]]
        },
        # Class: CfgVehicles|OTR21_Base|Wheels|RR2 [Indent level: 2],
        "rr2": {
            "bonename": "wheel_2_3_damper",
            "center": "wheel_2_3_axis",
            "boundary": "wheel_2_3_bound",
            "suspforceapppointoffset": "wheel_2_3_axis",
            "tireforceapppointoffset": "wheel_2_3_axis",
            "steering": 0,
            "maxhandbraketorque": 20000,
            "side": "right",
            "susptraveldirection": [-0.125,-1,0],
            "width": 0.4,
            "mass": 90,
            "moi": 14,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 12500,
            "maxcompression": 0.25,
            "maxdroop": 0.25,
            "sprungmass": 3000,
            "springstrength": 111813,
            "springdamperrate": 15872,
            "longitudinalstiffnessperunitgravity": 54582,
            "latstiffx": 3.5,
            "latstiffy": 18,
            "frictionvsslipgraph": [[0,1.2],[0.5,1.13],[1,1]]
        }
    },
    "htmin": 60,
    "htmax": 1800,
    "afmax": 200,
    "mfmax": 100,
    "mfact": 0,
    "tbody": 0,
    "vehicleclass": "rhs_vehclass_artillery",
    "editorsubcategory": "rhs_EdSubcat_artillery",
    "model": "rhsafrf|addons|rhs_ss21|SS21Veh.p3d",
    "hiddenselections": ["camo1","camo2","camo3","num1","num2","num3"],
    "hiddenselectionstextures": ["rhsafrf|addons|rhs_ss21|data|veh|tochka_body_co.paa","rhsafrf|addons|rhs_ss21|data|veh|tochka_misc_co.paa","rhsafrf|addons|rhs_ss21|data|veh|tochka_bottom_co.paa"],
    # Class: CfgVehicles|OTR21_Base|textureSources [Indent level: 1],
    "texturesources": {
        # Class: CfgVehicles|OTR21_Base|textureSources|standard [Indent level: 2]
        "standard": {
            "displayname": "Standard",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_ss21|data|veh|tochka_body_co.paa","rhsafrf|addons|rhs_ss21|data|veh|tochka_misc_co.paa","rhsafrf|addons|rhs_ss21|data|veh|tochka_bottom_co.paa"],
            "factions": ["rhs_faction_rva"]
        },
        # Class: CfgVehicles|OTR21_Base|textureSources|camo [Indent level: 2],
        "camo": {
            "displayname": "Camo",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_ss21_camo|data|tochka_body_co.paa","rhsafrf|addons|rhs_ss21_camo|data|tochka_misc_co.paa","rhsafrf|addons|rhs_ss21_camo|data|tochka_bottom_co.paa"],
            "factions": ["rhs_faction_rva"]
        }
    },
    "texturelist": [],
    # Class: CfgVehicles|OTR21_Base|Attributes [Indent level: 1],
    "attributes": {
        # Class: CfgVehicles|OTR21_Base|Attributes|ObjectTexture [Indent level: 2]
        "objecttexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayname": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        # Class: CfgVehicles|OTR21_Base|Attributes|rhs_decalNumber_type [Indent level: 2],
        "rhs_decalnumber_type": {
            "displayname": "Define font type of plate number",
            "tooltip": "Define kind of font that will be drawn on vehicle.",
            "property": "rhs_decalNumber_type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];[_this,[['Number', SS21NumberPlaces, _value]]] call rhs_fnc_decalsInit",
            "defaultvalue": 0,
            "typename": "STRING",
            # Class: CfgVehicles|OTR21_Base|Attributes|rhs_decalNumber_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|OTR21_Base|Attributes|rhs_decalNumber_type|values|Default [Indent level: 4]
                "default": {
                    "name": "Default",
                    "value": "Default",
                    "defaultvalue": "Default"
                },
                # Class: CfgVehicles|OTR21_Base|Attributes|rhs_decalNumber_type|values|DefaultRed [Indent level: 4],
                "defaultred": {
                    "name": "Default (Red)",
                    "value": "DefaultRed"
                },
                # Class: CfgVehicles|OTR21_Base|Attributes|rhs_decalNumber_type|values|BoldRed [Indent level: 4],
                "boldred": {
                    "name": "Bold Red",
                    "value": "BoldRed"
                },
                # Class: CfgVehicles|OTR21_Base|Attributes|rhs_decalNumber_type|values|CDF [Indent level: 4],
                "cdf": {
                    "name": "CDF",
                    "value": "CDF"
                },
                # Class: CfgVehicles|OTR21_Base|Attributes|rhs_decalNumber_type|values|Handpaint [Indent level: 4],
                "handpaint": {
                    "name": "Handpaint",
                    "value": "Handpaint"
                },
                # Class: CfgVehicles|OTR21_Base|Attributes|rhs_decalNumber_type|values|HandpaintBlack [Indent level: 4],
                "handpaintblack": {
                    "name": "Handpaint Black",
                    "value": "HandpaintBlack"
                },
                # Class: CfgVehicles|OTR21_Base|Attributes|rhs_decalNumber_type|values|Iraqi [Indent level: 4],
                "iraqi": {
                    "name": "Iraqi",
                    "value": "Iraqi"
                },
                # Class: CfgVehicles|OTR21_Base|Attributes|rhs_decalNumber_type|values|LicensePlate [Indent level: 4],
                "licenseplate": {
                    "name": "License Plate",
                    "value": "LicensePlate"
                }
            }
        },
        # Class: CfgVehicles|OTR21_Base|Attributes|rhs_decalNumber [Indent level: 2],
        "rhs_decalnumber": {
            "collapsed": 1,
            "displayname": "Set side number",
            "tooltip": "Set side number. 3 numbers are required. Type 0 to hide numbers complety & leave at -1 to get random number",
            "property": "rhs_decalNumber",
            "control": "Edit",
            "validate": "Number",
            "typename": "Number",
            "defaultvalue": "-1",
            "expression": "if( _value >= 0)then{if( _value == 0)then{{[_this setobjectTexture [_x,'a3|data_f|clear_empty.paa']]}foreach SS21NumberPlaces}else{[_this, [['Number', SS21NumberPlaces, _this getVariable ['rhs_decalNumber_type','Default'], _value] ] ] call rhs_fnc_decalsInit}};"
        },
        # Class: CfgVehicles|OTR21_Base|Attributes|rhs_deploy [Indent level: 2],
        "rhs_deploy": {
            "displayname": "Deploy Tochka",
            "tooltip": "Deploys Tochka in ready to launch state. In order to fire Tochka use following command Tochka doTarget enemyTarget (may be laser target or vehicle).",
            "property": "rhs_deploy",
            "control": "Checkbox",
            "expression": "if(_value)then{[_this,_value] call rhs_fnc_ss21_deploy}",
            "defaultvalue": 0
        }
    },
    "picture": "rhsafrf|addons|rhs_ss21|ico|rhs_tochkau_pic_ca.paa",
    "icon": "rhsafrf|addons|rhs_ss21|ico|tochka_mapicon_ca.paa",
    "driverlefthandanimname": "rul",
    "enablemanualfire": 0,
    "mapsize": 10,
    "side": 0,
    "threat": [0.5,0.5,0.1],
    "faction": "rhs_faction_rva",
    "crew": "rhs_rva_crew",
    "accuracy": 0.3,
    "transportsoldier": 1,
    "artilleryscanner": 0,
    "hideproxyincombat": 0,
    "transportammo": 0,
    "transportrepair": 0,
    "weapons": ["TruckHorn"],
    "magazines": [],
    "cost": 50000,
    "armor": 32,
    "damageresistance": 0.00243,
    "armorwheels": 0.12,
    "initcargoangley": 185,
    "viewdrivershadow": 1,
    "viewgunnershadow": 1,
    "viewcargoshadow": 1,
    "typicalcargo": [],
    "hasgunner": 1,
    "hascommander": 0,
    "driveraction": "BAZ_Driver",
    "cargoaction": ["BAZ_cargo"],
    "cargoiscodriver": [1,1,0],
    "memorypointsgetindriver": "pos driver",
    "memorypointsgetindriverdir": "pos driver dir",
    "memorypointsgetincargo": "pos cargo",
    "memorypointsgetincargodir": "pos cargo dir",
    "memorypointsgetingunner": "pos gunner",
    "memorypointsgetingunnerdir": "pos gunner dir",
    # Class: CfgVehicles|OTR21_Base|TransportMagazines [Indent level: 1],
    "transportmagazines": {
        # Class: CfgVehicles|OTR21_Base|TransportMagazines|_xx_30Rnd_545x39_AK [Indent level: 2]
        "_xx_30rnd_545x39_ak": {
            "magazine": "rhs_30Rnd_545x39_7N10_AK",
            "count": "30*1"
        }
    },
    # Class: CfgVehicles|OTR21_Base|Exhausts [Indent level: 1],
    "exhausts": {
        # Class: CfgVehicles|OTR21_Base|Exhausts|Exhaust [Indent level: 2]
        "exhaust": {
            "position": "vyfuk start",
            "direction": "vyfuk konec",
            "effect": "ExhaustsEffectBig"
        }
    },
    # Class: CfgVehicles|OTR21_Base|Damage [Indent level: 1],
    "damage": {
        "tex": [],
        "mat": ["rhsafrf|addons|rhs_ss21|data|veh|tochka_body.rvmat","rhsafrf|addons|rhs_ss21|data|veh|tochka_body_damage.rvmat","rhsafrf|addons|rhs_ss21|data|veh|tochka_body_destruct.rvmat","rhsafrf|addons|rhs_ss21|data|veh|tochka_glass.rvmat","rhsafrf|addons|rhs_ss21|data|veh|tochka_glass_damage.rvmat","rhsafrf|addons|rhs_ss21|data|veh|tochka_glass_damage.rvmat","rhsafrf|addons|rhs_ss21|data|veh|tochka_glass_in.rvmat","rhsafrf|addons|rhs_ss21|data|veh|tochka_glass_in_damage.rvmat","rhsafrf|addons|rhs_ss21|data|veh|tochka_glass_in_damage.rvmat","rhsafrf|addons|rhs_ss21|data|veh|tochka_misc.rvmat","rhsafrf|addons|rhs_ss21|data|veh|tochka_misc_damage.rvmat","rhsafrf|addons|rhs_ss21|data|veh|tochka_misc_destruct.rvmat","rhsafrf|addons|rhs_ss21|data|veh|tochka_bottom.rvmat","rhsafrf|addons|rhs_ss21|data|veh|tochka_bottom_damage.rvmat","rhsafrf|addons|rhs_ss21|data|veh|tochka_bottom_destruct.rvmat","rhsafrf|addons|rhs_ss21|data|veh|interior|seat.rvmat","rhsafrf|addons|rhs_ss21|data|veh|interior|seat.rvmat","rhsafrf|addons|rhs_ss21|data|veh|tochka_bottom_destruct.rvmat","rhsafrf|addons|rhs_ss21|data|veh|interior|in1.rvmat","rhsafrf|addons|rhs_ss21|data|veh|interior|in1.rvmat","rhsafrf|addons|rhs_ss21|data|veh|tochka_bottom_destruct.rvmat"]
    },
    # Class: CfgVehicles|OTR21_Base|ViewPilot [Indent level: 1],
    "viewpilot": {
        "initanglex": -2,
        "minanglex": -65,
        "maxanglex": 85,
        "initangley": 0,
        "minangley": -150,
        "maxangley": 150,
        "initfov": 0.9,
        "minfov": 0.25,
        "maxfov": 1.25,
        "minmovex": -0.2,
        "maxmovex": 0.2,
        "minmovey": -0.1,
        "maxmovey": 0.1,
        "minmovez": -0.1,
        "maxmovez": 0.2,
        "speedzoommaxspeed": 1e+010,
        "speedzoommaxfov": 0
    },
    # Class: CfgVehicles|OTR21_Base|AnimationSources [Indent level: 1],
    "animationsources": {
        # Class: CfgVehicles|OTR21_Base|AnimationSources|HitGlass1 [Indent level: 2]
        "hitglass1": {
            "source": "Hit",
            "hitpoint": "HitGlass1",
            "raw": 1
        },
        # Class: CfgVehicles|OTR21_Base|AnimationSources|HitGlass2 [Indent level: 2],
        "hitglass2": {
            "hitpoint": "HitGlass2",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|OTR21_Base|AnimationSources|HitGlass3 [Indent level: 2],
        "hitglass3": {
            "hitpoint": "HitGlass3",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|OTR21_Base|AnimationSources|HitGlass4 [Indent level: 2],
        "hitglass4": {
            "hitpoint": "HitGlass4",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|OTR21_Base|AnimationSources|HitGlass5 [Indent level: 2],
        "hitglass5": {
            "hitpoint": "HitGlass5",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|OTR21_Base|AnimationSources|HitLFWheel [Indent level: 2],
        "hitlfwheel": {
            "source": "Hit",
            "hitpoint": "HitLFWheel",
            "raw": 1
        },
        # Class: CfgVehicles|OTR21_Base|AnimationSources|HitRFWheel [Indent level: 2],
        "hitrfwheel": {
            "hitpoint": "HitRFWheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|OTR21_Base|AnimationSources|HitLBWheel [Indent level: 2],
        "hitlbwheel": {
            "hitpoint": "HitLBWheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|OTR21_Base|AnimationSources|HitRBWheel [Indent level: 2],
        "hitrbwheel": {
            "hitpoint": "HitRBWheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|OTR21_Base|AnimationSources|HitLMWheel [Indent level: 2],
        "hitlmwheel": {
            "hitpoint": "HitLMWheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|OTR21_Base|AnimationSources|HitRMWheel [Indent level: 2],
        "hitrmwheel": {
            "hitpoint": "HitRMWheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|OTR21_Base|AnimationSources|WipersSW [Indent level: 2],
        "wiperssw": {
            "source": "user",
            "animperiod": 0.1,
            "initphase": 0
        },
        # Class: CfgVehicles|OTR21_Base|AnimationSources|WindshieldWipers [Indent level: 2],
        "windshieldwipers": {
            "source": "user",
            "animperiod": 0.5,
            "initphase": 0
        },
        # Class: CfgVehicles|OTR21_Base|AnimationSources|MissileRise [Indent level: 2],
        "missilerise": {
            "source": "door",
            "animperiod": 15,
            "initphase": 0
        },
        # Class: CfgVehicles|OTR21_Base|AnimationSources|MissileHide [Indent level: 2],
        "missilehide": {
            "source": "user",
            "animperiod": 1,
            "initphase": 0
        },
        # Class: CfgVehicles|OTR21_Base|AnimationSources|StablePos [Indent level: 2],
        "stablepos": {
            "animperiod": 3,
            "source": "door",
            "initphase": 0
        },
        # Class: CfgVehicles|OTR21_Base|AnimationSources|MissileBayL [Indent level: 2],
        "missilebayl": {
            "animperiod": 9,
            "source": "door",
            "initphase": 0
        },
        # Class: CfgVehicles|OTR21_Base|AnimationSources|MissileBayR [Indent level: 2],
        "missilebayr": {
            "animperiod": 9,
            "source": "door",
            "initphase": 0
        },
        # Class: CfgVehicles|OTR21_Base|AnimationSources|MissileEnviro [Indent level: 2],
        "missileenviro": {
            "animperiod": 3,
            "source": "door",
            "initphase": 0
        },
        # Class: CfgVehicles|OTR21_Base|AnimationSources|RHS_Rocket_Handler [Indent level: 2],
        "rhs_rocket_handler": {
            "source": "user",
            "animperiod": 0.01,
            "displayname": "deploy launcher",
            "mass": 1,
            "onphasechanged": "_this spawn rhs_fnc_ss21_AI_prepare",
            "initphase": 0
        },
        # Class: CfgVehicles|Car_F|AnimationSources|HitLF2Wheel [Indent level: 2],
        "hitlf2wheel": {
            "hitpoint": "HitLBWheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|Car_F|AnimationSources|HitRF2Wheel [Indent level: 2],
        "hitrf2wheel": {
            "hitpoint": "HitRBWheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|Car_F|AnimationSources|HitGlass6 [Indent level: 2],
        "hitglass6": {
            "hitpoint": "HitGlass6",
            "source": "Hit",
            "raw": 1
        }
    },
    # Class: CfgVehicles|OTR21_Base|HitPoints [Indent level: 1],
    "hitpoints": {
        # Class: CfgVehicles|OTR21_Base|HitPoints|HitGlass1 [Indent level: 2]
        "hitglass1": {
            "armor": 0.1,
            "material": -1,
            "name": "glass5",
            "visual": "glass5",
            "passthrough": 0
        },
        # Class: CfgVehicles|OTR21_Base|HitPoints|HitGlass2 [Indent level: 2],
        "hitglass2": {
            "armor": 0.1,
            "material": -1,
            "passthrough": 0,
            "name": "glass2",
            "visual": "glass2"
        },
        # Class: CfgVehicles|OTR21_Base|HitPoints|HitGlass3 [Indent level: 2],
        "hitglass3": {
            "armor": 0.1,
            "material": -1,
            "passthrough": 0,
            "name": "glass3",
            "visual": "glass3"
        },
        # Class: CfgVehicles|OTR21_Base|HitPoints|HitGlass4 [Indent level: 2],
        "hitglass4": {
            "armor": 0.1,
            "material": -1,
            "passthrough": 0,
            "name": "glass4",
            "visual": "glass4"
        },
        # Class: CfgVehicles|OTR21_Base|HitPoints|HitGlass5 [Indent level: 2],
        "hitglass5": {
            "armor": 0.1,
            "material": -1,
            "passthrough": 0,
            "name": "glass5",
            "visual": "glass5"
        },
        # Class: CfgVehicles|OTR21_Base|HitPoints|HitLFWheel [Indent level: 2],
        "hitlfwheel": {
            "armor": 0.5,
            "passthrough": 0.3,
            "name": "wheel_1_1",
            "material": -1,
            "visual": "-",
            "explosionshielding": 4
        },
        # Class: CfgVehicles|OTR21_Base|HitPoints|HitLMWheel [Indent level: 2],
        "hitlmwheel": {
            "armor": 0.5,
            "passthrough": 0.3,
            "name": "wheel_1_2",
            "material": -1,
            "visual": "-",
            "explosionshielding": 4
        },
        # Class: CfgVehicles|OTR21_Base|HitPoints|HitLBWheel [Indent level: 2],
        "hitlbwheel": {
            "armor": 0.5,
            "passthrough": 0.3,
            "name": "wheel_1_3",
            "material": -1,
            "visual": "-",
            "explosionshielding": 4
        },
        # Class: CfgVehicles|OTR21_Base|HitPoints|HitRFWheel [Indent level: 2],
        "hitrfwheel": {
            "armor": 0.5,
            "passthrough": 0.3,
            "name": "wheel_2_1",
            "material": -1,
            "visual": "-",
            "explosionshielding": 4
        },
        # Class: CfgVehicles|OTR21_Base|HitPoints|HitRMWheel [Indent level: 2],
        "hitrmwheel": {
            "armor": 0.5,
            "passthrough": 0.3,
            "name": "wheel_2_2",
            "material": -1,
            "visual": "-",
            "explosionshielding": 4
        },
        # Class: CfgVehicles|OTR21_Base|HitPoints|HitRBWheel [Indent level: 2],
        "hitrbwheel": {
            "armor": 0.5,
            "passthrough": 0.3,
            "name": "wheel_2_3",
            "material": -1,
            "visual": "-",
            "explosionshielding": 4
        },
        # Class: CfgVehicles|OTR21_Base|HitPoints|HitBody [Indent level: 2],
        "hitbody": {
            "armor": 1,
            "material": -1,
            "name": "ammo",
            "visual": "karoserie",
            "passthrough": 1
        },
        # Class: CfgVehicles|OTR21_Base|HitPoints|HitFuel [Indent level: 2],
        "hitfuel": {
            "armor": 0.5,
            "material": -1,
            "name": "palivo",
            "visual": "-",
            "passthrough": 0.2
        },
        # Class: CfgVehicles|OTR21_Base|HitPoints|HitEngine [Indent level: 2],
        "hitengine": {
            "armor": 0.5,
            "material": -1,
            "name": "motor",
            "visual": "-",
            "passthrough": 0.2
        },
        # Class: CfgVehicles|Car_F|HitPoints|HitRGlass [Indent level: 2],
        "hitrglass": {
            "armor": 0.2,
            "material": -1,
            "name": "sklo predni P",
            "passthrough": 0,
            "explosionshielding": 2
        },
        # Class: CfgVehicles|Car_F|HitPoints|HitLGlass [Indent level: 2],
        "hitlglass": {
            "armor": 0.2,
            "material": -1,
            "name": "sklo predni L",
            "passthrough": 0,
            "explosionshielding": 2
        },
        # Class: CfgVehicles|Car_F|HitPoints|HitGlass6 [Indent level: 2],
        "hitglass6": {
            "armor": 0.1,
            "material": -1,
            "name": "glass6",
            "visual": "glass6",
            "passthrough": 0,
            "explosionshielding": 2
        },
        # Class: CfgVehicles|Car_F|HitPoints|HitLF2Wheel [Indent level: 2],
        "hitlf2wheel": {
            "armor": 0.2,
            "material": -1,
            "name": "wheel_1_2_steering",
            "visual": "-",
            "passthrough": 0.3,
            "explosionshielding": 4
        },
        # Class: CfgVehicles|Car_F|HitPoints|HitRF2Wheel [Indent level: 2],
        "hitrf2wheel": {
            "armor": 0.2,
            "material": -1,
            "name": "wheel_2_2_steering",
            "visual": "-",
            "passthrough": 0.3,
            "explosionshielding": 4
        },
        # Class: CfgVehicles|Car_F|HitPoints|HitHull [Indent level: 2],
        "hithull": {
            "armor": 1.5,
            "material": -1,
            "name": "palivo",
            "visual": "",
            "passthrough": 0.5,
            "explosionshielding": 8,
            "minimalhit": 0.1
        }
    },
    # Class: CfgVehicles|OTR21_Base|UserActions [Indent level: 1],
    "useractions": {
        # Class: CfgVehicles|OTR21_Base|UserActions|WiperOn [Indent level: 2]
        "wiperon": {
            "displayname": "Wiper On",
            "position": "zamerny",
            "radius": 0.01,
            "onlyforplayer": 0,
            "condition": "(alive this)&&((call rhs_fnc_findPlayer) == driver this)&&!(this getVariable 'wiper_on')",
            "statement": "[3,1,this] spawn (RHS_ss21_logic getVariable 'anim_ss21');"
        },
        # Class: CfgVehicles|OTR21_Base|UserActions|WiperOff [Indent level: 2],
        "wiperoff": {
            "displayname": "Wiper Off",
            "position": "zamerny",
            "radius": 0.01,
            "onlyforplayer": 0,
            "condition": "(alive this)&&((call rhs_fnc_findPlayer) == driver this)&&(this getVariable 'wiper_on')",
            "statement": "[3,0,this] call (RHS_ss21_logic getVariable 'anim_ss21');"
        },
        # Class: CfgVehicles|OTR21_Base|UserActions|ControlPanel [Indent level: 2],
        "controlpanel": {
            "displayname": "Open control panel",
            "position": "zamerny",
            "radius": 0.01,
            "onlyforplayer": 0,
            "condition": "(alive this)&&((call rhs_fnc_findPlayer)==(gunner this))",
            "statement": "createDialog 'ss21_main_dialog'"
        }
    },
    # Class: CfgVehicles|OTR21_Base|Reflectors [Indent level: 1],
    "reflectors": {
        # Class: CfgVehicles|OTR21_Base|Reflectors|LeftLight [Indent level: 2]
        "leftlight": {
            "color": [1900,1300,950],
            "ambient": [5,5,5],
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
            # Class: CfgVehicles|OTR21_Base|Reflectors|LeftLight|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardlimitstart": 30,
                "hardlimitend": 60
            }
        },
        # Class: CfgVehicles|OTR21_Base|Reflectors|RightLight [Indent level: 2],
        "rightlight": {
            "position": "P svetlo",
            "direction": "konec P svetla",
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
            # Class: CfgVehicles|OTR21_Base|Reflectors|LeftLight|Attenuation [Indent level: 3],
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
    # Class: CfgVehicles|OTR21_Base|RenderTargets [Indent level: 1],
    "rendertargets": {
        # Class: CfgVehicles|OTR21_Base|RenderTargets|LeftMirror [Indent level: 2]
        "leftmirror": {
            "rendertarget": "rendertarget0",
            # Class: CfgVehicles|OTR21_Base|RenderTargets|LeftMirror|CameraView1 [Indent level: 3],
            "cameraview1": {
                "pointposition": "m1p",
                "pointdirection": "m1d",
                "renderquality": 2,
                "rendervisionmode": 4,
                "fov": 0.7
            }
        },
        # Class: CfgVehicles|OTR21_Base|RenderTargets|RightMirror [Indent level: 2],
        "rightmirror": {
            "rendertarget": "rendertarget1",
            # Class: CfgVehicles|OTR21_Base|RenderTargets|RightMirror|CameraView1 [Indent level: 3],
            "cameraview1": {
                "pointposition": "m2p",
                "pointdirection": "m2d",
                "renderquality": 2,
                "rendervisionmode": 4,
                "fov": 0.7
            }
        }
    },
    # Class: CfgVehicles|OTR21_Base|EventHandlers [Indent level: 1],
    "eventhandlers": {
        # Class: CfgVehicles|OTR21_Base|EventHandlers|RHS_EventHandlers [Indent level: 2]
        "rhs_eventhandlers": {
            "init": "[_this select 0] execVM 'rhsafrf|addons|rhs_c_rva|scripts|init.sqf';(_this select 0) addeventhandler ['HandleDamage',{[_this,0.5,0.025,0.8,0.2] spawn rhs_fnc_activeTirePressure; _this select 2;}];"
        },
        "init": "",
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');"
    },
    "unitinfotype": "UnitInfoShip",
    # Class: CfgVehicles|OTR21_Base|Library [Indent level: 1],
    "library": {
        "libtextdesc": "Tochka-U is a short range ballistic missile system which was introduced in 1989. Tochka-U is an upgrade of initial design, with significant improvements in range and CEP. The missile is capable of precise strikes on enemy strategic targets at distances up to 120 km with several high precision warheads (HE-FRAG, cluster and nuclear(up to 100 kt)). Tochka-U was deployed in both wars in Chechnya and later in 2008 South Ossetia War, where it proved itself to be a highly accurate and devastating weapon. Missile is transported and launched by a BAZ-5921 6x6 mobile launcher vehicle. The NBC-protected vehicle is completely amphibious, with a maximum road speed of 60 km/h and 8 km/h in water."
    },
    "attenuationeffecttype": "TruckAttenuation",
    "sounddammage": ["",0.562341,1],
    "soundgetin": ["rhsafrf|addons|rhs_vehiclesounds|sounds|soft|ural4320|ural4320_engine_int_getout",1.77828,1,9],
    "soundgetout": ["rhsafrf|addons|rhs_vehiclesounds|sounds|soft|ural4320|ural4320_engine_ext_getout",2.51189,1,25],
    "soundengineonint": ["rhsafrf|addons|rhs_vehiclesounds|sounds|soft|ural4320|ural4320_engine_int_start",1.41254,1],
    "soundengineonext": ["rhsafrf|addons|rhs_vehiclesounds|sounds|soft|ural4320|ural4320_engine_ext_start",1.41254,1,200],
    "soundengineoffint": ["rhsafrf|addons|rhs_vehiclesounds|sounds|soft|ural4320|ural4320_engine_int_stop",1.41254,1],
    "soundengineoffext": ["rhsafrf|addons|rhs_vehiclesounds|sounds|soft|ural4320|ural4320_engine_ext_stop",1.41254,1,200],
    "buildcrash0": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_01",1.99526,1,75],
    "buildcrash1": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_02",1.99526,1,75],
    "buildcrash2": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_03",1.99526,1,75],
    "buildcrash3": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_04",1.99526,1,75],
    "buildcrash4": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_05",1.99526,1,75],
    "buildcrash5": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_06",1.99526,1,75],
    "buildcrash6": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_07",1.99526,1,75],
    "buildcrash7": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_08",1.99526,1,75],
    "soundbuildingcrash": ["buildCrash0",0.125,"buildCrash1",0.125,"buildCrash2",0.125,"buildCrash3",0.125,"buildCrash4",0.125,"buildCrash5",0.125,"buildCrash6",0.125,"buildCrash7",0.125],
    "woodcrash0": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_Wood_01",1.99526,1,75],
    "woodcrash1": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_Wood_02",1.99526,1,75],
    "woodcrash2": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_Wood_03",1.99526,1,75],
    "woodcrash3": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_Wood_04",1.99526,1,75],
    "woodcrash4": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_Wood_05",1.99526,1,75],
    "woodcrash5": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_Wood_06",1.99526,1,75],
    "woodcrash6": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_Wood_07",1.99526,1,75],
    "woodcrash7": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_Wood_08",1.99526,1,75],
    "soundwoodcrash": ["woodCrash0",0.125,"woodCrash1",0.125,"woodCrash2",0.125,"woodCrash3",0.125,"woodCrash4",0.125,"woodCrash5",0.125,"woodCrash6",0.125,"woodCrash7",0.125],
    "armorcrash0": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_01",1.99526,1,75],
    "armorcrash1": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_02",1.99526,1,75],
    "armorcrash2": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_03",1.99526,1,75],
    "armorcrash3": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_04",1.99526,1,75],
    "armorcrash4": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_05",1.99526,1,75],
    "armorcrash5": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_06",1.99526,1,75],
    "armorcrash6": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_07",1.99526,1,75],
    "armorcrash7": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_08",1.99526,1,75],
    "soundarmorcrash": ["ArmorCrash0",0.125,"ArmorCrash1",0.125,"ArmorCrash2",0.125,"ArmorCrash3",0.125,"ArmorCrash4",0.125,"ArmorCrash5",0.125,"ArmorCrash6",0.125,"ArmorCrash7",0.125],
    "crash0": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_01",1.99526,1,75],
    "crash1": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_02",1.99526,1,75],
    "crash2": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_03",1.99526,1,75],
    "crash3": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_04",1.99526,1,75],
    "crash4": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_05",1.99526,1,75],
    "crash5": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_06",1.99526,1,75],
    "crash6": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_07",1.99526,1,75],
    "crash7": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_08",1.99526,1,75],
    "soundcrashes": ["Crash0",0.125,"Crash1",0.125,"Crash2",0.125,"Crash3",0.125,"Crash4",0.125,"Crash5",0.125,"Crash6",0.125,"Crash7",0.125],
    "bushcrash1": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Light_Bush_01",0.630957,1,50],
    "bushcrash2": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Light_Bush_02",0.630957,1,50],
    "bushcrash3": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Light_Bush_03",0.630957,1,50],
    "bushcrash4": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Light_Bush_03",0.630957,0.8,50],
    "soundbushcrash": ["BushCrash1",0.25,"BushCrash2",0.25,"BushCrash3",0.25,"BushCrash4",0.25],
    # Class: CfgVehicles|OTR21_Base|Sounds [Indent level: 1],
    "sounds": {
        "soundsetsint": ["RHS_OTR21_Engine_RPM0_INT_SoundSet","RHS_OTR21_Engine_RPM1_INT_SoundSet","RHS_OTR21_Engine_RPM2_INT_SoundSet","RHS_OTR21_Engine_INT_Burst_SoundSet","RHS_OTR21_Rattling_INT_SoundSet","RHS_OTR21_Stress_INT_SoundSet","RHS_OTR21_Rain_INT_SoundSet","RHS_OTR21_Tires_Rock_Fast_INT_SoundSet","RHS_OTR21_Tires_Grass_Fast_INT_SoundSet","RHS_OTR21_Tires_Sand_Fast_INT_SoundSet","RHS_OTR21_Tires_Gravel_Fast_INT_SoundSet","RHS_OTR21_Tires_Mud_Fast_INT_SoundSet","RHS_OTR21_Tires_Asphalt_Fast_INT_SoundSet","RHS_OTR21_Tires_Water_Fast_INT_SoundSet","RHS_OTR21_Tires_Rock_Slow_INT_SoundSet","RHS_OTR21_Tires_Grass_Slow_INT_SoundSet","RHS_OTR21_Tires_Sand_Slow_INT_SoundSet","RHS_OTR21_Tires_Gravel_Slow_INT_SoundSet","RHS_OTR21_Tires_Mud_Slow_INT_SoundSet","RHS_OTR21_Tires_Asphalt_Slow_INT_SoundSet","RHS_OTR21_Tires_Water_Slow_INT_SoundSet","RHS_OTR21_Tires_Turn_Hard_INT_SoundSet","RHS_OTR21_Tires_Turn_Soft_INT_SoundSet","RHS_OTR21_Tires_Brake_Hard_INT_SoundSet","RHS_OTR21_Tires_Brake_Soft_INT_SoundSet"],
        "soundsetsext": ["RHS_OTR21_Engine_RPM0_EXT_SoundSet","RHS_OTR21_Engine_RPM1_EXT_SoundSet","RHS_OTR21_Engine_RPM2_EXT_SoundSet","RHS_OTR21_Engine_EXT_Burst_SoundSet","RHS_OTR21_Rattling_EXT_SoundSet","RHS_OTR21_Stress_EXT_SoundSet","RHS_OTR21_Rain_EXT_SoundSet","RHS_OTR21_Tires_Rock_Fast_EXT_SoundSet","RHS_OTR21_Tires_Grass_Fast_EXT_SoundSet","RHS_OTR21_Tires_Sand_Fast_EXT_SoundSet","RHS_OTR21_Tires_Gravel_Fast_EXT_SoundSet","RHS_OTR21_Tires_Mud_Fast_EXT_SoundSet","RHS_OTR21_Tires_Asphalt_Fast_EXT_SoundSet","RHS_OTR21_Tires_Water_Fast_EXT_SoundSet","RHS_OTR21_Tires_Rock_Slow_EXT_SoundSet","RHS_OTR21_Tires_Grass_Slow_EXT_SoundSet","RHS_OTR21_Tires_Sand_Slow_EXT_SoundSet","RHS_OTR21_Tires_Gravel_Slow_EXT_SoundSet","RHS_OTR21_Tires_Mud_Slow_EXT_SoundSet","RHS_OTR21_Tires_Asphalt_Slow_EXT_SoundSet","RHS_OTR21_Tires_Water_Slow_EXT_SoundSet","RHS_OTR21_Tires_Turn_Hard_EXT_SoundSet","RHS_OTR21_Tires_Turn_Soft_EXT_SoundSet","RHS_OTR21_Tires_Brake_Hard_EXT_SoundSet","RHS_OTR21_Tires_Brake_Soft_EXT_SoundSet"]
    },
    # Class: CfgVehicles|Truck_F|SpeechVariants [Indent level: 1],
    "speechvariants": {
        # Class: CfgVehicles|Truck_F|SpeechVariants|Default [Indent level: 2]
        "default": {
            "speechsingular": ["veh_vehicle_truck_s"],
            "speechplural": ["veh_vehicle_truck_p"]
        }
    },
    "textsingular": "truck",
    "textplural": "trucks",
    "namesound": "veh_vehicle_truck_s",
    "_generalmacro": "Truck_F",
    "fuelexplosionpower": 5,
    "supplyradius": 2.5,
    "audible": 9,
    "epeimpulsedamagecoef": 15,
    "crewcrashprotection": 2.65,
    "crewexplosionprotection": 0.8,
    "maximumload": 3000,
    "transportmaxbackpacks": 64,
    "transportmaxmagazines": 256,
    "transportmaxweapons": 64,
    # Class: CfgVehicles|Truck_F|PlayerSteeringCoefficients [Indent level: 1],
    "playersteeringcoefficients": {
        "turnincreaseconst": 0.5,
        "turnincreaselinear": 1,
        "turnincreasetime": 0,
        "turndecreaseconst": 5,
        "turndecreaselinear": 0,
        "turndecreasetime": 0,
        "maxturnhundred": 1
    },
    # Class: CfgVehicles|Truck_F|TransportBackpacks [Indent level: 1],
    "transportbackpacks": {
    },
    # Class: CfgVehicles|Truck_F|TransportWeapons [Indent level: 1],
    "transportweapons": {
    },
    # Class: CfgVehicles|Truck_F|TransportItems [Indent level: 1],
    "transportitems": {
        # Class: CfgVehicles|Truck_F|TransportItems|_xx_FirstAidKit [Indent level: 2]
        "_xx_firstaidkit": {
            "name": "FirstAidKit",
            "count": 10
        }
    },
    "numberphysicalwheels": 6,
    "occludesoundswhenin": 0,
    "obstructsoundswhenin": 0,
    "secondaryexplosion": -10,
    "dammagehalf": [],
    "dammagefull": [],
    "armorstructural": 4,
    "explosionshielding": 1,
    "mintotaldamagethreshold": 0.01,
    "getinaction": "GetInLow",
    "getoutaction": "GetOutLow",
    "cargogetinaction": ["GetInLow"],
    "cargogetoutaction": ["GetOutLow"],
    "gunnerhasflares": 0,
    "steeraheadsimul": 0.5,
    "steeraheadplan": 0.35,
    "predictturnplan": 2,
    "predictturnsimul": 1.5,
    "accelaidforceyoffset": -1,
    "drivercansee": "1 + 2 + 4 + 8 + 32",
    "gunnercansee": "1 + 2 + 4 + 8 + 32",
    "commandercansee": "1 + 2 + 4 + 8 + 32",
    "headgforceleaningfactor": [0.01,0.01,0.015],
    # Class: CfgVehicles|Car_F|NewTurret [Indent level: 1],
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
    "driverrighthandanimname": "drivewheel",
    "driverleftleganimname": "",
    "driverrightleganimname": "pedal_thrust",
    "holdoffroadformation": 1,
    # Class: CfgVehicles|Car_F|NVGMarkers [Indent level: 1],
    "nvgmarkers": {
        # Class: CfgVehicles|Car_F|NVGMarkers|NVGMarker01 [Indent level: 2]
        "nvgmarker01": {
            "name": "nvg_marker",
            "color": [0.03,0.003,0.003,1],
            "ambient": [0.003,0.0003,0.0003,1],
            "brightness": 0.001,
            "blinking": 1
        }
    },
    "viewcargoshadowdiff": 1,
    "viewcargoshadowamb": 1,
    "insidesoundcoef": 0.9,
    "soundenviron": ["",0.000562341,1],
    "soundcrash": ["A3|sounds_f|dummysound",1,1],
    "extcameraposition": [0.5,2,-10],
    "soundgear": ["",1e-005,1],
    "collisioneffect": "collisionEffect",
    "hideunitinfo": 0,
    "memorypointsupply": "doplnovani",
    "braketorque": 6000,
    "longstiff": 15000,
    "latstiffx": 2000,
    "latstiffy": 18000,
    "wheelmask": "wheel_X_X",
    "aggregatereflectors": [["Left","Right","Left2","Right2"]],
    "camshakecoef": 0.2,
    "maxgforce": 3,
    # Class: CfgVehicles|Car_F|camShakeGForce [Indent level: 1],
    "camshakegforce": {
        "power": 2,
        "frequency": 60,
        "distance": 0,
        "minspeed": 60
    },
    # Class: CfgVehicles|Car_F|Components [Indent level: 1],
    "components": {
        # Class: CfgVehicles|Car|Components|AICarSteeringComponent [Indent level: 2]
        "aicarsteeringcomponent": {
            "steeringpidweights": [2.9,0.1,0.2],
            "speedpidweights": [0.7,0.2,0],
            "convoypidweights": [1,0.01,0.01],
            "doremapspeed": 1,
            "remapspeedrange": [30,70],
            "remapspeedscalar": [1,0.35],
            "dopredictforward": 1,
            "predictforwardrange": [1,20],
            "steeraheadsaturation": [0.01,0.4],
            "speedpredictionmethod": 2,
            "wheelanglecoef": 0.7,
            "forwardanglecoef": 0.7,
            "steeringanglecoef": 1,
            "differenceanglecoef": 0.4,
            "stuckmaxtime": 3,
            "allowovertaking": 1,
            "allowdrifting": 0,
            "allowcollisionavoidance": 1,
            "maxwheelanglediff": 0.2616,
            "minspeedtokeep": 0.1,
            "commandturnfactor": 1
        },
        # Class: CfgVehicles|LandVehicle|Components|TransportCountermeasuresComponent [Indent level: 2],
        "transportcountermeasurescomponent": {
        }
    },
    "unloadincombat": 1,
    "limitedspeedcoef": 0.5,
    "hulldamagecauseexplosion": 1,
    # Class: CfgVehicles|Car|PlateInfos [Indent level: 1],
    "plateinfos": {
        "name": "spz",
        "color": [0,0,0,0.75]
    },
    "selectionfireanim": "zasleh",
    "alphatracks": 0.2,
    "memorypointtrackfll": "Stopa PLL",
    "memorypointtrackflr": "Stopa PLP",
    "memorypointtrackbll": "Stopa ZLL",
    "memorypointtrackblr": "Stopa ZLP",
    "memorypointtrackfrl": "Stopa PPL",
    "memorypointtrackfrr": "Stopa PPP",
    "memorypointtrackbrl": "Stopa ZPL",
    "memorypointtrackbrr": "Stopa ZPP",
    "memorypointcirculumreference": "circulumReference",
    "gearbox": [-8,0,10,6.15,4.44,3.33],
    "scudeffect": "ScudEffect",
    "armorlights": 0.4,
    "preferroads": 1,
    "formationx": 20,
    "formationz": 20,
    "type": 0,
    "scudmodel": "",
    "dampersize": 0.1,
    "damperforce": 1,
    "damperdamping": 1,
    "inputturncurve": [[0,[0,0,1,1]],[30,[0,0,0.2,0.008,0.4,0.032,0.6,0.216,0.8,0.512,1,1]]],
    "enablegps": 0,
    "soundengine": ["",1.77828,0.9],
    "memorypointtaskmarkeroffset": [0,0.3,0],
    "rightdusteffects": [["GdtKLDirt","RDustEffects"],["GdtKLGrass1","RDustEffects"],["GdtKLGrass1","RGrassEffects"],["GdtKLGrass2","RDustEffects"],["GdtKLGrass2","RGrassEffects"],["GdtKLForestCon","RDustEffects"],["GdtKLForestDec","RDustEffects"],["GdtKlMud","RDustEffects"],["GdtKlSoil","RDustEffects"],["GdtKlTarmac","RDustEffects"],["GdtKlStubble","RDustEffects"],["GdtKlStones","RStonesEffects"],["SurfRoadDirt_Enoch","RDustEffects"],["SurfTrailDirt_Enoch","RDustEffects"],["SurfRoadTarmac1_Enoch","RDustEffects"],["SurfRoadTarmac2_Enoch","RDustEffects"],["SurfRoadTarmac3_Enoch","RDustEffects"],["GdtGrassShort","RDustEffects"],["GdtGrassShort","RGrassEffects"],["GdtGrassTall","RDustEffects"],["GdtGrassTall","RGrassEffects"],["GdtRedDirt","RDustEffectsRed"],["GdtField","RDustEffects"],["GdtForest","RDustEffects"],["GdtVolcano","RDustEffects"],["GdtVolcano","RStonesEffects"],["GdtCliff","RDustEffects"],["GdtVolcanoBeach","RDustEffects"],["SurfRoadDirt_exp","RDustEffectsRed"],["SurfRoadConcrete_exp","RDustEffects"],["SurfRoadTarmac_exp","RDustEffects"],["GdtStratisConcrete","RDustEffects"],["GdtStratisConcrete","RDirtEffects"],["GdtStratisBeach","RDustEffects"],["GdtStratisBeach","RStonesEffects"],["GdtStratisDirt","RDustEffects"],["GdtStratisDirt","RDirtEffects"],["GdtStratisSeabedCluttered","RDustEffects"],["GdtStratisSeabed","RDustEffects"],["GdtStratisDryGrass","RDustEffects"],["GdtStratisDryGrass","RGrassDryEffects"],["GdtStratisDryGrass","RDirtEffects"],["GdtStratisGreenGrass","RDustEffects"],["GdtStratisGreenGrass","RGrassEffects"],["GdtStratisGreenGrass","RDirtEffects"],["GdtStratisRocky","RDustEffects"],["GdtStratisRocky","RGrassEffects"],["GdtStratisRocky","RDirtEffects"],["GdtStratisThistles","RDustEffects"],["GdtStratisThistles","RGrassEffects"],["GdtStratisThistles","RDirtEffects"],["GdtConcrete","RDustEffects"],["GdtConcrete","RDirtEffects"],["GdtAsphalt","RDustEffects"],["GdtAsphalt","RDirtEffects"],["GdtRubble","RDustEffects"],["GdtRubble","RDirtEffects"],["GdtSoil","RDustEffects"],["GdtSoil","RDirtEffects"],["GdtBeach","RDustEffects"],["GdtBeach","RStonesEffects"],["GdtRock","RDustEffects"],["GdtRock","RDirtEffects"],["GdtDead","RDustEffects"],["GdtDead","RDirtEffects"],["Default","RDustEffects"],["GdtDesert","RDustEffects"],["GdtDesert","RStonesEffects"],["GdtDesert1","RDustEffects"],["GdtDesert1","RSandEffects"],["GdtDesert1","RDirtEffects"],["GdtDesert1","RStonesEffects"],["GdtDesert2","RDustEffects"],["GdtDesert2","RSandEffects"],["GdtDesert2","RGrassEffects"],["GdtDesert2","RDirtEffects"],["GdtDirt","RDustEffects"],["GdtDirt","RDirtEffects"],["GdtGrassGreen","RDustEffects"],["GdtGrassGreen","RGrassEffects"],["GdtGrassGreen","RDirtEffects"],["GdtGrassDry","RDustEffects"],["GdtGrassDry","RGrassDryEffects"],["GdtGrassDry","RDirtEffects"],["GdtGrassWild","RDustEffects"],["GdtGrassWild","RGrassEffects"],["GdtGrassWild","RDirtEffects"],["GdtWildField","RDustEffects"],["GdtWildField","RGrassEffects"],["GdtWildField","RDirtEffects"],["GdtWeed1","RDustEffects"],["GdtWeed1","RGrassEffects"],["GdtWeed1","RDirtEffects"],["GdtWeed2","RDustEffects"],["GdtWeed2","RGrassEffects"],["GdtWeed2","RDirtEffects"],["GdtThorn","RDustEffects"],["GdtThorn","RGrassEffects"],["GdtThorn","RDirtEffects"],["GdtStony","RDustEffects"],["GdtStony","RGrassEffects"],["GdtStony","RDirtEffects"],["GdtStonyGreen","RDustEffects"],["GdtStonyGreen","RGrassEffects"],["GdtStonyGreen","RDirtEffects"],["GdtStonyThistle","RDustEffects"],["GdtStonyThistle","RGrassEffects"],["GdtStonyThistle","RDirtEffects"],["GdtSeabedDeep","RDustEffects"],["GdtSeabed","RDustEffects"],["SurfRoadDirt","RDustEffects"],["SurfRoadConcrete","RDustEffects"],["SurfRoadTarmac","RDustEffects"],["SurfWood","RDustEffects"],["SurfMetal","RDustEffects"],["SurfRoofTin","RDustEffects"],["SurfRoofTiles","RDustEffects"],["SurfIntWood","RDustEffects"],["SurfIntConcrete","RDustEffects"],["SurfIntTiles","RDustEffects"],["SurfIntMetal","RDustEffects"],["dirtrunway","RDustEffects"]],
    "leftdusteffects": [["GdtKLDirt","LDustEffects"],["GdtKLGrass1","LDustEffects"],["GdtKLGrass1","LGrassEffects"],["GdtKLGrass2","LDustEffects"],["GdtKLGrass2","LGrassEffects"],["GdtKLForestCon","LDustEffects"],["GdtKLForestDec","LDustEffects"],["GdtKlMud","LDustEffects"],["GdtKlSoil","LDustEffects"],["GdtKlTarmac","LDustEffects"],["GdtKlStubble","LDustEffects"],["GdtKlStones","LStonesEffects"],["SurfRoadDirt_Enoch","LDustEffects"],["SurfTrailDirt_Enoch","LDustEffects"],["SurfRoadTarmac1_Enoch","LDustEffects"],["SurfRoadTarmac2_Enoch","LDustEffects"],["SurfRoadTarmac3_Enoch","LDustEffects"],["GdtGrassShort","LDustEffects"],["GdtGrassShort","LGrassEffects"],["GdtGrassTall","LDustEffects"],["GdtGrassTall","LGrassEffects"],["GdtRedDirt","LDustEffectsRed"],["GdtField","LDustEffects"],["GdtForest","LDustEffects"],["GdtVolcano","LDustEffects"],["GdtVolcano","LStonesEffects"],["GdtCliff","LDustEffects"],["GdtVolcanoBeach","LDustEffects"],["SurfRoadDirt_exp","LDustEffectsRed"],["SurfRoadConcrete_exp","LDustEffects"],["SurfRoadTarmac_exp","LDustEffects"],["GdtStratisConcrete","LDustEffects"],["GdtStratisConcrete","LDirtEffects"],["GdtStratisBeach","LDustEffects"],["GdtStratisBeach","LStonesEffects"],["GdtStratisDirt","LDustEffects"],["GdtStratisDirt","LDirtEffects"],["GdtStratisSeabedCluttered","LDustEffects"],["GdtStratisSeabed","LDustEffects"],["GdtStratisDryGrass","LDustEffects"],["GdtStratisDryGrass","LGrassDryEffects"],["GdtStratisDryGrass","LDirtEffects"],["GdtStratisGreenGrass","LDustEffects"],["GdtStratisGreenGrass","LGrassEffects"],["GdtStratisGreenGrass","LDirtEffects"],["GdtStratisRocky","LDustEffects"],["GdtStratisRocky","LGrassEffects"],["GdtStratisRocky","LDirtEffects"],["GdtStratisThistles","LDustEffects"],["GdtStratisThistles","LGrassEffects"],["GdtStratisThistles","LDirtEffects"],["GdtConcrete","LDustEffects"],["GdtConcrete","LDirtEffects"],["GdtAsphalt","LDustEffects"],["GdtAsphalt","LDirtEffects"],["GdtRubble","LDustEffects"],["GdtRubble","LDirtEffects"],["GdtSoil","LDustEffects"],["GdtSoil","LDirtEffects"],["GdtBeach","LDustEffects"],["GdtBeach","LStonesEffects"],["GdtRock","LDustEffects"],["GdtRock","LDirtEffects"],["GdtDead","LDustEffects"],["GdtDead","LDirtEffects"],["Default","LDustEffects"],["GdtDesert","LDustEffects"],["GdtDesert","LStonesEffects"],["GdtDesert1","LDustEffects"],["GdtDesert1","LSandEffects"],["GdtDesert1","LDirtEffects"],["GdtDesert1","LStonesEffects"],["GdtDesert2","LDustEffects"],["GdtDesert2","LSandEffects"],["GdtDesert2","LGrassEffects"],["GdtDesert2","LDirtEffects"],["GdtDirt","LDustEffects"],["GdtDirt","LDirtEffects"],["GdtGrassGreen","LDustEffects"],["GdtGrassGreen","LGrassEffects"],["GdtGrassGreen","LDirtEffects"],["GdtGrassDry","LDustEffects"],["GdtGrassDry","LGrassDryEffects"],["GdtGrassDry","LDirtEffects"],["GdtGrassWild","LDustEffects"],["GdtGrassWild","LGrassEffects"],["GdtGrassWild","LDirtEffects"],["GdtWildField","LDustEffects"],["GdtWildField","LGrassEffects"],["GdtWildField","LDirtEffects"],["GdtWeed1","LDustEffects"],["GdtWeed1","LGrassEffects"],["GdtWeed1","LDirtEffects"],["GdtWeed2","LDustEffects"],["GdtWeed2","LGrassEffects"],["GdtWeed2","LDirtEffects"],["GdtThorn","LDustEffects"],["GdtThorn","LGrassEffects"],["GdtThorn","LDirtEffects"],["GdtStony","LDustEffects"],["GdtStony","LGrassEffects"],["GdtStony","LDirtEffects"],["GdtStonyGreen","LDustEffects"],["GdtStonyGreen","LGrassEffects"],["GdtStonyGreen","LDirtEffects"],["GdtStonyThistle","LDustEffects"],["GdtStonyThistle","LGrassEffects"],["GdtStonyThistle","LDirtEffects"],["GdtSeabedDeep","LDustEffects"],["GdtSeabed","LDustEffects"],["SurfRoadDirt","LDustEffects"],["SurfRoadConcrete","LDustEffects"],["SurfRoadTarmac","LDustEffects"],["SurfWood","LDustEffects"],["SurfMetal","LDustEffects"],["SurfRoofTin","LDustEffects"],["SurfRoofTiles","LDustEffects"],["SurfIntWood","LDustEffects"],["SurfIntConcrete","LDustEffects"],["SurfIntTiles","LDustEffects"],["SurfIntMetal","LDustEffects"],["dirtrunway","LDustEffects"]],
    # Class: CfgVehicles|Car|DustEffects [Indent level: 1],
    "dusteffects": {
        # Class: CfgDustEffectsCar|Both [Indent level: 0]
        "both": {
        },
        # Class: CfgDustEffectsCar|Left [Indent level: 0],
        "left": {
            "default": ["LDustEffects"],
            "gdtstratisconcrete": ["LDustEffects"],
            "gdtstratisbeach": ["LDustEffects"],
            "gdtstratisdirt": ["LDustEffects"],
            "gdtstratisseabedcluttered": ["LDustEffects"],
            "gdtstratisseabed": ["LDustEffects"],
            "gdtstratisdrygrass": ["LDustEffects"],
            "gdtstratisgreengrass": ["LDustEffects"],
            "gdtstratisrocky": ["LDustEffects"],
            "gdtstratisthistles": ["LDustEffects"],
            "gdtconcrete": ["LDustEffects"],
            "gdtasphalt": ["LDustEffects"],
            "gdtrubble": ["LDustEffects"],
            "gdtsoil": ["LDustEffects"],
            "gdtbeach": ["LDustEffects"],
            "gdtrock": ["LDustEffects"],
            "gdtdead": ["LDustEffects"],
            "gdtdesert": ["LDustEffects"],
            "gdtdesert1": ["LDustEffects"],
            "gdtdesert2": ["LDustEffects"],
            "gdtdirt": ["LDustEffects"],
            "gdtgrassgreen": ["LDustEffects"],
            "gdtgrassdry": ["LDustEffects"],
            "gdtgrasswild": ["LDustEffects","LGrassEffects","LDirtEffects"],
            "gdtwildfield": ["LDustEffects","LGrassEffects","LDirtEffects"],
            "gdtweed1": ["LDustEffects","LGrassEffects","LDirtEffects"],
            "gdtweed2": ["LDustEffects","LGrassEffects","LDirtEffects"],
            "gdtthorn": ["LDustEffects","LGrassEffects","LDirtEffects"],
            "gdtstony": ["LDustEffects","LGrassEffects","LDirtEffects"],
            "gdtstonygreen": ["LDustEffects","LGrassEffects","LDirtEffects"],
            "gdtstonythistle": ["LDustEffects","LGrassEffects","LDirtEffects"],
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
            "gdtgrassshort": ["LDustEffects","LGrassEffects"],
            "gdtgrasstall": ["LDustEffects","LGrassEffects"],
            "gdtreddirt": ["LDustEffectsRed"],
            "gdtfield": ["LDustEffects"],
            "gdtforest": ["LDustEffects"],
            "gdtvolcano": ["LDustEffects","LStonesEffects"],
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
        # Class: CfgDustEffectsCar|Right [Indent level: 0],
        "right": {
            "default": ["RDustEffects"],
            "gdtstratisconcrete": ["RDustEffects"],
            "gdtstratisbeach": ["RDustEffects"],
            "gdtstratisdirt": ["RDustEffects"],
            "gdtstratisseabedcluttered": ["RDustEffects"],
            "gdtstratisseabed": ["RDustEffects"],
            "gdtstratisdrygrass": ["RDustEffects"],
            "gdtstratisgreengrass": ["RDustEffects"],
            "gdtstratisrocky": ["RDustEffects"],
            "gdtstratisthistles": ["RDustEffects"],
            "gdtconcrete": ["RDustEffects"],
            "gdtasphalt": ["RDustEffects"],
            "gdtrubble": ["RDustEffects"],
            "gdtsoil": ["RDustEffects"],
            "gdtbeach": ["RDustEffects"],
            "gdtrock": ["RDustEffects"],
            "gdtdead": ["RDustEffects"],
            "gdtdesert": ["RDustEffects"],
            "gdtdesert1": ["RDustEffects"],
            "gdtdesert2": ["RDustEffects"],
            "gdtdirt": ["RDustEffects"],
            "gdtgrassgreen": ["RDustEffects"],
            "gdtgrassdry": ["RDustEffects"],
            "gdtgrasswild": ["RDustEffects","RGrassEffects","RDirtEffects"],
            "gdtwildfield": ["RDustEffects","RGrassEffects","RDirtEffects"],
            "gdtweed1": ["RDustEffects","RGrassEffects","RDirtEffects"],
            "gdtweed2": ["RDustEffects","RGrassEffects","RDirtEffects"],
            "gdtthorn": ["RDustEffects","RGrassEffects","RDirtEffects"],
            "gdtstony": ["RDustEffects","RGrassEffects","RDirtEffects"],
            "gdtstonygreen": ["RDustEffects","RGrassEffects","RDirtEffects"],
            "gdtstonythistle": ["RDustEffects","RGrassEffects","RDirtEffects"],
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
            "gdtgrassshort": ["RDustEffects","RGrassEffects"],
            "gdtgrasstall": ["RDustEffects","RGrassEffects"],
            "gdtreddirt": ["RDustEffectsRed"],
            "gdtfield": ["RDustEffects"],
            "gdtforest": ["RDustEffects"],
            "gdtvolcano": ["RDustEffects","RStonesEffects"],
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
    # Class: CfgVehicles|Car|DestructionEffects [Indent level: 1],
    "destructioneffects": {
        # Class: CfgVehicles|Car|DestructionEffects|Light1 [Indent level: 2]
        "light1": {
            "simulation": "light",
            "type": "ObjectDestructionLight",
            "position": "destructionEffect1",
            "intensity": 0.001,
            "interval": 1,
            "lifetime": 3,
            "enabled": "distToWater"
        },
        # Class: CfgVehicles|Car|DestructionEffects|Sound [Indent level: 2],
        "sound": {
            "simulation": "sound",
            "position": "destructionEffect1",
            "intensity": 1,
            "interval": 1,
            "lifetime": 1,
            "type": "Fire"
        },
        # Class: CfgVehicles|Car|DestructionEffects|Fire1 [Indent level: 2],
        "fire1": {
            "simulation": "particles",
            "type": "ObjectDestructionFire1Small",
            "position": "destructionEffect1",
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 3
        },
        # Class: CfgVehicles|Car|DestructionEffects|Refract1 [Indent level: 2],
        "refract1": {
            "simulation": "particles",
            "type": "ObjectDestructionRefractSmall",
            "position": "destructionEffect1",
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 3
        },
        # Class: CfgVehicles|Car|DestructionEffects|Smoke1 [Indent level: 2],
        "smoke1": {
            "simulation": "particles",
            "type": "ObjectDestructionSmokeSmall",
            "position": "destructionEffect1",
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 3.5
        },
        # Class: CfgVehicles|Car|DestructionEffects|Sparks1 [Indent level: 2],
        "sparks1": {
            "simulation": "particles",
            "type": "ObjectDestructionSparks",
            "position": "destructionEffect1",
            "intensity": 0,
            "interval": 1,
            "lifetime": 0
        },
        # Class: CfgVehicles|Car|DestructionEffects|FireSparks1 [Indent level: 2],
        "firesparks1": {
            "simulation": "particles",
            "type": "FireSparks",
            "position": "destructionEffect2",
            "intensity": 1,
            "interval": 1,
            "lifetime": 2.8
        },
        # Class: CfgVehicles|Car|DestructionEffects|Fire2 [Indent level: 2],
        "fire2": {
            "simulation": "particles",
            "type": "ObjectDestructionFire2Small",
            "position": "destructionEffect2",
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 3
        },
        # Class: CfgVehicles|Car|DestructionEffects|Smoke1_2 [Indent level: 2],
        "smoke1_2": {
            "simulation": "particles",
            "type": "ObjectDestructionSmoke1_2Small",
            "position": "destructionEffect2",
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 3.5
        },
        # Class: CfgVehicles|Car|DestructionEffects|Smoke2 [Indent level: 2],
        "smoke2": {
            "simulation": "particles",
            "type": "ObjectDestructionSmoke2",
            "position": "destructionEffect2",
            "intensity": 1,
            "interval": 1,
            "lifetime": 3.2
        }
    },
    "sensitivityear": 0.125,
    "sensitivity": 1.75,
    "selectionbrakelights": "brzdove svetlo",
    "memorypointmissile": ["spice rakety","usti hlavne"],
    "memorypointmissiledir": ["konec rakety","konec hlavne"],
    "enginestartspeed": 1.5,
    "leftdusteffect": "LDustEffects",
    "rightdusteffect": "RDustEffects",
    "leftwatereffect": "LWaterEffects",
    "rightwatereffect": "RWaterEffects",
    "leftfastwatereffect": "LWaterEffects",
    "rightfastwatereffect": "RWaterEffects",
    "tracksspeed": 0,
    "selectionleftoffset": "PasOffsetL",
    "selectionrightoffset": "PasOffsetP",
    "explosioneffect": "FuelExplosion",
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
    # Class: CfgVehicles|AllVehicles|ViewOptics [Indent level: 1],
    "viewoptics": {
        "initanglex": 0,
        "minanglex": -30,
        "maxanglex": 30,
        "initangley": 0,
        "minangley": -100,
        "maxangley": 100,
        "initfov": 0.7,
        "minfov": 0.42,
        "maxfov": 0.85,
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
    "cargoproxyindexes": [],
    "driverdoor": "",
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
    "camouflage": 2,
    "spotabledarknightlightsoff": 0.001,
    "spotablenightlightsoff": 0.02,
    "spotablenightlightson": 4,
    "accuracydarknightlightsoff": 0.001,
    "accuracynightlightsoff": 0.006,
    "accuracynightlightson": 0.1,
    "outsidesoundfilter": 0,
    "obstructsoundlfratio": 0,
    "occludesoundlfratio": 0.25,
    "portrait": "",
    "ghostpreview": "",
    "destrtype": "DestructDefault",
    "crewvulnerable": 1,
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
    "irscanrangemin": 0,
    "irscanrangemax": 0,
    "irscantoeyefactor": 1,
    "irscanground": 1,
    "lasertarget": 0,
    "laserscanner": 0,
    "nvtarget": 0,
    "nvscanner": 0,
    "artillerytarget": 0,
    "canusescanners": 1,
    "unitinfotypelite": 0,
    "nightvision": 0,
    "radartype": 0,
    "hasdriver": 1,
    "driverforceoptics": 0,
    "hideweaponsdriver": 1,
    "hideweaponscargo": 0,
    "getinradius": 2.5,
    "enablewatch": 0,
    "enableradio": 0,
    "lockdetectionsystem": 0,
    "incomingmissiledetectionsystem": 0,
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
    "isbackpack": 0,
    "transportfuel": 0,
    "transportvehiclescount": 0,
    "transportvehiclesmass": 0,
    "attendant": 0,
    "engineer": 0,
    "uavhacker": 0,
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
    "soundlandcrashes": ["soundLandCrash",1],
    "soundwatercrashes": ["soundWaterCrash",1],
    "emptysound": ["",0,1],
    "soundlocked": ["",1,1],
    "soundincommingmissile": ["",1,1],
    "driverinaction": "",
    "drivercompartments": "Compartment1",
    "cargocompartments": ["Compartment1"],
    "driveropticsmodel": "",
    "driveropticseffect": [],
    "driveropticscolor": [1,1,1,1],
    "forcehidedriver": 0,
    "canhidedriver": -1,
    "castdrivershadow": 0,
    "castcargoshadow": 0,
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
    "mingforce": 0.2,
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