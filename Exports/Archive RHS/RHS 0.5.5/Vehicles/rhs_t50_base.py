rhs_t50_base = {
    "scope": 1,
    "dlc": "RHS_AFRF",
    "rhs_decalparameters": ["['Number',cRHSAIRT50NumberPlaces,'AviaBlue']","['Label', cRHSAIRT50SquadPlaces, 'AviationsSquadrons']","['Label', cRHSAIRT50StarPlaces, 'Aviation',1]"],
    "displayname": "T-50 obr. 2011",
    "model": "rhsafrf|addons|rhs_air|t50|t50",
    "picture": "rhsafrf|addons|rhs_air|t50|data|ui|pak_fa_icon.paa",
    "icon": "rhsafrf|addons|rhs_air|t50|data|ui|icomap_pakfa.paa",
    "lesh_canbetowed": 1,
    "lesh_towfromfront": 1,
    "lesh_axisoffsettarget": [0,6.8,-2.04],
    "lesh_wheeloffset": [0,-0.7],
    "category": "Air",
    "vehicleclass": "rhs_vehclass_aircraft",
    "memorypointsgetindriver": "pos driver",
    "memorypointsgetindriverdir": "pos driver dir",
    "memorypointsgetindriverprecise": "pos driver",
    "camshakecoef": 0.7,
    "drivercaneject": 1,
    "drivercompartments": 1,
    "driverlefthandanimname": "lever_pilot",
    "driverrighthandanimname": "stick_pilot",
    "driverleftleganimname": "pedal_L",
    "driverrightleganimname": "pedal_R",
    "driveraction": "rhs_PAKFA_Pilot",
    "getinaction": "RHS_PAKFA_Pilot_getin",
    "getoutaction": "pilot_plane_cas_02_Exit",
    "precisegetinout": 1,
    "allowtablock": 1,
    "destrtype": "DestructDefault",
    "selectiondamage": "zbytek",
    "incommingmissliedetectionsystem": "8+16",
    "ejectdamagelimit": 1,
    "driverweaponsinfotype": "RscOptics_CAS_01_TGP",
    "headaimdown": 6,
    "headgforceleaningfactor": [0.005,0.001,0.015],
    "slingloadcargomemorypoints": ["SlingLoadCargo1","SlingLoadCargo2","SlingLoadCargo3","SlingLoadCargo4"],
    "memorypointtaskmarker": "TaskMarker_1_pos",
    "memorypointlmissile": "missile_1",
    "memorypointlrocket": "rocket_1",
    "memorypointrmissile": "missile_2",
    "memorypointrrocket": "rocket_2",
    # Class: CfgVehicles|RHS_T50_base|EjectionSystem [Indent level: 1],
    "ejectionsystem": {
    },
    # Class: CfgVehicles|RHS_T50_base|Turrets [Indent level: 1],
    "turrets": {
    },
    # Class: CfgVehicles|RHS_T50_base|TransportItems [Indent level: 1],
    "transportitems": {
    },
    "threat": [1,1,1],
    "waterleakiness": 1.5,
    "showalltargets": 4,
    "laserscanner": 1,
    "extcameraposition": [0,4.1,-20],
    # Class: CfgVehicles|RHS_T50_base|Damage [Indent level: 1],
    "damage": {
        "tex": ["rhsafrf|addons|rhs_air|t50|data|afterburner_ca.paa","#(argb,8,8,3)color(0,0,0,0,co)"],
        "mat": ["rhsafrf|addons|rhs_air|t50|data|pakfa_glass.rvmat","rhsafrf|addons|rhs_air|t50|data|pakfa_glass_damage.rvmat","rhsafrf|addons|rhs_air|t50|data|pakfa_glass_destruct.rvmat","rhsafrf|addons|rhs_air|t50|data|PakFa.rvmat","rhsafrf|addons|rhs_air|t50|data|PakFa_damage.rvmat","rhsafrf|addons|rhs_air|t50|data|PakFa_destruct.rvmat","a3|data_f|default.rvmat","a3|data_f|default.rvmat","a3|data_f|default_destruct.rvmat"]
    },
    # Class: CfgVehicles|RHS_T50_base|UserActions [Indent level: 1],
    "useractions": {
        # Class: CfgVehicles|RHS_T50_base|UserActions|MFD_top [Indent level: 2]
        "mfd_top": {
            "displayname": "Topographic Map",
            "condition": "this animationPhase 'display2_switch' == 0 and player in this and isengineon this",
            "statement": "this animate ['display2_switch',1,true]; [this,0] spawn RHS_fnc_PAKFA_MapData;",
            "position": "pilotcontrol",
            "radius": 10,
            "onlyforplayer": 1,
            "showwindow": 0,
            "hideonuse": 1
        },
        # Class: CfgVehicles|RHS_T50_base|UserActions|MFD_glonass [Indent level: 2],
        "mfd_glonass": {
            "displayname": "GLONASS",
            "condition": "this animationPhase 'display2_switch' == 1 and player in this and isengineon this",
            "statement": "this animate ['display2_switch',2,true]; [this,1] spawn RHS_fnc_PAKFA_MapData;",
            "position": "pilotcontrol",
            "radius": 10,
            "onlyforplayer": 1,
            "showwindow": 0,
            "hideonuse": 1
        },
        # Class: CfgVehicles|RHS_T50_base|UserActions|MFD_off [Indent level: 2],
        "mfd_off": {
            "displayname": "Map Off",
            "condition": "this animationPhase 'display2_switch' == 2 and player in this and isengineon this",
            "statement": " this animate ['display2_switch',0];[this,2] spawn RHS_fnc_PAKFA_MapData;",
            "position": "pilotcontrol",
            "radius": 10,
            "onlyforplayer": 1,
            "showwindow": 0,
            "hideonuse": 1
        },
        # Class: CfgVehicles|RHS_T50_base|UserActions|SAFEMODE [Indent level: 2],
        "safemode": {
            "displayname": "<t color='#00FF7F'>MASTERSAFE</t>",
            "condition": "(call rhs_fnc_findPlayer) in this",
            "statement": "(call rhs_fnc_findPlayer) action ['SwitchWeapon', this, (call rhs_fnc_findPlayer), (weapons this) find 'rhs_weap_MASTERSAFE'];",
            "position": "",
            "radius": 10,
            "priority": 10.5,
            "onlyforplayer": 1,
            "showwindow": 0,
            "shortcut": "user13",
            "hideonuse": 1
        }
    },
    "weapons": ["rhs_weap_MASTERSAFE_Holdster15","rhs_weap_CMFlareLauncher","rhs_weap_GSh301"],
    "magazines": ["rhs_mag_gsh30_bt_250","120Rnd_CMFlare_Chaff_Magazine"],
    "weaponsgroup1": 128,
    "weaponsgroup4": 64,
    "hiddenselectionstextures": ["|rhsafrf|addons|rhs_air|t50|data|pakfa_generic_co.paa","|rhsafrf|addons|rhs_decals|Data|Labels|Aviation|no_ca.paa","|rhsafrf|addons|rhs_decals|Data|Labels|Aviation|no_ca.paa","|rhsafrf|addons|rhs_decals|Data|Labels|Aviation|no_ca.paa","|rhsafrf|addons|rhs_decals|Data|Labels|Aviation|no_ca.paa","|rhsafrf|addons|rhs_decals|Data|Labels|Aviation|no_ca.paa","|rhsafrf|addons|rhs_decals|Data|Labels|Aviation|no_ca.paa","|rhsafrf|addons|rhs_decals|Data|Labels|Aviation|no_ca.paa","|rhsafrf|addons|rhs_decals|Data|Labels|Aviation|star_new2_ca.paa","rhsafrf|addons|rhs_c_air|scripts|data|altis_co.paa","rhsafrf|addons|rhs_c_air|scripts|data|WP_move_ca.paa"],
    "hiddenselections": ["camo1","n1","n2","n3","n4","n5","n6","i1","i2","Glonass_map","display2_wp2"],
    # Class: CfgVehicles|RHS_T50_base|textureSources [Indent level: 1],
    "texturesources": {
        # Class: CfgVehicles|RHS_T50_base|textureSources|standard [Indent level: 2]
        "standard": {
            "displayname": "Blue Camouflage",
            "author": "Red Hammer Studios",
            "textures": ["|rhsafrf|addons|rhs_air|t50|data|pakfa_bluecamo_co.paa","|rhsafrf|addons|rhs_decals|Data|Labels|Aviation|no_ca.paa","|rhsafrf|addons|rhs_decals|Data|Numbers|AviaBlue|5_ca.paa","|rhsafrf|addons|rhs_decals|Data|Numbers|AviaBlue|1_ca.paa","|rhsafrf|addons|rhs_decals|Data|Labels|Aviation|no_ca.paa","|rhsafrf|addons|rhs_decals|Data|Labels|Aviation|no_ca.paa","|rhsafrf|addons|rhs_decals|Data|Labels|Aviation|no_ca.paa","|rhsafrf|addons|rhs_decals|Data|Labels|AviationCompanies|sukhoi_ca.paa","|rhsafrf|addons|rhs_decals|Data|Labels|Aviation|star_new2_ca.paa","rhsafrf|addons|rhs_c_air|scripts|data|altis_co.paa","rhsafrf|addons|rhs_c_air|scripts|data|WP_move_ca.paa"],
            "factions": ["rhs_faction_vvs_c","rhs_faction_vvs"]
        },
        # Class: CfgVehicles|RHS_T50_base|textureSources|standard2 [Indent level: 2],
        "standard2": {
            "displayname": "Blue on Blue",
            "author": "Red Hammer Studios",
            "textures": ["|rhsafrf|addons|rhs_air|t50|data|pakfa_blueonblue_co.paa","|rhsafrf|addons|rhs_decals|Data|Labels|Aviation|no_ca.paa","|rhsafrf|addons|rhs_decals|Data|Labels|Aviation|no_ca.paa","|rhsafrf|addons|rhs_decals|Data|Labels|Aviation|no_ca.paa","|rhsafrf|addons|rhs_decals|Data|Labels|Aviation|no_ca.paa","|rhsafrf|addons|rhs_decals|Data|Labels|Aviation|no_ca.paa","|rhsafrf|addons|rhs_decals|Data|Labels|Aviation|no_ca.paa","|rhsafrf|addons|rhs_decals|Data|Labels|Aviation|no_ca.paa","|rhsafrf|addons|rhs_decals|Data|Labels|Aviation|star_new2_ca.paa","rhsafrf|addons|rhs_c_air|scripts|data|altis_co.paa","rhsafrf|addons|rhs_c_air|scripts|data|WP_move_ca.paa"],
            "factions": ["rhs_faction_vvs_c","rhs_faction_vvs"]
        },
        # Class: CfgVehicles|RHS_T50_base|textureSources|standard3 [Indent level: 2],
        "standard3": {
            "displayname": "Grey Camouflage",
            "author": "Red Hammer Studios",
            "textures": ["|rhsafrf|addons|rhs_air|t50|data|pakfa_greycamo_co.paa","|rhsafrf|addons|rhs_decals|Data|Labels|Aviation|no_ca.paa","|rhsafrf|addons|rhs_decals|Data|Numbers|AviaBlue|5_ca.paa","|rhsafrf|addons|rhs_decals|Data|Numbers|AviaBlue|1_ca.paa","|rhsafrf|addons|rhs_decals|Data|Labels|Aviation|no_ca.paa","|rhsafrf|addons|rhs_decals|Data|Labels|Aviation|no_ca.paa","|rhsafrf|addons|rhs_decals|Data|Labels|Aviation|no_ca.paa","|rhsafrf|addons|rhs_decals|Data|Labels|AviationCompanies|sukhoi_ca.paa","|rhsafrf|addons|rhs_decals|Data|Labels|Aviation|star_new2_ca.paa","rhsafrf|addons|rhs_c_air|scripts|data|altis_co.paa","rhsafrf|addons|rhs_c_air|scripts|data|WP_move_ca.paa"],
            "factions": ["rhs_faction_vvs_c","rhs_faction_vvs"]
        },
        # Class: CfgVehicles|RHS_T50_base|textureSources|standard4 [Indent level: 2],
        "standard4": {
            "displayname": "Blue (Generic)",
            "author": "Red Hammer Studios",
            "textures": ["|rhsafrf|addons|rhs_air|t50|data|pakfa_generic_co.paa","|rhsafrf|addons|rhs_decals|Data|Labels|Aviation|no_ca.paa","|rhsafrf|addons|rhs_decals|Data|Labels|Aviation|no_ca.paa","|rhsafrf|addons|rhs_decals|Data|Labels|Aviation|no_ca.paa","|rhsafrf|addons|rhs_decals|Data|Labels|Aviation|no_ca.paa","|rhsafrf|addons|rhs_decals|Data|Labels|Aviation|no_ca.paa","|rhsafrf|addons|rhs_decals|Data|Labels|Aviation|no_ca.paa","|rhsafrf|addons|rhs_decals|Data|Labels|Aviation|no_ca.paa","|rhsafrf|addons|rhs_decals|Data|Labels|Aviation|star_new2_ca.paa","rhsafrf|addons|rhs_c_air|scripts|data|altis_co.paa","rhsafrf|addons|rhs_c_air|scripts|data|WP_move_ca.paa"],
            "factions": ["rhs_faction_vvs_c","rhs_faction_vvs"]
        }
    },
    "texturelist": [],
    # Class: CfgVehicles|RHS_T50_base|Attributes [Indent level: 1],
    "attributes": {
        # Class: CfgVehicles|RHS_T50_base|Attributes|ObjectTexture [Indent level: 2]
        "objecttexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayname": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalNumber_type [Indent level: 2],
        "rhs_decalnumber_type": {
            "displayname": "Define font type of side number",
            "tooltip": "Define kind of font that will be drawn on vehicle",
            "property": "rhs_decalNumber_type",
            "control": "Combo",
            "expression": "if(_value != 'NoChange')then{ _this setVariable ['%s', _value];[_this,[['Number', cRHSAIRT50NumberPlaces, _value]]] call rhs_fnc_decalsInit}",
            "defaultvalue": 0,
            "typename": "STRING",
            # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalNumber_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalNumber_type|values|NoChange [Indent level: 4]
                "nochange": {
                    "name": "Default",
                    "value": "NoChange"
                },
                # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalNumber_type|values|AviaBlue [Indent level: 4],
                "aviablue": {
                    "name": "Aviation Blue",
                    "value": "AviaBlue",
                    "defaultvalue": "AviaBlue"
                },
                # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalNumber_type|values|AviaYellow [Indent level: 4],
                "aviayellow": {
                    "name": "Aviation Yellow",
                    "value": "AviaYellow"
                },
                # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalNumber_type|values|AviaRed [Indent level: 4],
                "aviared": {
                    "name": "Aviation Red",
                    "value": "AviaRed"
                },
                # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalNumber_type|values|AviaWhiteOut [Indent level: 4],
                "aviawhiteout": {
                    "name": "Aviation White Out",
                    "value": "AviaWhiteOut"
                },
                # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalNumber_type|values|AviaCDF [Indent level: 4],
                "aviacdf": {
                    "name": "Aviation CDF",
                    "value": "AviaCDF"
                },
                # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalNumber_type|values|Default [Indent level: 4],
                "default": {
                    "name": "Default (White)",
                    "value": "Default"
                },
                # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalNumber_type|values|DefaultRed [Indent level: 4],
                "defaultred": {
                    "name": "Default (Red)",
                    "value": "DefaultRed"
                },
                # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalNumber_type|values|BoldRed [Indent level: 4],
                "boldred": {
                    "name": "Bold Red",
                    "value": "BoldRed"
                },
                # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalNumber_type|values|CDF [Indent level: 4],
                "cdf": {
                    "name": "CDF",
                    "value": "CDF"
                },
                # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalNumber_type|values|Handpaint [Indent level: 4],
                "handpaint": {
                    "name": "Handpaint",
                    "value": "Handpaint"
                },
                # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalNumber_type|values|HandpaintBlack [Indent level: 4],
                "handpaintblack": {
                    "name": "Handpaint Black",
                    "value": "HandpaintBlack"
                },
                # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalNumber_type|values|Iraqi [Indent level: 4],
                "iraqi": {
                    "name": "Iraqi",
                    "value": "Iraqi"
                }
            }
        },
        # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalNumber [Indent level: 2],
        "rhs_decalnumber": {
            "displayname": "Set side number",
            "tooltip": "Set side number. 2 numbers are required. Hides on 0",
            "property": "rhs_decalNumber",
            "control": "Edit",
            "validate": "Number",
            "defaultvalue": "-1",
            "expression": "if(_value >= 0)then{if(_value == 0)then{{[_this setobjectTexture [_x,'a3|data_f|clear_empty.paa']]}foreach cRHSAIRT50NumberPlaces}else{[_this, [['Number', cRHSAIRT50NumberPlaces, _this getVariable ['rhs_decalNumber_type','AviaBlue'], _value] ] ] call rhs_fnc_decalsInit}};"
        },
        # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalNumber_type2 [Indent level: 2],
        "rhs_decalnumber_type2": {
            "displayname": "Define font type of side number (3 digits)",
            "tooltip": "Define kind of font that will be drawn on vehicle",
            "property": "rhs_decalNumber_type2",
            "expression": "if(_value != 'NoChange')then{ _this setVariable ['%s', _value];[_this,[['Number', cRHSAIRT50NumberPlaces2, _value]]] call rhs_fnc_decalsInit}",
            "control": "Combo",
            "defaultvalue": 0,
            "typename": "STRING",
            # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalNumber_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalNumber_type|values|NoChange [Indent level: 4]
                "nochange": {
                    "name": "Default",
                    "value": "NoChange"
                },
                # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalNumber_type|values|AviaBlue [Indent level: 4],
                "aviablue": {
                    "name": "Aviation Blue",
                    "value": "AviaBlue",
                    "defaultvalue": "AviaBlue"
                },
                # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalNumber_type|values|AviaYellow [Indent level: 4],
                "aviayellow": {
                    "name": "Aviation Yellow",
                    "value": "AviaYellow"
                },
                # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalNumber_type|values|AviaRed [Indent level: 4],
                "aviared": {
                    "name": "Aviation Red",
                    "value": "AviaRed"
                },
                # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalNumber_type|values|AviaWhiteOut [Indent level: 4],
                "aviawhiteout": {
                    "name": "Aviation White Out",
                    "value": "AviaWhiteOut"
                },
                # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalNumber_type|values|AviaCDF [Indent level: 4],
                "aviacdf": {
                    "name": "Aviation CDF",
                    "value": "AviaCDF"
                },
                # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalNumber_type|values|Default [Indent level: 4],
                "default": {
                    "name": "Default (White)",
                    "value": "Default"
                },
                # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalNumber_type|values|DefaultRed [Indent level: 4],
                "defaultred": {
                    "name": "Default (Red)",
                    "value": "DefaultRed"
                },
                # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalNumber_type|values|BoldRed [Indent level: 4],
                "boldred": {
                    "name": "Bold Red",
                    "value": "BoldRed"
                },
                # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalNumber_type|values|CDF [Indent level: 4],
                "cdf": {
                    "name": "CDF",
                    "value": "CDF"
                },
                # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalNumber_type|values|Handpaint [Indent level: 4],
                "handpaint": {
                    "name": "Handpaint",
                    "value": "Handpaint"
                },
                # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalNumber_type|values|HandpaintBlack [Indent level: 4],
                "handpaintblack": {
                    "name": "Handpaint Black",
                    "value": "HandpaintBlack"
                },
                # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalNumber_type|values|Iraqi [Indent level: 4],
                "iraqi": {
                    "name": "Iraqi",
                    "value": "Iraqi"
                }
            }
        },
        # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalNumber2 [Indent level: 2],
        "rhs_decalnumber2": {
            "displayname": "Set side number (3 digits)",
            "tooltip": "Set side number. 3 numbers are required. Hides on 0",
            "property": "rhs_decalNumber2",
            "expression": "if(_value >= 0)then{if( _value == 0)then{{[_this setobjectTexture [_x,'a3|data_f|clear_empty.paa']]}foreach cRHSAIRT50NumberPlaces2}else{[_this, [['Number', cRHSAIRT50NumberPlaces2, _this getVariable ['rhs_decalNumber_type2','AviaBlue'], _value] ] ] call rhs_fnc_decalsInit}};",
            "control": "Edit",
            "validate": "Number",
            "defaultvalue": "-1"
        },
        # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalSquadArt [Indent level: 2],
        "rhs_decalsquadart": {
            "displayname": "Define Squadron Art",
            "tooltip": "Define Squadron Art texture located on tail wings. Appears on both sides",
            "property": "rhs_decalNoseArt",
            "control": "Combo",
            "expression": "if(_value >= 0)then{ [_this, [ [ 'Label', cRHSAIRT50SquadPlaces, 'AviationsSquadrons',_value] ] ] call rhs_fnc_decalsInit};",
            "defaultvalue": "-1",
            "typename": "Number",
            # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalSquadArt|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalSquadArt|values|Random [Indent level: 4]
                "random": {
                    "name": "Random",
                    "value": -1,
                    "defaultvalue": -1
                },
                # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalSquadArt|values|Empty [Indent level: 4],
                "empty": {
                    "name": "Empty",
                    "value": 0
                },
                # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalSquadArt|values|Seal1 [Indent level: 4],
                "seal1": {
                    "name": "Seal 1",
                    "value": 1
                },
                # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalSquadArt|values|Polar [Indent level: 4],
                "polar": {
                    "name": "Polar bear",
                    "value": 2
                },
                # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalSquadArt|values|Wolf [Indent level: 4],
                "wolf": {
                    "name": "Wolf",
                    "value": 3
                },
                # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalSquadArt|values|Weird [Indent level: 4],
                "weird": {
                    "name": "Weird Piece of Decal",
                    "value": 4
                },
                # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalSquadArt|values|One [Indent level: 4],
                "one": {
                    "name": "One",
                    "value": 5
                },
                # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalSquadArt|values|Snake [Indent level: 4],
                "snake": {
                    "name": "Snake",
                    "value": 6
                },
                # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalSquadArt|values|Eagle [Indent level: 4],
                "eagle": {
                    "name": "Eagle",
                    "value": 7
                },
                # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalSquadArt|values|seal2 [Indent level: 4],
                "seal2": {
                    "name": "Seal 2",
                    "value": 8
                },
                # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalSquadArt|values|russia [Indent level: 4],
                "russia": {
                    "name": "Russia Decal",
                    "value": 9
                },
                # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalSquadArt|values|navy [Indent level: 4],
                "navy": {
                    "name": "Russian Navy",
                    "value": 10
                }
            }
        },
        # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalStarArt [Indent level: 2],
        "rhs_decalstarart": {
            "displayname": "Define Stars Art",
            "tooltip": "Define Stars Art texture located on wings",
            "property": "rhs_decalStarArt",
            "expression": "if(_value >= 0)then{ [_this, [ [ 'Label', cRHSAIRT50StarPlaces, 'Aviation',_value] ] ] call rhs_fnc_decalsInit};",
            # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalStarArt|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalStarArt|values|Random [Indent level: 4]
                "random": {
                    "name": "Random",
                    "value": -1,
                    "defaultvalue": -1
                },
                # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalStarArt|values|Empty [Indent level: 4],
                "empty": {
                    "name": "Empty",
                    "value": 0
                },
                # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalStarArt|values|New [Indent level: 4],
                "new": {
                    "name": "New type star",
                    "value": 1
                },
                # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_decalStarArt|values|Old [Indent level: 4],
                "old": {
                    "name": "Old type star",
                    "value": 2
                }
            },
            "control": "Combo",
            "defaultvalue": "-1",
            "typename": "Number"
        },
        # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_hideantenna [Indent level: 2],
        "rhs_hideantenna": {
            "displayname": "Remove antenna",
            "property": "rhs_hideantenna",
            "control": "CheckboxNumber",
            "expression": "_this animate ['antenna_hide',_value,true]",
            "defaultvalue": "0"
        },
        # Class: CfgVehicles|RHS_T50_base|Attributes|rhs_hidesensors [Indent level: 2],
        "rhs_hidesensors": {
            "displayname": "Remove sensors",
            "property": "rhs_hidesensors",
            "expression": "_this animate ['sensors_hide',_value,true]",
            "control": "CheckboxNumber",
            "defaultvalue": "0"
        }
    },
    "landingaoa": "rad 10",
    "landingspeed": 240,
    "acceleration": 1775,
    "maxspeed": 1800,
    "stallspeed": 240,
    "stallwarningtreshold": 0.5,
    "rhs_afterburner_maxspeed": 2100,
    "takeoffspeed": 180,
    "altfullforce": 9000,
    "altnoforce": 20000,
    "aileronsensitivity": 1.2,
    "elevatorsensitivity": 2.3,
    "rudderinfluence": 0.02,
    "aileroncontrolssensitivitycoef": 4,
    "elevatorcontrolssensitivity": 5,
    "elevatorcontrolssensitivitycoef": 3.4,
    "ruddercontrolssensitivitycoef": 4,
    "elevatorcoef": [0.8,1.1,0.7,0.6,0.55,0.5,0.5],
    "aileroncoef": [0.7,1,1,1,0.95,0.9,0.85],
    "ruddercoef": [0.7,1,1,1,0.9,0.8,0.7],
    "flapsfrictioncoef": 0.5,
    "angleofindicence": 0.04,
    "draconicforcexcoef": 5.4,
    "draconicforceycoef": 3,
    "draconicforcezcoef": 0.1,
    "draconictorquexcoef": 1.2,
    "draconictorqueycoef": 3,
    "envelope": [0,0.15,1.1,3,5,5.83,6,5.85,5.5,4.8,3.6,1.8,0],
    "thrustcoef": [2.5,2.2,2.1,2,2,2,2,1.9,1.7,1.5,1.3,1.1,1,1,1,1],
    "airbrake": 1,
    "gearuptime": 4.5,
    "geardowntime": 3,
    "wheelsteeringsensitivity": 1.5,
    "memorypointcm": ["flare_launcher1","flare_launcher2","flare_launcher3"],
    "memorypointcmdir": ["flare_launcher1_dir","flare_launcher2_dir","flare_launcher3_dir"],
    "unitinfotype": "RHS_RscUnitInfoAir_PAKFA",
    "drivercansee": "1+2+4+8+16",
    "defaultusermfdvalues": [0.15,1,0.15,0.4],
    # Class: CfgVehicles|RHS_T50_base|MFD [Indent level: 1],
    "mfd": {
        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD [Indent level: 2]
        "airplanehud": {
            "topleft": "HUD_top_left",
            "topright": "HUD_top_right",
            "bottomleft": "HUD_bottom_left",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0,1,0,0.1],
            "enableparallax": 1,
            "font": "rhs_digital_font_rus",
            # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones [Indent level: 3],
            "bones": {
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones|PlaneOrientation [Indent level: 4]
                "planeorientation": {
                    "type": "fixed",
                    "pos": [0.5,0.53]
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones|ClimbFixed [Indent level: 4],
                "climbfixed": {
                    "type": "fixed",
                    "pos": ["0.898+0.09",0.53]
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones|ClimbRotate [Indent level: 4],
                "climbrotate": {
                    "type": "rotational",
                    "source": "vspeed",
                    "sourcescale": 1,
                    "center": ["0.91+0.09",0.53],
                    "min": -30,
                    "max": 30,
                    "minangle": -80,
                    "maxangle": 80,
                    "aspectratio": 1.25806
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones|WeaponAim [Indent level: 4],
                "weaponaim": {
                    "type": "fixed",
                    "source": "weapon",
                    "pos": [0.5,0.53]
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones|Velocity [Indent level: 4],
                "velocity": {
                    "type": "vector",
                    "source": "velocity",
                    "pos0": [0.5,0.53],
                    "pos10": [1.12,1.31]
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones|HorizonBankSource [Indent level: 4],
                "horizonbanksource": {
                    "type": "rotational",
                    "source": "HorizonBank",
                    "center": [0.5,0.53],
                    "min": -6.2831,
                    "max": 6.2831,
                    "minangle": -360,
                    "maxangle": 360
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones|HorizonBankInverted [Indent level: 4],
                "horizonbankinverted": {
                    "type": "rotational",
                    "source": "HorizonBank",
                    "center": [0.5,0.53],
                    "min": -6.2831,
                    "max": 6.2831,
                    "minangle": 360,
                    "maxangle": -360
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones|HorizonBankRotFull [Indent level: 4],
                "horizonbankrotfull": {
                    "type": "rotational",
                    "source": "horizonBank",
                    "center": [0,0],
                    "min": -3.1416,
                    "max": 3.1416,
                    "minangle": -180,
                    "maxangle": 180,
                    "aspectratio": 1
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones|Level0 [Indent level: 4],
                "level0": {
                    "source": "horizonDive",
                    "type": "linear",
                    "angle": 0,
                    "min": -3.4,
                    "max": 3.4,
                    "minpos": [0.5,4.78],
                    "maxpos": [0.5,-3.72]
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones|TerrainBone [Indent level: 4],
                "terrainbone": {
                    "type": "linear",
                    "source": "altitudeAGL",
                    "sourcescale": 1,
                    "min": 0,
                    "max": 200,
                    "minpos": [0,0.666],
                    "maxpos": [0,0.4]
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones|ImpactPoint [Indent level: 4],
                "impactpoint": {
                    "type": "vector",
                    "source": "ImpactPoint",
                    "pos0": [0.5,0.53],
                    "pos10": [1.12,1.31]
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones|ImpactPointRelative [Indent level: 4],
                "impactpointrelative": {
                    "type": "vector",
                    "source": "impactpointweaponRelative",
                    "pos0": [0.5,0.53],
                    "pos10": [1.12,1.31]
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones|Limit0109 [Indent level: 4],
                "limit0109": {
                    "type": "limit",
                    "limits": [0.1,0.1,0.9,0.9]
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones|Target [Indent level: 4],
                "target": {
                    "source": "target",
                    "type": "vector",
                    "pos0": [0.5,0.53],
                    "pos10": [1.12,1.31]
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones|WPPoint [Indent level: 4],
                "wppoint": {
                    "type": "vector",
                    "source": "WPPoint",
                    "pos0": [0.5,0.53],
                    "pos10": [1.12,1.31]
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot1 [Indent level: 4],
                "missileflighttimerot1": {
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "max": 0.5,
                    "minangle": 0,
                    "maxangle": 18,
                    "aspectratio": 1.25806
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot2 [Indent level: 4],
                "missileflighttimerot2": {
                    "maxangle": 37,
                    "max": 2,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.25806
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot3 [Indent level: 4],
                "missileflighttimerot3": {
                    "maxangle": 55.5,
                    "max": 3,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.25806
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot4 [Indent level: 4],
                "missileflighttimerot4": {
                    "maxangle": 74,
                    "max": 4,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.25806
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot5 [Indent level: 4],
                "missileflighttimerot5": {
                    "maxangle": 92.5,
                    "max": 5,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.25806
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot6 [Indent level: 4],
                "missileflighttimerot6": {
                    "maxangle": 111,
                    "max": 6,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.25806
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot7 [Indent level: 4],
                "missileflighttimerot7": {
                    "maxangle": 129.5,
                    "max": 7,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.25806
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot8 [Indent level: 4],
                "missileflighttimerot8": {
                    "maxangle": 148,
                    "max": 8,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.25806
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot9 [Indent level: 4],
                "missileflighttimerot9": {
                    "maxangle": 166.5,
                    "max": 9,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.25806
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot10 [Indent level: 4],
                "missileflighttimerot10": {
                    "maxangle": 185,
                    "max": 10,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.25806
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot11 [Indent level: 4],
                "missileflighttimerot11": {
                    "maxangle": 203.5,
                    "max": 11,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.25806
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot12 [Indent level: 4],
                "missileflighttimerot12": {
                    "maxangle": 222,
                    "max": 12,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.25806
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot13 [Indent level: 4],
                "missileflighttimerot13": {
                    "maxangle": 240.5,
                    "max": 13,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.25806
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot14 [Indent level: 4],
                "missileflighttimerot14": {
                    "maxangle": 259,
                    "max": 14,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.25806
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot15 [Indent level: 4],
                "missileflighttimerot15": {
                    "maxangle": 277.5,
                    "max": 15,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.25806
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot16 [Indent level: 4],
                "missileflighttimerot16": {
                    "maxangle": 296,
                    "max": 16,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.25806
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot17 [Indent level: 4],
                "missileflighttimerot17": {
                    "maxangle": 314.5,
                    "max": 17,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.25806
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot18 [Indent level: 4],
                "missileflighttimerot18": {
                    "maxangle": 333,
                    "max": 18,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.25806
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot19 [Indent level: 4],
                "missileflighttimerot19": {
                    "maxangle": 351.5,
                    "max": 19,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.25806
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot20 [Indent level: 4],
                "missileflighttimerot20": {
                    "maxangle": 370,
                    "max": 20,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.25806
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones|Airport1 [Indent level: 4],
                "airport1": {
                    "type": "vector",
                    "source": "airportCorner1",
                    "pos0": [0.5,0.53],
                    "pos10": [1.12,1.31]
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones|Airport2 [Indent level: 4],
                "airport2": {
                    "source": "airportCorner2",
                    "type": "vector",
                    "pos0": [0.5,0.53],
                    "pos10": [1.12,1.31]
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones|Airport3 [Indent level: 4],
                "airport3": {
                    "source": "airportCorner3",
                    "type": "vector",
                    "pos0": [0.5,0.53],
                    "pos10": [1.12,1.31]
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones|Airport4 [Indent level: 4],
                "airport4": {
                    "source": "airportCorner4",
                    "type": "vector",
                    "pos0": [0.5,0.53],
                    "pos10": [1.12,1.31]
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones|ILS_H [Indent level: 4],
                "ils_h": {
                    "type": "ils",
                    "pos0": [0.5,0.53],
                    "pos3": [0.686,0.53]
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones|ILS_W [Indent level: 4],
                "ils_w": {
                    "pos3": [0.5,0.764],
                    "type": "ils",
                    "pos0": [0.5,0.53]
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones|LarAmmoMax [Indent level: 4],
                "larammomax": {
                    "type": "linear",
                    "source": "LarAmmoMax",
                    "sourcescale": 1,
                    "min": 0,
                    "max": 1,
                    "minpos": [0,1],
                    "maxpos": [0,0]
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones|LarAmmoMin [Indent level: 4],
                "larammomin": {
                    "source": "LarAmmoMin",
                    "type": "linear",
                    "sourcescale": 1,
                    "min": 0,
                    "max": 1,
                    "minpos": [0,1],
                    "maxpos": [0,0]
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones|LarTargetDist [Indent level: 4],
                "lartargetdist": {
                    "source": "LarTargetDist",
                    "type": "linear",
                    "sourcescale": 1,
                    "min": 0,
                    "max": 1,
                    "minpos": [0,1],
                    "maxpos": [0,0]
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones|LarAmmoMGunMax [Indent level: 4],
                "larammomgunmax": {
                    "type": "rotational",
                    "source": "LarAmmoMax",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "max": 1,
                    "minangle": -180,
                    "maxangle": 180,
                    "aspectratio": 1.25806
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Bones|LarAmmoMGunMin [Indent level: 4],
                "larammomgunmin": {
                    "source": "LarAmmoMin",
                    "type": "rotational",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "max": 1,
                    "minangle": -180,
                    "maxangle": 180,
                    "aspectratio": 1.25806
                }
            },
            # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw [Indent level: 3],
            "draw": {
                "alpha": "user3",
                "color": ["user0","user1","user2"],
                "condition": "on",
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont [Indent level: 4],
                "horizont": {
                    "cliptl": [0.1,0.28],
                    "clipbr": [0.9,0.8],
                    # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed [Indent level: 5],
                    "dimmed": {
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level00 [Indent level: 6]
                        "level00": {
                            "type": "line",
                            "width": 2,
                            "points": [["Level0",[0.24,0],1],["Level0",[-0.24,0],1],[]]
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level2MH5 [Indent level: 6],
                        "level2mh5": {
                            "type": "line",
                            "linetype": 0,
                            "points": [["Level0",[0.204,-0.14625],1],["Level0",[0.196,-0.14625],1],[],["Level0",[0.188,-0.14625],1],["Level0",[0.18,-0.14625],1]],
                            "width": 2
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level2MH0 [Indent level: 6],
                        "level2mh0": {
                            "type": "line",
                            "linetype": 0,
                            "points": [["Level0",[0.204,-0.04875],1],["Level0",[0.196,-0.04875],1],[],["Level0",[0.188,-0.04875],1],["Level0",[0.18,-0.04875],1]],
                            "width": 2
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level2PH5 [Indent level: 6],
                        "level2ph5": {
                            "type": "line",
                            "linetype": 0,
                            "points": [["Level0",[0.204,0.14625],1],["Level0",[0.18,0.14625],1]],
                            "width": 2
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level2PH0 [Indent level: 6],
                        "level2ph0": {
                            "type": "line",
                            "linetype": 0,
                            "points": [["Level0",[0.204,0.04875],1],["Level0",[0.18,0.04875],1]],
                            "width": 2
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level2M5 [Indent level: 6],
                        "level2m5": {
                            "type": "line",
                            "points": [["Level0",[0.22,-0.0975],1],["Level0",[0.212,-0.0975],1],[],["Level0",[0.204,-0.0975],1],["Level0",[0.196,-0.0975],1],[],["Level0",[0.188,-0.0975],1],["Level0",[0.18,-0.0975],1]],
                            "width": 2
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM2_1_5 [Indent level: 6],
                        "valm2_1_5": {
                            "type": "text",
                            "source": "static",
                            "text": 5,
                            "align": "center",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["Level0",[0.26,-0.1135],1],
                            "right": ["Level0",[0.3,-0.1135],1],
                            "down": ["Level0",[0.26,-0.0815],1]
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level2P5 [Indent level: 6],
                        "level2p5": {
                            "type": "line",
                            "points": [["Level0",[0.22,0.0975],1],["Level0",[0.18,0.0975],1]],
                            "width": 2
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP2_1_5 [Indent level: 6],
                        "valp2_1_5": {
                            "type": "text",
                            "source": "static",
                            "text": -5,
                            "align": "center",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["Level0",[0.26,0.0815],1],
                            "right": ["Level0",[0.3,0.0815],1],
                            "down": ["Level0",[0.26,0.1135],1]
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level2MH10 [Indent level: 6],
                        "level2mh10": {
                            "type": "line",
                            "linetype": 0,
                            "points": [["Level0",[0.204,-0.24375],1],["Level0",[0.196,-0.24375],1],[],["Level0",[0.188,-0.24375],1],["Level0",[0.18,-0.24375],1]],
                            "width": 2
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level2PH10 [Indent level: 6],
                        "level2ph10": {
                            "type": "line",
                            "linetype": 0,
                            "points": [["Level0",[0.204,0.24375],1],["Level0",[0.18,0.24375],1]],
                            "width": 2
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level2M10 [Indent level: 6],
                        "level2m10": {
                            "type": "line",
                            "points": [["Level0",[0.22,-0.195],1],["Level0",[0.212,-0.195],1],[],["Level0",[0.204,-0.195],1],["Level0",[0.196,-0.195],1],[],["Level0",[0.188,-0.195],1],["Level0",[0.18,-0.195],1]],
                            "width": 2
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM2_1_10 [Indent level: 6],
                        "valm2_1_10": {
                            "type": "text",
                            "source": "static",
                            "text": 10,
                            "align": "center",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["Level0",[0.26,-0.211],1],
                            "right": ["Level0",[0.3,-0.211],1],
                            "down": ["Level0",[0.26,-0.179],1]
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level2P10 [Indent level: 6],
                        "level2p10": {
                            "type": "line",
                            "points": [["Level0",[0.22,0.195],1],["Level0",[0.18,0.195],1]],
                            "width": 2
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP2_1_10 [Indent level: 6],
                        "valp2_1_10": {
                            "type": "text",
                            "source": "static",
                            "text": -10,
                            "align": "center",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["Level0",[0.26,0.179],1],
                            "right": ["Level0",[0.3,0.179],1],
                            "down": ["Level0",[0.26,0.211],1]
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level2MH15 [Indent level: 6],
                        "level2mh15": {
                            "type": "line",
                            "linetype": 0,
                            "points": [["Level0",[0.204,-0.34125],1],["Level0",[0.196,-0.34125],1],[],["Level0",[0.188,-0.34125],1],["Level0",[0.18,-0.34125],1]],
                            "width": 2
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level2PH15 [Indent level: 6],
                        "level2ph15": {
                            "type": "line",
                            "linetype": 0,
                            "points": [["Level0",[0.204,0.34125],1],["Level0",[0.18,0.34125],1]],
                            "width": 2
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level2M15 [Indent level: 6],
                        "level2m15": {
                            "type": "line",
                            "points": [["Level0",[0.22,-0.2925],1],["Level0",[0.212,-0.2925],1],[],["Level0",[0.204,-0.2925],1],["Level0",[0.196,-0.2925],1],[],["Level0",[0.188,-0.2925],1],["Level0",[0.18,-0.2925],1]],
                            "width": 2
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM2_1_15 [Indent level: 6],
                        "valm2_1_15": {
                            "type": "text",
                            "source": "static",
                            "text": 15,
                            "align": "center",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["Level0",[0.26,-0.3085],1],
                            "right": ["Level0",[0.3,-0.3085],1],
                            "down": ["Level0",[0.26,-0.2765],1]
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level2P15 [Indent level: 6],
                        "level2p15": {
                            "type": "line",
                            "points": [["Level0",[0.22,0.2925],1],["Level0",[0.18,0.2925],1]],
                            "width": 2
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP2_1_15 [Indent level: 6],
                        "valp2_1_15": {
                            "type": "text",
                            "source": "static",
                            "text": -15,
                            "align": "center",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["Level0",[0.26,0.2765],1],
                            "right": ["Level0",[0.3,0.2765],1],
                            "down": ["Level0",[0.26,0.3085],1]
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level2MH20 [Indent level: 6],
                        "level2mh20": {
                            "type": "line",
                            "linetype": 0,
                            "points": [["Level0",[0.204,-0.43875],1],["Level0",[0.196,-0.43875],1],[],["Level0",[0.188,-0.43875],1],["Level0",[0.18,-0.43875],1]],
                            "width": 2
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level2PH20 [Indent level: 6],
                        "level2ph20": {
                            "type": "line",
                            "linetype": 0,
                            "points": [["Level0",[0.204,0.43875],1],["Level0",[0.18,0.43875],1]],
                            "width": 2
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level2M20 [Indent level: 6],
                        "level2m20": {
                            "type": "line",
                            "points": [["Level0",[0.22,-0.39],1],["Level0",[0.212,-0.39],1],[],["Level0",[0.204,-0.39],1],["Level0",[0.196,-0.39],1],[],["Level0",[0.188,-0.39],1],["Level0",[0.18,-0.39],1]],
                            "width": 2
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM2_1_20 [Indent level: 6],
                        "valm2_1_20": {
                            "type": "text",
                            "source": "static",
                            "text": 20,
                            "align": "center",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["Level0",[0.26,-0.406],1],
                            "right": ["Level0",[0.3,-0.406],1],
                            "down": ["Level0",[0.26,-0.374],1]
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level2P20 [Indent level: 6],
                        "level2p20": {
                            "type": "line",
                            "points": [["Level0",[0.22,0.39],1],["Level0",[0.18,0.39],1]],
                            "width": 2
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP2_1_20 [Indent level: 6],
                        "valp2_1_20": {
                            "type": "text",
                            "source": "static",
                            "text": -20,
                            "align": "center",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["Level0",[0.26,0.374],1],
                            "right": ["Level0",[0.3,0.374],1],
                            "down": ["Level0",[0.26,0.406],1]
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level2MH25 [Indent level: 6],
                        "level2mh25": {
                            "type": "line",
                            "linetype": 0,
                            "points": [["Level0",[0.204,-0.53625],1],["Level0",[0.196,-0.53625],1],[],["Level0",[0.188,-0.53625],1],["Level0",[0.18,-0.53625],1]],
                            "width": 2
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level2PH25 [Indent level: 6],
                        "level2ph25": {
                            "type": "line",
                            "linetype": 0,
                            "points": [["Level0",[0.204,0.53625],1],["Level0",[0.18,0.53625],1]],
                            "width": 2
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level2M25 [Indent level: 6],
                        "level2m25": {
                            "type": "line",
                            "points": [["Level0",[0.22,-0.4875],1],["Level0",[0.212,-0.4875],1],[],["Level0",[0.204,-0.4875],1],["Level0",[0.196,-0.4875],1],[],["Level0",[0.188,-0.4875],1],["Level0",[0.18,-0.4875],1]],
                            "width": 2
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM2_1_25 [Indent level: 6],
                        "valm2_1_25": {
                            "type": "text",
                            "source": "static",
                            "text": 25,
                            "align": "center",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["Level0",[0.26,-0.5035],1],
                            "right": ["Level0",[0.3,-0.5035],1],
                            "down": ["Level0",[0.26,-0.4715],1]
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level2P25 [Indent level: 6],
                        "level2p25": {
                            "type": "line",
                            "points": [["Level0",[0.22,0.4875],1],["Level0",[0.18,0.4875],1]],
                            "width": 2
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP2_1_25 [Indent level: 6],
                        "valp2_1_25": {
                            "type": "text",
                            "source": "static",
                            "text": -25,
                            "align": "center",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["Level0",[0.26,0.4715],1],
                            "right": ["Level0",[0.3,0.4715],1],
                            "down": ["Level0",[0.26,0.5035],1]
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level2MH30 [Indent level: 6],
                        "level2mh30": {
                            "type": "line",
                            "linetype": 0,
                            "points": [["Level0",[0.204,-0.63375],1],["Level0",[0.196,-0.63375],1],[],["Level0",[0.188,-0.63375],1],["Level0",[0.18,-0.63375],1]],
                            "width": 2
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level2PH30 [Indent level: 6],
                        "level2ph30": {
                            "type": "line",
                            "linetype": 0,
                            "points": [["Level0",[0.204,0.63375],1],["Level0",[0.18,0.63375],1]],
                            "width": 2
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level2M30 [Indent level: 6],
                        "level2m30": {
                            "type": "line",
                            "points": [["Level0",[0.22,-0.585],1],["Level0",[0.212,-0.585],1],[],["Level0",[0.204,-0.585],1],["Level0",[0.196,-0.585],1],[],["Level0",[0.188,-0.585],1],["Level0",[0.18,-0.585],1]],
                            "width": 2
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM2_1_30 [Indent level: 6],
                        "valm2_1_30": {
                            "type": "text",
                            "source": "static",
                            "text": 30,
                            "align": "center",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["Level0",[0.26,-0.601],1],
                            "right": ["Level0",[0.3,-0.601],1],
                            "down": ["Level0",[0.26,-0.569],1]
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level2P30 [Indent level: 6],
                        "level2p30": {
                            "type": "line",
                            "points": [["Level0",[0.22,0.585],1],["Level0",[0.18,0.585],1]],
                            "width": 2
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP2_1_30 [Indent level: 6],
                        "valp2_1_30": {
                            "type": "text",
                            "source": "static",
                            "text": -30,
                            "align": "center",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["Level0",[0.26,0.569],1],
                            "right": ["Level0",[0.3,0.569],1],
                            "down": ["Level0",[0.26,0.601],1]
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level2MH35 [Indent level: 6],
                        "level2mh35": {
                            "type": "line",
                            "linetype": 0,
                            "points": [["Level0",[0.204,-0.73125],1],["Level0",[0.196,-0.73125],1],[],["Level0",[0.188,-0.73125],1],["Level0",[0.18,-0.73125],1]],
                            "width": 2
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level2PH35 [Indent level: 6],
                        "level2ph35": {
                            "type": "line",
                            "linetype": 0,
                            "points": [["Level0",[0.204,0.73125],1],["Level0",[0.18,0.73125],1]],
                            "width": 2
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level2M35 [Indent level: 6],
                        "level2m35": {
                            "type": "line",
                            "points": [["Level0",[0.22,-0.6825],1],["Level0",[0.212,-0.6825],1],[],["Level0",[0.204,-0.6825],1],["Level0",[0.196,-0.6825],1],[],["Level0",[0.188,-0.6825],1],["Level0",[0.18,-0.6825],1]],
                            "width": 2
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM2_1_35 [Indent level: 6],
                        "valm2_1_35": {
                            "type": "text",
                            "source": "static",
                            "text": 35,
                            "align": "center",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["Level0",[0.26,-0.6985],1],
                            "right": ["Level0",[0.3,-0.6985],1],
                            "down": ["Level0",[0.26,-0.6665],1]
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level2P35 [Indent level: 6],
                        "level2p35": {
                            "type": "line",
                            "points": [["Level0",[0.22,0.6825],1],["Level0",[0.18,0.6825],1]],
                            "width": 2
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP2_1_35 [Indent level: 6],
                        "valp2_1_35": {
                            "type": "text",
                            "source": "static",
                            "text": -35,
                            "align": "center",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["Level0",[0.26,0.6665],1],
                            "right": ["Level0",[0.3,0.6665],1],
                            "down": ["Level0",[0.26,0.6985],1]
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level2MH40 [Indent level: 6],
                        "level2mh40": {
                            "type": "line",
                            "linetype": 0,
                            "points": [["Level0",[0.204,-0.82875],1],["Level0",[0.196,-0.82875],1],[],["Level0",[0.188,-0.82875],1],["Level0",[0.18,-0.82875],1]],
                            "width": 2
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level2PH40 [Indent level: 6],
                        "level2ph40": {
                            "type": "line",
                            "linetype": 0,
                            "points": [["Level0",[0.204,0.82875],1],["Level0",[0.18,0.82875],1]],
                            "width": 2
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level2M40 [Indent level: 6],
                        "level2m40": {
                            "type": "line",
                            "points": [["Level0",[0.22,-0.78],1],["Level0",[0.212,-0.78],1],[],["Level0",[0.204,-0.78],1],["Level0",[0.196,-0.78],1],[],["Level0",[0.188,-0.78],1],["Level0",[0.18,-0.78],1]],
                            "width": 2
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM2_1_40 [Indent level: 6],
                        "valm2_1_40": {
                            "type": "text",
                            "source": "static",
                            "text": 40,
                            "align": "center",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["Level0",[0.26,-0.796],1],
                            "right": ["Level0",[0.3,-0.796],1],
                            "down": ["Level0",[0.26,-0.764],1]
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level2P40 [Indent level: 6],
                        "level2p40": {
                            "type": "line",
                            "points": [["Level0",[0.22,0.78],1],["Level0",[0.18,0.78],1]],
                            "width": 2
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP2_1_40 [Indent level: 6],
                        "valp2_1_40": {
                            "type": "text",
                            "source": "static",
                            "text": -40,
                            "align": "center",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["Level0",[0.26,0.764],1],
                            "right": ["Level0",[0.3,0.764],1],
                            "down": ["Level0",[0.26,0.796],1]
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level2MH45 [Indent level: 6],
                        "level2mh45": {
                            "type": "line",
                            "linetype": 0,
                            "points": [["Level0",[0.204,-0.92625],1],["Level0",[0.196,-0.92625],1],[],["Level0",[0.188,-0.92625],1],["Level0",[0.18,-0.92625],1]],
                            "width": 2
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level2PH45 [Indent level: 6],
                        "level2ph45": {
                            "type": "line",
                            "linetype": 0,
                            "points": [["Level0",[0.204,0.92625],1],["Level0",[0.18,0.92625],1]],
                            "width": 2
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level2M45 [Indent level: 6],
                        "level2m45": {
                            "type": "line",
                            "points": [["Level0",[0.22,-0.8775],1],["Level0",[0.212,-0.8775],1],[],["Level0",[0.204,-0.8775],1],["Level0",[0.196,-0.8775],1],[],["Level0",[0.188,-0.8775],1],["Level0",[0.18,-0.8775],1]],
                            "width": 2
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM2_1_45 [Indent level: 6],
                        "valm2_1_45": {
                            "type": "text",
                            "source": "static",
                            "text": 45,
                            "align": "center",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["Level0",[0.26,-0.8935],1],
                            "right": ["Level0",[0.3,-0.8935],1],
                            "down": ["Level0",[0.26,-0.8615],1]
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level2P45 [Indent level: 6],
                        "level2p45": {
                            "type": "line",
                            "points": [["Level0",[0.22,0.8775],1],["Level0",[0.18,0.8775],1]],
                            "width": 2
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP2_1_45 [Indent level: 6],
                        "valp2_1_45": {
                            "type": "text",
                            "source": "static",
                            "text": -45,
                            "align": "center",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["Level0",[0.26,0.8615],1],
                            "right": ["Level0",[0.3,0.8615],1],
                            "down": ["Level0",[0.26,0.8935],1]
                        }
                    }
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|PlaneOrientationCrosshair [Indent level: 4],
                "planeorientationcrosshair": {
                    "type": "line",
                    "width": 3,
                    "points": [["HorizonBankInverted",[-0.165,0],1],["HorizonBankInverted",[-0.11,0],1],["HorizonBankInverted",[-0.1,-0.02],1],["HorizonBankInverted",[-0.09,0],1],["HorizonBankInverted",[-0.05,0],1],[],["HorizonBankInverted",[0.05,0],1],["HorizonBankInverted",[0.09,0],1],["HorizonBankInverted",[0.1,-0.02],1],["HorizonBankInverted",[0.11,0],1],["HorizonBankInverted",[0.165,0],1],[],["HorizonBankInverted",[-0,0.06],1],["HorizonBankInverted",[-0,0.12],1],[],["PlaneOrientation",[-0.205,0],1],["PlaneOrientation",[-0.175,0],1],[],["PlaneOrientation",[0.175,0],1],["PlaneOrientation",[0.205,0],1],[],["PlaneOrientation",[0,-0.002],1],["PlaneOrientation",[-0.002,0],1],["PlaneOrientation",[0,0.002],1],["PlaneOrientation",[0.002,0],1],["PlaneOrientation",[0,-0.002],1],[]]
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|BankDetailed [Indent level: 4],
                "bankdetailed": {
                    "condition": "1-(bomb+mgun+atmissile+aamissile+rocket+missilelocked + missilelocking+activeSensorsOn)",
                    # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|BankDetailed|Level00 [Indent level: 5],
                    "level00": {
                        "type": "line",
                        "width": 5,
                        "points": [["PlaneOrientation",[-0.129904,0.0943549],1],["PlaneOrientation",[-0.147224,0.106935],1],[],["PlaneOrientation",[-0.075,0.163427],1],["PlaneOrientation",[-0.085,0.185218],1],[],["PlaneOrientation",[1.31134e-008,0.18871],1],["PlaneOrientation",[1.48619e-008,0.213871],1],[],["PlaneOrientation",[0.129904,0.0943548],1],["PlaneOrientation",[0.147224,0.106935],1],[],["PlaneOrientation",[0.075,0.163427],1],["PlaneOrientation",[0.085,0.185218],1],[]]
                    }
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|PlaneMovementCrosshair [Indent level: 4],
                "planemovementcrosshair": {
                    "type": "line",
                    "width": 3,
                    "points": [["Velocity",[0,-0.0251613],1],["Velocity",[0.01,-0.0217897],1],["Velocity",[0.01732,-0.0125806],1],["Velocity",[0.02,0],1],["Velocity",[0.01732,0.0125806],1],["Velocity",[0.01,0.0217897],1],["Velocity",[0,0.0251613],1],["Velocity",[-0.01,0.0217897],1],["Velocity",[-0.01732,0.0125806],1],["Velocity",[-0.02,0],1],["Velocity",[-0.01732,-0.0125806],1],["Velocity",[-0.01,-0.0217897],1],["Velocity",[0,-0.0251613],1],[],["Velocity",[0.04,0],1],["Velocity",[0.02,0],1],[],["Velocity",[-0.04,0],1],["Velocity",[-0.02,0],1],[],["Velocity",[0,-0.0503226],1],["Velocity",[0,-0.0251613],1]]
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|WeaponsGroupMGun [Indent level: 4],
                "weaponsgroupmgun": {
                    "condition": "mgun",
                    # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|WeaponsGroupMGun|WeaponName [Indent level: 5],
                    "weaponname": {
                        "type": "text",
                        "source": "static",
                        "sourcescale": 1,
                        "text": "ГШ",
                        "align": "right",
                        "scale": 1,
                        "pos": [[0.14,0.74],1],
                        "right": [[0.19,0.74],1],
                        "down": [[0.14,0.785],1]
                    }
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|WeaponsGroup [Indent level: 4],
                "weaponsgroup": {
                    "condition": "1-mgun",
                    # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|WeaponsGroup|PylonName1 [Indent level: 5],
                    "pylonname1": {
                        "type": "pylonicon",
                        "pos": [[0.145,0.72],1],
                        "pylon": 1,
                        "name": "rhs_rus_ammoname_right"
                    },
                    # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|WeaponsGroup|PylonName2 [Indent level: 5],
                    "pylonname2": {
                        "pylon": 2,
                        "type": "pylonicon",
                        "pos": [[0.145,0.72],1],
                        "name": "rhs_rus_ammoname_right"
                    },
                    # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|WeaponsGroup|PylonName3 [Indent level: 5],
                    "pylonname3": {
                        "pylon": 3,
                        "type": "pylonicon",
                        "pos": [[0.145,0.72],1],
                        "name": "rhs_rus_ammoname_right"
                    },
                    # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|WeaponsGroup|PylonName4 [Indent level: 5],
                    "pylonname4": {
                        "pylon": 4,
                        "type": "pylonicon",
                        "pos": [[0.145,0.72],1],
                        "name": "rhs_rus_ammoname_right"
                    },
                    # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|WeaponsGroup|PylonName5 [Indent level: 5],
                    "pylonname5": {
                        "pylon": 5,
                        "type": "pylonicon",
                        "pos": [[0.145,0.72],1],
                        "name": "rhs_rus_ammoname_right"
                    },
                    # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|WeaponsGroup|PylonName6 [Indent level: 5],
                    "pylonname6": {
                        "pylon": 6,
                        "type": "pylonicon",
                        "pos": [[0.145,0.72],1],
                        "name": "rhs_rus_ammoname_right"
                    }
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|AmmoCount [Indent level: 4],
                "ammocount": {
                    "type": "text",
                    "source": "ammo",
                    "sourcescale": 1,
                    "align": "right",
                    "scale": 1,
                    "pos": [[0.14,"0.000+0.79"],1],
                    "right": [[0.19,"0.000+0.79"],1],
                    "down": [[0.14,"0.045+0.79"],1]
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|CMText [Indent level: 4],
                "cmtext": {
                    "type": "text",
                    "source": "static",
                    "text": "ЛТЦ",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "left",
                    "pos": [[0.95,0.25],1],
                    "right": [[1,0.25],1],
                    "down": [[0.95,0.3],1]
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|CMCount [Indent level: 4],
                "cmcount": {
                    "type": "text",
                    "source": "cmammo",
                    "sourcescale": 1,
                    "align": "left",
                    "scale": 1,
                    "pos": [[0.95,0.3],1],
                    "right": [[1,0.3],1],
                    "down": [[0.95,0.34],1]
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|GearGroup [Indent level: 4],
                "geargroup": {
                    "type": "group",
                    "condition": "ils",
                    # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|GearGroup|GearText [Indent level: 5],
                    "geartext": {
                        "type": "text",
                        "source": "static",
                        "text": "ШАССИ",
                        "align": "center",
                        "scale": 1,
                        "pos": [[0.495,0.885],1],
                        "right": [[0.545,0.885],1],
                        "down": [[0.495,0.925],1]
                    }
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|ILS [Indent level: 4],
                "ils": {
                    "condition": "ils",
                    # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|ILS|Glideslope [Indent level: 5],
                    "glideslope": {
                        "cliptl": [0,0],
                        "clipbr": [1,1],
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|ILS|Glideslope|ILS [Indent level: 6],
                        "ils": {
                            "type": "line",
                            "points": [["ILS_W",[-0.24,0],1],["ILS_W",[0.24,0],1],[],["ILS_W",[-0.24,-0.0301935],1],["ILS_W",[-0.24,0.0301935],1],[],["ILS_W",[-0.12,-0.0226452],1],["ILS_W",[-0.12,0.0226452],1],[],["ILS_W",[0,-0.0301935],1],["ILS_W",[0,0.0301935],1],[],["ILS_W",[0.12,-0.0226452],1],["ILS_W",[0.12,0.0226452],1],[],["ILS_W",[0.24,-0.0301935],1],["ILS_W",[0.24,0.0301935],1],[],["ILS_H",[0,-0.301935],1],["ILS_H",[0,0.301935],1],[],["ILS_H",[-0.024,-0.301935],1],["ILS_H",[0.024,-0.301935],1],[],["ILS_H",[-0.018,-0.150968],1],["ILS_H",[0.018,-0.150968],1],[],["ILS_H",[-0.024,0],1],["ILS_H",[0.024,0],1],[],["ILS_H",[-0.018,0.150968],1],["ILS_H",[0.018,0.150968],1],[],["ILS_H",[-0.024,0.301935],1],["ILS_H",[0.024,0.301935],1]]
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|ILS|Glideslope|airport [Indent level: 6],
                        "airport": {
                            "type": "line",
                            "points": [["airport1",1],["airport2",1],["airport4",1],["airport3",1],["airport1",1]]
                        }
                    }
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|SpeedNumber [Indent level: 4],
                "speednumber": {
                    "type": "text",
                    "source": "speed",
                    "sourcescale": 3.6,
                    "sourcelength": 3,
                    "align": "left",
                    "scale": 1,
                    "pos": [[0.21,0.11],1],
                    "right": [[0.255,0.11],1],
                    "down": [[0.21,0.155],1]
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|SpeedText [Indent level: 4],
                "speedtext": {
                    "type": "text",
                    "source": "static",
                    "text": "И",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": [[0.24,0.11],1],
                    "right": [[0.285,0.11],1],
                    "down": [[0.24,0.155],1]
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|MachNumber [Indent level: 4],
                "machnumber": {
                    "sourcescale": 0.002939,
                    "sourcelength": 1,
                    "sourceprecision": 2,
                    "pos": [[0.21,0.15],1],
                    "right": [[0.255,0.15],1],
                    "down": [[0.21,0.195],1],
                    "type": "text",
                    "source": "speed",
                    "align": "left",
                    "scale": 1
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|MachText [Indent level: 4],
                "machtext": {
                    "type": "text",
                    "source": "static",
                    "text": "М",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": [[0.24,0.15],1],
                    "right": [[0.285,0.15],1],
                    "down": [[0.24,0.195],1]
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|TerrainNumber [Indent level: 4],
                "terrainnumber": {
                    "type": "text",
                    "source": "altitudeAGL",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "sourceoffset": -2,
                    "align": "right",
                    "scale": 1,
                    "pos": [[0.78,0.15],1],
                    "right": [[0.825,0.15],1],
                    "down": [[0.78,0.195],1]
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|RadarText [Indent level: 4],
                "radartext": {
                    "type": "text",
                    "source": "static",
                    "text": "Р",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": [[0.86,0.15],1],
                    "right": [[0.905,0.15],1],
                    "down": [[0.86,0.195],1]
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|AltitudeNumber [Indent level: 4],
                "altitudenumber": {
                    "type": "text",
                    "source": "altitudeASL",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "align": "right",
                    "scale": 1,
                    "pos": [[0.78,0.11],1],
                    "right": [[0.825,0.11],1],
                    "down": [[0.78,0.155],1]
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|ClimbNumber [Indent level: 4],
                "climbnumber": {
                    "type": "text",
                    "source": "vspeed",
                    "sourcescale": 1,
                    "align": "left",
                    "scale": 1,
                    "pos": [[0.885,0.51],1],
                    "right": [[0.935,0.51],1],
                    "down": [[0.885,0.55],1]
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|ClimbArrow [Indent level: 4],
                "climbarrow": {
                    "type": "line",
                    "width": 4,
                    "points": [["ClimbRotate",[-0.074,-0.006],1],["ClimbRotate",[-0.084,0],1],["ClimbRotate",[-0.074,0.006],1],["ClimbRotate",[-0.074,-0.006],1],[],["ClimbRotate",[-0.084,0],1],["ClimbRotate",[0.006,0],1]]
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|ClimbLine [Indent level: 4],
                "climbline": {
                    "type": "line",
                    "width": 4,
                    "points": [["ClimbFixed",[-0.09,4.94926e-009],1],["ClimbFixed",[-0.075,4.12438e-009],1],[],["ClimbFixed",[-0.070477,-0.0322712],1],["ClimbFixed",[-0.0798739,-0.0365741],1],[],["ClimbFixed",[-0.0574533,-0.0606501],1],["ClimbFixed",[-0.0651138,-0.0687368],1],[],["ClimbFixed",[-0.0375,-0.0817137],1],["ClimbFixed",[-0.0425,-0.0926088],1],[],["ClimbFixed",[-0.0130236,-0.0929214],1],["ClimbFixed",[-0.0147601,-0.105311],1],[],["ClimbFixed",[-0.0704769,0.0322713],1],["ClimbFixed",[-0.0798739,0.0365741],1],[],["ClimbFixed",[-0.0574533,0.0606501],1],["ClimbFixed",[-0.0651138,0.0687368],1],[],["ClimbFixed",[-0.0375,0.0817137],1],["ClimbFixed",[-0.0425,0.0926089],1],[],["ClimbFixed",[-0.0130236,0.0929214],1],["ClimbFixed",[-0.0147601,0.105311],1],[]]
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|HeadingArrow [Indent level: 4],
                "headingarrow": {
                    "type": "line",
                    "width": 3,
                    "points": [[[0.48,0.145],1],[[0.5,0.125],1],[[0.52,0.145],1],[[0.54,0.145],1],[[0.54,0.18],1],[[0.46,0.18],1],[[0.46,0.145],1],[[0.48,0.145],1]]
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|HeadingLine [Indent level: 4],
                "headingline": {
                    "type": "line",
                    "width": 4,
                    "points": [[[0.3,0.12],1],[[0.7,0.12],1]]
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|HeadingNumber [Indent level: 4],
                "headingnumber": {
                    "type": "text",
                    "source": "heading",
                    "sourcescale": 1,
                    "align": "center",
                    "scale": 1,
                    "pos": [[0.5,0.145],1],
                    "right": [[0.55,0.145],1],
                    "down": [[0.5,0.18],1]
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|HeadingScale [Indent level: 4],
                "headingscale": {
                    "type": "scale",
                    "horizontal": 1,
                    "source": "heading",
                    "sourcescale": 0.1,
                    "width": 4,
                    "nevereatseaweed": 1,
                    "top": 0.3,
                    "center": 0.5,
                    "bottom": 0.7,
                    "linexleft": 0.118,
                    "lineyright": 0.108,
                    "linexleftmajor": 0.118,
                    "lineyrightmajor": 0.098,
                    "majorlineeach": 2,
                    "numbereach": 2,
                    "step": 0.5,
                    "stepsize": 0.0344828,
                    "align": "center",
                    "scale": 1,
                    "pos": [0.295,0.05],
                    "right": [0.35,0.05],
                    "down": [0.295,0.09]
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|MGun [Indent level: 4],
                "mgun": {
                    "condition": "-2+(mgun+rocket)*ImpactDistance",
                    # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|MGun|Cross [Indent level: 5],
                    "cross": {
                        "type": "line",
                        "width": 3,
                        "points": [["ImpactPointRelative",[0,-0.07],1],["ImpactPointRelative",[0,-0.03],1],[],["ImpactPointRelative",[0,0.045],1],["ImpactPointRelative",[0,0.03],1],[],["ImpactPointRelative",[-0.045,0],1],["ImpactPointRelative",[-0.03,0],1],[],["ImpactPointRelative",[0.045,0],1],["ImpactPointRelative",[0.03,0],1],[],["ImpactPointRelative",[0,-0.002],1],["ImpactPointRelative",[0,0.002],1],[],["ImpactPointRelative",[-0.002,0],1],["ImpactPointRelative",[0.002,0],1],[]]
                    },
                    # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|MGun|Circle [Indent level: 5],
                    "circle": {
                        "type": "line",
                        "width": 6,
                        "points": [["ImpactPointRelative",[0,-0.0503226],1],["ImpactPointRelative",[0,-0.0629032],1],["MissileFlightTimeRot1",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot2",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot3",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot4",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot5",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot6",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot7",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot8",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot9",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot10",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot11",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot12",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot13",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot14",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot15",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot16",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot17",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot18",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot19",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot20",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot20",[0,0.04],1,"ImpactPointRelative",1]]
                    },
                    # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|MGun|Circle_LAR [Indent level: 5],
                    "circle_lar": {
                        "type": "line",
                        "width": 5,
                        "points": [["ImpactPointRelative",1,["LarAmmoMGunMin",0,-0.0754839],1],["ImpactPointRelative",1,["LarAmmoMGunMin",0,-0.0629032],1],[],["ImpactPointRelative",1,["LarAmmoMGunMax",0,-0.0754839],1],["ImpactPointRelative",1,["LarAmmoMGunMax",0,-0.0629032],1],[]]
                    },
                    # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|MGun|Distance [Indent level: 5],
                    "distance": {
                        "type": "text",
                        "source": "ImpactDistance",
                        "sourcescale": 0.001,
                        "sourceprecision": 1,
                        "max": 15,
                        "align": "center",
                        "scale": 1,
                        "pos": ["ImpactPointRelative",[-0.002,-0.1],1],
                        "right": ["ImpactPointRelative",[0.045,-0.1],1],
                        "down": ["ImpactPointRelative",[-0.002,-0.06],1]
                    }
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|AAMissileCrosshairGroup [Indent level: 4],
                "aamissilecrosshairgroup": {
                    "type": "group",
                    "condition": "AAmissile",
                    # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|AAMissileCrosshairGroup|AAMissileCrosshair [Indent level: 5],
                    "aamissilecrosshair": {
                        "type": "line",
                        "width": 4,
                        "points": [["WeaponAim",[0,-0.314516],1],["WeaponAim",[0.0434,-0.309735],1],["WeaponAim",[0.0855,-0.295551],1],["WeaponAim",[0.125,-0.272371],1],["WeaponAim",[0.1607,-0.240919],1],["WeaponAim",[0.1915,-0.202171],1],["WeaponAim",[0.2165,-0.157258],1],["WeaponAim",[0.234925,-0.107565],1],["WeaponAim",[0.2462,-0.0546],1],["WeaponAim",[0.25,0],1],["WeaponAim",[0.2462,0.0546],1],["WeaponAim",[0.234925,0.107565],1],["WeaponAim",[0.2165,0.157258],1],["WeaponAim",[0.1915,0.202171],1],["WeaponAim",[0.1607,0.240919],1],["WeaponAim",[0.125,0.272371],1],["WeaponAim",[0.0855,0.295551],1],["WeaponAim",[0.0434,0.309735],1],["WeaponAim",[0,0.314516],1],["WeaponAim",[-0.0434,0.309735],1],["WeaponAim",[-0.0855,0.295551],1],["WeaponAim",[-0.125,0.272371],1],["WeaponAim",[-0.1607,0.240919],1],["WeaponAim",[-0.1915,0.202171],1],["WeaponAim",[-0.2165,0.157258],1],["WeaponAim",[-0.234925,0.107565],1],["WeaponAim",[-0.2462,0.0546],1],["WeaponAim",[-0.25,0],1],["WeaponAim",[-0.2462,-0.0546],1],["WeaponAim",[-0.234925,-0.107565],1],["WeaponAim",[-0.2165,-0.157258],1],["WeaponAim",[-0.1915,-0.202171],1],["WeaponAim",[-0.1607,-0.240919],1],["WeaponAim",[-0.125,-0.272371],1],["WeaponAim",[-0.0855,-0.295551],1],["WeaponAim",[-0.0434,-0.309735],1],["WeaponAim",[0,-0.314516],1]]
                    }
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|ATMissileCrosshairGroup [Indent level: 4],
                "atmissilecrosshairgroup": {
                    "condition": "ATmissile",
                    "type": "group",
                    # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|ATMissileCrosshairGroup|ATMissileCrosshair [Indent level: 5],
                    "atmissilecrosshair": {
                        "type": "line",
                        "width": 4,
                        "points": [["WeaponAim",[-0.15,-0.15],1],["WeaponAim",[-0.15,-0.13],1],[],["WeaponAim",[-0.15,0.15],1],["WeaponAim",[-0.15,0.13],1],[],["WeaponAim",[0.15,-0.15],1],["WeaponAim",[0.15,-0.13],1],[],["WeaponAim",[0.15,0.15],1],["WeaponAim",[0.15,0.13],1],[],["WeaponAim",[-0.15,-0.15],1],["WeaponAim",[-0.13,-0.15],1],[],["WeaponAim",[-0.15,0.15],1],["WeaponAim",[-0.13,0.15],1],[],["WeaponAim",[0.15,-0.15],1],["WeaponAim",[0.13,-0.15],1],[],["WeaponAim",[0.15,0.15],1],["WeaponAim",[0.13,0.15],1]]
                    }
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|BombCrosshairGroup [Indent level: 4],
                "bombcrosshairgroup": {
                    "type": "group",
                    "condition": "bomb",
                    # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|BombCrosshairGroup|BombCrosshair [Indent level: 5],
                    "bombcrosshair": {
                        "type": "line",
                        "width": 4,
                        "points": [["ImpactPoint",[0,-0.125806],1],["ImpactPoint",[0.01736,-0.123894],1],["ImpactPoint",[0.0342,-0.11822],1],["ImpactPoint",[0.05,-0.108948],1],["ImpactPoint",[0.06428,-0.0963677],1],["ImpactPoint",[0.0766,-0.0808684],1],["ImpactPoint",[0.0866,-0.0629032],1],["ImpactPoint",[0.09397,-0.0430258],1],["ImpactPoint",[0.09848,-0.02184],1],["ImpactPoint",[0.1,0],1],["ImpactPoint",[0.09848,0.02184],1],["ImpactPoint",[0.09397,0.0430258],1],["ImpactPoint",[0.0866,0.0629032],1],["ImpactPoint",[0.0766,0.0808684],1],["ImpactPoint",[0.06428,0.0963677],1],["ImpactPoint",[0.05,0.108948],1],["ImpactPoint",[0.0342,0.11822],1],["ImpactPoint",[0.01736,0.123894],1],["ImpactPoint",[0,0.125806],1],["ImpactPoint",[-0.01736,0.123894],1],["ImpactPoint",[-0.0342,0.11822],1],["ImpactPoint",[-0.05,0.108948],1],["ImpactPoint",[-0.06428,0.0963677],1],["ImpactPoint",[-0.0766,0.0808684],1],["ImpactPoint",[-0.0866,0.0629032],1],["ImpactPoint",[-0.09397,0.0430258],1],["ImpactPoint",[-0.09848,0.02184],1],["ImpactPoint",[-0.1,0],1],["ImpactPoint",[-0.09848,-0.02184],1],["ImpactPoint",[-0.09397,-0.0430258],1],["ImpactPoint",[-0.0866,-0.0629032],1],["ImpactPoint",[-0.0766,-0.0808684],1],["ImpactPoint",[-0.06428,-0.0963677],1],["ImpactPoint",[-0.05,-0.108948],1],["ImpactPoint",[-0.0342,-0.11822],1],["ImpactPoint",[-0.01736,-0.123894],1],["ImpactPoint",[0,-0.125806],1],[],["ImpactPoint",1,"Limit0109",1,[0,-0.0251613],1],["ImpactPoint",1,"Limit0109",1,[0.014,-0.0176129],1],["ImpactPoint",1,"Limit0109",1,["+ 0.02",0],1],["ImpactPoint",1,"Limit0109",1,[0.014,0.0176129],1],["ImpactPoint",1,"Limit0109",1,[0,0.0251613],1],["ImpactPoint",1,"Limit0109",1,[-0.014,0.0176129],1],["ImpactPoint",1,"Limit0109",1,["- 0.02",0],1],["ImpactPoint",1,"Limit0109",1,[-0.014,-0.0176129],1],["ImpactPoint",1,"Limit0109",1,[0,-0.0251613],1],[],["Velocity",0.001,"ImpactPoint",1,"Limit0109",1,[0,0],1],["Velocity",1,"Limit0109",1,[0,0],1]]
                    },
                    # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|BombCrosshairGroup|Distance [Indent level: 5],
                    "distance": {
                        "type": "text",
                        "source": "ImpactDistance",
                        "sourcescale": 0.001,
                        "sourceprecision": 1,
                        "max": 15,
                        "align": "center",
                        "scale": 1,
                        "pos": ["ImpactPoint",[-0.002,0.11],1],
                        "right": ["ImpactPoint",[0.045,0.11],1],
                        "down": ["ImpactPoint",[-0.002,0.15],1]
                    }
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|WP [Indent level: 4],
                "wp": {
                    "condition": "wpvalid",
                    # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|WP|WPdist [Indent level: 5],
                    "wpdist": {
                        "type": "text",
                        "source": "WPDist",
                        "sourcescale": 0.001,
                        "sourceprecision": 1,
                        "align": "center",
                        "scale": 1,
                        "pos": [[0.5,0.8],1],
                        "right": [[0.55,0.8],1],
                        "down": [[0.5,0.85],1]
                    },
                    # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|WP|WP [Indent level: 5],
                    "wp": {
                        "width": 1,
                        "type": "line",
                        "points": [["Limit0109",1,"wppoint",1,["HorizonBankRotFull",0.015,-0.035],1],["Limit0109",1,"wppoint",1,["HorizonBankRotFull",0,0],1],["Limit0109",1,"wppoint",1,["HorizonBankRotFull",-0.015,-0.035],1]]
                    }
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|CoordXNumber [Indent level: 4],
                "coordxnumber": {
                    "type": "text",
                    "source": "coordinateX",
                    "sourcescale": 0.01,
                    "sourcelength": 3,
                    "sourceoffset": -0.5,
                    "align": "left",
                    "scale": 1,
                    "pos": [[0.874,0.789],1],
                    "right": [[0.924,0.789],1],
                    "down": [[0.874,0.824],1]
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|CoordYNumber [Indent level: 4],
                "coordynumber": {
                    "source": "coordinateY",
                    "pos": [[0.951,0.789],1],
                    "right": [[1.001,0.789],1],
                    "down": [[0.951,0.824],1],
                    "type": "text",
                    "sourcescale": 0.01,
                    "sourcelength": 3,
                    "sourceoffset": -0.5,
                    "align": "left",
                    "scale": 1
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|Time [Indent level: 4],
                "time": {
                    "source": "time",
                    "text": "%X",
                    "align": "left",
                    "pos": [[0.949,0.822],1],
                    "right": [[0.999,0.822],1],
                    "down": [[0.949,0.857],1],
                    "type": "text",
                    "sourcescale": 0.01,
                    "sourcelength": 3,
                    "sourceoffset": -0.5,
                    "scale": 1
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|MissileLocked [Indent level: 4],
                "missilelocked": {
                    "condition": "missilelocked",
                    # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|MissileLocked|LaunchReady [Indent level: 5],
                    "launchready": {
                        "type": "text",
                        "source": "static",
                        "text": "ПР",
                        "align": "center",
                        "scale": 1,
                        "pos": [[0.5,"0.49+0.19"],1],
                        "right": [[0.58,"0.49+0.19"],1],
                        "down": [[0.5,0.75],1]
                    }
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|MissileLocking [Indent level: 4],
                "missilelocking": {
                    "condition": "missilelocking",
                    "blinkingpattern": [0.2,0.5],
                    "blinkingstartson": 1,
                    # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|MissileLocking|LaunchReady [Indent level: 5],
                    "launchready": {
                        "type": "text",
                        "source": "static",
                        "text": "ПР",
                        "align": "center",
                        "scale": 1,
                        "pos": [[0.5,"0.49+0.19"],1],
                        "right": [[0.58,"0.49+0.19"],1],
                        "down": [[0.5,0.75],1]
                    }
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|TargetLocked [Indent level: 4],
                "targetlocked": {
                    "condition": "TargetHeight>=1",
                    # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|TargetLocked|shape [Indent level: 5],
                    "shape": {
                        "type": "line",
                        "width": 4,
                        "points": [["Target",1,"Limit0109",1,[0,-0.015],1],["Target",1,"Limit0109",1,[-0.0075,0],1],["Target",1,"Limit0109",1,[0,0.0125],1],["Target",1,"Limit0109",1,[0.0075,0],1],["Target",1,"Limit0109",1,[0,-0.0125],1],[],[[0.145,0.06],1],[[0.215,0.06],1],[[0.215,0.11],1],[[0.145,0.11],1],[[0.145,0.06],1],[],[[0.777,0.06],1],[[0.847,0.06],1],[[0.847,0.11],1],[[0.777,0.11],1],[[0.777,0.06],1]]
                    },
                    # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|TargetLocked|TargetSquare [Indent level: 5],
                    "targetsquare": {
                        "type": "line",
                        "width": 4,
                        "points": [["Target",1,"Limit0109",1,[0,-0.0629032],1],["Target",1,"Limit0109",1,[0.05,0],1],["Target",1,"Limit0109",1,[0,0.0629032],1],["Target",1,"Limit0109",1,[-0.05,0],1],["Target",1,"Limit0109",1,[0,-0.0629032],1]]
                    },
                    # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|TargetLocked|TargetSpeed [Indent level: 5],
                    "targetspeed": {
                        "source": "LarTargetSpeed",
                        "sourcescale": 0.36,
                        "pos": [[0.21,0.065],1],
                        "right": [[0.255,0.065],1],
                        "down": [[0.21,0.11],1],
                        "type": "text",
                        "sourcelength": 3,
                        "align": "left",
                        "scale": 1
                    },
                    # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|TargetLocked|TargetHeight [Indent level: 5],
                    "targetheight": {
                        "source": "TargetHeight",
                        "sourcescale": 0.1,
                        "sourcelength": 3,
                        "pos": [[0.78,0.065],1],
                        "right": [[0.825,0.065],1],
                        "down": [[0.78,0.11],1],
                        "type": "text",
                        "align": "right",
                        "scale": 1
                    }
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|RadarOnGroup [Indent level: 4],
                "radarongroup": {
                    "condition": "activeSensorsOn",
                    # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|RadarOnGroup|RadarText [Indent level: 5],
                    "radartext": {
                        "type": "text",
                        "source": "static",
                        "text": "РЛ",
                        "align": "left",
                        "scale": 1,
                        "pos": [[0.1,0.45],1],
                        "right": [[0.15,0.45],1],
                        "down": [[0.1,0.5],1]
                    }
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|LAR [Indent level: 4],
                "lar": {
                    "type": "group",
                    "condition": "bomb+mgun+atmissile+aamissile+rocket",
                    # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|LAR|Lines [Indent level: 5],
                    "lines": {
                        "type": "line",
                        "width": 3,
                        "points": [[[0.18,0.245],1],[[0.2,0.245],1],[[0.2,0.695],1],[[0.18,0.695],1],[],[[0.18,0.605],1],[[0.2,0.605],1],[],[[0.18,0.515],1],[[0.2,0.515],1],[],[[0.18,0.425],1],[[0.2,0.425],1],[],[[0.18,0.335],1],[[0.2,0.335],1],[],["LarTargetDist",-0.45,[0.212,0.707],1],["LarTargetDist",-0.45,[0.2,0.695],1],["LarTargetDist",-0.45,[0.212,0.683],1],["LarTargetDist",-0.45,[0.212,0.692],1],["LarTargetDist",-0.45,[0.222,0.692],1],["LarTargetDist",-0.45,[0.222,0.698],1],["LarTargetDist",-0.45,[0.212,0.698],1],["LarTargetDist",-0.45,[0.212,0.707],1]]
                    },
                    # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|LAR|Poly [Indent level: 5],
                    "poly": {
                        "type": "polygon",
                        "points": [[["LarAmmoMin",-0.45,[0.201,0.695],1],["LarAmmoMin",-0.45,[0.201,0.7],1],["LarAmmoMin",-0.45,[0.212,0.7],1],["LarAmmoMin",-0.45,[0.212,0.695],1]],[["LarAmmoMin",-0.45,[0.201,0.62],1],["LarAmmoMin",-0.45,[0.201,0.63],1],["LarAmmoMin",-0.45,[0.212,0.63],1],["LarAmmoMin",-0.45,[0.212,0.62],1]],[["LarAmmoMax",-0.45,[0.201,0.795],1],["LarAmmoMax",-0.45,[0.201,0.8],1],["LarAmmoMax",-0.45,[0.212,0.8],1],["LarAmmoMax",-0.45,[0.212,0.795],1]]]
                    },
                    # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|LAR|LARText1 [Indent level: 5],
                    "lartext1": {
                        "type": "text",
                        "source": "LarTop",
                        "sourcescale": 0.001,
                        "scale": 1,
                        "pos": [[0.175,0.231],1],
                        "right": [[0.21,0.231],1],
                        "down": [[0.175,0.259],1],
                        "align": "left"
                    },
                    # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|LAR|LARText2 [Indent level: 5],
                    "lartext2": {
                        "source": "LarTop",
                        "sourceprecision": -1,
                        "sourcescale": 0.0008,
                        "pos": [[0.175,0.321],1],
                        "right": [[0.21,0.321],1],
                        "down": [[0.175,0.349],1],
                        "type": "text",
                        "scale": 1,
                        "align": "left"
                    },
                    # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|LAR|LARText3 [Indent level: 5],
                    "lartext3": {
                        "source": "LarTop",
                        "sourceprecision": -1,
                        "sourcescale": 0.0006,
                        "pos": [[0.175,0.411],1],
                        "right": [[0.21,0.411],1],
                        "down": [[0.175,0.439],1],
                        "type": "text",
                        "scale": 1,
                        "align": "left"
                    },
                    # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|LAR|LARText4 [Indent level: 5],
                    "lartext4": {
                        "source": "LarTop",
                        "sourceprecision": -1,
                        "sourcescale": 0.0004,
                        "pos": [[0.175,0.501],1],
                        "right": [[0.21,0.501],1],
                        "down": [[0.175,0.529],1],
                        "type": "text",
                        "scale": 1,
                        "align": "left"
                    },
                    # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|LAR|LARText5 [Indent level: 5],
                    "lartext5": {
                        "source": "LarTop",
                        "sourceprecision": -1,
                        "sourcescale": 0.0002,
                        "pos": [[0.175,0.591],1],
                        "right": [[0.21,0.591],1],
                        "down": [[0.175,0.619],1],
                        "type": "text",
                        "scale": 1,
                        "align": "left"
                    },
                    # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|LAR|LARText6 [Indent level: 5],
                    "lartext6": {
                        "source": "static",
                        "text": 0,
                        "sourceprecision": -1,
                        "sourcescale": 0.0002,
                        "pos": [[0.175,0.681],1],
                        "right": [[0.21,0.681],1],
                        "down": [[0.175,0.709],1],
                        "type": "text",
                        "scale": 1,
                        "align": "left"
                    }
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|AirplaneHUD|Draw|RadarBoxes [Indent level: 4],
                "radarboxes": {
                    "type": "radar",
                    "pos0": [0.5,0.53],
                    "pos10": [1.12,1.31],
                    "width": 4,
                    "points": [[[0,-0.0503226],1],[[0.006944,-0.0495577],1],[[0.01368,-0.0472881],1],[[0.02,-0.0435794],1],[[0.025712,-0.0385471],1],[[0.03064,-0.0323474],1],[[0.03464,-0.0251613],1],[[0.037588,-0.0172103],1],[[0.039392,-0.008736],1],[[0.04,0],1],[[0.039392,0.008736],1],[[0.037588,0.0172103],1],[[0.03464,0.0251613],1],[[0.03064,0.0323474],1],[[0.025712,0.0385471],1],[[0.02,0.0435794],1],[[0.01368,0.0472881],1],[[0.006944,0.0495577],1],[[0,0.0503226],1],[[-0.006944,0.0495577],1],[[-0.01368,0.0472881],1],[[-0.02,0.0435794],1],[[-0.025712,0.0385471],1],[[-0.03064,0.0323474],1],[[-0.03464,0.0251613],1],[[-0.037588,0.0172103],1],[[-0.039392,0.008736],1],[[-0.04,0],1],[[-0.039392,-0.008736],1],[[-0.037588,-0.0172103],1],[[-0.03464,-0.0251613],1],[[-0.03064,-0.0323474],1],[[-0.025712,-0.0385471],1],[[-0.02,-0.0435794],1],[[-0.01368,-0.0472881],1],[[-0.006944,-0.0495577],1],[[0,-0.0503226],1],[]]
                }
            }
        },
        # Class: CfgVehicles|RHS_T50_base|MFD|HMD [Indent level: 2],
        "hmd": {
            "topleft": "HUD_top_left",
            "topright": "HUD_top_right",
            "bottomleft": "HUD_bottom_left",
            "helmetmounteddisplay": 1,
            "helmetposition": [-0.0325,0.0325,0.1],
            "helmetright": [0.065,0,0],
            "helmetdown": [0,-0.065,0],
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0,1,0,0.1],
            "font": "rhs_digital_font_rus",
            # Class: CfgVehicles|RHS_T50_base|MFD|HMD|Bones [Indent level: 3],
            "bones": {
                # Class: CfgVehicles|RHS_T50_base|MFD|HMD|Bones|PlaneW [Indent level: 4]
                "planew": {
                    "type": "fixed",
                    "pos": [0.5,0.5],
                    "pos10": [0.774,0.77]
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|HMD|Bones|Target [Indent level: 4],
                "target": {
                    "source": "targettoview",
                    "type": "vector",
                    "pos0": [0.5,0.5],
                    "pos10": [0.774,0.77]
                }
            },
            # Class: CfgVehicles|RHS_T50_base|MFD|HMD|Draw [Indent level: 3],
            "draw": {
                "color": [0.15,1,0.15],
                "alpha": 1,
                "condition": "on",
                # Class: CfgVehicles|RHS_T50_base|MFD|HMD|Draw|HeadOutside [Indent level: 4],
                "headoutside": {
                    "condition": "(abs(cameraHeadingDiffY)>7)+(abs(cameraHeadingDiffX)>12)",
                    # Class: CfgVehicles|RHS_T50_base|MFD|HMD|Draw|HeadOutside|SearchMode [Indent level: 5],
                    "searchmode": {
                        "condition": "1-missileLocked - missileLocking",
                        # Class: CfgVehicles|RHS_T50_base|MFD|HMD|Draw|HeadOutside|SearchMode|CircleLock [Indent level: 6],
                        "circlelock": {
                            "type": "line",
                            "width": 12,
                            "points": [["PlaneW",[0,-0.0591241],1],["PlaneW",[0.010416,-0.0582254],1],["PlaneW",[0.02052,-0.0555589],1],["PlaneW",[0.03,-0.0512015],1],["PlaneW",[0.038568,-0.0452891],1],["PlaneW",[0.04596,-0.038005],1],["PlaneW",[0.05196,-0.029562],1],["PlaneW",[0.056382,-0.0202204],1],["PlaneW",[0.059088,-0.0102639],1],["PlaneW",[0.06,0],1],["PlaneW",[0.059088,0.0102639],1],["PlaneW",[0.056382,0.0202204],1],["PlaneW",[0.05196,0.029562],1],["PlaneW",[0.04596,0.038005],1],["PlaneW",[0.038568,0.0452891],1],["PlaneW",[0.03,0.0512015],1],["PlaneW",[0.02052,0.0555589],1],["PlaneW",[0.010416,0.0582254],1],["PlaneW",[0,0.0591241],1],["PlaneW",[-0.010416,0.0582254],1],["PlaneW",[-0.02052,0.0555589],1],["PlaneW",[-0.03,0.0512015],1],["PlaneW",[-0.038568,0.0452891],1],["PlaneW",[-0.04596,0.038005],1],["PlaneW",[-0.05196,0.029562],1],["PlaneW",[-0.056382,0.0202204],1],["PlaneW",[-0.059088,0.0102639],1],["PlaneW",[-0.06,0],1],["PlaneW",[-0.059088,-0.0102639],1],["PlaneW",[-0.056382,-0.0202204],1],["PlaneW",[-0.05196,-0.029562],1],["PlaneW",[-0.04596,-0.038005],1],["PlaneW",[-0.038568,-0.0452891],1],["PlaneW",[-0.03,-0.0512015],1],["PlaneW",[-0.02052,-0.0555589],1],["PlaneW",[-0.010416,-0.0582254],1],["PlaneW",[0,-0.0591241],1],[]]
                        }
                    },
                    # Class: CfgVehicles|RHS_T50_base|MFD|HMD|Draw|HeadOutside|Locking [Indent level: 5],
                    "locking": {
                        "blinkingpattern": [0.2,0.2],
                        "blinkingstartson": 1,
                        "condition": "missileLocking",
                        # Class: CfgVehicles|RHS_T50_base|MFD|HMD|Draw|HeadOutside|Locking|CircleLock [Indent level: 6],
                        "circlelock": {
                            "type": "line",
                            "width": 12,
                            "points": [["Target",[0,-0.0591241],1],["Target",[0.010416,-0.0582254],1],["Target",[0.02052,-0.0555589],1],["Target",[0.03,-0.0512015],1],["Target",[0.038568,-0.0452891],1],["Target",[0.04596,-0.038005],1],["Target",[0.05196,-0.029562],1],["Target",[0.056382,-0.0202204],1],["Target",[0.059088,-0.0102639],1],["Target",[0.06,0],1],["Target",[0.059088,0.0102639],1],["Target",[0.056382,0.0202204],1],["Target",[0.05196,0.029562],1],["Target",[0.04596,0.038005],1],["Target",[0.038568,0.0452891],1],["Target",[0.03,0.0512015],1],["Target",[0.02052,0.0555589],1],["Target",[0.010416,0.0582254],1],["Target",[0,0.0591241],1],["Target",[-0.010416,0.0582254],1],["Target",[-0.02052,0.0555589],1],["Target",[-0.03,0.0512015],1],["Target",[-0.038568,0.0452891],1],["Target",[-0.04596,0.038005],1],["Target",[-0.05196,0.029562],1],["Target",[-0.056382,0.0202204],1],["Target",[-0.059088,0.0102639],1],["Target",[-0.06,0],1],["Target",[-0.059088,-0.0102639],1],["Target",[-0.056382,-0.0202204],1],["Target",[-0.05196,-0.029562],1],["Target",[-0.04596,-0.038005],1],["Target",[-0.038568,-0.0452891],1],["Target",[-0.03,-0.0512015],1],["Target",[-0.02052,-0.0555589],1],["Target",[-0.010416,-0.0582254],1],["Target",[0,-0.0591241],1],[]]
                        }
                    },
                    # Class: CfgVehicles|RHS_T50_base|MFD|HMD|Draw|HeadOutside|Locked [Indent level: 5],
                    "locked": {
                        "condition": "missileLocked",
                        # Class: CfgVehicles|RHS_T50_base|MFD|HMD|Draw|HeadOutside|Locked|CircleLock [Indent level: 6],
                        "circlelock": {
                            "type": "line",
                            "width": 12,
                            "points": [["Target",[0,-0.0591241],1],["Target",[0.010416,-0.0582254],1],["Target",[0.02052,-0.0555589],1],["Target",[0.03,-0.0512015],1],["Target",[0.038568,-0.0452891],1],["Target",[0.04596,-0.038005],1],["Target",[0.05196,-0.029562],1],["Target",[0.056382,-0.0202204],1],["Target",[0.059088,-0.0102639],1],["Target",[0.06,0],1],["Target",[0.059088,0.0102639],1],["Target",[0.056382,0.0202204],1],["Target",[0.05196,0.029562],1],["Target",[0.04596,0.038005],1],["Target",[0.038568,0.0452891],1],["Target",[0.03,0.0512015],1],["Target",[0.02052,0.0555589],1],["Target",[0.010416,0.0582254],1],["Target",[0,0.0591241],1],["Target",[-0.010416,0.0582254],1],["Target",[-0.02052,0.0555589],1],["Target",[-0.03,0.0512015],1],["Target",[-0.038568,0.0452891],1],["Target",[-0.04596,0.038005],1],["Target",[-0.05196,0.029562],1],["Target",[-0.056382,0.0202204],1],["Target",[-0.059088,0.0102639],1],["Target",[-0.06,0],1],["Target",[-0.059088,-0.0102639],1],["Target",[-0.056382,-0.0202204],1],["Target",[-0.05196,-0.029562],1],["Target",[-0.04596,-0.038005],1],["Target",[-0.038568,-0.0452891],1],["Target",[-0.03,-0.0512015],1],["Target",[-0.02052,-0.0555589],1],["Target",[-0.010416,-0.0582254],1],["Target",[0,-0.0591241],1],[]]
                        }
                    },
                    # Class: CfgVehicles|RHS_T50_base|MFD|HMD|Draw|HeadOutside|SpeedNumber [Indent level: 5],
                    "speednumber": {
                        "type": "text",
                        "source": "speed",
                        "sourcescale": 3.6,
                        "sourcelength": 3,
                        "align": "left",
                        "scale": 1,
                        "pos": [[0.21,0.11],1],
                        "right": [[0.255,0.11],1],
                        "down": [[0.21,0.155],1]
                    },
                    # Class: CfgVehicles|RHS_T50_base|MFD|HMD|Draw|HeadOutside|SpeedText [Indent level: 5],
                    "speedtext": {
                        "type": "text",
                        "source": "static",
                        "text": "И",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": [[0.24,0.11],1],
                        "right": [[0.285,0.11],1],
                        "down": [[0.24,0.155],1]
                    },
                    # Class: CfgVehicles|RHS_T50_base|MFD|HMD|Draw|HeadOutside|MachNumber [Indent level: 5],
                    "machnumber": {
                        "sourcescale": 0.002939,
                        "sourcelength": 1,
                        "sourceprecision": 2,
                        "pos": [[0.21,0.15],1],
                        "right": [[0.255,0.15],1],
                        "down": [[0.21,0.195],1],
                        "type": "text",
                        "source": "speed",
                        "align": "left",
                        "scale": 1
                    },
                    # Class: CfgVehicles|RHS_T50_base|MFD|HMD|Draw|HeadOutside|MachText [Indent level: 5],
                    "machtext": {
                        "type": "text",
                        "source": "static",
                        "text": "М",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": [[0.24,0.15],1],
                        "right": [[0.285,0.15],1],
                        "down": [[0.24,0.195],1]
                    },
                    # Class: CfgVehicles|RHS_T50_base|MFD|HMD|Draw|HeadOutside|TerrainNumber [Indent level: 5],
                    "terrainnumber": {
                        "type": "text",
                        "source": "altitudeAGL",
                        "sourcescale": 1,
                        "sourcelength": 3,
                        "sourceoffset": -2,
                        "align": "right",
                        "scale": 1,
                        "pos": [[0.78,0.15],1],
                        "right": [[0.825,0.15],1],
                        "down": [[0.78,0.195],1]
                    },
                    # Class: CfgVehicles|RHS_T50_base|MFD|HMD|Draw|HeadOutside|RadarText [Indent level: 5],
                    "radartext": {
                        "type": "text",
                        "source": "static",
                        "text": "Р",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": [[0.86,0.15],1],
                        "right": [[0.905,0.15],1],
                        "down": [[0.86,0.195],1]
                    },
                    # Class: CfgVehicles|RHS_T50_base|MFD|HMD|Draw|HeadOutside|AltitudeNumber [Indent level: 5],
                    "altitudenumber": {
                        "type": "text",
                        "source": "altitudeASL",
                        "sourcescale": 1,
                        "sourcelength": 3,
                        "align": "right",
                        "scale": 1,
                        "pos": [[0.78,0.11],1],
                        "right": [[0.825,0.11],1],
                        "down": [[0.78,0.155],1]
                    },
                    # Class: CfgVehicles|RHS_T50_base|MFD|HMD|Draw|HeadOutside|RadarBoxes [Indent level: 5],
                    "radarboxes": {
                        "type": "radartoview",
                        "pos0": [0.5,0.5],
                        "pos10": [0.774,0.77],
                        "width": 3,
                        "points": [[[0,-0.019708],1],[[0.003472,-0.0194085],1],[[0.00684,-0.0185196],1],[[0.01,-0.0170672],1],[[0.012856,-0.0150964],1],[[0.01532,-0.0126683],1],[[0.01732,-0.00985401],1],[[0.018794,-0.00674015],1],[[0.019696,-0.00342131],1],[[0.02,0],1],[[0.019696,0.00342131],1],[[0.018794,0.00674015],1],[[0.01732,0.00985401],1],[[0.01532,0.0126683],1],[[0.012856,0.0150964],1],[[0.01,0.0170672],1],[[0.00684,0.0185196],1],[[0.003472,0.0194085],1],[[0,0.019708],1],[[-0.003472,0.0194085],1],[[-0.00684,0.0185196],1],[[-0.01,0.0170672],1],[[-0.012856,0.0150964],1],[[-0.01532,0.0126683],1],[[-0.01732,0.00985401],1],[[-0.018794,0.00674015],1],[[-0.019696,0.00342131],1],[[-0.02,0],1],[[-0.019696,-0.00342131],1],[[-0.018794,-0.00674015],1],[[-0.01732,-0.00985401],1],[[-0.01532,-0.0126683],1],[[-0.012856,-0.0150964],1],[[-0.01,-0.0170672],1],[[-0.00684,-0.0185196],1],[[-0.003472,-0.0194085],1],[[0,-0.019708],1],[]]
                    },
                    # Class: CfgVehicles|RHS_T50_base|MFD|HMD|Draw|HeadOutside|WeaponsGroupMGun [Indent level: 5],
                    "weaponsgroupmgun": {
                        "condition": "mgun",
                        # Class: CfgVehicles|RHS_T50_base|MFD|HMD|Draw|HeadOutside|WeaponsGroupMGun|WeaponName [Indent level: 6],
                        "weaponname": {
                            "type": "text",
                            "source": "static",
                            "sourcescale": 1,
                            "text": "ГШ",
                            "align": "right",
                            "scale": 1,
                            "pos": [[0.14,0.74],1],
                            "right": [[0.19,0.74],1],
                            "down": [[0.14,0.785],1]
                        }
                    },
                    # Class: CfgVehicles|RHS_T50_base|MFD|HMD|Draw|HeadOutside|WeaponsGroup [Indent level: 5],
                    "weaponsgroup": {
                        "condition": "1-mgun",
                        # Class: CfgVehicles|RHS_T50_base|MFD|HMD|Draw|HeadOutside|WeaponsGroup|PylonName1 [Indent level: 6],
                        "pylonname1": {
                            "type": "pylonicon",
                            "pos": [[0.145,0.72],1],
                            "pylon": 1,
                            "name": "rhs_rus_ammoname_right"
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|HMD|Draw|HeadOutside|WeaponsGroup|PylonName2 [Indent level: 6],
                        "pylonname2": {
                            "pylon": 2,
                            "type": "pylonicon",
                            "pos": [[0.145,0.72],1],
                            "name": "rhs_rus_ammoname_right"
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|HMD|Draw|HeadOutside|WeaponsGroup|PylonName3 [Indent level: 6],
                        "pylonname3": {
                            "pylon": 3,
                            "type": "pylonicon",
                            "pos": [[0.145,0.72],1],
                            "name": "rhs_rus_ammoname_right"
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|HMD|Draw|HeadOutside|WeaponsGroup|PylonName4 [Indent level: 6],
                        "pylonname4": {
                            "pylon": 4,
                            "type": "pylonicon",
                            "pos": [[0.145,0.72],1],
                            "name": "rhs_rus_ammoname_right"
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|HMD|Draw|HeadOutside|WeaponsGroup|PylonName5 [Indent level: 6],
                        "pylonname5": {
                            "pylon": 5,
                            "type": "pylonicon",
                            "pos": [[0.145,0.72],1],
                            "name": "rhs_rus_ammoname_right"
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|HMD|Draw|HeadOutside|WeaponsGroup|PylonName6 [Indent level: 6],
                        "pylonname6": {
                            "pylon": 6,
                            "type": "pylonicon",
                            "pos": [[0.145,0.72],1],
                            "name": "rhs_rus_ammoname_right"
                        }
                    },
                    # Class: CfgVehicles|RHS_T50_base|MFD|HMD|Draw|HeadOutside|AmmoCount [Indent level: 5],
                    "ammocount": {
                        "type": "text",
                        "source": "ammo",
                        "sourcescale": 1,
                        "align": "right",
                        "scale": 1,
                        "pos": [[0.14,"0.000+0.79"],1],
                        "right": [[0.19,"0.000+0.79"],1],
                        "down": [[0.14,"0.045+0.79"],1]
                    },
                    # Class: CfgVehicles|RHS_T50_base|MFD|HMD|Draw|HeadOutside|TargetLocked [Indent level: 5],
                    "targetlocked": {
                        "condition": "TargetHeight>=1",
                        # Class: CfgVehicles|RHS_T50_base|MFD|HMD|Draw|HeadOutside|TargetLocked|shape [Indent level: 6],
                        "shape": {
                            "type": "line",
                            "width": 4,
                            "points": [[[0.145,0.06],1],[[0.215,0.06],1],[[0.215,0.11],1],[[0.145,0.11],1],[[0.145,0.06],1],[],[[0.777,0.06],1],[[0.847,0.06],1],[[0.847,0.11],1],[[0.777,0.11],1],[[0.777,0.06],1]]
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|HMD|Draw|HeadOutside|TargetLocked|TargetSpeed [Indent level: 6],
                        "targetspeed": {
                            "source": "LarTargetSpeed",
                            "sourcescale": 0.36,
                            "pos": [[0.21,0.065],1],
                            "right": [[0.255,0.065],1],
                            "down": [[0.21,0.11],1],
                            "type": "text",
                            "sourcelength": 3,
                            "align": "left",
                            "scale": 1
                        },
                        # Class: CfgVehicles|RHS_T50_base|MFD|HMD|Draw|HeadOutside|TargetLocked|TargetHeight [Indent level: 6],
                        "targetheight": {
                            "source": "TargetHeight",
                            "sourcescale": 0.1,
                            "sourcelength": 3,
                            "pos": [[0.78,0.065],1],
                            "right": [[0.825,0.065],1],
                            "down": [[0.78,0.11],1],
                            "type": "text",
                            "align": "right",
                            "scale": 1
                        }
                    },
                    # Class: CfgVehicles|RHS_T50_base|MFD|HMD|Draw|HeadOutside|HeadingHeadNumber [Indent level: 5],
                    "headingheadnumber": {
                        "type": "text",
                        "source": "cameraDir",
                        "sourcescale": 1,
                        "align": "center",
                        "scale": 1,
                        "pos": [["0.80-0.302","0.082+0.001"],1],
                        "right": [["0.83-0.302","0.082+0.001"],1],
                        "down": [["0.80-0.302","0.113+0.001"],1]
                    },
                    # Class: CfgVehicles|RHS_T50_base|MFD|HMD|Draw|HeadOutside|HeadingArrow [Indent level: 5],
                    "headingarrow": {
                        "type": "line",
                        "width": 3,
                        "points": [[[0.478,0.075],1],[[0.522,0.075],1],[[0.552,0.095],1],[[0.522,0.115],1],[[0.478,0.115],1],[[0.448,0.095],1],[[0.478,0.075],1],[]]
                    }
                },
                # Class: CfgVehicles|RHS_T50_base|MFD|HMD|Draw|InvalidLock [Indent level: 4],
                "invalidlock": {
                    "condition": "abs(cameraHeadingDiff) > 85 - missileLocked - missileLocking",
                    # Class: CfgVehicles|RHS_T50_base|MFD|HMD|Draw|InvalidLock|CircleLock [Indent level: 5],
                    "circlelock": {
                        "type": "line",
                        "width": 12,
                        "points": [["PlaneW",[-0.0707107,0.0696784],1],["PlaneW",[0.0707107,-0.0696784],1],[],["PlaneW",[-0.0707107,-0.0696784],1],["PlaneW",[0.0707107,0.0696784],1]]
                    }
                }
            }
        }
    },
    "enginemoi": 16,
    "maxomega": 2000,
    "dampingratefullthrottle": 0.4,
    "clutchstrength": 100,
    # Class: CfgVehicles|RHS_T50_base|Wheels [Indent level: 1],
    "wheels": {
        "disablewheelswhendestroyed": 1,
        # Class: CfgVehicles|RHS_T50_base|Wheels|Wheel_1 [Indent level: 2],
        "wheel_1": {
            "bonename": "gear_f1",
            "steering": 1,
            "side": "left",
            "center": "Wheel_1_center",
            "boundary": "Wheel_1_rim",
            "width": 0.16,
            "mass": 150,
            "moi": 40,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 21500,
            "maxhandbraketorque": 0,
            "susptraveldirection": [0,-1,0],
            "suspforceapppointoffset": "Wheel_1_center",
            "tireforceapppointoffset": "Wheel_1_center",
            "maxcompression": 0.05,
            "maxdroop": 0.05,
            "sprungmass": 4066,
            "springstrength": 56600,
            "springdamperrate": 115570,
            "longitudinalstiffnessperunitgravity": 5000,
            "latstiffx": 25,
            "latstiffy": 180,
            "frictionvsslipgraph": [[0,1],[0.5,1],[1,1]]
        },
        # Class: CfgVehicles|RHS_T50_base|Wheels|Wheel_1_fake [Indent level: 2],
        "wheel_1_fake": {
            "bonename": "gear_f1",
            "steering": 1,
            "side": "left",
            "center": "Wheel_1_center",
            "boundary": "Wheel_1_rim",
            "width": 0.16,
            "mass": 150,
            "moi": 40,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 21500,
            "maxhandbraketorque": 0,
            "susptraveldirection": [0,-1,0],
            "suspforceapppointoffset": "Wheel_1_center",
            "tireforceapppointoffset": "Wheel_1_center",
            "maxcompression": 0.05,
            "maxdroop": 0.05,
            "sprungmass": 4066,
            "springstrength": 56600,
            "springdamperrate": 115570,
            "longitudinalstiffnessperunitgravity": 5000,
            "latstiffx": 25,
            "latstiffy": 180,
            "frictionvsslipgraph": [[0,1],[0.5,1],[1,1]]
        },
        # Class: CfgVehicles|RHS_T50_base|Wheels|Wheel_2 [Indent level: 2],
        "wheel_2": {
            "bonename": "gear_l2",
            "steering": 0,
            "center": "Wheel_2_center",
            "boundary": "Wheel_2_rim",
            "width": 0.28,
            "maxcompression": 0.06,
            "maxdroop": 0.06,
            "sprungmass": 1952,
            "springstrength": 51000,
            "springdamperrate": 20569.6,
            "suspforceapppointoffset": "Wheel_2_center",
            "tireforceapppointoffset": "Wheel_2_center",
            "side": "left",
            "mass": 150,
            "moi": 40,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 21500,
            "maxhandbraketorque": 0,
            "susptraveldirection": [0,-1,0],
            "longitudinalstiffnessperunitgravity": 5000,
            "latstiffx": 25,
            "latstiffy": 180,
            "frictionvsslipgraph": [[0,1],[0.5,1],[1,1]]
        },
        # Class: CfgVehicles|RHS_T50_base|Wheels|Wheel_3 [Indent level: 2],
        "wheel_3": {
            "bonename": "gear_r2",
            "side": "right",
            "center": "Wheel_3_center",
            "boundary": "Wheel_3_rim",
            "suspforceapppointoffset": "Wheel_3_center",
            "tireforceapppointoffset": "Wheel_3_center",
            "steering": 0,
            "width": 0.28,
            "maxcompression": 0.06,
            "maxdroop": 0.06,
            "sprungmass": 1952,
            "springstrength": 51000,
            "springdamperrate": 20569.6,
            "mass": 150,
            "moi": 40,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 21500,
            "maxhandbraketorque": 0,
            "susptraveldirection": [0,-1,0],
            "longitudinalstiffnessperunitgravity": 5000,
            "latstiffx": 25,
            "latstiffy": 180,
            "frictionvsslipgraph": [[0,1],[0.5,1],[1,1]]
        }
    },
    "soundsetsonicboom": ["Plane_Fighter_SonicBoom_SoundSet"],
    "soundlocked": ["A3|Sounds_F_Jets|vehicles|air|Shared|FX_Plane_Jet_lockedOn1",1,1],
    "soundincommingmissile": ["A3|Sounds_F_Jets|vehicles|air|Shared|FX_Plane_Jet_lockedon2",1,1.5],
    "soundgearup": ["A3|Sounds_F_Jets|vehicles|air|Shared|FX_Plane_Jet_gear_up",2.25,1,250],
    "soundgeardown": ["A3|Sounds_F_Jets|vehicles|air|Shared|FX_Plane_Jet_gear_down",2.25,1,250],
    "soundflapsup": ["A3|Sounds_F_Jets|vehicles|air|Shared|FX_Plane_Jet_Flaps_Up",1.5,1,150],
    "soundflapsdown": ["A3|Sounds_F_Jets|vehicles|air|Shared|FX_Plane_Jet_Flaps_Down",1.5,1,150],
    "cabinopensound": ["A3|Sounds_F_Jets|vehicles|air|Plane_Fighter_02|FX_Plane_Fighter_02_cabine_open_ext",3.16228,1,40],
    "cabinclosesound": ["A3|Sounds_F_Jets|vehicles|air|Plane_Fighter_02|FX_Plane_Fighter_02_cabine_close_ext",3.16228,1,40],
    "cabinopensoundinternal": ["A3|Sounds_F_Jets|vehicles|air|Plane_Fighter_02|FX_Plane_Fighter_02_cabine_open_int",10,1,40],
    "cabinclosesoundinternal": ["A3|Sounds_F_Jets|vehicles|air|Plane_Fighter_02|FX_Plane_Fighter_02_cabine_close_int",10,1,40],
    "soundengineonint": ["A3|Sounds_F_Jets|vehicles|air|Plane_Fighter_02|O_Plane_Fighter_02_engine_start_int",1,1],
    "soundengineonext": ["A3|Sounds_F_Jets|vehicles|air|Plane_Fighter_02|O_Plane_Fighter_02_engine_start_ext",1.75,1,300],
    "soundengineoffint": ["A3|Sounds_F_Jets|vehicles|air|Plane_Fighter_02|O_Plane_Fighter_02_engine_shut_int",1,1],
    "soundengineoffext": ["A3|Sounds_F_Jets|vehicles|air|Plane_Fighter_02|O_Plane_Fighter_02_engine_shut_ext",1.75,1,300],
    "soundgetin": ["A3|Sounds_F|vehicles|air|CAS_01|getin_wipeout",1,1,40],
    "soundgetout": ["A3|Sounds_F|air|Plane_Fighter_03|getout",1,1,40],
    "soundwatercollision1": ["A3|Sounds_F|vehicles|crashes|planes|plane_crash_water_1",1.41254,1,500],
    "soundwatercollision2": ["A3|Sounds_F|vehicles|crashes|planes|plane_crash_water_2",1.41254,1,500],
    "soundwatercrashes": ["soundWaterCollision1",0.5,"soundWaterCollision2",0.5],
    "buildcrash0": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_1",1,1,900],
    "buildcrash1": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_2",1,1,900],
    "buildcrash2": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_3",1,1,900],
    "buildcrash3": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_4",1,1,900],
    "soundbuildingcrash": ["buildCrash0",0.25,"buildCrash1",0.25,"buildCrash2",0.25,"buildCrash3",0.25],
    "woodcrash0": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_wood_ext_1",3.16228,1,900],
    "woodcrash1": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_wood_ext_2",3.16228,1,900],
    "woodcrash2": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_wood_ext_6",3.16228,1,900],
    "woodcrash3": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_wood_ext_8",3.16228,1,900],
    "soundwoodcrash": ["woodCrash0",0.25,"woodCrash1",0.25,"woodCrash2",0.25,"woodCrash3",0.25],
    "armorcrash0": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_1",1,1,900],
    "armorcrash1": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_2",1,1,900],
    "armorcrash2": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_3",1,1,900],
    "armorcrash3": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_4",1,1,900],
    "soundarmorcrash": ["ArmorCrash0",0.25,"ArmorCrash1",0.25,"ArmorCrash2",0.25,"ArmorCrash3",0.25],
    "crash0": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_1",1,1,900],
    "crash1": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_2",1,1,900],
    "crash2": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_3",1,1,900],
    "crash3": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_4",1,1,900],
    "soundcrashes": ["Crash0",0.25,"Crash1",0.25,"Crash2",0.25,"Crash3",0.25],
    "sounddammage": ["",0.562341,1],
    # Class: CfgVehicles|RHS_T50_base|scrubLandInt [Indent level: 1],
    "scrublandint": {
        "sound": ["A3|Sounds_F|vehicles|air|noises|wheelsInt",1,1,100],
        "frequency": 1,
        "volume": "(scrubLand factor[0.01, 0.20])"
    },
    # Class: CfgVehicles|RHS_T50_base|Sounds [Indent level: 1],
    "sounds": {
        "soundsets": ["Plane_Fighter_02_EngineLowExt_SoundSet","Plane_Fighter_02_EngineHighExt_SoundSet","Plane_Fighter_02_ForsageExt_SoundSet","Plane_Fighter_02_WindNoiseExt_SoundSet","Plane_Fighter_02_EngineExt_Dist_Front_SoundSet","Plane_Fighter_02_EngineExt_Middle_SoundSet","Plane_Fighter_02_EngineExt_Dist_Rear_SoundSet","Plane_Fighter_02_EngineLowInt_SoundSet","Plane_Fighter_02_EngineHighInt_SoundSet","Plane_Fighter_02_ForsageInt_SoundSet","Plane_Fighter_02_WindNoiseInt_SoundSet","Plane_Fighter_02_VelocityInt_SoundSet"]
    },
    "driveoncomponent": [],
    # Class: CfgVehicles|RHS_T50_base|Exhausts [Indent level: 1],
    "exhausts": {
        # Class: CfgVehicles|RHS_T50_base|Exhausts|Exhaust1 [Indent level: 2]
        "exhaust1": {
            "position": "exhaust1",
            "direction": "exhaust1_dir",
            "effect": "ExhaustsEffectPlaneHP",
            "engineindex": 0
        },
        # Class: CfgVehicles|RHS_T50_base|Exhausts|Exhaust2 [Indent level: 2],
        "exhaust2": {
            "position": "exhaust2",
            "direction": "exhaust2_dir",
            "effect": "ExhaustsEffectPlaneHP",
            "engineindex": 1
        }
    },
    # Class: CfgVehicles|RHS_T50_base|WingVortices [Indent level: 1],
    "wingvortices": {
        # Class: CfgVehicles|RHS_T50_base|WingVortices|WingTipLeft [Indent level: 2]
        "wingtipleft": {
            "effectname": "WingVortices",
            "position": "wing_vortex_l"
        },
        # Class: CfgVehicles|RHS_T50_base|WingVortices|WingTipRight [Indent level: 2],
        "wingtipright": {
            "effectname": "WingVortices",
            "position": "wing_vortex_r"
        },
        # Class: CfgVehicles|RHS_T50_base|WingVortices|BodyLeft [Indent level: 2],
        "bodyleft": {
            "effectname": "BodyVortices",
            "position": "body_vapour_L_S"
        },
        # Class: CfgVehicles|RHS_T50_base|WingVortices|BodyRight [Indent level: 2],
        "bodyright": {
            "effectname": "BodyVortices",
            "position": "body_vapour_R_S"
        }
    },
    "attenuationeffecttype": "PlaneAttenuation",
    "damageresistance": 0.00336,
    "armor": 80,
    "armorstructural": 3,
    "armorlights": 0.1,
    "explosionshielding": 1,
    "epeimpulsedamagecoef": 1,
    # Class: CfgVehicles|RHS_T50_base|Hitpoints [Indent level: 1],
    "hitpoints": {
        # Class: CfgVehicles|RHS_T50_base|Hitpoints|HitHull [Indent level: 2]
        "hithull": {
            "armor": 999,
            "explosionshielding": 0,
            "passthrough": 0.01,
            "minimalhit": 1,
            "radius": 0.15,
            "material": -1,
            "name": "hit_hull",
            "visual": "-",
            "depends": "Total"
        },
        # Class: CfgVehicles|RHS_T50_base|Hitpoints|HitAvionics [Indent level: 2],
        "hitavionics": {
            "armor": 0.2,
            "explosionshielding": 0.2,
            "passthrough": 0.01,
            "minimalhit": 0.1,
            "radius": 0.08,
            "material": -1,
            "name": "hit_avionics",
            "visual": "vis_avionics",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_T50_base|Hitpoints|HitEngine_c [Indent level: 2],
        "hitengine_c": {
            "armor": 0.7,
            "explosionshielding": 0.65,
            "passthrough": 0.01,
            "minimalhit": 0.01,
            "radius": 0.07,
            "material": -1,
            "name": "hit_engine",
            "visual": "vis_engine",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_T50_base|Hitpoints|HitEngine [Indent level: 2],
        "hitengine": {
            "armor": 0.7,
            "explosionshielding": 0.65,
            "passthrough": 0.01,
            "minimalhit": 0.01,
            "radius": 0.07,
            "material": -1,
            "name": "hit_engine_l",
            "visual": "vis_engine_l",
            "depends": "HitEngine_c*0.7"
        },
        # Class: CfgVehicles|RHS_T50_base|Hitpoints|HitEngine2 [Indent level: 2],
        "hitengine2": {
            "armor": 0.7,
            "explosionshielding": 0.65,
            "passthrough": 0.01,
            "minimalhit": 0.01,
            "radius": 0.07,
            "material": -1,
            "name": "hit_engine_r",
            "visual": "vis_engine_r",
            "depends": "HitEngine_c*0.7"
        },
        # Class: CfgVehicles|RHS_T50_base|Hitpoints|HitFuel [Indent level: 2],
        "hitfuel": {
            "armor": 1.1,
            "explosionshielding": 0.4,
            "passthrough": 0.01,
            "minimalhit": 0.1,
            "radius": 0.1,
            "material": -1,
            "name": "hit_fuel",
            "visual": "vis_fuel",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_T50_base|Hitpoints|HitFuel_left [Indent level: 2],
        "hitfuel_left": {
            "armor": 1.1,
            "explosionshielding": 0.4,
            "passthrough": 0.01,
            "minimalhit": 0.1,
            "radius": 0.1,
            "material": -1,
            "name": "hit_fuel_wing_l",
            "visual": "vis_wing_l",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_T50_base|Hitpoints|HitFuel_right [Indent level: 2],
        "hitfuel_right": {
            "armor": 1.1,
            "explosionshielding": 0.4,
            "passthrough": 0.01,
            "minimalhit": 0.1,
            "radius": 0.1,
            "material": -1,
            "name": "hit_fuel_wing_r",
            "visual": "vis_wing_r",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_T50_base|Hitpoints|HitFuel2 [Indent level: 2],
        "hitfuel2": {
            "armor": 1.1,
            "explosionshielding": 0.4,
            "passthrough": 0.01,
            "minimalhit": 1,
            "radius": 0.01,
            "material": -1,
            "name": "hit_fuel",
            "visual": "-",
            "depends": "(HitFuel_left+HitFuel_right)*0.5"
        },
        # Class: CfgVehicles|RHS_T50_base|Hitpoints|HitLAileron_link [Indent level: 2],
        "hitlaileron_link": {
            "armor": 0.7,
            "explosionshielding": 0.7,
            "passthrough": 0.01,
            "minimalhit": 0.1,
            "radius": 0.12,
            "material": -1,
            "name": "hit_aileron_link_l",
            "visual": "-",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_T50_base|Hitpoints|HitRAileron_link [Indent level: 2],
        "hitraileron_link": {
            "armor": 0.7,
            "explosionshielding": 0.7,
            "passthrough": 0.01,
            "minimalhit": 0.1,
            "radius": 0.12,
            "material": -1,
            "name": "hit_aileron_link_r",
            "visual": "-",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_T50_base|Hitpoints|HitLAileron [Indent level: 2],
        "hitlaileron": {
            "armor": 0.2,
            "explosionshielding": 0.3,
            "passthrough": 0.01,
            "minimalhit": 0.1,
            "radius": 0.13,
            "material": -1,
            "name": "hit_aileron_l",
            "visual": "vis_wing_l",
            "depends": "HitLAileron_link*0.7"
        },
        # Class: CfgVehicles|RHS_T50_base|Hitpoints|HitRAileron [Indent level: 2],
        "hitraileron": {
            "armor": 0.2,
            "explosionshielding": 0.3,
            "passthrough": 0.01,
            "minimalhit": 0.1,
            "radius": 0.13,
            "material": -1,
            "name": "hit_aileron_r",
            "visual": "vis_wing_r",
            "depends": "HitRAileron_link*0.7"
        },
        # Class: CfgVehicles|RHS_T50_base|Hitpoints|HitControlRear [Indent level: 2],
        "hitcontrolrear": {
            "armor": 0.2,
            "explosionshielding": 0.3,
            "passthrough": 0.01,
            "minimalhit": 0.1,
            "radius": 0.04,
            "material": -1,
            "name": "hit_control_link",
            "visual": "-",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_T50_base|Hitpoints|HitLCElevator [Indent level: 2],
        "hitlcelevator": {
            "armor": 0.2,
            "explosionshielding": 0.3,
            "passthrough": 0.01,
            "minimalhit": 0.1,
            "radius": 0.15,
            "material": -1,
            "name": "hit_elevator_l",
            "visual": "vis_elevator_l",
            "depends": "HitControlRear"
        },
        # Class: CfgVehicles|RHS_T50_base|Hitpoints|HitRElevator [Indent level: 2],
        "hitrelevator": {
            "armor": 0.2,
            "explosionshielding": 0.3,
            "passthrough": 0.01,
            "minimalhit": 0.1,
            "radius": 0.15,
            "material": -1,
            "name": "hit_elevator_r",
            "visual": "vis_elevator_r",
            "depends": "HitControlRear"
        },
        # Class: CfgVehicles|RHS_T50_base|Hitpoints|HitLCRudder [Indent level: 2],
        "hitlcrudder": {
            "armor": 0.2,
            "explosionshielding": 0.3,
            "passthrough": 0.01,
            "minimalhit": 0.1,
            "radius": 0.15,
            "material": -1,
            "name": "hit_rudder_l",
            "visual": "vis_rudder_l",
            "depends": "HitControlRear"
        },
        # Class: CfgVehicles|RHS_T50_base|Hitpoints|HitRightRudder [Indent level: 2],
        "hitrightrudder": {
            "armor": 0.2,
            "explosionshielding": 0.3,
            "passthrough": 0.01,
            "minimalhit": 0.1,
            "radius": 0.15,
            "material": -1,
            "name": "hit_rudder_r",
            "visual": "vis_rudder_r",
            "depends": "HitControlRear"
        },
        # Class: CfgVehicles|RHS_T50_base|Hitpoints|HitGlass1 [Indent level: 2],
        "hitglass1": {
            "armor": 0.2,
            "explosionshielding": 0.6,
            "passthrough": 0.01,
            "minimalhit": 0.1,
            "radius": 0.4,
            "material": -1,
            "name": "glass1",
            "visual": "glass1",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_T50_base|Hitpoints|HitGlass2 [Indent level: 2],
        "hitglass2": {
            "armor": 0.2,
            "explosionshielding": 0.6,
            "passthrough": 0.01,
            "minimalhit": 0.1,
            "radius": 0.4,
            "material": -1,
            "name": "glass2",
            "visual": "glass2",
            "depends": "0"
        }
    },
    # Class: CfgVehicles|RHS_T50_base|AnimationSources [Indent level: 1],
    "animationsources": {
        # Class: CfgVehicles|RHS_T50_base|AnimationSources|Damper_1_source [Indent level: 2]
        "damper_1_source": {
            "source": "damper",
            "wheel": "Wheel_1"
        },
        # Class: CfgVehicles|RHS_T50_base|AnimationSources|Damper_2_source [Indent level: 2],
        "damper_2_source": {
            "source": "damper",
            "wheel": "Wheel_2"
        },
        # Class: CfgVehicles|RHS_T50_base|AnimationSources|Damper_3_source [Indent level: 2],
        "damper_3_source": {
            "source": "damper",
            "wheel": "Wheel_3"
        },
        # Class: CfgVehicles|RHS_T50_base|AnimationSources|Wheel_1_source [Indent level: 2],
        "wheel_1_source": {
            "source": "wheel",
            "wheel": "Wheel_1"
        },
        # Class: CfgVehicles|RHS_T50_base|AnimationSources|Wheel_2_source [Indent level: 2],
        "wheel_2_source": {
            "source": "wheel",
            "wheel": "Wheel_2"
        },
        # Class: CfgVehicles|RHS_T50_base|AnimationSources|Wheel_3_source [Indent level: 2],
        "wheel_3_source": {
            "source": "wheel",
            "wheel": "Wheel_3"
        },
        # Class: CfgVehicles|RHS_T50_base|AnimationSources|CollisionLightRed_source [Indent level: 2],
        "collisionlightred_source": {
            "source": "MarkerLight",
            "markerlight": "CollisionRed"
        },
        # Class: CfgVehicles|RHS_T50_base|AnimationSources|CollisionLightWhite_source [Indent level: 2],
        "collisionlightwhite_source": {
            "markerlight": "CollisionWhite",
            "source": "MarkerLight"
        },
        # Class: CfgVehicles|RHS_T50_base|AnimationSources|Muzzle_flash [Indent level: 2],
        "muzzle_flash": {
            "source": "ammorandom",
            "weapon": "rhs_weap_GSh30"
        },
        # Class: CfgVehicles|RHS_T50_base|AnimationSources|Cannon_30mm_ammorandom [Indent level: 2],
        "cannon_30mm_ammorandom": {
            "source": "ammorandom",
            "weapon": "rhs_weap_GSh30"
        },
        # Class: CfgVehicles|RHS_T50_base|AnimationSources|Cannon_30mm_revolving [Indent level: 2],
        "cannon_30mm_revolving": {
            "source": "revolving",
            "weapon": "rhs_weap_GSh30"
        },
        # Class: CfgVehicles|RHS_T50_base|AnimationSources|Hatch_open [Indent level: 2],
        "hatch_open": {
            "source": "user",
            "initphase": 0,
            "animperiod": 0.4
        },
        # Class: CfgVehicles|RHS_T50_base|AnimationSources|Numbers_hide [Indent level: 2],
        "numbers_hide": {
            "source": "user",
            "initphase": 0,
            "animperiod": 0.001
        },
        # Class: CfgVehicles|RHS_T50_base|AnimationSources|afterburner_source [Indent level: 2],
        "afterburner_source": {
            "source": "user",
            "initphase": 0,
            "animperiod": 1.5
        },
        # Class: CfgVehicles|RHS_T50_base|AnimationSources|lever_pilot_1 [Indent level: 2],
        "lever_pilot_1": {
            "source": "user",
            "initphase": 0,
            "animperiod": 0.3
        },
        # Class: CfgVehicles|RHS_T50_base|AnimationSources|pods_hide [Indent level: 2],
        "pods_hide": {
            "source": "user",
            "initphase": 1,
            "animperiod": 0.001
        },
        # Class: CfgVehicles|RHS_T50_base|AnimationSources|eject [Indent level: 2],
        "eject": {
            "source": "door",
            "animperiod": 0.6,
            "initphase": 0
        },
        # Class: CfgVehicles|RHS_T50_base|AnimationSources|eject_hide [Indent level: 2],
        "eject_hide": {
            "source": "user",
            "animperiod": 0.6,
            "initphase": 0
        },
        # Class: CfgVehicles|RHS_T50_base|AnimationSources|Display2 [Indent level: 2],
        "display2": {
            "source": "user",
            "initphase": 0,
            "animperiod": 0.0001
        },
        # Class: CfgVehicles|RHS_T50_base|AnimationSources|form_lights_hide [Indent level: 2],
        "form_lights_hide": {
            "source": "user",
            "initphase": 0,
            "animperiod": 0.0001
        },
        # Class: CfgVehicles|RHS_T50_base|AnimationSources|Display2_wp1_rot [Indent level: 2],
        "display2_wp1_rot": {
            "source": "user",
            "initphase": 0,
            "animperiod": 0.0001
        },
        # Class: CfgVehicles|RHS_T50_base|AnimationSources|Display2_wp1_m [Indent level: 2],
        "display2_wp1_m": {
            "source": "user",
            "initphase": 0,
            "animperiod": 0.0001
        },
        # Class: CfgVehicles|RHS_T50_base|AnimationSources|Display2_select_wp [Indent level: 2],
        "display2_select_wp": {
            "source": "user",
            "initphase": 0,
            "animperiod": 0.0001
        },
        # Class: CfgVehicles|RHS_T50_base|AnimationSources|Display2_sector_hide [Indent level: 2],
        "display2_sector_hide": {
            "source": "user",
            "initphase": 0,
            "animperiod": 0.0001
        },
        # Class: CfgVehicles|RHS_T50_base|AnimationSources|Display2_sector_rot [Indent level: 2],
        "display2_sector_rot": {
            "source": "user",
            "initphase": 0,
            "animperiod": 0.0001
        },
        # Class: CfgVehicles|RHS_T50_base|AnimationSources|Display_Glonass_Map_X [Indent level: 2],
        "display_glonass_map_x": {
            "source": "user",
            "initphase": 0,
            "animperiod": 0.0001
        },
        # Class: CfgVehicles|RHS_T50_base|AnimationSources|Display_Glonass_Map_Y [Indent level: 2],
        "display_glonass_map_y": {
            "source": "user",
            "initphase": 0,
            "animperiod": 0.0001
        },
        # Class: CfgVehicles|RHS_T50_base|AnimationSources|display2_wp2_rot [Indent level: 2],
        "display2_wp2_rot": {
            "source": "user",
            "initphase": 0,
            "animperiod": 0.0001
        },
        # Class: CfgVehicles|RHS_T50_base|AnimationSources|display2_switch [Indent level: 2],
        "display2_switch": {
            "animperiod": 1,
            "source": "user",
            "initphase": 0
        },
        # Class: CfgVehicles|RHS_T50_base|AnimationSources|antenna_hide [Indent level: 2],
        "antenna_hide": {
            "source": "user",
            "initphase": 1,
            "animperiod": 0.001,
            "mass": 1,
            "displayname": "hide antenna"
        },
        # Class: CfgVehicles|RHS_T50_base|AnimationSources|sensors_hide [Indent level: 2],
        "sensors_hide": {
            "displayname": "hide sensors",
            "source": "user",
            "initphase": 1,
            "animperiod": 0.001,
            "mass": 1
        }
    },
    # Class: CfgVehicles|RHS_T50_base|MarkerLights [Indent level: 1],
    "markerlights": {
        # Class: CfgVehicles|RHS_T50_base|MarkerLights|PositionRed [Indent level: 2]
        "positionred": {
            "color": [0.8,0,0],
            "ambient": [0.08,0,0],
            "intensity": 500,
            "name": "PositionLight_red_1_pos",
            "drawlight": 1.5,
            "drawlightsize": 0.25,
            "drawlightcentersize": 0.04,
            "activelight": 0,
            "blinking": 0,
            "daylight": 0,
            "useflare": 0,
            # Class: CfgVehicles|RHS_T50_base|MarkerLights|PositionRed|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardlimitstart": 0.75,
                "hardlimitend": 1
            }
        },
        # Class: CfgVehicles|RHS_T50_base|MarkerLights|PositionGreen [Indent level: 2],
        "positiongreen": {
            "color": [0,0.8,0],
            "ambient": [0,0.08,0],
            "name": "PositionLight_green_1_pos",
            "intensity": 500,
            "drawlight": 1.5,
            "drawlightsize": 0.25,
            "drawlightcentersize": 0.04,
            "activelight": 0,
            "blinking": 0,
            "daylight": 0,
            "useflare": 0,
            # Class: CfgVehicles|RHS_T50_base|MarkerLights|PositionRed|Attenuation [Indent level: 3],
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
    # Class: CfgVehicles|RHS_T50_base|RenderTargets [Indent level: 1],
    "rendertargets": {
        # Class: CfgVehicles|RHS_T50_base|RenderTargets|right_mirror [Indent level: 2]
        "right_mirror": {
            "rendertarget": "rendertarget0",
            # Class: CfgVehicles|RHS_T50_base|RenderTargets|right_mirror|CameraView1 [Indent level: 3],
            "cameraview1": {
                "pointposition": "PIP_mirror_0",
                "pointdirection": "PIP_mirror_0_dir",
                "renderquality": 0,
                "rendervisionmode": 0,
                "fov": 1
            }
        },
        # Class: CfgVehicles|RHS_T50_base|RenderTargets|Glonass_Camera [Indent level: 2],
        "glonass_camera": {
            "rendertarget": "rendertarget4",
            # Class: CfgVehicles|RHS_T50_base|RenderTargets|Glonass_Camera|CameraView1 [Indent level: 3],
            "cameraview1": {
                "pointposition": "pip_GPS_1",
                "pointdirection": "pip_GPS_1_dir",
                "renderquality": 2,
                "rendervisionmode": 0,
                "fov": 0.7
            },
            "bboxes": ["PIP_4_TL","PIP_4_TR","PIP_4_BL","PIP_4_BR"]
        }
    },
    # Class: CfgVehicles|RHS_T50_base|compartmentsLights [Indent level: 1],
    "compartmentslights": {
        # Class: CfgVehicles|RHS_T50_base|compartmentsLights|Comp1 [Indent level: 2]
        "comp1": {
            # Class: CfgVehicles|RHS_T50_base|compartmentsLights|Comp1|Light_General [Indent level: 3]
            "light_general": {
                "color": [20,40,20],
                "ambient": [0,0,0],
                "intensity": 2.5,
                "size": 0,
                "useflare": 0,
                "flaresize": 0,
                "flaremaxdistance": 0,
                "daylight": 0,
                "blinking": 0,
                # Class: CfgVehicles|RHS_T50_base|compartmentsLights|Comp1|Light_General|Attenuation [Indent level: 4],
                "attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardlimitstart": 1.45,
                    "hardlimitend": 2.45
                },
                "point": "light_general"
            }
        }
    },
    # Class: CfgVehicles|RHS_T50_base|Reflectors [Indent level: 1],
    "reflectors": {
        # Class: CfgVehicles|RHS_T50_base|Reflectors|Left [Indent level: 2]
        "left": {
            "color": [7000,7500,10000,1],
            "ambient": [100,100,100],
            "position": "l svetlo",
            "selection": "l svetlo",
            "direction": "konec l svetla",
            "hitpoint": "l svetlo",
            "innerangle": 20,
            "outerangle": 60,
            "conefadecoef": 10,
            "intensity": 50,
            "useflare": 1,
            "daylight": 0,
            "flaresize": 1,
            "size": 1,
            # Class: CfgVehicles|RHS_T50_base|Reflectors|Left|Attenuation [Indent level: 3],
            "attenuation": {
                "constant": 0,
                "linear": 0,
                "quadratic": 4,
                "start": 1,
                "hardlimitstart": 150,
                "hardlimitend": 300
            }
        },
        # Class: CfgVehicles|RHS_T50_base|Reflectors|Right [Indent level: 2],
        "right": {
            "position": "p svetlo",
            "direction": "konec p svetla",
            "hitpoint": "p svetlo",
            "selection": "p svetlo",
            "color": [7000,7500,10000,1],
            "ambient": [100,100,100],
            "innerangle": 20,
            "outerangle": 60,
            "conefadecoef": 10,
            "intensity": 50,
            "useflare": 1,
            "daylight": 0,
            "flaresize": 1,
            "size": 1,
            # Class: CfgVehicles|RHS_T50_base|Reflectors|Left|Attenuation [Indent level: 3],
            "attenuation": {
                "constant": 0,
                "linear": 0,
                "quadratic": 4,
                "start": 1,
                "hardlimitstart": 150,
                "hardlimitend": 300
            }
        }
    },
    "aggregatereflectors": [["Left"],["Right"]],
    # Class: CfgVehicles|RHS_T50_base|EventHandlers [Indent level: 1],
    "eventhandlers": {
        "hit": "",
        # Class: CfgVehicles|RHS_T50_base|EventHandlers|RHS_EventHandlers [Indent level: 2],
        "rhs_eventhandlers": {
            "hit": "_this call RHS_fnc_AI_eject",
            "init": "_this call rhs_fnc_air_init",
            "incomingmissile": "_this call rhs_fnc_rwr_air",
            "getout": "[_this select 0, _this select 2,'rhs_t50_canopy'] call rhs_fnc_K36D_seatEjection",
            "engine": "[_this select 0,_this select 1,10] call rhs_fnc_engineStartupDelay;_this call rhs_fnc_addParachutes;"
        },
        "init": "",
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');"
    },
    "irtarget": 1,
    "irtargetsize": 0.5,
    "visualtarget": 1,
    "visualtargetsize": 1,
    "radartarget": 1,
    "radartargetsize": 0.4,
    "lockdetectionsystem": 8,
    "incomingmissiledetectionsystem": 16,
    "receiveremotetargets": 1,
    "reportremotetargets": 1,
    "reportownposition": 1,
    # Class: CfgVehicles|RHS_T50_base|Components [Indent level: 1],
    "components": {
        # Class: CfgVehicles|RHS_T50_base|Components|TransportPylonsComponent [Indent level: 2]
        "transportpylonscomponent": {
            "uipicture": "rhsafrf|addons|rhs_air|t50|data|loadouts|RHS_T50_EDEN_CA.paa",
            # Class: CfgVehicles|RHS_T50_base|Components|TransportPylonsComponent|pylons [Indent level: 3],
            "pylons": {
                # Class: CfgVehicles|RHS_T50_base|Components|TransportPylonsComponent|pylons|pylonBayCenter1 [Indent level: 4]
                "pylonbaycenter1": {
                    "hardpoints": ["RHS_HP_R77","RHS_HP_R77M","RHS_HP_KAB250_INT","RHS_HP_Kh38_INT"],
                    "priority": 9,
                    "attachment": "rhs_mag_R77M",
                    "maxweight": 1200,
                    "uiposition": [0.27,0.3],
                    "bay": 1
                },
                # Class: CfgVehicles|RHS_T50_base|Components|TransportPylonsComponent|pylons|pylonBayCenter2 [Indent level: 4],
                "pylonbaycenter2": {
                    "uiposition": [0.27,0.25],
                    "mirroredmissilepos": 1,
                    "hardpoints": ["RHS_HP_R77","RHS_HP_R77M","RHS_HP_KAB250_INT","RHS_HP_Kh38_INT"],
                    "priority": 9,
                    "attachment": "rhs_mag_R77M",
                    "maxweight": 1200,
                    "bay": 1
                },
                # Class: CfgVehicles|RHS_T50_base|Components|TransportPylonsComponent|pylons|pylonBayCenter3 [Indent level: 4],
                "pylonbaycenter3": {
                    "priority": 7,
                    "uiposition": [0.45,0.25],
                    "bay": 2,
                    "hardpoints": ["RHS_HP_R77","RHS_HP_R77M","RHS_HP_KAB250_INT","RHS_HP_Kh38_INT"],
                    "attachment": "rhs_mag_R77M",
                    "maxweight": 1200
                },
                # Class: CfgVehicles|RHS_T50_base|Components|TransportPylonsComponent|pylons|pylonBayCenter4 [Indent level: 4],
                "pylonbaycenter4": {
                    "uiposition": [0.45,0.3],
                    "mirroredmissilepos": 3,
                    "priority": 7,
                    "bay": 2,
                    "hardpoints": ["RHS_HP_R77","RHS_HP_R77M","RHS_HP_KAB250_INT","RHS_HP_Kh38_INT"],
                    "attachment": "rhs_mag_R77M",
                    "maxweight": 1200
                },
                # Class: CfgVehicles|RHS_T50_base|Components|TransportPylonsComponent|pylons|pylonBayRight1 [Indent level: 4],
                "pylonbayright1": {
                    "hardpoints": ["RHS_HP_R74M2_int"],
                    "priority": 10,
                    "attachment": "rhs_mag_R74M2_int",
                    "maxweight": 1200,
                    "uiposition": [0.18,0.37],
                    "bay": 4
                },
                # Class: CfgVehicles|RHS_T50_base|Components|TransportPylonsComponent|pylons|pylonBayLeft1 [Indent level: 4],
                "pylonbayleft1": {
                    "uiposition": [0.18,0.18],
                    "mirroredmissilepos": 4,
                    "bay": 3,
                    "hardpoints": ["RHS_HP_R74M2_int"],
                    "priority": 10,
                    "attachment": "rhs_mag_R74M2_int",
                    "maxweight": 1200
                }
            },
            # Class: CfgVehicles|RHS_T50_base|Components|TransportPylonsComponent|Bays [Indent level: 3],
            "bays": {
                # Class: CfgVehicles|RHS_T50_base|Components|TransportPylonsComponent|Bays|BayCenter1 [Indent level: 4]
                "baycenter1": {
                    "bayopentime": 0.5,
                    "openbaywhenweaponselected": 0,
                    "autoclosewhenemptydelay": 4.5
                },
                # Class: CfgVehicles|RHS_T50_base|Components|TransportPylonsComponent|Bays|BayCenter2 [Indent level: 4],
                "baycenter2": {
                    "bayopentime": 0.5,
                    "openbaywhenweaponselected": 0,
                    "autoclosewhenemptydelay": 4.5
                },
                # Class: CfgVehicles|RHS_T50_base|Components|TransportPylonsComponent|Bays|BayLeft1 [Indent level: 4],
                "bayleft1": {
                    "bayopentime": 0.5,
                    "openbaywhenweaponselected": 0,
                    "autoclosewhenemptydelay": 2
                },
                # Class: CfgVehicles|RHS_T50_base|Components|TransportPylonsComponent|Bays|BayRight1 [Indent level: 4],
                "bayright1": {
                    "bayopentime": 0.5,
                    "openbaywhenweaponselected": 0,
                    "autoclosewhenemptydelay": 2
                }
            }
        },
        # Class: CfgVehicles|RHS_T50_base|Components|SensorsManagerComponent [Indent level: 2],
        "sensorsmanagercomponent": {
            # Class: CfgVehicles|RHS_T50_base|Components|SensorsManagerComponent|Components [Indent level: 3]
            "components": {
                # Class: CfgVehicles|RHS_T50_base|Components|SensorsManagerComponent|Components|IRSensorComponent [Indent level: 4]
                "irsensorcomponent": {
                    # Class: CfgVehicles|RHS_T50_base|Components|SensorsManagerComponent|Components|IRSensorComponent|AirTarget [Indent level: 5]
                    "airtarget": {
                        "minrange": 500,
                        "maxrange": 16000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": 1
                    },
                    # Class: CfgVehicles|RHS_T50_base|Components|SensorsManagerComponent|Components|IRSensorComponent|GroundTarget [Indent level: 5],
                    "groundtarget": {
                        "minrange": 500,
                        "maxrange": 12000,
                        "objectdistancelimitcoef": 1,
                        "viewdistancelimitcoef": 1
                    },
                    "anglerangehorizontal": 360,
                    "anglerangevertical": 120,
                    "maxtrackablespeed": 500,
                    "componenttype": "IRSensorComponent",
                    "typerecognitiondistance": 2000,
                    "maxfogseethrough": 0.995,
                    "color": [1,0,0,1],
                    "allowsmarking": 1,
                    "groundnoisedistancecoef": -1,
                    "maxgroundnoisedistance": -1,
                    "minspeedthreshold": 0,
                    "maxspeedthreshold": 0,
                    "animdirection": "",
                    "aimdown": 0,
                    "mintrackablespeed": -1e+010,
                    "mintrackableatl": -1e+010,
                    "maxtrackableatl": 1e+010
                },
                # Class: CfgVehicles|RHS_T50_base|Components|SensorsManagerComponent|Components|VisualSensorComponent [Indent level: 4],
                "visualsensorcomponent": {
                    # Class: CfgVehicles|RHS_T50_base|Components|SensorsManagerComponent|Components|VisualSensorComponent|AirTarget [Indent level: 5]
                    "airtarget": {
                        "minrange": 500,
                        "maxrange": 4000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": 1
                    },
                    # Class: CfgVehicles|RHS_T50_base|Components|SensorsManagerComponent|Components|VisualSensorComponent|GroundTarget [Indent level: 5],
                    "groundtarget": {
                        "minrange": 500,
                        "maxrange": 3000,
                        "objectdistancelimitcoef": 1,
                        "viewdistancelimitcoef": 1
                    },
                    "anglerangehorizontal": 26,
                    "anglerangevertical": 20,
                    "maxtrackablespeed": 100,
                    "aimdown": 1,
                    "componenttype": "VisualSensorComponent",
                    "nightrangecoef": 0,
                    "maxfogseethrough": 0.94,
                    "color": [1,1,0.5,0.8],
                    "typerecognitiondistance": 2000,
                    "allowsmarking": 1,
                    "groundnoisedistancecoef": -1,
                    "maxgroundnoisedistance": -1,
                    "minspeedthreshold": 0,
                    "maxspeedthreshold": 0,
                    "animdirection": "",
                    "mintrackablespeed": -1e+010,
                    "mintrackableatl": -1e+010,
                    "maxtrackableatl": 1e+010
                },
                # Class: CfgVehicles|RHS_T50_base|Components|SensorsManagerComponent|Components|PassiveRadarSensorComponent [Indent level: 4],
                "passiveradarsensorcomponent": {
                    "componenttype": "PassiveRadarSensorComponent",
                    # Class: SensorTemplatePassiveRadar|AirTarget [Indent level: 0],
                    "airtarget": {
                        "minrange": 16000,
                        "maxrange": 16000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    # Class: SensorTemplatePassiveRadar|GroundTarget [Indent level: 0],
                    "groundtarget": {
                        "minrange": 16000,
                        "maxrange": 16000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    "typerecognitiondistance": 12000,
                    "anglerangehorizontal": 360,
                    "anglerangevertical": 360,
                    "groundnoisedistancecoef": -1,
                    "maxgroundnoisedistance": -1,
                    "minspeedthreshold": 0,
                    "maxspeedthreshold": 0,
                    "animdirection": "",
                    "aimdown": 0,
                    "color": [0.5,1,0.5,0.5],
                    "mintrackablespeed": -1e+010,
                    "maxtrackablespeed": 1e+010,
                    "mintrackableatl": -1e+010,
                    "maxtrackableatl": 1e+010,
                    "allowsmarking": 0
                },
                # Class: CfgVehicles|RHS_T50_base|Components|SensorsManagerComponent|Components|ActiveRadarSensorComponent [Indent level: 4],
                "activeradarsensorcomponent": {
                    # Class: CfgVehicles|RHS_T50_base|Components|SensorsManagerComponent|Components|ActiveRadarSensorComponent|AirTarget [Indent level: 5]
                    "airtarget": {
                        "minrange": 32000,
                        "maxrange": 32000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    # Class: CfgVehicles|RHS_T50_base|Components|SensorsManagerComponent|Components|ActiveRadarSensorComponent|GroundTarget [Indent level: 5],
                    "groundtarget": {
                        "minrange": 10000,
                        "maxrange": 10000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    "typerecognitiondistance": 6000,
                    "anglerangehorizontal": 60,
                    "anglerangevertical": 60,
                    "groundnoisedistancecoef": 0.0004,
                    "componenttype": "ActiveRadarSensorComponent",
                    "maxgroundnoisedistance": 200,
                    "minspeedthreshold": 20.8333,
                    "maxspeedthreshold": 27.7778,
                    "color": [0,1,1,1],
                    "allowsmarking": 1,
                    "animdirection": "",
                    "aimdown": 0,
                    "mintrackablespeed": -1e+010,
                    "maxtrackablespeed": 1e+010,
                    "mintrackableatl": -1e+010,
                    "maxtrackableatl": 1e+010
                },
                # Class: CfgVehicles|RHS_T50_base|Components|SensorsManagerComponent|Components|LaserSensorComponent [Indent level: 4],
                "lasersensorcomponent": {
                    "componenttype": "LaserSensorComponent",
                    # Class: SensorTemplateLaser|AirTarget [Indent level: 0],
                    "airtarget": {
                        "minrange": 6000,
                        "maxrange": 6000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    # Class: SensorTemplateLaser|GroundTarget [Indent level: 0],
                    "groundtarget": {
                        "minrange": 6000,
                        "maxrange": 6000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    "anglerangehorizontal": 180,
                    "anglerangevertical": 180,
                    "typerecognitiondistance": 0,
                    "color": [1,1,1,0],
                    "allowsmarking": 1,
                    "groundnoisedistancecoef": -1,
                    "maxgroundnoisedistance": -1,
                    "minspeedthreshold": 0,
                    "maxspeedthreshold": 0,
                    "animdirection": "",
                    "aimdown": 0,
                    "mintrackablespeed": -1e+010,
                    "maxtrackablespeed": 1e+010,
                    "mintrackableatl": -1e+010,
                    "maxtrackableatl": 1e+010
                },
                # Class: CfgVehicles|RHS_T50_base|Components|SensorsManagerComponent|Components|NVSensorComponent [Indent level: 4],
                "nvsensorcomponent": {
                    "componenttype": "NVSensorComponent",
                    "color": [1,1,1,0],
                    # Class: SensorTemplateLaser|AirTarget [Indent level: 0],
                    "airtarget": {
                        "minrange": 6000,
                        "maxrange": 6000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    # Class: SensorTemplateLaser|GroundTarget [Indent level: 0],
                    "groundtarget": {
                        "minrange": 6000,
                        "maxrange": 6000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    "anglerangehorizontal": 180,
                    "anglerangevertical": 180,
                    "typerecognitiondistance": 0,
                    "allowsmarking": 1,
                    "groundnoisedistancecoef": -1,
                    "maxgroundnoisedistance": -1,
                    "minspeedthreshold": 0,
                    "maxspeedthreshold": 0,
                    "animdirection": "",
                    "aimdown": 0,
                    "mintrackablespeed": -1e+010,
                    "maxtrackablespeed": 1e+010,
                    "mintrackableatl": -1e+010,
                    "maxtrackableatl": 1e+010
                },
                # Class: CfgVehicles|RHS_T50_base|Components|SensorsManagerComponent|Components|DataLinkSensorComponent [Indent level: 4],
                "datalinksensorcomponent": {
                    "componenttype": "DataLinkSensorComponent",
                    "allowsmarking": 1,
                    "typerecognitiondistance": 0,
                    "color": [1,1,1,0],
                    # Class: SensorTemplatePassiveRadar|AirTarget [Indent level: 0],
                    "airtarget": {
                        "minrange": 16000,
                        "maxrange": 16000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    # Class: SensorTemplatePassiveRadar|GroundTarget [Indent level: 0],
                    "groundtarget": {
                        "minrange": 16000,
                        "maxrange": 16000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    "anglerangehorizontal": 360,
                    "anglerangevertical": 360,
                    "groundnoisedistancecoef": -1,
                    "maxgroundnoisedistance": -1,
                    "minspeedthreshold": 0,
                    "maxspeedthreshold": 0,
                    "animdirection": "",
                    "aimdown": 0,
                    "mintrackablespeed": -1e+010,
                    "maxtrackablespeed": 1e+010,
                    "mintrackableatl": -1e+010,
                    "maxtrackableatl": 1e+010
                }
            }
        },
        # Class: CfgVehicles|RHS_T50_base|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 2],
        "vehiclesystemsdisplaymanagercomponentleft": {
            # Class: CfgVehicles|RHS_T50_base|Components|VehicleSystemsDisplayManagerComponentLeft|Components [Indent level: 3]
            "components": {
                # Class: CfgVehicles|RHS_T50_base|Components|VehicleSystemsDisplayManagerComponentLeft|Components|EmptyDisplay [Indent level: 4]
                "emptydisplay": {
                    "componenttype": "EmptyDisplayComponent"
                },
                # Class: CfgVehicles|RHS_T50_base|Components|VehicleSystemsDisplayManagerComponentLeft|Components|MinimapDisplay [Indent level: 4],
                "minimapdisplay": {
                    "componenttype": "MinimapDisplayComponent",
                    "resource": "RscCustomInfoMiniMap"
                },
                # Class: CfgVehicles|RHS_T50_base|Components|VehicleSystemsDisplayManagerComponentLeft|Components|UAVDisplay [Indent level: 4],
                "uavdisplay": {
                    "componenttype": "UAVFeedDisplayComponent"
                },
                # Class: CfgVehicles|RHS_T50_base|Components|VehicleSystemsDisplayManagerComponentLeft|Components|SensorDisplay [Indent level: 4],
                "sensordisplay": {
                    "componenttype": "SensorsDisplayComponent",
                    "resource": "RscCustomInfoSensors",
                    "range": [16000,35000,3000,8000]
                }
            },
            "componenttype": "VehicleSystemsDisplayManager",
            "left": 1,
            "defaultdisplay": "EmptyDisplay",
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,	(safezoneX + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
        },
        # Class: CfgVehicles|RHS_T50_base|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 2],
        "vehiclesystemsdisplaymanagercomponentright": {
            "defaultdisplay": "SensorDisplay",
            # Class: CfgVehicles|RHS_T50_base|Components|VehicleSystemsDisplayManagerComponentRight|Components [Indent level: 3],
            "components": {
                # Class: CfgVehicles|RHS_T50_base|Components|VehicleSystemsDisplayManagerComponentRight|Components|EmptyDisplay [Indent level: 4]
                "emptydisplay": {
                    "componenttype": "EmptyDisplayComponent"
                },
                # Class: CfgVehicles|RHS_T50_base|Components|VehicleSystemsDisplayManagerComponentRight|Components|MinimapDisplay [Indent level: 4],
                "minimapdisplay": {
                    "componenttype": "MinimapDisplayComponent",
                    "resource": "RscCustomInfoMiniMap"
                },
                # Class: CfgVehicles|RHS_T50_base|Components|VehicleSystemsDisplayManagerComponentRight|Components|UAVDisplay [Indent level: 4],
                "uavdisplay": {
                    "componenttype": "UAVFeedDisplayComponent"
                },
                # Class: CfgVehicles|RHS_T50_base|Components|VehicleSystemsDisplayManagerComponentRight|Components|SensorDisplay [Indent level: 4],
                "sensordisplay": {
                    "componenttype": "SensorsDisplayComponent",
                    "resource": "RscCustomInfoSensors",
                    "range": [16000,35000,3000,8000]
                }
            },
            "componenttype": "VehicleSystemsDisplayManager",
            "right": 1,
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,	((safezoneX + safezoneW) - (		(10 * 			(			((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40)))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
        },
        # Class: CfgVehicles|Air|Components|TransportCountermeasuresComponent [Indent level: 2],
        "transportcountermeasurescomponent": {
        }
    },
    "author": "Bohemia Interactive",
    "_generalmacro": "Plane_Base_F",
    "gunnercansee": "1 + 2 + 4 + 8 + 32",
    "commandercansee": "1 + 2 + 4 + 8 + 32",
    "waterlineardampingcoefy": 0,
    "waterlineardampingcoefx": 5,
    "waterresistancecoef": 0.04,
    "ejectspeed": [0,60,0],
    "transportmaxweapons": 6,
    "transportmaxmagazines": 24,
    "transportmaxbackpacks": 6,
    "maximumload": 500,
    "supplyradius": 2,
    "memorypointsupply": "doplnovani",
    # Class: CfgVehicles|Plane_Base_F|TransportBackpacks [Indent level: 1],
    "transportbackpacks": {
    },
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
    "gearretracting": 1,
    "cabinopening": 1,
    "durationgetin": 0.99,
    "durationgetout": 0.99,
    "flaps": 1,
    "vtol": 0,
    "tailhook": 0,
    "lightongear": 1,
    "minfiretime": 60,
    "cost": 2e+006,
    "simulation": "airplanex",
    "mingunelev": 0,
    "maxgunelev": 0,
    "mingunturn": 0,
    "maxgunturn": 0,
    "gunaimdown": 0,
    "vtolyawinfluence": 2,
    "vtolpitchinfluence": 2,
    "vtolrollinfluence": 2,
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
    "memorypointldust": "levy prach",
    "memorypointrdust": "pravy prach",
    "selectionfireanim": "zasleh",
    "leftdusteffect": "LDustEffects",
    "rightdusteffect": "RDustEffects",
    "dusteffect": "HeliDust",
    "watereffect": "HeliWater",
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
    "mapsize": 17.78,
    "textsingular": "fast mover",
    "textplural": "fast movers",
    "namesound": "veh_air_plane_s",
    "type": 2,
    "memorypointgun": "kulomet",
    "fuelexplosionpower": 10,
    "crewcrashprotection": 0.15,
    "damageeffect": "AirDestructionEffects",
    "cargogetinaction": ["GetInHigh"],
    "cargogetoutaction": ["GetOutHigh"],
    "gunnergetinaction": "GetInHigh",
    "gunnergetoutaction": "GetOutHigh",
    "getinradius": 1.2,
    "accuracy": 0.02,
    "camouflage": 100,
    "audible": 60,
    # Class: CfgVehicles|Plane|CamShake [Indent level: 1],
    "camshake": {
        "power": 50,
        "frequency": 20,
        "distance": 50,
        "minspeed": 200
    },
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
    "fuelcapacity": 1000,
    "insidesoundcoef": 0.0316228,
    "outsidesoundfilter": 1,
    "occludesoundswhenin": 0.316228,
    "obstructsoundswhenin": 0.316228,
    "irscanrangemin": 2000,
    "irscanrangemax": 10000,
    "irscantoeyefactor": 2,
    "nightvision": 0,
    "cargocompartments": [0],
    "typicalcargo": ["Soldier"],
    "enablegps": 1,
    "weaponsgroup2": 4,
    "weaponsgroup3": "8 + 	16 + 	32",
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
    "radartype": 4,
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
    "memorypointsgetincargo": "pos cargo",
    "memorypointsgetincargodir": "pos cargo dir",
    "memorypointsgetincodriver": "pos codriver",
    "memorypointsgetincodriverdir": "pos codriver dir",
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
    "cargoproxyindexes": [],
    "driverdoor": "",
    "cargodoors": [],
    "hasterminal": 0,
    "getinoutonproxy": 0,
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
    "side": 4,
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
    "irscanground": 1,
    "lasertarget": 0,
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
    "soundlandcrashes": ["soundLandCrash",1],
    "emptysound": ["",0,1],
    "soundbushcrash": ["emptySound",0],
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
    "crew": "Civilian",
    "hiddenselectionsmaterials": [],
    "hiddenunderwaterselections": [],
    "shownunderwaterselections": [],
    "hiddenunderwaterselectionstextures": [],
    # Class: CfgVehicles|All|FxExplo [Indent level: 1],
    "fxexplo": {
        "access": 1
    },
    "cargocaneject": 1,
    "fireresistance": 10,
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
    "soundturnin": ["",0.000316228,1],
    "soundturnout": ["",0.000316228,1],
    "soundturnininternal": ["",0.000316228,1],
    "soundturnoutinternal": ["",0.000316228,1],
    "features": "",
    "insidedetectcoef": 0.05,
}