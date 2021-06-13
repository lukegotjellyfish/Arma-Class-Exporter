rhsusf_mkvsoc = {
    "dlc": "RHS_USAF",
    "editorpreview": "rhsusf|addons|rhsusf_editorPreviews|data|rhsusf_mkvsoc.paa",
    "scope": 2,
    "author": "Hatchet_AS",
    "displayname": "Mk.V SOC",
    "side": 1,
    "faction": "rhs_faction_socom",
    "vehicleclass": "Ship",
    "editorsubcategory": "EdSubcat_Boats",
    "model": "rhsusf|addons|rhsusf_markvsoc|mkvsoc.p3d",
    "picture": "A3|boat_f|Boat_Armed_01|data|ui|Boat_Armed_01_base.paa",
    "icon": "A3|boat_f|Boat_Armed_01|data|ui|map_boat_armed_01.paa",
    "namesound": "veh_ship_attackBoat_s",
    "textsingular": "attack boat",
    "textplural": "attack boats",
    "mapsize": 22,
    "canfloat": 0,
    "type": 1,
    "armor": 600,
    "canbeshot": 1,
    "enablemanualfire": 0,
    "extcameraposition": [0,2.5,-25],
    "fuelcapacity": 1000,
    "hideproxyincombat": 0,
    "precision": 80,
    "secondaryexplosion": -1,
    "sensitivity": 2,
    "memorypointcommondamage": "zamerny",
    "driveoncomponent": ["Slide"],
    "accuracy": 0.6,
    "camouflage": 3,
    "cost": 500000,
    "threat": [1,0.6,0.6],
    "htmin": 60,
    "htmax": 1800,
    "afmax": 100,
    "mfmax": 80,
    "mfact": 1,
    "tbody": 150,
    "crew": "rhsusf_socom_swcc_officer",
    "typicalcargo": ["rhsusf_socom_swcc_crewman","rhsusf_socom_swcc_crewman","rhsusf_socom_swcc_crewman","rhsusf_socom_swcc_crewman"],
    "crewcrashprotection": 0.1,
    "ejectdamagelimit": 0.9,
    "unloadincombat": 0,
    "hascommander": 1,
    "commanderaction": "RHS_MKVSOC_Commander",
    "commandercansee": "1+2+4+8+16",
    "hideweaponscommander": 1,
    "shownvgcommander": 1,
    "commanderopticsmodel": "A3|weapons_f|reticle|Optics_Commander_02_F",
    "hasdriver": 1,
    "driveraction": "RHS_MKVSOC_Driver",
    "driveriscommander": 0,
    "drivercansee": "1+2+8+16",
    "hideweaponsdriver": 1,
    "castdrivershadow": 1,
    "shownvgdriver": 1,
    "driverlefthandanimname": "drv_hand_l",
    "driverrighthandanimname": "drv_hand_r",
    "driverleftleganimname": "drv_leg_l",
    "driverrightleganimname": "drv_leg_r",
    "hasgunner": 1,
    "gunneriscommander": 0,
    "gunnercansee": "1+4+8+16",
    "hideweaponsgunner": 1,
    "shownvggunner": 1,
    "cargoaction": ["RHS_MKVSOC_Cargo01","RHS_MKVSOC_Cargo02","RHS_MKVSOC_Cargo03","RHS_MKVSOC_Cargo04","RHS_MKVSOC_Cargo05","RHS_MKVSOC_Cargo06","RHS_MKVSOC_Cargo07","RHS_MKVSOC_Cargo08","RHS_MKVSOC_Cargo09","RHS_MKVSOC_Cargo010","RHS_MKVSOC_Cargo011","RHS_MKVSOC_Cargo012","RHS_MKVSOC_Cargo013","RHS_MKVSOC_Cargo014","RHS_MKVSOC_Cargo015","RHS_MKVSOC_Cargo016","RHS_MKVSOC_Cargo017","RHS_MKVSOC_Cargo018","RHS_MKVSOC_Cargo019","RHS_MKVSOC_Cargo020","RHS_MKVSOC_Cargo021","RHS_MKVSOC_Cargo022","RHS_MKVSOC_Cargo023","RHS_MKVSOC_Cargo024","RHS_MKVSOC_Cargo025","RHS_MKVSOC_Cargo026"],
    "hideweaponscargo": 1,
    "castcargoshadow": 1,
    "shownvgcargo": [1],
    "supplyradius": 0,
    "transportammo": 0,
    "transportsoldier": 26,
    "transportvehiclescount": 0,
    "maximumload": 3000,
    "getinradius": 10,
    "getinaction": "GetInLow",
    "getoutaction": "GetOutLow",
    "cargogetinaction": ["GetInLow"],
    "cargogetoutaction": ["GetOutLow"],
    "memorypointsgetindriver": "driver_pos",
    "memorypointsgetindriverdir": "driver_dir",
    "memorypointsgetincargo": "cargo_pos",
    "memorypointsgetincargodir": "cargo_dir",
    "memorypointsgetingunner": "gunner_pos",
    "memorypointsgetingunnerdir": "gunner_dir",
    "memorypointsgetincommander": "comm_pos",
    "memorypointsgetincommanderdir": "comm_dir",
    "lockdetectionsystem": "8 + 4",
    "incomingmissiledetectionsystem": 16,
    "irtarget": 1,
    "irtargetsize": 1.7,
    "visualtarget": 1,
    "visualtargetsize": 1.8,
    "radartarget": 1,
    "radartargetsize": 1.5,
    "enablegps": 1,
    # Class: CfgVehicles|rhsusf_mkvsoc|Components [Indent level: 1],
    "components": {
        # Class: CfgVehicles|rhsusf_mkvsoc|Components|SensorsManagerComponent [Indent level: 2]
        "sensorsmanagercomponent": {
            # Class: CfgVehicles|rhsusf_mkvsoc|Components|SensorsManagerComponent|Components [Indent level: 3]
            "components": {
                # Class: CfgVehicles|rhsusf_mkvsoc|Components|SensorsManagerComponent|Components|ActiveRadarSensorComponent [Indent level: 4]
                "activeradarsensorcomponent": {
                    # Class: CfgVehicles|rhsusf_mkvsoc|Components|SensorsManagerComponent|Components|ActiveRadarSensorComponent|AirTarget [Indent level: 5]
                    "airtarget": {
                        "minrange": 11000,
                        "maxrange": 11000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    # Class: CfgVehicles|rhsusf_mkvsoc|Components|SensorsManagerComponent|Components|ActiveRadarSensorComponent|GroundTarget [Indent level: 5],
                    "groundtarget": {
                        "minrange": 11000,
                        "maxrange": 11000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    "groundnoisedistancecoef": -1,
                    "maxgroundnoisedistance": -1,
                    "anglerangehorizontal": 360,
                    "anglerangevertical": 20,
                    "typerecognitiondistance": 4000,
                    "maxfogseethrough": 1,
                    "maxtrackableatl": 100,
                    "maxtrackablespeed": 75,
                    "componenttype": "ActiveRadarSensorComponent",
                    "minspeedthreshold": 20.8333,
                    "maxspeedthreshold": 27.7778,
                    "color": [0,1,1,1],
                    "allowsmarking": 1,
                    "animdirection": "",
                    "aimdown": 0,
                    "mintrackablespeed": -1e+010,
                    "mintrackableatl": -1e+010
                }
            }
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 2],
        "vehiclesystemsdisplaymanagercomponentleft": {
            # Class: CfgVehicles|rhsusf_mkvsoc|Components|VehicleSystemsDisplayManagerComponentLeft|Components [Indent level: 3]
            "components": {
                # Class: CfgVehicles|rhsusf_mkvsoc|Components|VehicleSystemsDisplayManagerComponentLeft|Components|EmptyDisplay [Indent level: 4]
                "emptydisplay": {
                    "componenttype": "EmptyDisplayComponent"
                },
                # Class: CfgVehicles|rhsusf_mkvsoc|Components|VehicleSystemsDisplayManagerComponentLeft|Components|MinimapDisplay [Indent level: 4],
                "minimapdisplay": {
                    "componenttype": "MinimapDisplayComponent",
                    "resource": "RscCustomInfoMiniMap"
                },
                # Class: CfgVehicles|rhsusf_mkvsoc|Components|VehicleSystemsDisplayManagerComponentLeft|Components|CrewDisplay [Indent level: 4],
                "crewdisplay": {
                    "componenttype": "CrewDisplayComponent",
                    "resource": "RscCustomInfoCrew"
                },
                # Class: CfgVehicles|rhsusf_mkvsoc|Components|VehicleSystemsDisplayManagerComponentLeft|Components|SensorDisplay [Indent level: 4],
                "sensordisplay": {
                    "componenttype": "SensorsDisplayComponent",
                    "range": [8000,16000,4000],
                    "resource": "RscCustomInfoSensors"
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
        # Class: CfgVehicles|rhsusf_mkvsoc|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 2],
        "vehiclesystemsdisplaymanagercomponentright": {
            "defaultdisplay": "SensorDisplay",
            # Class: CfgVehicles|rhsusf_mkvsoc|Components|VehicleSystemsDisplayManagerComponentRight|Components [Indent level: 3],
            "components": {
                # Class: CfgVehicles|rhsusf_mkvsoc|Components|VehicleSystemsDisplayManagerComponentRight|Components|EmptyDisplay [Indent level: 4]
                "emptydisplay": {
                    "componenttype": "EmptyDisplayComponent"
                },
                # Class: CfgVehicles|rhsusf_mkvsoc|Components|VehicleSystemsDisplayManagerComponentRight|Components|MinimapDisplay [Indent level: 4],
                "minimapdisplay": {
                    "componenttype": "MinimapDisplayComponent",
                    "resource": "RscCustomInfoMiniMap"
                },
                # Class: CfgVehicles|rhsusf_mkvsoc|Components|VehicleSystemsDisplayManagerComponentRight|Components|CrewDisplay [Indent level: 4],
                "crewdisplay": {
                    "componenttype": "CrewDisplayComponent",
                    "resource": "RscCustomInfoCrew"
                },
                # Class: CfgVehicles|rhsusf_mkvsoc|Components|VehicleSystemsDisplayManagerComponentRight|Components|SensorDisplay [Indent level: 4],
                "sensordisplay": {
                    "componenttype": "SensorsDisplayComponent",
                    "range": [8000,16000,4000],
                    "resource": "RscCustomInfoSensors"
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
        },
        # Class: CfgVehicles|Ship|Components|TransportCountermeasuresComponent [Indent level: 2],
        "transportcountermeasurescomponent": {
        }
    },
    "smokelaunchergrenadecount": 8,
    "smokelaunchervelocity": 75,
    "smokelauncheronturret": 0,
    "smokelauncherangle": 360,
    "weapons": [],
    "magazines": [],
    "memorypointcm": ["cm_port","cm_stbd"],
    "memorypointcmdir": ["cm_port_dir","cm_stbd_dir"],
    "predictturnsimul": 0.95,
    "predictturnplan": 0.75,
    "steeraheadsimul": 0.95,
    "steeraheadplan": 0.75,
    "brakedistance": 5,
    "simulation": "shipx",
    "waterleakiness": 95.5,
    "waterlineardampingcoefy": 1.65,
    "waterlineardampingcoefx": 1.15,
    "waterangulardampingcoef": 1.125,
    "turncoef": 0.5,
    "waterresistancecoef": 0.0024,
    "rudderforcecoef": 0.825,
    "rudderforcecoefatmaxspeed": 0.155,
    "torquecurve": [[0.3,0.850031],[0.4,0.950031],[0.5,1],[0.6,0.950031],[0.7,0.850031],[0.8,0.650031],[0.9,0.550031],[1,0.410018]],
    "maxomega": 209.44,
    "enginepower": 3908,
    "peaktorque": 16270,
    "idlerpm": 600,
    "redrpm": 2000,
    "maxspeed": 115,
    "minspeed": -25,
    "engineshifty": 1.125,
    "thrustdelay": 1.175,
    "overspeedbrakecoef": 0.01,
    "slowspeedforwardcoef": 0.275,
    "normalspeedforwardcoef": 0.675,
    # Class: CfgVehicles|rhsusf_mkvsoc|complexGearbox [Indent level: 1],
    "complexgearbox": {
        "gearboxratios": ["R1",-7.625,"N",0,"D1",1.97],
        "transmissionratios": ["High",1],
        "gearboxmode": "auto",
        "moveoffgear": 1,
        "drivestring": "D",
        "neutralstring": "N",
        "reversestring": "R"
    },
    "leftfastwatereffect": "LFastWaterEffects",
    "rightfastwatereffect": "RFastWaterEffects",
    "watereffectspeed": 10,
    "engineeffectspeed": 1,
    "waterfasteffectspeed": 1,
    "memorypointexhaust": "eng_1_exh",
    "memorypointexhaustdir": "eng_1_exh_dir",
    "memorypointsleftwatereffect": "waterEffectLeft",
    "memorypointsrightwatereffect": "waterEffectRight",
    # Class: CfgVehicles|rhsusf_mkvsoc|AnimationSources [Indent level: 1],
    "animationsources": {
        # Class: CfgVehicles|rhsusf_mkvsoc|AnimationSources|mL_pos_port_source [Indent level: 2]
        "ml_pos_port_source": {
            "source": "markerLight",
            "markerlight": "mL_pos_port"
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|AnimationSources|mL_pos_stbd_source [Indent level: 2],
        "ml_pos_stbd_source": {
            "source": "markerLight",
            "markerlight": "mL_pos_stbd"
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|AnimationSources|mL_pos_aft_source [Indent level: 2],
        "ml_pos_aft_source": {
            "source": "markerLight",
            "markerlight": "mL_pos_aft"
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|AnimationSources|rL_nav_source [Indent level: 2],
        "rl_nav_source": {
            "source": "user",
            "animperiod": 1,
            "initphase": 1
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|AnimationSources|rL_remSpot_source [Indent level: 2],
        "rl_remspot_source": {
            "source": "user",
            "animperiod": 1,
            "initphase": 1
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|AnimationSources|c_displays_off_source [Indent level: 2],
        "c_displays_off_source": {
            "source": "user",
            "animperiod": 0.001,
            "initphase": 0
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|AnimationSources|c_eng_ctrl_off_source [Indent level: 2],
        "c_eng_ctrl_off_source": {
            "source": "user",
            "animperiod": 0.001,
            "initphase": 0
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|AnimationSources|c_instr_off_source [Indent level: 2],
        "c_instr_off_source": {
            "source": "user",
            "animperiod": 0.001,
            "initphase": 0
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|AnimationSources|rL_opR_source [Indent level: 2],
        "rl_opr_source": {
            "source": "user",
            "animperiod": 1,
            "initphase": 1
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|AnimationSources|rL_opT_source [Indent level: 2],
        "rl_opt_source": {
            "source": "user",
            "animperiod": 1,
            "initphase": 1
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|AnimationSources|Beacons [Indent level: 2],
        "beacons": {
            "source": "user",
            "animperiod": 1,
            "initphase": 1
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|AnimationSources|m2_p_muzzle_source [Indent level: 2],
        "m2_p_muzzle_source": {
            "source": "reload",
            "weapon": "RHS_MKV_M2_p"
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|AnimationSources|m2_p_reloadMagazine [Indent level: 2],
        "m2_p_reloadmagazine": {
            "source": "reloadMagazine",
            "weapon": "RHS_MKV_M2_p"
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|AnimationSources|m2_p_muzzle_source_rot [Indent level: 2],
        "m2_p_muzzle_source_rot": {
            "source": "ammorandom",
            "weapon": "RHS_MKV_M2_p"
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|AnimationSources|m2_s_muzzle_source [Indent level: 2],
        "m2_s_muzzle_source": {
            "source": "reload",
            "weapon": "RHS_MKV_M2_s"
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|AnimationSources|m2_s_reloadMagazine [Indent level: 2],
        "m2_s_reloadmagazine": {
            "source": "reloadMagazine",
            "weapon": "RHS_MKV_M2_s"
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|AnimationSources|m2_s_muzzle_source_rot [Indent level: 2],
        "m2_s_muzzle_source_rot": {
            "source": "ammorandom",
            "weapon": "RHS_MKV_M2_s"
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|AnimationSources|m134_p_muzzle_source [Indent level: 2],
        "m134_p_muzzle_source": {
            "source": "reload",
            "weapon": "RHS_MKV_M134"
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|AnimationSources|m134_p_muzzle_source_rot [Indent level: 2],
        "m134_p_muzzle_source_rot": {
            "source": "ammorandom",
            "weapon": "RHS_MKV_M134"
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|AnimationSources|m134_p_revolving_source [Indent level: 2],
        "m134_p_revolving_source": {
            "source": "revolving",
            "weapon": "RHS_MKV_M134"
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|AnimationSources|mk19_s_muzzle_source [Indent level: 2],
        "mk19_s_muzzle_source": {
            "source": "reload",
            "weapon": "RHS_MKV_MK19"
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|AnimationSources|mk19_s_muzzle_source_rot [Indent level: 2],
        "mk19_s_muzzle_source_rot": {
            "source": "ammorandom",
            "weapon": "RHS_MKV_MK19"
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|AnimationSources|attach_load_1 [Indent level: 2],
        "attach_load_1": {
            "source": "user",
            "animperiod": 6,
            "initphase": 0
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|AnimationSources|attach_load_2 [Indent level: 2],
        "attach_load_2": {
            "source": "user",
            "animperiod": 6,
            "initphase": 0
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|AnimationSources|attach_load_3 [Indent level: 2],
        "attach_load_3": {
            "animperiod": 3,
            "source": "user",
            "initphase": 0
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|AnimationSources|attach_load_4 [Indent level: 2],
        "attach_load_4": {
            "source": "user",
            "animperiod": 6,
            "initphase": 0
        }
    },
    # Class: CfgVehicles|rhsusf_mkvsoc|Damage [Indent level: 1],
    "damage": {
        "tex": [],
        "mat": ["rhsusf|addons|rhsusf_markvsoc|data|mkvsoc_hull.rvmat","rhsusf|addons|rhsusf_markvsoc|data|mkvsoc_hull_d.rvmat","rhsusf|addons|rhsusf_markvsoc|data|rhs_destr_mkvsoc.rvmat","rhsusf|addons|rhsusf_markvsoc|data|RHIB.rvmat","rhsusf|addons|rhsusf_markvsoc|data|RHIB_d.rvmat","rhsusf|addons|rhsusf_markvsoc|data|rhs_destr_mkvsoc.rvmat"]
    },
    # Class: CfgVehicles|rhsusf_mkvsoc|EventHandlers [Indent level: 1],
    "eventhandlers": {
        # Class: CfgVehicles|rhsusf_mkvsoc|EventHandlers|rhs_markvsoc_eh [Indent level: 2]
        "rhs_markvsoc_eh": {
        },
        "init": "",
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');"
    },
    # Class: CfgVehicles|rhsusf_mkvsoc|Exhausts [Indent level: 1],
    "exhausts": {
        # Class: CfgVehicles|rhsusf_mkvsoc|Exhausts|Exhaust1 [Indent level: 2]
        "exhaust1": {
            "position": "eng_1_exh",
            "direction": "eng_1_exh_dir",
            "effect": "ExhaustsEffectBig"
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|Exhausts|Exhaust2 [Indent level: 2],
        "exhaust2": {
            "position": "eng_2_exh",
            "direction": "eng_2_exh_dir",
            "effect": "ExhaustsEffectBig"
        }
    },
    # Class: CfgVehicles|rhsusf_mkvsoc|Library [Indent level: 1],
    "library": {
        "libtextdesc": "MKVLIB"
    },
    # Class: CfgVehicles|rhsusf_mkvsoc|MarkerLights [Indent level: 1],
    "markerlights": {
        # Class: CfgVehicles|rhsusf_mkvsoc|MarkerLights|mL_pos_port [Indent level: 2]
        "ml_pos_port": {
            "color": [0.8,0,0],
            "ambient": [0.08,0,0],
            "intensity": 100,
            "name": "mL_pos_port",
            "drawlight": 1,
            "drawlightsize": 1.2,
            "drawlightcentersize": 0.1,
            "activelight": 0,
            "blinking": 0,
            "daylight": 0,
            "useflare": 0
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|MarkerLights|mL_pos_stbd [Indent level: 2],
        "ml_pos_stbd": {
            "color": [0,0.8,0],
            "ambient": [0,0.08,0],
            "name": "mL_pos_stbd",
            "intensity": 100,
            "drawlight": 1,
            "drawlightsize": 1.2,
            "drawlightcentersize": 0.1,
            "activelight": 0,
            "blinking": 0,
            "daylight": 0,
            "useflare": 0
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|MarkerLights|mL_pos_aft [Indent level: 2],
        "ml_pos_aft": {
            "color": [0.8,0.8,0.8],
            "ambient": [0.08,0.08,0.08],
            "intensity": 100,
            "name": "mL_pos_aft",
            "drawlight": 1,
            "drawlightsize": 1.2,
            "drawlightcentersize": 0.1,
            "activelight": 0,
            "blinking": 0,
            "daylight": 0,
            "useflare": 0
        }
    },
    # Class: CfgVehicles|rhsusf_mkvsoc|Reflectors [Indent level: 1],
    "reflectors": {
        # Class: CfgVehicles|rhsusf_mkvsoc|Reflectors|rL_nav [Indent level: 2]
        "rl_nav": {
            "color": [1900,1800,1700],
            "ambient": [5,5,5],
            "position": "axis_rL_nav",
            "direction": "axis_rL_nav_dir",
            "hitpoint": "rL_nav_illum",
            "selection": "rL_nav_illum",
            "size": 5,
            "innerangle": 10,
            "outerangle": 25,
            "conefadecoef": 3,
            "intensity": 1500,
            "useflare": 1,
            "daylight": 0,
            "flaresize": 1,
            "flaremaxdistance": 350,
            # Class: CfgVehicles|rhsusf_mkvsoc|Reflectors|rL_nav|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0.1,
                "quadratic": 0,
                "hardlimitstart": 150,
                "hardlimitend": 300
            }
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|Reflectors|rL_rem_spot [Indent level: 2],
        "rl_rem_spot": {
            "color": [1900,1800,1700],
            "ambient": [10,9,8],
            "position": "axis_remSpot_pos",
            "direction": "axis_remSpot_dir",
            "hitpoint": "rL_remSpot_illum",
            "selection": "rL_remSpot_illum",
            "size": 5,
            "innerangle": 2,
            "outerangle": 6,
            "conefadecoef": 1,
            "intensity": 5000,
            "useflare": 1,
            "daylight": 0,
            "flaresize": 1.5,
            "flaremaxdistance": 750,
            # Class: CfgVehicles|rhsusf_mkvsoc|Reflectors|rL_rem_spot|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0.1,
                "quadratic": 0,
                "hardlimitstart": 500,
                "hardlimitend": 750
            }
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|Reflectors|rL_opR_boom [Indent level: 2],
        "rl_opr_boom": {
            "color": [15000,100,100],
            "ambient": [15,1,1],
            "intensity": 3,
            "size": 1,
            "innerangle": 45,
            "outerangle": 120,
            "conefadecoef": 5,
            "position": "axis_rL_opR_boom_pos",
            "direction": "axis_rL_opR_boom_dir",
            "hitpoint": "rL_op_red_illum",
            "selection": "rL_op_red_illum",
            "useflare": 0,
            "flaresize": 0.65,
            "flaremaxdistance": 20,
            "daylight": 0,
            "blinking": 0,
            # Class: CfgVehicles|rhsusf_mkvsoc|Reflectors|rL_opR_boom|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 2,
                "constant": 0,
                "linear": 1,
                "quadratic": 50,
                "hardlimitstart": 3,
                "hardlimitend": 75
            }
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|Reflectors|rL_opR_cabin [Indent level: 2],
        "rl_opr_cabin": {
            "color": [1800,0,0],
            "ambient": [5,0,0],
            "intensity": 11,
            "size": 1,
            "innerangle": 90,
            "outerangle": 165,
            "conefadecoef": 1,
            "position": "axis_rL_opR_cabin_pos",
            "direction": "axis_rL_opR_cabin_dir",
            "hitpoint": "rL_op_red_illum",
            "selection": "rL_op_red_illum",
            "useflare": 1,
            "flaresize": 1,
            "flaremaxdistance": 5,
            "daylight": 0,
            "blinking": 0,
            # Class: CfgVehicles|rhsusf_mkvsoc|Reflectors|rL_opR_cabin|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 50,
                "hardlimitstart": 0,
                "hardlimitend": 3
            }
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|Reflectors|rL_opR_cabin2 [Indent level: 2],
        "rl_opr_cabin2": {
            "position": "axis_rL_opR_cabin2_pos",
            "direction": "axis_rL_opR_cabin2_dir",
            "hitpoint": "rL_op_red_illum",
            "selection": "rL_op_red_illum",
            "color": [1800,0,0],
            "ambient": [5,0,0],
            "intensity": 11,
            "size": 1,
            "innerangle": 90,
            "outerangle": 165,
            "conefadecoef": 1,
            "useflare": 1,
            "flaresize": 1,
            "flaremaxdistance": 5,
            "daylight": 0,
            "blinking": 0,
            # Class: CfgVehicles|rhsusf_mkvsoc|Reflectors|rL_opR_cabin|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 50,
                "hardlimitstart": 0,
                "hardlimitend": 3
            }
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|Reflectors|rL_opT_boom [Indent level: 2],
        "rl_opt_boom": {
            "color": [1875,2475,2175],
            "ambient": [5,5,5],
            "position": "axis_rL_opT_boom_pos",
            "direction": "axis_rL_opT_boom_dir",
            "hitpoint": "rL_op_teal_illum",
            "selection": "rL_op_teal_illum",
            "size": 5,
            "innerangle": 35,
            "outerangle": 90,
            "conefadecoef": 2,
            "intensity": 2,
            "useflare": 1,
            "daylight": 0,
            "flaresize": 1,
            "flaremaxdistance": 250,
            # Class: CfgVehicles|rhsusf_mkvsoc|Reflectors|rL_opT_boom|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0.1,
                "quadratic": 0,
                "hardlimitstart": 25,
                "hardlimitend": 150
            }
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|Reflectors|rL_opT_cabin [Indent level: 2],
        "rl_opt_cabin": {
            "color": [1875,2475,2175],
            "ambient": [5,5,5],
            "intensity": 1,
            "size": 1,
            "innerangle": 90,
            "outerangle": 165,
            "conefadecoef": 1,
            "position": "axis_rL_opT_cabin_pos",
            "direction": "axis_rL_opT_cabin_dir",
            "hitpoint": "rL_op_teal_illum",
            "selection": "rL_op_teal_illum",
            "useflare": 1,
            "flaresize": 1,
            "flaremaxdistance": 5,
            "daylight": 0,
            "blinking": 0,
            # Class: CfgVehicles|rhsusf_mkvsoc|Reflectors|rL_opT_cabin|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 50,
                "hardlimitstart": 0,
                "hardlimitend": 3
            }
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|Reflectors|rL_opT_cabin2 [Indent level: 2],
        "rl_opt_cabin2": {
            "position": "axis_rL_opT_cabin2_pos",
            "direction": "axis_rL_opT_cabin2_dir",
            "hitpoint": "rL_op_teal_illum",
            "selection": "rL_op_teal_illum",
            "color": [1875,2475,2175],
            "ambient": [5,5,5],
            "intensity": 1,
            "size": 1,
            "innerangle": 90,
            "outerangle": 165,
            "conefadecoef": 1,
            "useflare": 1,
            "flaresize": 1,
            "flaremaxdistance": 5,
            "daylight": 0,
            "blinking": 0,
            # Class: CfgVehicles|rhsusf_mkvsoc|Reflectors|rL_opT_cabin|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 50,
                "hardlimitstart": 0,
                "hardlimitend": 3
            }
        }
    },
    "aggregatereflectors": [],
    # Class: CfgVehicles|rhsusf_mkvsoc|RenderTargets [Indent level: 1],
    "rendertargets": {
        # Class: CfgVehicles|rhsusf_mkvsoc|RenderTargets|display_cam_cmdr [Indent level: 2]
        "display_cam_cmdr": {
            "rendertarget": "rendertarget0",
            # Class: CfgVehicles|rhsusf_mkvsoc|RenderTargets|display_cam_cmdr|CameraView1 [Indent level: 3],
            "cameraview1": {
                "pointposition": "axis_camera_b_pos",
                "pointdirection": "axis_camera_b_dir",
                "rendervisionmode": 2,
                "renderquality": 2,
                "fov": 0.7
            },
            "bboxes": ["PIP_1_TL","PIP_1_TR","PIP_1_BL","PIP_1_BR"]
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|RenderTargets|cam_drv_bow [Indent level: 2],
        "cam_drv_bow": {
            "rendertarget": "rendertarget1",
            # Class: CfgVehicles|rhsusf_mkvsoc|RenderTargets|cam_drv_bow|CameraView1 [Indent level: 3],
            "cameraview1": {
                "pointposition": "axis_cam_drv_bow_pos",
                "pointdirection": "axis_cam_drv_bow_dir",
                "rendervisionmode": 1,
                "fov": 0.6
            },
            "bboxes": ["PIP_2_TL","PIP_2_TR","PIP_2_BL","PIP_2_BR"]
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|RenderTargets|cam_drv_deck [Indent level: 2],
        "cam_drv_deck": {
            "rendertarget": "rendertarget2",
            # Class: CfgVehicles|rhsusf_mkvsoc|RenderTargets|cam_drv_deck|CameraView1 [Indent level: 3],
            "cameraview1": {
                "pointposition": "axis_cam_drv_deck_pos",
                "pointdirection": "axis_cam_drv_deck_dir",
                "rendervisionmode": 0,
                "fov": 0.7
            },
            "bboxes": ["PIP_3_TL","PIP_3_TR","PIP_3_BL","PIP_3_BR"]
        }
    },
    "attenuationeffecttype": "CarAttenuation",
    "audible": 4,
    "insidesoundcoef": 0.75,
    "occludesoundswhenin": 0.316228,
    "obstructsoundswhenin": 0.562341,
    "buildcrash0": ["A3|sounds_f|Vehicles|soft|noises|crash_building_01",1.77828,1,200],
    "buildcrash1": ["A3|sounds_f|Vehicles|soft|noises|crash_building_02",1.77828,1,200],
    "buildcrash2": ["A3|sounds_f|Vehicles|soft|noises|crash_building_03",1.77828,1,200],
    "buildcrash3": ["A3|sounds_f|Vehicles|soft|noises|crash_building_04",1.77828,1,200],
    "soundbuildingcrash": ["buildCrash0",0.25,"buildCrash1",0.25,"buildCrash2",0.25,"buildCrash3",0.25],
    "woodcrash0": ["A3|sounds_f|Vehicles|soft|noises|crash_mix_wood_01",1.77828,1,200],
    "woodcrash1": ["A3|sounds_f|Vehicles|soft|noises|crash_mix_wood_02",1.77828,1,200],
    "woodcrash2": ["A3|sounds_f|Vehicles|soft|noises|crash_mix_wood_03",1.77828,1,200],
    "woodcrash3": ["A3|sounds_f|Vehicles|soft|noises|crash_mix_wood_04",1.77828,1,200],
    "woodcrash4": ["A3|sounds_f|Vehicles|soft|noises|crash_mix_wood_05",1.77828,1,200],
    "woodcrash5": ["A3|sounds_f|Vehicles|soft|noises|crash_mix_wood_06",1.77828,1,200],
    "soundwoodcrash": ["woodCrash0",0.166,"woodCrash1",0.166,"woodCrash2",0.166,"woodCrash3",0.166,"woodCrash4",0.166,"woodCrash5",0.166],
    "armorcrash0": ["A3|sounds_f|Vehicles|soft|noises|crash_vehicle_01",1.77828,1,200],
    "armorcrash1": ["A3|sounds_f|Vehicles|soft|noises|crash_vehicle_02",1.77828,1,200],
    "armorcrash2": ["A3|sounds_f|Vehicles|soft|noises|crash_vehicle_03",1.77828,1,200],
    "armorcrash3": ["A3|sounds_f|Vehicles|soft|noises|crash_vehicle_04",1.77828,1,200],
    "soundarmorcrash": ["ArmorCrash0",0.25,"ArmorCrash1",0.25,"ArmorCrash2",0.25,"ArmorCrash3",0.25],
    # Class: CfgVehicles|rhsusf_mkvsoc|Sounds [Indent level: 1],
    "sounds": {
        # Class: CfgVehicles|rhsusf_mkvsoc|Sounds|IdleOut [Indent level: 2]
        "idleout": {
            "sound": ["rhsusf|addons|rhsusf_markvsoc|data|Sound|idle_ext",1,1,250],
            "frequency": "0.95 + ((rpm/ 2000) factor[(0/ 2000),(500/ 2000)])*0.5",
            "volume": "engineOn*(((rpm/ 2000) factor[(0/ 2000),(30/ 2000)]) * ((rpm/ 2000) factor[(500/ 2000),(300/ 2000)]))"
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|Sounds|Engine [Indent level: 2],
        "engine": {
            "sound": ["rhsusf|addons|rhsusf_markvsoc|data|Sound|engine_ext",1,1,350],
            "frequency": "0.5 + ((rpm/ 2000) factor[(150/ 2000),(2000/ 2000)])*0.8",
            "volume": "engineOn*((rpm/ 2000) factor[(300/ 600),(2000/ 2000)])"
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|Sounds|EngineMidOut [Indent level: 2],
        "enginemidout": {
            "sound": ["rhsusf|addons|rhsusf_markvsoc|data|Sound|distance",1,1,800],
            "frequency": "0.5 + ((rpm/ 2000) factor[(150/ 2000),(2000/ 2000)])*0.8",
            "volume": "engineOn*((rpm/ 2000) factor[(300/ 600),(2000/ 2000)])"
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|Sounds|EngineMaxOut [Indent level: 2],
        "enginemaxout": {
            "sound": ["rhsusf|addons|rhsusf_markvsoc|data|Sound|engine_rev",0.75,1,400],
            "frequency": "0.5 + ((rpm/ 2000) factor[(150/ 2000),(2000/ 2000)])*0.8",
            "volume": "engineOn*((rpm/ 2000) factor[(1300/ 2000),(2000/ 2000)])"
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|Sounds|WaternoiseOutW0 [Indent level: 2],
        "waternoiseoutw0": {
            "sound": ["A3|Sounds_F|vehicles|boat|SFX|voda-o-bok-lodi-0-speed1",0.707946,1,150],
            "frequency": "1",
            "volume": "(speed factor[4, 1]) * water"
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|Sounds|WaternoiseOutW1 [Indent level: 2],
        "waternoiseoutw1": {
            "sound": ["A3|Sounds_F|vehicles|boat|SFX|voda-o-bok-lodi-20-speed",0.794328,1,250],
            "frequency": "1",
            "volume": "((speed factor[2, 6]) min (speed factor[6, 4]))"
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|Sounds|WaternoiseOutW2 [Indent level: 2],
        "waternoiseoutw2": {
            "sound": ["A3|Sounds_F|vehicles|boat|SFX|voda-o-bok-lodi-50-speed",1,1,350],
            "frequency": "1",
            "volume": "(speed factor[3, 9])"
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|Sounds|WaternoiseOutW3 [Indent level: 2],
        "waternoiseoutw3": {
            "sound": ["A3|Sounds_F|vehicles|boat|SFX|voda-o-bok-lodi-0-speed1",0.707946,1,150],
            "frequency": "1",
            "volume": "(speed factor[-4, -1]) * water"
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|Sounds|WaternoiseOutW4 [Indent level: 2],
        "waternoiseoutw4": {
            "sound": ["A3|Sounds_F|vehicles|boat|SFX|voda-o-bok-lodi-20-speed",0.794328,0.9,250],
            "frequency": "1",
            "volume": "((speed factor[-2, -6]) min (speed factor[-6, -4]))"
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|Sounds|WaternoiseOutW5 [Indent level: 2],
        "waternoiseoutw5": {
            "sound": ["A3|Sounds_F|vehicles|boat|SFX|voda-o-bok-lodi-50-speed",1,0.9,350],
            "frequency": "1",
            "volume": "(speed factor[-3, -9])"
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|Sounds|scrubLandExt [Indent level: 2],
        "scrublandext": {
            "sound": ["A3|Sounds_F|vehicles|boat|noises|boat_land_on_shallow",1.77828,0.9,100],
            "frequency": 1,
            "volume": "(scrubLand factor[0.01, 0.20])"
        }
    },
    # Class: CfgVehicles|rhsusf_mkvsoc|SoundEvents [Indent level: 1],
    "soundevents": {
    },
    # Class: CfgVehicles|rhsusf_mkvsoc|SpeechVariants [Indent level: 1],
    "speechvariants": {
        # Class: CfgVehicles|rhsusf_mkvsoc|SpeechVariants|Default [Indent level: 2]
        "default": {
            "speechsingular": ["veh_ship_attackBoat_s"],
            "speechplural": ["veh_ship_attackBoat_p"]
        }
    },
    # Class: CfgVehicles|rhsusf_mkvsoc|TransportItems [Indent level: 1],
    "transportitems": {
    },
    # Class: CfgVehicles|rhsusf_mkvsoc|Turrets [Indent level: 1],
    "turrets": {
        # Class: CfgVehicles|rhsusf_mkvsoc|Turrets|MainTurret [Indent level: 2]
        "mainturret": {
            "gunnertype": "rhsusf_socom_swcc_crewman",
            "stabilizedinaxes": 3,
            "proxytype": "CPGunner",
            "proxyindex": 1,
            "gunnercompartments": "Compartment2",
            "body": "mainTurret",
            "gun": "mainGun",
            "animationsourcebody": "mainTurret",
            "animationsourcegun": "mainGun",
            "gunneraction": "RHS_MKVSOC_Gunner",
            "gunnergetinaction": "",
            "gunnergetoutaction": "",
            "gunnerreversedgetout": 0,
            "memorypointsgetingunner": "gunner_pos_s_m2",
            "memorypointsgetingunnerdir": "gunner_dir_s_m2",
            "ejectdeadgunner": 1,
            "outgunnermayfire": 1,
            "ingunnermayfire": 1,
            "soundservo": ["A3|sounds_f|dummysound",0.00562341,1],
            "gunbeg": "m2_p_beginBarrel",
            "gunend": "m2_p_endBarrel",
            "weapons": ["RHS_MKV_M2_p"],
            "magazines": ["rhs_mag_100rnd_127x99_mag_Tracer_Red","rhs_mag_100rnd_127x99_mag_Tracer_Red","rhs_mag_100rnd_127x99_mag_Tracer_Red","rhs_mag_100rnd_127x99_mag_Tracer_Red","rhs_mag_100rnd_127x99_mag_Tracer_Red","rhs_mag_100rnd_127x99_mag_Tracer_Red"],
            "turretinfotype": "RHS_RscWeaponZeroing",
            "discretedistance": [100,200,300,400,500,600,800,1000,1200,1500],
            "discretedistanceinitindex": 2,
            "gunnername": "Port M2",
            "memorypointgunneroptics": "m2_p_sight",
            "gunnerlefthandanimname": "m2_p_hand_l",
            "gunnerrighthandanimname": "m2_p_hand_r",
            "gunnerleftleganimname": "m2_p_leg_l",
            "gunnerrightleganimname": "m2_p_leg_r",
            "gunneropticsmodel": "a3|weapons_f|Reticle|optics_empty",
            "gunnerforceoptics": 0,
            "startengine": 0,
            "commanding": 0,
            "primarygunner": 0,
            "primaryobserver": 0,
            "usepip": 0,
            "lodopticsin": 1000,
            "lodopticsout": 1000,
            "lodturnedin": 1000,
            "lodturnedout": 1000,
            "minelev": -45,
            "maxelev": 45,
            "initelev": 45,
            "minturn": 5,
            "maxturn": 145,
            "initturn": 65,
            # Class: CfgVehicles|rhsusf_mkvsoc|Turrets|MainTurret|m2_p_ViewOptics [Indent level: 3],
            "m2_p_viewoptics": {
                "initanglex": 0,
                "minanglex": -30,
                "maxanglex": 30,
                "initangley": 0,
                "minangley": -100,
                "maxangley": 100,
                "initfov": 0.7,
                "minfov": 0.25,
                "maxfov": 1.1,
                "minmovex": 0,
                "maxmovex": 0,
                "minmovey": 0,
                "maxmovey": 0,
                "minmovez": 0,
                "maxmovez": 0,
                "speedzoommaxspeed": 1e+010,
                "speedzoommaxfov": 0
            },
            # Class: CfgVehicles|rhsusf_mkvsoc|Turrets|MainTurret|m2_p_ViewGunner [Indent level: 3],
            "m2_p_viewgunner": {
                "initanglex": 5,
                "minanglex": -65,
                "maxanglex": 85,
                "initangley": 0,
                "minangley": -150,
                "maxangley": 150,
                "initfov": 0.7,
                "minfov": 0.25,
                "maxfov": 1.1,
                "minmovex": 0,
                "maxmovex": 0,
                "minmovey": 0,
                "maxmovey": 0,
                "minmovez": 0,
                "maxmovez": 0,
                "speedzoommaxspeed": 1e+010,
                "speedzoommaxfov": 0
            },
            "disablesoundattenuation": 1,
            "maxhorizontalrotspeed": 1.8,
            "maxverticalrotspeed": 1.2,
            # Class: CfgVehicles|rhsusf_mkvsoc|Turrets|MainTurret|HitPoints [Indent level: 3],
            "hitpoints": {
                # Class: CfgVehicles|rhsusf_mkvsoc|Turrets|MainTurret|HitPoints|HitTurret1 [Indent level: 4]
                "hitturret1": {
                    "isturret": 1,
                    "armor": 0.8,
                    "material": 60,
                    "name": "hit_gunTurret_m2_1",
                    "visual": "gunTurret_m2_1",
                    "passthrough": 0
                },
                # Class: CfgVehicles|rhsusf_mkvsoc|Turrets|MainTurret|HitPoints|HitGun1 [Indent level: 4],
                "hitgun1": {
                    "isgun": 1,
                    "armor": 0.6,
                    "material": 60,
                    "name": "hit_gunBarrel_m2_1",
                    "visual": "gunBarrel_m2_1",
                    "passthrough": 0
                }
            },
            "animationsourcehatch": "hatchGunner",
            "animationsourcecamelev": "camElev",
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
            "hideweaponsgunner": 1,
            "canhidegunner": -1,
            "forcehidegunner": 0,
            "showhmd": 0,
            "viewgunnerinexternal": 0,
            "lockwhendriverout": 0,
            "lockwhenvehiclespeed": -1,
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
            "iscopilot": 0,
            "caneject": 1,
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
            "memorypointgun": "kulas",
            "selectionfireanim": "zasleh",
            "showcrewaim": 0
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|Turrets|m2_s_gunTurret [Indent level: 2],
        "m2_s_gunturret": {
            "proxyindex": 2,
            "gunnercompartments": "Compartment3",
            "body": "m2_s_gunTurret",
            "gun": "m2_s_gun",
            "animationsourcebody": "m2_s_gunTurret",
            "animationsourcegun": "m2_s_gun",
            "gunneraction": "RHS_MKVSOC_Gunner04",
            "memorypointsgetingunner": "gunner_pos_p_m2",
            "memorypointsgetingunnerdir": "gunner_dir_p_m2",
            "gunbeg": "m2_s_beginBarrel",
            "gunend": "m2_s_endBarrel",
            "weapons": ["RHS_MKV_M2_s"],
            "gunnername": "Stbd M2",
            "memorypointgunneroptics": "m2_s_sight",
            "gunnerlefthandanimname": "m2_s_hand_l",
            "gunnerrighthandanimname": "m2_s_hand_r",
            "gunnerleftleganimname": "m2_s_leg_l",
            "gunnerrightleganimname": "m2_s_leg_r",
            "minelev": -45,
            "maxelev": 45,
            "initelev": 45,
            "minturn": -145,
            "maxturn": -5,
            "initturn": -65,
            # Class: CfgVehicles|rhsusf_mkvsoc|Turrets|m2_s_gunTurret|HitPoints [Indent level: 3],
            "hitpoints": {
                # Class: CfgVehicles|rhsusf_mkvsoc|Turrets|m2_s_gunTurret|HitPoints|HitTurret2 [Indent level: 4]
                "hitturret2": {
                    "isturret": 1,
                    "armor": 0.8,
                    "material": 60,
                    "name": "m2_s_turret",
                    "visual": "-",
                    "passthrough": 0
                },
                # Class: CfgVehicles|rhsusf_mkvsoc|Turrets|m2_s_gunTurret|HitPoints|HitGun2 [Indent level: 4],
                "hitgun2": {
                    "isgun": 1,
                    "armor": 0.6,
                    "material": 60,
                    "name": "m2_s_barrels",
                    "visual": "-",
                    "passthrough": 0
                }
            },
            "gunnertype": "rhsusf_socom_swcc_crewman",
            "stabilizedinaxes": 3,
            "proxytype": "CPGunner",
            "gunnergetinaction": "",
            "gunnergetoutaction": "",
            "gunnerreversedgetout": 0,
            "ejectdeadgunner": 1,
            "outgunnermayfire": 1,
            "ingunnermayfire": 1,
            "soundservo": ["A3|sounds_f|dummysound",0.00562341,1],
            "magazines": ["rhs_mag_100rnd_127x99_mag_Tracer_Red","rhs_mag_100rnd_127x99_mag_Tracer_Red","rhs_mag_100rnd_127x99_mag_Tracer_Red","rhs_mag_100rnd_127x99_mag_Tracer_Red","rhs_mag_100rnd_127x99_mag_Tracer_Red","rhs_mag_100rnd_127x99_mag_Tracer_Red"],
            "turretinfotype": "RHS_RscWeaponZeroing",
            "discretedistance": [100,200,300,400,500,600,800,1000,1200,1500],
            "discretedistanceinitindex": 2,
            "gunneropticsmodel": "a3|weapons_f|Reticle|optics_empty",
            "gunnerforceoptics": 0,
            "startengine": 0,
            "commanding": 0,
            "primarygunner": 0,
            "primaryobserver": 0,
            "usepip": 0,
            "lodopticsin": 1000,
            "lodopticsout": 1000,
            "lodturnedin": 1000,
            "lodturnedout": 1000,
            # Class: CfgVehicles|rhsusf_mkvsoc|Turrets|MainTurret|m2_p_ViewOptics [Indent level: 3],
            "m2_p_viewoptics": {
                "initanglex": 0,
                "minanglex": -30,
                "maxanglex": 30,
                "initangley": 0,
                "minangley": -100,
                "maxangley": 100,
                "initfov": 0.7,
                "minfov": 0.25,
                "maxfov": 1.1,
                "minmovex": 0,
                "maxmovex": 0,
                "minmovey": 0,
                "maxmovey": 0,
                "minmovez": 0,
                "maxmovez": 0,
                "speedzoommaxspeed": 1e+010,
                "speedzoommaxfov": 0
            },
            # Class: CfgVehicles|rhsusf_mkvsoc|Turrets|MainTurret|m2_p_ViewGunner [Indent level: 3],
            "m2_p_viewgunner": {
                "initanglex": 5,
                "minanglex": -65,
                "maxanglex": 85,
                "initangley": 0,
                "minangley": -150,
                "maxangley": 150,
                "initfov": 0.7,
                "minfov": 0.25,
                "maxfov": 1.1,
                "minmovex": 0,
                "maxmovex": 0,
                "minmovey": 0,
                "maxmovey": 0,
                "minmovez": 0,
                "maxmovez": 0,
                "speedzoommaxspeed": 1e+010,
                "speedzoommaxfov": 0
            },
            "disablesoundattenuation": 1,
            "maxhorizontalrotspeed": 1.8,
            "maxverticalrotspeed": 1.2,
            "animationsourcehatch": "hatchGunner",
            "animationsourcecamelev": "camElev",
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
            "hideweaponsgunner": 1,
            "canhidegunner": -1,
            "forcehidegunner": 0,
            "showhmd": 0,
            "viewgunnerinexternal": 0,
            "lockwhendriverout": 0,
            "lockwhenvehiclespeed": -1,
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
            "iscopilot": 0,
            "caneject": 1,
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
            "memorypointgun": "kulas",
            "selectionfireanim": "zasleh",
            "showcrewaim": 0
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|Turrets|m134_p_gunTurret [Indent level: 2],
        "m134_p_gunturret": {
            "proxyindex": 3,
            "gunnercompartments": "Compartment4",
            "body": "m134_p_gunTurret",
            "gun": "m134_p_gun",
            "animationsourcebody": "m134_p_gunTurret",
            "animationsourcegun": "m134_p_gun",
            "gunneraction": "RHS_MKVSOC_Gunner02",
            "memorypointsgetingunner": "gunner_pos_m134",
            "memorypointsgetingunnerdir": "gunner_dir_m134",
            "gunbeg": "m134_p_beginBarrel",
            "gunend": "m134_p_endBarrel",
            "weapons": ["RHS_MKV_M134"],
            "magazines": ["2000Rnd_762x51_Belt_T_Red","2000Rnd_762x51_Belt_T_Red"],
            "discretedistance": [300],
            "discretedistanceinitindex": 2,
            "gunnername": "Port M134",
            "memorypointgunneroptics": "m134_p_sight",
            "gunnerlefthandanimname": "m134_p_hand_l",
            "gunnerrighthandanimname": "m134_p_hand_r",
            "gunnerleftleganimname": "m134_p_leg_l",
            "gunnerrightleganimname": "m134_p_leg_r",
            "minelev": -45,
            "maxelev": 35,
            "initelev": 45,
            "minturn": 35,
            "maxturn": 140,
            "initturn": 65,
            # Class: CfgVehicles|rhsusf_mkvsoc|Turrets|m134_p_gunTurret|m134_p_ViewOptics [Indent level: 3],
            "m134_p_viewoptics": {
                "initanglex": 0,
                "minanglex": -30,
                "maxanglex": 30,
                "initangley": 0,
                "minangley": -100,
                "maxangley": 100,
                "initfov": 0.7,
                "minfov": 0.25,
                "maxfov": 1.1,
                "minmovex": 0,
                "maxmovex": 0,
                "minmovey": 0,
                "maxmovey": 0,
                "minmovez": 0,
                "maxmovez": 0,
                "speedzoommaxspeed": 1e+010,
                "speedzoommaxfov": 0
            },
            # Class: CfgVehicles|rhsusf_mkvsoc|Turrets|m134_p_gunTurret|m134_p_ViewGunner [Indent level: 3],
            "m134_p_viewgunner": {
                "initanglex": 5,
                "minanglex": -65,
                "maxanglex": 85,
                "initangley": 0,
                "minangley": -150,
                "maxangley": 150,
                "initfov": 0.7,
                "minfov": 0.25,
                "maxfov": 1.1,
                "minmovex": 0,
                "maxmovex": 0,
                "minmovey": 0,
                "maxmovey": 0,
                "minmovez": 0,
                "maxmovez": 0,
                "speedzoommaxspeed": 1e+010,
                "speedzoommaxfov": 0
            },
            "maxhorizontalrotspeed": 1.8,
            "maxverticalrotspeed": 1.2,
            # Class: CfgVehicles|rhsusf_mkvsoc|Turrets|m134_p_gunTurret|HitPoints [Indent level: 3],
            "hitpoints": {
                # Class: CfgVehicles|rhsusf_mkvsoc|Turrets|m134_p_gunTurret|HitPoints|HitTurret3 [Indent level: 4]
                "hitturret3": {
                    "armor": 0.8,
                    "material": 60,
                    "name": "m134_p_turret",
                    "visual": "m134_p_gunTurret",
                    "passthrough": 0
                },
                # Class: CfgVehicles|rhsusf_mkvsoc|Turrets|m134_p_gunTurret|HitPoints|HitGun3 [Indent level: 4],
                "hitgun3": {
                    "armor": 0.6,
                    "material": 60,
                    "name": "m134_p_barrels",
                    "visual": "m134_p_gun",
                    "passthrough": 0
                }
            },
            "gunnertype": "rhsusf_socom_swcc_crewman",
            "stabilizedinaxes": 3,
            "proxytype": "CPGunner",
            "gunnergetinaction": "",
            "gunnergetoutaction": "",
            "gunnerreversedgetout": 0,
            "ejectdeadgunner": 1,
            "outgunnermayfire": 1,
            "ingunnermayfire": 1,
            "soundservo": ["A3|sounds_f|dummysound",0.00562341,1],
            "turretinfotype": "RHS_RscWeaponZeroing",
            "gunneropticsmodel": "a3|weapons_f|Reticle|optics_empty",
            "gunnerforceoptics": 0,
            "startengine": 0,
            "commanding": 0,
            "primarygunner": 0,
            "primaryobserver": 0,
            "usepip": 0,
            "lodopticsin": 1000,
            "lodopticsout": 1000,
            "lodturnedin": 1000,
            "lodturnedout": 1000,
            # Class: CfgVehicles|rhsusf_mkvsoc|Turrets|MainTurret|m2_p_ViewOptics [Indent level: 3],
            "m2_p_viewoptics": {
                "initanglex": 0,
                "minanglex": -30,
                "maxanglex": 30,
                "initangley": 0,
                "minangley": -100,
                "maxangley": 100,
                "initfov": 0.7,
                "minfov": 0.25,
                "maxfov": 1.1,
                "minmovex": 0,
                "maxmovex": 0,
                "minmovey": 0,
                "maxmovey": 0,
                "minmovez": 0,
                "maxmovez": 0,
                "speedzoommaxspeed": 1e+010,
                "speedzoommaxfov": 0
            },
            # Class: CfgVehicles|rhsusf_mkvsoc|Turrets|MainTurret|m2_p_ViewGunner [Indent level: 3],
            "m2_p_viewgunner": {
                "initanglex": 5,
                "minanglex": -65,
                "maxanglex": 85,
                "initangley": 0,
                "minangley": -150,
                "maxangley": 150,
                "initfov": 0.7,
                "minfov": 0.25,
                "maxfov": 1.1,
                "minmovex": 0,
                "maxmovex": 0,
                "minmovey": 0,
                "maxmovey": 0,
                "minmovez": 0,
                "maxmovez": 0,
                "speedzoommaxspeed": 1e+010,
                "speedzoommaxfov": 0
            },
            "disablesoundattenuation": 1,
            "animationsourcehatch": "hatchGunner",
            "animationsourcecamelev": "camElev",
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
            "hideweaponsgunner": 1,
            "canhidegunner": -1,
            "forcehidegunner": 0,
            "showhmd": 0,
            "viewgunnerinexternal": 0,
            "lockwhendriverout": 0,
            "lockwhenvehiclespeed": -1,
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
            "iscopilot": 0,
            "caneject": 1,
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
            "memorypointgun": "kulas",
            "selectionfireanim": "zasleh",
            "showcrewaim": 0
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|Turrets|mk19_s_gunTurret [Indent level: 2],
        "mk19_s_gunturret": {
            "proxyindex": 4,
            "gunnercompartments": "Compartment5",
            "body": "mk19_s_gunTurret",
            "gun": "mk19_s_gun",
            "animationsourcebody": "mk19_s_gunTurret",
            "animationsourcegun": "mk19_s_gun",
            "gunneraction": "RHS_MKVSOC_Gunner03",
            "gunnergetinaction": "GetInLow",
            "gunnergetoutaction": "GetOutLow",
            "memorypointsgetingunner": "gunner_pos_mk19",
            "memorypointsgetingunnerdir": "gunner_dir_mk19",
            "gunbeg": "mk19_s_beginBarrel",
            "gunend": "mk19_s_endBarrel",
            "weapons": ["RHS_MKV_MK19"],
            "magazines": ["RHS_48Rnd_40mm_MK19_M430A1","RHS_48Rnd_40mm_MK19_M430A1","RHS_48Rnd_40mm_MK19_M430A1","RHS_48Rnd_40mm_MK19_M430A1"],
            "discretedistance": [300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500],
            "discretedistanceinitindex": 2,
            "gunnername": "Stbd Mk19",
            "memorypointgunneroptics": "mk19_s_sight",
            "gunnerlefthandanimname": "mk19_s_hand_l",
            "gunnerrighthandanimname": "mk19_s_hand_r",
            "gunnerleftleganimname": "mk19_s_leg_l",
            "gunnerrightleganimname": "mk19_s_leg_r",
            "minelev": -45,
            "maxelev": 55,
            "initelev": 45,
            "minturn": -137,
            "maxturn": -35,
            "initturn": -65,
            # Class: CfgVehicles|rhsusf_mkvsoc|Turrets|mk19_s_gunTurret|mk19_s_ViewOptics [Indent level: 3],
            "mk19_s_viewoptics": {
                "initanglex": 0,
                "minanglex": -30,
                "maxanglex": 30,
                "initangley": 0,
                "minangley": -100,
                "maxangley": 100,
                "initfov": 0.7,
                "minfov": 0.25,
                "maxfov": 1.1,
                "minmovex": 0,
                "maxmovex": 0,
                "minmovey": 0,
                "maxmovey": 0,
                "minmovez": 0,
                "maxmovez": 0,
                "speedzoommaxspeed": 1e+010,
                "speedzoommaxfov": 0
            },
            # Class: CfgVehicles|rhsusf_mkvsoc|Turrets|mk19_s_gunTurret|mk19_s_ViewGunner [Indent level: 3],
            "mk19_s_viewgunner": {
                "initanglex": 5,
                "minanglex": -65,
                "maxanglex": 85,
                "initangley": 0,
                "minangley": -150,
                "maxangley": 150,
                "initfov": 0.7,
                "minfov": 0.25,
                "maxfov": 1.1,
                "minmovex": 0,
                "maxmovex": 0,
                "minmovey": 0,
                "maxmovey": 0,
                "minmovez": 0,
                "maxmovez": 0,
                "speedzoommaxspeed": 1e+010,
                "speedzoommaxfov": 0
            },
            # Class: CfgVehicles|rhsusf_mkvsoc|Turrets|mk19_s_gunTurret|HitPoints [Indent level: 3],
            "hitpoints": {
                # Class: CfgVehicles|rhsusf_mkvsoc|Turrets|mk19_s_gunTurret|HitPoints|HitTurret4 [Indent level: 4]
                "hitturret4": {
                    "isturret": 1,
                    "armor": 0.8,
                    "material": 60,
                    "name": "m134_p_turret",
                    "visual": "m134_p_gunTurret",
                    "passthrough": 0
                },
                # Class: CfgVehicles|rhsusf_mkvsoc|Turrets|mk19_s_gunTurret|HitPoints|HitGun4 [Indent level: 4],
                "hitgun4": {
                    "isgun": 1,
                    "armor": 0.6,
                    "material": 60,
                    "name": "m134_p_barrels",
                    "visual": "m134_p_gun",
                    "passthrough": 0
                }
            },
            "gunnertype": "rhsusf_socom_swcc_crewman",
            "stabilizedinaxes": 3,
            "proxytype": "CPGunner",
            "gunnerreversedgetout": 0,
            "ejectdeadgunner": 1,
            "outgunnermayfire": 1,
            "ingunnermayfire": 1,
            "soundservo": ["A3|sounds_f|dummysound",0.00562341,1],
            "turretinfotype": "RHS_RscWeaponZeroing",
            "gunneropticsmodel": "a3|weapons_f|Reticle|optics_empty",
            "gunnerforceoptics": 0,
            "startengine": 0,
            "commanding": 0,
            "primarygunner": 0,
            "primaryobserver": 0,
            "usepip": 0,
            "lodopticsin": 1000,
            "lodopticsout": 1000,
            "lodturnedin": 1000,
            "lodturnedout": 1000,
            # Class: CfgVehicles|rhsusf_mkvsoc|Turrets|MainTurret|m2_p_ViewOptics [Indent level: 3],
            "m2_p_viewoptics": {
                "initanglex": 0,
                "minanglex": -30,
                "maxanglex": 30,
                "initangley": 0,
                "minangley": -100,
                "maxangley": 100,
                "initfov": 0.7,
                "minfov": 0.25,
                "maxfov": 1.1,
                "minmovex": 0,
                "maxmovex": 0,
                "minmovey": 0,
                "maxmovey": 0,
                "minmovez": 0,
                "maxmovez": 0,
                "speedzoommaxspeed": 1e+010,
                "speedzoommaxfov": 0
            },
            # Class: CfgVehicles|rhsusf_mkvsoc|Turrets|MainTurret|m2_p_ViewGunner [Indent level: 3],
            "m2_p_viewgunner": {
                "initanglex": 5,
                "minanglex": -65,
                "maxanglex": 85,
                "initangley": 0,
                "minangley": -150,
                "maxangley": 150,
                "initfov": 0.7,
                "minfov": 0.25,
                "maxfov": 1.1,
                "minmovex": 0,
                "maxmovex": 0,
                "minmovey": 0,
                "maxmovey": 0,
                "minmovez": 0,
                "maxmovez": 0,
                "speedzoommaxspeed": 1e+010,
                "speedzoommaxfov": 0
            },
            "disablesoundattenuation": 1,
            "maxhorizontalrotspeed": 1.8,
            "maxverticalrotspeed": 1.2,
            "animationsourcehatch": "hatchGunner",
            "animationsourcecamelev": "camElev",
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
            "hideweaponsgunner": 1,
            "canhidegunner": -1,
            "forcehidegunner": 0,
            "showhmd": 0,
            "viewgunnerinexternal": 0,
            "lockwhendriverout": 0,
            "lockwhenvehiclespeed": -1,
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
            "iscopilot": 0,
            "caneject": 1,
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
            "memorypointgun": "kulas",
            "selectionfireanim": "zasleh",
            "showcrewaim": 0
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|Turrets|camera_b_gunTurret [Indent level: 2],
        "camera_b_gunturret": {
            "gunnertype": "rhsusf_socom_swcc_officer",
            "stabilizedinaxes": 3,
            "proxytype": "CPCommander",
            "proxyindex": 1,
            "gunnercompartments": "Compartment1",
            "body": "camera_b_gunTurret",
            "gun": "camera_b_gun",
            "animationsourcebody": "camera_b_gunTurret",
            "animationsourcegun": "camera_b_gun",
            "gunneraction": "RHS_MKVSOC_Commander",
            "gunnergetinaction": "GetInMedium",
            "gunnergetoutaction": "GetOutMedium",
            "ejectdeadgunner": 0,
            "outgunnermayfire": 1,
            "ingunnermayfire": 1,
            "soundservo": ["A3|Sounds_F|vehicles|armor|noises|servo_best",0.01,1,50],
            "gunbeg": "axis_camera_b_dir",
            "gunend": "axis_camera_b_pos",
            "memorypointgunneroptics": "axis_camera_b_pos",
            "memorypointsgetingunner": "comm_pos",
            "memorypointsgetingunnerdir": "comm_dir",
            "weapons": ["Laserdesignator_mounted"],
            "magazines": ["Laserbatteries"],
            "gunnerlefthandanimname": "cmdr_hand_l",
            "gunnerrighthandanimname": "cmdr_hand_r",
            "gunnerleftleganimname": "cmdr_leg_l",
            "gunnerrightleganimname": "cmdr_leg_r",
            "gunnername": "Commander",
            "gunneropticsmodel": "A3|weapons_f_beta|reticle|reticle_SDV",
            "gunnerforceoptics": 0,
            "startengine": 0,
            "commanding": 0,
            "primarygunner": 0,
            "primaryobserver": 1,
            "usepip": 1,
            "laser": 1,
            "minelev": -30,
            "maxelev": 60,
            "initelev": 60,
            "minturn": -180,
            "maxturn": 180,
            "initturn": 0,
            # Class: CfgVehicles|rhsusf_mkvsoc|Turrets|camera_b_gunTurret|camera_b_ViewOptics [Indent level: 3],
            "camera_b_viewoptics": {
                "initanglex": 0,
                "minanglex": 0,
                "maxanglex": 0,
                "initangley": 0,
                "minangley": -180,
                "maxangley": 180,
                "initfov": 0.14,
                "minfov": 0.0175,
                "maxfov": 0.14,
                "visionmode": ["Normal","NVG","Ti"],
                "thermalmode": [2,3,4],
                "minmovex": 0,
                "maxmovex": 0,
                "minmovey": 0,
                "maxmovey": 0,
                "minmovez": 0,
                "maxmovez": 0,
                "speedzoommaxspeed": 1e+010,
                "speedzoommaxfov": 0
            },
            # Class: CfgVehicles|rhsusf_mkvsoc|Turrets|camera_b_gunTurret|camera_b_ViewGunner [Indent level: 3],
            "camera_b_viewgunner": {
                "initanglex": -15,
                "minanglex": -45,
                "maxanglex": 45,
                "initangley": 0,
                "minangley": -150,
                "maxangley": 150,
                "initfov": 0.9,
                "minfov": 0.42,
                "maxfov": 0.9,
                "visionmode": [],
                "minmovex": 0,
                "maxmovex": 0,
                "minmovey": 0,
                "maxmovey": 0,
                "minmovez": 0,
                "maxmovez": 0,
                "speedzoommaxspeed": 1e+010,
                "speedzoommaxfov": 0
            },
            "maxhorizontalrotspeed": 1.8,
            "maxverticalrotspeed": 1.2,
            # Class: CfgVehicles|rhsusf_mkvsoc|Turrets|camera_b_gunTurret|HitPoints [Indent level: 3],
            "hitpoints": {
            },
            "gunnerreversedgetout": 0,
            "turretinfotype": "RHS_RscWeaponZeroing",
            "discretedistance": [100,200,300,400,500,600,800,1000,1200,1500],
            "discretedistanceinitindex": 2,
            "lodopticsin": 1000,
            "lodopticsout": 1000,
            "lodturnedin": 1000,
            "lodturnedout": 1000,
            # Class: CfgVehicles|rhsusf_mkvsoc|Turrets|MainTurret|m2_p_ViewOptics [Indent level: 3],
            "m2_p_viewoptics": {
                "initanglex": 0,
                "minanglex": -30,
                "maxanglex": 30,
                "initangley": 0,
                "minangley": -100,
                "maxangley": 100,
                "initfov": 0.7,
                "minfov": 0.25,
                "maxfov": 1.1,
                "minmovex": 0,
                "maxmovex": 0,
                "minmovey": 0,
                "maxmovey": 0,
                "minmovez": 0,
                "maxmovez": 0,
                "speedzoommaxspeed": 1e+010,
                "speedzoommaxfov": 0
            },
            # Class: CfgVehicles|rhsusf_mkvsoc|Turrets|MainTurret|m2_p_ViewGunner [Indent level: 3],
            "m2_p_viewgunner": {
                "initanglex": 5,
                "minanglex": -65,
                "maxanglex": 85,
                "initangley": 0,
                "minangley": -150,
                "maxangley": 150,
                "initfov": 0.7,
                "minfov": 0.25,
                "maxfov": 1.1,
                "minmovex": 0,
                "maxmovex": 0,
                "minmovey": 0,
                "maxmovey": 0,
                "minmovez": 0,
                "maxmovez": 0,
                "speedzoommaxspeed": 1e+010,
                "speedzoommaxfov": 0
            },
            "disablesoundattenuation": 1,
            "animationsourcehatch": "hatchGunner",
            "animationsourcecamelev": "camElev",
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
            "hideweaponsgunner": 1,
            "canhidegunner": -1,
            "forcehidegunner": 0,
            "showhmd": 0,
            "viewgunnerinexternal": 0,
            "lockwhendriverout": 0,
            "lockwhenvehiclespeed": -1,
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
            "iscopilot": 0,
            "caneject": 1,
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
            "memorypointgun": "kulas",
            "selectionfireanim": "zasleh",
            "showcrewaim": 0
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|Turrets|rem_spotL_gunTurret [Indent level: 2],
        "rem_spotl_gunturret": {
            "gunnertype": "rhsusf_socom_swcc_officer",
            "stabilizedinaxes": 4,
            "proxytype": "CPCommander",
            "proxyindex": 2,
            "gunnercompartments": "Compartment1",
            "body": "rem_spotL_gunTurret",
            "gun": "rem_spotL_gun",
            "animationsourcebody": "rem_spotL_gunTurret",
            "animationsourcegun": "rem_spotL_gun",
            "gunneraction": "RHS_MKVSOC_Commander02",
            "gunnergetinaction": "GetInMedium",
            "gunnergetoutaction": "GetOutMedium",
            "ejectdeadgunner": 0,
            "outgunnermayfire": 1,
            "ingunnermayfire": 0,
            "soundservo": ["A3|Sounds_F|vehicles|armor|noises|servo_best",0.2,1,1],
            "gunbeg": "axis_rem_spotL_dir",
            "gunend": "axis_rem_spotL_pos",
            "memorypointgunneroptics": "rem_spotL_sight",
            "memorypointsgetingunner": "gunner_pos",
            "memorypointsgetingunnerdir": "gunner_dir",
            "weapons": [],
            "magazines": [],
            "gunnername": "Technician",
            "gunneropticsmodel": "a3|weapons_f|Reticle|optics_empty",
            "gunnerforceoptics": 0,
            "startengine": 0,
            "commanding": 0,
            "primarygunner": 0,
            "primaryobserver": 0,
            "usepip": 0,
            "laser": 0,
            "minelev": -7.5,
            "maxelev": 60,
            "initelev": 0,
            "minturn": -145,
            "maxturn": 145,
            "initturn": 0,
            # Class: CfgVehicles|rhsusf_mkvsoc|Turrets|rem_spotL_gunTurret|rem_spotL_ViewOptics [Indent level: 3],
            "rem_spotl_viewoptics": {
                "initanglex": 0,
                "minanglex": 0,
                "maxanglex": 0,
                "initangley": 0,
                "minangley": -150,
                "maxangley": 150,
                "initfov": 0.14,
                "minfov": 0.0175,
                "maxfov": 0.14,
                "visionmode": [],
                "thermalmode": [],
                "minmovex": 0,
                "maxmovex": 0,
                "minmovey": 0,
                "maxmovey": 0,
                "minmovez": 0,
                "maxmovez": 0,
                "speedzoommaxspeed": 1e+010,
                "speedzoommaxfov": 0
            },
            # Class: CfgVehicles|rhsusf_mkvsoc|Turrets|rem_spotL_gunTurret|rem_spotL_ViewGunner [Indent level: 3],
            "rem_spotl_viewgunner": {
                "initanglex": -15,
                "minanglex": -45,
                "maxanglex": 45,
                "initangley": 0,
                "minangley": -150,
                "maxangley": 150,
                "initfov": 0.9,
                "minfov": 0.42,
                "maxfov": 0.9,
                "visionmode": [],
                "minmovex": 0,
                "maxmovex": 0,
                "minmovey": 0,
                "maxmovey": 0,
                "minmovez": 0,
                "maxmovez": 0,
                "speedzoommaxspeed": 1e+010,
                "speedzoommaxfov": 0
            },
            "maxhorizontalrotspeed": 1.8,
            "maxverticalrotspeed": 1.2,
            # Class: CfgVehicles|rhsusf_mkvsoc|Turrets|rem_spotL_gunTurret|HitPoints [Indent level: 3],
            "hitpoints": {
            },
            "gunnerreversedgetout": 0,
            "turretinfotype": "RHS_RscWeaponZeroing",
            "discretedistance": [100,200,300,400,500,600,800,1000,1200,1500],
            "discretedistanceinitindex": 2,
            "gunnerlefthandanimname": "m2_p_hand_l",
            "gunnerrighthandanimname": "m2_p_hand_r",
            "gunnerleftleganimname": "m2_p_leg_l",
            "gunnerrightleganimname": "m2_p_leg_r",
            "lodopticsin": 1000,
            "lodopticsout": 1000,
            "lodturnedin": 1000,
            "lodturnedout": 1000,
            # Class: CfgVehicles|rhsusf_mkvsoc|Turrets|MainTurret|m2_p_ViewOptics [Indent level: 3],
            "m2_p_viewoptics": {
                "initanglex": 0,
                "minanglex": -30,
                "maxanglex": 30,
                "initangley": 0,
                "minangley": -100,
                "maxangley": 100,
                "initfov": 0.7,
                "minfov": 0.25,
                "maxfov": 1.1,
                "minmovex": 0,
                "maxmovex": 0,
                "minmovey": 0,
                "maxmovey": 0,
                "minmovez": 0,
                "maxmovez": 0,
                "speedzoommaxspeed": 1e+010,
                "speedzoommaxfov": 0
            },
            # Class: CfgVehicles|rhsusf_mkvsoc|Turrets|MainTurret|m2_p_ViewGunner [Indent level: 3],
            "m2_p_viewgunner": {
                "initanglex": 5,
                "minanglex": -65,
                "maxanglex": 85,
                "initangley": 0,
                "minangley": -150,
                "maxangley": 150,
                "initfov": 0.7,
                "minfov": 0.25,
                "maxfov": 1.1,
                "minmovex": 0,
                "maxmovex": 0,
                "minmovey": 0,
                "maxmovey": 0,
                "minmovez": 0,
                "maxmovez": 0,
                "speedzoommaxspeed": 1e+010,
                "speedzoommaxfov": 0
            },
            "disablesoundattenuation": 1,
            "animationsourcehatch": "hatchGunner",
            "animationsourcecamelev": "camElev",
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
            "hideweaponsgunner": 1,
            "canhidegunner": -1,
            "forcehidegunner": 0,
            "showhmd": 0,
            "viewgunnerinexternal": 0,
            "lockwhendriverout": 0,
            "lockwhenvehiclespeed": -1,
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
            "iscopilot": 0,
            "caneject": 1,
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
            "memorypointgun": "kulas",
            "selectionfireanim": "zasleh",
            "showcrewaim": 0
        }
    },
    # Class: CfgVehicles|rhsusf_mkvsoc|UserActions [Indent level: 1],
    "useractions": {
        # Class: CfgVehicles|rhsusf_mkvsoc|UserActions|OpenMenu [Indent level: 2]
        "openmenu": {
            "useractionid": 74,
            "priority": 11.008,
            "displayname": "<t color='#FDDE00'>Open control panel</t>",
            "position": "beacon_point",
            "radius": 10,
            "animperiod": 2,
            "onlyforplayer": 1,
            "condition": "driver this == (call rhsusf_fnc_findPlayer)",
            "statement": "[this] call rhsusf_fnc_markvsoc_openMenu"
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|UserActions|OpenLoadMenu [Indent level: 2],
        "openloadmenu": {
            "useractionid": 74,
            "priority": 10.008,
            "displayname": "<t color='#038D4A'>Open vehicle loading menu</t>",
            "position": "beacon_point",
            "radius": 10,
            "animperiod": 2,
            "onlyforplayer": 1,
            "condition": "driver this == (call rhsusf_fnc_findPlayer)",
            "statement": "[this] spawn rhsusf_fnc_markvsoc_loadMenuInit"
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|UserActions|GetOnDeck [Indent level: 2],
        "getondeck": {
            "useractionid": 74,
            "priority": 11.008,
            "displayname": "Get on deck",
            "position": "axis_ramp_roller",
            "radius": 4,
            "animperiod": 2,
            "onlyforplayer": 1,
            "condition": "(getposasl (call rhsusf_fnc_findPlayer)) select 2 < -1",
            "statement": "[] spawn rhsusf_fnc_markvsoc_getIn"
        }
    },
    # Class: CfgVehicles|rhsusf_mkvsoc|Attributes [Indent level: 1],
    "attributes": {
        # Class: CfgVehicles|rhsusf_mkvsoc|Attributes|ObjectTexture [Indent level: 2]
        "objecttexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayname": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        # Class: CfgVehicles|rhsusf_mkvsoc|Attributes|rhs_attachCargo [Indent level: 2],
        "rhs_attachcargo": {
            "control": "CheckboxNumber",
            "defaultvalue": "0",
            "displayname": "Attach cargo",
            "tooltip": "Attaching cargo (using attachTo command) just like when you use ramp action",
            "property": "rhs_attachCargo",
            "expression": "if(_value == 1)then{[_this] spawn rhsusf_fnc_markvsoc_attachBoats};"
        }
    },
    "hiddenselections": ["camo1"],
    "hiddenselectionstextures": ["rhsusf|addons|rhsusf_markvsoc|data|hull_co.paa"],
    # Class: CfgVehicles|rhsusf_mkvsoc|textureSources [Indent level: 1],
    "texturesources": {
        # Class: CfgVehicles|rhsusf_mkvsoc|textureSources|marsoc [Indent level: 2]
        "marsoc": {
            "displayname": "US",
            "author": "Red Hammer Studios",
            "textures": ["rhsusf|addons|rhsusf_markvsoc|data|hull_co.paa"]
        }
    },
    "texturelist": [],
    "unitinfotype": "UnitInfoShip",
    "memorypointsleftengineeffect": "EngineEffectL",
    "memorypointsrightengineeffect": "EngineEffectR",
    "_generalmacro": "Ship_F",
    "armorstructural": 1,
    "explosionshielding": 4,
    "mintotaldamagethreshold": 0.01,
    "crewexplosionprotection": 0.5,
    # Class: CfgVehicles|Ship_F|HitPoints [Indent level: 1],
    "hitpoints": {
        # Class: CfgVehicles|Ship_F|HitPoints|HitEngine [Indent level: 2]
        "hitengine": {
            "armor": 1,
            "material": 60,
            "name": "motor",
            "visual": "motor",
            "passthrough": 1
        }
    },
    "epeimpulsedamagecoef": 70,
    "fuelexplosionpower": 10,
    "transportmaxbackpacks": 5,
    "transportmaxmagazines": 100,
    "transportmaxweapons": 10,
    "ejectdeaddriver": 0,
    "ejectdeadcargo": 0,
    "gunnerhasflares": 0,
    # Class: CfgVehicles|Ship_F|CamShake [Indent level: 1],
    "camshake": {
        "power": 10,
        "frequency": 10,
        "distance": 20,
        "minspeed": 5
    },
    "camshakecoef": 0,
    # Class: CfgVehicles|Ship_F|ViewPilot [Indent level: 1],
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
    "headgforceleaningfactor": [0.015,0.015,0.02],
    # Class: CfgVehicles|Ship_F|DestructionEffects [Indent level: 1],
    "destructioneffects": {
    },
    "safedepth": 2,
    "formationx": 50,
    "formationz": 100,
    "formationtime": 20,
    "verticalturncoef": 0.2,
    "shipsteercoef": 0.5,
    "periscopedepth": 2.8,
    "pointpilot": "pilot",
    "pointcommander": "velitel",
    "selectionfireanim": "zasleh",
    "selectionbrakelights": "brzdove svetlo",
    "memorypointmissile": ["spice rakety","usti hlavne"],
    "memorypointmissiledir": ["konec rakety","konec hlavne"],
    "soundgear": ["",0.000177828,1],
    "leftdusteffect": "LDustEffects",
    "rightdusteffect": "RDustEffects",
    "leftwatereffect": "LWaterEffects",
    "rightwatereffect": "RWaterEffects",
    "leftengineeffect": "LEngEffects",
    "rightengineeffect": "REngEffects",
    # Class: CfgVehicles|Ship|ViewOptics [Indent level: 1],
    "viewoptics": {
        "initfov": 0.7,
        "minfov": 0.07,
        "maxfov": 0.35,
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
    "memorypointtaskmarkeroffset": [0,0.3,0],
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
    "tracksspeed": 0,
    "selectionleftoffset": "",
    "selectionrightoffset": "",
    "cargoproxyindexes": [],
    "driverdoor": "",
    "cargodoors": [],
    "hasterminal": 0,
    "getinoutonproxy": 0,
    "precisegetinout": 0,
    "cargoprecisegetinout": [0],
    "availableforsupporttypes": [],
    "waterppinvehicle": 1,
    "weaponsgroup1": "1 + 		2",
    "weaponsgroup2": 4,
    "weaponsgroup3": "8 + 	16 + 	32",
    "weaponsgroup4": "64 + 		128",
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
    "outsidesoundfilter": 0,
    "obstructsoundlfratio": 0,
    "occludesoundlfratio": 0.25,
    "antirollbarforcecoef": 0,
    "antirollbarforcelimit": 5,
    "antirollbarspeedmin": 20,
    "antirollbarspeedmax": 60,
    "sensitivityear": 0.0075,
    "portrait": "",
    "ghostpreview": "",
    "destrtype": "DestructDefault",
    "armorlights": 0.4,
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
    "alwaystarget": 0,
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
    "preferroads": 0,
    "unitinfotypelite": 0,
    "hideunitinfo": 0,
    "nightvision": 0,
    "radartype": 0,
    "limitedspeedcoef": 0.22,
    "driverforceoptics": 0,
    "memorypointsupply": "doplnovani",
    "enablewatch": 0,
    "enableradio": 0,
    "useprecisegetinaction": 0,
    "allowtablock": 1,
    "showalltargets": 0,
    "dustfrontleftpos": "dustFrontLeft",
    "dustfrontrightpos": "dustFrontRight",
    "dustbackleftpos": "dustBackLeft",
    "dustbackrightpos": "dustBackRight",
    "wheelcircumference": 1,
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
    "isbackpack": 0,
    "transportfuel": 0,
    "transportrepair": 0,
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
    "soundbushcrash": ["emptySound",0],
    "soundlocked": ["",1,1],
    "soundincommingmissile": ["",1,1],
    "sounddammage": ["",1,1],
    "driverinaction": "",
    "cargoiscodriver": [0],
    "drivercompartments": "Compartment1",
    "cargocompartments": ["Compartment1"],
    "driveropticsmodel": "",
    "driveropticseffect": [],
    "driveropticscolor": [1,1,1,1],
    "forcehidedriver": 0,
    "canhidedriver": -1,
    "viewdrivershadow": 1,
    "viewdrivershadowdiff": 1,
    "viewdrivershadowamb": 1,
    "viewcargoshadow": 1,
    "viewcargoshadowdiff": 1,
    "viewcargoshadowamb": 1,
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
    "waterresistance": 10,
    "waterdamageengine": 0.2,
    "maxfordingdepth": 1,
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
    "soundturnin": ["",0.000316228,1],
    "soundturnout": ["",0.000316228,1],
    "soundturnininternal": ["",0.000316228,1],
    "soundturnoutinternal": ["",0.000316228,1],
    "features": "",
    "insidedetectcoef": 0.05,
}