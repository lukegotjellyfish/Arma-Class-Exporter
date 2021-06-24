rhsgref_cdf_b_reg_uaz = {
    "author": "Red Hammer Studios",
    "faction": "rhsgref_faction_cdf_ground_b",
    "side": 1,
    "scope": 2,
    "scopecurator": 2,
    "crew": "rhsgref_cdf_b_reg_rifleman",
    "editorpreview": "rhsgref|addons|rhsgref_editorPreviews|data|rhsgref_cdf_reg_uaz.paa",
    "dlc": "RHS_GREF",
    "accuracy": 0.5,
    "rhs_decalparameters": ["['Number', cDecals4CarsNumberPlaces, 'LicensePlate']"],
    "hiddenselectionstextures": ["rhsafrf|addons|rhs_a2port_car|uaz|data|uaz_main_002_co.paa"],
    "category": "Car",
    "insidesoundcoef": 0.2,
    "slingloadcargomemorypoints": ["SlingLoadCargo1","SlingLoadCargo2","SlingLoadCargo3","SlingLoadCargo4"],
    "model": "rhsafrf|addons|rhs_a2port_car|UAZ|UAZ.p3d",
    "icon": "rhsafrf|addons|rhs_a2port_car|data|mapico|icomap_uaz_ca.paa",
    "picture": "rhsafrf|addons|rhs_a2port_car|data|ico|rhs_uaz_pic_ca.paa",
    "mapsize": 4,
    "displayname": "UAZ-3151",
    "tf_haslrradio_api": 0,
    "hiddenselections": ["camo1","camo2g","n1","n2","n3","n4","i1","i2","i3","i4"],
    # Class: CfgVehicles|RHS_UAZ_Base|textureSources [Indent level: 1],
    "texturesources": {
        # Class: CfgVehicles|RHS_UAZ_Base|textureSources|standard [Indent level: 2]
        "standard": {
            "displayname": "Standard",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_a2port_car|uaz|data|uaz_main_ind_co.paa"],
            "factions": ["rhs_faction_msv","rhs_faction_vmf","rhs_faction_vdv","rhs_faction_vdv","rhs_faction_vv"]
        },
        # Class: CfgVehicles|RHS_UAZ_Base|textureSources|Camo [Indent level: 2],
        "camo": {
            "displayname": "Camo",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_a2port_car|uaz|data|uaz_main_co.paa"],
            "factions": ["rhs_faction_msv","rhs_faction_vmf","rhs_faction_vdv","rhs_faction_vdv","rhs_faction_vv"]
        },
        # Class: CfgVehicles|RHS_UAZ_Base|textureSources|Camo1 [Indent level: 2],
        "camo1": {
            "displayname": "Chedaki",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_a2port_car|uaz|data|uaz_main_001_co.paa"],
            "factions": ["rhs_faction_msv","rhs_faction_vmf","rhs_faction_vdv","rhs_faction_vdv","rhs_faction_vv"]
        },
        # Class: CfgVehicles|RHS_UAZ_Base|textureSources|Camo2 [Indent level: 2],
        "camo2": {
            "displayname": "CDF",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_a2port_car|uaz|data|uaz_main_002_co.paa"],
            "factions": ["rhs_faction_msv","rhs_faction_vmf","rhs_faction_vdv","rhs_faction_vdv","rhs_faction_vv"]
        },
        # Class: CfgVehicles|RHS_UAZ_Base|textureSources|Camo3 [Indent level: 2],
        "camo3": {
            "displayname": "Civil",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_a2port_car|uaz|data|uaz_main_civil_co.paa"],
            "factions": ["rhs_faction_msv","rhs_faction_vmf","rhs_faction_vdv","rhs_faction_vdv","rhs_faction_vv"]
        },
        # Class: CfgVehicles|RHS_UAZ_Base|textureSources|Camo4 [Indent level: 2],
        "camo4": {
            "displayname": "UN",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_a2port_car|uaz|data|uaz_main_un_co.paa"],
            "factions": ["rhs_faction_msv","rhs_faction_vmf","rhs_faction_vdv","rhs_faction_vdv","rhs_faction_vv"]
        },
        # Class: CfgVehicles|RHS_UAZ_Base|textureSources|Takistan [Indent level: 2],
        "takistan": {
            "displayname": "Takistan",
            "author": "Red Hammer Studios",
            "textures": ["rhsgref|addons|rhsgref_vehicles_ret|data|tak|uaz_main_ind_co.paa"]
        }
    },
    "texturelist": [],
    # Class: CfgVehicles|RHS_UAZ_Base|Attributes [Indent level: 1],
    "attributes": {
        # Class: CfgVehicles|RHS_UAZ_Base|Attributes|ObjectTexture [Indent level: 2]
        "objecttexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayname": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Attributes|rhs_decalNumber_type [Indent level: 2],
        "rhs_decalnumber_type": {
            "displayname": "Define font type of plate number",
            "tooltip": "Define kind of font that will be drawn on vehicle.",
            "property": "rhs_decalNumber_type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];[_this,[['Number', cDecals4CarsNumberPlaces, _value]]] call rhs_fnc_decalsInit",
            "defaultvalue": 0,
            "typename": "STRING",
            # Class: CfgVehicles|RHS_UAZ_Base|Attributes|rhs_decalNumber_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|RHS_UAZ_Base|Attributes|rhs_decalNumber_type|values|Default [Indent level: 4]
                "default": {
                    "name": "Default",
                    "value": "Default",
                    "defaultvalue": "Default"
                },
                # Class: CfgVehicles|RHS_UAZ_Base|Attributes|rhs_decalNumber_type|values|DefaultRed [Indent level: 4],
                "defaultred": {
                    "name": "Default (Red)",
                    "value": "DefaultRed"
                },
                # Class: CfgVehicles|RHS_UAZ_Base|Attributes|rhs_decalNumber_type|values|BoldRed [Indent level: 4],
                "boldred": {
                    "name": "Bold Red",
                    "value": "BoldRed"
                },
                # Class: CfgVehicles|RHS_UAZ_Base|Attributes|rhs_decalNumber_type|values|CDF [Indent level: 4],
                "cdf": {
                    "name": "CDF",
                    "value": "CDF"
                },
                # Class: CfgVehicles|RHS_UAZ_Base|Attributes|rhs_decalNumber_type|values|Handpaint [Indent level: 4],
                "handpaint": {
                    "name": "Handpaint",
                    "value": "Handpaint"
                },
                # Class: CfgVehicles|RHS_UAZ_Base|Attributes|rhs_decalNumber_type|values|HandpaintBlack [Indent level: 4],
                "handpaintblack": {
                    "name": "Handpaint Black",
                    "value": "HandpaintBlack"
                },
                # Class: CfgVehicles|RHS_UAZ_Base|Attributes|rhs_decalNumber_type|values|Iraqi [Indent level: 4],
                "iraqi": {
                    "name": "Iraqi",
                    "value": "Iraqi"
                },
                # Class: CfgVehicles|RHS_UAZ_Base|Attributes|rhs_decalNumber_type|values|LicensePlate [Indent level: 4],
                "licenseplate": {
                    "name": "License Plate",
                    "value": "LicensePlate"
                }
            }
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Attributes|rhs_decalNumber [Indent level: 2],
        "rhs_decalnumber": {
            "collapsed": 1,
            "displayname": "Set plate number",
            "tooltip": "Set plate number. 4 numbers are required. If 0, random number will be generated",
            "property": "rhs_decalNumber",
            "control": "Edit",
            "validate": "Number",
            "typename": "Number",
            "defaultvalue": "-1",
            "expression": "if(_value >= 0)then{[_this,[['Number', cDecals4CarsNumberPlaces, _this getVariable ['rhs_decalNumber_type','LicensePlate'], _value]]] call rhs_fnc_decalsInit};"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Attributes|rhs_decalArmy_type [Indent level: 2],
        "rhs_decalarmy_type": {
            "displayname": "Define large door roundel type",
            "tooltip": "Decal type",
            "property": "rhs_decalArmy_type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": "0",
            "typename": "STRING",
            # Class: CfgVehicles|RHS_UAZ_Base|Attributes|rhs_decalArmy_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|RHS_UAZ_Base|Attributes|rhs_decalArmy_type|values|Army [Indent level: 4]
                "army": {
                    "name": "Army",
                    "value": "Army",
                    "defaultvalue": "Army"
                },
                # Class: CfgVehicles|RHS_UAZ_Base|Attributes|rhs_decalArmy_type|values|Honor [Indent level: 4],
                "honor": {
                    "name": "Honor",
                    "value": "Honor"
                },
                # Class: CfgVehicles|RHS_UAZ_Base|Attributes|rhs_decalArmy_type|values|HonorGDR [Indent level: 4],
                "honorgdr": {
                    "name": "Honor GDR",
                    "value": "HonorGDR"
                },
                # Class: CfgVehicles|RHS_UAZ_Base|Attributes|rhs_decalArmy_type|values|Platoon [Indent level: 4],
                "platoon": {
                    "name": "Platoon",
                    "value": "Platoon"
                },
                # Class: CfgVehicles|RHS_UAZ_Base|Attributes|rhs_decalArmy_type|values|PlatoonGDR [Indent level: 4],
                "platoongdr": {
                    "name": "Platoon GDR",
                    "value": "PlatoonGDR"
                },
                # Class: CfgVehicles|RHS_UAZ_Base|Attributes|rhs_decalArmy_type|values|PlatoonVDV [Indent level: 4],
                "platoonvdv": {
                    "name": "Platoon VDV",
                    "value": "PlatoonVDV"
                }
            }
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Attributes|rhs_decalArmy [Indent level: 2],
        "rhs_decalarmy": {
            "displayname": "Set large door roundel symbol",
            "tooltip": "Set large door roundel located on both sides. Usually used for army symbols. -1 leaves current symbol & 0 clears decal.",
            "property": "rhs_decalArmy",
            "control": "Edit",
            "validate": "none",
            "defaultvalue": "-1",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', cDecalsCarsRightArmyPlaces,  _this getVariable ['rhs_decalArmy_type','Army'],call compile _value] ] ] call rhs_fnc_decalsInit};"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Attributes|rhs_decalPlatoon_type [Indent level: 2],
        "rhs_decalplatoon_type": {
            "displayname": "Define small door roundel type",
            "property": "rhs_decalPlatoon_type",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": "0",
            "tooltip": "Decal type",
            "control": "Combo",
            "typename": "STRING",
            # Class: CfgVehicles|RHS_UAZ_Base|Attributes|rhs_decalArmy_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|RHS_UAZ_Base|Attributes|rhs_decalArmy_type|values|Army [Indent level: 4]
                "army": {
                    "name": "Army",
                    "value": "Army",
                    "defaultvalue": "Army"
                },
                # Class: CfgVehicles|RHS_UAZ_Base|Attributes|rhs_decalArmy_type|values|Honor [Indent level: 4],
                "honor": {
                    "name": "Honor",
                    "value": "Honor"
                },
                # Class: CfgVehicles|RHS_UAZ_Base|Attributes|rhs_decalArmy_type|values|HonorGDR [Indent level: 4],
                "honorgdr": {
                    "name": "Honor GDR",
                    "value": "HonorGDR"
                },
                # Class: CfgVehicles|RHS_UAZ_Base|Attributes|rhs_decalArmy_type|values|Platoon [Indent level: 4],
                "platoon": {
                    "name": "Platoon",
                    "value": "Platoon"
                },
                # Class: CfgVehicles|RHS_UAZ_Base|Attributes|rhs_decalArmy_type|values|PlatoonGDR [Indent level: 4],
                "platoongdr": {
                    "name": "Platoon GDR",
                    "value": "PlatoonGDR"
                },
                # Class: CfgVehicles|RHS_UAZ_Base|Attributes|rhs_decalArmy_type|values|PlatoonVDV [Indent level: 4],
                "platoonvdv": {
                    "name": "Platoon VDV",
                    "value": "PlatoonVDV"
                }
            }
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Attributes|rhs_decalPlatoon [Indent level: 2],
        "rhs_decalplatoon": {
            "displayname": "Set small door roundel symbol",
            "tooltip": "Define small door roundel located on both sides. Usually used for platoon symbols. -1 leaves current symbol & 0 clears decal.",
            "property": "rhs_decalPlatoon",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', cDecalsCarsRightPlatoonPlaces,  _this getVariable ['rhs_decalPlatoon_type','Army'],call compile _value] ] ] call rhs_fnc_decalsInit};",
            "control": "Edit",
            "validate": "none",
            "defaultvalue": "-1"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Attributes|rhs_hideLightCover [Indent level: 2],
        "rhs_hidelightcover": {
            "displayname": "Hide light covers",
            "property": "rhs_hideLightCover",
            "control": "CheckboxNumber",
            "expression": "_this animate ['light_hide',_value,true]",
            "defaultvalue": "0"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Attributes|rhs_hidespare [Indent level: 2],
        "rhs_hidespare": {
            "displayname": "Remove spare wheel",
            "property": "rhs_hidespare",
            "expression": "_this animate ['spare_hide',_value,true]",
            "control": "CheckboxNumber",
            "defaultvalue": "0"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Attributes|Door_LF [Indent level: 2],
        "door_lf": {
            "displayname": "Open front left door",
            "property": "Door_LF",
            "expression": "_this animateDoor ['%s',_value,true]",
            "control": "CheckboxNumber",
            "defaultvalue": "0"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Attributes|Door_RF [Indent level: 2],
        "door_rf": {
            "displayname": "Open front right door",
            "property": "Door_RF",
            "expression": "_this animateDoor ['%s',_value,true]",
            "control": "CheckboxNumber",
            "defaultvalue": "0"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Attributes|Door_LB [Indent level: 2],
        "door_lb": {
            "displayname": "Open left back door",
            "property": "Door_LB",
            "expression": "_this animateDoor ['%s',_value,true]",
            "control": "CheckboxNumber",
            "defaultvalue": "0"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Attributes|Door_RB [Indent level: 2],
        "door_rb": {
            "displayname": "Open right back door",
            "property": "Door_RB",
            "expression": "_this animateDoor ['%s',_value,true]",
            "control": "CheckboxNumber",
            "defaultvalue": "0"
        }
    },
    "driveraction": "RHS_UAZ_driver",
    "driverinaction": "RHS_UAZ_driver",
    "hideproxyincombat": 0,
    "cost": 50000,
    "transportmaxbackpacks": 6,
    "transportsoldier": 6,
    "driverlefthandanimname": "drivewheel",
    "driverrighthandanimname": "shift",
    "driverrightleganimname": "pedalR",
    "driverleftleganimname": "pedalL",
    "soundattenuationcargo": [1],
    "vehicleclass": "rhs_vehclass_car",
    "editorsubcategory": "rhs_EdSubcat_car",
    "soundgear": ["rhsafrf|addons|rhs_a2port_car|sounds|Gear_Change",2,1],
    "soundgetin": ["rhsafrf|addons|rhs_vehiclesounds|sounds|soft|uaz469|ext-uaz469_engine-getin",1.58489,1,9],
    "soundgetout": ["rhsafrf|addons|rhs_vehiclesounds|sounds|soft|uaz469|ext-uaz469_engine-getout",1.58489,1,25],
    "soundengineonint": ["rhsafrf|addons|rhs_vehiclesounds|sounds|soft|uaz469|uaz469_engine_int_start1",1.58489,1],
    "soundengineonext": ["rhsafrf|addons|rhs_vehiclesounds|sounds|soft|uaz469|uaz469_engine_ext_start1",1.41254,1,200],
    "soundengineoffint": ["rhsafrf|addons|rhs_vehiclesounds|sounds|soft|uaz469|uaz469_engine_int_stop1",1.58489,1],
    "soundengineoffext": ["rhsafrf|addons|rhs_vehiclesounds|sounds|soft|uaz469|uaz469_engine_ext_stop1",1.41254,1,200],
    # Class: CfgVehicles|RHS_UAZ_Base|Sounds [Indent level: 1],
    "sounds": {
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|Idle_ext [Indent level: 2]
        "idle_ext": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|UAZ|uaz_ext_idle",1.58489,1,150],
            "frequency": "0.9	+	((rpm/	4000) factor[(200/	4000),(1150/	4000)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	4000) factor[(450/	4000),(590/	4000)])	*	((rpm/	4000) factor[(900/	4000),(690/	4000)]))"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|Engine [Indent level: 2],
        "engine": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|UAZ|uaz_ext_acceleration",1.41254,1,200],
            "frequency": "0.8	+	((rpm/	4000) factor[(900/	4000),(2100/	4000)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	4000) factor[(870/	4000),(1100/	4000)])	*	((rpm/	4000) factor[(2100/	4000),(1300/	4000)]))"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|Engine1_ext [Indent level: 2],
        "engine1_ext": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|UAZ|uaz_ext_low1",1.41254,1,240],
            "frequency": "0.8	+		((rpm/	4000) factor[(1300/	4000),(3100/	4000)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	4000) factor[(1250/	4000),(2050/	4000)])	*	((rpm/	4000) factor[(3100/	4000),(2300/	4000)]))"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|Engine2_ext [Indent level: 2],
        "engine2_ext": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|UAZ|uaz_ext_high1",1.25893,1,280],
            "frequency": "0.8	+	((rpm/	4000) factor[(2200/	4000),(4100/	4000)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	4000) factor[(2250/	4000),(3050/	4000)])	*	((rpm/	4000) factor[(4100/	4000),(3300/	4000)]))"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|Engine3_ext [Indent level: 2],
        "engine3_ext": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|UAZ|uaz_ext_high1",1.25893,1,320],
            "frequency": "0.8	+	((rpm/	4000) factor[(3300/	4000),(4900/	4000)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	4000) factor[(3250/	4000),(4050/	4000)])	*	((rpm/	4000) factor[(4870/	4000),(4200/	4000)]))"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|Engine4_ext [Indent level: 2],
        "engine4_ext": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|UAZ|uaz_ext_high1",1.12202,1,360],
            "frequency": "0.8	+	((rpm/	4000) factor[(4200/	4000),(6200/	4000)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	4000) factor[(4150/	4000),(4800/	4000)])	*	((rpm/	4000) factor[(6150/	4000),(5150/	4000)]))"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|Engine5_ext [Indent level: 2],
        "engine5_ext": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|UAZ|uaz_ext_high1",1.12202,1,420],
            "frequency": "0.95	+	((rpm/	4000) factor[(5100/	4000),(6900/	4000)])*0.15",
            "volume": "engineOn*camPos*((rpm/	4000) factor[(5100/	4000),(6100/	4000)])"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|IdleThrust [Indent level: 2],
        "idlethrust": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|UAZ|uaz_ext_idle_exhaust",1.25893,1,200],
            "frequency": "0.9	+	((rpm/	4000) factor[(200/	4000),(1150/	4000)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	4000) factor[(450/	4000),(590/	4000)])	*	((rpm/	4000) factor[(900/	4000),(690/	4000)]))"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|EngineThrust [Indent level: 2],
        "enginethrust": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|UAZ|uaz_ext_low1_exhaust",1.12202,1,250],
            "frequency": "0.8	+	((rpm/	4000) factor[(900/	4000),(2100/	4000)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	4000) factor[(870/	4000),(1100/	4000)])	*	((rpm/	4000) factor[(2100/	4000),(1300/	4000)]))"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|Engine1_Thrust_ext [Indent level: 2],
        "engine1_thrust_ext": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|UAZ|uaz_ext_low1_exhaust",1.12202,1,280],
            "frequency": "0.8	+		((rpm/	4000) factor[(1300/	4000),(3100/	4000)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	4000) factor[(1250/	4000),(2050/	4000)])	*	((rpm/	4000) factor[(3100/	4000),(2300/	4000)]))"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|Engine2_Thrust_ext [Indent level: 2],
        "engine2_thrust_ext": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|UAZ|uaz_ext_high1_exhaust",1.12202,1,320],
            "frequency": "0.8	+	((rpm/	4000) factor[(2200/	4000),(4100/	4000)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	4000) factor[(2250/	4000),(3050/	4000)])	*	((rpm/	4000) factor[(4100/	4000),(3300/	4000)]))"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|Engine3_Thrust_ext [Indent level: 2],
        "engine3_thrust_ext": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|UAZ|uaz_ext_high1_exhaust",1.12202,1,360],
            "frequency": "0.8	+	((rpm/	4000) factor[(3300/	4000),(4900/	4000)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	4000) factor[(3250/	4000),(4050/	4000)])	*	((rpm/	4000) factor[(4870/	4000),(4200/	4000)]))"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|Engine4_Thrust_ext [Indent level: 2],
        "engine4_thrust_ext": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|UAZ|uaz_ext_high1_exhaust",1,1,400],
            "frequency": "0.8	+	((rpm/	4000) factor[(4200/	4000),(6200/	4000)])*0.3",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	4000) factor[(4150/	4000),(4800/	4000)])	*	((rpm/	4000) factor[(6150/	4000),(5150/	4000)]))"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|Engine5_Thrust_ext [Indent level: 2],
        "engine5_thrust_ext": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|UAZ|uaz_ext_high1_exhaust",1.25893,1,450],
            "frequency": "0.9	+	((rpm/	4000) factor[(5100/	4000),(6900/	4000)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*((rpm/	4000) factor[(5100/	4000),(6100/	4000)])"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|Idle_int [Indent level: 2],
        "idle_int": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|UAZ|uaz_int_idle",1.25893,1],
            "frequency": "0.9	+	((rpm/	4000) factor[(200/	4000),(1150/	4000)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	4000) factor[(450/	4000),(590/	4000)])	*	((rpm/	4000) factor[(900/	4000),(690/	4000)]))"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|Engine_int [Indent level: 2],
        "engine_int": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|UAZ|uaz_int_acceleration",1.41254,1],
            "frequency": "0.8	+	((rpm/	4000) factor[(900/	4000),(2100/	4000)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	4000) factor[(870/	4000),(1100/	4000)])	*	((rpm/	4000) factor[(2100/	4000),(1300/	4000)]))"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|Engine1_int [Indent level: 2],
        "engine1_int": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|UAZ|uaz_int_low1",1.41254,1],
            "frequency": "0.8	+		((rpm/	4000) factor[(1300/	4000),(3100/	4000)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	4000) factor[(1250/	4000),(2050/	4000)])	*	((rpm/	4000) factor[(3100/	4000),(2300/	4000)]))"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|Engine2_int [Indent level: 2],
        "engine2_int": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|UAZ|uaz_int_high1",1.25893,1],
            "frequency": "0.8	+	((rpm/	4000) factor[(2200/	4000),(4100/	4000)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	4000) factor[(2250/	4000),(3050/	4000)])	*	((rpm/	4000) factor[(4100/	4000),(3300/	4000)]))"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|Engine3_int [Indent level: 2],
        "engine3_int": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|UAZ|uaz_int_high1",1.25893,1],
            "frequency": "0.8	+	((rpm/	4000) factor[(3300/	4000),(4900/	4000)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	4000) factor[(3250/	4000),(4050/	4000)])	*	((rpm/	4000) factor[(4870/	4000),(4200/	4000)]))"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|Engine4_int [Indent level: 2],
        "engine4_int": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|UAZ|uaz_int_high1",1.25893,1],
            "frequency": "0.8	+	((rpm/	4000) factor[(4200/	4000),(6200/	4000)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	4000) factor[(4150/	4000),(4800/	4000)])	*	((rpm/	4000) factor[(6150/	4000),(5150/	4000)]))"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|Engine5_int [Indent level: 2],
        "engine5_int": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|UAZ|uaz_int_high1",1.25893,1],
            "frequency": "0.95	+	((rpm/	4000) factor[(5100/	4000),(6900/	4000)])*0.15",
            "volume": "engineOn*(1-camPos)*((rpm/	4000) factor[(5100/	4000),(6100/	4000)])"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|IdleThrust_int [Indent level: 2],
        "idlethrust_int": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|UAZ|uaz_int_idle_exhaust",1.25893,1],
            "frequency": "0.9	+	((rpm/	4000) factor[(200/	4000),(1150/	4000)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	4000) factor[(450/	4000),(590/	4000)])	*	((rpm/	4000) factor[(900/	4000),(690/	4000)]))"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|EngineThrust_int [Indent level: 2],
        "enginethrust_int": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|UAZ|uaz_int_low1_exhaust",1.41254,1],
            "frequency": "0.8	+	((rpm/	4000) factor[(900/	4000),(2100/	4000)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	4000) factor[(870/	4000),(1100/	4000)])	*	((rpm/	4000) factor[(2100/	4000),(1300/	4000)]))"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|Engine1_Thrust_int [Indent level: 2],
        "engine1_thrust_int": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|UAZ|uaz_int_low1_exhaust",1.25893,1],
            "frequency": "0.8	+		((rpm/	4000) factor[(1300/	4000),(3100/	4000)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	4000) factor[(1250/	4000),(2050/	4000)])	*	((rpm/	4000) factor[(3100/	4000),(2300/	4000)]))"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|Engine2_Thrust_int [Indent level: 2],
        "engine2_thrust_int": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|UAZ|uaz_int_high1_exhaust",1.25893,1],
            "frequency": "0.8	+	((rpm/	4000) factor[(2200/	4000),(4100/	4000)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	4000) factor[(2250/	4000),(3050/	4000)])	*	((rpm/	4000) factor[(4100/	4000),(3300/	4000)]))"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|Engine3_Thrust_int [Indent level: 2],
        "engine3_thrust_int": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|UAZ|uaz_int_high1_exhaust",1.12202,1],
            "frequency": "0.8	+	((rpm/	4000) factor[(3300/	4000),(4900/	4000)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	4000) factor[(3250/	4000),(4050/	4000)])	*	((rpm/	4000) factor[(4870/	4000),(4200/	4000)]))"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|Engine4_Thrust_int [Indent level: 2],
        "engine4_thrust_int": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|UAZ|uaz_int_high1_exhaust",1.12202,1],
            "frequency": "0.8	+	((rpm/	4000) factor[(4200/	4000),(6200/	4000)])*0.3",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	4000) factor[(4150/	4000),(4800/	4000)])	*	((rpm/	4000) factor[(6150/	4000),(5150/	4000)]))"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|Engine5_Thrust_int [Indent level: 2],
        "engine5_thrust_int": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|UAZ|uaz_int_high1_exhaust",1.12202,1],
            "frequency": "0.9	+	((rpm/	4000) factor[(5100/	4000),(6900/	4000)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*((rpm/	4000) factor[(5100/	4000),(6100/	4000)])"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|RainIn [Indent level: 2],
        "rainin": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|rain.wss",1.41254,1],
            "frequency": 1,
            "volume": "rain*(1-camPos)"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|RainExt [Indent level: 2],
        "rainext": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|rain.wss",1.41254,1],
            "frequency": 1,
            "volume": "rain*camPos"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|TiresRockOut [Indent level: 2],
        "tiresrockout": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|ext_tires_dirt_soft_1",1.41254,1,60],
            "frequency": "1",
            "volume": "camPos*rock*(speed factor[2, 20])"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|TiresSandOut [Indent level: 2],
        "tiressandout": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|ext-tires-sand1",1.41254,1,60],
            "frequency": "1",
            "volume": "camPos*sand*(speed factor[2, 20])"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|TiresGrassOut [Indent level: 2],
        "tiresgrassout": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|ext_tires_dirt_soft_2",1.41254,1,60],
            "frequency": "1",
            "volume": "camPos*grass*(speed factor[2, 20])"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|TiresMudOut [Indent level: 2],
        "tiresmudout": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|ext-tires-mud2",1.41254,1,60],
            "frequency": "1",
            "volume": "camPos*mud*(speed factor[2, 20])"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|TiresGravelOut [Indent level: 2],
        "tiresgravelout": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|ext_tires_gravel_1",1.41254,1,60],
            "frequency": "1",
            "volume": "camPos*gravel*(speed factor[2, 20])"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|TiresAsphaltOut [Indent level: 2],
        "tiresasphaltout": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|ext_tires_asfalt_2",1.41254,1,60],
            "frequency": "1",
            "volume": "camPos*asphalt*(speed factor[2, 20])"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|NoiseOut [Indent level: 2],
        "noiseout": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|noise_ext_car_3",1.58489,1,90],
            "frequency": "1",
            "volume": "camPos*(damper0 max 0.02)*(speed factor[0, 8])"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|TiresRockIn [Indent level: 2],
        "tiresrockin": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|int_tires_dirt_soft_1",1.12202,1],
            "frequency": "1",
            "volume": "(1-camPos)*rock*(speed factor[2, 20])"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|TiresSandIn [Indent level: 2],
        "tiressandin": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|int-tires-sand2",1.12202,1],
            "frequency": "1",
            "volume": "(1-camPos)*sand*(speed factor[2, 20])"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|TiresGrassIn [Indent level: 2],
        "tiresgrassin": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|int_tires_dirt_soft_2",1.12202,1],
            "frequency": "1",
            "volume": "(1-camPos)*grass*(speed factor[2, 20])"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|TiresMudIn [Indent level: 2],
        "tiresmudin": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|int-tires-mud2",1.12202,1],
            "frequency": "1",
            "volume": "(1-camPos)*mud*(speed factor[2, 20])"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|TiresGravelIn [Indent level: 2],
        "tiresgravelin": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|int_tires_gravel_1",1.12202,1],
            "frequency": "1",
            "volume": "(1-camPos)*gravel*(speed factor[2, 20])"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|TiresAsphaltIn [Indent level: 2],
        "tiresasphaltin": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|int_tires_asfalt_2",1.12202,1],
            "frequency": "1",
            "volume": "(1-camPos)*asphalt*(speed factor[2, 20])"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|NoiseIn [Indent level: 2],
        "noisein": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|noise_int_car_3",1,1],
            "frequency": "1",
            "volume": "(damper0 max 0.1)*(speed factor[0, 8])*(1-camPos)"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|breaking_ext_road [Indent level: 2],
        "breaking_ext_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_04",1.41254,1,80],
            "frequency": 1,
            "volume": "engineOn*camPos*asphalt*(LongSlipDrive Factor[-0.1, -0.4])*(Speed Factor[2, 15])"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|acceleration_ext_road [Indent level: 2],
        "acceleration_ext_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_02",1.41254,1,80],
            "frequency": 1,
            "volume": "engineOn*camPos*asphalt*(LongSlipDrive Factor[0.1, 0.4])*(Speed Factor[15, 2])"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|turn_left_ext_road [Indent level: 2],
        "turn_left_ext_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_02",1.41254,1,80],
            "frequency": 1,
            "volume": "engineOn*camPos*asphalt*(latSlipDrive Factor[0.1, 0.4])*(Speed Factor[2, 15])"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|turn_right_ext_road [Indent level: 2],
        "turn_right_ext_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_02",1.41254,1,80],
            "frequency": 1,
            "volume": "engineOn*camPos*asphalt*(latSlipDrive Factor[-0.1, -0.4])*(Speed Factor[2, 15])"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|breaking_ext_dirt [Indent level: 2],
        "breaking_ext_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_14_dirt_breaking",1.12202,1,60],
            "frequency": 1,
            "volume": "engineOn*camPos*(1-asphalt)*(LongSlipDrive Factor[-0.1, -0.4])*(Speed Factor[1, 15])"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|acceleration_ext_dirt [Indent level: 2],
        "acceleration_ext_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_16_dirt_acceleration",1.12202,1,60],
            "frequency": 1,
            "volume": "engineOn*camPos*(1-asphalt)*(LongSlipDrive Factor[0.1, 0.4])*(Speed Factor[15, 1])"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|turn_left_ext_dirt [Indent level: 2],
        "turn_left_ext_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_18_dirt",1.12202,1,60],
            "frequency": 1,
            "volume": "engineOn*camPos*(1-asphalt)*(latSlipDrive Factor[0.1, 0.4])*(Speed Factor[1, 15])"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|turn_right_ext_dirt [Indent level: 2],
        "turn_right_ext_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_18_dirt",1,1,60],
            "frequency": 1,
            "volume": "engineOn*camPos*(1-asphalt)*(latSlipDrive Factor[-0.1, -0.4])*(Speed Factor[1, 15])"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|breaking_int_road [Indent level: 2],
        "breaking_int_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_04_int",3.16228,1],
            "frequency": 1,
            "volume": "engineOn*asphalt*(1-camPos)*(LongSlipDrive Factor[-0.1, -0.4])*(Speed Factor[2, 15])"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|acceleration_int_road [Indent level: 2],
        "acceleration_int_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_02_int",3.16228,1],
            "frequency": 1,
            "volume": "engineOn*asphalt*(1-camPos)*(LongSlipDrive Factor[0.1, 0.4])*(Speed Factor[15, 2])"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|turn_left_int_road [Indent level: 2],
        "turn_left_int_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_02_int",3.16228,1],
            "frequency": 1,
            "volume": "engineOn*asphalt*(1-camPos)*(latSlipDrive Factor[0.1, 0.4])*(Speed Factor[2, 15])"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|turn_right_int_road [Indent level: 2],
        "turn_right_int_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_02_int",3.16228,1],
            "frequency": 1,
            "volume": "engineOn*asphalt*(1-camPos)*(latSlipDrive Factor[-0.1, -0.4])*(Speed Factor[2, 15])"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|breaking_int_dirt [Indent level: 2],
        "breaking_int_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_14_dirt_breaking_int",3.16228,1],
            "frequency": 1,
            "volume": "engineOn*(1-asphalt)*(1-camPos)*(LongSlipDrive Factor[-0.1, -0.4])*(Speed Factor[2, 15])"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|acceleration_int_dirt [Indent level: 2],
        "acceleration_int_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_16_dirt_acceleration_int",3.16228,1],
            "frequency": 1,
            "volume": "engineOn*(1-asphalt)*(1-camPos)*(LongSlipDrive Factor[0.1, 0.4])*(Speed Factor[15, 2])"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|turn_left_int_dirt [Indent level: 2],
        "turn_left_int_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_18_dirt_int",3.16228,1],
            "frequency": 1,
            "volume": "engineOn*(1-asphalt)*(1-camPos)*(latSlipDrive Factor[0.1, 0.4])*(Speed Factor[2, 15])"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Sounds|turn_right_int_dirt [Indent level: 2],
        "turn_right_int_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_18_dirt_int",3.16228,1],
            "frequency": 1,
            "volume": "engineOn*(1-asphalt)*(1-camPos)*(latSlipDrive Factor[-0.1, -0.4])*(Speed Factor[2, 15])"
        },
        "soundsetsint": ["RHS_UAZ469_Engine_RPM0_INT_SoundSet","RHS_UAZ469_Engine_RPM1_INT_SoundSet","RHS_UAZ469_Engine_RPM2_INT_SoundSet","RHS_UAZ469_Engine_RPM3_INT_SoundSet","RHS_UAZ469_Engine_INT_Burst_SoundSet","RHS_UAZ469_Rattling_INT_SoundSet","RHS_UAZ469_Stress_INT_SoundSet","RHS_UAZ469_Rain_INT_SoundSet","RHS_UAZ469_Tires_Rock_Fast_INT_SoundSet","RHS_UAZ469_Tires_Grass_Fast_INT_SoundSet","RHS_UAZ469_Tires_Sand_Fast_INT_SoundSet","RHS_UAZ469_Tires_Gravel_Fast_INT_SoundSet","RHS_UAZ469_Tires_Mud_Fast_INT_SoundSet","RHS_UAZ469_Tires_Asphalt_Fast_INT_SoundSet","RHS_UAZ469_Tires_Water_Fast_INT_SoundSet","RHS_UAZ469_Tires_Rock_Slow_INT_SoundSet","RHS_UAZ469_Tires_Grass_Slow_INT_SoundSet","RHS_UAZ469_Tires_Sand_Slow_INT_SoundSet","RHS_UAZ469_Tires_Gravel_Slow_INT_SoundSet","RHS_UAZ469_Tires_Mud_Slow_INT_SoundSet","RHS_UAZ469_Tires_Asphalt_Slow_INT_SoundSet","RHS_UAZ469_Tires_Water_Slow_INT_SoundSet","RHS_UAZ469_Tires_Turn_Hard_INT_SoundSet","RHS_UAZ469_Tires_Turn_Soft_INT_SoundSet","RHS_UAZ469_Tires_Brake_Hard_INT_SoundSet","RHS_UAZ469_Tires_Brake_Soft_INT_SoundSet","","Tires_Movement_Dirt_Int_01_SoundSet"],
        "soundsetsext": ["RHS_UAZ469_Engine_RPM0_EXT_SoundSet","RHS_UAZ469_Engine_RPM1_EXT_SoundSet","RHS_UAZ469_Engine_RPM2_EXT_SoundSet","RHS_UAZ469_Engine_RPM3_EXT_SoundSet","RHS_UAZ469_Engine_EXT_Burst_SoundSet","RHS_UAZ469_Rattling_EXT_SoundSet","RHS_UAZ469_Stress_EXT_SoundSet","RHS_UAZ469_Rain_EXT_SoundSet","RHS_UAZ469_Tires_Rock_Fast_EXT_SoundSet","RHS_UAZ469_Tires_Grass_Fast_EXT_SoundSet","RHS_UAZ469_Tires_Sand_Fast_EXT_SoundSet","RHS_UAZ469_Tires_Gravel_Fast_EXT_SoundSet","RHS_UAZ469_Tires_Mud_Fast_EXT_SoundSet","RHS_UAZ469_Tires_Asphalt_Fast_EXT_SoundSet","RHS_UAZ469_Tires_Water_Fast_EXT_SoundSet","RHS_UAZ469_Tires_Rock_Slow_EXT_SoundSet","RHS_UAZ469_Tires_Grass_Slow_EXT_SoundSet","RHS_UAZ469_Tires_Sand_Slow_EXT_SoundSet","RHS_UAZ469_Tires_Gravel_Slow_EXT_SoundSet","RHS_UAZ469_Tires_Mud_Slow_EXT_SoundSet","RHS_UAZ469_Tires_Asphalt_Slow_EXT_SoundSet","RHS_UAZ469_Tires_Water_Slow_EXT_SoundSet","RHS_UAZ469_Tires_Turn_Hard_EXT_SoundSet","RHS_UAZ469_Tires_Turn_Soft_EXT_SoundSet","RHS_UAZ469_Tires_Brake_Hard_EXT_SoundSet","RHS_UAZ469_Tires_Brake_Soft_EXT_SoundSet","","Tires_Movement_Dirt_Ext_01_SoundSet"]
    },
    # Class: CfgVehicles|RHS_UAZ_Base|Turrets [Indent level: 1],
    "turrets": {
        # Class: CfgVehicles|Car_F|Turrets|MainTurret [Indent level: 2]
        "mainturret": {
            "stabilizedinaxes": 4,
            "outgunnermayfire": 1,
            "memorypointgun": "machinegun",
            "body": "",
            "gun": "",
            "gunneraction": "ManActTestDriverOut",
            "gunnergetinaction": "GetInLow",
            "gunnergetoutaction": "GetOutLow",
            "gunbeg": "usti hlavne",
            "gunend": "konec hlavne",
            "soundservo": ["A3|sounds_f|dummysound",0.316228,1,15],
            "minelev": -5,
            "maxelev": 40,
            "minturn": -360,
            "maxturn": 360,
            "gunneropticsmodel": "A3|weapons_f|reticle|optics_empty",
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
            # Class: CfgVehicles|Car_F|Turrets|MainTurret|ViewOptics [Indent level: 3],
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
            # Class: CfgVehicles|Car_F|Turrets|MainTurret|ViewGunner [Indent level: 3],
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
            "gunnertype": "",
            "primaryobserver": 0,
            "weapons": [],
            "magazines": [],
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
            "primary": 1,
            "hasgunner": 1,
            "commanding": 1,
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
            "forcehidegunner": 0,
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
            "gunnerinaction": "ManActTestDriver",
            "memorypointgunneroptics": "gunnerview",
            "memorypointsgetingunner": "pos gunner",
            "memorypointsgetingunnerdir": "pos gunner dir",
            "selectionfireanim": "zasleh",
            "showcrewaim": 0
        }
    },
    "memorypointsgetincargo": ["pos codriver","pos cargo 2","pos cargo 2","pos cargo 1"],
    "memorypointsgetincargodir": ["pos codriver dir","pos cargo dir 2","pos cargo dir 2","pos cargo dir 1"],
    "driverdoor": "Door_LF",
    "cargodoors": ["Door_RF","Door_LB","Door_LB","Door_RB"],
    "drivercompartments": "Compartment1",
    "cargocompartments": ["Compartment1","Compartment2","Compartment2","Compartment2","Compartment2","Compartment2"],
    # Class: CfgVehicles|RHS_UAZ_Base|AnimationSources [Indent level: 1],
    "animationsources": {
        # Class: CfgVehicles|RHS_UAZ_Base|AnimationSources|longlights_hide [Indent level: 2]
        "longlights_hide": {
            "source": "user",
            "animperiod": 1e-006,
            "initphase": 1
        },
        # Class: CfgVehicles|RHS_UAZ_Base|AnimationSources|shortlights_hide [Indent level: 2],
        "shortlights_hide": {
            "initphase": 0,
            "source": "user",
            "animperiod": 1e-006
        },
        # Class: CfgVehicles|RHS_UAZ_Base|AnimationSources|lights_hide [Indent level: 2],
        "lights_hide": {
            "initphase": 0,
            "source": "user",
            "animperiod": 1e-006
        },
        # Class: CfgVehicles|RHS_UAZ_Base|AnimationSources|searchlight_hide [Indent level: 2],
        "searchlight_hide": {
            "source": "user",
            "animperiod": 1e-006,
            "initphase": 1
        },
        # Class: CfgVehicles|RHS_UAZ_Base|AnimationSources|cabinlights_hide [Indent level: 2],
        "cabinlights_hide": {
            "source": "user",
            "animperiod": 1e-006,
            "initphase": 1
        },
        # Class: CfgVehicles|RHS_UAZ_Base|AnimationSources|searchlight_rot [Indent level: 2],
        "searchlight_rot": {
            "source": "user",
            "animperiod": 1,
            "initphase": 0
        },
        # Class: CfgVehicles|RHS_UAZ_Base|AnimationSources|HitLFWheel [Indent level: 2],
        "hitlfwheel": {
            "source": "Hit",
            "hitpoint": "HitLFWheel",
            "raw": 1
        },
        # Class: CfgVehicles|RHS_UAZ_Base|AnimationSources|HitRFWheel [Indent level: 2],
        "hitrfwheel": {
            "hitpoint": "HitRFWheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|RHS_UAZ_Base|AnimationSources|HitLBWheel [Indent level: 2],
        "hitlbwheel": {
            "hitpoint": "HitLF2Wheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|RHS_UAZ_Base|AnimationSources|HitRBWheel [Indent level: 2],
        "hitrbwheel": {
            "hitpoint": "HitRF2Wheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|RHS_UAZ_Base|AnimationSources|HitLF2Wheel [Indent level: 2],
        "hitlf2wheel": {
            "hitpoint": "HitLBWheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|RHS_UAZ_Base|AnimationSources|HitRF2Wheel [Indent level: 2],
        "hitrf2wheel": {
            "hitpoint": "HitRBWheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|RHS_UAZ_Base|AnimationSources|HitLMWheel [Indent level: 2],
        "hitlmwheel": {
            "hitpoint": "HitLMWheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|RHS_UAZ_Base|AnimationSources|HitRMWheel [Indent level: 2],
        "hitrmwheel": {
            "hitpoint": "HitRMWheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|RHS_UAZ_Base|AnimationSources|HitSpare [Indent level: 2],
        "hitspare": {
            "hitpoint": "HitSpare",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|RHS_UAZ_Base|AnimationSources|UseSpare [Indent level: 2],
        "usespare": {
            "hitpoint": "UseSpare",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|RHS_UAZ_Base|AnimationSources|HitGlass1 [Indent level: 2],
        "hitglass1": {
            "source": "Hit",
            "hitpoint": "HitGlass1",
            "raw": 1
        },
        # Class: CfgVehicles|RHS_UAZ_Base|AnimationSources|HitGlass2 [Indent level: 2],
        "hitglass2": {
            "hitpoint": "HitGlass2",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|RHS_UAZ_Base|AnimationSources|HitGlass3 [Indent level: 2],
        "hitglass3": {
            "hitpoint": "HitGlass3",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|RHS_UAZ_Base|AnimationSources|HitGlass4 [Indent level: 2],
        "hitglass4": {
            "hitpoint": "HitGlass4",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|RHS_UAZ_Base|AnimationSources|HitGlass5 [Indent level: 2],
        "hitglass5": {
            "hitpoint": "HitGlass5",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|RHS_UAZ_Base|AnimationSources|HitGlass6 [Indent level: 2],
        "hitglass6": {
            "hitpoint": "HitGlass6",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|RHS_UAZ_Base|AnimationSources|HitDoor_1_1 [Indent level: 2],
        "hitdoor_1_1": {
            "hitpoint": "HitDoor_1_1",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|RHS_UAZ_Base|AnimationSources|HitDoor_1_2 [Indent level: 2],
        "hitdoor_1_2": {
            "hitpoint": "HitDoor_1_2",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|RHS_UAZ_Base|AnimationSources|HitDoor_2_1 [Indent level: 2],
        "hitdoor_2_1": {
            "hitpoint": "HitDoor_2_1",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|RHS_UAZ_Base|AnimationSources|HitDoor_2_2 [Indent level: 2],
        "hitdoor_2_2": {
            "hitpoint": "HitDoor_2_2",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|RHS_UAZ_Base|AnimationSources|HitHood [Indent level: 2],
        "hithood": {
            "hitpoint": "HitHood",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|RHS_UAZ_Base|AnimationSources|Door_LF [Indent level: 2],
        "door_lf": {
            "source": "door",
            "animperiod": 0.8,
            "sound": "RHS_UAZ_Door",
            "soundposition": "osa_dvere_lp"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|AnimationSources|Door_RF [Indent level: 2],
        "door_rf": {
            "soundposition": "osa_dvere_pp",
            "source": "door",
            "animperiod": 0.8,
            "sound": "RHS_UAZ_Door"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|AnimationSources|Door_LB [Indent level: 2],
        "door_lb": {
            "soundposition": "osa_dvere_lz",
            "source": "door",
            "animperiod": 0.8,
            "sound": "RHS_UAZ_Door"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|AnimationSources|Door_RB [Indent level: 2],
        "door_rb": {
            "soundposition": "osa_dvere_pz",
            "source": "door",
            "animperiod": 0.8,
            "sound": "RHS_UAZ_Door"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|AnimationSources|gearbox [Indent level: 2],
        "gearbox": {
            "sound": "RHS_gearbox",
            "soundposition": "gear_axis",
            "source": "door",
            "animperiod": 0.8
        },
        # Class: CfgVehicles|RHS_UAZ_Base|AnimationSources|wiper [Indent level: 2],
        "wiper": {
            "source": "user",
            "animperiod": 1,
            "initphase": 0
        },
        # Class: CfgVehicles|RHS_UAZ_Base|AnimationSources|spare_hide [Indent level: 2],
        "spare_hide": {
            "mass": 1,
            "animperiod": 1e-011,
            "displayname": "hide spare wheel",
            "source": "user",
            "initphase": 0
        },
        # Class: CfgVehicles|RHS_UAZ_Base|AnimationSources|light_hide [Indent level: 2],
        "light_hide": {
            "displayname": "hide light covers",
            "onphasechanged": "(_this select 0) animateSource ['light_hide',(_this select 1),true];",
            "mass": 1,
            "animperiod": 1e-011,
            "source": "user",
            "initphase": 0
        },
        # Class: CfgVehicles|RHS_UAZ_Base|AnimationSources|wipers [Indent level: 2],
        "wipers": {
            "animperiod": 1,
            "sound": "RHS_Wipers",
            "soundposition": "wiper_1_axis",
            "source": "door"
        }
    },
    "armor": 52,
    "mintotaldamagethreshold": 0.21,
    "wheeldamageradiuscoef": 0.9,
    "wheeldestroyradiuscoef": 0.4,
    "crewcrashprotection": 0.25,
    "fuelexplosionpower": 0.1,
    # Class: CfgVehicles|RHS_UAZ_Base|HitPoints [Indent level: 1],
    "hitpoints": {
        # Class: CfgVehicles|RHS_UAZ_Base|HitPoints|HitLFWheel [Indent level: 2]
        "hitlfwheel": {
            "radius": 0.15,
            "armor": 0.175,
            "passthrough": 0.3,
            "visual": "wheel_1_1_damage",
            "armorcomponent": "wheel_1_1_hide",
            "minimalhit": -0.00833333,
            "explosionshielding": 4,
            "material": -1,
            "name": "wheel_1_1_steering"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|HitPoints|HitLF2Wheel [Indent level: 2],
        "hitlf2wheel": {
            "radius": 0.15,
            "armor": 0.175,
            "passthrough": 0.3,
            "visual": "wheel_1_2_damage",
            "armorcomponent": "wheel_1_2_hide",
            "minimalhit": -0.00833333,
            "explosionshielding": 4,
            "material": -1,
            "name": "wheel_1_2_steering"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|HitPoints|HitRFWheel [Indent level: 2],
        "hitrfwheel": {
            "radius": 0.15,
            "armor": 0.175,
            "passthrough": 0.3,
            "visual": "wheel_2_1_damage",
            "armorcomponent": "wheel_2_1_hide",
            "minimalhit": -0.00833333,
            "explosionshielding": 4,
            "material": -1,
            "name": "wheel_2_1_steering"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|HitPoints|HitRF2Wheel [Indent level: 2],
        "hitrf2wheel": {
            "radius": 0.15,
            "armor": 0.175,
            "passthrough": 0.3,
            "visual": "wheel_2_2_damage",
            "armorcomponent": "wheel_2_2_hide",
            "minimalhit": -0.00833333,
            "explosionshielding": 4,
            "material": -1,
            "name": "wheel_2_2_steering"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|HitPoints|HitSpare [Indent level: 2],
        "hitspare": {
            "name": "spare1",
            "visual": "-",
            "radius": 0.15,
            "armor": 0.175,
            "passthrough": 0.3,
            "armorcomponent": "wheel_2_2_hide",
            "minimalhit": -0.00833333,
            "explosionshielding": 4,
            "material": -1
        },
        # Class: CfgVehicles|RHS_UAZ_Base|HitPoints|UseSpare [Indent level: 2],
        "usespare": {
            "name": "",
            "visual": "-",
            "armor": 1,
            "radius": 0.15,
            "passthrough": 0.3,
            "armorcomponent": "wheel_2_2_hide",
            "minimalhit": -0.00833333,
            "explosionshielding": 4,
            "material": -1
        },
        # Class: CfgVehicles|RHS_UAZ_Base|HitPoints|HitLightL [Indent level: 2],
        "hitlightl": {
            "armor": 0.02,
            "minimalhit": 0.1,
            "material": -1,
            "name": "L svetlo",
            "visual": "-",
            "passthrough": 0,
            "radius": 0.1
        },
        # Class: CfgVehicles|RHS_UAZ_Base|HitPoints|HitLightR [Indent level: 2],
        "hitlightr": {
            "name": "P svetlo",
            "armor": 0.02,
            "minimalhit": 0.1,
            "material": -1,
            "visual": "-",
            "passthrough": 0,
            "radius": 0.1
        },
        # Class: CfgVehicles|RHS_UAZ_Base|HitPoints|HitSearchlight [Indent level: 2],
        "hitsearchlight": {
            "name": "searchlight",
            "armor": 0.02,
            "minimalhit": 0.1,
            "material": -1,
            "visual": "-",
            "passthrough": 0,
            "radius": 0.1
        },
        # Class: CfgVehicles|RHS_UAZ_Base|HitPoints|HitHull [Indent level: 2],
        "hithull": {
            "armor": 0.5,
            "material": -1,
            "name": "hull",
            "visual": "-",
            "passthrough": 0.2,
            "radius": 0.1
        },
        # Class: CfgVehicles|RHS_UAZ_Base|HitPoints|HitFuel [Indent level: 2],
        "hitfuel": {
            "armor": 0.5,
            "material": -1,
            "name": "Hit_Fuel",
            "visual": "-",
            "passthrough": 0.2,
            "radius": 0.1
        },
        # Class: CfgVehicles|RHS_UAZ_Base|HitPoints|HitEngine [Indent level: 2],
        "hitengine": {
            "armor": 0.5,
            "material": -1,
            "name": "Hit_Engine",
            "armorcomponent": "Hit_Engine",
            "visual": "zbytek",
            "passthrough": 0.2,
            "radius": 0.16,
            # Class: CfgVehicles|RHS_UAZ_Base|HitPoints|HitEngine|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|RHS_UAZ_Base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Smoke [Indent level: 4],
                "rhs_engine_smoke": {
                    "simulation": "particles",
                    "type": "SmallWreckSmoke",
                    "position": "engine_smoke",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|RHS_UAZ_Base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Smoke_small1 [Indent level: 4],
                "rhs_engine_smoke_small1": {
                    "type": "WeaponWreckSmoke",
                    "position": "engine_smoke2",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|RHS_UAZ_Base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Smoke_small2 [Indent level: 4],
                "rhs_engine_smoke_small2": {
                    "position": "engine_smoke3",
                    "type": "WeaponWreckSmoke",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|RHS_UAZ_Base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Sounds [Indent level: 4],
                "rhs_engine_sounds": {
                    "simulation": "sound",
                    "type": "SmokeWreck1",
                    "position": "engine_smoke",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                }
            }
        },
        # Class: CfgVehicles|RHS_UAZ_Base|HitPoints|HitBody [Indent level: 2],
        "hitbody": {
            "name": "karoserie",
            "visual": "camo1",
            "passthrough": 1,
            "radius": 0.1,
            "armor": 1,
            "material": -1,
            "explosionshielding": 1.5
        },
        # Class: CfgVehicles|RHS_UAZ_Base|HitPoints|HitGlass1 [Indent level: 2],
        "hitglass1": {
            "armor": 0.1,
            "radius": 0.2,
            "material": -1,
            "name": "glass1",
            "visual": "glass1",
            "passthrough": 0,
            "explosionshielding": 2
        },
        # Class: CfgVehicles|RHS_UAZ_Base|HitPoints|HitGlass2 [Indent level: 2],
        "hitglass2": {
            "armor": 0.05,
            "radius": 0.2,
            "material": -1,
            "name": "glass2",
            "visual": "glass2",
            "passthrough": 0,
            "explosionshielding": 2
        },
        # Class: CfgVehicles|RHS_UAZ_Base|HitPoints|HitGlass3 [Indent level: 2],
        "hitglass3": {
            "armor": 0.05,
            "radius": 0.2,
            "material": -1,
            "name": "glass3",
            "visual": "glass3",
            "passthrough": 0,
            "explosionshielding": 2
        },
        # Class: CfgVehicles|RHS_UAZ_Base|HitPoints|HitGlass4 [Indent level: 2],
        "hitglass4": {
            "visual": "glass4",
            "armor": 0.05,
            "radius": 0.2,
            "material": -1,
            "name": "glass4",
            "passthrough": 0,
            "explosionshielding": 2
        },
        # Class: CfgVehicles|RHS_UAZ_Base|HitPoints|HitGlass5 [Indent level: 2],
        "hitglass5": {
            "armor": 0.05,
            "radius": 0.2,
            "material": -1,
            "name": "glass5",
            "visual": "glass5",
            "passthrough": 0,
            "explosionshielding": 2
        },
        # Class: CfgVehicles|RHS_UAZ_Base|HitPoints|HitGlass6 [Indent level: 2],
        "hitglass6": {
            "armor": 0.05,
            "radius": 0.2,
            "material": -1,
            "name": "glass6",
            "visual": "glass6",
            "passthrough": 0,
            "explosionshielding": 2
        },
        # Class: CfgVehicles|RHS_UAZ_Base|HitPoints|HitDoor_1_1 [Indent level: 2],
        "hitdoor_1_1": {
            "armor": 0.2,
            "minimalhit": 0.075,
            "material": -1,
            "name": "door11",
            "visual": "-",
            "passthrough": 0.1,
            "radius": 0.17,
            "explosionshielding": 0.5
        },
        # Class: CfgVehicles|RHS_UAZ_Base|HitPoints|HitDoor_1_2 [Indent level: 2],
        "hitdoor_1_2": {
            "name": "door12",
            "armor": 0.2,
            "minimalhit": 0.075,
            "material": -1,
            "visual": "-",
            "passthrough": 0.1,
            "radius": 0.17,
            "explosionshielding": 0.5
        },
        # Class: CfgVehicles|RHS_UAZ_Base|HitPoints|HitDoor_2_1 [Indent level: 2],
        "hitdoor_2_1": {
            "name": "door21",
            "armor": 0.2,
            "minimalhit": 0.075,
            "material": -1,
            "visual": "-",
            "passthrough": 0.1,
            "radius": 0.17,
            "explosionshielding": 0.5
        },
        # Class: CfgVehicles|RHS_UAZ_Base|HitPoints|HitDoor_2_2 [Indent level: 2],
        "hitdoor_2_2": {
            "name": "door22",
            "armor": 0.2,
            "minimalhit": 0.075,
            "material": -1,
            "visual": "-",
            "passthrough": 0.1,
            "radius": 0.17,
            "explosionshielding": 0.5
        },
        # Class: CfgVehicles|RHS_UAZ_Base|HitPoints|Hithood [Indent level: 2],
        "hithood": {
            "armor": 0.3,
            "name": "hood1",
            "minimalhit": 0.075,
            "material": -1,
            "visual": "-",
            "passthrough": 0.1,
            "radius": 0.17,
            "explosionshielding": 0.5
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
        # Class: CfgVehicles|Car_F|HitPoints|HitLBWheel [Indent level: 2],
        "hitlbwheel": {
            "armor": 0.2,
            "material": -1,
            "name": "wheel_1_4_steering",
            "visual": "-",
            "passthrough": 0.3,
            "explosionshielding": 4
        },
        # Class: CfgVehicles|Car_F|HitPoints|HitLMWheel [Indent level: 2],
        "hitlmwheel": {
            "armor": 0.2,
            "material": -1,
            "name": "wheel_1_3_steering",
            "visual": "-",
            "passthrough": 0.3,
            "explosionshielding": 4
        },
        # Class: CfgVehicles|Car_F|HitPoints|HitRBWheel [Indent level: 2],
        "hitrbwheel": {
            "armor": 0.2,
            "material": -1,
            "name": "wheel_2_4_steering",
            "visual": "-",
            "passthrough": 0.3,
            "explosionshielding": 4
        },
        # Class: CfgVehicles|Car_F|HitPoints|HitRMWheel [Indent level: 2],
        "hitrmwheel": {
            "armor": 0.2,
            "material": -1,
            "name": "wheel_2_3_steering",
            "visual": "-",
            "passthrough": 0.3,
            "explosionshielding": 4
        }
    },
    "cargoaction": ["RHS_UAZ_Cargo01","RHS_UAZ_Cargo01","RHS_UAZ_Cargo01","RHS_UAZ_Cargo01","RHS_UAZ_Cargo01","RHS_UAZ_Cargo02"],
    "getinaction": "GetInOffroad",
    "getoutaction": "GetOutLow",
    "cargogetinaction": ["GetInLow"],
    "cargogetoutaction": ["GetOutLow"],
    "memorypointtrackfll": "TrackFLL",
    "memorypointtrackflr": "TrackFLR",
    "memorypointtrackbll": "TrackBLL",
    "memorypointtrackblr": "TrackBLR",
    "memorypointtrackfrl": "TrackFRL",
    "memorypointtrackfrr": "TrackFRR",
    "memorypointtrackbrl": "TrackBRL",
    "memorypointtrackbrr": "TrackBRR",
    # Class: CfgVehicles|RHS_UAZ_Base|Damage [Indent level: 1],
    "damage": {
        "tex": [],
        "mat": ["rhsafrf|addons|rhs_a2port_car|UAZ|Data|uaz_skla.rvmat","a3|data_f|glass_veh_armored_damage.rvmat","a3|data_f|glass_veh_armored_damage.rvmat","rhsafrf|addons|rhs_a2port_car|UAZ|Data|uaz_skla_in.rvmat","a3|data_f|glass_veh_armored_damage.rvmat","a3|data_f|glass_veh_armored_damage.rvmat","rhsafrf|addons|rhs_a2port_car|UAZ|Data|uaz_main_metal.rvmat","rhsafrf|addons|rhs_a2port_car|UAZ|Data|uaz_main_metal_damage.rvmat","rhsafrf|addons|rhs_a2port_car|UAZ|Data|uaz_main_metal_destruct.rvmat","rhsafrf|addons|rhs_a2port_car|UAZ|Data|uaz_other_metal.rvmat","rhsafrf|addons|rhs_a2port_car|UAZ|Data|uaz_other_metal_damage.rvmat","rhsafrf|addons|rhs_a2port_car|UAZ|Data|uaz_other_metal_destruct.rvmat","rhsafrf|addons|rhs_a2port_car|data|drziaky.rvmat","rhsafrf|addons|rhs_a2port_car|data|drziaky.rvmat","rhsafrf|addons|rhs_a2port_car|data|drziaky_destruct.rvmat","rhsafrf|addons|rhs_a2port_car|UAZ|Data|uaz_mount.rvmat","rhsafrf|addons|rhs_a2port_car|UAZ|Data|uaz_mount_damage.rvmat","rhsafrf|addons|rhs_a2port_car|UAZ|Data|uaz_mount_destruct.rvmat","rhsafrf|addons|rhs_a2port_car|UAZ|Data|rhs_uaz_wheels.rvmat","rhsafrf|addons|rhs_a2port_car|UAZ|Data|rhs_uaz_wheels_damage.rvmat","rhsafrf|addons|rhs_a2port_car|UAZ|Data|rhs_uaz_wheels_damage.rvmat"]
    },
    # Class: CfgVehicles|RHS_UAZ_Base|Exhausts [Indent level: 1],
    "exhausts": {
        # Class: CfgVehicles|RHS_UAZ_Base|Exhausts|Exhaust1 [Indent level: 2]
        "exhaust1": {
            "position": "vyfuk start",
            "direction": "vyfuk konec",
            "effect": "ExhaustEffectOffroad"
        }
    },
    # Class: CfgVehicles|RHS_UAZ_Base|Reflectors [Indent level: 1],
    "reflectors": {
        # Class: CfgVehicles|RHS_UAZ_Base|Reflectors|LSvetla [Indent level: 2]
        "lsvetla": {
            "color": [800,900,650],
            "ambient": [2,2,2],
            "position": "L svetlo",
            "direction": "konec L svetla",
            "hitpoint": "L svetlo",
            "hitpointclass": "HitLightL",
            "selection": "L svetlo",
            "size": 1,
            "innerangle": 30,
            "outerangle": 100,
            "conefadecoef": 10,
            "intensity": 1.5,
            "useflare": 1,
            "daylight": 0,
            "flaresize": 0.85,
            # Class: CfgVehicles|RHS_UAZ_Base|Reflectors|LSvetla|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardlimitstart": 30,
                "hardlimitend": 60
            }
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Reflectors|RSvetla [Indent level: 2],
        "rsvetla": {
            "position": "P svetlo",
            "direction": "konec P svetla",
            "hitpoint": "P svetlo",
            "hitpointclass": "HitLightR",
            "selection": "P svetlo",
            "innerangle": 40,
            "outerangle": 120,
            "intensity": 2.5,
            "color": [800,900,650],
            "ambient": [2,2,2],
            "size": 1,
            "conefadecoef": 10,
            "useflare": 1,
            "daylight": 0,
            "flaresize": 0.85,
            # Class: CfgVehicles|RHS_UAZ_Base|Reflectors|LSvetla|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardlimitstart": 30,
                "hardlimitend": 60
            }
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Reflectors|Right2 [Indent level: 2],
        "right2": {
            "position": "Light_R_Flare",
            "direction": "Light_R_Flare_end",
            "useflare": 1,
            "innerangle": 50,
            "outerangle": 179,
            "conefadecoef": 51,
            "intensity": 1,
            # Class: CfgVehicles|RHS_UAZ_Base|Reflectors|Right2|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 50,
                "hardlimitstart": 0,
                "hardlimitend": 3
            },
            "hitpoint": "P svetlo",
            "hitpointclass": "HitLightR",
            "selection": "P svetlo",
            "color": [800,900,650],
            "ambient": [2,2,2],
            "size": 1,
            "daylight": 0,
            "flaresize": 0.85
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Reflectors|Left2 [Indent level: 2],
        "left2": {
            "position": "Light_L_Flare",
            "direction": "Light_L_Flare_end",
            "useflare": 1,
            "innerangle": 50,
            "outerangle": 179,
            "conefadecoef": 51,
            "intensity": 1,
            # Class: CfgVehicles|RHS_UAZ_Base|Reflectors|Left2|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 50,
                "hardlimitstart": 0,
                "hardlimitend": 3
            },
            "color": [800,900,650],
            "ambient": [2,2,2],
            "hitpoint": "L svetlo",
            "hitpointclass": "HitLightL",
            "selection": "L svetlo",
            "size": 1,
            "daylight": 0,
            "flaresize": 0.85
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Reflectors|Searchlight [Indent level: 2],
        "searchlight": {
            "position": "Searchlight_pos",
            "direction": "Searchlight_dir",
            "hitpoint": "Searchlight",
            "hitpointclass": "HitSearchlight",
            "selection": "Searchlight",
            "useflare": 1,
            "innerangle": 35,
            "outerangle": 179,
            "color": [800,900,650],
            "ambient": [2,2,2],
            "size": 1,
            "conefadecoef": 10,
            "intensity": 1.5,
            "daylight": 0,
            "flaresize": 0.85,
            # Class: CfgVehicles|RHS_UAZ_Base|Reflectors|LSvetla|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardlimitstart": 30,
                "hardlimitend": 60
            }
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Reflectors|Long_Left [Indent level: 2],
        "long_left": {
            "color": [800,900,650],
            "ambient": [5,5,5],
            "position": "Light_L_Long",
            "direction": "Light_L_Long_end",
            "hitpoint": "L svetlo",
            "hitpointclass": "HitLightL",
            "selection": "L svetlo",
            "size": 1,
            "innerangle": 22,
            "outerangle": 29,
            "conefadecoef": 1,
            "intensity": 100,
            "useflare": 0,
            "daylight": 0,
            "flaresize": 1.5,
            "flaremaxdistance": 750,
            # Class: CfgVehicles|RHS_UAZ_Base|Reflectors|Long_Left|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0.1,
                "quadratic": 0,
                "hardlimitstart": 500,
                "hardlimitend": 750
            }
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Reflectors|Long_Right [Indent level: 2],
        "long_right": {
            "position": "Light_R_Long",
            "direction": "Light_R_Long_end",
            "hitpoint": "P svetlo",
            "hitpointclass": "HitLightR",
            "selection": "P svetlo",
            "color": [800,900,650],
            "ambient": [5,5,5],
            "size": 1,
            "innerangle": 22,
            "outerangle": 29,
            "conefadecoef": 1,
            "intensity": 100,
            "useflare": 0,
            "daylight": 0,
            "flaresize": 1.5,
            "flaremaxdistance": 750,
            # Class: CfgVehicles|RHS_UAZ_Base|Reflectors|Long_Left|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0.1,
                "quadratic": 0,
                "hardlimitstart": 500,
                "hardlimitend": 750
            }
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Reflectors|Long_Right2 [Indent level: 2],
        "long_right2": {
            "useflare": 1,
            "position": "light_R_Long_flare",
            "innerangle": 50,
            "outerangle": 139,
            "conefadecoef": 51,
            "flaresize": 1,
            "intensity": 1,
            # Class: CfgVehicles|RHS_UAZ_Base|Reflectors|Long_Right2|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 50,
                "hardlimitstart": 0,
                "hardlimitend": 3
            },
            "direction": "Light_R_Long_end",
            "hitpoint": "P svetlo",
            "hitpointclass": "HitLightR",
            "selection": "P svetlo",
            "color": [800,900,650],
            "ambient": [5,5,5],
            "size": 1,
            "daylight": 0,
            "flaremaxdistance": 750
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Reflectors|Long_Left2 [Indent level: 2],
        "long_left2": {
            "useflare": 1,
            "position": "light_L_Long_flare",
            "innerangle": 50,
            "outerangle": 139,
            "conefadecoef": 51,
            "flaresize": 1,
            "intensity": 1,
            # Class: CfgVehicles|RHS_UAZ_Base|Reflectors|Long_Left2|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 50,
                "hardlimitstart": 0,
                "hardlimitend": 3
            },
            "color": [800,900,650],
            "ambient": [5,5,5],
            "direction": "Light_L_Long_end",
            "hitpoint": "L svetlo",
            "hitpointclass": "HitLightL",
            "selection": "L svetlo",
            "size": 1,
            "daylight": 0,
            "flaremaxdistance": 750
        }
    },
    "aggregatereflectors": [["LSvetla"],["Left2"],["RSvetla"],["Right2"],["Long_Left2","Long_Right2"]],
    "armorlights": 0.05,
    # Class: CfgVehicles|RHS_UAZ_Base|RenderTargets [Indent level: 1],
    "rendertargets": {
        # Class: CfgVehicles|RHS_UAZ_Base|RenderTargets|LeftMirror [Indent level: 2]
        "leftmirror": {
            "rendertarget": "rendertarget0",
            # Class: CfgVehicles|RHS_UAZ_Base|RenderTargets|LeftMirror|CameraView1 [Indent level: 3],
            "cameraview1": {
                "pointposition": "m1p",
                "pointdirection": "m1d",
                "renderquality": 1,
                "rendervisionmode": 4,
                "fov": 0.7
            },
            "bboxes": ["PIP_1_TL","PIP_1_TR","PIP_1_BL","PIP_1_BR"]
        },
        # Class: CfgVehicles|RHS_UAZ_Base|RenderTargets|RightMirror [Indent level: 2],
        "rightmirror": {
            "rendertarget": "rendertarget1",
            # Class: CfgVehicles|RHS_UAZ_Base|RenderTargets|RightMirror|CameraView1 [Indent level: 3],
            "cameraview1": {
                "pointposition": "m2p",
                "pointdirection": "m2d",
                "renderquality": 1,
                "rendervisionmode": 4,
                "fov": 0.7
            },
            "bboxes": ["PIP_2_TL","PIP_2_TR","PIP_2_BL","PIP_2_BR"]
        },
        # Class: CfgVehicles|RHS_UAZ_Base|RenderTargets|BackMirror [Indent level: 2],
        "backmirror": {
            "rendertarget": "rendertarget2",
            # Class: CfgVehicles|RHS_UAZ_Base|RenderTargets|BackMirror|CameraView1 [Indent level: 3],
            "cameraview1": {
                "pointposition": "m3p",
                "pointdirection": "m3d",
                "renderquality": 0,
                "rendervisionmode": 4,
                "fov": 0.7
            },
            "bboxes": ["PIP_3_TL","PIP_3_TR","PIP_3_BL","PIP_3_BR"]
        }
    },
    # Class: CfgVehicles|RHS_UAZ_Base|UserActions [Indent level: 1],
    "useractions": {
        # Class: CfgVehicles|RHS_UAZ_Base|UserActions|wiperson [Indent level: 2]
        "wiperson": {
            "displayname": "Wipers on",
            "position": "",
            "radius": 2,
            "priority": 1.5,
            "showwindow": 0,
            "onlyforplayer": 1,
            "condition": "(player == driver this) AND isengineon (this) AND this animationPhase 'wipers' < 0.5",
            "statement": "[this,0] spawn rhs_fnc_wipers"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|UserActions|wipersoff [Indent level: 2],
        "wipersoff": {
            "displayname": "Wipers off",
            "condition": "(player == driver this) AND this animationPhase 'wipers' > 0.5",
            "statement": "[this,1] spawn rhs_fnc_wipers",
            "position": "",
            "radius": 2,
            "priority": 1.5,
            "showwindow": 0,
            "onlyforplayer": 1
        },
        # Class: CfgVehicles|RHS_UAZ_Base|UserActions|lights_toggle [Indent level: 2],
        "lights_toggle": {
            "displayname": "Toggle short/long lights",
            "position": "",
            "shortcut": "vehLockTargets",
            "radius": 12,
            "priority": 1.5,
            "showwindow": 0,
            "onlyforplayer": 1,
            "condition": "((call rhs_fnc_findPlayer) == driver this) AND (isLightOn this)",
            "statement": "[this,2] call rhs_fnc_carLightToggle"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|UserActions|searchlight_toggle [Indent level: 2],
        "searchlight_toggle": {
            "shortcut": "lockTarget",
            "displayname": "Toggle searchlight",
            "statement": "[this,3] call rhs_fnc_carLightToggle",
            "position": "",
            "radius": 12,
            "priority": 1.5,
            "showwindow": 0,
            "onlyforplayer": 1,
            "condition": "((call rhs_fnc_findPlayer) == driver this) AND (isLightOn this)"
        },
        # Class: CfgVehicles|RHS_UAZ_Base|UserActions|searchlight_adjust [Indent level: 2],
        "searchlight_adjust": {
            "shortcut": "",
            "displayname": "Adjust searchlight",
            "condition": "((call rhs_fnc_findPlayer) == driver this) AND (isLightOn this) AND (this animationPhase 'searchlight_hide' == 0)",
            "statement": "[this] spawn rhs_fnc_adjustSearchlight",
            "position": "",
            "radius": 12,
            "priority": 1.5,
            "showwindow": 0,
            "onlyforplayer": 1
        }
    },
    # Class: CfgVehicles|RHS_UAZ_Base|RHS_TowingSystem [Indent level: 1],
    "rhs_towingsystem": {
        # Class: CfgVehicles|RHS_UAZ_Base|RHS_TowingSystem|Carrier [Indent level: 2]
        "carrier": {
            "rhs_maxcargomass": 800,
            "rhs_attachpoint": "",
            "rhs_attachpointpos": [0,-1.85,-0.55]
        }
    },
    "normalspeedforwardcoef": 0.8,
    "slowspeedforwardcoef": 0.45,
    "turncoef": 2.5,
    "terraincoef": 0.4,
    "waterspeedfactor": 0.4,
    "simulation": "carx",
    "dampersbumpcoef": 4,
    "precision": 10,
    "brakedistance": 3,
    "acceleration": 15,
    "fireresistance": 5,
    "maxspeed": 120,
    "fuelcapacity": 30,
    "rhs_fuelcapacity": 78,
    "wheelcircumference": 2.45,
    "brakeidlespeed": 0.5,
    "maxfordingdepth": 0,
    "waterresistance": 1,
    "waterresistancecoef": 0.2,
    "waterleakiness": 10,
    # Class: CfgVehicles|RHS_UAZ_Base|complexGearbox [Indent level: 1],
    "complexgearbox": {
        "gearboxratios": ["R1",-5.224,"N",0,"D1",3.78,"D2",2.6,"D3",1.55,"D4",1],
        "transmissionratios": ["High",5.125],
        "gearboxmode": "auto",
        "moveoffgear": 1,
        "drivestring": "D",
        "neutralstring": "N",
        "reversestring": "R"
    },
    "changegearmineffectivity": [0.95,0.15,0.85,0.95,0.95,0.95],
    "switchtime": 0.51,
    "latency": 1,
    "differentialtype": "all_limited",
    "frontrearsplit": 0.5,
    "frontbias": 1.5,
    "rearbias": 1.5,
    "centrebias": 1.3,
    "clutchstrength": 15,
    "transmissionlosses": 20,
    "dampingratefullthrottle": 0.08,
    "dampingratezerothrottleclutchengaged": 1.35,
    "dampingratezerothrottleclutchdisengaged": 0.35,
    "torquecurve": [[0.15,0.289017],[0.3,0.895954],[0.48,1],[0.52,1],[0.7,0.953757],[0.8,0.895954],[0.9,0.809249],[1,0.693642]],
    "enginepower": 67,
    "enginemoi": 1.1,
    "peaktorque": 173,
    "maxomega": 523.6,
    "minomega": 20,
    "idlerpm": 750,
    "redrpm": 5000,
    "enginelosses": 14,
    "thrustdelay": 0.2,
    "enginebrakecoef": 0.9,
    "accelaidforceyoffset": -0.85,
    "accelaidforcecoef": 5,
    "accelaidforcespd": 4.23,
    "antirollbarforcecoef": 0.5,
    "antirollbarforcelimit": 0.5,
    "antirollbarspeedmin": 10,
    "antirollbarspeedmax": 80,
    # Class: CfgVehicles|RHS_UAZ_Base|Wheels [Indent level: 1],
    "wheels": {
        # Class: CfgVehicles|RHS_UAZ_Base|Wheels|LF [Indent level: 2]
        "lf": {
            "side": "left",
            "bonename": "wheel_1_1_damper",
            "center": "wheel_1_1_axis",
            "boundary": "wheel_1_1_bound",
            "suspforceapppointoffset": "wheel_1_1_axis",
            "tireforceapppointoffset": "wheel_1_1_axis",
            "susptraveldirection": [-0.125,-1,0],
            "steering": 1,
            "width": 0.16,
            "mass": 20,
            "moi": 24,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 2000,
            "maxhandbraketorque": 0,
            "maxcompression": 0.2,
            "maxdroop": 0.1,
            "sprungmass": -1,
            "springstrength": 14000,
            "springdamperrate": 2400,
            "longitudinalstiffnessperunitgravity": 10000,
            "latstiffx": 2.5,
            "latstiffy": 18,
            "frictionvsslipgraph": [[0,1.2],[0.5,1.13],[1,1]]
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Wheels|LR [Indent level: 2],
        "lr": {
            "bonename": "wheel_1_2_damper",
            "steering": 0,
            "center": "wheel_1_2_axis",
            "boundary": "wheel_1_2_bound",
            "suspforceapppointoffset": "wheel_1_2_axis",
            "tireforceapppointoffset": "wheel_1_2_axis",
            "maxhandbraketorque": 3000,
            "side": "left",
            "susptraveldirection": [-0.125,-1,0],
            "width": 0.16,
            "mass": 20,
            "moi": 24,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 2000,
            "maxcompression": 0.2,
            "maxdroop": 0.1,
            "sprungmass": -1,
            "springstrength": 14000,
            "springdamperrate": 2400,
            "longitudinalstiffnessperunitgravity": 10000,
            "latstiffx": 2.5,
            "latstiffy": 18,
            "frictionvsslipgraph": [[0,1.2],[0.5,1.13],[1,1]]
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Wheels|RF [Indent level: 2],
        "rf": {
            "bonename": "wheel_2_1_damper",
            "center": "wheel_2_1_axis",
            "boundary": "wheel_2_1_bound",
            "suspforceapppointoffset": "wheel_2_1_axis",
            "tireforceapppointoffset": "wheel_2_1_axis",
            "steering": 1,
            "side": "right",
            "susptraveldirection": [0.125,-1,0],
            "width": 0.16,
            "mass": 20,
            "moi": 24,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 2000,
            "maxhandbraketorque": 0,
            "maxcompression": 0.2,
            "maxdroop": 0.1,
            "sprungmass": -1,
            "springstrength": 14000,
            "springdamperrate": 2400,
            "longitudinalstiffnessperunitgravity": 10000,
            "latstiffx": 2.5,
            "latstiffy": 18,
            "frictionvsslipgraph": [[0,1.2],[0.5,1.13],[1,1]]
        },
        # Class: CfgVehicles|RHS_UAZ_Base|Wheels|RR [Indent level: 2],
        "rr": {
            "bonename": "wheel_2_2_damper",
            "steering": 0,
            "center": "wheel_2_2_axis",
            "boundary": "wheel_2_2_bound",
            "suspforceapppointoffset": "wheel_2_2_axis",
            "tireforceapppointoffset": "wheel_2_2_axis",
            "maxhandbraketorque": 3000,
            "side": "right",
            "susptraveldirection": [0.125,-1,0],
            "width": 0.16,
            "mass": 20,
            "moi": 24,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 2000,
            "maxcompression": 0.2,
            "maxdroop": 0.1,
            "sprungmass": -1,
            "springstrength": 14000,
            "springdamperrate": 2400,
            "longitudinalstiffnessperunitgravity": 10000,
            "latstiffx": 2.5,
            "latstiffy": 18,
            "frictionvsslipgraph": [[0,1.2],[0.5,1.13],[1,1]]
        }
    },
    # Class: CfgVehicles|RHS_UAZ_Base|EventHandlers [Indent level: 1],
    "eventhandlers": {
        # Class: CfgVehicles|RHS_UAZ_Base|EventHandlers|RHS_EventHandlers [Indent level: 2]
        "rhs_eventhandlers": {
            "init": "_this call rhs_fnc_a2port_car_init",
            "postinit": "_this call rhs_fnc_reapplyTextures",
            "engine": "if(_this select 1)then{_this call RHS_fnc_gearSound};_this call rhs_fnc_engineCheckDamage;",
            "dammaged": "_this call rhs_fnc_wheelDamaged"
        },
        "init": "",
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');"
    },
    "attenuationeffecttype": "SemiOpenCarAttenuation2",
    "sounddammage": ["",0.562341,1],
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
    "_generalmacro": "Offroad_01_base_F",
    "namesound": "veh_car",
    # Class: CfgVehicles|Offroad_01_base_F|Library [Indent level: 1],
    "library": {
        "libtextdesc": "The 4x4 pickup by Generic Motors is a perfect choice for farmers and hunters. The durable chassis and powerful engine have been designed to withstand anything from the cratered highways of Central Europe to the rugged terrain of the Mediterranean. The armed version is fitted either with a .50 caliber heavy machine gun or an anti-tank recoilless rifle. It provides the combination of mobility and firepower to many paramilitary and guerilla forces in local conflicts around the globe. Specialized versions, which sport a hard rear cover and rack-mounted communications equipment, are in use by law enforcement, national park rangers, and armed forces. These vehicles feature a large floodlight, loudspeakers, and long-range antennas."
    },
    "weapons": ["SportCarHorn"],
    "memorypointtaskmarker": "TaskMarker_1_pos",
    "unitinfotype": "RscUnitInfoNoWeapon",
    "maximumload": 2500,
    # Class: CfgVehicles|Offroad_01_base_F|TransportItems [Indent level: 1],
    "transportitems": {
        # Class: CfgVehicles|Offroad_01_base_F|TransportItems|_xx_FirstAidKit [Indent level: 2]
        "_xx_firstaidkit": {
            "name": "FirstAidKit",
            "count": 4
        }
    },
    "shownvgcargo": [0,1],
    "extcameraposition": [0,2,-8.75],
    "camshakecoef": 0.8,
    "wheeldamagethreshold": 0.0416667,
    # Class: CfgVehicles|Offroad_01_base_F|PlayerSteeringCoefficients [Indent level: 1],
    "playersteeringcoefficients": {
        "turnincreaseconst": 0.7,
        "turnincreaselinear": 2.5,
        "turnincreasetime": 0,
        "turndecreaseconst": 8,
        "turndecreaselinear": 0,
        "turndecreasetime": 0,
        "maxturnhundred": 1
    },
    "cargoiscodriver": [1,0],
    "forcehidedriver": 1,
    "viewdriverinexternal": 1,
    "canhidedriver": 0,
    "occludesoundswhenin": 0,
    "obstructsoundswhenin": 0,
    "secondaryexplosion": -10,
    "dammagehalf": [],
    "dammagefull": [],
    "armorstructural": 4,
    "explosionshielding": 1,
    "crewexplosionprotection": 0.8,
    "gunnerhasflares": 0,
    "steeraheadsimul": 0.5,
    "steeraheadplan": 0.35,
    "predictturnplan": 2,
    "predictturnsimul": 1.5,
    "epeimpulsedamagecoef": 15,
    "drivercansee": "1 + 2 + 4 + 8 + 32",
    "gunnercansee": "1 + 2 + 4 + 8 + 32",
    "commandercansee": "1 + 2 + 4 + 8 + 32",
    # Class: CfgVehicles|Car_F|ViewPilot [Indent level: 1],
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
    "audible": 5,
    "magazines": [],
    "threat": [0,0,0],
    "soundenviron": ["",0.000562341,1],
    "soundcrash": ["A3|sounds_f|dummysound",1,1],
    "collisioneffect": "collisionEffect",
    "hideunitinfo": 0,
    "htmin": 60,
    "htmax": 1800,
    "afmax": 100,
    "mfmax": 80,
    "mfact": 1,
    "tbody": 150,
    "transportmaxweapons": 12,
    "transportmaxmagazines": 64,
    "supplyradius": -1,
    "memorypointsupply": "doplnovani",
    # Class: CfgVehicles|Car_F|TransportBackpacks [Indent level: 1],
    "transportbackpacks": {
    },
    # Class: CfgVehicles|Car_F|TransportMagazines [Indent level: 1],
    "transportmagazines": {
    },
    # Class: CfgVehicles|Car_F|TransportWeapons [Indent level: 1],
    "transportweapons": {
    },
    "braketorque": 6000,
    "longstiff": 15000,
    "latstiffx": 2000,
    "latstiffy": 18000,
    "wheelmask": "wheel_X_X",
    "numberphysicalwheels": 4,
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
    "canfloat": 0,
    "limitedspeedcoef": 0.5,
    "hulldamagecauseexplosion": 1,
    # Class: CfgVehicles|Car|PlateInfos [Indent level: 1],
    "plateinfos": {
        "name": "spz",
        "color": [0,0,0,0.75]
    },
    "selectionfireanim": "zasleh",
    "alphatracks": 0.2,
    "memorypointcirculumreference": "circulumReference",
    "gearbox": [-8,0,10,6.15,4.44,3.33],
    "scudeffect": "ScudEffect",
    "preferroads": 1,
    "formationx": 20,
    "formationz": 20,
    "type": 0,
    "typicalcargo": ["Soldier"],
    "scudmodel": "",
    "dampersize": 0.1,
    "damperforce": 1,
    "damperdamping": 1,
    "inputturncurve": [[0,[0,0,1,1]],[30,[0,0,0.2,0.008,0.4,0.032,0.6,0.216,0.8,0.512,1,1]]],
    "enablegps": 0,
    "soundengine": ["",1.77828,0.9],
    # Class: CfgVehicles|Car|SpeechVariants [Indent level: 1],
    "speechvariants": {
        # Class: CfgVehicles|Car|SpeechVariants|Default [Indent level: 2]
        "default": {
            "speechsingular": ["veh_vehicle_car_s"],
            "speechplural": ["veh_vehicle_car_p"]
        }
    },
    "textsingular": "car",
    "textplural": "cars",
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
    "wheeldestroythreshold": 0.99,
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
    "memorypointsgetindriver": "pos driver",
    "memorypointsgetindriverdir": "pos driver dir",
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
    "enablemanualfire": 1,
    "portrait": "",
    "ghostpreview": "",
    "destrtype": "DestructDefault",
    "crewvulnerable": 1,
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
    "artilleryscanner": 0,
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
    "waterlineardampingcoefx": 0,
    "waterlineardampingcoefy": 0,
    "waterangulardampingcoef": 0,
    "shownvgdriver": 0,
    "shownvgcommander": 0,
    "shownvggunner": 0,
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
    "driveropticsmodel": "",
    "driveropticseffect": [],
    "driveropticscolor": [1,1,1,1],
    "castdrivershadow": 0,
    "castcargoshadow": 0,
    "viewdrivershadow": 1,
    "viewdrivershadowdiff": 1,
    "viewdrivershadowamb": 1,
    "viewcargoshadow": 1,
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
    "waterdamageengine": 0.2,
    "damagetexdelay": 0,
    "coefinside": 2,
    "coefinsideheur": 2,
    "coefspeedinside": 2,
    "windsockexist": 0,
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