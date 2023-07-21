d = {
    "_generalmacro": "Plane_Base_F",
    "access": 0,
    "accuracy": 0.5,
    "accuracydarknightlightsoff": 0.001,
    "accuracynightlightsoff": 0.006,
    "accuracynightlightson": 0.1,
    "afmax": 200,
    "aggregatereflectors": [],
    "aileroncoef": [],
    "aileroncontrolssensitivitycoef": 4,
    "aileronsensitivity": 0.4,
    "airbrake": 0,
    "airbrakefrictioncoef": 3,
    "aircapacity": 10,
    "airfrictioncoefs0": [
        0,
        0,
        0
    ],
    "airfrictioncoefs1": [
        0.1,
        0.05,
        0.006
    ],
    "airfrictioncoefs2": [
        0.001,
        0.0005,
        6e-05
    ],
    "allowtablock": 1,
    "altfullforce": 2000,
    "altnoforce": 6000,
    "alwaystarget": 0,
    "angleofindicence": 0,
    "animated": 1,
    "animationsources": {
        "door": {
            "animperiod": 2.5,
            "sound": "ServoRampSound_2",
            "source": "user"
        },
        "hidedoor": {
            "animperiod": 1e-06,
            "author": "Community Upgrade Project",
            "displayname": "Hide Door...",
            "forceanimate": [],
            "forceanimatephase": 0,
            "initphase": 0,
            "mass": 20,
            "source": "user"
        },
        "hitglass1": {
            "hitpoint": "HitGlass1",
            "raw": 1,
            "source": "Hit"
        },
        "hitglass2": {
            "hitpoint": "HitGlass2",
            "raw": 1,
            "source": "Hit"
        },
        "hitglass3": {
            "hitpoint": "HitGlass3",
            "raw": 1,
            "source": "Hit"
        },
        "hitglass4": {
            "hitpoint": "HitGlass4",
            "raw": 1,
            "source": "Hit"
        }
    },
    "antirollbarforcecoef": 0,
    "antirollbarforcelimit": 5,
    "antirollbarspeedmax": 60,
    "antirollbarspeedmin": 20,
    "armor": 25,
    "armorlights": 0.4,
    "armorstructural": 1,
    "artilleryscanner": 0,
    "artillerytarget": 0,
    "attendant": 0,
    "attenuationeffecttype": "HeliAttenuation",
    "attributes": {
        "door": {
            "control": "slider",
            "defaultvalue": "0",
            "displayname": "Open Door",
            "expression": "_this animate ['door',_value];",
            "property": "door"
        },
        "objecttexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayname": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        "rhs_decalnumber": {
            "control": "Edit",
            "defaultvalue": "-1",
            "displayname": "Set side number",
            "expression": "if( _value >= 0)then{if(_value == 0)then{{[_this setobjectTexture [_x,'a3/data_f/clear_empty.paa']]}foreach [3,4]}else{[_this, [['Number', [3,4], _this getVariable ['rhs_decalNumber_type','AviaCDF'], _value] ] ] call rhs_fnc_decalsInit}};",
            "property": "rhs_decalNumber",
            "tooltip": "Set side number. 2 numbers are required. Type 0 to hide numbers completly",
            "typename": "Number",
            "validate": "Number"
        },
        "rhs_decalnumber_type": {
            "control": "Combo",
            "defaultvalue": 0,
            "displayname": "Define font type of side number",
            "expression": "if(_value != 'NoChange')then{ _this setVariable ['%s', _value];[_this,[['Number', [3,4], _value]]] call rhs_fnc_decalsInit}",
            "property": "rhs_decalNumber_type",
            "tooltip": "Define kind of font that will be drawn on vehicle",
            "typename": "STRING",
            "values": {
                "aviablue": {
                    "name": "Aviation Blue",
                    "value": "AviaBlue"
                },
                "aviacdf": {
                    "defaultvalue": "AviaCDF",
                    "name": "Aviation CDF",
                    "value": "AviaCDF"
                },
                "aviared": {
                    "name": "Aviation Red",
                    "value": "AviaRed"
                },
                "aviawhiteout": {
                    "name": "Aviation White Out",
                    "value": "AviaWhiteOut"
                },
                "aviayellow": {
                    "name": "Aviation Yellow",
                    "value": "AviaYellow"
                },
                "boldred": {
                    "name": "Bold Red",
                    "value": "BoldRed"
                },
                "cdf": {
                    "name": "CDF",
                    "value": "CDF"
                },
                "default": {
                    "name": "Default (White)",
                    "value": "Default"
                },
                "defaultred": {
                    "name": "Default (Red)",
                    "value": "DefaultRed"
                },
                "handpaint": {
                    "name": "Handpaint",
                    "value": "Handpaint"
                },
                "handpaintblack": {
                    "name": "Handpaint Black",
                    "value": "HandpaintBlack"
                },
                "iraqi": {
                    "name": "Iraqi",
                    "value": "Iraqi"
                },
                "nochange": {
                    "name": "Default",
                    "value": "NoChange"
                }
            }
        },
        "rhs_decaltail": {
            "control": "Combo",
            "defaultvalue": -1,
            "displayname": "Define tail decal",
            "expression": "[_this,[['Label', [5], 'Aviation',_value]]] call rhs_fnc_decalsInit",
            "property": "rhs_decalTail",
            "tooltip": "Define tail decal that will be drawn on vehicle",
            "typename": "Number",
            "values": {
                "cdf": {
                    "defaultvalue": 4,
                    "name": "CDF",
                    "value": 4
                },
                "default": {
                    "name": "Default",
                    "value": -1
                },
                "empty": {
                    "name": "Empty",
                    "value": 0
                },
                "star": {
                    "name": "Red Star",
                    "value": 2
                }
            }
        }
    },
    "audible": 60,
    "author": "Red Hammer Studios",
    "autocenter": 1,
    "availableforsupporttypes": [],
    "brakedistance": 500,
    "cabinclosesound": [
        "",
        1,
        1
    ],
    "cabinclosesoundinternal": [
        "",
        1,
        1
    ],
    "cabinopening": 0,
    "cabinopensound": [
        "",
        1,
        1
    ],
    "cabinopensoundinternal": [
        "",
        1,
        1
    ],
    "camerasmoothspeed": 5,
    "camouflage": 100,
    "camshake": {
        "distance": 50,
        "frequency": 20,
        "minspeed": 200,
        "power": 50
    },
    "camshakecoef": 0,
    "camshakedamage": {
        "attenuation": 0.5,
        "distance": -1,
        "duration": 3,
        "frequency": 60,
        "minspeed": 1,
        "power": 0.5
    },
    "camshakegforce": {
        "distance": 0,
        "frequency": 20,
        "minspeed": 1,
        "power": 1
    },
    "canhidedriver": -1,
    "canusescanners": 1,
    "cargoaction": [
        "RHS_AN2_Cargo01",
        "RHS_AN2_Cargo02",
        "RHS_AN2_Cargo01",
        "RHS_AN2_Cargo03",
        "RHS_AN2_Cargo02",
        "RHS_AN2_Cargo01",
        "RHS_AN2_Cargo03",
        "RHS_AN2_Cargo01",
        "RHS_AN2_Cargo03",
        "RHS_AN2_Cargo02",
        "RHS_AN2_Cargo01",
        "RHS_AN2_Cargo02",
        "RHS_AN2_Cargo02",
        "RHS_AN2_Cargo03"
    ],
    "cargocaneject": 1,
    "cargocompartments": [
        "Compartment1"
    ],
    "cargodoors": [],
    "cargogetinaction": [
        "GetInHigh"
    ],
    "cargogetoutaction": [
        "GetOutHigh"
    ],
    "cargoiscodriver": [
        1,
        0
    ],
    "cargoprecisegetinout": [
        0
    ],
    "cargoproxyindexes": [],
    "cargospec": {
        "cargo1": {
            "showheadphones": 0
        }
    },
    "cargoturret": {
        "aggregatereflectors": [],
        "allowlauncherin": 0,
        "allowlauncherout": 0,
        "allowtablock": 1,
        "animationsourcebody": "",
        "animationsourcecamelev": "camElev",
        "animationsourcegun": "",
        "animationsourcehatch": "hatchGunner",
        "armorlights": 0.4,
        "body": "",
        "caneject": 1,
        "canhidegunner": -1,
        "canusescanners": 1,
        "castgunnershadow": 0,
        "commanding": 0,
        "disablesoundattenuation": 1,
        "dontcreateai": 1,
        "ejectdeadgunner": 0,
        "forcehidegunner": 0,
        "forcenvg": 0,
        "gun": "",
        "gunbeg": "usti hlavne",
        "gunclouds": {
            "access": 0,
            "cloudletaccy": 0.4,
            "cloudletalpha": 1,
            "cloudletanimperiod": 1,
            "cloudletcolor": [
                1,
                1,
                1,
                0
            ],
            "cloudletduration": 0.3,
            "cloudletfadein": 0.01,
            "cloudletfadeout": 1,
            "cloudletgrowup": 1,
            "cloudletmaxyspeed": 0.8,
            "cloudletminyspeed": 0.2,
            "cloudletshape": "cloudletClouds",
            "cloudletsize": 1,
            "deltat": 0,
            "initt": 0,
            "interval": 0.05,
            "size": 3,
            "sourcesize": 0.5,
            "table": {
                "t0": {
                    "color": [
                        1,
                        1,
                        1,
                        0
                    ],
                    "maxt": 0
                }
            },
            "timetolive": 0
        },
        "gunend": "konec hlavne",
        "gunfire": {
            "access": 0,
            "cloudletaccy": 0,
            "cloudletalpha": 1,
            "cloudletanimperiod": 1,
            "cloudletcolor": [
                1,
                1,
                1,
                0
            ],
            "cloudletduration": 0.2,
            "cloudletfadein": 0.01,
            "cloudletfadeout": 0.5,
            "cloudletgrowup": 0.2,
            "cloudletmaxyspeed": 100,
            "cloudletminyspeed": -100,
            "cloudletshape": "cloudletFire",
            "cloudletsize": 1,
            "deltat": -3000,
            "initt": 4500,
            "interval": 0.01,
            "size": 3,
            "sourcesize": 0.5,
            "table": {
                "t0": {
                    "color": [
                        0.82,
                        0.95,
                        0.93,
                        0
                    ],
                    "maxt": 0
                },
                "t1": {
                    "color": [
                        0.75,
                        0.77,
                        0.9,
                        0
                    ],
                    "maxt": 200
                },
                "t10": {
                    "color": [
                        0.62,
                        0.29,
                        0.03,
                        0
                    ],
                    "maxt": 2600
                },
                "t11": {
                    "color": [
                        0.59,
                        0.35,
                        0.05,
                        0
                    ],
                    "maxt": 2650
                },
                "t12": {
                    "color": [
                        0.75,
                        0.37,
                        0.03,
                        0
                    ],
                    "maxt": 2700
                },
                "t13": {
                    "color": [
                        0.88,
                        0.34,
                        0.03,
                        0
                    ],
                    "maxt": 2750
                },
                "t14": {
                    "color": [
                        0.91,
                        0.5,
                        0.17,
                        0
                    ],
                    "maxt": 2800
                },
                "t15": {
                    "color": [
                        1,
                        0.6,
                        0.2,
                        0
                    ],
                    "maxt": 2850
                },
                "t16": {
                    "color": [
                        1,
                        0.71,
                        0.3,
                        0
                    ],
                    "maxt": 2900
                },
                "t17": {
                    "color": [
                        0.98,
                        0.83,
                        0.41,
                        0
                    ],
                    "maxt": 2950
                },
                "t18": {
                    "color": [
                        0.98,
                        0.91,
                        0.54,
                        0
                    ],
                    "maxt": 3000
                },
                "t19": {
                    "color": [
                        0.98,
                        0.99,
                        0.6,
                        0
                    ],
                    "maxt": 3100
                },
                "t2": {
                    "color": [
                        0.56,
                        0.62,
                        0.67,
                        0
                    ],
                    "maxt": 400
                },
                "t20": {
                    "color": [
                        0.96,
                        0.99,
                        0.72,
                        0
                    ],
                    "maxt": 3300
                },
                "t21": {
                    "color": [
                        1,
                        0.98,
                        0.91,
                        0
                    ],
                    "maxt": 3600
                },
                "t22": {
                    "color": [
                        1,
                        1,
                        1,
                        0
                    ],
                    "maxt": 4200
                },
                "t3": {
                    "color": [
                        0.39,
                        0.46,
                        0.47,
                        0
                    ],
                    "maxt": 600
                },
                "t4": {
                    "color": [
                        0.24,
                        0.31,
                        0.31,
                        0
                    ],
                    "maxt": 800
                },
                "t5": {
                    "color": [
                        0.23,
                        0.31,
                        0.29,
                        0
                    ],
                    "maxt": 1000
                },
                "t6": {
                    "color": [
                        0.21,
                        0.29,
                        0.27,
                        0
                    ],
                    "maxt": 1500
                },
                "t7": {
                    "color": [
                        0.19,
                        0.23,
                        0.21,
                        0
                    ],
                    "maxt": 2000
                },
                "t8": {
                    "color": [
                        0.22,
                        0.19,
                        0.1,
                        0
                    ],
                    "maxt": 2300
                },
                "t9": {
                    "color": [
                        0.35,
                        0.2,
                        0.02,
                        0
                    ],
                    "maxt": 2500
                }
            },
            "timetolive": 0
        },
        "gunneraction": "ManActTestDriver",
        "gunnercompartments": "Compartment1",
        "gunnerdoor": "",
        "gunnerfirealsoininternalcamera": 1,
        "gunnerforceoptics": 1,
        "gunnergetinaction": "GetInLow",
        "gunnergetoutaction": "GetOutLow",
        "gunnerinaction": "ManActTestDriver",
        "gunnerlefthandanimname": "",
        "gunnerleftleganimname": "",
        "gunnername": "cargo",
        "gunneropticscolor": [
            0,
            0,
            0,
            1
        ],
        "gunneropticseffect": [],
        "gunneropticsmodel": "",
        "gunneropticsshowcursor": 0,
        "gunneroutfirealsoininternalcamera": 1,
        "gunneroutforceoptics": 0,
        "gunneroutopticscolor": [
            0,
            0,
            0,
            1
        ],
        "gunneroutopticseffect": [],
        "gunneroutopticsmodel": "",
        "gunneroutopticsshowcursor": 0,
        "gunnerrighthandanimname": "",
        "gunnerrightleganimname": "",
        "gunnertype": "",
        "gunnerusespilotview": 0,
        "hasgunner": 1,
        "hideweaponsgunner": 0,
        "hitpoints": {},
        "ingunnermayfire": 1,
        "initcamelev": 0,
        "initelev": 0,
        "initoutelev": 0,
        "initoutturn": 0,
        "initturn": 0,
        "iscopilot": 0,
        "ispersonturret": 1,
        "lockwhendriverout": 0,
        "lockwhenvehiclespeed": -1,
        "lodturnedin": -1,
        "lodturnedout": -1,
        "magazines": [],
        "maxcamelev": 90,
        "maxelev": 45,
        "maxhorizontalrotspeed": 1.2,
        "maxoutelev": 20,
        "maxoutturn": 60,
        "maxturn": 95,
        "maxverticalrotspeed": 1.2,
        "memorypointgun": "kulas",
        "memorypointgunneroptics": "gunnerview",
        "memorypointgunneroutoptics": "",
        "memorypointsgetingunner": "pos cargo",
        "memorypointsgetingunnerdir": "pos cargo dir",
        "memorypointsgetingunnerprecise": "",
        "mgunclouds": {
            "access": 0,
            "cloudletaccy": 0,
            "cloudletalpha": 0.3,
            "cloudletanimperiod": 1,
            "cloudletcolor": [
                1,
                1,
                1,
                0
            ],
            "cloudletduration": 0.05,
            "cloudletfadein": 0,
            "cloudletfadeout": 0.1,
            "cloudletgrowup": 0.05,
            "cloudletmaxyspeed": 100,
            "cloudletminyspeed": -100,
            "cloudletshape": "cloudletClouds",
            "cloudletsize": 1,
            "deltat": 0,
            "initt": 0,
            "interval": 0.02,
            "size": 0.3,
            "sourcesize": 0.02,
            "table": {
                "t0": {
                    "color": [
                        1,
                        1,
                        1,
                        0
                    ],
                    "maxt": 0
                }
            },
            "timetolive": 0
        },
        "mincamelev": -90,
        "minelev": -45,
        "minoutelev": -4,
        "minoutturn": -60,
        "minturn": -95,
        "missilebeg": "spice rakety",
        "missileend": "konec rakety",
        "outgunnermayfire": 1,
        "playerposition": 0,
        "precisegetinout": 0,
        "primary": 1,
        "primarygunner": 0,
        "primaryobserver": 0,
        "proxyindex": 1,
        "proxytype": "CPCargo",
        "reflectors": {},
        "selectionfireanim": "zasleh",
        "showalltargets": 0,
        "showascargo": 1,
        "showcrewaim": 0,
        "showhmd": 0,
        "slingloadoperator": 0,
        "soundelevation": [
            "",
            0.00316228,
            1
        ],
        "soundservo": [
            "",
            0.00316228,
            1
        ],
        "stabilizedinaxes": 3,
        "startengine": 0,
        "turnin": {
            "turnoffset": 0
        },
        "turnout": {
            "turnoffset": 0
        },
        "turretcansee": 0,
        "turretfollowfreelook": 0,
        "turretinfotype": "",
        "turrets": {},
        "turretspec": {
            "showheadphones": 0
        },
        "viewgunner": {
            "initanglex": 5,
            "initangley": 0,
            "initfov": 0.75,
            "maxanglex": 85,
            "maxangley": 150,
            "maxfov": 1.25,
            "maxmovex": 0,
            "maxmovey": 0,
            "maxmovez": 0,
            "minanglex": -75,
            "minangley": -150,
            "minfov": 0.25,
            "minmovex": 0,
            "minmovey": 0,
            "minmovez": 0,
            "speedzoommaxfov": 0,
            "speedzoommaxspeed": 10000000000.0
        },
        "viewgunnerinexternal": 1,
        "viewgunnershadow": 1,
        "viewgunnershadowamb": 1,
        "viewgunnershadowdiff": 1,
        "viewoptics": {
            "initanglex": 0,
            "initangley": 0,
            "initfov": 0.3,
            "maxanglex": 30,
            "maxangley": 100,
            "maxfov": 0.35,
            "maxmovex": 0,
            "maxmovey": 0,
            "maxmovez": 0,
            "minanglex": -30,
            "minangley": -100,
            "minfov": 0.07,
            "minmovex": 0,
            "minmovey": 0,
            "minmovez": 0,
            "speedzoommaxfov": 0,
            "speedzoommaxspeed": 10000000000.0
        },
        "weapons": []
    },
    "castcargoshadow": 0,
    "castdrivershadow": 0,
    "coefinside": 2,
    "coefinsideheur": 2,
    "coefspeedinside": 2,
    "commandercansee": "1 + 2 + 4 + 8 + 32",
    "components": {
        "vehiclesystemsdisplaymanagercomponentleft": {
            "components": {
                "crewdisplay": {
                    "componenttype": "CrewDisplayComponent",
                    "resource": "RscCustomInfoCrew"
                },
                "emptydisplay": {
                    "componenttype": "EmptyDisplayComponent"
                },
                "minedetectordisplay": {
                    "componenttype": "MineDetectorDisplayComponent"
                },
                "minimapdisplay": {
                    "componenttype": "MinimapDisplayComponent"
                },
                "slingloaddisplay": {
                    "componenttype": "SlingLoadDisplayComponent"
                },
                "uavdisplay": {
                    "componenttype": "UAVFeedDisplayComponent"
                }
            },
            "componenttype": "VehicleSystemsDisplayManager",
            "defaultdisplay": "EmptyDisplay",
            "left": 1,
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,\t(safezoneX + 0.5 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,\t(safezoneY + safezoneH - 21 * \t\t\t(\t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
        },
        "vehiclesystemsdisplaymanagercomponentright": {
            "components": {
                "crewdisplay": {
                    "componenttype": "CrewDisplayComponent",
                    "resource": "RscCustomInfoCrew"
                },
                "emptydisplay": {
                    "componenttype": "EmptyDisplayComponent"
                },
                "minedetectordisplay": {
                    "componenttype": "MineDetectorDisplayComponent"
                },
                "minimapdisplay": {
                    "componenttype": "MinimapDisplayComponent"
                },
                "slingloaddisplay": {
                    "componenttype": "SlingLoadDisplayComponent"
                },
                "uavdisplay": {
                    "componenttype": "UAVFeedDisplayComponent"
                }
            },
            "componenttype": "VehicleSystemsDisplayManager",
            "defaultdisplay": "",
            "right": 1,
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,\t((safezoneX + safezoneW) - (\t\t(10 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40)))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,\t(safezoneY + safezoneH - 21 * \t\t\t(\t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
        }
    },
    "cost": 20000,
    "countermeasureactivationradius": 10000,
    "countsforscoreboard": 1,
    "crew": "rhsgref_cdf_b_air_pilot",
    "crewcrashprotection": 0.15,
    "crewvulnerable": 1,
    "curatorinfotype": "RscDisplayAttributesVehicle",
    "curatorinfotypeempty": "RscDisplayAttributesVehicleEmpty",
    "damage": {
        "mat": [
            "rhsgref/addons/rhsgref_air/AN2/Data/an2_1.rvmat",
            "rhsgref/addons/rhsgref_air/AN2/Data/an2_1_damage.rvmat",
            "rhsgref/addons/rhsgref_air/AN2/Data/an2_1_destruct.rvmat",
            "rhsgref/addons/rhsgref_air/AN2/Data/an2_2.rvmat",
            "rhsgref/addons/rhsgref_air/AN2/Data/an2_2_damage.rvmat",
            "rhsgref/addons/rhsgref_air/AN2/Data/an2_2_destruct.rvmat",
            "rhsgref/addons/rhsgref_air/AN2/Data/an2_interier.rvmat",
            "rhsgref/addons/rhsgref_air/AN2/Data/an2_interier_damage.rvmat",
            "rhsgref/addons/rhsgref_air/AN2/Data/an2_interier_destruct.rvmat",
            "rhsgref/addons/rhsgref_air/AN2/Data/an2_cockpit.rvmat",
            "rhsgref/addons/rhsgref_air/AN2/Data/an2_cockpit_damage.rvmat",
            "rhsgref/addons/rhsgref_air/AN2/Data/an2_cockpit_destruct.rvmat",
            "rhsgref/addons/rhsgref_air/AN2/Data/an2_wings.rvmat",
            "rhsgref/addons/rhsgref_air/AN2/Data/an2_wings_damage.rvmat",
            "rhsgref/addons/rhsgref_air/AN2/Data/an2_wings_destruct.rvmat",
            "rhsgref/addons/rhsgref_air/AN2/Data/an2_window.rvmat",
            "rhsgref/addons/rhsgref_air/AN2/Data/an2_window_damage.rvmat",
            "rhsgref/addons/rhsgref_air/AN2/Data/an2_window_destruct.rvmat",
            "a3/data_f/default.rvmat",
            "a3/data_f/default.rvmat",
            "a3/data_f/default_destruct.rvmat"
        ],
        "tex": []
    },
    "damageeffect": "AirDestructionEffects",
    "damagefull": [],
    "damagehalf": [],
    "damageresistance": 0.00278,
    "damagetexdelay": 0,
    "destrtype": "DestructWreck",
    "destructioneffects": {},
    "detectskill": 20,
    "displayname": "Antonov An-2",
    "dlc": "RHS_GREF",
    "draconicforcexcoef": 3.15,
    "draconicforceycoef": 0.5,
    "draconicforcezcoef": 0.5,
    "draconictorquexcoef": 0.15,
    "draconictorqueycoef": 3.15,
    "driveoncomponent": [],
    "driveraction": "RHS_AN2_Pilot",
    "drivercaneject": 1,
    "drivercansee": "1 + 2 + 4 + 8 + 32",
    "drivercompartments": "Compartment1",
    "driverdoor": "",
    "driverforceoptics": 0,
    "driverinaction": "",
    "driverlefthandanimname": "left_stick_aileron",
    "driverleftleganimname": "pedal_l",
    "driveropticscolor": [
        1,
        1,
        1,
        1
    ],
    "driveropticseffect": [],
    "driveropticsmodel": "",
    "driverrighthandanimname": "left_stick_aileron",
    "driverrightleganimname": "pedal_r",
    "durationgetin": 0.99,
    "durationgetout": 0.99,
    "dustbackleftpos": "dustBackLeft",
    "dustbackrightpos": "dustBackRight",
    "dusteffect": "HeliDust",
    "dusteffects": {
        "both": {},
        "left": {
            "default": [
                "LDustEffectsAir"
            ],
            "gdtasphalt": [
                "LDustEffectsAir",
                "LDirtEffects"
            ],
            "gdtbeach": [
                "LDustEffectsAir",
                "LStonesEffects"
            ],
            "gdtcliff": [
                "LDustEffectsAir"
            ],
            "gdtconcrete": [
                "LDustEffectsAir",
                "LDirtEffects"
            ],
            "gdtdead": [
                "LDustEffectsAir",
                "LDirtEffects"
            ],
            "gdtdesert1": [
                "LDustEffectsAir",
                "LSandEffects",
                "LDirtEffects",
                "LStonesEffects"
            ],
            "gdtdesert2": [
                "LDustEffectsAir",
                "LSandEffects",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtdirt": [
                "LDustEffectsAir",
                "LDirtEffects"
            ],
            "gdtfield": [
                "LDustEffectsAir"
            ],
            "gdtforest": [
                "LDustEffectsAir"
            ],
            "gdtgrassdry": [
                "LDustEffectsAir",
                "LGrassDryEffects",
                "LDirtEffects"
            ],
            "gdtgrassgreen": [
                "LDustEffectsAir",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtgrassshort": [
                "LDustEffectsAir",
                "LGrassEffects"
            ],
            "gdtgrasstall": [
                "LDustEffectsAir",
                "LGrassEffects"
            ],
            "gdtgrasswild": [
                "LDustEffectsAir",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtkldirt": [
                "LDustEffectsAir"
            ],
            "gdtklforestcon": [
                "LDustEffectsAir"
            ],
            "gdtklforestdec": [
                "LDustEffectsAir"
            ],
            "gdtklgrass1": [
                "LDustEffectsAir",
                "LGrassEffects"
            ],
            "gdtklgrass2": [
                "LDustEffectsAir",
                "LGrassEffects"
            ],
            "gdtklmud": [
                "LDustEffectsAir"
            ],
            "gdtklsoil": [
                "LDustEffectsAir"
            ],
            "gdtklstones": [
                "LDustEffectsAir"
            ],
            "gdtklstubble": [
                "LDustEffectsAir"
            ],
            "gdtkltarmac": [
                "LDustEffectsAir"
            ],
            "gdtreddirt": [
                "LDustEffectsAirRed"
            ],
            "gdtrock": [
                "LDustEffectsAir",
                "LDirtEffects"
            ],
            "gdtrubble": [
                "LDustEffectsAir",
                "LDirtEffects"
            ],
            "gdtseabed": [
                "LDustEffectsAir"
            ],
            "gdtseabeddeep": [
                "LDustEffectsAir"
            ],
            "gdtsoil": [
                "LDustEffectsAir",
                "LDirtEffects"
            ],
            "gdtstony": [
                "LDustEffectsAir",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtstonygreen": [
                "LDustEffectsAir",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtstonythistle": [
                "LDustEffectsAir",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtstratisbeach": [
                "LDustEffectsAir",
                "LStonesEffects"
            ],
            "gdtstratisconcrete": [
                "LDustEffectsAir",
                "LDirtEffects"
            ],
            "gdtstratisdirt": [
                "LDustEffectsAir",
                "LDirtEffects"
            ],
            "gdtstratisdrygrass": [
                "LDustEffectsAir",
                "LGrassDryEffects",
                "LDirtEffects"
            ],
            "gdtstratisgreengrass": [
                "LDustEffectsAir",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtstratisrocky": [
                "LDustEffectsAir",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtstratisseabed": [
                "LDustEffectsAir"
            ],
            "gdtstratisseabedcluttered": [
                "LDustEffectsAir"
            ],
            "gdtstratisthistles": [
                "LDustEffectsAir",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtthorn": [
                "LDustEffectsAir",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtvolcano": [
                "LDustEffectsAir",
                "LStonesEffects"
            ],
            "gdtvolcanobeach": [
                "LDustEffectsAir"
            ],
            "gdtweed1": [
                "LDustEffectsAir",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtweed2": [
                "LDustEffectsAir",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "gdtwildfield": [
                "LDustEffectsAir",
                "LGrassEffects",
                "LDirtEffects"
            ],
            "surfintconcrete": [
                "LDustEffectsAir"
            ],
            "surfintmetal": [
                "LDustEffectsAir"
            ],
            "surfinttiles": [
                "LDustEffectsAir"
            ],
            "surfintwood": [
                "LDustEffectsAir"
            ],
            "surfmetal": [
                "LDustEffectsAir"
            ],
            "surfroadconcrete": [
                "LDustEffectsAir"
            ],
            "surfroadconcrete_exp": [
                "LDustEffectsAir"
            ],
            "surfroaddirt": [
                "LDustEffectsAir"
            ],
            "surfroaddirt_enoch": [
                "LDustEffectsAir"
            ],
            "surfroaddirt_exp": [
                "LDustEffectsAirRed"
            ],
            "surfroadtarmac": [
                "LDustEffectsAir"
            ],
            "surfroadtarmac1_enoch": [
                "LDustEffectsAir"
            ],
            "surfroadtarmac2_enoch": [
                "LDustEffectsAir"
            ],
            "surfroadtarmac3_enoch": [
                "LDustEffectsAir"
            ],
            "surfroadtarmac_exp": [
                "LDustEffectsAir"
            ],
            "surfrooftiles": [
                "LDustEffectsAir"
            ],
            "surfrooftin": [
                "LDustEffectsAir"
            ],
            "surftraildirt_enoch": [
                "LDustEffectsAir"
            ],
            "surfwood": [
                "LDustEffectsAir"
            ]
        },
        "right": {
            "default": [
                "RDustEffectsAir"
            ],
            "gdtasphalt": [
                "RDustEffectsAir",
                "RDirtEffects"
            ],
            "gdtbeach": [
                "RDustEffectsAir",
                "RStonesEffects"
            ],
            "gdtcliff": [
                "RDustEffectsAir"
            ],
            "gdtconcrete": [
                "RDustEffectsAir",
                "RDirtEffects"
            ],
            "gdtdead": [
                "RDustEffectsAir",
                "RDirtEffects"
            ],
            "gdtdesert1": [
                "RDustEffectsAir",
                "RSandEffects",
                "RDirtEffects",
                "RStonesEffects"
            ],
            "gdtdesert2": [
                "RDustEffectsAir",
                "RSandEffects",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtdirt": [
                "RDustEffectsAir",
                "RDirtEffects"
            ],
            "gdtfield": [
                "RDustEffectsAir"
            ],
            "gdtforest": [
                "RDustEffectsAir"
            ],
            "gdtgrassdry": [
                "RDustEffectsAir",
                "RGrassDryEffects",
                "RDirtEffects"
            ],
            "gdtgrassgreen": [
                "RDustEffectsAir",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtgrassshort": [
                "RDustEffectsAir",
                "RGrassEffects"
            ],
            "gdtgrasstall": [
                "RDustEffectsAir",
                "RGrassEffects"
            ],
            "gdtgrasswild": [
                "RDustEffectsAir",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtkldirt": [
                "RDustEffectsAir"
            ],
            "gdtklforestcon": [
                "RDustEffectsAir"
            ],
            "gdtklforestdec": [
                "RDustEffectsAir"
            ],
            "gdtklgrass1": [
                "RDustEffectsAir",
                "RGrassEffects"
            ],
            "gdtklgrass2": [
                "RDustEffectsAir",
                "RGrassEffects"
            ],
            "gdtklmud": [
                "RDustEffectsAir"
            ],
            "gdtklsoil": [
                "RDustEffectsAir"
            ],
            "gdtklstones": [
                "RDustEffectsAir"
            ],
            "gdtklstubble": [
                "RDustEffectsAir"
            ],
            "gdtkltarmac": [
                "RDustEffectsAir"
            ],
            "gdtreddirt": [
                "RDustEffectsAirRed"
            ],
            "gdtrock": [
                "RDustEffectsAir",
                "RDirtEffects"
            ],
            "gdtrubble": [
                "RDustEffectsAir",
                "RDirtEffects"
            ],
            "gdtseabed": [
                "RDustEffectsAir"
            ],
            "gdtseabeddeep": [
                "RDustEffectsAir"
            ],
            "gdtsoil": [
                "RDustEffectsAir",
                "RDirtEffects"
            ],
            "gdtstony": [
                "RDustEffectsAir",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtstonygreen": [
                "RDustEffectsAir",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtstonythistle": [
                "RDustEffectsAir",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtstratisbeach": [
                "RDustEffectsAir",
                "RStonesEffects"
            ],
            "gdtstratisconcrete": [
                "RDustEffectsAir",
                "RDirtEffects"
            ],
            "gdtstratisdirt": [
                "RDustEffectsAir",
                "RDirtEffects"
            ],
            "gdtstratisdrygrass": [
                "RDustEffectsAir",
                "RGrassDryEffects",
                "RDirtEffects"
            ],
            "gdtstratisgreengrass": [
                "RDustEffectsAir",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtstratisrocky": [
                "RDustEffectsAir",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtstratisseabed": [
                "RDustEffectsAir"
            ],
            "gdtstratisseabedcluttered": [
                "RDustEffectsAir"
            ],
            "gdtstratisthistles": [
                "RDustEffectsAir",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtthorn": [
                "RDustEffectsAir",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtvolcano": [
                "RDustEffectsAir",
                "RStonesEffects"
            ],
            "gdtvolcanobeach": [
                "RDustEffectsAir"
            ],
            "gdtweed1": [
                "RDustEffectsAir",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtweed2": [
                "RDustEffectsAir",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "gdtwildfield": [
                "RDustEffectsAir",
                "RGrassEffects",
                "RDirtEffects"
            ],
            "surfintconcrete": [
                "RDustEffectsAir"
            ],
            "surfintmetal": [
                "RDustEffectsAir"
            ],
            "surfinttiles": [
                "RDustEffectsAir"
            ],
            "surfintwood": [
                "RDustEffectsAir"
            ],
            "surfmetal": [
                "RDustEffectsAir"
            ],
            "surfroadconcrete": [
                "RDustEffectsAir"
            ],
            "surfroadconcrete_exp": [
                "RDustEffectsAir"
            ],
            "surfroaddirt": [
                "RDustEffectsAir"
            ],
            "surfroaddirt_enoch": [
                "RDustEffectsAir"
            ],
            "surfroaddirt_exp": [
                "RDustEffectsAirRed"
            ],
            "surfroadtarmac": [
                "RDustEffectsAir"
            ],
            "surfroadtarmac1_enoch": [
                "RDustEffectsAir"
            ],
            "surfroadtarmac2_enoch": [
                "RDustEffectsAir"
            ],
            "surfroadtarmac3_enoch": [
                "RDustEffectsAir"
            ],
            "surfroadtarmac_exp": [
                "RDustEffectsAir"
            ],
            "surfrooftiles": [
                "RDustEffectsAir"
            ],
            "surfrooftin": [
                "RDustEffectsAir"
            ],
            "surftraildirt_enoch": [
                "RDustEffectsAir"
            ],
            "surfwood": [
                "RDustEffectsAir"
            ]
        }
    },
    "dustfrontleftpos": "dustFrontLeft",
    "dustfrontrightpos": "dustFrontRight",
    "editorpreview": "rhsgref/addons/rhsgref_editorPreviews/data/RHS_AN2.paa",
    "editorsubcategory": "EdSubcat_Planes",
    "ejectdamagelimit": 0.45,
    "ejectdeadcargo": 0,
    "ejectdeaddriver": 0,
    "ejectspeed": [
        0,
        0,
        0
    ],
    "elevatorcoef": [],
    "elevatorcontrolssensitivitycoef": 4,
    "elevatorsensitivity": 0.4,
    "emptysound": [
        "",
        0,
        1
    ],
    "enablegps": 1,
    "enablemanualfire": 1,
    "enableradio": 1,
    "enablewatch": 0,
    "engineer": 0,
    "envelope": [
        0,
        0,
        0.43,
        1.2,
        2.3,
        2.42,
        3.53,
        7.12,
        8.56,
        11.05,
        9.39,
        7.94,
        5.2,
        2.82,
        0
    ],
    "epeimpulsedamagecoef": 10,
    "eventhandlers": {
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "init": "",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');",
        "rhs_defaulteventhandlers": {
            "hitpart": "_this call rhs_fnc_hitPart"
        },
        "rhs_eventhandlers": {
            "init": "_this call rhs_fnc_air_init"
        }
    },
    "exhausts": {
        "exhaust1": {
            "direction": "exhaust1_dir",
            "effect": "ExhaustsEffectPlane",
            "position": "exhaust1"
        }
    },
    "explosionshielding": 2,
    "extcameraparams": [
        1
    ],
    "extcameraposition": [
        0,
        5,
        -20
    ],
    "faction": "rhsgref_faction_cdf_air_b",
    "features": "",
    "featuretype": 0,
    "fireresistance": 10,
    "flaps": 1,
    "flapsfrictioncoef": 0.95,
    "flarevelocity": 100,
    "forcehidedriver": 0,
    "formationtime": 10,
    "formationx": 200,
    "formationz": 300,
    "fuelcapacity": 1000,
    "fuelconsumptionrate": 0.01,
    "fuelexplosionpower": 10,
    "fxexplo": {
        "access": 1
    },
    "geardowntime": 2,
    "gearretracting": 0,
    "gearsupfrictioncoef": 0.5,
    "gearuptime": 3.33,
    "getinaction": "GetInHigh",
    "getinoutonproxy": 0,
    "getinradius": 1.2,
    "getoutaction": "GetOutHigh",
    "gforceshakeattenuation": 0.5,
    "ghostpreview": "",
    "groupcameraposition": [
        0,
        5,
        -30
    ],
    "gunaimdown": 0,
    "gunclouds": {
        "access": 0,
        "cloudletaccy": 0.4,
        "cloudletalpha": 1,
        "cloudletanimperiod": 1,
        "cloudletcolor": [
            1,
            1,
            1,
            0
        ],
        "cloudletduration": 0.3,
        "cloudletfadein": 0.01,
        "cloudletfadeout": 1,
        "cloudletgrowup": 1,
        "cloudletmaxyspeed": 0.8,
        "cloudletminyspeed": 0.2,
        "cloudletshape": "cloudletClouds",
        "cloudletsize": 1,
        "deltat": 0,
        "initt": 0,
        "interval": 0.05,
        "size": 3,
        "sourcesize": 0.5,
        "table": {
            "t0": {
                "color": [
                    1,
                    1,
                    1,
                    0
                ],
                "maxt": 0
            }
        },
        "timetolive": 0
    },
    "gunfire": {
        "access": 0,
        "cloudletaccy": 0,
        "cloudletalpha": 1,
        "cloudletanimperiod": 1,
        "cloudletcolor": [
            1,
            1,
            1,
            0
        ],
        "cloudletduration": 0.2,
        "cloudletfadein": 0.01,
        "cloudletfadeout": 0.5,
        "cloudletgrowup": 0.2,
        "cloudletmaxyspeed": 100,
        "cloudletminyspeed": -100,
        "cloudletshape": "cloudletFire",
        "cloudletsize": 1,
        "deltat": -3000,
        "initt": 4500,
        "interval": 0.01,
        "size": 3,
        "sourcesize": 0.5,
        "table": {
            "t0": {
                "color": [
                    0.82,
                    0.95,
                    0.93,
                    0
                ],
                "maxt": 0
            },
            "t1": {
                "color": [
                    0.75,
                    0.77,
                    0.9,
                    0
                ],
                "maxt": 200
            },
            "t10": {
                "color": [
                    0.62,
                    0.29,
                    0.03,
                    0
                ],
                "maxt": 2600
            },
            "t11": {
                "color": [
                    0.59,
                    0.35,
                    0.05,
                    0
                ],
                "maxt": 2650
            },
            "t12": {
                "color": [
                    0.75,
                    0.37,
                    0.03,
                    0
                ],
                "maxt": 2700
            },
            "t13": {
                "color": [
                    0.88,
                    0.34,
                    0.03,
                    0
                ],
                "maxt": 2750
            },
            "t14": {
                "color": [
                    0.91,
                    0.5,
                    0.17,
                    0
                ],
                "maxt": 2800
            },
            "t15": {
                "color": [
                    1,
                    0.6,
                    0.2,
                    0
                ],
                "maxt": 2850
            },
            "t16": {
                "color": [
                    1,
                    0.71,
                    0.3,
                    0
                ],
                "maxt": 2900
            },
            "t17": {
                "color": [
                    0.98,
                    0.83,
                    0.41,
                    0
                ],
                "maxt": 2950
            },
            "t18": {
                "color": [
                    0.98,
                    0.91,
                    0.54,
                    0
                ],
                "maxt": 3000
            },
            "t19": {
                "color": [
                    0.98,
                    0.99,
                    0.6,
                    0
                ],
                "maxt": 3100
            },
            "t2": {
                "color": [
                    0.56,
                    0.62,
                    0.67,
                    0
                ],
                "maxt": 400
            },
            "t20": {
                "color": [
                    0.96,
                    0.99,
                    0.72,
                    0
                ],
                "maxt": 3300
            },
            "t21": {
                "color": [
                    1,
                    0.98,
                    0.91,
                    0
                ],
                "maxt": 3600
            },
            "t22": {
                "color": [
                    1,
                    1,
                    1,
                    0
                ],
                "maxt": 4200
            },
            "t3": {
                "color": [
                    0.39,
                    0.46,
                    0.47,
                    0
                ],
                "maxt": 600
            },
            "t4": {
                "color": [
                    0.24,
                    0.31,
                    0.31,
                    0
                ],
                "maxt": 800
            },
            "t5": {
                "color": [
                    0.23,
                    0.31,
                    0.29,
                    0
                ],
                "maxt": 1000
            },
            "t6": {
                "color": [
                    0.21,
                    0.29,
                    0.27,
                    0
                ],
                "maxt": 1500
            },
            "t7": {
                "color": [
                    0.19,
                    0.23,
                    0.21,
                    0
                ],
                "maxt": 2000
            },
            "t8": {
                "color": [
                    0.22,
                    0.19,
                    0.1,
                    0
                ],
                "maxt": 2300
            },
            "t9": {
                "color": [
                    0.35,
                    0.2,
                    0.02,
                    0
                ],
                "maxt": 2500
            }
        },
        "timetolive": 0
    },
    "gunnercansee": "1 + 2 + 4 + 8 + 32",
    "gunnergetinaction": "GetInHigh",
    "gunnergetoutaction": "GetOutHigh",
    "gunnerhasflares": 1,
    "hasdriver": 1,
    "hasterminal": 0,
    "headaimdown": 0,
    "headgforceleaningfactor": [
        0.005,
        0.001,
        0.025
    ],
    "headlimits": {
        "initanglex": 5,
        "initangley": 0,
        "maxanglex": 40,
        "maxangley": 90,
        "maxanglez": 45,
        "minanglex": -30,
        "minangley": -90,
        "minanglez": -45,
        "rotzradius": 0.2
    },
    "hiddenselections": [
        "Camo1",
        "Camo2",
        "Camo3",
        "n1",
        "n2",
        "i1",
        "i2"
    ],
    "hiddenselectionsmaterials": [],
    "hiddenselectionstextures": [
        "rhsgref/addons/rhsgref_air/an2/data/an2_1_co.paa",
        "rhsgref/addons/rhsgref_air/an2/data/an2_2_co.paa",
        "rhsgref/addons/rhsgref_air/an2/data/an2_wings_co.paa"
    ],
    "hiddenunderwaterselections": [],
    "hiddenunderwaterselectionstextures": [],
    "hideproxyincombat": 0,
    "hideunitinfo": 0,
    "hideweaponscargo": 0,
    "hideweaponsdriver": 1,
    "hitpoints": {
        "hitcontrolrear": {
            "armor": 0.6,
            "depends": "0",
            "explosionshielding": 0.1,
            "material": -1,
            "minimalhit": 0.1,
            "name": "hit_control_rear",
            "passthrough": 0.1,
            "radius": 0.04,
            "visual": "-"
        },
        "hitengine": {
            "armor": 0.5,
            "depends": "0",
            "explosionshielding": 1,
            "material": -1,
            "minimalhit": 0.1,
            "name": "hit_engine",
            "passthrough": 0.2,
            "radius": 0.15,
            "visual": "vis_engine"
        },
        "hitfuel": {
            "armor": 1.5,
            "depends": "0",
            "explosionshielding": 2,
            "material": -1,
            "minimalhit": 0,
            "name": "hit_fuel_l",
            "passthrough": 0.2,
            "radius": 0.1,
            "visual": "vis_wing_lh"
        },
        "hitfuel2": {
            "armor": 1.5,
            "depends": "0",
            "explosionshielding": 2,
            "material": -1,
            "minimalhit": 0,
            "name": "hit_fuel_r",
            "passthrough": 0.2,
            "radius": 0.1,
            "visual": "vis_wing_rh"
        },
        "hitglass1": {
            "armor": 0.1,
            "material": -1,
            "name": "glass1",
            "passthrough": 0,
            "visual": "glass1"
        },
        "hitglass2": {
            "armor": 0.1,
            "material": -1,
            "name": "glass2",
            "passthrough": 0,
            "visual": "glass2"
        },
        "hitglass3": {
            "armor": 0.1,
            "material": -1,
            "name": "glass3",
            "passthrough": 0,
            "visual": "glass3"
        },
        "hitglass4": {
            "armor": 0.1,
            "material": -1,
            "name": "glass4",
            "passthrough": 0,
            "visual": "glass4"
        },
        "hithull": {
            "armor": 1.5,
            "depends": "Total",
            "explosionshielding": 1,
            "material": -1,
            "minimalhit": 0,
            "name": "HitHull",
            "passthrough": 0.5,
            "radius": 0.3,
            "visual": "vis_hull"
        },
        "hitlaileron": {
            "armor": 1.5,
            "depends": "(HitLAileron_1 + HitLAileron_2)*0.5",
            "explosionshielding": 3,
            "material": -1,
            "minimalhit": 0.1,
            "name": "hit_aileron_lh",
            "passthrough": 0.1,
            "radius": 0.12,
            "visual": "vis_wing_lh"
        },
        "hitlaileron_1": {
            "armor": 1.5,
            "depends": "HitLAileron_link*0.7",
            "explosionshielding": 3,
            "material": -1,
            "minimalhit": 0.1,
            "name": "hit_aileron_lh",
            "passthrough": 0.1,
            "radius": 0.12,
            "visual": "vis_wing_lh"
        },
        "hitlaileron_2": {
            "armor": 1.5,
            "depends": "0",
            "explosionshielding": 3,
            "material": -1,
            "minimalhit": 0.1,
            "name": "hit_aileron_ld",
            "passthrough": 0.1,
            "radius": 0.1,
            "visual": "vis_wing_ld"
        },
        "hitlaileron_link": {
            "armor": 0.3,
            "depends": "0",
            "explosionshielding": 0.9,
            "material": -1,
            "minimalhit": 0.03,
            "name": "hit_aileron_link_l",
            "passthrough": 0.01,
            "radius": 0.1,
            "visual": ""
        },
        "hitlcelevator": {
            "armor": 1.5,
            "depends": "HitControlRear",
            "explosionshielding": 3,
            "material": -1,
            "minimalhit": 0.1,
            "name": "hit_elevator_l",
            "passthrough": 0.1,
            "radius": 0.11,
            "visual": "vis_elevator_l"
        },
        "hitlcrudder": {
            "armor": 1.5,
            "depends": "HitControlRear",
            "explosionshielding": 3,
            "material": -1,
            "minimalhit": 0.1,
            "name": "hit_rudder",
            "passthrough": 0.1,
            "radius": 0.15,
            "visual": "vis_rudder"
        },
        "hitraileron": {
            "armor": 1.5,
            "depends": "(HitRAileron_1 + HitRAileron_2)*0.5",
            "explosionshielding": 3,
            "material": -1,
            "minimalhit": 0.1,
            "name": "hit_aileron_rh",
            "passthrough": 0.1,
            "radius": 0.12,
            "visual": "vis_wing_rh"
        },
        "hitraileron_1": {
            "armor": 1.5,
            "depends": "HitRAileron_link*0.7",
            "explosionshielding": 3,
            "material": -1,
            "minimalhit": 0.1,
            "name": "hit_aileron_rh",
            "passthrough": 0.1,
            "radius": 0.12,
            "visual": "vis_wing_rh"
        },
        "hitraileron_2": {
            "armor": 1.5,
            "depends": "0",
            "explosionshielding": 3,
            "material": -1,
            "minimalhit": 0.1,
            "name": "hit_aileron_rd",
            "passthrough": 0.1,
            "radius": 0.1,
            "visual": "vis_wing_rd"
        },
        "hitraileron_link": {
            "armor": 0.3,
            "depends": "0",
            "explosionshielding": 0.9,
            "material": -1,
            "minimalhit": 0.03,
            "name": "hit_aileron_link_r",
            "passthrough": 0.01,
            "radius": 0.1,
            "visual": ""
        },
        "hitrelevator": {
            "armor": 1.5,
            "depends": "HitControlRear",
            "explosionshielding": 3,
            "material": -1,
            "minimalhit": 0.1,
            "name": "hit_elevator_r",
            "passthrough": 0.1,
            "radius": 0.11,
            "visual": "vis_elevator_r"
        }
    },
    "htmax": 1800,
    "htmin": 60,
    "hulldamagecauseexplosion": 0,
    "icon": "rhsgref/addons/rhsgref_air/AN2/data/UI/icon_an2_CA.paa",
    "impacteffectspeedlimit": 8,
    "impacteffectssea": "ImpactEffectsAir",
    "incomingmissiledetectionsystem": "8 + 16",
    "indirecthitciviliancoefai": -20,
    "indirecthitenemycoefai": 10,
    "indirecthitfriendlycoefai": -20,
    "indirecthitunknowncoefai": -0.5,
    "insidedetectcoef": 0.05,
    "insidesoundcoef": 0.2,
    "irscanground": 1,
    "irscanrangemax": 10000,
    "irscanrangemin": 2000,
    "irscantoeyefactor": 2,
    "irtarget": 1,
    "irtargetsize": 1,
    "isbackpack": 0,
    "keepinepesceneafterdeath": 0,
    "killfriendlyexpcoef": 1,
    "landingaoa": "rad(10)",
    "landingspeed": 85,
    "laserscanner": 0,
    "lasertarget": 0,
    "leftdusteffect": "LDustEffects",
    "leftdusteffects": [
        [
            "GdtKLDirt",
            "LDustEffectsAir"
        ],
        [
            "GdtKLGrass1",
            "LDustEffectsAir"
        ],
        [
            "GdtKLGrass1",
            "LGrassEffects"
        ],
        [
            "GdtKLGrass2",
            "LDustEffectsAir"
        ],
        [
            "GdtKLGrass2",
            "LGrassEffects"
        ],
        [
            "GdtKLForestCon",
            "LDustEffectsAir"
        ],
        [
            "GdtKLForestDec",
            "LDustEffectsAir"
        ],
        [
            "GdtKlMud",
            "LDustEffectsAir"
        ],
        [
            "GdtKlSoil",
            "LDustEffectsAir"
        ],
        [
            "GdtKlTarmac",
            "LDustEffectsAir"
        ],
        [
            "GdtKlStubble",
            "LDustEffectsAir"
        ],
        [
            "GdtKlStones",
            "LDustEffectsAir"
        ],
        [
            "SurfRoadDirt_Enoch",
            "LDustEffectsAir"
        ],
        [
            "SurfTrailDirt_Enoch",
            "LDustEffectsAir"
        ],
        [
            "SurfRoadTarmac1_Enoch",
            "LDustEffectsAir"
        ],
        [
            "SurfRoadTarmac2_Enoch",
            "LDustEffectsAir"
        ],
        [
            "SurfRoadTarmac3_Enoch",
            "LDustEffectsAir"
        ],
        [
            "GdtGrassShort",
            "LDustEffectsAir"
        ],
        [
            "GdtGrassShort",
            "LGrassEffects"
        ],
        [
            "GdtGrassTall",
            "LDustEffectsAir"
        ],
        [
            "GdtGrassTall",
            "LGrassEffects"
        ],
        [
            "GdtRedDirt",
            "LDustEffectsAirRed"
        ],
        [
            "GdtField",
            "LDustEffectsAir"
        ],
        [
            "GdtForest",
            "LDustEffectsAir"
        ],
        [
            "GdtVolcano",
            "LDustEffectsAir"
        ],
        [
            "GdtVolcano",
            "LStonesEffects"
        ],
        [
            "GdtCliff",
            "LDustEffectsAir"
        ],
        [
            "GdtVolcanoBeach",
            "LDustEffectsAir"
        ],
        [
            "SurfRoadDirt_exp",
            "LDustEffectsAirRed"
        ],
        [
            "SurfRoadConcrete_exp",
            "LDustEffectsAir"
        ],
        [
            "SurfRoadTarmac_exp",
            "LDustEffectsAir"
        ],
        [
            "GdtStratisConcrete",
            "LDustEffectsAir"
        ],
        [
            "GdtStratisConcrete",
            "LDirtEffects"
        ],
        [
            "GdtStratisBeach",
            "LDustEffectsAir"
        ],
        [
            "GdtStratisBeach",
            "LStonesEffects"
        ],
        [
            "GdtStratisDirt",
            "LDustEffectsAir"
        ],
        [
            "GdtStratisDirt",
            "LDirtEffects"
        ],
        [
            "GdtStratisSeabedCluttered",
            "LDustEffectsAir"
        ],
        [
            "GdtStratisSeabed",
            "LDustEffectsAir"
        ],
        [
            "GdtStratisDryGrass",
            "LDustEffectsAir"
        ],
        [
            "GdtStratisDryGrass",
            "LGrassDryEffects"
        ],
        [
            "GdtStratisDryGrass",
            "LDirtEffects"
        ],
        [
            "GdtStratisGreenGrass",
            "LDustEffectsAir"
        ],
        [
            "GdtStratisGreenGrass",
            "LGrassEffects"
        ],
        [
            "GdtStratisGreenGrass",
            "LDirtEffects"
        ],
        [
            "GdtStratisRocky",
            "LDustEffectsAir"
        ],
        [
            "GdtStratisRocky",
            "LGrassEffects"
        ],
        [
            "GdtStratisRocky",
            "LDirtEffects"
        ],
        [
            "GdtStratisThistles",
            "LDustEffectsAir"
        ],
        [
            "GdtStratisThistles",
            "LGrassEffects"
        ],
        [
            "GdtStratisThistles",
            "LDirtEffects"
        ],
        [
            "GdtConcrete",
            "LDustEffectsAir"
        ],
        [
            "GdtConcrete",
            "LDirtEffects"
        ],
        [
            "GdtAsphalt",
            "LDustEffectsAir"
        ],
        [
            "GdtAsphalt",
            "LDirtEffects"
        ],
        [
            "GdtRubble",
            "LDustEffectsAir"
        ],
        [
            "GdtRubble",
            "LDirtEffects"
        ],
        [
            "GdtSoil",
            "LDustEffectsAir"
        ],
        [
            "GdtSoil",
            "LDirtEffects"
        ],
        [
            "GdtBeach",
            "LDustEffectsAir"
        ],
        [
            "GdtBeach",
            "LStonesEffects"
        ],
        [
            "GdtRock",
            "LDustEffectsAir"
        ],
        [
            "GdtRock",
            "LDirtEffects"
        ],
        [
            "GdtDead",
            "LDustEffectsAir"
        ],
        [
            "GdtDead",
            "LDirtEffects"
        ],
        [
            "Default",
            "LDustEffectsAir"
        ],
        [
            "GdtDesert1",
            "LDustEffectsAir"
        ],
        [
            "GdtDesert1",
            "LSandEffects"
        ],
        [
            "GdtDesert1",
            "LDirtEffects"
        ],
        [
            "GdtDesert1",
            "LStonesEffects"
        ],
        [
            "GdtDesert2",
            "LDustEffectsAir"
        ],
        [
            "GdtDesert2",
            "LSandEffects"
        ],
        [
            "GdtDesert2",
            "LGrassEffects"
        ],
        [
            "GdtDesert2",
            "LDirtEffects"
        ],
        [
            "GdtDirt",
            "LDustEffectsAir"
        ],
        [
            "GdtDirt",
            "LDirtEffects"
        ],
        [
            "GdtGrassGreen",
            "LDustEffectsAir"
        ],
        [
            "GdtGrassGreen",
            "LGrassEffects"
        ],
        [
            "GdtGrassGreen",
            "LDirtEffects"
        ],
        [
            "GdtGrassDry",
            "LDustEffectsAir"
        ],
        [
            "GdtGrassDry",
            "LGrassDryEffects"
        ],
        [
            "GdtGrassDry",
            "LDirtEffects"
        ],
        [
            "GdtGrassWild",
            "LDustEffectsAir"
        ],
        [
            "GdtGrassWild",
            "LGrassEffects"
        ],
        [
            "GdtGrassWild",
            "LDirtEffects"
        ],
        [
            "GdtWildField",
            "LDustEffectsAir"
        ],
        [
            "GdtWildField",
            "LGrassEffects"
        ],
        [
            "GdtWildField",
            "LDirtEffects"
        ],
        [
            "GdtWeed1",
            "LDustEffectsAir"
        ],
        [
            "GdtWeed1",
            "LGrassEffects"
        ],
        [
            "GdtWeed1",
            "LDirtEffects"
        ],
        [
            "GdtWeed2",
            "LDustEffectsAir"
        ],
        [
            "GdtWeed2",
            "LGrassEffects"
        ],
        [
            "GdtWeed2",
            "LDirtEffects"
        ],
        [
            "GdtThorn",
            "LDustEffectsAir"
        ],
        [
            "GdtThorn",
            "LGrassEffects"
        ],
        [
            "GdtThorn",
            "LDirtEffects"
        ],
        [
            "GdtStony",
            "LDustEffectsAir"
        ],
        [
            "GdtStony",
            "LGrassEffects"
        ],
        [
            "GdtStony",
            "LDirtEffects"
        ],
        [
            "GdtStonyGreen",
            "LDustEffectsAir"
        ],
        [
            "GdtStonyGreen",
            "LGrassEffects"
        ],
        [
            "GdtStonyGreen",
            "LDirtEffects"
        ],
        [
            "GdtStonyThistle",
            "LDustEffectsAir"
        ],
        [
            "GdtStonyThistle",
            "LGrassEffects"
        ],
        [
            "GdtStonyThistle",
            "LDirtEffects"
        ],
        [
            "GdtSeabedDeep",
            "LDustEffectsAir"
        ],
        [
            "GdtSeabed",
            "LDustEffectsAir"
        ],
        [
            "SurfRoadDirt",
            "LDustEffectsAir"
        ],
        [
            "SurfRoadConcrete",
            "LDustEffectsAir"
        ],
        [
            "SurfRoadTarmac",
            "LDustEffectsAir"
        ],
        [
            "SurfWood",
            "LDustEffectsAir"
        ],
        [
            "SurfMetal",
            "LDustEffectsAir"
        ],
        [
            "SurfRoofTin",
            "LDustEffectsAir"
        ],
        [
            "SurfRoofTiles",
            "LDustEffectsAir"
        ],
        [
            "SurfIntWood",
            "LDustEffectsAir"
        ],
        [
            "SurfIntConcrete",
            "LDustEffectsAir"
        ],
        [
            "SurfIntTiles",
            "LDustEffectsAir"
        ],
        [
            "SurfIntMetal",
            "LDustEffectsAir"
        ]
    ],
    "lightongear": 0,
    "limitedspeedcoef": 0.22,
    "lockdetectionsystem": "8 + 4",
    "magazines": [],
    "mapsize": 20,
    "markerlights": {
        "greenstill": {
            "activelight": 0,
            "ambient": [
                0,
                0.08,
                0
            ],
            "blinking": 0,
            "color": [
                0,
                0.8,
                0
            ],
            "daylight": 0,
            "drawlight": 1,
            "drawlightcentersize": 0.04,
            "drawlightsize": 0.25,
            "intensity": 75,
            "name": "pos_light_still_green",
            "useflare": 1
        },
        "redblinking": {
            "ambient": [
                0.09,
                0.015,
                0.01
            ],
            "blinking": 1,
            "blinkingpattern": [
                2.9,
                0.1
            ],
            "blinkingpatternguarantee": 0,
            "blinkingstartson": 0,
            "color": [
                0.9,
                0.15,
                0.1
            ],
            "drawlightcentersize": 0.04,
            "drawlightsize": 0.2,
            "intensity": 75,
            "name": "pos_light_blink_red"
        },
        "redstill": {
            "activelight": 0,
            "ambient": [
                0.08,
                0,
                0
            ],
            "blinking": 0,
            "color": [
                0.8,
                0,
                0
            ],
            "daylight": 0,
            "drawlight": 1,
            "drawlightcentersize": 0.04,
            "drawlightsize": 0.25,
            "intensity": 75,
            "name": "pos_light_still_red",
            "useflare": 1
        },
        "whiteblinking1": {
            "ambient": [
                0.1,
                0.1,
                0.1
            ],
            "blinking": 1,
            "blinkingpattern": [
                0.1,
                2.9
            ],
            "blinkingpatternguarantee": 0,
            "color": [
                1,
                1,
                1
            ],
            "drawlightcentersize": 0.08,
            "drawlightsize": 0.35,
            "intensity": 100,
            "name": "pos_light_blink1_white"
        },
        "whiteblinking2": {
            "ambient": [
                0.1,
                0.1,
                0.1
            ],
            "blinking": 1,
            "blinkingpattern": [
                0.1,
                2.9
            ],
            "blinkingpatternguarantee": 0,
            "color": [
                1,
                1,
                1
            ],
            "drawlightcentersize": 0.08,
            "drawlightsize": 0.35,
            "intensity": 100,
            "name": "pos_light_blink2_white"
        },
        "whiteblinking3": {
            "ambient": [
                0.1,
                0.1,
                0.1
            ],
            "blinking": 1,
            "blinkingpattern": [
                0.1,
                2.9
            ],
            "blinkingpatternguarantee": 0,
            "color": [
                1,
                1,
                1
            ],
            "drawlightcentersize": 0.08,
            "drawlightsize": 0.35,
            "intensity": 100,
            "name": "pos_light_blink3_white"
        },
        "whitestill": {
            "activelight": 0,
            "ambient": [
                0.1,
                0.1,
                0.1
            ],
            "blinking": 0,
            "color": [
                1,
                1,
                1
            ],
            "daylight": 0,
            "drawlight": 1,
            "drawlightcentersize": 0.04,
            "drawlightsize": 0.25,
            "intensity": 75,
            "name": "pos_light_still_white",
            "useflare": 1
        }
    },
    "maxdetectrange": 20,
    "maxfordingdepth": 0.001,
    "maxgforce": 3,
    "maxgunelev": 0,
    "maxgunturn": 0,
    "maximumload": 500,
    "maxomega": 2000,
    "maxspeed": 258,
    "memorypointcm": [
        "flare_launcher1",
        "flare_launcher2"
    ],
    "memorypointcmdir": [
        "flare_launcher1_dir",
        "flare_launcher2_dir"
    ],
    "memorypointdriveroptics": [
        "driverview",
        "pilot"
    ],
    "memorypointgun": "kulomet",
    "memorypointldust": "levy prach",
    "memorypointlrocket": "L raketa",
    "memorypointrdust": "pravy prach",
    "memorypointrrocket": "P raketa",
    "memorypointsgetincargo": [
        "pos cargo"
    ],
    "memorypointsgetincargodir": [
        "pos cargo dir"
    ],
    "memorypointsgetincargoprecise": [
        "pos cargo"
    ],
    "memorypointsgetincodriver": "pos codriver",
    "memorypointsgetincodriverdir": "pos codriver dir",
    "memorypointsgetindriver": "pos cargo",
    "memorypointsgetindriverdir": "pos cargo dir",
    "memorypointsgetindriverprecise": "pos driver",
    "memorypointsleftwatereffect": "waterEffectL",
    "memorypointsrightwatereffect": "waterEffectR",
    "memorypointsupply": "doplnovani",
    "memorypointtaskmarker": "",
    "memorypointtaskmarkeroffset": [
        0,
        0.3,
        0
    ],
    "mfact": 0.2,
    "mfd": {
        "hud": {
            "bones": {
                "aglmove1": {
                    "max": 100,
                    "maxpos": [
                        0.05,
                        0.8
                    ],
                    "min": 0,
                    "minpos": [
                        0.05,
                        0.1
                    ],
                    "source": "altitudeAGL",
                    "type": "linear"
                },
                "aglmove2": {
                    "pos": [
                        0.05,
                        0.8
                    ],
                    "type": "fixed"
                },
                "aslmove1": {
                    "max": 500,
                    "maxpos": [
                        0.1,
                        0.8
                    ],
                    "min": 0,
                    "minpos": [
                        0.1,
                        0.1
                    ],
                    "source": "altitudeASL",
                    "type": "linear"
                },
                "aslmove2": {
                    "pos": [
                        0.1,
                        0.8
                    ],
                    "type": "fixed"
                },
                "ils": {
                    "pos0": [
                        0.5,
                        0.4
                    ],
                    "pos3": [
                        0.7,
                        0.6
                    ],
                    "type": "ils"
                },
                "level0": {
                    "angle": 0,
                    "pos0": [
                        0.5,
                        0.27
                    ],
                    "pos10": [
                        "0.5+0.9",
                        "0.27+0.7"
                    ],
                    "type": "horizon"
                },
                "levelm10": {
                    "angle": -10,
                    "pos0": [
                        0.5,
                        0.27
                    ],
                    "pos10": [
                        "0.5+0.9",
                        "0.27+0.7"
                    ],
                    "type": "horizon"
                },
                "levelm15": {
                    "angle": -15,
                    "pos0": [
                        0.5,
                        0.27
                    ],
                    "pos10": [
                        "0.5+0.9",
                        "0.27+0.7"
                    ],
                    "type": "horizon"
                },
                "levelm5": {
                    "angle": -5,
                    "pos0": [
                        0.5,
                        0.27
                    ],
                    "pos10": [
                        "0.5+0.9",
                        "0.27+0.7"
                    ],
                    "type": "horizon"
                },
                "levelp10": {
                    "angle": 10,
                    "pos0": [
                        0.5,
                        0.27
                    ],
                    "pos10": [
                        "0.5+0.9",
                        "0.27+0.7"
                    ],
                    "type": "horizon"
                },
                "levelp15": {
                    "angle": 15,
                    "pos0": [
                        0.5,
                        0.27
                    ],
                    "pos10": [
                        "0.5+0.9",
                        "0.27+0.7"
                    ],
                    "type": "horizon"
                },
                "levelp5": {
                    "angle": 5,
                    "pos0": [
                        0.5,
                        0.27
                    ],
                    "pos10": [
                        "0.5+0.9",
                        "0.27+0.7"
                    ],
                    "type": "horizon"
                },
                "planew": {
                    "pos": [
                        0.5,
                        0.27
                    ],
                    "type": "fixed"
                },
                "spdmove2": {
                    "max": 200,
                    "maxpos": [
                        0.94,
                        0.87
                    ],
                    "min": 33,
                    "minpos": [
                        0.94,
                        0.1
                    ],
                    "source": "speed",
                    "type": "linear"
                },
                "target": {
                    "pos0": [
                        0.5,
                        0.27
                    ],
                    "pos10": [
                        "0.5+0.9",
                        "0.27+0.7"
                    ],
                    "source": "target",
                    "type": "vector"
                },
                "targetdistancemgun": {
                    "center": [
                        0,
                        0
                    ],
                    "max": 1000,
                    "maxangle": 90,
                    "min": 100,
                    "minangle": -180,
                    "source": "targetDist",
                    "type": "rotational"
                },
                "targetdistancemissile": {
                    "center": [
                        0,
                        0
                    ],
                    "max": 3000,
                    "maxangle": 120,
                    "min": 100,
                    "minangle": -120,
                    "source": "targetDist",
                    "type": "rotational"
                },
                "velocity": {
                    "pos0": [
                        0.5,
                        0.27
                    ],
                    "pos10": [
                        "0.5+0.9",
                        "0.27+0.7"
                    ],
                    "source": "velocity",
                    "type": "vector"
                },
                "vertspeed": {
                    "max": 25,
                    "maxpos": [
                        0,
                        0.4
                    ],
                    "min": -25,
                    "minpos": [
                        0,
                        -0.4
                    ],
                    "source": "vSpeed",
                    "type": "linear"
                },
                "weaponaim": {
                    "pos0": [
                        0.5,
                        0.27
                    ],
                    "pos10": [
                        "0.5+0.9",
                        "0.27+0.7"
                    ],
                    "source": "weapon",
                    "type": "vector"
                }
            },
            "borderbottom": 0.1,
            "borderleft": 0.09,
            "borderright": 0.02,
            "bordertop": 0.02,
            "bottomleft": "HUD LD",
            "color": [
                0,
                1,
                0,
                0.1
            ],
            "draw": {
                "alpha": 0.8,
                "altitude": {
                    "points": [
                        [
                            "AGLMove1",
                            1
                        ],
                        [
                            "AGLMove2",
                            1
                        ],
                        [],
                        [
                            "ASLMove2",
                            1
                        ],
                        [
                            "ASLMove1",
                            1
                        ],
                        [
                            "ASLMove1",
                            [
                                0.02,
                                0
                            ],
                            1
                        ],
                        [
                            "ASLMove1",
                            [
                                0.02,
                                0
                            ],
                            1,
                            "VertSpeed",
                            1
                        ]
                    ],
                    "type": "line"
                },
                "clipbr": [
                    1,
                    0.9
                ],
                "cliptl": [
                    0,
                    0.05
                ],
                "color": [
                    0.1,
                    0.5,
                    0.05
                ],
                "condition": "on",
                "dimmedbase": {
                    "alpha": 0.3,
                    "altitudebase": {
                        "points": [
                            [
                                "AGLMove2",
                                1
                            ],
                            [
                                "ASLMove2",
                                1
                            ]
                        ],
                        "type": "line"
                    }
                },
                "horizont": {
                    "clipbr": [
                        0.8,
                        0.9
                    ],
                    "cliptl": [
                        0.2,
                        0.1
                    ],
                    "dimmed": {
                        "alpha": 0.6,
                        "level0": {
                            "points": [
                                [
                                    "Level0",
                                    [
                                        -0.4,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "Level0",
                                    [
                                        -0.13,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "Level0",
                                    [
                                        0.13,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "Level0",
                                    [
                                        0.4,
                                        0
                                    ],
                                    1
                                ]
                            ],
                            "type": "line"
                        }
                    },
                    "levelm10": {
                        "points": [
                            [
                                "LevelM10",
                                [
                                    -0.2,
                                    -0.05
                                ],
                                1
                            ],
                            [
                                "LevelM10",
                                [
                                    -0.2,
                                    0
                                ],
                                1
                            ],
                            [
                                "LevelM10",
                                [
                                    0.2,
                                    0
                                ],
                                1
                            ],
                            [
                                "LevelM10",
                                [
                                    0.2,
                                    -0.05
                                ],
                                1
                            ]
                        ],
                        "type": "line"
                    },
                    "levelm15": {
                        "points": [
                            [
                                "LevelM15",
                                [
                                    -0.2,
                                    -0.07
                                ],
                                1
                            ],
                            [
                                "LevelM15",
                                [
                                    -0.2,
                                    0
                                ],
                                1
                            ],
                            [
                                "LevelM15",
                                [
                                    0.2,
                                    0
                                ],
                                1
                            ],
                            [
                                "LevelM15",
                                [
                                    0.2,
                                    -0.07
                                ],
                                1
                            ]
                        ],
                        "type": "line"
                    },
                    "levelm5": {
                        "points": [
                            [
                                "LevelM5",
                                [
                                    -0.15,
                                    -0.03
                                ],
                                1
                            ],
                            [
                                "LevelM5",
                                [
                                    -0.15,
                                    0
                                ],
                                1
                            ],
                            [
                                "LevelM5",
                                [
                                    0.15,
                                    0
                                ],
                                1
                            ],
                            [
                                "LevelM5",
                                [
                                    0.15,
                                    -0.03
                                ],
                                1
                            ]
                        ],
                        "type": "line"
                    },
                    "levelp10": {
                        "points": [
                            [
                                "LevelP10",
                                [
                                    -0.2,
                                    0.05
                                ],
                                1
                            ],
                            [
                                "LevelP10",
                                [
                                    -0.2,
                                    0
                                ],
                                1
                            ],
                            [
                                "LevelP10",
                                [
                                    0.2,
                                    0
                                ],
                                1
                            ],
                            [
                                "LevelP10",
                                [
                                    0.2,
                                    0.05
                                ],
                                1
                            ]
                        ],
                        "type": "line"
                    },
                    "levelp15": {
                        "points": [
                            [
                                "LevelP15",
                                [
                                    -0.2,
                                    0.07
                                ],
                                1
                            ],
                            [
                                "LevelP15",
                                [
                                    -0.2,
                                    0
                                ],
                                1
                            ],
                            [
                                "LevelP15",
                                [
                                    0.2,
                                    0
                                ],
                                1
                            ],
                            [
                                "LevelP15",
                                [
                                    0.2,
                                    0.07
                                ],
                                1
                            ]
                        ],
                        "type": "line"
                    },
                    "levelp5": {
                        "points": [
                            [
                                "LevelP5",
                                [
                                    -0.15,
                                    0.03
                                ],
                                1
                            ],
                            [
                                "LevelP5",
                                [
                                    -0.15,
                                    0
                                ],
                                1
                            ],
                            [
                                "LevelP5",
                                [
                                    0.15,
                                    0
                                ],
                                1
                            ],
                            [
                                "LevelP5",
                                [
                                    0.15,
                                    0.03
                                ],
                                1
                            ]
                        ],
                        "type": "line"
                    }
                },
                "ils": {
                    "aoabracket": {
                        "points": [
                            [
                                [
                                    0.42,
                                    0.78
                                ],
                                1
                            ],
                            [
                                [
                                    0.4,
                                    0.78
                                ],
                                1
                            ],
                            [
                                [
                                    0.4,
                                    0.88
                                ],
                                1
                            ],
                            [
                                [
                                    0.42,
                                    0.88
                                ],
                                1
                            ]
                        ],
                        "type": "line"
                    },
                    "condition": "ils",
                    "glideslope": {
                        "clipbr": [
                            0.71,
                            0.71
                        ],
                        "cliptl": [
                            0.29,
                            0.29
                        ],
                        "ils": {
                            "points": [
                                [
                                    "ILS",
                                    [
                                        -10,
                                        0
                                    ],
                                    1
                                ],
                                [
                                    "ILS",
                                    [
                                        10,
                                        0
                                    ],
                                    1
                                ],
                                [],
                                [
                                    "ILS",
                                    [
                                        0,
                                        -10
                                    ],
                                    1
                                ],
                                [
                                    "ILS",
                                    [
                                        0,
                                        10
                                    ],
                                    1
                                ]
                            ],
                            "type": "line"
                        }
                    }
                },
                "mgun": {
                    "circle": {
                        "points": [
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.07
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "+0.7*0.07",
                                    "-0.7*0.07"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.07,
                                    0
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "+0.7*0.07",
                                    "+0.7*0.07"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    0.07
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "-0.7*0.07",
                                    "+0.7*0.07"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.07,
                                    0
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "-0.7*0.07",
                                    "-0.7*0.07"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.07
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.01
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "+0.7*0.01",
                                    "-0.7*0.01"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.01,
                                    0
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "+0.7*0.01",
                                    "+0.7*0.01"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    0.01
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "-0.7*0.01",
                                    "+0.7*0.01"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.01,
                                    0
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "-0.7*0.01",
                                    "-0.7*0.01"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.01
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    "0.03*sin(-180)",
                                    "-0.03*cos(-180)"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "0.07*sin(-180)",
                                    "-0.07*cos(-180)"
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    "0.03*sin(+90)",
                                    "-0.03*cos(+90)"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "0.07*sin(+90)",
                                    "-0.07*cos(+90)"
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                1,
                                "TargetDistanceMGun",
                                [
                                    0,
                                    0.04
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                1,
                                "TargetDistanceMGun",
                                [
                                    0,
                                    0.07
                                ],
                                1
                            ]
                        ],
                        "type": "line"
                    },
                    "condition": "mgun"
                },
                "missile": {
                    "circle": {
                        "points": [
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.1
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "+0.7*0.1",
                                    "-0.7*0.1"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0.1,
                                    0
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "+0.7*0.1",
                                    "+0.7*0.1"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    0.1
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "-0.7*0.1",
                                    "+0.7*0.1"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    -0.1,
                                    0
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "-0.7*0.1",
                                    "-0.7*0.1"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    0,
                                    -0.1
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    "0.1*0.8*sin(-120)",
                                    "-0.1*0.8*cos(-120)"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "0.1*1.2*sin(-120)",
                                    "-0.1*1.2*cos(-120)"
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                [
                                    "0.1*0.8*sin(+120)",
                                    "-0.1*0.8*cos(+120)"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                [
                                    "0.1*1.2*sin(+120)",
                                    "-0.1*1.2*cos(+120)"
                                ],
                                1
                            ],
                            [],
                            [
                                "WeaponAim",
                                1,
                                "TargetDistanceMissile",
                                [
                                    0,
                                    "0.1*0.8"
                                ],
                                1
                            ],
                            [
                                "WeaponAim",
                                1,
                                "TargetDistanceMissile",
                                [
                                    0,
                                    "0.1*1.2"
                                ],
                                1
                            ]
                        ],
                        "type": "line"
                    },
                    "condition": "missile",
                    "target": {
                        "points": [
                            [
                                "Target",
                                [
                                    -0.05,
                                    -0.05
                                ],
                                1
                            ],
                            [
                                "Target",
                                [
                                    0.05,
                                    -0.05
                                ],
                                1
                            ],
                            [
                                "Target",
                                [
                                    0.05,
                                    0.05
                                ],
                                1
                            ],
                            [
                                "Target",
                                [
                                    -0.05,
                                    0.05
                                ],
                                1
                            ],
                            [
                                "Target",
                                [
                                    -0.05,
                                    -0.05
                                ],
                                1
                            ]
                        ],
                        "type": "line"
                    }
                },
                "planew": {
                    "clipbr": [
                        1,
                        0.9
                    ],
                    "cliptl": [
                        0,
                        0.1
                    ],
                    "linehl": {
                        "points": [
                            [
                                "PlaneW",
                                [
                                    -0.07,
                                    0
                                ],
                                1
                            ],
                            [
                                "PlaneW",
                                [
                                    -0.02,
                                    0
                                ],
                                1
                            ],
                            [
                                "PlaneW",
                                [
                                    0,
                                    -0.02
                                ],
                                1
                            ],
                            [
                                "PlaneW",
                                [
                                    0.02,
                                    0
                                ],
                                1
                            ],
                            [
                                "PlaneW",
                                [
                                    0,
                                    0.02
                                ],
                                1
                            ],
                            [
                                "PlaneW",
                                [
                                    -0.02,
                                    0
                                ],
                                1
                            ],
                            [],
                            [
                                "PlaneW",
                                [
                                    0.02,
                                    0
                                ],
                                1
                            ],
                            [
                                "PlaneW",
                                [
                                    0.07,
                                    0
                                ],
                                1
                            ]
                        ],
                        "type": "line"
                    },
                    "velocity": {
                        "points": [
                            [
                                "Velocity",
                                [
                                    0,
                                    -0.02
                                ],
                                1
                            ],
                            [
                                "Velocity",
                                [
                                    0.02,
                                    0
                                ],
                                1
                            ],
                            [
                                "Velocity",
                                [
                                    0,
                                    0.02
                                ],
                                1
                            ],
                            [
                                "Velocity",
                                [
                                    -0.02,
                                    0
                                ],
                                1
                            ],
                            [
                                "Velocity",
                                [
                                    0,
                                    -0.02
                                ],
                                1
                            ]
                        ],
                        "type": "line"
                    }
                },
                "speed": {
                    "points": [
                        [
                            [
                                0.95,
                                0.87
                            ],
                            1
                        ],
                        [
                            [
                                0.95,
                                0.1
                            ],
                            1
                        ],
                        [],
                        [
                            "SpdMove2",
                            [
                                -0.05,
                                0
                            ],
                            1
                        ],
                        [
                            "SpdMove2",
                            1
                        ]
                    ],
                    "type": "line"
                },
                "speednumber": {
                    "align": "left",
                    "down": [
                        "SpdMove2",
                        [
                            -0.05,
                            0.03
                        ],
                        1
                    ],
                    "pos": [
                        "SpdMove2",
                        [
                            -0.05,
                            -0.03
                        ],
                        1
                    ],
                    "right": [
                        "SpdMove2",
                        [
                            0.01,
                            -0.03
                        ],
                        1
                    ],
                    "scale": 1,
                    "source": "speed",
                    "sourcescale": 3.6,
                    "type": "text"
                }
            },
            "helmetdown": [
                0,
                -0.05,
                0
            ],
            "helmetmounteddisplay": 1,
            "helmetposition": [
                -0.025,
                0.025,
                0.1
            ],
            "helmetright": [
                0.05,
                0,
                0
            ],
            "pos10vector": {
                "pos0": [
                    0.5,
                    0.27
                ],
                "pos10": [
                    "0.5+0.9",
                    "0.27+0.7"
                ],
                "type": "vector"
            },
            "topleft": "HUD LH",
            "topright": "HUD PH"
        }
    },
    "mfmax": 100,
    "mgunclouds": {
        "access": 0,
        "cloudletaccy": 0,
        "cloudletalpha": 0.3,
        "cloudletanimperiod": 1,
        "cloudletcolor": [
            1,
            1,
            1,
            0
        ],
        "cloudletduration": 0.05,
        "cloudletfadein": 0,
        "cloudletfadeout": 0.1,
        "cloudletgrowup": 0.05,
        "cloudletmaxyspeed": 100,
        "cloudletminyspeed": -100,
        "cloudletshape": "cloudletClouds",
        "cloudletsize": 1,
        "deltat": 0,
        "initt": 0,
        "interval": 0.02,
        "size": 0.3,
        "sourcesize": 0.02,
        "table": {
            "t0": {
                "color": [
                    1,
                    1,
                    1,
                    0
                ],
                "maxt": 0
            }
        },
        "timetolive": 0
    },
    "mgunfire": {
        "access": 0,
        "cloudletaccy": 0,
        "cloudletalpha": 1,
        "cloudletanimperiod": 1,
        "cloudletcolor": [
            1,
            1,
            1,
            0
        ],
        "cloudletduration": 0,
        "cloudletfadein": 0,
        "cloudletfadeout": 0.12,
        "cloudletgrowup": 0.06,
        "cloudletmaxyspeed": 100,
        "cloudletminyspeed": -100,
        "cloudletshape": "cloudletFire",
        "cloudletsize": 1,
        "deltat": -4000,
        "initt": 3200,
        "interval": 0.005,
        "size": 0.12,
        "sourcesize": 0.01,
        "table": {
            "t0": {
                "color": [
                    0.82,
                    0.95,
                    0.93,
                    0
                ],
                "maxt": 0
            },
            "t1": {
                "color": [
                    0.75,
                    0.77,
                    0.9,
                    0
                ],
                "maxt": 200
            },
            "t10": {
                "color": [
                    0.62,
                    0.29,
                    0.03,
                    0
                ],
                "maxt": 2600
            },
            "t11": {
                "color": [
                    0.59,
                    0.35,
                    0.05,
                    0
                ],
                "maxt": 2650
            },
            "t12": {
                "color": [
                    0.75,
                    0.37,
                    0.03,
                    0
                ],
                "maxt": 2700
            },
            "t13": {
                "color": [
                    0.88,
                    0.34,
                    0.03,
                    0
                ],
                "maxt": 2750
            },
            "t14": {
                "color": [
                    0.91,
                    0.5,
                    0.17,
                    0
                ],
                "maxt": 2800
            },
            "t15": {
                "color": [
                    1,
                    0.6,
                    0.2,
                    0
                ],
                "maxt": 2850
            },
            "t16": {
                "color": [
                    1,
                    0.71,
                    0.3,
                    0
                ],
                "maxt": 2900
            },
            "t17": {
                "color": [
                    0.98,
                    0.83,
                    0.41,
                    0
                ],
                "maxt": 2950
            },
            "t18": {
                "color": [
                    0.98,
                    0.91,
                    0.54,
                    0
                ],
                "maxt": 3000
            },
            "t19": {
                "color": [
                    0.98,
                    0.99,
                    0.6,
                    0
                ],
                "maxt": 3100
            },
            "t2": {
                "color": [
                    0.56,
                    0.62,
                    0.67,
                    0
                ],
                "maxt": 400
            },
            "t20": {
                "color": [
                    0.96,
                    0.99,
                    0.72,
                    0
                ],
                "maxt": 3300
            },
            "t21": {
                "color": [
                    1,
                    0.98,
                    0.91,
                    0
                ],
                "maxt": 3600
            },
            "t22": {
                "color": [
                    1,
                    1,
                    1,
                    0
                ],
                "maxt": 4200
            },
            "t3": {
                "color": [
                    0.39,
                    0.46,
                    0.47,
                    0
                ],
                "maxt": 600
            },
            "t4": {
                "color": [
                    0.24,
                    0.31,
                    0.31,
                    0
                ],
                "maxt": 800
            },
            "t5": {
                "color": [
                    0.23,
                    0.31,
                    0.29,
                    0
                ],
                "maxt": 1000
            },
            "t6": {
                "color": [
                    0.21,
                    0.29,
                    0.27,
                    0
                ],
                "maxt": 1500
            },
            "t7": {
                "color": [
                    0.19,
                    0.23,
                    0.21,
                    0
                ],
                "maxt": 2000
            },
            "t8": {
                "color": [
                    0.22,
                    0.19,
                    0.1,
                    0
                ],
                "maxt": 2300
            },
            "t9": {
                "color": [
                    0.35,
                    0.2,
                    0.02,
                    0
                ],
                "maxt": 2500
            }
        },
        "timetolive": 0
    },
    "minealerticonrange": 200,
    "minfiretime": 60,
    "mingforce": 0.3,
    "mingunelev": 0,
    "mingunturn": 0,
    "mintotaldamagethreshold": 0.005,
    "model": "rhsgref/addons/rhsgref_air/AN2/AN2.p3d",
    "namesound": "veh_air_plane_s",
    "newturret": {
        "aggregatereflectors": [],
        "allowlauncherin": 0,
        "allowlauncherout": 0,
        "allowtablock": 1,
        "animationsourcebody": "mainTurret",
        "animationsourcecamelev": "camElev",
        "animationsourcegun": "mainGun",
        "animationsourcehatch": "hatchGunner",
        "armorlights": 0.4,
        "body": "mainTurret",
        "caneject": 1,
        "canhidegunner": -1,
        "canusescanners": 1,
        "castgunnershadow": 0,
        "commanding": 1,
        "disablesoundattenuation": 0,
        "dontcreateai": 0,
        "ejectdeadgunner": 0,
        "forcehidegunner": 0,
        "forcenvg": 0,
        "gun": "mainGun",
        "gunbeg": "usti hlavne",
        "gunclouds": {
            "access": 0,
            "cloudletaccy": 0.4,
            "cloudletalpha": 1,
            "cloudletanimperiod": 1,
            "cloudletcolor": [
                1,
                1,
                1,
                0
            ],
            "cloudletduration": 0.3,
            "cloudletfadein": 0.01,
            "cloudletfadeout": 1,
            "cloudletgrowup": 1,
            "cloudletmaxyspeed": 0.8,
            "cloudletminyspeed": 0.2,
            "cloudletshape": "cloudletClouds",
            "cloudletsize": 1,
            "deltat": 0,
            "initt": 0,
            "interval": 0.05,
            "size": 3,
            "sourcesize": 0.5,
            "table": {
                "t0": {
                    "color": [
                        1,
                        1,
                        1,
                        0
                    ],
                    "maxt": 0
                }
            },
            "timetolive": 0
        },
        "gunend": "konec hlavne",
        "gunfire": {
            "access": 0,
            "cloudletaccy": 0,
            "cloudletalpha": 1,
            "cloudletanimperiod": 1,
            "cloudletcolor": [
                1,
                1,
                1,
                0
            ],
            "cloudletduration": 0.2,
            "cloudletfadein": 0.01,
            "cloudletfadeout": 0.5,
            "cloudletgrowup": 0.2,
            "cloudletmaxyspeed": 100,
            "cloudletminyspeed": -100,
            "cloudletshape": "cloudletFire",
            "cloudletsize": 1,
            "deltat": -3000,
            "initt": 4500,
            "interval": 0.01,
            "size": 3,
            "sourcesize": 0.5,
            "table": {
                "t0": {
                    "color": [
                        0.82,
                        0.95,
                        0.93,
                        0
                    ],
                    "maxt": 0
                },
                "t1": {
                    "color": [
                        0.75,
                        0.77,
                        0.9,
                        0
                    ],
                    "maxt": 200
                },
                "t10": {
                    "color": [
                        0.62,
                        0.29,
                        0.03,
                        0
                    ],
                    "maxt": 2600
                },
                "t11": {
                    "color": [
                        0.59,
                        0.35,
                        0.05,
                        0
                    ],
                    "maxt": 2650
                },
                "t12": {
                    "color": [
                        0.75,
                        0.37,
                        0.03,
                        0
                    ],
                    "maxt": 2700
                },
                "t13": {
                    "color": [
                        0.88,
                        0.34,
                        0.03,
                        0
                    ],
                    "maxt": 2750
                },
                "t14": {
                    "color": [
                        0.91,
                        0.5,
                        0.17,
                        0
                    ],
                    "maxt": 2800
                },
                "t15": {
                    "color": [
                        1,
                        0.6,
                        0.2,
                        0
                    ],
                    "maxt": 2850
                },
                "t16": {
                    "color": [
                        1,
                        0.71,
                        0.3,
                        0
                    ],
                    "maxt": 2900
                },
                "t17": {
                    "color": [
                        0.98,
                        0.83,
                        0.41,
                        0
                    ],
                    "maxt": 2950
                },
                "t18": {
                    "color": [
                        0.98,
                        0.91,
                        0.54,
                        0
                    ],
                    "maxt": 3000
                },
                "t19": {
                    "color": [
                        0.98,
                        0.99,
                        0.6,
                        0
                    ],
                    "maxt": 3100
                },
                "t2": {
                    "color": [
                        0.56,
                        0.62,
                        0.67,
                        0
                    ],
                    "maxt": 400
                },
                "t20": {
                    "color": [
                        0.96,
                        0.99,
                        0.72,
                        0
                    ],
                    "maxt": 3300
                },
                "t21": {
                    "color": [
                        1,
                        0.98,
                        0.91,
                        0
                    ],
                    "maxt": 3600
                },
                "t22": {
                    "color": [
                        1,
                        1,
                        1,
                        0
                    ],
                    "maxt": 4200
                },
                "t3": {
                    "color": [
                        0.39,
                        0.46,
                        0.47,
                        0
                    ],
                    "maxt": 600
                },
                "t4": {
                    "color": [
                        0.24,
                        0.31,
                        0.31,
                        0
                    ],
                    "maxt": 800
                },
                "t5": {
                    "color": [
                        0.23,
                        0.31,
                        0.29,
                        0
                    ],
                    "maxt": 1000
                },
                "t6": {
                    "color": [
                        0.21,
                        0.29,
                        0.27,
                        0
                    ],
                    "maxt": 1500
                },
                "t7": {
                    "color": [
                        0.19,
                        0.23,
                        0.21,
                        0
                    ],
                    "maxt": 2000
                },
                "t8": {
                    "color": [
                        0.22,
                        0.19,
                        0.1,
                        0
                    ],
                    "maxt": 2300
                },
                "t9": {
                    "color": [
                        0.35,
                        0.2,
                        0.02,
                        0
                    ],
                    "maxt": 2500
                }
            },
            "timetolive": 0
        },
        "gunneraction": "ManActTestDriver",
        "gunnercompartments": "Compartment1",
        "gunnerdoor": "",
        "gunnerfirealsoininternalcamera": 1,
        "gunnerforceoptics": 1,
        "gunnergetinaction": "",
        "gunnergetoutaction": "",
        "gunnerinaction": "ManActTestDriver",
        "gunnerlefthandanimname": "",
        "gunnerleftleganimname": "",
        "gunnername": "Gunner",
        "gunneropticscolor": [
            0,
            0,
            0,
            1
        ],
        "gunneropticseffect": [],
        "gunneropticsmodel": "",
        "gunneropticsshowcursor": 0,
        "gunneroutfirealsoininternalcamera": 1,
        "gunneroutforceoptics": 0,
        "gunneroutopticscolor": [
            0,
            0,
            0,
            1
        ],
        "gunneroutopticseffect": [],
        "gunneroutopticsmodel": "",
        "gunneroutopticsshowcursor": 0,
        "gunnerrighthandanimname": "",
        "gunnerrightleganimname": "",
        "gunnertype": "",
        "gunnerusespilotview": 0,
        "hasgunner": 1,
        "hideweaponsgunner": 1,
        "hitpoints": {
            "hitgun": {
                "armor": 0.6,
                "explosionshielding": 1,
                "material": 52,
                "name": "gun",
                "passthrough": 1,
                "visual": "gun"
            },
            "hitturret": {
                "armor": 0.8,
                "explosionshielding": 1,
                "material": 51,
                "name": "turret",
                "passthrough": 1,
                "visual": "turret"
            }
        },
        "ingunnermayfire": 1,
        "initcamelev": 0,
        "initelev": 0,
        "initoutelev": 0,
        "initoutturn": 0,
        "initturn": 0,
        "iscopilot": 0,
        "lockwhendriverout": 0,
        "lockwhenvehiclespeed": -1,
        "lodturnedin": -1,
        "lodturnedout": -1,
        "magazines": [],
        "maxcamelev": 90,
        "maxelev": 20,
        "maxhorizontalrotspeed": 1.2,
        "maxoutelev": 20,
        "maxoutturn": 60,
        "maxturn": 360,
        "maxverticalrotspeed": 1.2,
        "memorypointgun": "kulas",
        "memorypointgunneroptics": "gunnerview",
        "memorypointgunneroutoptics": "",
        "memorypointsgetingunner": "pos gunner",
        "memorypointsgetingunnerdir": "pos gunner dir",
        "memorypointsgetingunnerprecise": "",
        "mgunclouds": {
            "access": 0,
            "cloudletaccy": 0,
            "cloudletalpha": 0.3,
            "cloudletanimperiod": 1,
            "cloudletcolor": [
                1,
                1,
                1,
                0
            ],
            "cloudletduration": 0.05,
            "cloudletfadein": 0,
            "cloudletfadeout": 0.1,
            "cloudletgrowup": 0.05,
            "cloudletmaxyspeed": 100,
            "cloudletminyspeed": -100,
            "cloudletshape": "cloudletClouds",
            "cloudletsize": 1,
            "deltat": 0,
            "initt": 0,
            "interval": 0.02,
            "size": 0.3,
            "sourcesize": 0.02,
            "table": {
                "t0": {
                    "color": [
                        1,
                        1,
                        1,
                        0
                    ],
                    "maxt": 0
                }
            },
            "timetolive": 0
        },
        "mincamelev": -90,
        "minelev": -4,
        "minoutelev": -4,
        "minoutturn": -60,
        "minturn": -360,
        "missilebeg": "spice rakety",
        "missileend": "konec rakety",
        "outgunnermayfire": 0,
        "playerposition": 0,
        "precisegetinout": 0,
        "primary": 1,
        "primarygunner": 1,
        "primaryobserver": 0,
        "proxyindex": 1,
        "proxytype": "CPGunner",
        "reflectors": {},
        "selectionfireanim": "zasleh",
        "showalltargets": 0,
        "showcrewaim": 0,
        "showhmd": 0,
        "slingloadoperator": 0,
        "soundelevation": [
            "",
            0.00316228,
            1
        ],
        "soundservo": [
            "",
            0.00316228,
            1
        ],
        "stabilizedinaxes": 3,
        "startengine": 1,
        "turnin": {
            "turnoffset": 0
        },
        "turnout": {
            "turnoffset": 0
        },
        "turretcansee": 0,
        "turretfollowfreelook": 0,
        "turretinfotype": "",
        "turrets": {},
        "turretspec": {
            "showheadphones": 0
        },
        "viewgunner": {
            "continuous": 0,
            "initanglex": 5,
            "initangley": 0,
            "initfov": 0.75,
            "maxanglex": 85,
            "maxangley": 150,
            "maxfov": 1.25,
            "maxmovex": 0,
            "maxmovey": 0,
            "maxmovez": 0,
            "minanglex": -75,
            "minangley": -150,
            "minfov": 0.25,
            "minmovex": 0,
            "minmovey": 0,
            "minmovez": 0,
            "speedzoommaxfov": 0,
            "speedzoommaxspeed": 10000000000.0
        },
        "viewgunnerinexternal": 0,
        "viewgunnershadow": 1,
        "viewgunnershadowamb": 1,
        "viewgunnershadowdiff": 1,
        "viewoptics": {
            "initanglex": 0,
            "initangley": 0,
            "initfov": 0.3,
            "maxanglex": 30,
            "maxangley": 100,
            "maxfov": 0.35,
            "maxmovex": 0,
            "maxmovey": 0,
            "maxmovez": 0,
            "minanglex": -30,
            "minangley": -100,
            "minfov": 0.07,
            "minmovex": 0,
            "minmovey": 0,
            "minmovez": 0,
            "speedzoommaxfov": 0,
            "speedzoommaxspeed": 10000000000.0
        },
        "weapons": []
    },
    "nightvision": 0,
    "normalspeedforwardcoef": 0.85,
    "numberphysicalwheels": 3,
    "nvgmarker": {
        "ambient": [
            1,
            1,
            1,
            1
        ],
        "blinking": 0,
        "brightness": 1,
        "diffuse": [
            1,
            1,
            1,
            1
        ],
        "onlyinnvg": 0
    },
    "nvgmarkers": {},
    "nvscanner": 0,
    "nvtarget": 0,
    "obstructsoundlfratio": 0,
    "obstructsoundswhenin": 0.316228,
    "occludesoundlfratio": 0.25,
    "occludesoundswhenin": 0.316228,
    "outsidesoundfilter": 1,
    "picture": "rhsgref/addons/rhsgref_air/AN2/data/UI/picture_an2_CA.paa",
    "pilotspec": {
        "showheadphones": 0
    },
    "portrait": "",
    "precisegetinout": 0,
    "precision": 200,
    "predictturnplan": 1,
    "predictturnsimul": 1.2,
    "preferroads": 0,
    "pulsationsound": {},
    "radartarget": 1,
    "radartargetsize": 1,
    "radartype": 4,
    "reflectors": {
        "left": {
            "ambient": [
                100,
                100,
                100,
                0
            ],
            "attenuation": {
                "constant": 0,
                "linear": 0,
                "quadratic": 4,
                "start": 1
            },
            "color": [
                7000,
                7500,
                10000,
                1
            ],
            "conefadecoef": 10,
            "daylight": 0,
            "direction": "light_l_dir",
            "flaresize": 6,
            "hitpoint": "light_l",
            "innerangle": 20,
            "intensity": 50,
            "outerangle": 60,
            "position": "light_l",
            "selection": "light_l",
            "size": 1,
            "useflare": 1
        },
        "right": {
            "ambient": [
                100,
                100,
                100,
                0
            ],
            "attenuation": {
                "constant": 0,
                "linear": 0,
                "quadratic": 4,
                "start": 1
            },
            "color": [
                7000,
                7500,
                10000,
                1
            ],
            "conefadecoef": 10,
            "daylight": 0,
            "direction": "light_r_dir",
            "flaresize": 6,
            "hitpoint": "light_r",
            "innerangle": 20,
            "intensity": 50,
            "outerangle": 60,
            "position": "light_r",
            "selection": "light_r",
            "size": 1,
            "useflare": 1
        }
    },
    "rendertargets": {},
    "replacedamaged": "",
    "replacedamagedhitpoints": [],
    "replacedamagedlimit": 0.9,
    "reversed": 1,
    "rhs_decalparameters": [
        "['Number',[3,4],'AviaCDF']",
        "['Label',[5],'Aviation', 4]",
        "['Label',[6],'AviationSquadronsCDF']"
    ],
    "rightdusteffect": "RDustEffects",
    "rightdusteffects": [
        [
            "GdtKLDirt",
            "RDustEffectsAir"
        ],
        [
            "GdtKLGrass1",
            "RDustEffectsAir"
        ],
        [
            "GdtKLGrass1",
            "RGrassEffects"
        ],
        [
            "GdtKLGrass2",
            "RDustEffectsAir"
        ],
        [
            "GdtKLGrass2",
            "RGrassEffects"
        ],
        [
            "GdtKLForestCon",
            "RDustEffectsAir"
        ],
        [
            "GdtKLForestDec",
            "RDustEffectsAir"
        ],
        [
            "GdtKlMud",
            "RDustEffectsAir"
        ],
        [
            "GdtKlSoil",
            "RDustEffectsAir"
        ],
        [
            "GdtKlTarmac",
            "RDustEffectsAir"
        ],
        [
            "GdtKlStubble",
            "RDustEffectsAir"
        ],
        [
            "GdtKlStones",
            "RDustEffectsAir"
        ],
        [
            "SurfRoadDirt_Enoch",
            "RDustEffectsAir"
        ],
        [
            "SurfTrailDirt_Enoch",
            "RDustEffectsAir"
        ],
        [
            "SurfRoadTarmac1_Enoch",
            "RDustEffectsAir"
        ],
        [
            "SurfRoadTarmac2_Enoch",
            "RDustEffectsAir"
        ],
        [
            "SurfRoadTarmac3_Enoch",
            "RDustEffectsAir"
        ],
        [
            "GdtGrassShort",
            "RDustEffectsAir"
        ],
        [
            "GdtGrassShort",
            "RGrassEffects"
        ],
        [
            "GdtGrassTall",
            "RDustEffectsAir"
        ],
        [
            "GdtGrassTall",
            "RGrassEffects"
        ],
        [
            "GdtRedDirt",
            "RDustEffectsAirRed"
        ],
        [
            "GdtField",
            "RDustEffectsAir"
        ],
        [
            "GdtForest",
            "RDustEffectsAir"
        ],
        [
            "GdtVolcano",
            "RDustEffectsAir"
        ],
        [
            "GdtVolcano",
            "RStonesEffects"
        ],
        [
            "GdtCliff",
            "RDustEffectsAir"
        ],
        [
            "GdtVolcanoBeach",
            "RDustEffectsAir"
        ],
        [
            "SurfRoadDirt_exp",
            "RDustEffectsAirRed"
        ],
        [
            "SurfRoadConcrete_exp",
            "RDustEffectsAir"
        ],
        [
            "SurfRoadTarmac_exp",
            "RDustEffectsAir"
        ],
        [
            "GdtStratisConcrete",
            "RDustEffectsAir"
        ],
        [
            "GdtStratisConcrete",
            "RDirtEffects"
        ],
        [
            "GdtStratisBeach",
            "RDustEffectsAir"
        ],
        [
            "GdtStratisBeach",
            "RStonesEffects"
        ],
        [
            "GdtStratisDirt",
            "RDustEffectsAir"
        ],
        [
            "GdtStratisDirt",
            "RDirtEffects"
        ],
        [
            "GdtStratisSeabedCluttered",
            "RDustEffectsAir"
        ],
        [
            "GdtStratisSeabed",
            "RDustEffectsAir"
        ],
        [
            "GdtStratisDryGrass",
            "RDustEffectsAir"
        ],
        [
            "GdtStratisDryGrass",
            "RGrassDryEffects"
        ],
        [
            "GdtStratisDryGrass",
            "RDirtEffects"
        ],
        [
            "GdtStratisGreenGrass",
            "RDustEffectsAir"
        ],
        [
            "GdtStratisGreenGrass",
            "RGrassEffects"
        ],
        [
            "GdtStratisGreenGrass",
            "RDirtEffects"
        ],
        [
            "GdtStratisRocky",
            "RDustEffectsAir"
        ],
        [
            "GdtStratisRocky",
            "RGrassEffects"
        ],
        [
            "GdtStratisRocky",
            "RDirtEffects"
        ],
        [
            "GdtStratisThistles",
            "RDustEffectsAir"
        ],
        [
            "GdtStratisThistles",
            "RGrassEffects"
        ],
        [
            "GdtStratisThistles",
            "RDirtEffects"
        ],
        [
            "GdtConcrete",
            "RDustEffectsAir"
        ],
        [
            "GdtConcrete",
            "RDirtEffects"
        ],
        [
            "GdtAsphalt",
            "RDustEffectsAir"
        ],
        [
            "GdtAsphalt",
            "RDirtEffects"
        ],
        [
            "GdtRubble",
            "RDustEffectsAir"
        ],
        [
            "GdtRubble",
            "RDirtEffects"
        ],
        [
            "GdtSoil",
            "RDustEffectsAir"
        ],
        [
            "GdtSoil",
            "RDirtEffects"
        ],
        [
            "GdtBeach",
            "RDustEffectsAir"
        ],
        [
            "GdtBeach",
            "RStonesEffects"
        ],
        [
            "GdtRock",
            "RDustEffectsAir"
        ],
        [
            "GdtRock",
            "RDirtEffects"
        ],
        [
            "GdtDead",
            "RDustEffectsAir"
        ],
        [
            "GdtDead",
            "RDirtEffects"
        ],
        [
            "Default",
            "RDustEffectsAir"
        ],
        [
            "GdtDesert1",
            "RDustEffectsAir"
        ],
        [
            "GdtDesert1",
            "RSandEffects"
        ],
        [
            "GdtDesert1",
            "RDirtEffects"
        ],
        [
            "GdtDesert1",
            "RStonesEffects"
        ],
        [
            "GdtDesert2",
            "RDustEffectsAir"
        ],
        [
            "GdtDesert2",
            "RSandEffects"
        ],
        [
            "GdtDesert2",
            "RGrassEffects"
        ],
        [
            "GdtDesert2",
            "RDirtEffects"
        ],
        [
            "GdtDirt",
            "RDustEffectsAir"
        ],
        [
            "GdtDirt",
            "RDirtEffects"
        ],
        [
            "GdtGrassGreen",
            "RDustEffectsAir"
        ],
        [
            "GdtGrassGreen",
            "RGrassEffects"
        ],
        [
            "GdtGrassGreen",
            "RDirtEffects"
        ],
        [
            "GdtGrassDry",
            "RDustEffectsAir"
        ],
        [
            "GdtGrassDry",
            "RGrassDryEffects"
        ],
        [
            "GdtGrassDry",
            "RDirtEffects"
        ],
        [
            "GdtGrassWild",
            "RDustEffectsAir"
        ],
        [
            "GdtGrassWild",
            "RGrassEffects"
        ],
        [
            "GdtGrassWild",
            "RDirtEffects"
        ],
        [
            "GdtWildField",
            "RDustEffectsAir"
        ],
        [
            "GdtWildField",
            "RGrassEffects"
        ],
        [
            "GdtWildField",
            "RDirtEffects"
        ],
        [
            "GdtWeed1",
            "RDustEffectsAir"
        ],
        [
            "GdtWeed1",
            "RGrassEffects"
        ],
        [
            "GdtWeed1",
            "RDirtEffects"
        ],
        [
            "GdtWeed2",
            "RDustEffectsAir"
        ],
        [
            "GdtWeed2",
            "RGrassEffects"
        ],
        [
            "GdtWeed2",
            "RDirtEffects"
        ],
        [
            "GdtThorn",
            "RDustEffectsAir"
        ],
        [
            "GdtThorn",
            "RGrassEffects"
        ],
        [
            "GdtThorn",
            "RDirtEffects"
        ],
        [
            "GdtStony",
            "RDustEffectsAir"
        ],
        [
            "GdtStony",
            "RGrassEffects"
        ],
        [
            "GdtStony",
            "RDirtEffects"
        ],
        [
            "GdtStonyGreen",
            "RDustEffectsAir"
        ],
        [
            "GdtStonyGreen",
            "RGrassEffects"
        ],
        [
            "GdtStonyGreen",
            "RDirtEffects"
        ],
        [
            "GdtStonyThistle",
            "RDustEffectsAir"
        ],
        [
            "GdtStonyThistle",
            "RGrassEffects"
        ],
        [
            "GdtStonyThistle",
            "RDirtEffects"
        ],
        [
            "GdtSeabedDeep",
            "RDustEffectsAir"
        ],
        [
            "GdtSeabed",
            "RDustEffectsAir"
        ],
        [
            "SurfRoadDirt",
            "RDustEffectsAir"
        ],
        [
            "SurfRoadConcrete",
            "RDustEffectsAir"
        ],
        [
            "SurfRoadTarmac",
            "RDustEffectsAir"
        ],
        [
            "SurfWood",
            "RDustEffectsAir"
        ],
        [
            "SurfMetal",
            "RDustEffectsAir"
        ],
        [
            "SurfRoofTin",
            "RDustEffectsAir"
        ],
        [
            "SurfRoofTiles",
            "RDustEffectsAir"
        ],
        [
            "SurfIntWood",
            "RDustEffectsAir"
        ],
        [
            "SurfIntConcrete",
            "RDustEffectsAir"
        ],
        [
            "SurfIntTiles",
            "RDustEffectsAir"
        ],
        [
            "SurfIntMetal",
            "RDustEffectsAir"
        ]
    ],
    "ruddercoef": [],
    "ruddercontrolssensitivitycoef": 4,
    "rudderinfluence": 0.5,
    "scope": 2,
    "secondaryexplosion": -1,
    "selectionbacklights": "zadni svetlo",
    "selectionclan": "clan",
    "selectiondamage": "zbytek",
    "selectiondashboard": "podsvit pristroju",
    "selectionfireanim": "zasleh",
    "selectionleftoffset": "",
    "selectionrightoffset": "",
    "selectionrotormove": "vrtule blur",
    "selectionrotorstill": "vrtule staticka",
    "selectionshowdamage": "poskozeni",
    "sensitivity": 2.5,
    "sensitivityear": 0.0075,
    "shadow": 1,
    "showalltargets": 0,
    "showcrewaim": 0,
    "shownunderwaterselections": [],
    "shownvgcargo": [
        0
    ],
    "shownvgcommander": 0,
    "shownvgdriver": 0,
    "shownvggunner": 0,
    "side": 1,
    "simulation": "airplaneX",
    "slingloadcargomemorypoints": [],
    "slingloadcargomemorypointsdir": [],
    "slowspeedforwardcoef": 0.3,
    "soundarmorcrash": [
        "emptySound",
        0
    ],
    "soundattenuationcargo": [
        1
    ],
    "soundbreath": {},
    "soundbreathautomatic": {},
    "soundbreathinjured": {},
    "soundbreathswimming": {},
    "soundbuildingcrash": [
        "emptySound",
        0
    ],
    "soundburning": {},
    "soundbushcrash": [
        "emptySound",
        0
    ],
    "soundchoke": {},
    "soundcrash": [
        "",
        0.316228,
        1
    ],
    "soundcrashes": [
        "soundCrash",
        1
    ],
    "sounddamage": [
        "",
        1,
        1
    ],
    "sounddammage": [
        "",
        0.562341,
        1
    ],
    "sounddrown": {},
    "sounddrowning": {},
    "soundelevation": [
        "",
        0.00316228,
        0.5
    ],
    "soundengine": [
        "",
        1,
        1
    ],
    "soundengineoffext": [
        "rhsgref/addons/rhsgref_air/AN2/data/sound/AN2_engine_stop_ext",
        0.398107,
        1,
        700
    ],
    "soundengineoffint": [
        "rhsgref/addons/rhsgref_air/AN2/data/sound/AN2_engine_stop_int",
        0.177828,
        1
    ],
    "soundengineonext": [
        "rhsgref/addons/rhsgref_air/AN2/data/sound/AN2_engine_start_ext",
        0.398107,
        1,
        700
    ],
    "soundengineonint": [
        "rhsgref/addons/rhsgref_air/AN2/data/sound/AN2_engine_start_int",
        0.177828,
        1
    ],
    "soundenviron": [
        "",
        1,
        1
    ],
    "soundenvironext": {},
    "soundequipment": {},
    "soundevents": {},
    "soundflapsdown": [
        "",
        1,
        1
    ],
    "soundflapsup": [
        "",
        1,
        1
    ],
    "soundgear": {},
    "soundgeardown": [
        "",
        1,
        1
    ],
    "soundgearup": [
        "",
        1,
        1
    ],
    "soundgetin": [
        "rhsgref/addons/rhsgref_air/AN2/data/sound/close",
        0.316228,
        1
    ],
    "soundgetout": [
        "rhsgref/addons/rhsgref_air/AN2/data/sound/open",
        0.316228,
        1,
        40
    ],
    "soundhitscream": {},
    "soundincommingmissile": [
        "/A3/Sounds_F/weapons/Rockets/locked_3",
        0.1,
        1.5
    ],
    "soundinjured": {},
    "soundlandcrash": [
        "",
        1,
        1
    ],
    "soundlandcrashes": [
        "soundLandCrash",
        1
    ],
    "soundlocked": [
        "/A3/Sounds_F/weapons/Rockets/locked_1",
        0.1,
        1
    ],
    "soundrecovered": {},
    "sounds": {
        "enginehighin": {
            "frequency": "1",
            "sound": [
                "rhsgref/addons/rhsgref_air/AN2/data/sound/AN2_engine_high_int",
                1,
                1
            ],
            "volume": "(1-camPos)*(engineOn*(rpm factor[0.55, 1.0]))"
        },
        "enginehighout": {
            "frequency": "1",
            "sound": [
                "rhsgref/addons/rhsgref_air/AN2/data/sound/AN2_engine_high_ext",
                1.77828,
                1,
                1100
            ],
            "volume": "camPos*engineOn*(rpm factor[0.55, 1.0])"
        },
        "enginelowin": {
            "frequency": "1.0 min (rpm + 0.5)",
            "sound": [
                "rhsgref/addons/rhsgref_air/AN2/data/sound/AN2_engine_low_int",
                1,
                1
            ],
            "volume": "(1-camPos)*(engineOn*(rpm factor[0.85, 0]))"
        },
        "enginelowout": {
            "frequency": "1.0 min (rpm + 0.5)",
            "sound": [
                "rhsgref/addons/rhsgref_air/AN2/data/sound/AN2_engine_low_ext",
                1.77828,
                1,
                900
            ],
            "volume": "camPos*engineOn*(rpm factor[0.85, 0])"
        },
        "forsagein": {
            "frequency": "1",
            "sound": [
                "rhsgref/addons/rhsgref_air/AN2/data/sound/AN2_engine_high_int",
                1.41254,
                1.1
            ],
            "volume": "(1-camPos)*(engineOn*(thrust factor[0.5, 1.0]))"
        },
        "forsageout": {
            "cone": [
                1.14,
                3.92,
                2,
                0.4
            ],
            "frequency": "1",
            "sound": [
                "rhsgref/addons/rhsgref_air/AN2/data/sound/AN2_engine_high_ext",
                1.41254,
                1,
                1500
            ],
            "volume": "camPos*engineOn*(thrust factor[0.5, 1.0])"
        },
        "windnoisein": {
            "frequency": "(0.1+(1.2*(speed factor[1, 100])))",
            "sound": [
                "rhsgref/addons/rhsgref_air/AN2/data/sound/int-wind",
                0.001,
                0.6
            ],
            "volume": "(1-camPos)*(speed factor[1, 100])"
        },
        "windnoiseout": {
            "frequency": "(0.1+(1.2*(speed factor[1, 100])))",
            "sound": [
                "rhsgref/addons/rhsgref_air/AN2/data/sound/ext-wind",
                0.001,
                0.6,
                150
            ],
            "volume": "camPos*(speed factor[1, 100])"
        }
    },
    "soundservo": [
        "",
        0.00316228,
        0.5
    ],
    "soundturnin": [
        "",
        0.000316228,
        1
    ],
    "soundturnininternal": [
        "",
        0.000316228,
        1
    ],
    "soundturnout": [
        "",
        0.000316228,
        1
    ],
    "soundturnoutinternal": [
        "",
        0.000316228,
        1
    ],
    "soundwatercrash": [
        "",
        0.177828,
        1
    ],
    "soundwatercrashes": [
        "soundWaterCrash",
        1
    ],
    "soundwoodcrash": [
        "emptySound",
        0
    ],
    "speechplural": [],
    "speechsingular": [],
    "speechvariants": {
        "default": {
            "speechplural": [
                "veh_air_plane_p"
            ],
            "speechsingular": [
                "veh_air_plane_s"
            ]
        }
    },
    "spotabledarknightlightsoff": 0.001,
    "spotablenightlightsoff": 0.02,
    "spotablenightlightson": 4,
    "squadtitles": {
        "color": [
            0,
            0,
            0,
            0.75
        ],
        "name": "clan_sign"
    },
    "stallwarningtreshold": 0.2,
    "steeraheadplan": 2,
    "steeraheadsimul": 1,
    "supplyradius": 2,
    "tailhook": 0,
    "takeoffspeed": 90,
    "tbody": 150,
    "textplural": "fast movers",
    "textsingular": "fast mover",
    "texturelist": [],
    "texturesources": {
        "aeroschrot": {
            "author": "Bohemia Interactive",
            "displayname": "\u0410\u044d\u0440\u043e\u0428\u0440\u043e\u0442",
            "factions": [],
            "textures": [
                "rhsgref/addons/rhsgref_air/AN2/data/an2_1_A_CO",
                "rhsgref/addons/rhsgref_air/AN2/data/an2_2_A_CO",
                "rhsgref/addons/rhsgref_air/AN2/data/an2_wings_A_CO"
            ]
        },
        "airtak": {
            "author": "Bohemia Interactive",
            "displayname": "AirTak",
            "factions": [],
            "textures": [
                "rhsgref/addons/rhsgref_air/AN2/data/an2_1_B_CO",
                "rhsgref/addons/rhsgref_air/AN2/data/an2_2_B_CO",
                "rhsgref/addons/rhsgref_air/AN2/data/an2_wings_B_CO"
            ]
        },
        "military": {
            "author": "Bohemia Interactive",
            "displayname": "Military",
            "factions": [],
            "textures": [
                "rhsgref/addons/rhsgref_air/AN2/data/an2_1_CO",
                "rhsgref/addons/rhsgref_air/AN2/data/an2_2_CO",
                "rhsgref/addons/rhsgref_air/AN2/data/an2_wings_CO"
            ]
        },
        "standardcdf": {
            "author": "Red Hammer Studios",
            "displayname": "CDF",
            "factions": [
                "rhsgref_faction_cdf_air"
            ],
            "textures": [
                "rhsgref/addons/rhsgref_air/an2/data/an2_1_co.paa",
                "rhsgref/addons/rhsgref_air/an2/data/an2_2_co.paa",
                "rhsgref/addons/rhsgref_air/an2/data/an2_wings_co.paa"
            ]
        }
    },
    "threat": [
        0,
        0,
        0
    ],
    "thrustcoef": [
        1.4,
        1.3,
        1.2,
        1.2,
        1.1,
        1.1,
        1,
        1,
        0.9,
        0.7,
        0.5,
        0.3,
        0.1,
        0,
        0,
        0
    ],
    "tracksspeed": 0,
    "transportammo": 0,
    "transportbackpacks": {
        "_xx_b_parachute": {
            "backpack": "B_Parachute",
            "count": 16
        }
    },
    "transportfuel": 0,
    "transportitems": {
        "_xx_firstaidkit": {
            "count": 20,
            "name": "FirstAidKit"
        },
        "_xx_medikit": {
            "count": 5,
            "name": "Medikit"
        }
    },
    "transportmagazines": {},
    "transportmaxbackpacks": 6,
    "transportmaxmagazines": 24,
    "transportmaxweapons": 6,
    "transportrepair": 0,
    "transportsoldier": 12,
    "transportvehiclescount": 0,
    "transportvehiclesmass": 0,
    "transportweapons": {},
    "turncoef": 1.5,
    "turrets": {
        "copilotturret": {
            "aggregatereflectors": [],
            "allowlauncherin": 0,
            "allowlauncherout": 0,
            "allowtablock": 1,
            "animationsourcebody": "",
            "animationsourcecamelev": "camElev",
            "animationsourcegun": "",
            "animationsourcehatch": "hatchGunner",
            "armorlights": 0.4,
            "body": "",
            "caneject": 1,
            "canhidegunner": -1,
            "canusescanners": 1,
            "castgunnershadow": 0,
            "commanding": -1,
            "disablesoundattenuation": 0,
            "dontcreateai": 0,
            "ejectdeadgunner": 0,
            "forcehidegunner": 0,
            "forcenvg": 0,
            "gun": "",
            "gunbeg": "usti hlavne",
            "gunclouds": {
                "access": 0,
                "cloudletaccy": 0.4,
                "cloudletalpha": 1,
                "cloudletanimperiod": 1,
                "cloudletcolor": [
                    1,
                    1,
                    1,
                    0
                ],
                "cloudletduration": 0.3,
                "cloudletfadein": 0.01,
                "cloudletfadeout": 1,
                "cloudletgrowup": 1,
                "cloudletmaxyspeed": 0.8,
                "cloudletminyspeed": 0.2,
                "cloudletshape": "cloudletClouds",
                "cloudletsize": 1,
                "deltat": 0,
                "initt": 0,
                "interval": 0.05,
                "size": 3,
                "sourcesize": 0.5,
                "table": {
                    "t0": {
                        "color": [
                            1,
                            1,
                            1,
                            0
                        ],
                        "maxt": 0
                    }
                },
                "timetolive": 0
            },
            "gunend": "konec hlavne",
            "gunfire": {
                "access": 0,
                "cloudletaccy": 0,
                "cloudletalpha": 1,
                "cloudletanimperiod": 1,
                "cloudletcolor": [
                    1,
                    1,
                    1,
                    0
                ],
                "cloudletduration": 0.2,
                "cloudletfadein": 0.01,
                "cloudletfadeout": 0.5,
                "cloudletgrowup": 0.2,
                "cloudletmaxyspeed": 100,
                "cloudletminyspeed": -100,
                "cloudletshape": "cloudletFire",
                "cloudletsize": 1,
                "deltat": -3000,
                "initt": 4500,
                "interval": 0.01,
                "size": 3,
                "sourcesize": 0.5,
                "table": {
                    "t0": {
                        "color": [
                            0.82,
                            0.95,
                            0.93,
                            0
                        ],
                        "maxt": 0
                    },
                    "t1": {
                        "color": [
                            0.75,
                            0.77,
                            0.9,
                            0
                        ],
                        "maxt": 200
                    },
                    "t10": {
                        "color": [
                            0.62,
                            0.29,
                            0.03,
                            0
                        ],
                        "maxt": 2600
                    },
                    "t11": {
                        "color": [
                            0.59,
                            0.35,
                            0.05,
                            0
                        ],
                        "maxt": 2650
                    },
                    "t12": {
                        "color": [
                            0.75,
                            0.37,
                            0.03,
                            0
                        ],
                        "maxt": 2700
                    },
                    "t13": {
                        "color": [
                            0.88,
                            0.34,
                            0.03,
                            0
                        ],
                        "maxt": 2750
                    },
                    "t14": {
                        "color": [
                            0.91,
                            0.5,
                            0.17,
                            0
                        ],
                        "maxt": 2800
                    },
                    "t15": {
                        "color": [
                            1,
                            0.6,
                            0.2,
                            0
                        ],
                        "maxt": 2850
                    },
                    "t16": {
                        "color": [
                            1,
                            0.71,
                            0.3,
                            0
                        ],
                        "maxt": 2900
                    },
                    "t17": {
                        "color": [
                            0.98,
                            0.83,
                            0.41,
                            0
                        ],
                        "maxt": 2950
                    },
                    "t18": {
                        "color": [
                            0.98,
                            0.91,
                            0.54,
                            0
                        ],
                        "maxt": 3000
                    },
                    "t19": {
                        "color": [
                            0.98,
                            0.99,
                            0.6,
                            0
                        ],
                        "maxt": 3100
                    },
                    "t2": {
                        "color": [
                            0.56,
                            0.62,
                            0.67,
                            0
                        ],
                        "maxt": 400
                    },
                    "t20": {
                        "color": [
                            0.96,
                            0.99,
                            0.72,
                            0
                        ],
                        "maxt": 3300
                    },
                    "t21": {
                        "color": [
                            1,
                            0.98,
                            0.91,
                            0
                        ],
                        "maxt": 3600
                    },
                    "t22": {
                        "color": [
                            1,
                            1,
                            1,
                            0
                        ],
                        "maxt": 4200
                    },
                    "t3": {
                        "color": [
                            0.39,
                            0.46,
                            0.47,
                            0
                        ],
                        "maxt": 600
                    },
                    "t4": {
                        "color": [
                            0.24,
                            0.31,
                            0.31,
                            0
                        ],
                        "maxt": 800
                    },
                    "t5": {
                        "color": [
                            0.23,
                            0.31,
                            0.29,
                            0
                        ],
                        "maxt": 1000
                    },
                    "t6": {
                        "color": [
                            0.21,
                            0.29,
                            0.27,
                            0
                        ],
                        "maxt": 1500
                    },
                    "t7": {
                        "color": [
                            0.19,
                            0.23,
                            0.21,
                            0
                        ],
                        "maxt": 2000
                    },
                    "t8": {
                        "color": [
                            0.22,
                            0.19,
                            0.1,
                            0
                        ],
                        "maxt": 2300
                    },
                    "t9": {
                        "color": [
                            0.35,
                            0.2,
                            0.02,
                            0
                        ],
                        "maxt": 2500
                    }
                },
                "timetolive": 0
            },
            "gunneraction": "ManActTestDriver",
            "gunnercompartments": "Compartment1",
            "gunnerdoor": "",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 0,
            "gunnergetinaction": "GetInHigh",
            "gunnergetoutaction": "GetOutHigh",
            "gunnerinaction": "ManActTestDriver",
            "gunnerlefthandanimname": "",
            "gunnerleftleganimname": "",
            "gunnername": "Copilot",
            "gunnernotspawned": 1,
            "gunneropticscolor": [
                0,
                0,
                0,
                1
            ],
            "gunneropticseffect": [],
            "gunneropticsmodel": "",
            "gunneropticsshowcursor": 0,
            "gunneroutfirealsoininternalcamera": 1,
            "gunneroutforceoptics": 0,
            "gunneroutopticscolor": [
                0,
                0,
                0,
                1
            ],
            "gunneroutopticseffect": [],
            "gunneroutopticsmodel": "",
            "gunneroutopticsshowcursor": 0,
            "gunnerrighthandanimname": "",
            "gunnerrightleganimname": "",
            "gunnertype": "",
            "gunnerusespilotview": 1,
            "hasgunner": 1,
            "hideweaponsgunner": 1,
            "hitpoints": {
                "hitgun": {
                    "armor": 0.6,
                    "explosionshielding": 1,
                    "material": 52,
                    "name": "gun",
                    "passthrough": 1,
                    "visual": "gun"
                },
                "hitturret": {
                    "armor": 0.8,
                    "explosionshielding": 1,
                    "material": 51,
                    "name": "turret",
                    "passthrough": 1,
                    "visual": "turret"
                }
            },
            "ingunnermayfire": 1,
            "initcamelev": 0,
            "initelev": 11,
            "initoutelev": 0,
            "initoutturn": 0,
            "initturn": 0,
            "iscopilot": 0,
            "lockwhendriverout": 0,
            "lockwhenvehiclespeed": -1,
            "lodturnedin": -1,
            "lodturnedout": -1,
            "magazines": [],
            "maxcamelev": 90,
            "maxelev": 30,
            "maxhorizontalrotspeed": 3,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": 170,
            "maxverticalrotspeed": 3,
            "memorypointgun": "kulas",
            "memorypointgunneroptics": "gunnerview",
            "memorypointgunneroutoptics": "",
            "memorypointsgetingunner": "pos codriver",
            "memorypointsgetingunnerdir": "pos codriver dir",
            "memorypointsgetingunnerprecise": "",
            "mgunclouds": {
                "access": 0,
                "cloudletaccy": 0,
                "cloudletalpha": 0.3,
                "cloudletanimperiod": 1,
                "cloudletcolor": [
                    1,
                    1,
                    1,
                    0
                ],
                "cloudletduration": 0.05,
                "cloudletfadein": 0,
                "cloudletfadeout": 0.1,
                "cloudletgrowup": 0.05,
                "cloudletmaxyspeed": 100,
                "cloudletminyspeed": -100,
                "cloudletshape": "cloudletClouds",
                "cloudletsize": 1,
                "deltat": 0,
                "initt": 0,
                "interval": 0.02,
                "size": 0.3,
                "sourcesize": 0.02,
                "table": {
                    "t0": {
                        "color": [
                            1,
                            1,
                            1,
                            0
                        ],
                        "maxt": 0
                    }
                },
                "timetolive": 0
            },
            "mincamelev": -90,
            "minelev": -50,
            "minoutelev": -4,
            "minoutturn": -60,
            "minturn": -170,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "outgunnermayfire": 0,
            "playerposition": 0,
            "precisegetinout": 0,
            "primary": 1,
            "primarygunner": 0,
            "primaryobserver": 0,
            "proxyindex": 1,
            "proxytype": "CPGunner",
            "reflectors": {},
            "selectionfireanim": "zasleh",
            "showalltargets": 0,
            "showcrewaim": 0,
            "showhmd": 0,
            "slingloadoperator": 0,
            "soundelevation": [
                "",
                0.00316228,
                1
            ],
            "soundservo": [
                "",
                0.00316228,
                1
            ],
            "stabilizedinaxes": 3,
            "startengine": 0,
            "turnin": {
                "turnoffset": 0
            },
            "turnout": {
                "turnoffset": 0
            },
            "turretcansee": "1 + 2 + 4 + 8 + 32",
            "turretfollowfreelook": 0,
            "turretinfotype": "",
            "turrets": {},
            "turretspec": {
                "showheadphones": 0
            },
            "viewgunner": {
                "initanglex": 0,
                "initangley": 0,
                "initfov": 0.75,
                "maxanglex": 85,
                "maxangley": 150,
                "maxfov": 1.25,
                "maxmovex": 0.2,
                "maxmovey": 0.1,
                "maxmovez": 0.2,
                "minanglex": -65,
                "minangley": -150,
                "minfov": 0.25,
                "minmovex": -0.2,
                "minmovey": -0.1,
                "minmovez": -0.1,
                "speedzoommaxfov": 0,
                "speedzoommaxspeed": 10000000000.0
            },
            "viewgunnerinexternal": 0,
            "viewgunnershadow": 1,
            "viewgunnershadowamb": 1,
            "viewgunnershadowdiff": 1,
            "viewoptics": {
                "initanglex": 0,
                "initangley": 0,
                "initfov": 0.3,
                "maxanglex": 30,
                "maxangley": 100,
                "maxfov": 0.35,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": -30,
                "minangley": -100,
                "minfov": 0.07,
                "minmovex": 0,
                "minmovey": 0,
                "minmovez": 0,
                "speedzoommaxfov": 0,
                "speedzoommaxspeed": 10000000000.0
            },
            "weapons": []
        },
        "mainturret": {
            "aggregatereflectors": [],
            "allowlauncherin": 0,
            "allowlauncherout": 0,
            "allowtablock": 1,
            "animationsourcebody": "",
            "animationsourcecamelev": "camElev",
            "animationsourcegun": "",
            "animationsourcehatch": "hatchGunner",
            "armorlights": 0.4,
            "body": "",
            "caneject": 0,
            "canhidegunner": -1,
            "canusescanners": 1,
            "castgunnershadow": 1,
            "commanding": -1,
            "components": {
                "vehiclesystemsdisplaymanagercomponentleft": {
                    "components": {
                        "crewdisplay": {
                            "componenttype": "CrewDisplayComponent",
                            "resource": "RscCustomInfoCrew"
                        },
                        "emptydisplay": {
                            "componenttype": "EmptyDisplayComponent"
                        },
                        "minedetectordisplay": {
                            "componenttype": "MineDetectorDisplayComponent"
                        },
                        "minimapdisplay": {
                            "componenttype": "MinimapDisplayComponent"
                        },
                        "slingloaddisplay": {
                            "componenttype": "SlingLoadDisplayComponent"
                        },
                        "uavdisplay": {
                            "componenttype": "UAVFeedDisplayComponent"
                        }
                    },
                    "componenttype": "VehicleSystemsDisplayManager",
                    "defaultdisplay": "EmptyDisplay",
                    "left": 1,
                    "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,\t(safezoneX + 0.5 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40))])",
                    "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,\t(safezoneY + safezoneH - 21 * \t\t\t(\t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                },
                "vehiclesystemsdisplaymanagercomponentright": {
                    "components": {
                        "crewdisplay": {
                            "componenttype": "CrewDisplayComponent",
                            "resource": "RscCustomInfoCrew"
                        },
                        "emptydisplay": {
                            "componenttype": "EmptyDisplayComponent"
                        },
                        "minedetectordisplay": {
                            "componenttype": "MineDetectorDisplayComponent"
                        },
                        "minimapdisplay": {
                            "componenttype": "MinimapDisplayComponent"
                        },
                        "slingloaddisplay": {
                            "componenttype": "SlingLoadDisplayComponent"
                        },
                        "uavdisplay": {
                            "componenttype": "UAVFeedDisplayComponent"
                        }
                    },
                    "componenttype": "VehicleSystemsDisplayManager",
                    "defaultdisplay": "",
                    "right": 1,
                    "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,\t((safezoneX + safezoneW) - (\t\t(10 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40)))])",
                    "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,\t(safezoneY + safezoneH - 21 * \t\t\t(\t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                }
            },
            "disablesoundattenuation": 0,
            "dontcreateai": 0,
            "ejectdeadgunner": 0,
            "enablemanualfire": 0,
            "forcehidegunner": 0,
            "forcenvg": 0,
            "gun": "",
            "gunbeg": "usti hlavne",
            "gunclouds": {
                "access": 0,
                "cloudletaccy": 0.4,
                "cloudletalpha": 1,
                "cloudletanimperiod": 1,
                "cloudletcolor": [
                    1,
                    1,
                    1,
                    0
                ],
                "cloudletduration": 0.3,
                "cloudletfadein": 0.01,
                "cloudletfadeout": 1,
                "cloudletgrowup": 1,
                "cloudletmaxyspeed": 0.8,
                "cloudletminyspeed": 0.2,
                "cloudletshape": "cloudletClouds",
                "cloudletsize": 1,
                "deltat": 0,
                "initt": 0,
                "interval": 0.05,
                "size": 3,
                "sourcesize": 0.5,
                "table": {
                    "t0": {
                        "color": [
                            1,
                            1,
                            1,
                            0
                        ],
                        "maxt": 0
                    }
                },
                "timetolive": 0
            },
            "gunend": "konec hlavne",
            "gunfire": {
                "access": 0,
                "cloudletaccy": 0,
                "cloudletalpha": 1,
                "cloudletanimperiod": 1,
                "cloudletcolor": [
                    1,
                    1,
                    1,
                    0
                ],
                "cloudletduration": 0.2,
                "cloudletfadein": 0.01,
                "cloudletfadeout": 0.5,
                "cloudletgrowup": 0.2,
                "cloudletmaxyspeed": 100,
                "cloudletminyspeed": -100,
                "cloudletshape": "cloudletFire",
                "cloudletsize": 1,
                "deltat": -3000,
                "initt": 4500,
                "interval": 0.01,
                "size": 3,
                "sourcesize": 0.5,
                "table": {
                    "t0": {
                        "color": [
                            0.82,
                            0.95,
                            0.93,
                            0
                        ],
                        "maxt": 0
                    },
                    "t1": {
                        "color": [
                            0.75,
                            0.77,
                            0.9,
                            0
                        ],
                        "maxt": 200
                    },
                    "t10": {
                        "color": [
                            0.62,
                            0.29,
                            0.03,
                            0
                        ],
                        "maxt": 2600
                    },
                    "t11": {
                        "color": [
                            0.59,
                            0.35,
                            0.05,
                            0
                        ],
                        "maxt": 2650
                    },
                    "t12": {
                        "color": [
                            0.75,
                            0.37,
                            0.03,
                            0
                        ],
                        "maxt": 2700
                    },
                    "t13": {
                        "color": [
                            0.88,
                            0.34,
                            0.03,
                            0
                        ],
                        "maxt": 2750
                    },
                    "t14": {
                        "color": [
                            0.91,
                            0.5,
                            0.17,
                            0
                        ],
                        "maxt": 2800
                    },
                    "t15": {
                        "color": [
                            1,
                            0.6,
                            0.2,
                            0
                        ],
                        "maxt": 2850
                    },
                    "t16": {
                        "color": [
                            1,
                            0.71,
                            0.3,
                            0
                        ],
                        "maxt": 2900
                    },
                    "t17": {
                        "color": [
                            0.98,
                            0.83,
                            0.41,
                            0
                        ],
                        "maxt": 2950
                    },
                    "t18": {
                        "color": [
                            0.98,
                            0.91,
                            0.54,
                            0
                        ],
                        "maxt": 3000
                    },
                    "t19": {
                        "color": [
                            0.98,
                            0.99,
                            0.6,
                            0
                        ],
                        "maxt": 3100
                    },
                    "t2": {
                        "color": [
                            0.56,
                            0.62,
                            0.67,
                            0
                        ],
                        "maxt": 400
                    },
                    "t20": {
                        "color": [
                            0.96,
                            0.99,
                            0.72,
                            0
                        ],
                        "maxt": 3300
                    },
                    "t21": {
                        "color": [
                            1,
                            0.98,
                            0.91,
                            0
                        ],
                        "maxt": 3600
                    },
                    "t22": {
                        "color": [
                            1,
                            1,
                            1,
                            0
                        ],
                        "maxt": 4200
                    },
                    "t3": {
                        "color": [
                            0.39,
                            0.46,
                            0.47,
                            0
                        ],
                        "maxt": 600
                    },
                    "t4": {
                        "color": [
                            0.24,
                            0.31,
                            0.31,
                            0
                        ],
                        "maxt": 800
                    },
                    "t5": {
                        "color": [
                            0.23,
                            0.31,
                            0.29,
                            0
                        ],
                        "maxt": 1000
                    },
                    "t6": {
                        "color": [
                            0.21,
                            0.29,
                            0.27,
                            0
                        ],
                        "maxt": 1500
                    },
                    "t7": {
                        "color": [
                            0.19,
                            0.23,
                            0.21,
                            0
                        ],
                        "maxt": 2000
                    },
                    "t8": {
                        "color": [
                            0.22,
                            0.19,
                            0.1,
                            0
                        ],
                        "maxt": 2300
                    },
                    "t9": {
                        "color": [
                            0.35,
                            0.2,
                            0.02,
                            0
                        ],
                        "maxt": 2500
                    }
                },
                "timetolive": 0
            },
            "gunneraction": "RHS_AN2_Cargo",
            "gunnercompartments": "Compartment1",
            "gunnerdoor": "",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 0,
            "gunnergetinaction": "GetInLow",
            "gunnergetoutaction": "GetOutLow",
            "gunnerinaction": "RHS_AN2_Cargo",
            "gunnerlefthandanimname": "yoke_copilot",
            "gunnerleftleganimname": "pedal_l_copilot",
            "gunnername": "Copilot",
            "gunnernotspawned": 0,
            "gunneropticscolor": [
                0,
                0,
                0,
                1
            ],
            "gunneropticseffect": [],
            "gunneropticsmodel": "A3/Weapons_F/empty.p3d",
            "gunneropticsshowcursor": 0,
            "gunneroutfirealsoininternalcamera": 1,
            "gunneroutforceoptics": 0,
            "gunneroutopticscolor": [
                0,
                0,
                0,
                1
            ],
            "gunneroutopticseffect": [],
            "gunneroutopticsmodel": "",
            "gunneroutopticsshowcursor": 0,
            "gunnerrighthandanimname": "right_stick_aileron",
            "gunnerrightleganimname": "pedal_r_copilot",
            "gunnertype": "",
            "gunnerusepilotview": 1,
            "gunnerusespilotview": 0,
            "hasgunner": 1,
            "hideweaponsgunner": 1,
            "hitpoints": {},
            "ingunnermayfire": 1,
            "initcamelev": 0,
            "initelev": 11,
            "initoutelev": 0,
            "initoutturn": 0,
            "initturn": 0,
            "iscopilot": 1,
            "lockwhendriverout": 0,
            "lockwhenvehiclespeed": -1,
            "lodturnedin": 1100,
            "lodturnedout": 1100,
            "magazines": [],
            "maxcamelev": 90,
            "maxelev": 30,
            "maxhorizontalrotspeed": 1.2,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": 170,
            "maxverticalrotspeed": 1.2,
            "memorypointgun": "machinegun",
            "memorypointgunneroptics": "gunnerview",
            "memorypointgunneroutoptics": "",
            "memorypointsgetingunner": "pos driver",
            "memorypointsgetingunnerdir": "pos driver dir",
            "memorypointsgetingunnerprecise": "",
            "mgunclouds": {
                "access": 0,
                "cloudletaccy": 0,
                "cloudletalpha": 0.3,
                "cloudletanimperiod": 1,
                "cloudletcolor": [
                    1,
                    1,
                    1,
                    0
                ],
                "cloudletduration": 0.05,
                "cloudletfadein": 0,
                "cloudletfadeout": 0.1,
                "cloudletgrowup": 0.05,
                "cloudletmaxyspeed": 100,
                "cloudletminyspeed": -100,
                "cloudletshape": "cloudletClouds",
                "cloudletsize": 1,
                "deltat": 0,
                "initt": 0,
                "interval": 0.02,
                "size": 0.3,
                "sourcesize": 0.02,
                "table": {
                    "t0": {
                        "color": [
                            1,
                            1,
                            1,
                            0
                        ],
                        "maxt": 0
                    }
                },
                "timetolive": 0
            },
            "mincamelev": -90,
            "minelev": -50,
            "minoutelev": -4,
            "minoutturn": -60,
            "minturn": -170,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "outgunnermayfire": 1,
            "playerposition": 0,
            "precisegetinout": 0,
            "primary": 1,
            "primarygunner": 0,
            "primaryobserver": 0,
            "proxyindex": 1,
            "proxytype": "CPGunner",
            "reflectors": {},
            "selectionfireanim": "zasleh",
            "showalltargets": 0,
            "showcrewaim": 0,
            "showhmd": 0,
            "slingloadoperator": 0,
            "soundelevation": [
                "",
                0.00316228,
                1
            ],
            "soundservo": [
                "",
                0.00316228,
                1
            ],
            "stabilizedinaxes": 3,
            "startengine": 0,
            "turnin": {
                "turnoffset": 0
            },
            "turnout": {
                "turnoffset": 0
            },
            "turretcansee": 15,
            "turretfollowfreelook": 0,
            "turretinfotype": "",
            "turrets": {},
            "turretspec": {
                "showheadphones": 0
            },
            "viewgunner": {
                "continuous": 0,
                "initanglex": 5,
                "initangley": 0,
                "initfov": 0.75,
                "maxanglex": 85,
                "maxangley": 150,
                "maxfov": 1.25,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": -75,
                "minangley": -150,
                "minfov": 0.25,
                "minmovex": 0,
                "minmovey": 0,
                "minmovez": 0,
                "speedzoommaxfov": 0,
                "speedzoommaxspeed": 10000000000.0
            },
            "viewgunnerinexternal": 0,
            "viewgunnershadow": 1,
            "viewgunnershadowamb": 1,
            "viewgunnershadowdiff": 1,
            "viewoptics": {
                "initanglex": 0,
                "initangley": 0,
                "initfov": 0.3,
                "maxanglex": 30,
                "maxangley": 100,
                "maxfov": 0.35,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": -30,
                "minangley": -100,
                "minfov": 0.07,
                "minmovex": 0,
                "minmovey": 0,
                "minmovez": 0,
                "speedzoommaxfov": 0,
                "speedzoommaxspeed": 10000000000.0
            },
            "viewpilot": {
                "initanglex": 0,
                "initangley": 0,
                "initfov": 1,
                "maxanglex": 85,
                "maxangley": 150,
                "maxfov": 1.2,
                "maxmovex": 0.2,
                "maxmovey": 0.1,
                "maxmovez": 0.2,
                "minanglex": -65,
                "minangley": -150,
                "minfov": 0.3,
                "minmovex": -0.2,
                "minmovey": -0.1,
                "minmovez": -0.1,
                "speedzoommaxfov": 0,
                "speedzoommaxspeed": 10000000000.0
            },
            "weapons": []
        }
    },
    "type": 2,
    "typicalcargo": [
        "rhsgref_cdf_b_air_pilot"
    ],
    "uavhacker": 0,
    "unitinfotype": "RscUnitInfoAirPlane",
    "unitinfotypelite": 0,
    "unloadincombat": 0,
    "useprecisegetinaction": 0,
    "useractions": {
        "doorclose": {
            "condition": "this animationPhase 'door' == 1 && (alive this) && (player in crew this) && (this animationPhase 'hideDoor' < 0.5);",
            "displayname": "Close Doors",
            "displaynamedefault": "Close doors",
            "onlyforplayer": 1,
            "position": "cargo_door_handle",
            "radius": 2,
            "showwindow": 0,
            "statement": "this animate ['door',0, false];"
        },
        "dooropen": {
            "condition": "this animationPhase 'door' == 0 && (alive this) && (player in crew this) && (this animationPhase 'hideDoor' < 0.5);",
            "displayname": "Open Doors",
            "displaynamedefault": "Open doors",
            "onlyforplayer": 1,
            "position": "cargo_door_handle",
            "radius": 2,
            "showwindow": 0,
            "statement": "this animate ['door',1, false];"
        }
    },
    "vehicleclass": "rhs_vehclass_aircraft",
    "viewcargo": {
        "initanglex": 5,
        "initangley": 0,
        "initfov": 0.75,
        "maxanglex": 85,
        "maxangley": 150,
        "maxfov": 1.25,
        "maxmovex": 0,
        "maxmovey": 0,
        "maxmovez": 0,
        "minanglex": -75,
        "minangley": -150,
        "minfov": 0.25,
        "minmovex": 0,
        "minmovey": 0,
        "minmovez": 0,
        "speedzoommaxfov": 0,
        "speedzoommaxspeed": 10000000000.0
    },
    "viewcargoshadow": 1,
    "viewcargoshadowamb": 1,
    "viewcargoshadowdiff": 1,
    "viewdrivershadow": 1,
    "viewdrivershadowamb": 1,
    "viewdrivershadowdiff": 1,
    "viewoptics": {
        "initanglex": 0,
        "initangley": 0,
        "initfov": 0.5,
        "maxanglex": 0,
        "maxangley": 0,
        "maxfov": 0.5,
        "maxmovex": 0,
        "maxmovey": 0,
        "maxmovez": 0,
        "minanglex": 0,
        "minangley": 0,
        "minfov": 0.5,
        "minmovex": 0,
        "minmovey": 0,
        "minmovez": 0,
        "speedzoommaxfov": 0,
        "speedzoommaxspeed": 10000000000.0
    },
    "viewpilot": {
        "initanglex": 0,
        "initangley": 0,
        "initfov": 0.75,
        "maxanglex": 85,
        "maxangley": 150,
        "maxfov": 1.25,
        "maxmovex": 0.2,
        "maxmovey": 0.1,
        "maxmovez": 0.2,
        "minanglex": -65,
        "minangley": -150,
        "minfov": 0.25,
        "minmovex": -0.2,
        "minmovey": -0.1,
        "minmovez": -0.1,
        "speedzoommaxfov": 0,
        "speedzoommaxspeed": 10000000000.0
    },
    "visualtarget": 1,
    "visualtargetsize": 1,
    "vtol": 0,
    "vtolpitchinfluence": 2,
    "vtolrollinfluence": 2,
    "vtolyawinfluence": 2,
    "waterangulardampingcoef": 0,
    "waterdamageengine": 0.2,
    "watereffect": "HeliWater",
    "waterleakiness": 150,
    "waterlineardampingcoefx": 5,
    "waterlineardampingcoefy": 0,
    "waterppinvehicle": 1,
    "waterresistance": 1,
    "waterresistancecoef": 0.04,
    "weapons": [],
    "weaponsgroup1": "1 + \t\t2",
    "weaponsgroup2": 4,
    "weaponsgroup3": "8 + \t16 + \t32",
    "weaponsgroup4": "64 + \t\t128",
    "weaponslots": 0,
    "wheelcircumference": 1,
    "wheels": {
        "wheel_1": {
            "bonename": "Wheel_1_1",
            "boundary": "wheel_1_1_bound",
            "center": "wheel_1_1_center",
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "frictionvsslipgraph": [
                [
                    0,
                    2
                ],
                [
                    0.5,
                    1
                ],
                [
                    1,
                    1
                ]
            ],
            "latstiffx": 15,
            "latstiffy": 120,
            "longitudinalstiffnessperunitgravity": 90,
            "mass": 50,
            "maxbraketorque": 10,
            "maxcompression": 0.1,
            "maxdroop": 0.1,
            "maxhandbraketorque": 0,
            "moi": 8,
            "side": "left",
            "springdamperrate": 128000,
            "springstrength": 100000,
            "sprungmass": 2400,
            "steering": 1,
            "suspforceapppointoffset": "Wheel_1_1_center",
            "susptraveldirection": [
                0,
                -1,
                0
            ],
            "tireforceapppointoffset": "Wheel_1_1_center",
            "width": 0.3
        },
        "wheel_2": {
            "bonename": "wheel_1_2",
            "boundary": "wheel_1_2_bound",
            "center": "wheel_1_2_center",
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "frictionvsslipgraph": [
                [
                    0,
                    2
                ],
                [
                    0.5,
                    1
                ],
                [
                    1,
                    1
                ]
            ],
            "latstiffx": 15,
            "latstiffy": 120,
            "longitudinalstiffnessperunitgravity": 90,
            "mass": 50,
            "maxbraketorque": 10,
            "maxcompression": 0.1,
            "maxdroop": 0.1,
            "maxhandbraketorque": 0,
            "moi": 8,
            "side": "left",
            "springdamperrate": 128000,
            "springstrength": 100000,
            "sprungmass": 2400,
            "steering": 1,
            "suspforceapppointoffset": "Wheel_1_2_center",
            "susptraveldirection": [
                0,
                -1,
                0
            ],
            "tireforceapppointoffset": "Wheel_1_2_center",
            "width": 0.3
        },
        "wheel_3": {
            "bonename": "Wheel_2_1",
            "boundary": "wheel_2_1_bound",
            "center": "wheel_2_1_center",
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "frictionvsslipgraph": [
                [
                    0,
                    2
                ],
                [
                    0.5,
                    1
                ],
                [
                    1,
                    1
                ]
            ],
            "latstiffx": 15,
            "latstiffy": 120,
            "longitudinalstiffnessperunitgravity": 90,
            "mass": 50,
            "maxbraketorque": 10,
            "maxcompression": 0.1,
            "maxdroop": 0.1,
            "maxhandbraketorque": 0,
            "moi": 8,
            "side": "left",
            "springdamperrate": 12000,
            "springstrength": 1580000.0,
            "sprungmass": 700,
            "steering": 0,
            "suspforceapppointoffset": "Wheel_2_1_center",
            "susptraveldirection": [
                0,
                -1,
                0
            ],
            "tireforceapppointoffset": "Wheel_2_1_center",
            "width": 0.16
        }
    },
    "wheelsteeringsensitivity": 2,
    "windsockexist": 0,
    "wingvortices": {
        "bodyleft": {
            "effectname": "BodyVortices",
            "position": "body_vapour_L_S"
        },
        "bodylefttop": {
            "effectname": "BodyVortices",
            "position": "body_vapour_L_S_T"
        },
        "bodyright": {
            "effectname": "BodyVortices",
            "position": "body_vapour_R_S"
        },
        "bodyrighttop": {
            "effectname": "BodyVortices",
            "position": "body_vapour_R_S_T"
        },
        "wingtipleft": {
            "effectname": "WingVortices",
            "position": "body_vapour_L_E"
        },
        "wingtiplefttop": {
            "effectname": "WingVortices",
            "position": "body_vapour_L_E_T"
        },
        "wingtipright": {
            "effectname": "WingVortices",
            "position": "body_vapour_R_E"
        },
        "wingtiprighttop": {
            "effectname": "WingVortices",
            "position": "body_vapour_R_E_T"
        }
    }
}