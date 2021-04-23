rhs_towedweapons_base = {
    # Class: CfgVehicles|RHS_TowedWeapons_Base|Hitpoints [Indent level: 1]
    "hitpoints": {
    },
    # Class: CfgVehicles|RHS_TowedWeapons_Base|Reflectors [Indent level: 1],
    "reflectors": {
    },
    # Class: CfgVehicles|RHS_TowedWeapons_Base|Turrets [Indent level: 1],
    "turrets": {
    },
    # Class: CfgVehicles|RHS_TowedWeapons_Base|UserActions [Indent level: 1],
    "useractions": {
        # Class: CfgVehicles|RHS_TowedWeapons_Base|UserActions|Detach [Indent level: 2]
        "detach": {
            "displaynamedefault": "<img image='|rhsusf|addons|rhsusf_main|data|actions|rhs_tow_detach_ca.paa' size='3.5' />",
            "displayname": "<img image='|rhsusf|addons|rhsusf_main|data|actions|rhs_tow_detach_ca.paa' size='1.5' /> <t color='#00FF7F'>Detach vehicle</t>",
            "position": "",
            "radius": 2.5,
            "onlyforplayer": 1,
            "priority": 15,
            "showwindow": 1,
            "condition": "(alive this) && {speed this < 3}  && {this getVariable ['rhs_towing_detach',true]}",
            "statement": "[this] spawn rhs_fnc_towing_detach;"
        }
    },
    # Class: CfgVehicles|RHS_TowedWeapons_Base|EventHandlers [Indent level: 1],
    "eventhandlers": {
        "killed": "_this call rhs_fnc_towing_destroyed",
        "fired": "",
        "init": ""
    },
    "simulation": "helicopterX",
    "destrtype": "DestructDefault",
    "armor": 80,
    "armorstructural": 50,
    "epeimpulsedamagecoef": 1,
    "gearretracting": 1,
    "hasdriver": 0,
    "secondaryexplosion": 0,
    "fuelexplosionpower": 0,
    "disableinventory": 1,
    "author": "Bohemia Interactive",
    "_generalmacro": "Helicopter_Base_F",
    "side": 3,
    "faction": "CIV_F",
    "crew": "C_man_pilot_F",
    "drivercansee": "1 + 2 + 4 + 8 + 32",
    "gunnercansee": "1 + 2 + 4 + 8 + 32",
    "commandercansee": "1 + 2 + 4 + 8 + 32",
    "washdownstrength": "1.0f",
    "washdowndiameter": "40.0f",
    "minsmokedamage": 0.3,
    "maxsmokedamage": 0.99,
    "selectionhrotorstill": "main rotor static",
    "selectionhrotormove": "main rotor blur",
    "selectionvrotorstill": "tail rotor static",
    "selectionvrotormove": "tail rotor blur",
    "driverlefthandanimname": "lever_pilot",
    "driverrighthandanimname": "stick_pilot",
    "driverleftleganimname": "pedalL",
    "driverrightleganimname": "pedalR",
    # Class: CfgVehicles|Helicopter_Base_F|CamShake [Indent level: 1],
    "camshake": {
        "power": 30,
        "frequency": 20,
        "distance": 50,
        "minspeed": 50
    },
    "camshakecoef": 0,
    "unitinfotypertd": "RscUnitInfoAirRTDFullDigital",
    "unitinfotypelite": "RscUnitInfoAirRTDBasic",
    "unitinfotype": "RscUnitInfoAir",
    "vehicleclass": "Air",
    "icon": "iconHelicopter",
    "displayname": "Helicopter",
    "dusteffect": "HeliDust",
    "watereffect": "HeliWater",
    "gearuptime": 3.33,
    "geardowntime": 2,
    "gearminalt": 0.5,
    # Class: CfgVehicles|Helicopter|ViewPilot [Indent level: 1],
    "viewpilot": {
        "initfov": 0.9,
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
    # Class: CfgVehicles|Helicopter|CargoSpec [Indent level: 1],
    "cargospec": {
        # Class: CfgVehicles|Helicopter|CargoSpec|Cargo1 [Indent level: 2]
        "cargo1": {
            "showheadphones": 1
        },
        # Class: CfgVehicles|Helicopter|CargoSpec|Cargo2 [Indent level: 2],
        "cargo2": {
            "showheadphones": 0
        }
    },
    "mainrotorspeed": 1,
    "backrotorspeed": 1.5,
    "startduration": 20,
    "mainbladeradius": 0,
    "maxmainrotordive": 0,
    "maxbackrotordive": 0,
    "minmainrotordive": 0,
    "minbackrotordive": 0,
    "neutralbackrotordive": 0,
    "neutralmainrotordive": 0,
    "liftforcecoef": 1,
    "cyclicasideforcecoef": 1,
    "cyclicforwardforcecoef": 1,
    "backrotorforcecoef": 1,
    "bodyfrictioncoef": 1,
    "memorypointlmissile": "L strela",
    "memorypointrmissile": "P strela",
    "memorypointlrocket": "L raketa",
    "memorypointrrocket": "P raketa",
    "memorypointgun": "",
    "memorypointpilot": "pilot",
    "_mainbladecenter": "rotor_center",
    "selectionfireanim": "zasleh",
    "maxspeed": 300,
    "enablesweep": 1,
    "envelope": [0,0.2,0.9,2.1,2.5,3.3,3.5,3.6,3.7,3.8,3.8,3,0.9,0.7,0.5],
    "minfiretime": 20,
    "steeraheadsimul": 0.5,
    "steeraheadplan": 0.7,
    # Class: CfgVehicles|Helicopter|ViewOptics [Indent level: 1],
    "viewoptics": {
        "initanglex": 0,
        "minanglex": -40,
        "maxanglex": 17,
        "initangley": 0,
        "minangley": -100,
        "maxangley": 100,
        "initfov": 0.5,
        "minfov": 0.3,
        "maxfov": 1.2,
        "minmovex": 0,
        "maxmovex": 0,
        "minmovey": 0,
        "maxmovey": 0,
        "minmovez": 0,
        "maxmovez": 0,
        "speedzoommaxspeed": 1e+010,
        "speedzoommaxfov": 0
    },
    # Class: CfgVehicles|Helicopter|MFD [Indent level: 1],
    "mfd": {
        # Class: CfgVehicles|Helicopter|MFD|HUD [Indent level: 2]
        "hud": {
            "topleft": "HUD LH",
            "topright": "HUD PH",
            "bottomleft": "HUD LD",
            "color": [0,1,0,0.1],
            # Class: AirplaneHUD|Pos10Vector [Indent level: 0],
            "pos10vector": {
                "type": "vector",
                "pos0": [0.5,0.27],
                "pos10": ["0.5+0.9","0.27+0.7"]
            },
            # Class: AirplaneHUD|Bones [Indent level: 0],
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
            # Class: AirplaneHUD|Draw [Indent level: 0],
            "draw": {
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
                # Class: AirplaneHUD|Draw|DimmedBase [Indent level: 1],
                "dimmedbase": {
                    "alpha": 0.3,
                    # Class: AirplaneHUD|Draw|DimmedBase|AltitudeBase [Indent level: 2],
                    "altitudebase": {
                        "type": "line",
                        "points": [["AGLMove2",1],["ASLMove2",1]]
                    }
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
                },
                # Class: AirplaneHUD|Draw|PlaneW [Indent level: 1],
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
                # Class: AirplaneHUD|Draw|MGun [Indent level: 1],
                "mgun": {
                    "condition": "mgun",
                    # Class: AirplaneHUD|Draw|MGun|Circle [Indent level: 2],
                    "circle": {
                        "type": "line",
                        "points": [["WeaponAim",[0,-0.07],1],["WeaponAim",["+0.7*0.07","-0.7*0.07"],1],["WeaponAim",[0.07,0],1],["WeaponAim",["+0.7*0.07","+0.7*0.07"],1],["WeaponAim",[0,0.07],1],["WeaponAim",["-0.7*0.07","+0.7*0.07"],1],["WeaponAim",[-0.07,0],1],["WeaponAim",["-0.7*0.07","-0.7*0.07"],1],["WeaponAim",[0,-0.07],1],[],["WeaponAim",[0,-0.01],1],["WeaponAim",["+0.7*0.01","-0.7*0.01"],1],["WeaponAim",[0.01,0],1],["WeaponAim",["+0.7*0.01","+0.7*0.01"],1],["WeaponAim",[0,0.01],1],["WeaponAim",["-0.7*0.01","+0.7*0.01"],1],["WeaponAim",[-0.01,0],1],["WeaponAim",["-0.7*0.01","-0.7*0.01"],1],["WeaponAim",[0,-0.01],1],[],["WeaponAim",["0.03*sin(-180)","-0.03*cos(-180)"],1],["WeaponAim",["0.07*sin(-180)","-0.07*cos(-180)"],1],[],["WeaponAim",["0.03*sin(+90)","-0.03*cos(+90)"],1],["WeaponAim",["0.07*sin(+90)","-0.07*cos(+90)"],1],[],["WeaponAim",1,"TargetDistanceMGun",[0,0.04],1],["WeaponAim",1,"TargetDistanceMGun",[0,0.07],1]]
                    }
                },
                # Class: AirplaneHUD|Draw|Missile [Indent level: 1],
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
                # Class: AirplaneHUD|Draw|Horizont [Indent level: 1],
                "horizont": {
                    "cliptl": [0.2,0.1],
                    "clipbr": [0.8,0.9],
                    # Class: AirplaneHUD|Draw|Horizont|Dimmed [Indent level: 2],
                    "dimmed": {
                        "alpha": 0.6,
                        # Class: AirplaneHUD|Draw|Horizont|Dimmed|Level0 [Indent level: 3],
                        "level0": {
                            "type": "line",
                            "points": [["Level0",[-0.4,0],1],["Level0",[-0.13,0],1],[],["Level0",[0.13,0],1],["Level0",[0.4,0],1]]
                        }
                    },
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
                # Class: AirplaneHUD|Draw|ILS [Indent level: 1],
                "ils": {
                    "condition": "ils",
                    # Class: AirplaneHUD|Draw|ILS|Glideslope [Indent level: 2],
                    "glideslope": {
                        "cliptl": [0.29,0.29],
                        "clipbr": [0.71,0.71],
                        # Class: AirplaneHUD|Draw|ILS|Glideslope|ILS [Indent level: 3],
                        "ils": {
                            "type": "line",
                            "points": [["ILS",[-10,0],1],["ILS",[10,0],1],[],["ILS",[0,-10],1],["ILS",[0,10],1]]
                        }
                    },
                    # Class: AirplaneHUD|Draw|ILS|AOABracket [Indent level: 2],
                    "aoabracket": {
                        "type": "line",
                        "points": [[[0.42,0.78],1],[[0.4,0.78],1],[[0.4,0.88],1],[[0.42,0.88],1]]
                    }
                }
            },
            "helmetposition": [-0.025,0.025,0.1],
            "helmetright": [0.05,0,0],
            "helmetdown": [-0,-0.05,0],
            "borderleft": 0.09,
            "borderright": 0.02,
            "bordertop": 0.02,
            "borderbottom": 0.1,
            "helmetmounteddisplay": 1
        }
    },
    "weapons": [],
    "magazines": [],
    # Class: CfgVehicles|Helicopter|Sounds [Indent level: 1],
    "sounds": {
        # Class: CfgVehicles|Helicopter|Sounds|Engine [Indent level: 2]
        "engine": {
            "sound": "soundEngine",
            "frequency": "(1-randomizer*0.05)*rotorSpeed*(1-rotorThrust*0.1)",
            "volume": "1"
        },
        # Class: CfgVehicles|Helicopter|Sounds|Movement [Indent level: 2],
        "movement": {
            "sound": "soundEnviron",
            "frequency": "1",
            "volume": "speed * 0.03334"
        }
    },
    "soundlandinggear": ["",1,1],
    # Class: CfgVehicles|Helicopter|Exhausts [Indent level: 1],
    "exhausts": {
    },
    # Class: CfgVehicles|Helicopter|RotorLibHelicopterProperties [Indent level: 1],
    "rotorlibhelicopterproperties": {
        "rtdconfig": "",
        "hasapu": 0,
        "maxtorque": 10000,
        "autohovercorrection": [0,0,0],
        "maxmainrotorstress": 10000,
        "maxtailrotorstress": 10000,
        "maxhorizontalstabilizerleftstress": 10000,
        "maxhorizontalstabilizerrightstress": 10000,
        "maxverticalstabilizerstress": 10000,
        "stressdamagepersec": 0.01,
        "retreatbladestallwarningspeed": 69.4,
        "horizontalwingsanglecollmin": 0,
        "horizontalwingsanglecollmax": 0,
        "defaultcollective": 0.7,
        "vrsshakepowercoef": 1
    },
    "slingloadmemorypoint": "slingLoad0",
    "slingloadmaxcargomass": 0,
    # Class: CfgVehicles|Helicopter|SpeechVariants [Indent level: 1],
    "speechvariants": {
        # Class: CfgVehicles|Helicopter|SpeechVariants|Default [Indent level: 2]
        "default": {
            "speechsingular": ["veh_air_helicopter_s"],
            "speechplural": ["veh_air_helicopter_p"]
        }
    },
    "editorsubcategory": "EdSubcat_Helicopters",
    "extcameraparams": [-1],
    "textsingular": "helicopter",
    "textplural": "helicopters",
    "namesound": "veh_air_helicopter_s",
    "accuracy": 0.02,
    "camouflage": 100,
    "audible": 50,
    "crewcrashprotection": 0.25,
    "headgforceleaningfactor": [0.01,0.0025,0.01],
    "getinaction": "GetInLow",
    "getoutaction": "GetOutLow",
    "cargogetinaction": ["GetInLow"],
    "cargogetoutaction": ["GetOutLow"],
    "drivercaneject": 0,
    "damageeffect": "AirDestructionEffects",
    "type": 2,
    "transportmaxbackpacks": 1,
    "supplyradius": 1.2,
    "dammagehalf": [],
    "dammagefull": [],
    "crewvulnerable": 1,
    "explosionshielding": 4,
    "mintotaldamagethreshold": 0.005,
    # Class: CfgVehicles|Helicopter|DestructionEffects [Indent level: 1],
    "destructioneffects": {
    },
    # Class: CfgVehicles|Helicopter|AnimationSources [Indent level: 1],
    "animationsources": {
        # Class: CfgVehicles|Helicopter|AnimationSources|HitGlass1 [Indent level: 2]
        "hitglass1": {
            "source": "Hit",
            "hitpoint": "HitGlass1",
            "raw": 1
        },
        # Class: CfgVehicles|Helicopter|AnimationSources|HitGlass2 [Indent level: 2],
        "hitglass2": {
            "hitpoint": "HitGlass2",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|Helicopter|AnimationSources|HitGlass3 [Indent level: 2],
        "hitglass3": {
            "hitpoint": "HitGlass3",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|Helicopter|AnimationSources|HitGlass4 [Indent level: 2],
        "hitglass4": {
            "hitpoint": "HitGlass4",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|Helicopter|AnimationSources|HitGlass5 [Indent level: 2],
        "hitglass5": {
            "hitpoint": "HitGlass5",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|Helicopter|AnimationSources|HitGlass6 [Indent level: 2],
        "hitglass6": {
            "hitpoint": "HitGlass6",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|Helicopter|AnimationSources|HitEngine1 [Indent level: 2],
        "hitengine1": {
            "source": "hit",
            "hitpoint": "HitEngine1",
            "raw": 1
        },
        # Class: CfgVehicles|Helicopter|AnimationSources|HitEngine2 [Indent level: 2],
        "hitengine2": {
            "source": "hit",
            "hitpoint": "HitEngine2",
            "raw": 1
        },
        # Class: CfgVehicles|Helicopter|AnimationSources|HitWinch_Source [Indent level: 2],
        "hitwinch_source": {
            "source": "hit",
            "hitpoint": "HitWinch",
            "raw": 1
        },
        # Class: CfgVehicles|Air|AnimationSources|CollisionLightRed_source [Indent level: 2],
        "collisionlightred_source": {
            "source": "MarkerLight",
            "markerlight": "CollisionRed"
        },
        # Class: CfgVehicles|Air|AnimationSources|CollisionLightWhite_source [Indent level: 2],
        "collisionlightwhite_source": {
            "source": "MarkerLight",
            "markerlight": "CollisionWhite"
        }
    },
    "lockdetectionsystem": 8,
    "incomingmissiledetectionsystem": 16,
    "mainbladecenter": "rotor_center",
    "tailbladecenter": "rotor_02_center",
    "tailbladeradius": 0.5,
    "tailbladevertical": 1,
    "slingloadmincargomass": 0,
    "formationx": 50,
    "formationz": 100,
    "precision": 100,
    "brakedistance": 200,
    "formationtime": 10,
    "gearsupfrictioncoef": 0.5,
    "airbrakefrictioncoef": 3,
    "airfrictioncoefs2": [0.001,0.0005,6e-005],
    "airfrictioncoefs1": [0.1,0.05,0.006],
    "airfrictioncoefs0": [0,0,0],
    # Class: CfgVehicles|Air|Components [Indent level: 1],
    "components": {
        # Class: CfgVehicles|Air|Components|TransportCountermeasuresComponent [Indent level: 2]
        "transportcountermeasurescomponent": {
        }
    },
    "altfullforce": 2000,
    "altnoforce": 6000,
    "cost": 1e+007,
    "fuelcapacity": 1000,
    "attenuationeffecttype": "",
    "insidesoundcoef": 0.0316228,
    "outsidesoundfilter": 1,
    "occludesoundswhenin": 0.316228,
    "obstructsoundswhenin": 0.316228,
    "irscanrangemin": 2000,
    "irscanrangemax": 10000,
    "irscantoeyefactor": 2,
    "nightvision": 0,
    "threat": [0.3,1,0.7],
    "driveraction": "",
    "drivercompartments": 0,
    "cargocompartments": [0],
    "typicalcargo": ["Soldier"],
    "getinradius": 5,
    "transportmaxmagazines": 20,
    "transportmaxweapons": 3,
    "enablegps": 1,
    # Class: CfgVehicles|Air|MarkerLights [Indent level: 1],
    "markerlights": {
        # Class: CfgVehicles|Air|MarkerLights|RedStill [Indent level: 2]
        "redstill": {
            "name": "cerveny pozicni",
            "color": [0.3,0.03,0.03,1],
            "ambient": [0.03,0.003,0.003,1],
            "brightness": 0.01,
            "blinking": 0
        },
        # Class: CfgVehicles|Air|MarkerLights|GreenStill [Indent level: 2],
        "greenstill": {
            "name": "zeleny pozicni",
            "color": [0.03,0.3,0.03,1],
            "ambient": [0.003,0.03,0.003,1],
            "brightness": 0.01,
            "blinking": 0
        },
        # Class: CfgVehicles|Air|MarkerLights|WhiteStill [Indent level: 2],
        "whitestill": {
            "name": "bily pozicni",
            "color": [0.3,0.3,0.3,1],
            "ambient": [0.03,0.03,0.03,1],
            "brightness": 0.01,
            "blinking": 0
        },
        # Class: CfgVehicles|Air|MarkerLights|WhiteBlinking [Indent level: 2],
        "whiteblinking": {
            "name": "bily pozicni blik",
            "color": [1,1,1,1],
            "ambient": [0.1,0.1,0.1,1],
            "brightness": 0.01,
            "blinking": 1
        },
        # Class: CfgVehicles|Air|MarkerLights|RedBlinking [Indent level: 2],
        "redblinking": {
            "name": "cerveny pozicni blik",
            "color": [0.5,0.05,0.05,1],
            "ambient": [0.05,0.005,0.005,1],
            "brightness": 0.01,
            "blinking": 1
        },
        # Class: CfgVehicles|Air|MarkerLights|PositionRed [Indent level: 2],
        "positionred": {
            "color": [0.8,0,0],
            "ambient": [0.08,0,0],
            "intensity": 75,
            "name": "PositionLight_red_1_pos",
            "drawlight": 1,
            "drawlightsize": 0.15,
            "drawlightcentersize": 0.04,
            "activelight": 0,
            "blinking": 0,
            "daylight": 0,
            "useflare": 0,
            # Class: CfgVehicles|Air|MarkerLights|PositionRed|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardlimitstart": 0.75,
                "hardlimitend": 1
            }
        },
        # Class: CfgVehicles|Air|MarkerLights|PositionGreen [Indent level: 2],
        "positiongreen": {
            "color": [0,0.8,0],
            "ambient": [0,0.08,0],
            "name": "PositionLight_green_1_pos",
            "intensity": 75,
            "drawlight": 1,
            "drawlightsize": 0.15,
            "drawlightcentersize": 0.04,
            "activelight": 0,
            "blinking": 0,
            "daylight": 0,
            "useflare": 0,
            # Class: CfgVehicles|Air|MarkerLights|PositionRed|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardlimitstart": 0.75,
                "hardlimitend": 1
            }
        },
        # Class: CfgVehicles|Air|MarkerLights|PositionWhite [Indent level: 2],
        "positionwhite": {
            "color": [1,1,1],
            "ambient": [0.1,0.1,0.1],
            "name": "PositionLight_white_1_pos",
            "drawlightsize": 0.2,
            "intensity": 75,
            "drawlight": 1,
            "drawlightcentersize": 0.04,
            "activelight": 0,
            "blinking": 0,
            "daylight": 0,
            "useflare": 0,
            # Class: CfgVehicles|Air|MarkerLights|PositionRed|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardlimitstart": 0.75,
                "hardlimitend": 1
            }
        },
        # Class: CfgVehicles|Air|MarkerLights|CollisionRed [Indent level: 2],
        "collisionred": {
            "color": [0.9,0.15,0.1],
            "ambient": [0.09,0.015,0.01],
            "name": "CollisionLight_red_1_pos",
            "blinking": 1,
            "blinkingpattern": [0.2,1.3],
            "blinkingpatternguarantee": 0,
            "drawlightsize": 0.25,
            "drawlightcentersize": 0.08,
            "intensity": 75,
            "drawlight": 1,
            "activelight": 0,
            "daylight": 0,
            "useflare": 0,
            # Class: CfgVehicles|Air|MarkerLights|PositionRed|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardlimitstart": 0.75,
                "hardlimitend": 1
            }
        },
        # Class: CfgVehicles|Air|MarkerLights|CollisionWhite [Indent level: 2],
        "collisionwhite": {
            "color": [1,1,1],
            "ambient": [0.1,0.1,0.1],
            "name": "CollisionLight_white_1_pos",
            "blinking": 1,
            "blinkingpattern": [0.1,0.9],
            "blinkingpatternguarantee": 0,
            "drawlightsize": 0.2,
            "drawlightcentersize": 0.04,
            "intensity": 75,
            "drawlight": 1,
            "activelight": 0,
            "daylight": 0,
            "useflare": 0,
            # Class: CfgVehicles|Air|MarkerLights|PositionRed|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardlimitstart": 0.75,
                "hardlimitend": 1
            }
        }
    },
    "weaponsgroup1": "1 + 		2",
    "weaponsgroup2": 4,
    "weaponsgroup3": "8 + 	16 + 	32",
    "weaponsgroup4": "64 + 		128",
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
    "mapsize": 10.56,
    "waterleakiness": 100,
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
    "countermeasureactivationradius": 10000,
    # Class: CfgVehicles|Air|TransportItems [Indent level: 1],
    "transportitems": {
        # Class: CfgVehicles|Air|TransportItems|_xx_FirstAidKit [Indent level: 2]
        "_xx_firstaidkit": {
            "name": "FirstAidKit",
            "count": 4
        }
    },
    # Class: CfgVehicles|Air|camShakeGForce [Indent level: 1],
    "camshakegforce": {
        "power": 0.2,
        "frequency": 3,
        "distance": 0,
        "minspeed": 1
    },
    # Class: CfgVehicles|Air|camShakeDamage [Indent level: 1],
    "camshakedamage": {
        "power": 0.5,
        "frequency": 60,
        "distance": -1,
        "minspeed": 1,
        "attenuation": 0.5,
        "duration": 3
    },
    "mingforce": 0.2,
    "maxgforce": 2,
    "gforceshakeattenuation": 0.5,
    # Class: CfgVehicles|AllVehicles|SquadTitles [Indent level: 1],
    "squadtitles": {
        "name": "clan_sign",
        "color": [0,0,0,0.75]
    },
    "memorypointdriveroptics": ["driverview","pilot"],
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
    "scope": 0,
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
    "picture": "",
    "portrait": "",
    "ghostpreview": "",
    "armorlights": 0.4,
    "damageresistance": 0.004,
    "replacedamaged": "",
    "replacedamagedlimit": 0.9,
    "replacedamagedhitpoints": [],
    "keepinepesceneafterdeath": 0,
    "fuelconsumptionrate": 0.01,
    "extcameraposition": [0,2,-20],
    "groupcameraposition": [0,5,-30],
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
    "hideunitinfo": 0,
    "limitedspeedcoef": 0.22,
    "driverforceoptics": 0,
    "hideweaponsdriver": 1,
    "hideweaponscargo": 0,
    "memorypointsupply": "doplnovani",
    "enablewatch": 0,
    "useprecisegetinaction": 0,
    "allowtablock": 1,
    "showalltargets": 0,
    "dustfrontleftpos": "dustFrontLeft",
    "dustfrontrightpos": "dustFrontRight",
    "dustbackleftpos": "dustBackLeft",
    "dustbackrightpos": "dustBackRight",
    "wheelcircumference": 1,
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
    "transportsoldier": 0,
    "transportammo": 0,
    "isbackpack": 0,
    "transportfuel": 0,
    "transportrepair": 0,
    "transportvehiclescount": 0,
    "transportvehiclesmass": 0,
    # Class: CfgVehicles|All|TransportWeapons [Indent level: 1],
    "transportweapons": {
    },
    # Class: CfgVehicles|All|TransportMagazines [Indent level: 1],
    "transportmagazines": {
    },
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
    "soundgetin": ["",0.000316228,1],
    "soundgetout": ["",0.000316228,1],
    "soundservo": ["",0.00316228,0.5],
    "soundelevation": ["",0.00316228,0.5],
    "sounddamage": ["",1,1],
    "soundengineonint": ["",1,1],
    "soundengineoffint": ["",1,1],
    "soundengineonext": ["",1,1],
    "soundengineoffext": ["",1,1],
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
    "soundlocked": ["",1,1],
    "soundincommingmissile": ["",1,1],
    "sounddammage": ["",1,1],
    "aggregatereflectors": [],
    "driverinaction": "",
    "cargoaction": [],
    "cargoiscodriver": [0],
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
    "hiddenselections": [],
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
    # Class: CfgVehicles|All|Damage [Indent level: 1],
    "damage": {
        "tex": [],
        "mat": []
    },
    "selectiondamage": "zbytek",
    "headaimdown": 0,
    "cargocaneject": 1,
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
    "numberphysicalwheels": 0,
    "damagehalf": [],
    "damagefull": [],
    "soundturnin": ["",0.000316228,1],
    "soundturnout": ["",0.000316228,1],
    "soundturnininternal": ["",0.000316228,1],
    "soundturnoutinternal": ["",0.000316228,1],
    "features": "",
    "model": "A3|Weapons_F|empty.p3d",
    "insidedetectcoef": 0.05,
}