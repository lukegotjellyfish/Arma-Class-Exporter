d = {
    "_generalmacro": "Land_PortableLight_02_quad_olive_F",
    "access": 0,
    "accuracy": 1000,
    "accuracydarknightlightsoff": 0.001,
    "accuracynightlightsoff": 0.006,
    "accuracynightlightson": 0.1,
    "aggregatereflectors": [
        [
            "Light_1",
            "Light_2",
            "Light_3",
            "Light_4"
        ]
    ],
    "aircapacity": 10,
    "allowtablock": 1,
    "alwaystarget": 0,
    "animated": 0,
    "animationsources": {
        "light_1_extend_source": {
            "animperiod": 2,
            "initphase": 1,
            "source": "user"
        },
        "light_1_pitch_source": {
            "animperiod": 2,
            "initphase": 0,
            "source": "user"
        },
        "light_1_yaw_source": {
            "animperiod": 2,
            "initphase": 0,
            "source": "user"
        },
        "light_2_extend_source": {
            "animperiod": 2,
            "initphase": 1,
            "source": "user"
        },
        "light_2_pitch_source": {
            "animperiod": 2,
            "initphase": 0,
            "source": "user"
        },
        "light_2_yaw_source": {
            "animperiod": 2,
            "initphase": 0,
            "source": "user"
        },
        "light_3_extend_source": {
            "animperiod": 2,
            "initphase": 0,
            "source": "user"
        },
        "light_3_pitch_source": {
            "animperiod": 2,
            "initphase": 0,
            "source": "user"
        },
        "light_3_yaw_source": {
            "animperiod": 2,
            "initphase": 0,
            "source": "user"
        },
        "light_4_extend_source": {
            "animperiod": 2,
            "initphase": 0,
            "source": "user"
        },
        "light_4_pitch_source": {
            "animperiod": 2,
            "initphase": 0,
            "source": "user"
        },
        "light_4_yaw_source": {
            "animperiod": 2,
            "initphase": 0,
            "source": "user"
        }
    },
    "antirollbarforcecoef": 0,
    "antirollbarforcelimit": 5,
    "antirollbarspeedmax": 60,
    "antirollbarspeedmin": 20,
    "armor": 500,
    "armorlights": 0.001,
    "armorstructural": 1,
    "artilleryscanner": 0,
    "artillerytarget": 0,
    "attendant": 0,
    "attenuationeffecttype": "",
    "attributes": {
        "hit_light_1": {
            "control": "CheckboxNumber",
            "defaultvalue": 0,
            "displayname": "Turn off light #1",
            "expression": "_this setHitpointDamage ['%s',_value];",
            "property": "Light_1_off"
        },
        "hit_light_2": {
            "control": "CheckboxNumber",
            "defaultvalue": 0,
            "displayname": "Turn off light #2",
            "expression": "_this setHitpointDamage ['%s',_value];",
            "property": "Light_2_Off"
        },
        "hit_light_3": {
            "control": "CheckboxNumber",
            "defaultvalue": 0,
            "displayname": "Turn off light #3",
            "expression": "_this setHitpointDamage ['%s',_value];",
            "property": "Light_3_Off"
        },
        "hit_light_4": {
            "control": "CheckboxNumber",
            "defaultvalue": 0,
            "displayname": "Turn off light #4",
            "expression": "_this setHitpointDamage ['%s',_value];",
            "property": "Light_4_Off"
        },
        "light_1_extend_source": {
            "control": "Slider",
            "defaultvalue": 1,
            "displayname": "Extend light #1",
            "expression": "_this animateSource ['%s',_value,true]",
            "property": "Light_1_Extend",
            "tooltip": "0-1 range",
            "validate": "number"
        },
        "light_1_pitch_source": {
            "control": "edit",
            "defaultvalue": 0,
            "displayname": "Pitch light #1",
            "expression": "_this animateSource ['%s',_value,true]",
            "property": "Light_1_Pitch",
            "tooltip": "+/-90 degrees range",
            "validate": "number"
        },
        "light_1_yaw_source": {
            "control": "edit",
            "defaultvalue": 0,
            "displayname": "Yaw light #1",
            "expression": "_this animateSource ['%s',_value,true]",
            "property": "Light_1_yaw",
            "tooltip": "+/-180 degrees range",
            "validate": "number"
        },
        "light_2_extend_source": {
            "control": "Slider",
            "defaultvalue": 1,
            "displayname": "Extend light #2",
            "expression": "_this animateSource ['%s',_value,true]",
            "property": "Light_2_Extend",
            "tooltip": "0-1 range",
            "validate": "number"
        },
        "light_2_pitch_source": {
            "control": "edit",
            "defaultvalue": 0,
            "displayname": "Pitch light #2",
            "expression": "_this animateSource ['%s',_value,true]",
            "property": "Light_2_Pitch",
            "tooltip": "+/-90 degrees range",
            "validate": "number"
        },
        "light_2_yaw_source": {
            "control": "edit",
            "defaultvalue": 0,
            "displayname": "Yaw light #2",
            "expression": "_this animateSource ['%s',_value,true]",
            "property": "Light_2_yaw",
            "tooltip": "+/-180 degrees range",
            "validate": "number"
        },
        "light_3_extend_source": {
            "control": "Slider",
            "defaultvalue": 0,
            "displayname": "Extend light #3",
            "expression": "_this animateSource ['%s',_value,true]",
            "property": "Light_3_Extend",
            "tooltip": "0-1 range",
            "validate": "number"
        },
        "light_3_pitch_source": {
            "control": "edit",
            "defaultvalue": 0,
            "displayname": "Pitch light #3",
            "expression": "_this animateSource ['%s',_value,true]",
            "property": "Light_3_Pitch",
            "tooltip": "+/-90 degrees range",
            "validate": "number"
        },
        "light_3_yaw_source": {
            "control": "edit",
            "defaultvalue": 0,
            "displayname": "Yaw light #3",
            "expression": "_this animateSource ['%s',_value,true]",
            "property": "Light_3_yaw",
            "tooltip": "+/-180 degrees range",
            "validate": "number"
        },
        "light_4_extend_source": {
            "control": "Slider",
            "defaultvalue": 0,
            "displayname": "Extend light #4",
            "expression": "_this animateSource ['%s',_value,true]",
            "property": "Light_4_Extend",
            "tooltip": "0-1 range",
            "validate": "number"
        },
        "light_4_pitch_source": {
            "control": "edit",
            "defaultvalue": 0,
            "displayname": "Pitch light #4",
            "expression": "_this animateSource ['%s',_value,true]",
            "property": "Light_4_Pitch",
            "tooltip": "+/-90 degrees range",
            "validate": "number"
        },
        "light_4_yaw_source": {
            "control": "edit",
            "defaultvalue": 0,
            "displayname": "Yaw light #4",
            "expression": "_this animateSource ['%s',_value,true]",
            "property": "Light_4_yaw",
            "tooltip": "+/-180 degrees range",
            "validate": "number"
        }
    },
    "audible": 0,
    "author": "Bohemia Interactive",
    "autocenter": 1,
    "brakedistance": 5,
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
    "camouflage": 2,
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
        "duration": 3,
        "frequency": 20,
        "minspeed": 1,
        "power": 1
    },
    "canhidedriver": -1,
    "canusescanners": 1,
    "cargoaction": [],
    "cargocaneject": 1,
    "cargocompartments": [
        "Compartment1"
    ],
    "cargogetinaction": [],
    "cargogetoutaction": [],
    "cargoiscodriver": [
        0
    ],
    "cargospec": {
        "cargo1": {
            "showheadphones": 0
        }
    },
    "castcargoshadow": 0,
    "castdrivershadow": 0,
    "coefinside": 2,
    "coefinsideheur": 2,
    "coefspeedinside": 2,
    "commandercansee": 31,
    "cost": 1000,
    "countsforscoreboard": 0,
    "crew": "Civilian",
    "crewcrashprotection": 1,
    "crewvulnerable": 1,
    "damage": {
        "mat": [],
        "tex": []
    },
    "damagefull": [],
    "damagehalf": [],
    "damageresistance": 0.004,
    "damagetexdelay": 0,
    "destrtype": "DestructTree",
    "destructioneffects": {
        "damagearound1": {
            "intensity": 1,
            "interval": 1,
            "lifetime": 1,
            "position": "",
            "simulation": "damageAround",
            "type": "DamageAroundHouse"
        },
        "destroyphase1": {
            "intensity": 1,
            "interval": 1,
            "lifetime": 2.5,
            "position": "",
            "simulation": "destroy",
            "type": "DelayedDestruction"
        },
        "smoke1": {
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 0.05,
            "position": "destructionEffect1",
            "qualitylevel": 2,
            "simulation": "particles",
            "type": "HouseDestructionSmoke3Small"
        },
        "smoke1low": {
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 0.05,
            "position": "destructionEffect1",
            "qualitylevel": 0,
            "simulation": "particles",
            "type": "HouseDestructionSmoke3Small"
        },
        "smoke1med": {
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 0.05,
            "position": "destructionEffect1",
            "qualitylevel": 1,
            "simulation": "particles",
            "type": "HouseDestructionSmoke3Small"
        },
        "smoke2": {
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 0.035,
            "position": "destructionEffect1",
            "qualitylevel": 2,
            "simulation": "particles",
            "type": "HouseDestructionSmoke4Small"
        },
        "smoke2low": {
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 0.035,
            "position": "destructionEffect1",
            "qualitylevel": 0,
            "simulation": "particles",
            "type": "HouseDestructionSmoke4Small"
        },
        "smoke2med": {
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 0.035,
            "position": "destructionEffect1",
            "qualitylevel": 1,
            "simulation": "particles",
            "type": "HouseDestructionSmoke4Small"
        },
        "smoke3": {
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 0.035,
            "position": "destructionEffect1",
            "qualitylevel": 2,
            "simulation": "particles",
            "type": "HouseDestrSmokeLongSmall"
        },
        "smoke3low": {
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 0.035,
            "position": "destructionEffect1",
            "qualitylevel": 0,
            "simulation": "particles",
            "type": "HouseDestrSmokeLongSmall"
        },
        "smoke3med": {
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 0.035,
            "position": "destructionEffect1",
            "qualitylevel": 1,
            "simulation": "particles",
            "type": "HouseDestrSmokeLongSmall"
        },
        "sound": {
            "intensity": 1,
            "interval": 1,
            "lifetime": 0.125,
            "position": "destructionEffect1",
            "simulation": "sound",
            "type": "DestrHouse"
        }
    },
    "detectskill": 20,
    "displayname": "Rugged Portable Lamp (Quad, Olive)",
    "dlc": "Enoch",
    "driveraction": "",
    "drivercaneject": 1,
    "drivercansee": "2+8+16",
    "drivercompartments": "Compartment1",
    "driverforceoptics": 0,
    "driverinaction": "",
    "driveropticscolor": [
        1,
        1,
        1,
        1
    ],
    "driveropticseffect": [],
    "driveropticsmodel": "",
    "dustbackleftpos": "dustBackLeft",
    "dustbackrightpos": "dustBackRight",
    "dustfrontleftpos": "dustFrontLeft",
    "dustfrontrightpos": "dustFrontRight",
    "editorcategory": "EdCat_Things",
    "editorpreview": "A3/EditorPreviews_F_Enoch/Data/CfgVehicles/Land_PortableLight_02_quad_olive_F.jpg",
    "editorsubcategory": "EdSubcat_Lamps",
    "ejectdeadcargo": 0,
    "ejectdeaddriver": 0,
    "emptysound": [
        "",
        0,
        1
    ],
    "enablegps": 0,
    "enablemanualfire": 1,
    "enableradio": 0,
    "enablewatch": 0,
    "engineer": 0,
    "epeimpulsedamagecoef": 30,
    "eventhandlers": {},
    "explosionshielding": 5,
    "extcameraparams": [
        1
    ],
    "extcameraposition": [
        0,
        2,
        -20
    ],
    "faction": "Default",
    "features": "",
    "featuretype": 0,
    "fireresistance": 10,
    "forcehidedriver": 0,
    "formationtime": 5,
    "formationx": 10,
    "formationz": 20,
    "fuelcapacity": 0,
    "fuelconsumptionrate": 0.01,
    "fxexplo": {
        "access": 1
    },
    "getinaction": "",
    "getinradius": 2.5,
    "getoutaction": "",
    "gforceshakeattenuation": 0.5,
    "ghostpreview": "",
    "groupcameraposition": [
        0,
        5,
        -30
    ],
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
    "gunnercansee": "4+8+16",
    "gunnerhasflares": 1,
    "hasdriver": 0,
    "headaimdown": 0,
    "headgforceleaningfactor": [
        0.01,
        0.002,
        0.01
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
        "Camo_1"
    ],
    "hiddenselectionsmaterials": [],
    "hiddenselectionstextures": [
        "a3/Props_F_Enoch/Military/Camps/data/Portable_light_02_Olive_CO.paa"
    ],
    "hiddenunderwaterselections": [],
    "hiddenunderwaterselectionstextures": [],
    "hideproxyincombat": 0,
    "hideunitinfo": 0,
    "hideweaponscargo": 0,
    "hideweaponsdriver": 1,
    "hitpoints": {
        "hit_light_1": {
            "armor": -5,
            "armorcomponent": "Light_1_Pitch",
            "explosionshielding": 3.5,
            "name": "Light_1_Hitpoint",
            "passthrough": 0.1,
            "radius": 0.1,
            "visual": "-"
        },
        "hit_light_2": {
            "armor": -5,
            "armorcomponent": "Light_2_Pitch",
            "explosionshielding": 3.5,
            "name": "Light_2_Hitpoint",
            "passthrough": 0.1,
            "radius": 0.1,
            "visual": "-"
        },
        "hit_light_3": {
            "armor": -5,
            "armorcomponent": "Light_3_Pitch",
            "explosionshielding": 3.5,
            "name": "Light_3_Hitpoint",
            "passthrough": 0.1,
            "radius": 0.1,
            "visual": "-"
        },
        "hit_light_4": {
            "armor": -5,
            "armorcomponent": "Light_4_Pitch",
            "explosionshielding": 3.5,
            "name": "Light_4_Hitpoint",
            "passthrough": 0.1,
            "radius": 0.1,
            "visual": "-"
        }
    },
    "hulldamagecauseexplosion": 0,
    "icon": "iconObject_5x4",
    "impacteffectssea": "ImpactEffectsSea",
    "incomingmissiledetectionsystem": 0,
    "indirecthitciviliancoefai": -20,
    "indirecthitenemycoefai": 10,
    "indirecthitfriendlycoefai": -20,
    "indirecthitunknowncoefai": -0.5,
    "insidedetectcoef": 0.05,
    "insidesoundcoef": 0.5,
    "irscanground": 1,
    "irscanrangemax": 0,
    "irscanrangemin": 0,
    "irscantoeyefactor": 1,
    "irtarget": 0,
    "isbackpack": 0,
    "islockingdisabled": 1,
    "keephorizontalplacement": 1,
    "keepinepesceneafterdeath": 0,
    "killfriendlyexpcoef": 1,
    "ladders": [],
    "laserscanner": 0,
    "lasertarget": 0,
    "limitedspeedcoef": 0.22,
    "lockdetectionsystem": 0,
    "magazines": [],
    "mapsize": 0.06,
    "markerlights": {},
    "maxdetectrange": 20,
    "maxfordingdepth": 1,
    "maxgforce": 2,
    "maxspeed": 0,
    "memorypointsupply": "doplnovani",
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
    "minealerticonrange": 200,
    "minfiretime": 20,
    "mingforce": 0.2,
    "mintotaldamagethreshold": 0.01,
    "model": "a3/Props_F_Enoch/Military/Camps/PortableLight_02_quad_F.p3d",
    "namesound": "obj_building",
    "nightvision": 0,
    "normalspeedforwardcoef": 0.85,
    "numberphysicalwheels": 0,
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
    "obstructsoundswhenin": 0.562341,
    "occludesoundlfratio": 0.25,
    "occludesoundswhenin": 0.316228,
    "outsidesoundfilter": 0,
    "picture": "pictureStaticObject",
    "pilotspec": {
        "showheadphones": 0
    },
    "portrait": "",
    "precision": 5,
    "predictturnplan": 1,
    "predictturnsimul": 1.2,
    "preferroads": 0,
    "pulsationsound": {},
    "radartype": 0,
    "reflectors": {
        "light_1": {
            "ambient": [
                10,
                10,
                12
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 70,
                "hardlimitstart": 50,
                "linear": 2,
                "quadratic": 0.5,
                "start": 0
            },
            "color": [
                1000,
                1000,
                1200
            ],
            "conefadecoef": 6,
            "direction": "Light_1_dir",
            "flaremaxdistance": 250,
            "flaresize": 0.9,
            "hitpoint": "Light_1_hitpoint",
            "hitpointclass": "Hit_Light_1",
            "innerangle": 60,
            "intensity": 2.5,
            "outerangle": 178,
            "position": "Light_1_pos",
            "selection": "Light_1_hide",
            "size": 1,
            "useflare": 1
        },
        "light_2": {
            "ambient": [
                10,
                10,
                12
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 70,
                "hardlimitstart": 50,
                "linear": 2,
                "quadratic": 0.5,
                "start": 0
            },
            "color": [
                1000,
                1000,
                1200
            ],
            "conefadecoef": 6,
            "direction": "Light_2_dir",
            "flaremaxdistance": 250,
            "flaresize": 0.9,
            "hitpoint": "Light_2_hitpoint",
            "hitpointclass": "Hit_Light_2",
            "innerangle": 60,
            "intensity": 2.5,
            "outerangle": 178,
            "position": "Light_2_pos",
            "selection": "Light_2_hide",
            "size": 1,
            "useflare": 1
        },
        "light_3": {
            "ambient": [
                10,
                10,
                12
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 70,
                "hardlimitstart": 50,
                "linear": 2,
                "quadratic": 0.5,
                "start": 0
            },
            "color": [
                1000,
                1000,
                1200
            ],
            "conefadecoef": 6,
            "direction": "Light_3_dir",
            "flaremaxdistance": 250,
            "flaresize": 0.9,
            "hitpoint": "Light_3_hitpoint",
            "hitpointclass": "Hit_Light_3",
            "innerangle": 60,
            "intensity": 2.5,
            "outerangle": 178,
            "position": "Light_3_pos",
            "selection": "Light_3_hide",
            "size": 1,
            "useflare": 1
        },
        "light_4": {
            "ambient": [
                10,
                10,
                12
            ],
            "attenuation": {
                "constant": 0,
                "hardlimitend": 70,
                "hardlimitstart": 50,
                "linear": 2,
                "quadratic": 0.5,
                "start": 0
            },
            "color": [
                1000,
                1000,
                1200
            ],
            "conefadecoef": 6,
            "direction": "Light_4_dir",
            "flaremaxdistance": 250,
            "flaresize": 0.9,
            "hitpoint": "Light_4_hitpoint",
            "hitpointclass": "Hit_Light_4",
            "innerangle": 60,
            "intensity": 2.5,
            "outerangle": 178,
            "position": "Light_4_pos",
            "selection": "Light_4_hide",
            "size": 1,
            "useflare": 1
        }
    },
    "replacedamaged": "",
    "replacedamagedhitpoints": [],
    "replacedamagedlimit": 0.99999,
    "reversed": 0,
    "scope": 2,
    "scopecurator": 2,
    "secondaryexplosion": -1,
    "selectionbacklights": "",
    "selectionclan": "",
    "selectiondamage": "zbytek",
    "selectiondashboard": "",
    "selectionfireanim": "",
    "selectionshowdamage": "",
    "sensitivity": 2.5,
    "sensitivityear": 0.0075,
    "shadow": 1,
    "showalltargets": 0,
    "showcrewaim": 7,
    "shownunderwaterselections": [],
    "shownvgcargo": [
        0
    ],
    "shownvgcommander": 0,
    "shownvgdriver": 0,
    "shownvggunner": 0,
    "side": 3,
    "simpleobject": {
        "animate": [
            [
                "batterylevel_1",
                0.38
            ],
            [
                "batterylevel_2",
                0.38
            ],
            [
                "batterylevel_3",
                0.38
            ],
            [
                "batterylevel_4",
                0.38
            ],
            [
                "display_clock_flash",
                2243.78
            ],
            [
                "display_hour_0x_hide",
                0.6
            ],
            [
                "display_hour_1x_hide",
                0.6
            ],
            [
                "display_hour_2x_hide",
                0.6
            ],
            [
                "display_hour_x0_hide",
                0.6
            ],
            [
                "display_hour_x1_hide",
                0.6
            ],
            [
                "display_hour_x2_hide",
                0.6
            ],
            [
                "display_hour_x3_hide",
                0.6
            ],
            [
                "display_hour_x4_hide",
                0.6
            ],
            [
                "display_hour_x5_hide",
                0.6
            ],
            [
                "display_hour_x6_hide",
                0.6
            ],
            [
                "display_hour_x7_hide",
                0.6
            ],
            [
                "display_hour_x8_hide",
                0.6
            ],
            [
                "display_hour_x9_hide",
                0.6
            ],
            [
                "display_minute_0x_hide",
                0.29
            ],
            [
                "display_minute_1x_hide",
                0.29
            ],
            [
                "display_minute_2x_hide",
                0.29
            ],
            [
                "display_minute_3x_hide",
                0.29
            ],
            [
                "display_minute_4x_hide",
                0.29
            ],
            [
                "display_minute_5x_hide",
                0.29
            ],
            [
                "display_minute_x0_hide",
                0.29
            ],
            [
                "display_minute_x1_hide",
                0.29
            ],
            [
                "display_minute_x2_hide",
                0.29
            ],
            [
                "display_minute_x3_hide",
                0.29
            ],
            [
                "display_minute_x4_hide",
                0.29
            ],
            [
                "display_minute_x5_hide",
                0.29
            ],
            [
                "display_minute_x6_hide",
                0.29
            ],
            [
                "display_minute_x7_hide",
                0.29
            ],
            [
                "display_minute_x8_hide",
                0.29
            ],
            [
                "display_minute_x9_hide",
                0.29
            ],
            [
                "light_1_pitch_rot",
                0
            ],
            [
                "light_1_yaw_rot",
                0
            ],
            [
                "light_1_extend_1",
                1
            ],
            [
                "light_1_extend_2",
                1
            ],
            [
                "light_1_extend_3",
                1
            ],
            [
                "light_2_pitch_rot",
                0
            ],
            [
                "light_2_yaw_rot",
                0
            ],
            [
                "light_2_extend_1",
                1
            ],
            [
                "light_2_extend_2",
                1
            ],
            [
                "light_2_extend_3",
                1
            ],
            [
                "light_3_pitch_rot",
                0
            ],
            [
                "light_3_yaw_rot",
                0
            ],
            [
                "light_3_extend_1",
                0
            ],
            [
                "light_3_extend_2",
                0
            ],
            [
                "light_3_extend_3",
                0
            ],
            [
                "light_4_pitch_rot",
                0
            ],
            [
                "light_4_yaw_rot",
                0
            ],
            [
                "light_4_extend_1",
                0
            ],
            [
                "light_4_extend_2",
                0
            ],
            [
                "light_4_extend_3",
                0
            ]
        ],
        "eden": 0,
        "hide": [
            "light_1_hide",
            "light_2_hide",
            "light_3_hide",
            "light_4_hide"
        ],
        "init": "''",
        "verticaloffset": 0.938,
        "verticaloffsetworld": 0
    },
    "simulation": "house",
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
        1,
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
        "",
        1,
        1
    ],
    "soundengineoffint": [
        "",
        1,
        1
    ],
    "soundengineonext": [
        "",
        1,
        1
    ],
    "soundengineonint": [
        "",
        1,
        1
    ],
    "soundenviron": [
        "",
        1,
        1
    ],
    "soundenvironext": {},
    "soundequipment": {},
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
        "",
        0.000316228,
        1
    ],
    "soundgetout": [
        "",
        0.000316228,
        1
    ],
    "soundhitscream": {},
    "soundincommingmissile": [
        "",
        1,
        1
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
        "",
        1,
        1
    ],
    "soundrecovered": {},
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
                "veh_unknown_p"
            ],
            "speechsingular": [
                "veh_unknown_s"
            ]
        }
    },
    "spotabledarknightlightsoff": 0.001,
    "spotablenightlightsoff": 0.02,
    "spotablenightlightson": 4,
    "steeraheadplan": 0.4,
    "steeraheadsimul": 0.3,
    "supplyradius": -1,
    "textplural": "unknown",
    "textsingular": "unknown",
    "threat": [
        0,
        0,
        0
    ],
    "transportammo": 0,
    "transportfuel": 0,
    "transportmagazines": {},
    "transportmaxbackpacks": 0,
    "transportmaxmagazines": 0,
    "transportmaxweapons": 0,
    "transportrepair": 0,
    "transportsoldier": 0,
    "transportvehiclescount": 0,
    "transportvehiclesmass": 0,
    "transportweapons": {},
    "turrets": {},
    "type": 1,
    "typicalcargo": [],
    "uavhacker": 0,
    "unitinfotype": "RscUnitInfoTank",
    "unitinfotypelite": 0,
    "unloadincombat": 0,
    "useprecisegetinaction": 0,
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
        "minanglex": -85,
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
        "initfov": 0.7,
        "maxanglex": 30,
        "maxangley": 100,
        "maxfov": 0.85,
        "maxmovex": 0,
        "maxmovey": 0,
        "maxmovez": 0,
        "minanglex": -30,
        "minangley": -100,
        "minfov": 0.42,
        "minmovex": 0,
        "minmovey": 0,
        "minmovez": 0,
        "speedzoommaxfov": 0,
        "speedzoommaxspeed": 10000000000.0
    },
    "viewpilot": {
        "initanglex": 5,
        "initangley": 0,
        "initfov": 0.75,
        "maxanglex": 85,
        "maxangley": 150,
        "maxfov": 1.25,
        "maxmovex": 0,
        "maxmovey": 0,
        "maxmovez": 0,
        "minanglex": -55,
        "minangley": -150,
        "minfov": 0.25,
        "minmovex": 0,
        "minmovey": 0,
        "minmovez": 0,
        "speedzoommaxfov": 0,
        "speedzoommaxspeed": 10000000000.0
    },
    "waterangulardampingcoef": 0,
    "waterdamageengine": 0.2,
    "waterleakiness": 0.5,
    "waterlineardampingcoefx": 0,
    "waterlineardampingcoefy": 0,
    "waterresistance": 10,
    "waterresistancecoef": 0.5,
    "weapons": [],
    "weaponsgroup1": "1 + 2",
    "weaponsgroup2": 4,
    "weaponsgroup3": "8 + 16 + 32",
    "weaponsgroup4": "64 + 128",
    "weaponslots": 0,
    "wheelcircumference": 1,
    "windsockexist": 0
}