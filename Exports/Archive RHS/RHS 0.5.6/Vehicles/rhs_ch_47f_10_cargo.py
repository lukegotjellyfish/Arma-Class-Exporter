rhs_ch_47f_10_cargo = {
    "faction": "rhs_faction_usarmy_d",
    "vehicleclass": "rhs_vehclass_helicopter",
    "crew": "rhsusf_army_ocp_helipilot",
    "typicalcargo": ["rhsusf_army_ocp_helicrew"],
    "author": "Red Hammer Studios",
    "editorpreview": "rhsusf|addons|rhsusf_editorPreviews|data|RHS_CH_47F_10.paa",
    "accuracy": 1000,
    "scope": 2,
    "displayname": "CH-47F (Cargo)",
    # Class: CfgVehicles|RHS_CH_47F_cargo_base|AnimationSources [Indent level: 1],
    "animationsources": {
        # Class: CfgVehicles|RHS_CH_47F_cargo_base|AnimationSources|hide_cargo [Indent level: 2]
        "hide_cargo": {
            "displayname": "",
            "initphase": 1,
            "source": "user",
            "mass": -20,
            "animperiod": 1e-005,
            "onphasechanged": "(_this select 0) lockCargo ((_this select 1)==1)"
        },
        # Class: CfgVehicles|RHS_CH_47F_base|AnimationSources|cargolights_hide [Indent level: 2],
        "cargolights_hide": {
            "source": "user",
            "animperiod": 1e-006,
            "initphase": 0
        },
        # Class: CfgVehicles|RHS_CH_47F_base|AnimationSources|cabinlights_hide [Indent level: 2],
        "cabinlights_hide": {
            "source": "user",
            "animperiod": 1e-006,
            "initphase": 0
        },
        # Class: CfgVehicles|RHS_CH_47F_base|AnimationSources|Gatling_1 [Indent level: 2],
        "gatling_1": {
            "source": "revolving",
            "weapon": "rhs_weap_m134_minigun_1"
        },
        # Class: CfgVehicles|RHS_CH_47F_base|AnimationSources|Gatling_2 [Indent level: 2],
        "gatling_2": {
            "source": "revolving",
            "weapon": "rhs_weap_m134_minigun_2"
        },
        # Class: CfgVehicles|RHS_CH_47F_base|AnimationSources|muzzle_rot_hmg [Indent level: 2],
        "muzzle_rot_hmg": {
            "source": "ammorandom",
            "weapon": "rhs_weap_m134_minigun_1"
        },
        # Class: CfgVehicles|RHS_CH_47F_base|AnimationSources|muzzle_rot_hmg2 [Indent level: 2],
        "muzzle_rot_hmg2": {
            "source": "ammorandom",
            "weapon": "rhs_weap_m134_minigun_2"
        },
        # Class: CfgVehicles|RHS_CH_47F_base|AnimationSources|ramp_anim [Indent level: 2],
        "ramp_anim": {
            "sound": "ServoRampSound_2",
            "soundposition": "osa_ramp",
            "source": "user",
            "animperiod": 5,
            "initphase": 0
        },
        # Class: CfgVehicles|RHS_CH_47F_base|AnimationSources|Hide_Scopes [Indent level: 2],
        "hide_scopes": {
            "source": "user",
            "initphase": 0,
            "usesource": 1,
            "animperiod": 0.1,
            "displayname": "Hide DCL-120 sights"
        },
        # Class: CfgVehicles|RHS_CH_47F_base|AnimationSources|HitGlass1 [Indent level: 2],
        "hitglass1": {
            "source": "Hit",
            "hitpoint": "HitGlass1",
            "raw": 1
        },
        # Class: CfgVehicles|RHS_CH_47F_base|AnimationSources|HitGlass2 [Indent level: 2],
        "hitglass2": {
            "source": "Hit",
            "hitpoint": "HitGlass2",
            "raw": 1
        },
        # Class: CfgVehicles|RHS_CH_47F_base|AnimationSources|HitGlass3 [Indent level: 2],
        "hitglass3": {
            "source": "Hit",
            "hitpoint": "HitGlass3",
            "raw": 1
        },
        # Class: CfgVehicles|RHS_CH_47F_base|AnimationSources|HitGlass4 [Indent level: 2],
        "hitglass4": {
            "source": "Hit",
            "hitpoint": "HitGlass4",
            "raw": 1
        },
        # Class: CfgVehicles|RHS_CH_47F_base|AnimationSources|HitGlass5 [Indent level: 2],
        "hitglass5": {
            "source": "Hit",
            "hitpoint": "HitGlass5",
            "raw": 1
        },
        # Class: CfgVehicles|RHS_CH_47F_base|AnimationSources|HitGlass6 [Indent level: 2],
        "hitglass6": {
            "source": "Hit",
            "hitpoint": "HitGlass6",
            "raw": 1
        },
        # Class: CfgVehicles|RHS_CH_47F_base|AnimationSources|HitGlass7 [Indent level: 2],
        "hitglass7": {
            "source": "Hit",
            "hitpoint": "HitGlass7",
            "raw": 1
        },
        # Class: CfgVehicles|RHS_CH_47F_base|AnimationSources|HitGlass8 [Indent level: 2],
        "hitglass8": {
            "source": "Hit",
            "hitpoint": "HitGlass8",
            "raw": 1
        },
        # Class: CfgVehicles|RHS_CH_47F_base|AnimationSources|HitGlass9 [Indent level: 2],
        "hitglass9": {
            "source": "Hit",
            "hitpoint": "HitGlass9",
            "raw": 1
        },
        # Class: CfgVehicles|RHS_CH_47F_base|AnimationSources|HitGlass10 [Indent level: 2],
        "hitglass10": {
            "source": "Hit",
            "hitpoint": "HitGlass10",
            "raw": 1
        },
        # Class: CfgVehicles|RHS_CH_47F_base|AnimationSources|HitGlass11 [Indent level: 2],
        "hitglass11": {
            "source": "Hit",
            "hitpoint": "HitGlass11",
            "raw": 1
        },
        # Class: CfgVehicles|RHS_CH_47F_base|AnimationSources|HitGlass12 [Indent level: 2],
        "hitglass12": {
            "source": "Hit",
            "hitpoint": "HitGlass12",
            "raw": 1
        },
        # Class: CfgVehicles|RHS_CH_47F_base|AnimationSources|HitGlass13 [Indent level: 2],
        "hitglass13": {
            "source": "Hit",
            "hitpoint": "HitGlass13",
            "raw": 1
        },
        # Class: CfgVehicles|RHS_CH_47F_base|AnimationSources|HitGlass14 [Indent level: 2],
        "hitglass14": {
            "source": "Hit",
            "hitpoint": "HitGlass14",
            "raw": 1
        },
        # Class: CfgVehicles|RHS_CH_47F_base|AnimationSources|HitGlass15 [Indent level: 2],
        "hitglass15": {
            "source": "Hit",
            "hitpoint": "HitGlass15",
            "raw": 1
        },
        # Class: CfgVehicles|RHS_CH_47F_base|AnimationSources|Damper_1_1_source [Indent level: 2],
        "damper_1_1_source": {
            "source": "damper",
            "wheel": "Wheel_1_1"
        },
        # Class: CfgVehicles|RHS_CH_47F_base|AnimationSources|Damper_1_2_source [Indent level: 2],
        "damper_1_2_source": {
            "source": "damper",
            "wheel": "Wheel_1_2"
        },
        # Class: CfgVehicles|RHS_CH_47F_base|AnimationSources|Damper_2_1_source [Indent level: 2],
        "damper_2_1_source": {
            "source": "damper",
            "wheel": "Wheel_2_1"
        },
        # Class: CfgVehicles|RHS_CH_47F_base|AnimationSources|Damper_2_2_source [Indent level: 2],
        "damper_2_2_source": {
            "source": "damper",
            "wheel": "Wheel_2_2"
        },
        # Class: CfgVehicles|RHS_CH_47F_base|AnimationSources|Wheel_1_1_source [Indent level: 2],
        "wheel_1_1_source": {
            "source": "wheel",
            "wheel": "Wheel_1_1"
        },
        # Class: CfgVehicles|RHS_CH_47F_base|AnimationSources|Wheel_1_2_source [Indent level: 2],
        "wheel_1_2_source": {
            "source": "wheel",
            "wheel": "Wheel_1_2"
        },
        # Class: CfgVehicles|RHS_CH_47F_base|AnimationSources|Wheel_2_1_source [Indent level: 2],
        "wheel_2_1_source": {
            "source": "wheel",
            "wheel": "Wheel_2_1"
        },
        # Class: CfgVehicles|RHS_CH_47F_base|AnimationSources|Wheel_2_2_source [Indent level: 2],
        "wheel_2_2_source": {
            "source": "wheel",
            "wheel": "Wheel_2_2"
        },
        # Class: CfgVehicles|RHS_CH_47F_base|AnimationSources|Helicopter_Brakes [Indent level: 2],
        "helicopter_brakes": {
            "source": "user",
            "animperiod": 0.01,
            "initphase": 1
        },
        # Class: CfgVehicles|Heli_Transport_02_base_F|AnimationSources|CargoRamp_Open [Indent level: 2],
        "cargoramp_open": {
            "source": "door",
            "animperiod": 5,
            "initphase": 0,
            "sound": "ServoRampSound_2"
        },
        # Class: CfgVehicles|Heli_Transport_02_base_F|AnimationSources|Door_Back_L [Indent level: 2],
        "door_back_l": {
            "source": "door",
            "animperiod": 0.6,
            "sound": "ServoDoorsSound"
        },
        # Class: CfgVehicles|Heli_Transport_02_base_F|AnimationSources|Door_Back_R [Indent level: 2],
        "door_back_r": {
            "source": "door",
            "animperiod": 0.6,
            "sound": "ServoDoorsSound"
        },
        # Class: CfgVehicles|Heli_Transport_02_base_F|AnimationSources|AddGunHolder [Indent level: 2],
        "addgunholder": {
            "source": "user",
            "animperiod": 1e-006,
            "initphase": 0
        },
        # Class: CfgVehicles|Heli_Transport_02_base_F|AnimationSources|Gun_HRot [Indent level: 2],
        "gun_hrot": {
            "source": "user",
            "animperiod": 1e-006,
            "initphase": 0
        },
        # Class: CfgVehicles|Heli_Transport_02_base_F|AnimationSources|Gun_VRot [Indent level: 2],
        "gun_vrot": {
            "source": "user",
            "animperiod": 1e-006,
            "initphase": 0
        },
        # Class: CfgVehicles|Heli_Transport_02_base_F|AnimationSources|HitGlass16 [Indent level: 2],
        "hitglass16": {
            "raw": 1,
            "source": "hit",
            "hitpoint": "HitGlass16"
        },
        # Class: CfgVehicles|Heli_Transport_02_base_F|AnimationSources|HitGlass17 [Indent level: 2],
        "hitglass17": {
            "raw": 1,
            "source": "hit",
            "hitpoint": "HitGlass17"
        },
        # Class: CfgVehicles|Helicopter_Base_H|AnimationSources|AddCargoHook [Indent level: 2],
        "addcargohook": {
            "source": "user",
            "animperiod": 1e-007,
            "initphase": 0,
            "iscomponent": 1
        },
        # Class: CfgVehicles|Helicopter_Base_H|AnimationSources|AddCargoHook_COver [Indent level: 2],
        "addcargohook_cover": {
            "source": "user",
            "animperiod": 1e-007,
            "initphase": 1,
            "iscomponent": 1
        },
        # Class: CfgVehicles|Helicopter_Base_H|AnimationSources|HitHRotor [Indent level: 2],
        "hithrotor": {
            "source": "hit",
            "hitpoint": "HitHRotor",
            "raw": 1
        },
        # Class: CfgVehicles|Helicopter_Base_H|AnimationSources|HitVRotor [Indent level: 2],
        "hitvrotor": {
            "source": "hit",
            "hitpoint": "HitVRotor",
            "raw": 1
        },
        # Class: CfgVehicles|Helicopter_Base_H|AnimationSources|HitEngine [Indent level: 2],
        "hitengine": {
            "source": "hit",
            "hitpoint": "HitEngine",
            "raw": 1
        },
        # Class: CfgVehicles|Helicopter_Base_H|AnimationSources|HitEngine2 [Indent level: 2],
        "hitengine2": {
            "source": "hit",
            "hitpoint": "HitEngine2",
            "raw": 1
        },
        # Class: CfgVehicles|Helicopter_Base_H|AnimationSources|HitBatteries [Indent level: 2],
        "hitbatteries": {
            "source": "hit",
            "hitpoint": "HitBatteries",
            "raw": 1
        },
        # Class: CfgVehicles|Helicopter_Base_H|AnimationSources|HitTransmission [Indent level: 2],
        "hittransmission": {
            "source": "hit",
            "hitpoint": "HitTransmission",
            "raw": 1
        },
        # Class: CfgVehicles|Helicopter_Base_H|AnimationSources|HitHydraulics [Indent level: 2],
        "hithydraulics": {
            "source": "hit",
            "hitpoint": "HitHydraulics",
            "raw": 1
        },
        # Class: CfgVehicles|Helicopter_Base_H|AnimationSources|HitFuel [Indent level: 2],
        "hitfuel": {
            "source": "hit",
            "hitpoint": "HitFuel",
            "raw": 1
        },
        # Class: CfgVehicles|Helicopter|AnimationSources|HitEngine1 [Indent level: 2],
        "hitengine1": {
            "source": "hit",
            "hitpoint": "HitEngine1",
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
    # Class: CfgVehicles|RHS_CH_47F_cargo_base|Turrets [Indent level: 1],
    "turrets": {
        # Class: CfgVehicles|RHS_CH_47F_cargo_base|Turrets|CopilotTurret [Indent level: 2]
        "copilotturret": {
            "iscopilot": 1,
            "caneject": 0,
            "gunneraction": "RHS_CH47_Pilot",
            "gunnerinaction": "RHS_CH47_Pilot",
            "memorypointsgetingunner": "pos codriver",
            "memorypointsgetingunnerdir": "pos codriver dir",
            "gunnergetinaction": "GetInHeli_Transport_01Cargo",
            "gunnergetoutaction": "GetOutLow",
            "gunnername": "Co-Pilot",
            "precisegetinout": 0,
            "gunnerdoor": "",
            "gunnerlefthandanimname": "lever_copilot",
            "gunnerrighthandanimname": "stick_copilot",
            "gunnerleftleganimname": "",
            "gunnerrightleganimname": "",
            "proxyindex": 4,
            "gunnercompartments": "Compartment3",
            "commanding": -3,
            "selectionfireanim": "",
            # Class: CfgVehicles|RHS_CH_47F_base|Turrets|CopilotTurret|Reflectors [Indent level: 3],
            "reflectors": {
                # Class: CfgVehicles|RHS_CH_47F_base|Turrets|CopilotTurret|Reflectors|cabin [Indent level: 4]
                "cabin": {
                    "color": [830,100,100],
                    "ambient": [5,0,0],
                    "intensity": 9,
                    "size": 1,
                    "innerangle": 90,
                    "outerangle": 165,
                    "conefadecoef": 1,
                    "position": "cabin_light",
                    "direction": "cabin_light_dir",
                    "hitpoint": "cabin_light",
                    "selection": "cabin_light",
                    "useflare": 1,
                    "flaresize": 1,
                    "flaremaxdistance": 5,
                    "daylight": 1,
                    "blinking": 0,
                    # Class: CfgVehicles|RHS_CH_47F_base|Turrets|CopilotTurret|Reflectors|cabin|Attenuation [Indent level: 5],
                    "attenuation": {
                        "start": 0,
                        "constant": 0,
                        "linear": 1,
                        "quadratic": 50,
                        "hardlimitstart": 1,
                        "hardlimitend": 1.5
                    }
                },
                # Class: CfgVehicles|RHS_CH_47F_base|Turrets|CopilotTurret|Reflectors|cargo_light_1 [Indent level: 4],
                "cargo_light_1": {
                    "color": [830,100,100],
                    "position": "cargo_light_1",
                    "direction": "cargo_light_1_dir",
                    "hitpoint": "cargo_light_1",
                    "selection": "cargo_light_1",
                    "intensity": 21,
                    "useflare": 0,
                    "conefadecoef": 0.1,
                    # Class: CfgVehicles|RHS_CH_47F_base|Turrets|CopilotTurret|Reflectors|cargo_light_1|Attenuation [Indent level: 5],
                    "attenuation": {
                        "start": 0,
                        "constant": 0,
                        "linear": 1,
                        "quadratic": 70,
                        "hardlimitstart": 2,
                        "hardlimitend": 2.5
                    },
                    "ambient": [5,0,0],
                    "size": 1,
                    "innerangle": 90,
                    "outerangle": 165,
                    "flaresize": 1,
                    "flaremaxdistance": 5,
                    "daylight": 1,
                    "blinking": 0
                },
                # Class: CfgVehicles|RHS_CH_47F_base|Turrets|CopilotTurret|Reflectors|cargo_light_2 [Indent level: 4],
                "cargo_light_2": {
                    "position": "cargo_light_2",
                    "direction": "cargo_light_2_dir",
                    "hitpoint": "cargo_light_2",
                    "selection": "cargo_light_2",
                    "color": [830,100,100],
                    "intensity": 21,
                    "useflare": 0,
                    "conefadecoef": 0.1,
                    # Class: CfgVehicles|RHS_CH_47F_base|Turrets|CopilotTurret|Reflectors|cargo_light_1|Attenuation [Indent level: 5],
                    "attenuation": {
                        "start": 0,
                        "constant": 0,
                        "linear": 1,
                        "quadratic": 70,
                        "hardlimitstart": 2,
                        "hardlimitend": 2.5
                    },
                    "ambient": [5,0,0],
                    "size": 1,
                    "innerangle": 90,
                    "outerangle": 165,
                    "flaresize": 1,
                    "flaremaxdistance": 5,
                    "daylight": 1,
                    "blinking": 0
                },
                # Class: CfgVehicles|RHS_CH_47F_base|Turrets|CopilotTurret|Reflectors|cargo_light_3 [Indent level: 4],
                "cargo_light_3": {
                    "position": "cargo_light_3",
                    "direction": "cargo_light_3_dir",
                    "hitpoint": "cargo_light_3",
                    "selection": "cargo_light_3",
                    "color": [830,100,100],
                    "intensity": 21,
                    "useflare": 0,
                    "conefadecoef": 0.1,
                    # Class: CfgVehicles|RHS_CH_47F_base|Turrets|CopilotTurret|Reflectors|cargo_light_1|Attenuation [Indent level: 5],
                    "attenuation": {
                        "start": 0,
                        "constant": 0,
                        "linear": 1,
                        "quadratic": 70,
                        "hardlimitstart": 2,
                        "hardlimitend": 2.5
                    },
                    "ambient": [5,0,0],
                    "size": 1,
                    "innerangle": 90,
                    "outerangle": 165,
                    "flaresize": 1,
                    "flaremaxdistance": 5,
                    "daylight": 1,
                    "blinking": 0
                }
            },
            "memorypointsgetingunnerprecise": "GetIn_Turret",
            # Class: CfgVehicles|Heli_Transport_02_base_F|Turrets|CopilotTurret|ViewGunner [Indent level: 3],
            "viewgunner": {
                "initanglex": -9,
                "initfov": 0.9,
                "minfov": 0.25,
                "maxfov": 1.25,
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
            # Class: CfgVehicles|Heli_Transport_02_base_F|Turrets|CopilotTurret|Components [Indent level: 3],
            "components": {
                # Class: CfgVehicles|Heli_Transport_02_base_F|Turrets|CopilotTurret|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 4]
                "vehiclesystemsdisplaymanagercomponentleft": {
                    # Class: VehicleSystemsTemplateLeftPilot|Components [Indent level: 0]
                    "components": {
                        # Class: VehicleSystemsTemplateLeftPilot|Components|EmptyDisplay [Indent level: 1]
                        "emptydisplay": {
                            "componenttype": "EmptyDisplayComponent"
                        },
                        # Class: VehicleSystemsTemplateLeftPilot|Components|MinimapDisplay [Indent level: 1],
                        "minimapdisplay": {
                            "componenttype": "MinimapDisplayComponent",
                            "resource": "RscCustomInfoAirborneMiniMap"
                        },
                        # Class: VehicleSystemsTemplateLeftPilot|Components|CrewDisplay [Indent level: 1],
                        "crewdisplay": {
                            "componenttype": "CrewDisplayComponent",
                            "resource": "RscCustomInfoCrew"
                        },
                        # Class: VehicleSystemsTemplateLeftPilot|Components|SlingLoadDisplay [Indent level: 1],
                        "slingloaddisplay": {
                            "componenttype": "SlingLoadDisplayComponent",
                            "resource": "RscCustomInfoSlingLoad"
                        },
                        # Class: VehicleSystemsTemplateLeftPilot|Components|UAVDisplay [Indent level: 1],
                        "uavdisplay": {
                            "componenttype": "UAVFeedDisplayComponent"
                        },
                        # Class: VehicleSystemsTemplateLeftPilot|Components|VehicleDriverDisplay [Indent level: 1],
                        "vehicledriverdisplay": {
                            "componenttype": "TransportFeedDisplayComponent",
                            "source": "Driver"
                        },
                        # Class: VehicleSystemsTemplateLeftPilot|Components|SensorDisplay [Indent level: 1],
                        "sensordisplay": {
                            "componenttype": "SensorsDisplayComponent",
                            "range": [4000,2000,16000,8000],
                            "resource": "RscCustomInfoSensors"
                        }
                    },
                    "componenttype": "VehicleSystemsDisplayManager",
                    "left": 1,
                    "defaultdisplay": "EmptyDisplay",
                    "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,	(safezoneX + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40))])",
                    "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                },
                # Class: CfgVehicles|Heli_Transport_02_base_F|Turrets|CopilotTurret|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 4],
                "vehiclesystemsdisplaymanagercomponentright": {
                    "defaultdisplay": "SensorDisplay",
                    # Class: VehicleSystemsTemplateRightPilot|Components [Indent level: 0],
                    "components": {
                        # Class: VehicleSystemsTemplateRightPilot|Components|EmptyDisplay [Indent level: 1]
                        "emptydisplay": {
                            "componenttype": "EmptyDisplayComponent"
                        },
                        # Class: VehicleSystemsTemplateRightPilot|Components|MinimapDisplay [Indent level: 1],
                        "minimapdisplay": {
                            "componenttype": "MinimapDisplayComponent",
                            "resource": "RscCustomInfoAirborneMiniMap"
                        },
                        # Class: VehicleSystemsTemplateRightPilot|Components|CrewDisplay [Indent level: 1],
                        "crewdisplay": {
                            "componenttype": "CrewDisplayComponent",
                            "resource": "RscCustomInfoCrew"
                        },
                        # Class: VehicleSystemsTemplateRightPilot|Components|SlingLoadDisplay [Indent level: 1],
                        "slingloaddisplay": {
                            "componenttype": "SlingLoadDisplayComponent",
                            "resource": "RscCustomInfoSlingLoad"
                        },
                        # Class: VehicleSystemsTemplateRightPilot|Components|UAVDisplay [Indent level: 1],
                        "uavdisplay": {
                            "componenttype": "UAVFeedDisplayComponent"
                        },
                        # Class: VehicleSystemsTemplateRightPilot|Components|VehicleDriverDisplay [Indent level: 1],
                        "vehicledriverdisplay": {
                            "componenttype": "TransportFeedDisplayComponent",
                            "source": "Driver"
                        },
                        # Class: VehicleSystemsTemplateRightPilot|Components|SensorDisplay [Indent level: 1],
                        "sensordisplay": {
                            "componenttype": "SensorsDisplayComponent",
                            "range": [4000,2000,16000,8000],
                            "resource": "RscCustomInfoSensors"
                        }
                    },
                    "componenttype": "VehicleSystemsDisplayManager",
                    "right": 1,
                    "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,	((safezoneX + safezoneW) - (		(10 * 			(			((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40)))])",
                    "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                }
            },
            "primarygunner": 0,
            "body": "",
            "gun": "",
            "animationsourcebody": "",
            "animationsourcegun": "",
            "weapons": [],
            "magazines": [],
            "gunnernotspawned": 1,
            "minelev": -50,
            "maxelev": 30,
            "initelev": 11,
            "minturn": -170,
            "maxturn": 170,
            "initturn": 0,
            "maxhorizontalrotspeed": 3,
            "maxverticalrotspeed": 3,
            "turretcansee": "1 + 2 + 4 + 8 + 32",
            "gunneropticsmodel": "",
            # Class: CfgVehicles|Helicopter|Turrets|MainTurret|TurretSpec [Indent level: 3],
            "turretspec": {
                "showheadphones": 1
            },
            "startengine": 0,
            "outgunnermayfire": 1,
            "memorypointgun": "machinegun",
            "memorypointgunneroptics": "gunnerview",
            "castgunnershadow": 1,
            "viewgunnershadow": 1,
            "gunnerforceoptics": 0,
            "enablemanualfire": 0,
            # Class: CfgVehicles|Helicopter|Turrets|MainTurret|HitPoints [Indent level: 3],
            "hitpoints": {
                # Class: CfgVehicles|Helicopter|Turrets|MainTurret|HitPoints|HitTurret [Indent level: 4]
                "hitturret": {
                    "armor": 0.2,
                    "material": 51,
                    "name": "vez",
                    "visual": "vez",
                    "passthrough": 0.3
                },
                # Class: CfgVehicles|Helicopter|Turrets|MainTurret|HitPoints|HitGun [Indent level: 4],
                "hitgun": {
                    "armor": 0.2,
                    "material": 51,
                    "name": "zbran",
                    "visual": "zbran",
                    "passthrough": 0.1
                }
            },
            "animationsourcehatch": "hatchGunner",
            "animationsourcecamelev": "camElev",
            "proxytype": "CPGunner",
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
            "lodturnedin": -1,
            "lodturnedout": -1,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "armorlights": 0.4,
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
        # Class: CfgVehicles|RHS_CH_47F_cargo_base|Turrets|MainTurret [Indent level: 2],
        "mainturret": {
            "iscopilot": 0,
            "body": "mainTurret",
            "gun": "mainGun",
            "minelev": -30,
            "maxelev": 30,
            "initelev": -10,
            "minturn": 36,
            "maxturn": 140,
            "initturn": 0,
            "soundservo": ["",0.01,1],
            "memorypointgunneroptics": "gunnerview",
            "memorypointgun": "machinegun_1",
            "animationsourcehatch": "",
            "stabilizedinaxes": "StabilizedInAxesNone",
            "selectionfireanim": "zasleh",
            "animationsourcebody": "MainTurret",
            "animationsourcegun": "MainGun",
            "gunbeg": "muzzle_1",
            "gunend": "chamber_1",
            "weapons": ["rhs_weap_m134_minigun_1"],
            "magazines": ["rhs_mag_762x51_m80a1_4000"],
            "gunnername": "Crew Chief",
            "gunneropticsmodel": "A3|weapons_f|reticle|optics_empty",
            "gunneroutopticsshowcursor": 1,
            "gunneropticsshowcursor": 1,
            "gunneraction": "RHS_CH47_Gunner",
            "gunnerinaction": "RHS_CH47_Gunner",
            "gunnerlefthandanimname": "OtocHlaven",
            "gunnerrighthandanimname": "OtocHlaven",
            "gunnerleftleganimname": "gunner1_leg_left",
            "gunnerrightleganimname": "gunner1_leg_right",
            "animationsourcestickx": "MainTurret_1_Inertia",
            "animationsourcesticky": "MainGun_1_Inertia",
            "gunnerforceoptics": 0,
            "commanding": -1,
            "primarygunner": 1,
            "outgunnermayfire": 1,
            # Class: CfgVehicles|RHS_CH_47F_base|Turrets|MainTurret|ViewOptics [Indent level: 3],
            "viewoptics": {
                "initanglex": 0,
                "minanglex": -30,
                "maxanglex": 30,
                "initangley": 0,
                "minangley": -100,
                "maxangley": 100,
                "initfov": 0.7,
                "minfov": 0.25,
                "maxfov": 1.1
            },
            "gunnercompartments": "Compartment2",
            "memorypointsgetingunner": "pos gunner",
            "memorypointsgetingunnerdir": "pos gunner dir",
            # Class: CfgVehicles|RHS_CH_47F_base|Turrets|MainTurret|Components [Indent level: 3],
            "components": {
                # Class: CfgVehicles|RHS_CH_47F_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 4]
                "vehiclesystemsdisplaymanagercomponentleft": {
                    # Class: CfgVehicles|RHS_CH_47F_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft|Components [Indent level: 5]
                    "components": {
                        # Class: CfgVehicles|RHS_CH_47F_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft|Components|EmptyDisplay [Indent level: 6]
                        "emptydisplay": {
                            "componenttype": "EmptyDisplayComponent"
                        },
                        # Class: CfgVehicles|RHS_CH_47F_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft|Components|CrewDisplay [Indent level: 6],
                        "crewdisplay": {
                            "componenttype": "CrewDisplayComponent",
                            "resource": "RscCustomInfoCrew"
                        }
                    },
                    "componenttype": "VehicleSystemsDisplayManager",
                    "left": 1,
                    "defaultdisplay": "EmptyDisplay",
                    "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,	(safezoneX + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40))])",
                    "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                },
                # Class: CfgVehicles|RHS_CH_47F_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 4],
                "vehiclesystemsdisplaymanagercomponentright": {
                    "defaultdisplay": "SensorDisplay",
                    # Class: CfgVehicles|RHS_CH_47F_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight|Components [Indent level: 5],
                    "components": {
                        # Class: CfgVehicles|RHS_CH_47F_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight|Components|EmptyDisplay [Indent level: 6]
                        "emptydisplay": {
                            "componenttype": "EmptyDisplayComponent"
                        },
                        # Class: CfgVehicles|RHS_CH_47F_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight|Components|CrewDisplay [Indent level: 6],
                        "crewdisplay": {
                            "componenttype": "CrewDisplayComponent",
                            "resource": "RscCustomInfoCrew"
                        }
                    },
                    "componenttype": "VehicleSystemsDisplayManager",
                    "right": 1,
                    "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,	((safezoneX + safezoneW) - (		(10 * 			(			((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40)))])",
                    "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                }
            },
            # Class: CfgVehicles|RHS_CH_47F_base|Turrets|MainTurret|Hitpoints [Indent level: 3],
            "hitpoints": {
            },
            "turretcansee": "1 + 2 + 4 + 8 + 32",
            # Class: CfgVehicles|Helicopter|Turrets|MainTurret|TurretSpec [Indent level: 3],
            "turretspec": {
                "showheadphones": 1
            },
            "startengine": 0,
            "gunnergetinaction": "GetInLow",
            "gunnergetoutaction": "GetOutLow",
            "castgunnershadow": 1,
            "viewgunnershadow": 1,
            "enablemanualfire": 0,
            "caneject": 0,
            "animationsourcecamelev": "camElev",
            "proxytype": "CPGunner",
            "proxyindex": 1,
            "gunnertype": "",
            "primaryobserver": 0,
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
            "gunneropticscolor": [0,0,0,1],
            "turretinfotype": "",
            "gunneroutopticsmodel": "",
            "gunneroutopticscolor": [0,0,0,1],
            "gunneropticseffect": [],
            "gunneroutopticseffect": [],
            "memorypointgunneroutoptics": "",
            "gunneroutforceoptics": 0,
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
            "showcrewaim": 0
        },
        # Class: CfgVehicles|RHS_CH_47F_cargo_base|Turrets|RightDoorGun [Indent level: 2],
        "rightdoorgun": {
            "iscopilot": 0,
            "body": "Turret2",
            "gun": "Gun_2",
            "minturn": -140,
            "maxturn": -36,
            "initturn": 0,
            "animationsourcebody": "Turret_2",
            "animationsourcegun": "Gun_2",
            "stabilizedinaxes": "StabilizedInAxesNone",
            "selectionfireanim": "zasleh_1",
            "proxyindex": 2,
            "weapons": ["rhs_weap_m134_minigun_2"],
            "magazines": ["rhs_mag_762x51_m80a1_4000"],
            "gunneropticsmodel": "A3|weapons_f|reticle|optics_empty",
            "gunneroutopticsshowcursor": 1,
            "gunneropticsshowcursor": 1,
            "gunnername": "Door Gunner",
            "gunnerlefthandanimname": "otochlaven_2",
            "gunnerrighthandanimname": "otochlaven_2",
            "gunnerleftleganimname": "gunner2_leg_left",
            "gunnerrightleganimname": "gunner2_leg_right",
            "animationsourcestickx": "MainTurret_2_inertia",
            "animationsourcesticky": "MainGun_2_Inertia",
            "commanding": -2,
            "gunbeg": "muzzle_2",
            "gunend": "chamber_2",
            "primarygunner": 0,
            "precisegetinout": 1,
            "memorypointgun": "machinegun_2",
            "memorypointgunneroptics": "gunnerview_2",
            "gunnercompartments": "Compartment2",
            "memorypointsgetingunner": "pos gunner",
            "memorypointsgetingunnerdir": "pos gunner dir",
            "minelev": -30,
            "maxelev": 30,
            "initelev": -10,
            "soundservo": ["",0.01,1],
            "animationsourcehatch": "",
            "gunneraction": "RHS_CH47_Gunner",
            "gunnerinaction": "RHS_CH47_Gunner",
            "gunnerforceoptics": 0,
            "outgunnermayfire": 1,
            # Class: CfgVehicles|RHS_CH_47F_base|Turrets|MainTurret|ViewOptics [Indent level: 3],
            "viewoptics": {
                "initanglex": 0,
                "minanglex": -30,
                "maxanglex": 30,
                "initangley": 0,
                "minangley": -100,
                "maxangley": 100,
                "initfov": 0.7,
                "minfov": 0.25,
                "maxfov": 1.1
            },
            # Class: CfgVehicles|RHS_CH_47F_base|Turrets|MainTurret|Components [Indent level: 3],
            "components": {
                # Class: CfgVehicles|RHS_CH_47F_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 4]
                "vehiclesystemsdisplaymanagercomponentleft": {
                    # Class: CfgVehicles|RHS_CH_47F_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft|Components [Indent level: 5]
                    "components": {
                        # Class: CfgVehicles|RHS_CH_47F_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft|Components|EmptyDisplay [Indent level: 6]
                        "emptydisplay": {
                            "componenttype": "EmptyDisplayComponent"
                        },
                        # Class: CfgVehicles|RHS_CH_47F_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft|Components|CrewDisplay [Indent level: 6],
                        "crewdisplay": {
                            "componenttype": "CrewDisplayComponent",
                            "resource": "RscCustomInfoCrew"
                        }
                    },
                    "componenttype": "VehicleSystemsDisplayManager",
                    "left": 1,
                    "defaultdisplay": "EmptyDisplay",
                    "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,	(safezoneX + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40))])",
                    "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                },
                # Class: CfgVehicles|RHS_CH_47F_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 4],
                "vehiclesystemsdisplaymanagercomponentright": {
                    "defaultdisplay": "SensorDisplay",
                    # Class: CfgVehicles|RHS_CH_47F_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight|Components [Indent level: 5],
                    "components": {
                        # Class: CfgVehicles|RHS_CH_47F_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight|Components|EmptyDisplay [Indent level: 6]
                        "emptydisplay": {
                            "componenttype": "EmptyDisplayComponent"
                        },
                        # Class: CfgVehicles|RHS_CH_47F_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight|Components|CrewDisplay [Indent level: 6],
                        "crewdisplay": {
                            "componenttype": "CrewDisplayComponent",
                            "resource": "RscCustomInfoCrew"
                        }
                    },
                    "componenttype": "VehicleSystemsDisplayManager",
                    "right": 1,
                    "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,	((safezoneX + safezoneW) - (		(10 * 			(			((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40)))])",
                    "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                }
            },
            # Class: CfgVehicles|RHS_CH_47F_base|Turrets|MainTurret|Hitpoints [Indent level: 3],
            "hitpoints": {
            },
            "turretcansee": "1 + 2 + 4 + 8 + 32",
            # Class: CfgVehicles|Helicopter|Turrets|MainTurret|TurretSpec [Indent level: 3],
            "turretspec": {
                "showheadphones": 1
            },
            "startengine": 0,
            "gunnergetinaction": "GetInLow",
            "gunnergetoutaction": "GetOutLow",
            "castgunnershadow": 1,
            "viewgunnershadow": 1,
            "enablemanualfire": 0,
            "caneject": 0,
            "animationsourcecamelev": "camElev",
            "proxytype": "CPGunner",
            "gunnertype": "",
            "primaryobserver": 0,
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
            "gunneropticscolor": [0,0,0,1],
            "turretinfotype": "",
            "gunneroutopticsmodel": "",
            "gunneroutopticscolor": [0,0,0,1],
            "gunneropticseffect": [],
            "gunneroutopticseffect": [],
            "memorypointgunneroutoptics": "",
            "gunneroutforceoptics": 0,
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
            "gunnerdoor": "",
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
            "showcrewaim": 0
        },
        # Class: CfgVehicles|RHS_CH_47F_base|Turrets|CargoTurret_01 [Indent level: 2],
        "cargoturret_01": {
            "weapons": ["rhsusf_weap_DummyLauncher"],
            "gunneraction": "passenger_inside_1",
            "gunnergetinaction": "GetInHeli_Transport_01Cargo",
            "gunnergetoutaction": "RHS_Heli_Cargo_Exit",
            "memorypointsgetingunner": "pos cargo L",
            "memorypointsgetingunnerdir": "pos cargo L dir",
            "gunnername": "Passenger (Left Ramp)",
            "gunnercompartments": "Compartment1",
            "proxyindex": 21,
            "maxelev": 6,
            "minelev": -25,
            "maxturn": -37,
            "minturn": -95,
            "ispersonturret": 1,
            "gunnerusespilotview": 1,
            "gunnerdoor": "Door_Cargo",
            "selectionfireanim": "",
            "playerposition": 2,
            "soundattenuationturret": "HeliAttenuationRamp",
            "disablesoundattenuation": 0,
            "memorypointgunneroptics": "",
            "enabledbyanimationsource": "ramp_anim",
            # Class: CfgVehicles|RHS_CH_47F_base|Turrets|CargoTurret_01|Hitpoints [Indent level: 3],
            "hitpoints": {
            },
            # Class: CfgVehicles|AllVehicles|CargoTurret|ViewGunner [Indent level: 2],
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
            "animationsourcebody": "",
            "animationsourcegun": "",
            "body": "",
            "caneject": 1,
            "commanding": 0,
            "dontcreateai": 1,
            "gun": "",
            "hideweaponsgunner": 0,
            "iscopilot": 0,
            "primarygunner": 0,
            "proxytype": "CPCargo",
            "startengine": 0,
            "turretfollowfreelook": 0,
            "viewgunnerinexternal": 1,
            "outgunnermayfire": 1,
            "showascargo": 1,
            "animationsourcehatch": "hatchGunner",
            "animationsourcecamelev": "camElev",
            "gunnertype": "",
            "primaryobserver": 0,
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
            "precisegetinout": 0,
            "allowtablock": 1,
            "showalltargets": 0,
            "slingloadoperator": 0,
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
            "gunbeg": "usti hlavne",
            "gunend": "konec hlavne",
            "memorypointgun": "kulas",
            "showcrewaim": 0
        },
        # Class: CfgVehicles|RHS_CH_47F_base|Turrets|CargoTurret_02 [Indent level: 2],
        "cargoturret_02": {
            "gunnername": "Passenger (Right Ramp)",
            "memorypointsgetingunner": "pos cargo R",
            "memorypointsgetingunnerdir": "pos cargo R dir",
            "proxyindex": 13,
            "maxturn": 84,
            "minturn": 37,
            "weapons": ["rhsusf_weap_DummyLauncher"],
            "gunneraction": "passenger_inside_1",
            "gunnergetinaction": "GetInHeli_Transport_01Cargo",
            "gunnergetoutaction": "RHS_Heli_Cargo_Exit",
            "gunnercompartments": "Compartment1",
            "maxelev": 6,
            "minelev": -25,
            "ispersonturret": 1,
            "gunnerusespilotview": 1,
            "gunnerdoor": "Door_Cargo",
            "selectionfireanim": "",
            "playerposition": 2,
            "soundattenuationturret": "HeliAttenuationRamp",
            "disablesoundattenuation": 0,
            "memorypointgunneroptics": "",
            "enabledbyanimationsource": "ramp_anim",
            # Class: CfgVehicles|RHS_CH_47F_base|Turrets|CargoTurret_01|Hitpoints [Indent level: 3],
            "hitpoints": {
            },
            # Class: CfgVehicles|AllVehicles|CargoTurret|ViewGunner [Indent level: 2],
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
            "animationsourcebody": "",
            "animationsourcegun": "",
            "body": "",
            "caneject": 1,
            "commanding": 0,
            "dontcreateai": 1,
            "gun": "",
            "hideweaponsgunner": 0,
            "iscopilot": 0,
            "primarygunner": 0,
            "proxytype": "CPCargo",
            "startengine": 0,
            "turretfollowfreelook": 0,
            "viewgunnerinexternal": 1,
            "outgunnermayfire": 1,
            "showascargo": 1,
            "animationsourcehatch": "hatchGunner",
            "animationsourcecamelev": "camElev",
            "gunnertype": "",
            "primaryobserver": 0,
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
            "precisegetinout": 0,
            "allowtablock": 1,
            "showalltargets": 0,
            "slingloadoperator": 0,
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
            "gunbeg": "usti hlavne",
            "gunend": "konec hlavne",
            "memorypointgun": "kulas",
            "showcrewaim": 0
        }
    },
    "transportsoldier": 0,
    # Class: CfgVehicles|RHS_CH_47F_cargo_base|VehicleTransport [Indent level: 1],
    "vehicletransport": {
        # Class: CfgVehicles|RHS_CH_47F_cargo_base|VehicleTransport|Carrier [Indent level: 2]
        "carrier": {
            "cargobaydimensions": ["VTV_limit_1_big","VTV_limit_2_big"],
            "disableheightlimit": 1,
            "maxloadmass": 9000,
            "cargoalignment": ["front","center"],
            "cargospacing": [0.075,0.075,0.075],
            "exits": ["VTV_exit_1"],
            "unloadinginterval": 2,
            "loadingdistance": 15,
            "loadingangle": 60,
            "parachuteclassdefault": "B_Parachute_02_F",
            "parachuteheightlimitdefault": 25
        }
    },
    "rhs_pararamp": "ramp_anim",
    "rhs_paraoff": -8.5,
    "rhs_rampanim": "ramp",
    "rhs_parascript": "rhs_fnc_vehPara",
    "dlc": "RHS_USAF",
    "rhs_hasnoradar": 1,
    "lesh_canbetowed": 1,
    "lesh_towfromfront": 0,
    "lesh_axisoffsettarget": [0,-8,-2.5],
    "lesh_wheeloffset": [0,3],
    "category": "Air",
    "maxomega": 2000,
    "numberphysicalwheels": 4,
    # Class: CfgVehicles|RHS_CH_47F_base|Wheels [Indent level: 1],
    "wheels": {
        "disablewheelswhendestroyed": 1,
        # Class: CfgVehicles|RHS_CH_47F_base|Wheels|Wheel_1_1 [Indent level: 2],
        "wheel_1_1": {
            "steering": 0,
            "side": "left",
            "bonename": "Wheel_1_1_axis_damper",
            "suspforceapppointoffset": "Wheel_1_1_axis",
            "tireforceapppointoffset": "Wheel_1_1_axis",
            "center": "Wheel_1_1_axis",
            "boundary": "Wheel_1_1_bound",
            "susptraveldirection": [0,-1,0],
            "width": 0.565,
            "mass": 15,
            "moi": 0.768,
            "dampingrate": 0.25,
            "dampingratedamaged": 2,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 2000,
            "maxhandbraketorque": 0,
            "maxcompression": 0.14,
            "maxdroop": 0,
            "sprungmass": 2500,
            "springstrength": 12000,
            "springdamperrate": 1280,
            "longitudinalstiffnessperunitgravity": 5000,
            "latstiffx": 2.5,
            "latstiffy": 18,
            "frictionvsslipgraph": [[0,1],[0.5,1],[1,1]]
        },
        # Class: CfgVehicles|RHS_CH_47F_base|Wheels|Wheel_2_1 [Indent level: 2],
        "wheel_2_1": {
            "bonename": "Wheel_2_1_axis_damper",
            "side": "right",
            "suspforceapppointoffset": "Wheel_2_1_axis",
            "tireforceapppointoffset": "Wheel_2_1_axis",
            "center": "Wheel_2_1_axis",
            "boundary": "Wheel_2_1_bound",
            "steering": 0,
            "susptraveldirection": [0,-1,0],
            "width": 0.565,
            "mass": 15,
            "moi": 0.768,
            "dampingrate": 0.25,
            "dampingratedamaged": 2,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 2000,
            "maxhandbraketorque": 0,
            "maxcompression": 0.14,
            "maxdroop": 0,
            "sprungmass": 2500,
            "springstrength": 12000,
            "springdamperrate": 1280,
            "longitudinalstiffnessperunitgravity": 5000,
            "latstiffx": 2.5,
            "latstiffy": 18,
            "frictionvsslipgraph": [[0,1],[0.5,1],[1,1]]
        },
        # Class: CfgVehicles|RHS_CH_47F_base|Wheels|Wheel_1_2 [Indent level: 2],
        "wheel_1_2": {
            "steering": 1,
            "side": "left",
            "bonename": "Wheel_1_2_axis_damper",
            "suspforceapppointoffset": "Wheel_1_2_axis",
            "tireforceapppointoffset": "Wheel_1_2_axis",
            "center": "Wheel_1_2_axis",
            "boundary": "Wheel_1_2_bound",
            "width": 0.21,
            "maxcompression": 0.15,
            "susptraveldirection": [0,-1,0],
            "mass": 15,
            "moi": 0.768,
            "dampingrate": 0.25,
            "dampingratedamaged": 2,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 2000,
            "maxhandbraketorque": 0,
            "maxdroop": 0,
            "sprungmass": 2500,
            "springstrength": 12000,
            "springdamperrate": 1280,
            "longitudinalstiffnessperunitgravity": 5000,
            "latstiffx": 2.5,
            "latstiffy": 18,
            "frictionvsslipgraph": [[0,1],[0.5,1],[1,1]]
        },
        # Class: CfgVehicles|RHS_CH_47F_base|Wheels|Wheel_2_2 [Indent level: 2],
        "wheel_2_2": {
            "bonename": "Wheel_2_2_axis_damper",
            "side": "right",
            "suspforceapppointoffset": "Wheel_2_2_axis",
            "tireforceapppointoffset": "Wheel_2_2_axis",
            "center": "Wheel_2_2_axis",
            "boundary": "Wheel_2_2_bound",
            "steering": 1,
            "width": 0.21,
            "maxcompression": 0.15,
            "susptraveldirection": [0,-1,0],
            "mass": 15,
            "moi": 0.768,
            "dampingrate": 0.25,
            "dampingratedamaged": 2,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 2000,
            "maxhandbraketorque": 0,
            "maxdroop": 0,
            "sprungmass": 2500,
            "springstrength": 12000,
            "springdamperrate": 1280,
            "longitudinalstiffnessperunitgravity": 5000,
            "latstiffx": 2.5,
            "latstiffy": 18,
            "frictionvsslipgraph": [[0,1],[0.5,1],[1,1]]
        }
    },
    "gearretracting": 0,
    "gearuptime": 1,
    "geardowntime": 1,
    "backrotorforcecoef": 0.9,
    "driveoncomponent": ["wheels"],
    "fuelcapacity": 3200,
    "fuelconsumptionrate": 0.398,
    "slingloadmaxcargomass": 12700,
    "canfloat": 1,
    "waterleakiness": 0.02,
    "maxfordingdepth": 1.5,
    "waterresistancecoef": 0.5,
    "waterresistance": 10,
    "waterlineardampingcoefy": 5,
    "waterlineardampingcoefx": 2,
    "waterangulardampingcoef": 5,
    "mainrotorspeed": 1,
    "backrotorspeed": 1,
    "mainbladeradius": 9.15,
    "tailbladeradius": 9.15,
    "tailbladevertical": 0,
    "liftforcecoef": 1.7,
    "cyclicasideforcecoef": 1,
    "cyclicforwardforcecoef": 1,
    "bodyfrictioncoef": 0.9,
    "useroadwayforvehicles": 1,
    # Class: CfgVehicles|RHS_CH_47F_base|RotorLibHelicopterProperties [Indent level: 1],
    "rotorlibhelicopterproperties": {
        "rtdconfig": "rhsusf|addons|rhsusf_c_a2port_air|CH47|Rotorlib_CH47.xml",
        "autohovercorrection": [4.7,3.8,0],
        "defaultcollective": 0.665,
        "retreatbladestallwarningspeed": 92.583,
        "maxtorque": 4014,
        "stressdamagepersec": 0.00333333,
        "maxhorizontalstabilizerleftstress": 10000,
        "maxhorizontalstabilizerrightstress": 10000,
        "maxverticalstabilizerstress": 10000,
        "horizontalwingsanglecollmin": 0,
        "horizontalwingsanglecollmax": 0,
        "maxmainrotorstress": 185000,
        "maxtailrotorstress": 185000
    },
    "availableforsupporttypes": ["Drop","Transport"],
    # Class: CfgVehicles|RHS_CH_47F_base|pilotCamera [Indent level: 1],
    "pilotcamera": {
    },
    "unitinfotype": "RHSUSF_RscUnitInfoAir_CH47",
    "unitinfotypertd": "RHSUSF_RscUnitInfoAirRTDFullDigital",
    "selectionfireanim": "",
    "destrtype": "DestructWreck",
    "side": 1,
    "shownvgcargo": [1],
    "maxspeed": 293,
    "namesound": "veh_helicopter",
    "model": "rhsusf|addons|rhsusf_a2port_air|CH47|CH_47F",
    "picture": "rhsusf|addons|rhsusf_a2port_air|data|ico|rhs_ch47_pic_ca.paa",
    "icon": "rhsusf|addons|rhsusf_a2port_air|data|mapico|Icon_ch47f_CA.paa",
    "mapsize": 25,
    "driveraction": "RHS_CH47_Pilot",
    "driverlefthandanimname": "lever_pilot",
    "driverrighthandanimname": "stick_pilot",
    "memorypointsgetincargo": ["pos cargo"],
    "memorypointsgetincargodir": ["pos cargo dir"],
    "cargoaction": ["RHS_CH47_Cargo01","RHS_CH47_Cargo01","RHS_CH47_Cargo01","RHS_CH47_Cargo02","RHS_CH47_Cargo03","RHS_CH47_Cargo01","RHS_CH47_Cargo03","RHS_CH47_Cargo02","RHS_CH47_Cargo01","RHS_CH47_Cargo03","RHS_CH47_Cargo02","RHS_CH47_Cargo03","RHS_CH47_Cargo02","RHS_CH47_Cargo03","RHS_CH47_Cargo01","RHS_CH47_Cargo02","RHS_CH47_Cargo01","RHS_CH47_Cargo03","RHS_CH47_Cargo02","RHS_CH47_Cargo01","RHS_CH47_Cargo03","RHS_CH47_Cargo02","RHS_CH47_Cargo01","RHS_CH47_Cargo03","RHS_CH47_Cargo02"],
    "cargoiscodriver": [0],
    "cargocompartments": ["Compartment1"],
    "cargoproxyindexes": [1,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19,20,22,23,24,25],
    "getinproxyorder": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25],
    "transportmaxbackpacks": 10,
    "reportownposition": 1,
    "irtarget": 1,
    "irtargetsize": 1.2,
    "visualtarget": 1,
    "visualtargetsize": 1.3,
    "radartarget": 1,
    "radartargetsize": 1.12,
    "radartype": 4,
    "lockdetectionsystem": "8",
    "incomingmissiledetectionsystem": "2 + 8 + 16",
    "armor": 40,
    "armorstructural": 20,
    "hulldamagecauseexplosion": 1,
    "hullexplosiondelay": [10,20],
    "damageresistance": 0.001,
    # Class: CfgVehicles|RHS_CH_47F_base|HitPoints [Indent level: 1],
    "hitpoints": {
        # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitHull [Indent level: 2]
        "hithull": {
            "simulation": "RHS_Hull_Helicopter",
            "armor": -100,
            "minimalhit": -0.2,
            "explosionshielding": 2,
            "radius": 0.4,
            "armorcomponent": "Hit_Hull",
            "name": "hit_hull",
            "visual": "zbytek",
            "passthrough": 1,
            # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitHull|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                # Class: RHS_Effects_Helicopter_Hull_Destruction|RHS_Hull_Smoke [Indent level: 0]
                "rhs_hull_smoke": {
                    "simulation": "particles",
                    "type": "SmallWreckSmoke",
                    "position": "hull_fire_1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: RHS_Effects_Helicopter_Hull_Destruction|RHS_Hull_Fire [Indent level: 0],
                "rhs_hull_fire": {
                    "type": "MediumDestructionFire",
                    "simulation": "particles",
                    "position": "hull_fire_1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: RHS_Effects_Helicopter_Hull_Destruction|RHS_Hull_Sparks [Indent level: 0],
                "rhs_hull_sparks": {
                    "type": "AirFireSparks",
                    "simulation": "particles",
                    "position": "hull_fire_1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: RHS_Effects_Helicopter_Hull_Destruction|RHS_Hull_Sounds [Indent level: 0],
                "rhs_hull_sounds": {
                    "simulation": "sound",
                    "type": "Fire",
                    "position": "hull_fire_1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: RHS_Effects_Helicopter_Hull_Destruction|RHS_Hull_Smoke_small1 [Indent level: 0],
                "rhs_hull_smoke_small1": {
                    "type": "WeaponWreckSmoke",
                    "position": "hull_fire_2",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: RHS_Effects_Helicopter_Hull_Destruction|RHS_Hull_Smoke_small2 [Indent level: 0],
                "rhs_hull_smoke_small2": {
                    "position": "hull_fire_3",
                    "type": "WeaponWreckSmoke",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: RHS_Effects_Helicopter_Hull_Destruction|RHS_Hull_Fire_2 [Indent level: 0],
                "rhs_hull_fire_2": {
                    "type": "MediumDestructionFire",
                    "position": "hull_fire_2",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: RHS_Effects_Helicopter_Hull_Destruction|RHS_Hull_Fire_3 [Indent level: 0],
                "rhs_hull_fire_3": {
                    "type": "MediumDestructionFire",
                    "position": "hull_fire_3",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1
            }
        },
        # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitEngine1 [Indent level: 2],
        "hitengine1": {
            "armor": -80,
            "radius": 0.18,
            "explosionshielding": 0.7,
            "minimalhit": -0.05,
            "passthrough": 0.4,
            "visual": "",
            "name": "engine_1_hit",
            "armorcomponent": "Hit_Engine_1"
        },
        # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitEngine2 [Indent level: 2],
        "hitengine2": {
            "name": "engine_2_hit",
            "armorcomponent": "Hit_Engine_2",
            "armor": -80,
            "radius": 0.18,
            "explosionshielding": 0.7,
            "minimalhit": -0.05,
            "passthrough": 0.4,
            "visual": ""
        },
        # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitEngine [Indent level: 2],
        "hitengine": {
            "armor": -200,
            "armorcomponent": "",
            "name": "engine_hit",
            "depends": "0.5 * (HitEngine1 + HitEngine2)",
            "radius": 0.18,
            "explosionshielding": 0.7,
            "minimalhit": -0.05,
            "passthrough": 0.4,
            "visual": ""
        },
        # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitVRotor [Indent level: 2],
        "hitvrotor": {
            "armor": -80,
            "minimalhit": -0.1,
            "name": "mala vrtule",
            "visual": "mala vrtule staticka",
            "passthrough": 0.5,
            "armorcomponent": "Hit_Rotor_Rear"
        },
        # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitHRotor [Indent level: 2],
        "hithrotor": {
            "armor": -80,
            "minimalhit": -0.1,
            "name": "velka vrtule",
            "visual": "velka vrtule staticka",
            "passthrough": 0.5,
            "armorcomponent": "Hit_Rotor_Main"
        },
        # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass1 [Indent level: 2],
        "hitglass1": {
            "name": "glass1",
            "visual": "glass1",
            "radius": 0.37,
            "armor": -5,
            "explosionshielding": 2,
            "minimalhit": -0.025,
            "passthrough": 0,
            "armorcomponent": "glass1",
            # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass1|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass1|DestructionEffects|BrokenGlass1 [Indent level: 4],
                "brokenglass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass1|DestructionEffects|BrokenGlass2 [Indent level: 4],
                "brokenglass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass1|DestructionEffects|BrokenGlass3 [Indent level: 4],
                "brokenglass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass1|DestructionEffects|BrokenGlass4 [Indent level: 4],
                "brokenglass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass1|DestructionEffects|BrokenGlass5 [Indent level: 4],
                "brokenglass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass1|DestructionEffects|BrokenGlass1S [Indent level: 4],
                "brokenglass1s": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass1|DestructionEffects|BrokenGlass2S [Indent level: 4],
                "brokenglass2s": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass1|DestructionEffects|BrokenGlass3S [Indent level: 4],
                "brokenglass3s": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass1|DestructionEffects|BrokenGlass4S [Indent level: 4],
                "brokenglass4s": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass1|DestructionEffects|BrokenGlass5S [Indent level: 4],
                "brokenglass5s": {
                    "simulation": "particles",
                    "type": "BrokenGlass5SS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                }
            }
        },
        # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass2 [Indent level: 2],
        "hitglass2": {
            "name": "glass2",
            "visual": "glass2",
            "radius": 0.37,
            "armor": -5,
            "explosionshielding": 1.5,
            "minimalhit": -0.025,
            "passthrough": 0,
            "armorcomponent": "glass2",
            # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass2|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass2|DestructionEffects|BrokenGlass1 [Indent level: 4],
                "brokenglass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects2",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass2|DestructionEffects|BrokenGlass2 [Indent level: 4],
                "brokenglass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects2",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass2|DestructionEffects|BrokenGlass3 [Indent level: 4],
                "brokenglass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects2",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass2|DestructionEffects|BrokenGlass4 [Indent level: 4],
                "brokenglass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects2",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass2|DestructionEffects|BrokenGlass5 [Indent level: 4],
                "brokenglass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects2",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass2|DestructionEffects|BrokenGlass1S [Indent level: 4],
                "brokenglass1s": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects2",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass2|DestructionEffects|BrokenGlass2S [Indent level: 4],
                "brokenglass2s": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects2",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass2|DestructionEffects|BrokenGlass3S [Indent level: 4],
                "brokenglass3s": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects2",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass2|DestructionEffects|BrokenGlass4S [Indent level: 4],
                "brokenglass4s": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects2",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass2|DestructionEffects|BrokenGlass5S [Indent level: 4],
                "brokenglass5s": {
                    "simulation": "particles",
                    "type": "BrokenGlass5SS",
                    "position": "GlassEffects2",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                }
            }
        },
        # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass3 [Indent level: 2],
        "hitglass3": {
            "name": "glass3",
            "visual": "glass3",
            "radius": 0.25,
            "armor": -5,
            "explosionshielding": 1.5,
            "minimalhit": -0.025,
            "passthrough": 0,
            "armorcomponent": "glass3",
            # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass3|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass3|DestructionEffects|BrokenGlass1 [Indent level: 4],
                "brokenglass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects3",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass3|DestructionEffects|BrokenGlass2 [Indent level: 4],
                "brokenglass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects3",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass3|DestructionEffects|BrokenGlass3 [Indent level: 4],
                "brokenglass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects3",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass3|DestructionEffects|BrokenGlass4 [Indent level: 4],
                "brokenglass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects3",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass3|DestructionEffects|BrokenGlass5 [Indent level: 4],
                "brokenglass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects3",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass3|DestructionEffects|BrokenGlass1S [Indent level: 4],
                "brokenglass1s": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects3",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass3|DestructionEffects|BrokenGlass2S [Indent level: 4],
                "brokenglass2s": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects3",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass3|DestructionEffects|BrokenGlass3S [Indent level: 4],
                "brokenglass3s": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects3",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass3|DestructionEffects|BrokenGlass4S [Indent level: 4],
                "brokenglass4s": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects3",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass3|DestructionEffects|BrokenGlass5S [Indent level: 4],
                "brokenglass5s": {
                    "simulation": "particles",
                    "type": "BrokenGlass5SS",
                    "position": "GlassEffects3",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                }
            }
        },
        # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass4 [Indent level: 2],
        "hitglass4": {
            "name": "glass4",
            "visual": "glass4",
            "radius": 0.25,
            "armor": -5,
            "explosionshielding": 1.5,
            "minimalhit": -0.025,
            "passthrough": 0,
            "armorcomponent": "glass4",
            # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass4|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass4|DestructionEffects|BrokenGlass1 [Indent level: 4],
                "brokenglass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects4",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass4|DestructionEffects|BrokenGlass2 [Indent level: 4],
                "brokenglass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects4",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass4|DestructionEffects|BrokenGlass3 [Indent level: 4],
                "brokenglass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects4",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass4|DestructionEffects|BrokenGlass4 [Indent level: 4],
                "brokenglass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects4",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass4|DestructionEffects|BrokenGlass5 [Indent level: 4],
                "brokenglass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects4",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass4|DestructionEffects|BrokenGlass1S [Indent level: 4],
                "brokenglass1s": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects4",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass4|DestructionEffects|BrokenGlass2S [Indent level: 4],
                "brokenglass2s": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects4",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass4|DestructionEffects|BrokenGlass3S [Indent level: 4],
                "brokenglass3s": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects4",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass4|DestructionEffects|BrokenGlass4S [Indent level: 4],
                "brokenglass4s": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects4",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass4|DestructionEffects|BrokenGlass5S [Indent level: 4],
                "brokenglass5s": {
                    "simulation": "particles",
                    "type": "BrokenGlass5SS",
                    "position": "GlassEffects4",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                }
            }
        },
        # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass5 [Indent level: 2],
        "hitglass5": {
            "name": "glass5",
            "visual": "glass5",
            "radius": 0.34,
            "armor": -5,
            "explosionshielding": 2,
            "minimalhit": -0.025,
            "passthrough": 0,
            "armorcomponent": "glass5",
            # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass5|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass5|DestructionEffects|BrokenGlass1 [Indent level: 4],
                "brokenglass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects5",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass5|DestructionEffects|BrokenGlass2 [Indent level: 4],
                "brokenglass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects5",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass5|DestructionEffects|BrokenGlass3 [Indent level: 4],
                "brokenglass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects5",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass5|DestructionEffects|BrokenGlass4 [Indent level: 4],
                "brokenglass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects5",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass5|DestructionEffects|BrokenGlass5 [Indent level: 4],
                "brokenglass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects5",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass5|DestructionEffects|BrokenGlass1S [Indent level: 4],
                "brokenglass1s": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects5",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass5|DestructionEffects|BrokenGlass2S [Indent level: 4],
                "brokenglass2s": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects5",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass5|DestructionEffects|BrokenGlass3S [Indent level: 4],
                "brokenglass3s": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects5",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass5|DestructionEffects|BrokenGlass4S [Indent level: 4],
                "brokenglass4s": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects5",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass5|DestructionEffects|BrokenGlass5S [Indent level: 4],
                "brokenglass5s": {
                    "simulation": "particles",
                    "type": "BrokenGlass5SS",
                    "position": "GlassEffects5",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                }
            }
        },
        # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass6 [Indent level: 2],
        "hitglass6": {
            "name": "glass6",
            "visual": "glass6",
            "radius": 0.34,
            "armor": -5,
            "explosionshielding": 1.5,
            "minimalhit": -0.025,
            "passthrough": 0,
            "armorcomponent": "glass6",
            # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass6|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass6|DestructionEffects|BrokenGlass1 [Indent level: 4],
                "brokenglass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects6",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass6|DestructionEffects|BrokenGlass2 [Indent level: 4],
                "brokenglass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects6",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass6|DestructionEffects|BrokenGlass3 [Indent level: 4],
                "brokenglass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects6",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass6|DestructionEffects|BrokenGlass4 [Indent level: 4],
                "brokenglass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects6",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass6|DestructionEffects|BrokenGlass5 [Indent level: 4],
                "brokenglass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects6",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass6|DestructionEffects|BrokenGlass1S [Indent level: 4],
                "brokenglass1s": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects6",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass6|DestructionEffects|BrokenGlass2S [Indent level: 4],
                "brokenglass2s": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects6",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass6|DestructionEffects|BrokenGlass3S [Indent level: 4],
                "brokenglass3s": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects6",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass6|DestructionEffects|BrokenGlass4S [Indent level: 4],
                "brokenglass4s": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects6",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass6|DestructionEffects|BrokenGlass5S [Indent level: 4],
                "brokenglass5s": {
                    "simulation": "particles",
                    "type": "BrokenGlass5SS",
                    "position": "GlassEffects6",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                }
            }
        },
        # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass7 [Indent level: 2],
        "hitglass7": {
            "name": "glass7",
            "visual": "glass7",
            "radius": 0.34,
            "armor": -5,
            "explosionshielding": 1.5,
            "minimalhit": -0.025,
            "passthrough": 0,
            "armorcomponent": "glass7",
            # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass7|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass7|DestructionEffects|BrokenGlass1 [Indent level: 4],
                "brokenglass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects7",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass7|DestructionEffects|BrokenGlass2 [Indent level: 4],
                "brokenglass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects7",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass7|DestructionEffects|BrokenGlass3 [Indent level: 4],
                "brokenglass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects7",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass7|DestructionEffects|BrokenGlass4 [Indent level: 4],
                "brokenglass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects7",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass7|DestructionEffects|BrokenGlass5 [Indent level: 4],
                "brokenglass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects7",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass7|DestructionEffects|BrokenGlass1S [Indent level: 4],
                "brokenglass1s": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects7",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass7|DestructionEffects|BrokenGlass2S [Indent level: 4],
                "brokenglass2s": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects7",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass7|DestructionEffects|BrokenGlass3S [Indent level: 4],
                "brokenglass3s": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects7",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass7|DestructionEffects|BrokenGlass4S [Indent level: 4],
                "brokenglass4s": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects7",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass7|DestructionEffects|BrokenGlass5S [Indent level: 4],
                "brokenglass5s": {
                    "simulation": "particles",
                    "type": "BrokenGlass5SS",
                    "position": "GlassEffects7",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                }
            }
        },
        # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass8 [Indent level: 2],
        "hitglass8": {
            "name": "glass8",
            "visual": "glass8",
            "radius": 0.34,
            "armor": -5,
            "explosionshielding": 1.5,
            "minimalhit": -0.025,
            "passthrough": 0,
            "armorcomponent": "glass8",
            # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass8|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass8|DestructionEffects|BrokenGlass1 [Indent level: 4],
                "brokenglass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects8",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass8|DestructionEffects|BrokenGlass2 [Indent level: 4],
                "brokenglass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects8",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass8|DestructionEffects|BrokenGlass3 [Indent level: 4],
                "brokenglass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects8",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass8|DestructionEffects|BrokenGlass4 [Indent level: 4],
                "brokenglass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects8",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass8|DestructionEffects|BrokenGlass5 [Indent level: 4],
                "brokenglass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects8",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass8|DestructionEffects|BrokenGlass1S [Indent level: 4],
                "brokenglass1s": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects8",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass8|DestructionEffects|BrokenGlass2S [Indent level: 4],
                "brokenglass2s": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects8",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass8|DestructionEffects|BrokenGlass3S [Indent level: 4],
                "brokenglass3s": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects8",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass8|DestructionEffects|BrokenGlass4S [Indent level: 4],
                "brokenglass4s": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects8",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass8|DestructionEffects|BrokenGlass5S [Indent level: 4],
                "brokenglass5s": {
                    "simulation": "particles",
                    "type": "BrokenGlass5SS",
                    "position": "GlassEffects8",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                }
            }
        },
        # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass9 [Indent level: 2],
        "hitglass9": {
            "name": "glass9",
            "visual": "glass9",
            "radius": 0.24,
            "armor": -5,
            "explosionshielding": 1,
            "minimalhit": -0.025,
            "passthrough": 0,
            "armorcomponent": "glass9",
            # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass9|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass9|DestructionEffects|BrokenGlass1 [Indent level: 4],
                "brokenglass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects9",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass9|DestructionEffects|BrokenGlass2 [Indent level: 4],
                "brokenglass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects9",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass9|DestructionEffects|BrokenGlass3 [Indent level: 4],
                "brokenglass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects9",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass9|DestructionEffects|BrokenGlass4 [Indent level: 4],
                "brokenglass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects9",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass9|DestructionEffects|BrokenGlass5 [Indent level: 4],
                "brokenglass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects9",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass9|DestructionEffects|BrokenGlass1S [Indent level: 4],
                "brokenglass1s": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects9",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass9|DestructionEffects|BrokenGlass2S [Indent level: 4],
                "brokenglass2s": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects9",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass9|DestructionEffects|BrokenGlass3S [Indent level: 4],
                "brokenglass3s": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects9",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass9|DestructionEffects|BrokenGlass4S [Indent level: 4],
                "brokenglass4s": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects9",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass9|DestructionEffects|BrokenGlass5S [Indent level: 4],
                "brokenglass5s": {
                    "simulation": "particles",
                    "type": "BrokenGlass5SS",
                    "position": "GlassEffects9",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                }
            }
        },
        # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass10 [Indent level: 2],
        "hitglass10": {
            "name": "glass10",
            "visual": "glass10",
            "radius": 0.24,
            "armor": -5,
            "explosionshielding": 1,
            "minimalhit": -0.025,
            "passthrough": 0,
            "armorcomponent": "glass10",
            # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass10|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass10|DestructionEffects|BrokenGlass1 [Indent level: 4],
                "brokenglass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects10",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass10|DestructionEffects|BrokenGlass2 [Indent level: 4],
                "brokenglass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects10",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass10|DestructionEffects|BrokenGlass3 [Indent level: 4],
                "brokenglass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects10",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass10|DestructionEffects|BrokenGlass4 [Indent level: 4],
                "brokenglass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects10",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass10|DestructionEffects|BrokenGlass5 [Indent level: 4],
                "brokenglass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects10",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass10|DestructionEffects|BrokenGlass1S [Indent level: 4],
                "brokenglass1s": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects10",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass10|DestructionEffects|BrokenGlass2S [Indent level: 4],
                "brokenglass2s": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects10",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass10|DestructionEffects|BrokenGlass3S [Indent level: 4],
                "brokenglass3s": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects10",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass10|DestructionEffects|BrokenGlass4S [Indent level: 4],
                "brokenglass4s": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects10",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass10|DestructionEffects|BrokenGlass5S [Indent level: 4],
                "brokenglass5s": {
                    "simulation": "particles",
                    "type": "BrokenGlass5SS",
                    "position": "GlassEffects10",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                }
            }
        },
        # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass11 [Indent level: 2],
        "hitglass11": {
            "name": "glass11",
            "visual": "glass11",
            "radius": 0.24,
            "armor": -5,
            "explosionshielding": 1,
            "minimalhit": -0.025,
            "passthrough": 0,
            "armorcomponent": "glass11",
            # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass11|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass11|DestructionEffects|BrokenGlass1 [Indent level: 4],
                "brokenglass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects11",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass11|DestructionEffects|BrokenGlass2 [Indent level: 4],
                "brokenglass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects11",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass11|DestructionEffects|BrokenGlass3 [Indent level: 4],
                "brokenglass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects11",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass11|DestructionEffects|BrokenGlass4 [Indent level: 4],
                "brokenglass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects11",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass11|DestructionEffects|BrokenGlass5 [Indent level: 4],
                "brokenglass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects11",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass11|DestructionEffects|BrokenGlass1S [Indent level: 4],
                "brokenglass1s": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects11",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass11|DestructionEffects|BrokenGlass2S [Indent level: 4],
                "brokenglass2s": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects11",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass11|DestructionEffects|BrokenGlass3S [Indent level: 4],
                "brokenglass3s": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects11",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass11|DestructionEffects|BrokenGlass4S [Indent level: 4],
                "brokenglass4s": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects11",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass11|DestructionEffects|BrokenGlass5S [Indent level: 4],
                "brokenglass5s": {
                    "simulation": "particles",
                    "type": "BrokenGlass5SS",
                    "position": "GlassEffects11",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                }
            }
        },
        # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass12 [Indent level: 2],
        "hitglass12": {
            "name": "glass12",
            "visual": "glass12",
            "radius": 0.24,
            "armor": -5,
            "explosionshielding": 1,
            "minimalhit": -0.025,
            "passthrough": 0,
            "armorcomponent": "glass12",
            # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass12|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass12|DestructionEffects|BrokenGlass1 [Indent level: 4],
                "brokenglass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects12",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass12|DestructionEffects|BrokenGlass2 [Indent level: 4],
                "brokenglass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects12",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass12|DestructionEffects|BrokenGlass3 [Indent level: 4],
                "brokenglass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects12",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass12|DestructionEffects|BrokenGlass4 [Indent level: 4],
                "brokenglass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects12",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass12|DestructionEffects|BrokenGlass5 [Indent level: 4],
                "brokenglass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects12",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass12|DestructionEffects|BrokenGlass1S [Indent level: 4],
                "brokenglass1s": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects12",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass12|DestructionEffects|BrokenGlass2S [Indent level: 4],
                "brokenglass2s": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects12",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass12|DestructionEffects|BrokenGlass3S [Indent level: 4],
                "brokenglass3s": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects12",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass12|DestructionEffects|BrokenGlass4S [Indent level: 4],
                "brokenglass4s": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects12",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass12|DestructionEffects|BrokenGlass5S [Indent level: 4],
                "brokenglass5s": {
                    "simulation": "particles",
                    "type": "BrokenGlass5SS",
                    "position": "GlassEffects12",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                }
            }
        },
        # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass13 [Indent level: 2],
        "hitglass13": {
            "name": "glass13",
            "visual": "glass13",
            "radius": 0.24,
            "armor": -5,
            "explosionshielding": 1,
            "minimalhit": -0.025,
            "passthrough": 0,
            "armorcomponent": "glass13",
            # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass13|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass13|DestructionEffects|BrokenGlass1 [Indent level: 4],
                "brokenglass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects13",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass13|DestructionEffects|BrokenGlass2 [Indent level: 4],
                "brokenglass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects13",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass13|DestructionEffects|BrokenGlass3 [Indent level: 4],
                "brokenglass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects13",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass13|DestructionEffects|BrokenGlass4 [Indent level: 4],
                "brokenglass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects13",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass13|DestructionEffects|BrokenGlass5 [Indent level: 4],
                "brokenglass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects13",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass13|DestructionEffects|BrokenGlass1S [Indent level: 4],
                "brokenglass1s": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects13",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass13|DestructionEffects|BrokenGlass2S [Indent level: 4],
                "brokenglass2s": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects13",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass13|DestructionEffects|BrokenGlass3S [Indent level: 4],
                "brokenglass3s": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects13",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass13|DestructionEffects|BrokenGlass4S [Indent level: 4],
                "brokenglass4s": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects13",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass13|DestructionEffects|BrokenGlass5S [Indent level: 4],
                "brokenglass5s": {
                    "simulation": "particles",
                    "type": "BrokenGlass5SS",
                    "position": "GlassEffects13",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                }
            }
        },
        # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass14 [Indent level: 2],
        "hitglass14": {
            "name": "glass14",
            "visual": "glass14",
            "radius": 0.24,
            "armor": -5,
            "explosionshielding": 1,
            "minimalhit": -0.025,
            "passthrough": 0,
            "armorcomponent": "glass14",
            # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass14|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass14|DestructionEffects|BrokenGlass1 [Indent level: 4],
                "brokenglass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects14",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass14|DestructionEffects|BrokenGlass2 [Indent level: 4],
                "brokenglass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects14",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass14|DestructionEffects|BrokenGlass3 [Indent level: 4],
                "brokenglass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects14",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass14|DestructionEffects|BrokenGlass4 [Indent level: 4],
                "brokenglass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects14",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass14|DestructionEffects|BrokenGlass5 [Indent level: 4],
                "brokenglass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects14",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass14|DestructionEffects|BrokenGlass1S [Indent level: 4],
                "brokenglass1s": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects14",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass14|DestructionEffects|BrokenGlass2S [Indent level: 4],
                "brokenglass2s": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects14",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass14|DestructionEffects|BrokenGlass3S [Indent level: 4],
                "brokenglass3s": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects14",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass14|DestructionEffects|BrokenGlass4S [Indent level: 4],
                "brokenglass4s": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects14",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass14|DestructionEffects|BrokenGlass5S [Indent level: 4],
                "brokenglass5s": {
                    "simulation": "particles",
                    "type": "BrokenGlass5SS",
                    "position": "GlassEffects14",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                }
            }
        },
        # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass15 [Indent level: 2],
        "hitglass15": {
            "name": "glass15",
            "visual": "glass15",
            "radius": 0.24,
            "armor": -5,
            "explosionshielding": 1,
            "minimalhit": -0.025,
            "passthrough": 0,
            "armorcomponent": "glass15",
            # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass15|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass15|DestructionEffects|BrokenGlass1 [Indent level: 4],
                "brokenglass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects15",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass15|DestructionEffects|BrokenGlass2 [Indent level: 4],
                "brokenglass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects15",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass15|DestructionEffects|BrokenGlass3 [Indent level: 4],
                "brokenglass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects15",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass15|DestructionEffects|BrokenGlass4 [Indent level: 4],
                "brokenglass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects15",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass15|DestructionEffects|BrokenGlass5 [Indent level: 4],
                "brokenglass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects15",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass15|DestructionEffects|BrokenGlass1S [Indent level: 4],
                "brokenglass1s": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects15",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass15|DestructionEffects|BrokenGlass2S [Indent level: 4],
                "brokenglass2s": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects15",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass15|DestructionEffects|BrokenGlass3S [Indent level: 4],
                "brokenglass3s": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects15",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass15|DestructionEffects|BrokenGlass4S [Indent level: 4],
                "brokenglass4s": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects15",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_CH_47F_base|HitPoints|HitGlass15|DestructionEffects|BrokenGlass5S [Indent level: 4],
                "brokenglass5s": {
                    "simulation": "particles",
                    "type": "BrokenGlass5SS",
                    "position": "GlassEffects15",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                }
            }
        },
        # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitFuel [Indent level: 2],
        "hitfuel": {
            "armor": 0.7,
            "radius": 0.125,
            "minimalhit": 0.05,
            "explosionshielding": 2,
            "name": "fuel_hit",
            "convexcomponent": "fuel_hit",
            "visual": "zbytek",
            "material": 51,
            "passthrough": 1
        },
        # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitAvionics [Indent level: 2],
        "hitavionics": {
            "armor": 1.3,
            "radius": 0.25,
            "minimalhit": 0.05,
            "explosionshielding": 1.5,
            "visual": "podsvit pristroju",
            "name": "avionics_hit",
            "convexcomponent": "avionics_hit",
            "material": 51,
            "passthrough": 1
        },
        # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass1A [Indent level: 2],
        "hitglass1a": {
            "armor": 999,
            "depends": "HitGlass1",
            # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass1A|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass1A|DestructionEffects|BrokenGlass1 [Indent level: 4],
                "brokenglass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects1A",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass1A|DestructionEffects|BrokenGlass2 [Indent level: 4],
                "brokenglass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects1A",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass1A|DestructionEffects|BrokenGlass3 [Indent level: 4],
                "brokenglass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects1A",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass1A|DestructionEffects|BrokenGlass4 [Indent level: 4],
                "brokenglass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects1A",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass1A|DestructionEffects|BrokenGlass5 [Indent level: 4],
                "brokenglass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects1A",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass1A|DestructionEffects|BrokenGlass1S [Indent level: 4],
                "brokenglass1s": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects1A",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass1A|DestructionEffects|BrokenGlass2S [Indent level: 4],
                "brokenglass2s": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects1A",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass1A|DestructionEffects|BrokenGlass3S [Indent level: 4],
                "brokenglass3s": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects1A",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass1A|DestructionEffects|BrokenGlass4S [Indent level: 4],
                "brokenglass4s": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects1A",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass1A|DestructionEffects|BrokenGlass5S [Indent level: 4],
                "brokenglass5s": {
                    "simulation": "particles",
                    "type": "BrokenGlass5SS",
                    "position": "GlassEffects1A",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                }
            },
            "name": "glass1",
            "visual": "glass1",
            "radius": 0.37,
            "explosionshielding": 2,
            "minimalhit": 0.025,
            "passthrough": 0
        },
        # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass1B [Indent level: 2],
        "hitglass1b": {
            "armor": 999,
            "depends": "HitGlass1",
            # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass1B|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass1B|DestructionEffects|BrokenGlass1 [Indent level: 4],
                "brokenglass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects1B",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass1B|DestructionEffects|BrokenGlass2 [Indent level: 4],
                "brokenglass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects1B",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass1B|DestructionEffects|BrokenGlass3 [Indent level: 4],
                "brokenglass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects1B",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass1B|DestructionEffects|BrokenGlass4 [Indent level: 4],
                "brokenglass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects1B",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass1B|DestructionEffects|BrokenGlass5 [Indent level: 4],
                "brokenglass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects1B",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass1B|DestructionEffects|BrokenGlass1S [Indent level: 4],
                "brokenglass1s": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects1B",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass1B|DestructionEffects|BrokenGlass2S [Indent level: 4],
                "brokenglass2s": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects1B",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass1B|DestructionEffects|BrokenGlass3S [Indent level: 4],
                "brokenglass3s": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects1B",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass1B|DestructionEffects|BrokenGlass4S [Indent level: 4],
                "brokenglass4s": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects1B",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass1B|DestructionEffects|BrokenGlass5S [Indent level: 4],
                "brokenglass5s": {
                    "simulation": "particles",
                    "type": "BrokenGlass5SS",
                    "position": "GlassEffects1B",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                }
            },
            "name": "glass1",
            "visual": "glass1",
            "radius": 0.37,
            "explosionshielding": 2,
            "minimalhit": 0.025,
            "passthrough": 0
        },
        # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass16 [Indent level: 2],
        "hitglass16": {
            "name": "glass16",
            "visual": "glass16",
            "radius": 0.24,
            "armor": 0.8,
            "explosionshielding": 1,
            "minimalhit": 0.025,
            "passthrough": 0,
            # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass16|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass16|DestructionEffects|BrokenGlass1 [Indent level: 4],
                "brokenglass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects16",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass16|DestructionEffects|BrokenGlass2 [Indent level: 4],
                "brokenglass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects16",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass16|DestructionEffects|BrokenGlass3 [Indent level: 4],
                "brokenglass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects16",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass16|DestructionEffects|BrokenGlass4 [Indent level: 4],
                "brokenglass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects16",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass16|DestructionEffects|BrokenGlass5 [Indent level: 4],
                "brokenglass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects16",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass16|DestructionEffects|BrokenGlass1S [Indent level: 4],
                "brokenglass1s": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects16",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass16|DestructionEffects|BrokenGlass2S [Indent level: 4],
                "brokenglass2s": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects16",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass16|DestructionEffects|BrokenGlass3S [Indent level: 4],
                "brokenglass3s": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects16",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass16|DestructionEffects|BrokenGlass4S [Indent level: 4],
                "brokenglass4s": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects16",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass16|DestructionEffects|BrokenGlass5S [Indent level: 4],
                "brokenglass5s": {
                    "simulation": "particles",
                    "type": "BrokenGlass5SS",
                    "position": "GlassEffects16",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                }
            }
        },
        # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass17 [Indent level: 2],
        "hitglass17": {
            "name": "glass17",
            "visual": "glass17",
            "radius": 0.24,
            "armor": 0.8,
            "explosionshielding": 1,
            "minimalhit": 0.025,
            "passthrough": 0,
            # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass17|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass17|DestructionEffects|BrokenGlass1 [Indent level: 4],
                "brokenglass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects17",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass17|DestructionEffects|BrokenGlass2 [Indent level: 4],
                "brokenglass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects17",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass17|DestructionEffects|BrokenGlass3 [Indent level: 4],
                "brokenglass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects17",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass17|DestructionEffects|BrokenGlass4 [Indent level: 4],
                "brokenglass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects17",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass17|DestructionEffects|BrokenGlass5 [Indent level: 4],
                "brokenglass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects17",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass17|DestructionEffects|BrokenGlass1S [Indent level: 4],
                "brokenglass1s": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects17",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass17|DestructionEffects|BrokenGlass2S [Indent level: 4],
                "brokenglass2s": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects17",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass17|DestructionEffects|BrokenGlass3S [Indent level: 4],
                "brokenglass3s": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects17",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass17|DestructionEffects|BrokenGlass4S [Indent level: 4],
                "brokenglass4s": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects17",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|Heli_Transport_02_base_F|HitPoints|HitGlass17|DestructionEffects|BrokenGlass5S [Indent level: 4],
                "brokenglass5s": {
                    "simulation": "particles",
                    "type": "BrokenGlass5SS",
                    "position": "GlassEffects17",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                }
            }
        },
        # Class: CfgVehicles|Helicopter_Base_F|HitPoints|HitMissiles [Indent level: 2],
        "hitmissiles": {
            "name": "ammo_hit",
            "convexcomponent": "ammo_hit",
            "explosionshielding": 1,
            "armor": 0.1,
            "material": 51,
            "visual": "munice",
            "passthrough": 0.5
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitRGlass [Indent level: 2],
        "hitrglass": {
            "convexcomponent": "sklo predni P",
            "explosionshielding": 1,
            "armor": 0.1,
            "material": 51,
            "name": "sklo predni P",
            "visual": "sklo predni P",
            "passthrough": 0
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitLGlass [Indent level: 2],
        "hitlglass": {
            "convexcomponent": "sklo predni L",
            "explosionshielding": 1,
            "armor": 0.1,
            "material": 51,
            "name": "sklo predni L",
            "visual": "sklo predni L",
            "passthrough": 0
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitEngine3 [Indent level: 2],
        "hitengine3": {
            "name": "engine_3_hit",
            "convexcomponent": "engine_3_hit",
            "explosionshielding": 1,
            "armor": 0.25,
            "material": 51,
            "visual": "motor",
            "passthrough": 1
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitWinch [Indent level: 2],
        "hitwinch": {
            "armor": -40,
            "material": 51,
            "name": "slingLoad0",
            "visual": "",
            "passthrough": 0,
            "radius": 0.1,
            # Class: CfgVehicles|Helicopter|HitPoints|HitWinch|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|Helicopter|HitPoints|HitWinch|DestructionEffects|Explo [Indent level: 4],
                "explo": {
                    "simulation": "particles",
                    "type": "WinchDestructionExplo",
                    "position": "slingLoad0",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.06
                },
                # Class: CfgVehicles|Helicopter|HitPoints|HitWinch|DestructionEffects|Sparks [Indent level: 4],
                "sparks": {
                    "simulation": "particles",
                    "type": "WinchDestructionSparks",
                    "position": "slingLoad0",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.1
                }
            }
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitTransmission [Indent level: 2],
        "hittransmission": {
            "armor": 0.8,
            "material": -1,
            "name": "transmission",
            "passthrough": 0.8
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitLight [Indent level: 2],
        "hitlight": {
            "armor": 0.1,
            "material": -1,
            "name": "light",
            "passthrough": 0
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitHydraulics [Indent level: 2],
        "hithydraulics": {
            "armor": 0.8,
            "material": -1,
            "name": "hydraulics",
            "passthrough": 0.8
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitGear [Indent level: 2],
        "hitgear": {
            "armor": 0.9,
            "material": -1,
            "name": "gear",
            "passthrough": 0
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitHStabilizerL1 [Indent level: 2],
        "hithstabilizerl1": {
            "armor": 0.8,
            "material": -1,
            "name": "HStabilizerL1",
            "passthrough": 1
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitHStabilizerR1 [Indent level: 2],
        "hithstabilizerr1": {
            "armor": 0.8,
            "material": -1,
            "name": "HStabilizerR1",
            "passthrough": 0
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitVStabilizer1 [Indent level: 2],
        "hitvstabilizer1": {
            "armor": 0.8,
            "material": -1,
            "name": "VStabilizer1",
            "passthrough": 1
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitTail [Indent level: 2],
        "hittail": {
            "armor": 0.8,
            "material": -1,
            "name": "tail boom",
            "passthrough": 1
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitPitotTube [Indent level: 2],
        "hitpitottube": {
            "armor": 0.5,
            "material": -1,
            "name": "pitot tube",
            "passthrough": 0.2
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitStaticPort [Indent level: 2],
        "hitstaticport": {
            "armor": 0.1,
            "material": -1,
            "name": "static port",
            "passthrough": 1
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitStarter1 [Indent level: 2],
        "hitstarter1": {
            "armor": 0.1,
            "material": -1,
            "name": "starter1",
            "passthrough": 0
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitStarter2 [Indent level: 2],
        "hitstarter2": {
            "armor": 0.1,
            "material": -1,
            "name": "starter2",
            "passthrough": 0
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitStarter3 [Indent level: 2],
        "hitstarter3": {
            "armor": 0.1,
            "material": -1,
            "name": "starter3",
            "passthrough": 0
        }
    },
    # Class: CfgVehicles|RHS_CH_47F_base|Components [Indent level: 1],
    "components": {
        # Class: CfgVehicles|RHS_CH_47F_base|Components|TransportPylonsComponent [Indent level: 2]
        "transportpylonscomponent": {
            "uipicture": "rhsusf|addons|rhsusf_a2port_air|data|loadouts|RHS_CH47_EDEN_CA.paa",
            # Class: CfgVehicles|RHS_CH_47F_base|Components|TransportPylonsComponent|pylons [Indent level: 3],
            "pylons": {
                # Class: CfgVehicles|RHS_CH_47F_base|Components|TransportPylonsComponent|pylons|cmDispenser [Indent level: 4]
                "cmdispenser": {
                    "hardpoints": ["RHSUSF_cm_M130","RHSUSF_cm_M130_x2","RHSUSF_cm_M130_x4","RHSUSF_cm_M130_x8"],
                    "priority": 1,
                    "attachment": "rhsusf_M130_CMFlare_Chaff_Magazine_x8",
                    "maxweight": 800,
                    "uiposition": [0.33,0]
                }
            }
        },
        # Class: CfgVehicles|RHS_CH_47F_base|Components|SensorsManagerComponent [Indent level: 2],
        "sensorsmanagercomponent": {
            # Class: CfgVehicles|RHS_CH_47F_base|Components|SensorsManagerComponent|Components [Indent level: 3]
            "components": {
                # Class: CfgVehicles|RHS_CH_47F_base|Components|SensorsManagerComponent|Components|PassiveRadarSensorComponent [Indent level: 4]
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
                }
            }
        },
        # Class: CfgVehicles|RHS_CH_47F_base|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 2],
        "vehiclesystemsdisplaymanagercomponentleft": {
            # Class: CfgVehicles|RHS_CH_47F_base|Components|VehicleSystemsDisplayManagerComponentLeft|Components [Indent level: 3]
            "components": {
                # Class: CfgVehicles|RHS_CH_47F_base|Components|VehicleSystemsDisplayManagerComponentLeft|Components|EmptyDisplay [Indent level: 4]
                "emptydisplay": {
                    "componenttype": "EmptyDisplayComponent"
                },
                # Class: CfgVehicles|RHS_CH_47F_base|Components|VehicleSystemsDisplayManagerComponentLeft|Components|MinimapDisplay [Indent level: 4],
                "minimapdisplay": {
                    "componenttype": "MinimapDisplayComponent",
                    "resource": "RscCustomInfoMiniMap"
                },
                # Class: CfgVehicles|RHS_CH_47F_base|Components|VehicleSystemsDisplayManagerComponentLeft|Components|CrewDisplay [Indent level: 4],
                "crewdisplay": {
                    "componenttype": "CrewDisplayComponent",
                    "resource": "RscCustomInfoCrew"
                },
                # Class: CfgVehicles|RHS_CH_47F_base|Components|VehicleSystemsDisplayManagerComponentLeft|Components|SlingLoadDisplay [Indent level: 4],
                "slingloaddisplay": {
                    "componenttype": "SlingLoadDisplayComponent",
                    "resource": "RscCustomInfoSlingLoad"
                },
                # Class: CfgVehicles|RHS_CH_47F_base|Components|VehicleSystemsDisplayManagerComponentLeft|Components|SensorDisplay [Indent level: 4],
                "sensordisplay": {
                    "componenttype": "SensorsDisplayComponent",
                    "resource": "RscCustomInfoSensors",
                    "range": [3000,8000,16000,35000]
                }
            },
            "componenttype": "VehicleSystemsDisplayManager",
            "left": 1,
            "defaultdisplay": "EmptyDisplay",
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,	(safezoneX + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
        },
        # Class: CfgVehicles|RHS_CH_47F_base|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 2],
        "vehiclesystemsdisplaymanagercomponentright": {
            "defaultdisplay": "SensorDisplay",
            # Class: CfgVehicles|RHS_CH_47F_base|Components|VehicleSystemsDisplayManagerComponentRight|Components [Indent level: 3],
            "components": {
                # Class: CfgVehicles|RHS_CH_47F_base|Components|VehicleSystemsDisplayManagerComponentRight|Components|EmptyDisplay [Indent level: 4]
                "emptydisplay": {
                    "componenttype": "EmptyDisplayComponent"
                },
                # Class: CfgVehicles|RHS_CH_47F_base|Components|VehicleSystemsDisplayManagerComponentRight|Components|MinimapDisplay [Indent level: 4],
                "minimapdisplay": {
                    "componenttype": "MinimapDisplayComponent",
                    "resource": "RscCustomInfoMiniMap"
                },
                # Class: CfgVehicles|RHS_CH_47F_base|Components|VehicleSystemsDisplayManagerComponentRight|Components|CrewDisplay [Indent level: 4],
                "crewdisplay": {
                    "componenttype": "CrewDisplayComponent",
                    "resource": "RscCustomInfoCrew"
                },
                # Class: CfgVehicles|RHS_CH_47F_base|Components|VehicleSystemsDisplayManagerComponentRight|Components|SlingLoadDisplay [Indent level: 4],
                "slingloaddisplay": {
                    "componenttype": "SlingLoadDisplayComponent",
                    "resource": "RscCustomInfoSlingLoad"
                },
                # Class: CfgVehicles|RHS_CH_47F_base|Components|VehicleSystemsDisplayManagerComponentRight|Components|SensorDisplay [Indent level: 4],
                "sensordisplay": {
                    "componenttype": "SensorsDisplayComponent",
                    "resource": "RscCustomInfoSensors",
                    "range": [3000,8000,16000,35000]
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
    # Class: CfgVehicles|RHS_CH_47F_base|UserActions [Indent level: 1],
    "useractions": {
        # Class: CfgVehicles|RHS_CH_47F_base|UserActions|OpenCargoDoor [Indent level: 2]
        "opencargodoor": {
            "displayname": "Open Ramp",
            "position": "pos driver",
            "radius": 15,
            "showwindow": 0,
            "condition": "this animationSourcePhase 'ramp_anim' < 1 and (alive this) and ({player == _x} count [driver this,  this turretUnit [3], this turretUnit [4]] > 0)",
            "statement": "this animateSource ['ramp_anim', 1];[this] call rhs_fnc_cargoDetach",
            "onlyforplayer": 1,
            "shortcut": "user12"
        },
        # Class: CfgVehicles|RHS_CH_47F_base|UserActions|LevelRamp [Indent level: 2],
        "levelramp": {
            "displayname": "Level Ramp",
            "condition": "this animationSourcePhase 'ramp_anim' != 0.6 and (alive this) and (alive this) and ({player == _x} count [driver this,  this turretUnit [3], this turretUnit [4]] > 0);",
            "statement": "this animateSource ['ramp_anim', 0.6];",
            "shortcut": "user13",
            "position": "pos driver",
            "radius": 15,
            "showwindow": 0,
            "onlyforplayer": 1
        },
        # Class: CfgVehicles|RHS_CH_47F_base|UserActions|CloseCargoDoor [Indent level: 2],
        "closecargodoor": {
            "displayname": "Close Ramp",
            "condition": "this animationSourcePhase 'ramp_anim' > 0 and (alive this) and (alive this) and ({player == _x} count [driver this,  this turretUnit [3], this turretUnit [4]] > 0);",
            "statement": "this animateSource ['ramp_anim', 0];[this] call rhs_fnc_cargoAttach",
            "position": "pos driver",
            "radius": 15,
            "showwindow": 0,
            "onlyforplayer": 1,
            "shortcut": "user12"
        },
        # Class: CfgVehicles|RHS_CH_47F_base|UserActions|VehicleParadrop [Indent level: 2],
        "vehicleparadrop": {
            "displayname": "Paradrop cargo",
            "condition": "(count (attachedObjects this) > 0) AND ('man' countType (attachedObjects this) == 0) AND Alive(this)",
            "statement": "[this] spawn rhs_fnc_vehPara",
            "shortcut": "",
            "position": "pos driver",
            "radius": 15,
            "showwindow": 0,
            "onlyforplayer": 1
        },
        # Class: CfgVehicles|RHS_CH_47F_base|UserActions|ToggleLight [Indent level: 2],
        "togglelight": {
            "displayname": "Toggle interior light",
            "position": "pos driver",
            "radius": 15,
            "showwindow": 0,
            "condition": "player in this;",
            "statement": "[this,'cargolights_hide'] call rhs_fnc_toggleIntLight",
            "onlyforplayer": 1
        },
        # Class: CfgVehicles|RHS_CH_47F_base|UserActions|WheelBrakes [Indent level: 2],
        "wheelbrakes": {
            "displayname": "Toggle Wheel Brakes",
            "shortcut": "binocular",
            "condition": "!difficultyEnabledRTD && (call rhs_fnc_findPlayer) isEqualTo (driver this)",
            "statement": "[this] call rhs_fnc_heli_wheelBrakes",
            "position": "pos driver",
            "radius": 15,
            "showwindow": 0,
            "onlyforplayer": 1
        }
    },
    "weapons": ["rhsusf_weap_ANALQ212"],
    "magazines": ["rhsusf_mag_DIRCM","rhsusf_mag_DIRCM","rhsusf_mag_DIRCM","rhsusf_mag_DIRCM","rhsusf_mag_DIRCM","rhsusf_mag_DIRCM","rhsusf_mag_DIRCM","rhsusf_mag_DIRCM","rhsusf_mag_DIRCM","rhsusf_mag_DIRCM"],
    "memorypointcm": ["flare_launcher1","flare_launcher2"],
    "memorypointcmdir": ["flare_launcher1_dir","flare_launcher2_dir"],
    "selectionhrotorstill": "velka vrtule staticka",
    "selectionhrotormove": "velka vrtule blur",
    "selectionvrotorstill": "mala vrtule staticka",
    "selectionvrotormove": "mala vrtule blur",
    "selectiondamage": "trup",
    "selectionshowdamage": "poskozeni",
    "memorypointlrocket": "l raketa",
    "memorypointrrocket": "p raketa",
    "memorypointlmissile": "l strela",
    "memorypointrmissile": "p strela",
    "enablemanualfire": 0,
    "threat": [0.8,1,0.6],
    "helmetmounteddisplay": 0,
    "cargocaneject": 1,
    "drivercaneject": 0,
    # Class: CfgVehicles|RHS_CH_47F_base|MFD [Indent level: 1],
    "mfd": {
    },
    # Class: CfgVehicles|RHS_CH_47F_base|TransportMagazines [Indent level: 1],
    "transportmagazines": {
        # Class: CfgVehicles|RHS_CH_47F_base|TransportMagazines|_xx_rhs_mag_30Rnd_556x45_M855A1_Stanag [Indent level: 2]
        "_xx_rhs_mag_30rnd_556x45_m855a1_stanag": {
            "magazine": "rhs_mag_30Rnd_556x45_M855A1_Stanag",
            "count": 12
        },
        # Class: CfgVehicles|RHS_CH_47F_base|TransportMagazines|_xx_rhs_mag_m67 [Indent level: 2],
        "_xx_rhs_mag_m67": {
            "magazine": "rhs_mag_m67",
            "count": 4
        },
        # Class: CfgVehicles|RHS_CH_47F_base|TransportMagazines|_xx_rhs_mag_m18_green [Indent level: 2],
        "_xx_rhs_mag_m18_green": {
            "magazine": "rhs_mag_m18_green",
            "count": 2
        },
        # Class: CfgVehicles|RHS_CH_47F_base|TransportMagazines|_xx_rhs_mag_m18_red [Indent level: 2],
        "_xx_rhs_mag_m18_red": {
            "magazine": "rhs_mag_m18_red",
            "count": 2
        },
        # Class: CfgVehicles|RHS_CH_47F_base|TransportMagazines|_xx_rhs_mag_an_m8hc [Indent level: 2],
        "_xx_rhs_mag_an_m8hc": {
            "magazine": "rhs_mag_an_m8hc",
            "count": 4
        }
    },
    # Class: CfgVehicles|RHS_CH_47F_base|TransportItems [Indent level: 1],
    "transportitems": {
        # Class: CfgVehicles|RHS_CH_47F_base|TransportItems|_xx_FirstAidKit [Indent level: 2]
        "_xx_firstaidkit": {
            "name": "FirstAidKit",
            "count": 10
        },
        # Class: CfgVehicles|RHS_CH_47F_base|TransportItems|_xx_Medikit [Indent level: 2],
        "_xx_medikit": {
            "name": "Medikit",
            "count": 2
        }
    },
    # Class: CfgVehicles|RHS_CH_47F_base|TransportWeapons [Indent level: 1],
    "transportweapons": {
        # Class: CfgVehicles|RHS_CH_47F_base|TransportWeapons|_xx_rhs_weap_m4_carryhandle [Indent level: 2]
        "_xx_rhs_weap_m4_carryhandle": {
            "weapon": "rhs_weap_m4_carryhandle",
            "count": 2
        }
    },
    # Class: CfgVehicles|RHS_CH_47F_base|TransportBackpacks [Indent level: 1],
    "transportbackpacks": {
        # Class: CfgVehicles|RHS_CH_47F_base|TransportBackpacks|_xx_B_Parachute [Indent level: 2]
        "_xx_b_parachute": {
            "backpack": "B_Parachute",
            "count": 4
        }
    },
    # Class: CfgVehicles|RHS_CH_47F_base|Library [Indent level: 1],
    "library": {
        "libtextdesc": "CH-47F"
    },
    "attenuationeffecttype": "HeliAttenuation",
    "soundgetin": ["rhsusf|addons|rhsusf_a2port_air|data|sounds|close",0.316228,1],
    "soundgetout": ["rhsusf|addons|rhsusf_a2port_air|data|sounds|open",0.316228,1,40],
    "sounddammage": ["rhsusf|addons|rhsusf_a2port_air|data|sounds|int-alarm_loop",0.562341,1],
    "soundengineonint": ["rhsusf|addons|rhsusf_a2port_air|data|sounds|CH47_start_int",0.1,1],
    "soundengineonext": ["rhsusf|addons|rhsusf_a2port_air|data|sounds|CH47_start_ext",0.562341,1,800],
    "soundengineoffint": ["rhsusf|addons|rhsusf_a2port_air|data|sounds|CH47_stop_int",0.1,1],
    "soundengineoffext": ["rhsusf|addons|rhsusf_a2port_air|data|sounds|CH47_stop_ext",0.562341,1,800],
    "occludesoundswhenin": 0.562341,
    "obstructsoundswhenin": 0.316228,
    "soundlocked": ["|A3|Sounds_F|weapons|Rockets|opfor_lock_1",0.1,1],
    "soundincommingmissile": ["|A3|Sounds_F|weapons|Rockets|opfor_lock_2",0.1,1],
    # Class: CfgVehicles|RHS_CH_47F_base|Sounds [Indent level: 1],
    "sounds": {
        # Class: CfgVehicles|RHS_CH_47F_base|Sounds|Engine [Indent level: 2]
        "engine": {
            "sound": ["rhsusf|addons|rhsusf_a2port_air|data|sounds|CH47_engine_high_ext",1,1,800],
            "frequency": "rotorSpeed",
            "volume": "camPos*((rotorSpeed-0.72)*4)"
        },
        # Class: CfgVehicles|RHS_CH_47F_base|Sounds|RotorLowOut [Indent level: 2],
        "rotorlowout": {
            "sound": ["rhsusf|addons|rhsusf_a2port_air|data|sounds|CH47_rotor_ext.ogg",8.16228,1,3500],
            "frequency": "rotorSpeed",
            "volume": "camPos*(0 max (rotorSpeed-0.1))",
            "cone": [1.8,3.14,2,0.09]
        },
        # Class: CfgVehicles|RHS_CH_47F_base|Sounds|RotorHighOut [Indent level: 2],
        "rotorhighout": {
            "sound": ["rhsusf|addons|rhsusf_a2port_air|data|sounds|CH47_rotor_forsage_ext",6.16228,1,2200],
            "frequency": "rotorSpeed",
            "volume": "camPos*10*(0 max (rotorThrust-0.95))",
            "cone": [1.8,3.14,2,0.09]
        },
        # Class: CfgVehicles|RHS_CH_47F_base|Sounds|EngineIn [Indent level: 2],
        "enginein": {
            "sound": ["rhsusf|addons|rhsusf_a2port_air|data|sounds|CH47_engine_high_int",1.77828,1],
            "frequency": "rotorSpeed",
            "volume": "(1-camPos)*((rotorSpeed-0.75)*4)"
        },
        # Class: CfgVehicles|RHS_CH_47F_base|Sounds|RotorLowIn [Indent level: 2],
        "rotorlowin": {
            "sound": ["rhsusf|addons|rhsusf_a2port_air|data|sounds|CH47_rotor_ext.ogg",2.77828,1],
            "frequency": "rotorSpeed",
            "volume": "2*(1-camPos)*((rotorSpeed factor[0.3, 1.1]) min (rotorSpeed factor[1.1, 0.3]))"
        },
        # Class: CfgVehicles|RHS_CH_47F_base|Sounds|RotorHighIn [Indent level: 2],
        "rotorhighin": {
            "sound": ["rhsusf|addons|rhsusf_a2port_air|data|sounds|CH47_rotor_forsage_int",2.77828,1],
            "frequency": "rotorSpeed",
            "volume": "(1-camPos)*3*(rotorThrust-0.9)"
        }
    },
    # Class: CfgVehicles|RHS_CH_47F_base|MarkerLights [Indent level: 1],
    "markerlights": {
        # Class: CfgVehicles|RHS_CH_47F_base|MarkerLights|WhiteStill [Indent level: 2]
        "whitestill": {
            "name": "bily pozicni",
            "color": [1,1,1],
            "ambient": [0.1,0.1,0.1],
            "blinking": 1,
            "intensity": 75,
            "blinkingpattern": [0.1,0.09],
            "blinkingpatternguarantee": 0,
            "drawlightsize": 0.2,
            "drawlightcentersize": 0.04
        },
        # Class: CfgVehicles|RHS_CH_47F_base|MarkerLights|RedStill [Indent level: 2],
        "redstill": {
            "name": "cerveny pozicni",
            "color": [0.8,0,0],
            "ambient": [0.08,0,0],
            "intensity": 75,
            "drawlight": 1,
            "drawlightsize": 0.15,
            "drawlightcentersize": 0.04,
            "activelight": 0,
            "blinking": 0,
            "daylight": 0,
            "useflare": 0
        },
        # Class: CfgVehicles|RHS_CH_47F_base|MarkerLights|GreenStill [Indent level: 2],
        "greenstill": {
            "name": "zeleny pozicni",
            "color": [0,0.8,0],
            "ambient": [0,0.08,0],
            "intensity": 75,
            "drawlight": 1,
            "drawlightsize": 0.15,
            "drawlightcentersize": 0.04,
            "activelight": 0,
            "blinking": 0,
            "daylight": 0,
            "useflare": 0
        },
        # Class: CfgVehicles|RHS_CH_47F_base|MarkerLights|RedBlinking [Indent level: 2],
        "redblinking": {
            "name": "bily pozicni blik",
            "color": [0.09,0.15,0.1],
            "ambient": [0.09,0.015,0.01],
            "intensity": 75,
            "blinking": 1,
            "blinkingpattern": [0.1,0.09],
            "blinkingpatternguarantee": 0,
            "drawlightsize": 0.2,
            "drawlightcentersize": 0.04
        },
        # Class: CfgVehicles|RHS_CH_47F_base|MarkerLights|WhiteBlinking [Indent level: 2],
        "whiteblinking": {
            "name": "cerveny pozicni blik",
            "color": [0.09,0.15,0.1],
            "intensity": 75,
            "ambient": [0.09,0.015,0.01],
            "blinking": 1,
            "blinkingpattern": [0.2,1.3],
            "blinkingpatternguarantee": 0,
            "drawlightsize": 0.25,
            "drawlightcentersize": 0.08
        }
    },
    # Class: CfgVehicles|RHS_CH_47F_base|Reflectors [Indent level: 1],
    "reflectors": {
        # Class: CfgVehicles|RHS_CH_47F_base|Reflectors|Middle [Indent level: 2]
        "middle": {
            "color": [7000,7500,10000,1],
            "ambient": [100,100,100,0],
            "position": "svetlo",
            "direction": "svetlo konec",
            "hitpoint": "svetlo",
            "selection": "svetlo",
            "size": 1,
            "innerangle": 20,
            "outerangle": 60,
            "conefadecoef": 10,
            "intensity": 50,
            "useflare": 1,
            "daylight": 0,
            "flaresize": 6,
            # Class: CfgVehicles|RHS_CH_47F_base|Reflectors|Middle|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 4
            }
        }
    },
    # Class: CfgVehicles|RHS_CH_47F_base|Exhausts [Indent level: 1],
    "exhausts": {
        # Class: CfgVehicles|RHS_CH_47F_base|Exhausts|Exhaust1 [Indent level: 2]
        "exhaust1": {
            "direction": "exhaust1_dir",
            "effect": "ExhaustEffectHeli",
            "position": "exhaust1"
        },
        # Class: CfgVehicles|RHS_CH_47F_base|Exhausts|Exhaust2 [Indent level: 2],
        "exhaust2": {
            "direction": "exhaust2_dir",
            "effect": "ExhaustEffectHeli",
            "position": "exhaust2"
        }
    },
    # Class: CfgVehicles|RHS_CH_47F_base|Damage [Indent level: 1],
    "damage": {
        "tex": [],
        "mat": ["rhsusf|addons|rhsusf_a2port_air|CH47|data|ch47_1.rvmat","rhsusf|addons|rhsusf_a2port_air|CH47|data|ch47_1_damage.rvmat","rhsusf|addons|rhsusf_a2port_air|CH47|data|ch47_1_destruct.rvmat","rhsusf|addons|rhsusf_a2port_air|CH47|data|ch47_2.rvmat","rhsusf|addons|rhsusf_a2port_air|CH47|data|ch47_2_damage.rvmat","rhsusf|addons|rhsusf_a2port_air|CH47|data|ch47_2_destruct.rvmat","rhsusf|addons|rhsusf_a2port_air|CH47|data|ch47_1_int.rvmat","rhsusf|addons|rhsusf_a2port_air|CH47|data|ch47_1_int.rvmat","rhsusf|addons|rhsusf_a2port_air|CH47|data|ch47_1_int_destruct.rvmat","rhsusf|addons|rhsusf_a2port_air|CH47|data|ch47_2_int.rvmat","rhsusf|addons|rhsusf_a2port_air|CH47|data|ch47_2_int.rvmat","rhsusf|addons|rhsusf_a2port_air|CH47|data|ch47_2_int_destruct.rvmat","rhsusf|addons|rhsusf_a2port_air|CH47|data|ch47_sklo_in.rvmat","rhsusf|addons|rhsusf_a2port_air|CH47|data|ch47_sklo_in_damage.rvmat","rhsusf|addons|rhsusf_a2port_air|CH47|data|ch47_sklo_in_damage.rvmat","rhsusf|addons|rhsusf_a2port_air|CH47|data|ch47_sklo.rvmat","rhsusf|addons|rhsusf_a2port_air|CH47|data|ch47_sklo_damage.rvmat","rhsusf|addons|rhsusf_a2port_air|CH47|data|ch47_sklo_damage.rvmat","a3|data_f|default.rvmat","a3|data_f|default.rvmat","a3|data_f|default_destruct.rvmat"]
    },
    "irscanrangemin": 0,
    "irscanrangemax": 1000,
    "irscantoeyefactor": 2,
    "gunnercansee": "2+4+8+16",
    "drivercansee": "2+4+8+16",
    "hiddenselections": ["camo1","camo2","camo3","camo4"],
    "hiddenselectionstextures": ["rhsusf|addons|rhsusf_a2port_air|ch47|data|ch47_ext_1_co.paa","rhsusf|addons|rhsusf_a2port_air|ch47|data|ch47_ext_2_co.paa","rhsusf|addons|rhsusf_a2port_air|ch47|data|ch47f_nalepky_ca.paa","rhsusf|addons|rhsusf_a2port_air|ch47|data|ch47_ext_mlod_co.paa"],
    # Class: CfgVehicles|RHS_CH_47F_base|textureSources [Indent level: 1],
    "texturesources": {
        # Class: CfgVehicles|RHS_CH_47F_base|textureSources|standard [Indent level: 2]
        "standard": {
            "displayname": "Standard",
            "author": "Red Hammer Studios",
            "textures": ["rhsusf|addons|rhsusf_a2port_air|ch47|data|ch47_ext_1_co.paa","rhsusf|addons|rhsusf_a2port_air|ch47|data|ch47_ext_2_co.paa","rhsusf|addons|rhsusf_a2port_air|ch47|data|ch47f_nalepky_ca.paa","rhsusf|addons|rhsusf_a2port_air|ch47|data|ch47_ext_mlod_co.paa"],
            "factions": ["rhs_faction_usarmy_wd","rhs_faction_usarmy_d"]
        },
        # Class: CfgVehicles|RHS_CH_47F_base|textureSources|Desert [Indent level: 2],
        "desert": {
            "displayname": "Desert",
            "author": "Red Hammer Studios",
            "textures": ["rhsusf|addons|rhsusf_a2port_air|ch47|data|ch47_ext_1_light_co.paa","rhsusf|addons|rhsusf_a2port_air|ch47|data|ch47_ext_2_light_co.paa","rhsusf|addons|rhsusf_a2port_air|ch47|data|ch47f_nalepky_ca.paa","rhsusf|addons|rhsusf_a2port_air|ch47|data|ch47_ext_light_mlod_co.paa"],
            "factions": ["rhs_faction_usarmy_wd","rhs_faction_usarmy_d"]
        }
    },
    "texturelist": [],
    # Class: CfgVehicles|RHS_CH_47F_base|Attributes [Indent level: 1],
    "attributes": {
        # Class: CfgVehicles|RHS_CH_47F_base|Attributes|ObjectTexture [Indent level: 2]
        "objecttexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayname": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        # Class: CfgVehicles|RHS_CH_47F_base|Attributes|ramp_anim [Indent level: 2],
        "ramp_anim": {
            "displayname": "Open ramp",
            "property": "ramp_anim",
            "control": "slider",
            "defaultvalue": "0",
            "expression": "_this animateSource ['%s',_value,true]"
        },
        # Class: CfgVehicles|RHS_CH_47F_base|Attributes|hide_cargo [Indent level: 2],
        "hide_cargo": {
            "displayname": "Hide cargo benches",
            "property": "hide_cargo",
            "control": "CheckboxNumber",
            "expression": "_this animate ['%s',_value,true];_this lockCargo (_value == 1)",
            "defaultvalue": "0"
        },
        # Class: CfgVehicles|RHS_CH_47F_base|Attributes|rhs_attachCargo [Indent level: 2],
        "rhs_attachcargo": {
            "displayname": "Attach cargo",
            "tooltip": "Attaching cargo (using attachTo command) just like when you use ramp action",
            "property": "rhs_attachCargo",
            "expression": "if(_value == 1)then{[_this] spawn rhs_fnc_cargoAttach}else{{if(not(_x isKindOf 'Man'))then{detach _x}}foreach attachedObjects _this};",
            "control": "CheckboxNumber",
            "defaultvalue": "0"
        }
    },
    "features": "Randomization: No						<br />Camo selections: 3 - main body, tail various attachments, engine						<br />Script door sources: CargoRamp_Open, Door_Back_L, Door_Back_R						<br />Script animations: None						<br />Executed scripts: None						<br />Firing from vehicles: No						<br />Slingload: Slingloads up to 4000 kg						<br />Cargo proxy indexes: 1 to 16",
    "_generalmacro": "Heli_Transport_02_base_F",
    "editorsubcategory": "EdSubcat_Helicopters",
    "memorypointtaskmarker": "TaskMarker_1_pos",
    "useprecisegetinaction": 0,
    "memorypointsgetindriverprecise": "GetIn_Pilot",
    "memorypointsgetincargoprecise": ["GetIn_Cargo"],
    "getinradius": 1.7,
    "precisegetinout": 0,
    "cargoprecisegetinout": [0],
    "getinaction": "GetInLow",
    "getoutaction": "GetOutLow",
    "cargogetinaction": ["GetInLow"],
    "cargogetoutaction": ["GetOutLow"],
    "driverdoor": "",
    "cargodoors": [],
    "castcargoshadow": 1,
    "hideweaponscargo": 1,
    "ejectdeadcargo": 0,
    "maximumload": 5000,
    "supplyradius": -0.3,
    "cost": 700000,
    "enablesweep": 0,
    "extcameraposition": [0,5,-30],
    # Class: CfgVehicles|Heli_Transport_02_base_F|ViewPilot [Indent level: 1],
    "viewpilot": {
        "initanglex": -9,
        "initfov": 0.9,
        "minfov": 0.25,
        "maxfov": 1.25,
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
    "emptysound": ["",0,1],
    "soundgeneralcollision1": ["A3|Sounds_F|vehicles|crashes|helis|Heli_coll_default_int_1",1,1,100],
    "soundgeneralcollision2": ["A3|Sounds_F|vehicles|crashes|helis|Heli_coll_default_int_2",1,1,100],
    "soundgeneralcollision3": ["A3|Sounds_F|vehicles|crashes|helis|Heli_coll_default_int_3",1,1,100],
    "soundcrashes": ["soundGeneralCollision1",0.33,"soundGeneralCollision2",0.33,"soundGeneralCollision3",0.33],
    "soundlandcrashes": ["emptySound",0],
    "soundbuildingcrash": ["soundGeneralCollision1",1,"soundGeneralCollision2",1,"soundGeneralCollision3",1],
    "soundarmorcrash": ["soundGeneralCollision1",1,"soundGeneralCollision2",1,"soundGeneralCollision3",1],
    "soundwoodcrash": ["soundGeneralCollision1",1,"soundGeneralCollision2",1,"soundGeneralCollision3",1],
    "soundbushcollision1": ["A3|Sounds_F|vehicles|crashes|helis|Heli_coll_bush_int_1",1,1,100],
    "soundbushcollision2": ["A3|Sounds_F|vehicles|crashes|helis|Heli_coll_bush_int_2",1,1,100],
    "soundbushcollision3": ["A3|Sounds_F|vehicles|crashes|helis|Heli_coll_bush_int_3",1,1,100],
    "soundbushcrash": ["soundBushCollision1",0.33,"soundBushCollision2",0.33,"soundBushCollision3",0.33],
    "soundwatercollision1": ["A3|Sounds_F|vehicles|crashes|helis|Heli_coll_water_ext_1",1,1,100],
    "soundwatercollision2": ["A3|Sounds_F|vehicles|crashes|helis|Heli_coll_water_ext_2",1,1,100],
    "soundwatercrashes": ["soundWaterCollision1",0.5,"soundWaterCollision2",0.5],
    "rotordamageint": ["A3|Sounds_F|vehicles|air|noises|heli_damage_rotor_int_1",1,1],
    "rotordamageout": ["A3|Sounds_F|vehicles|air|noises|heli_damage_rotor_ext_1",2.51189,1,300],
    "rotordamage": ["rotorDamageInt","rotorDamageOut"],
    "taildamageint": ["A3|Sounds_F|vehicles|air|noises|heli_damage_tail",1,1],
    "taildamageout": ["A3|Sounds_F|vehicles|air|noises|heli_damage_tail",1,1,300],
    "taildamage": ["tailDamageInt","tailDamageOut"],
    "landingsoundint0": ["A3|Sounds_F|vehicles|air|noises|landing_wheels_small_int1",1,1,100],
    "landingsoundint1": ["A3|Sounds_F|vehicles|air|noises|landing_wheels_small_int2",1,1,100],
    "landingsoundint": ["landingSoundInt0",0.5,"landingSoundInt1",0.5],
    "landingsoundout0": ["A3|Sounds_F|vehicles|air|noises|landing_wheels_ext1",1.77828,1,100],
    "landingsoundout1": ["A3|Sounds_F|vehicles|air|noises|landing_wheels_ext2",1.77828,1,100],
    "landingsoundout": ["landingSoundOut0",0.5,"landingSoundOut1",0.5],
    "slingcargoattach0": ["A3|Sounds_F|vehicles|air|noises|SL_engineDownEndINT",1,1],
    "slingcargoattach1": ["A3|Sounds_F|vehicles|air|noises|SL_1hookLock",1.77828,1,200],
    "slingcargoattach": ["slingCargoAttach0","slingCargoAttach1"],
    "slingcargodetach0": ["A3|Sounds_F|vehicles|air|noises|SL_engineUpEndINT",1,1],
    "slingcargodetach1": ["A3|Sounds_F|vehicles|air|noises|SL_1hookUnlock",1.77828,1,200],
    "slingcargodetach": ["slingCargoDetach0","slingCargoDetach1"],
    "slingcargodetachair0": ["A3|Sounds_F|vehicles|air|noises|SL_unhook_air_int",1,1],
    "slingcargodetachair1": ["A3|Sounds_F|vehicles|air|noises|SL_unhook_air_ext",1,1,300],
    "slingcargodetachair": ["slingCargoDetach0","slingCargoDetach1"],
    "slingcargoropebreak0": ["A3|Sounds_F|vehicles|air|noises|SL_rope_break_int",1,1],
    "slingcargoropebreak1": ["A3|Sounds_F|vehicles|air|noises|SL_rope_break_ext",1,1,200],
    "slingcargoropebreak": ["slingCargoDetach0","slingCargoDetach1"],
    "gearupext": ["A3|Sounds_F|vehicles|air|Heli_Transport_01|gear_up_OUT",1,1,1000],
    "gearupint": ["A3|Sounds_F|vehicles|air|Heli_Transport_01|gear_up_IN",1,1,100],
    "gearup": ["gearUpInt","gearUpExt"],
    "geardownint": ["A3|Sounds_F|vehicles|air|Heli_Transport_01|gear_down_IN",1,1,100],
    "geardownext": ["A3|Sounds_F|vehicles|air|Heli_Transport_01|gear_down_OUT",1,1,1000],
    "geardown": ["gearDownInt","gearDownExt"],
    # Class: CfgVehicles|Heli_Transport_02_base_F|SoundsExt [Indent level: 1],
    "soundsext": {
        # Class: CfgVehicles|Heli_Transport_02_base_F|SoundsExt|SoundEvents [Indent level: 2]
        "soundevents": {
        },
        # Class: CfgVehicles|Heli_Transport_02_base_F|SoundsExt|Sounds [Indent level: 2],
        "sounds": {
            # Class: CfgVehicles|Heli_Transport_02_base_F|SoundsExt|Sounds|EngineExt [Indent level: 3]
            "engineext": {
                "sound": ["A3|Sounds_F|vehicles|air|Heli_Transport_02|Heli_Transport_02_ext_engine",1.25893,1,900],
                "frequency": "rotorSpeed",
                "volume": "camPos*(rotorSpeed-0.72)*4"
            },
            # Class: CfgVehicles|Heli_Transport_02_base_F|SoundsExt|Sounds|RotorExt [Indent level: 3],
            "rotorext": {
                "sound": ["A3|Sounds_F|vehicles|air|Heli_Transport_02|Heli_Transport_02_ext_rotor",1.77828,1,2000],
                "frequency": "rotorSpeed * rotorSpeed * (1 - rotorThrust/6)",
                "volume": "camPos*(0 max (rotorSpeed-0.1))*(1 + rotorThrust)",
                "cone": [1.6,3.14,1.6,0.95]
            },
            # Class: CfgVehicles|Heli_Transport_02_base_F|SoundsExt|Sounds|RotorNoiseExt [Indent level: 3],
            "rotornoiseext": {
                "sound": ["A3|Sounds_F|vehicles|air|Heli_Transport_02|rotor_swist",0.707946,1,800],
                "frequency": 1,
                "volume": "camPos * (rotorThrust factor [0.7, 0.9])",
                "cone": [0.7,1.3,1,0]
            },
            # Class: CfgVehicles|Heli_Transport_02_base_F|SoundsExt|Sounds|EngineInt [Indent level: 3],
            "engineint": {
                "sound": ["A3|Sounds_F|vehicles|air|Heli_Transport_02|Heli_Transport_02_int_engine",1,1],
                "frequency": "rotorSpeed",
                "volume": "(1-camPos)*(rotorSpeed-0.75)*4"
            },
            # Class: CfgVehicles|Heli_Transport_02_base_F|SoundsExt|Sounds|RotorInt [Indent level: 3],
            "rotorint": {
                "sound": ["A3|Sounds_F|vehicles|air|Heli_Transport_02|Heli_Transport_02_int_rotor",1.25893,1],
                "frequency": "rotorSpeed * rotorSpeed * (1 - rotorThrust/6)",
                "volume": "(1-camPos)*(0 max (rotorSpeed-0.1))*(1 + rotorThrust)"
            },
            # Class: CfgVehicles|Heli_Transport_02_base_F|SoundsExt|Sounds|TransmissionDamageExt_phase1 [Indent level: 3],
            "transmissiondamageext_phase1": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_damage_transmission_ext_1",1,1,150],
                "frequency": "0.66 + rotorSpeed / 3",
                "volume": "camPos * (transmissionDamage factor [0.3, 0.35]) * (transmissionDamage factor [0.5, 0.45]) * (rotorSpeed factor [0.2, 0.5])"
            },
            # Class: CfgVehicles|Heli_Transport_02_base_F|SoundsExt|Sounds|TransmissionDamageExt_phase2 [Indent level: 3],
            "transmissiondamageext_phase2": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_damage_transmission_ext_2",1,1,150],
                "frequency": "0.66 + rotorSpeed / 3",
                "volume": "camPos * (transmissionDamage factor [0.45, 0.5]) * (rotorSpeed factor [0.2, 0.5])"
            },
            # Class: CfgVehicles|Heli_Transport_02_base_F|SoundsExt|Sounds|TransmissionDamageInt_phase1 [Indent level: 3],
            "transmissiondamageint_phase1": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_damage_transmission_int_1",1,1,150],
                "frequency": "0.66 + rotorSpeed / 3",
                "volume": "(1 - camPos) * (transmissionDamage factor [0.3, 0.35]) * (transmissionDamage factor [0.5, 0.45]) * (rotorSpeed factor [0.2, 0.5])"
            },
            # Class: CfgVehicles|Heli_Transport_02_base_F|SoundsExt|Sounds|TransmissionDamageInt_phase2 [Indent level: 3],
            "transmissiondamageint_phase2": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_damage_transmission_int_2",1,1,150],
                "frequency": "0.66 + rotorSpeed / 3",
                "volume": "(1 - camPos) * (transmissionDamage factor [0.45, 0.5]) * (rotorSpeed factor [0.2, 0.5])"
            },
            # Class: CfgVehicles|Heli_Transport_02_base_F|SoundsExt|Sounds|damageAlarmInt [Indent level: 3],
            "damagealarmint": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_alarm_opfor",0.316228,1],
                "frequency": 1,
                "volume": "engineOn * (1 - camPos) * ( 1 - ((transmissionDamage factor [0.61, 0.60]) * (motorDamage factor [0.61, 0.60]) * (rotorDamage factor [0.51, 0.50]))) * (rotorSpeed factor [0.0, 0.001])"
            },
            # Class: CfgVehicles|Heli_Transport_02_base_F|SoundsExt|Sounds|damageAlarmExt [Indent level: 3],
            "damagealarmext": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_alarm_opfor",0.223872,1,20],
                "frequency": 1,
                "volume": "engineOn * camPos * ( 1 - ((transmissionDamage factor [0.61, 0.60]) * (motorDamage factor [0.61, 0.60]) * (rotorDamage factor [0.51, 0.50]))) * (rotorSpeed factor [0, 0.001])"
            },
            # Class: CfgVehicles|Heli_Transport_02_base_F|SoundsExt|Sounds|rotorLowAlarmInt [Indent level: 3],
            "rotorlowalarmint": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_alarm_rotor_low",0.316228,1],
                "frequency": 1,
                "volume": "engineOn * (1 - camPos) * (rotorSpeed factor [0.9, 0.8999]) * (rotorSpeed factor [-0.5, 1]) * (speed factor [3, 3.01])"
            },
            # Class: CfgVehicles|Heli_Transport_02_base_F|SoundsExt|Sounds|rotorLowAlarmExt [Indent level: 3],
            "rotorlowalarmext": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_alarm_rotor_low",0.223872,1,20],
                "frequency": 1,
                "volume": "engineOn * camPos * (rotorSpeed factor [0.9, 0.8999]) * (rotorSpeed factor [-0.5, 1]) * (speed factor [3, 3.01])"
            },
            # Class: CfgVehicles|Heli_Transport_02_base_F|SoundsExt|Sounds|scrubLandInt [Indent level: 3],
            "scrublandint": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|wheelsInt",1,1,100],
                "frequency": 1,
                "volume": "2 * (1-camPos) * (scrubLand factor[0.02, 0.05]) * (1 - (lateralMovement factor [0.7,1]))"
            },
            # Class: CfgVehicles|Heli_Transport_02_base_F|SoundsExt|Sounds|scrubLandExt [Indent level: 3],
            "scrublandext": {
                "sound": ["A3|Sounds_F|dummysound",1,1,100],
                "frequency": 1,
                "volume": "camPos * (scrubLand factor[0.02, 0.05]) * (1 - (lateralMovement factor [0.7,1]))"
            },
            # Class: CfgVehicles|Heli_Transport_02_base_F|SoundsExt|Sounds|scrubBuildingInt [Indent level: 3],
            "scrubbuildingint": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|wheelsInt",1,1,100],
                "frequency": 1,
                "volume": "(1-camPos) * (scrubBuilding factor[0.02, 0.05]) * (1 - (lateralMovement factor [0.7,1]))"
            },
            # Class: CfgVehicles|Heli_Transport_02_base_F|SoundsExt|Sounds|scrubBuildingExt [Indent level: 3],
            "scrubbuildingext": {
                "sound": ["A3|Sounds_F|dummysound",1,1,100],
                "frequency": 1,
                "volume": "camPos * (scrubBuilding factor[0.02, 0.05])"
            },
            # Class: CfgVehicles|Heli_Transport_02_base_F|SoundsExt|Sounds|scrubTreeInt [Indent level: 3],
            "scrubtreeint": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|scrubTreeInt",1,1,100],
                "frequency": 1,
                "volume": "(1 - camPos) * ((scrubTree) factor [0, 0.01])"
            },
            # Class: CfgVehicles|Heli_Transport_02_base_F|SoundsExt|Sounds|scrubTreeExt [Indent level: 3],
            "scrubtreeext": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|scrubTreeExt",1,1,100],
                "frequency": 1,
                "volume": "camPos * ((scrubTree) factor [0, 0.01])"
            },
            # Class: CfgVehicles|Heli_Transport_02_base_F|SoundsExt|Sounds|RainExt [Indent level: 3],
            "rainext": {
                "sound": ["A3|Sounds_F|vehicles|noises|rain1_ext",1,1,100],
                "frequency": 1,
                "volume": "camPos * (rain - rotorSpeed/2) * 2"
            },
            # Class: CfgVehicles|Heli_Transport_02_base_F|SoundsExt|Sounds|RainInt [Indent level: 3],
            "rainint": {
                "sound": ["A3|Sounds_F|vehicles|noises|rain1_int",1,1,100],
                "frequency": 1,
                "volume": "(1-camPos)*(rain - rotorSpeed/2)*2"
            },
            # Class: CfgVehicles|Heli_Transport_02_base_F|SoundsExt|Sounds|SlingLoadDownExt [Indent level: 3],
            "slingloaddownext": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineDownEXT",1,1,500],
                "frequency": 1,
                "volume": "camPos*(slingLoadActive factor [0,-1])"
            },
            # Class: CfgVehicles|Heli_Transport_02_base_F|SoundsExt|Sounds|SlingLoadUpExt [Indent level: 3],
            "slingloadupext": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineUpEXT",1,1,500],
                "frequency": 1,
                "volume": "camPos*(slingLoadActive factor [0,1])"
            },
            # Class: CfgVehicles|Heli_Transport_02_base_F|SoundsExt|Sounds|SlingLoadDownInt [Indent level: 3],
            "slingloaddownint": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineDownINT",1,1,500],
                "frequency": 1,
                "volume": "(1-camPos)*(slingLoadActive factor [0,-1])"
            },
            # Class: CfgVehicles|Heli_Transport_02_base_F|SoundsExt|Sounds|SlingLoadUpInt [Indent level: 3],
            "slingloadupint": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineUpINT",1,1,500],
                "frequency": 1,
                "volume": "(1-camPos)*(slingLoadActive factor [0,1])"
            },
            # Class: CfgVehicles|Heli_Transport_02_base_F|SoundsExt|Sounds|WindInt [Indent level: 3],
            "windint": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|wind_closed",0.707946,1,50],
                "frequency": 1,
                "volume": "(1-camPos)*(speed factor[5, 50])*(speed factor[5, 50])"
            },
            # Class: CfgVehicles|Heli_Transport_02_base_F|SoundsExt|Sounds|GStress [Indent level: 3],
            "gstress": {
                "sound": ["A3|Sounds_F|vehicles|noises|vehicle_stress2d",0.707946,1,50],
                "frequency": 1,
                "volume": "engineOn * (1-camPos) * ((gmeterZ factor[1.5, 2.5]) + (gmeterZ factor[0.5, -0.5]))"
            },
            # Class: CfgVehicles|Heli_Transport_02_base_F|SoundsExt|Sounds|SpeedStress [Indent level: 3],
            "speedstress": {
                "sound": ["A3|Sounds_F|vehicles|noises|vehicle_stress3",0.707946,1,50],
                "frequency": 1,
                "volume": "(1-camPos)*(speed factor[40,60])"
            }
        }
    },
    # Class: CfgVehicles|Heli_Transport_02_base_F|Armory [Indent level: 1],
    "armory": {
        "description": "A successor to the wide-spread Merlin helicopter, the CH-49 Mohawk is a primary transport used by the AAF. It can carry up to 16 soldiers plus crew. Besides the transport version, many other versions of the Mohawk exist, serving as evac, anti-submarine warfare or armed air support. Upgrades over its predecessor consist of more powerful engines and construction changes fully utilizing modern materials."
    },
    "memorypointdriveroptics": "slingCamera",
    # Class: CfgVehicles|Helicopter_Base_H|PilotSpec [Indent level: 1],
    "pilotspec": {
        "showheadphones": 1
    },
    # Class: CfgVehicles|Helicopter_Base_H|CargoSpec [Indent level: 1],
    "cargospec": {
        # Class: CfgVehicles|Helicopter_Base_H|CargoSpec|Cargo1 [Indent level: 2]
        "cargo1": {
            "showheadphones": 1
        }
    },
    "transportmaxweapons": 12,
    "transportmaxmagazines": 48,
    "memorypointsupply": "doplnovani",
    "commandercansee": "1 + 2 + 4 + 8 + 32",
    "washdownstrength": "1.0f",
    "washdowndiameter": "40.0f",
    "minsmokedamage": 0.3,
    "maxsmokedamage": 0.99,
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
    # Class: CfgVehicles|Helicopter_Base_F|EventHandlers [Indent level: 1],
    "eventhandlers": {
        "fired": "",
        "init": "",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');"
    },
    "simulation": "helicopterrtd",
    "unitinfotypelite": "RscUnitInfoAirRTDBasic",
    "dusteffect": "HeliDust",
    "watereffect": "HeliWater",
    "gearminalt": 0.5,
    "startduration": 20,
    "maxmainrotordive": 0,
    "maxbackrotordive": 0,
    "minmainrotordive": 0,
    "minbackrotordive": 0,
    "neutralbackrotordive": 0,
    "neutralmainrotordive": 0,
    "memorypointgun": "",
    "memorypointpilot": "pilot",
    "_mainbladecenter": "rotor_center",
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
    "soundlandinggear": ["",1,1],
    "slingloadmemorypoint": "slingLoad0",
    # Class: CfgVehicles|Helicopter|SpeechVariants [Indent level: 1],
    "speechvariants": {
        # Class: CfgVehicles|Helicopter|SpeechVariants|Default [Indent level: 2]
        "default": {
            "speechsingular": ["veh_air_helicopter_s"],
            "speechplural": ["veh_air_helicopter_p"]
        }
    },
    "extcameraparams": [-1],
    "textsingular": "helicopter",
    "textplural": "helicopters",
    "camouflage": 100,
    "audible": 50,
    "epeimpulsedamagecoef": 50,
    "crewcrashprotection": 0.25,
    "headgforceleaningfactor": [0.01,0.0025,0.01],
    "damageeffect": "AirDestructionEffects",
    "type": 2,
    "dammagehalf": [],
    "dammagefull": [],
    "crewvulnerable": 1,
    "explosionshielding": 4,
    "mintotaldamagethreshold": 0.005,
    # Class: CfgVehicles|Helicopter|DestructionEffects [Indent level: 1],
    "destructioneffects": {
    },
    "mainbladecenter": "rotor_center",
    "tailbladecenter": "rotor_02_center",
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
    "altfullforce": 2000,
    "altnoforce": 6000,
    "insidesoundcoef": 0.0316228,
    "outsidesoundfilter": 1,
    "nightvision": 0,
    "drivercompartments": 0,
    "enablegps": 1,
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
    "impacteffectssea": "ImpactEffectsAir",
    "flarevelocity": 100,
    "enableradio": 1,
    "countermeasureactivationradius": 10000,
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
    "secondaryexplosion": -1,
    "fuelexplosionpower": 1,
    # Class: CfgVehicles|AllVehicles|SquadTitles [Indent level: 1],
    "squadtitles": {
        "name": "clan_sign",
        "color": [0,0,0,0.75]
    },
    "memorypointsgetindriver": "pos driver",
    "memorypointsgetindriverdir": "pos driver dir",
    "memorypointsgetincodriver": "pos codriver",
    "memorypointsgetincodriverdir": "pos codriver dir",
    "memorypointsleftwatereffect": "waterEffectL",
    "memorypointsrightwatereffect": "waterEffectR",
    "selectionclan": "clan",
    "selectiondashboard": "podsvit pristroju",
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
    # Class: CfgVehicles|AllVehicles|SoundEvents [Indent level: 1],
    "soundevents": {
    },
    "tracksspeed": 0,
    "selectionleftoffset": "",
    "selectionrightoffset": "",
    # Class: CfgVehicles|AllVehicles|RenderTargets [Indent level: 1],
    "rendertargets": {
    },
    "hasterminal": 0,
    "getinoutonproxy": 0,
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
    "sensitivity": 2.5,
    "sensitivityear": 0.0075,
    "portrait": "",
    "ghostpreview": "",
    "armorlights": 0.4,
    "replacedamaged": "",
    "replacedamagedlimit": 0.9,
    "replacedamagedhitpoints": [],
    "keepinepesceneafterdeath": 0,
    "groupcameraposition": [0,5,-30],
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
    "laserscanner": 0,
    "nvtarget": 0,
    "nvscanner": 0,
    "artillerytarget": 0,
    "artilleryscanner": 0,
    "canusescanners": 1,
    "preferroads": 0,
    "hideunitinfo": 0,
    "limitedspeedcoef": 0.22,
    "hasdriver": 1,
    "driverforceoptics": 0,
    "hideweaponsdriver": 1,
    "enablewatch": 0,
    "allowtablock": 1,
    "showalltargets": 0,
    "dustfrontleftpos": "dustFrontLeft",
    "dustfrontrightpos": "dustFrontRight",
    "dustbackleftpos": "dustBackLeft",
    "dustbackrightpos": "dustBackRight",
    "wheelcircumference": 1,
    "shownvgdriver": 0,
    "shownvgcommander": 0,
    "shownvggunner": 0,
    "soundattenuationcargo": [1],
    "countsforscoreboard": 1,
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
    "aggregatereflectors": [],
    "driverinaction": "",
    "driveropticsmodel": "",
    "driveropticseffect": [],
    "driveropticscolor": [1,1,1,1],
    "hideproxyincombat": 0,
    "forcehidedriver": 0,
    "canhidedriver": -1,
    "castdrivershadow": 0,
    "viewdrivershadow": 1,
    "viewdrivershadowdiff": 1,
    "viewdrivershadowamb": 1,
    "viewcargoshadow": 1,
    "viewcargoshadowdiff": 1,
    "viewcargoshadowamb": 1,
    "ejectdeaddriver": 0,
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
    "headaimdown": 0,
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
    "insidedetectcoef": 0.05,
}