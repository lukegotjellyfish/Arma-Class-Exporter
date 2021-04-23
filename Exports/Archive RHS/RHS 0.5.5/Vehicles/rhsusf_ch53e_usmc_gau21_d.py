rhsusf_ch53e_usmc_gau21_d = {
    "faction": "rhs_faction_usmc_d",
    "vehicleclass": "rhs_vehclass_helicopter",
    "crew": "rhsusf_usmc_marpat_d_helipilot",
    "typicalcargo": ["rhsusf_usmc_marpat_d_helicrew"],
    "author": "Rocket, RHS",
    "editorpreview": "rhsusf|addons|rhsusf_editorPreviews|data|rhsusf_CH53E_USMC_D.paa",
    # Class: CfgVehicles|rhsusf_CH53E_USMC_GAU21_D|Turrets [Indent level: 1],
    "turrets": {
        # Class: CfgVehicles|rhsusf_CH53E_USMC_GAU21_D|Turrets|CopilotTurret [Indent level: 2]
        "copilotturret": {
            "gunneraction": "RHS_CH53_Pilot",
            "gunnerinaction": "RHS_CH53_Pilot",
            "memorypointsgetingunner": "pos codriver",
            "memorypointsgetingunnerdir": "pos codriver dir",
            "gunnergetinaction": "GetInLow",
            "gunnergetoutaction": "GetOutLow",
            "gunnerdoor": "",
            "lodturnedin": 1000,
            "lodturnedout": 1000,
            "body": "ObsTurret",
            "gun": "ObsGun",
            "animationsourcebody": "ObsTurret",
            "animationsourcegun": "ObsGun",
            "gunbeg": "flir_end",
            "gunend": "flir_begin",
            "memorypointgun": "flir_end",
            "memorypointgunneroptics": "commanderview",
            "stabilizedinaxes": 3,
            "minelev": -90,
            "maxelev": 38.2,
            "initelev": 0,
            "minturn": -70,
            "maxturn": 70,
            "initturn": 0,
            "gunnername": "Copilot",
            "iscopilot": 1,
            "turretinfotype": "RHS_RscUH1Y_Observer",
            "soundservo": ["",0.01,1,30],
            "weapons": ["rhs_weap_laserDesignator_AI"],
            "magazines": ["rhs_LaserMag_ai"],
            "ingunnermayfire": 1,
            "precisegetinout": 0,
            "gunneropticseffect": [],
            "gunneropticsmodel": "",
            "gunnerlefthandanimname": "lever_copilot",
            "gunnerrighthandanimname": "stick_copilot",
            "gunnerleftleganimname": "pedalL",
            "gunnerrightleganimname": "pedalR",
            "usepip": 1,
            "caneject": 1,
            "primarygunner": 1,
            "proxyindex": 1,
            "commanding": -1,
            "gunneropticsshowcursor": 1,
            "showgunneroptics": 1,
            "gunnerforceoptics": 0,
            "gunneropticscolor": [0.227,0.769,0.24,1],
            "gunnerforceoutoptics": 0,
            "gunnerusespilotview": 0,
            "hasgunner": 1,
            "hideweaponsgunner": 1,
            "lockwhendriverout": 0,
            "enablemanualfire": 1,
            "maxhorizontalrotspeed": 3.2,
            "maxverticalrotspeed": 3.2,
            "outgunnermayfire": 1,
            "showhmd": 0,
            # Class: CfgVehicles|rhsusf_CH53E_USMC|Turrets|CopilotTurret|OpticsIn [Indent level: 3],
            "opticsin": {
                # Class: CfgVehicles|rhsusf_CH53E_USMC|Turrets|CopilotTurret|OpticsIn|WideNGS [Indent level: 4]
                "widengs": {
                    "opticsdisplayname": "W",
                    "initanglex": 0,
                    "minanglex": -80,
                    "maxanglex": 20,
                    "initangley": 0,
                    "minangley": -100,
                    "maxangley": 100,
                    "initfov": 1,
                    "minfov": 1,
                    "maxfov": 1,
                    "visionmode": ["Normal","Ti"],
                    "thermalmode": [0,1],
                    "gunneropticscolor": [1,0,0,0],
                    "gunneropticsmodel": "a3|weapons_f|Reticle|Optics_Gunner_AAA_01_w_F.p3d",
                    "directionstabilized": 0
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|Turrets|CopilotTurret|OpticsIn|Wide [Indent level: 4],
                "wide": {
                    "opticsdisplayname": "W",
                    "initanglex": 0,
                    "minanglex": -80,
                    "maxanglex": 20,
                    "initangley": 0,
                    "minangley": -100,
                    "maxangley": 100,
                    "initfov": 0.466,
                    "minfov": 0.466,
                    "maxfov": 0.466,
                    "visionmode": ["Normal","Ti"],
                    "thermalmode": [0,1],
                    "gunneropticscolor": [1,0,0,0],
                    "gunneropticsmodel": "a3|weapons_f|Reticle|Optics_Gunner_AAA_01_m_F.p3d",
                    "directionstabilized": 1,
                    "stabilizedinaxes": 3
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|Turrets|CopilotTurret|OpticsIn|WideL [Indent level: 4],
                "widel": {
                    "opticsdisplayname": "WL",
                    "initfov": 0.2,
                    "minfov": 0.2,
                    "maxfov": 0.2,
                    "initanglex": 0,
                    "minanglex": -80,
                    "maxanglex": 20,
                    "initangley": 0,
                    "minangley": -100,
                    "maxangley": 100,
                    "visionmode": ["Normal","Ti"],
                    "thermalmode": [0,1],
                    "gunneropticscolor": [1,0,0,0],
                    "gunneropticsmodel": "a3|weapons_f|Reticle|Optics_Gunner_AAA_01_m_F.p3d",
                    "directionstabilized": 1,
                    "stabilizedinaxes": 3
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|Turrets|CopilotTurret|OpticsIn|Medium [Indent level: 4],
                "medium": {
                    "opticsdisplayname": "M",
                    "initfov": 0.1,
                    "minfov": 0.1,
                    "maxfov": 0.1,
                    "initanglex": 0,
                    "minanglex": -80,
                    "maxanglex": 20,
                    "initangley": 0,
                    "minangley": -100,
                    "maxangley": 100,
                    "visionmode": ["Normal","Ti"],
                    "thermalmode": [0,1],
                    "gunneropticscolor": [1,0,0,0],
                    "gunneropticsmodel": "a3|weapons_f|Reticle|Optics_Gunner_AAA_01_m_F.p3d",
                    "directionstabilized": 1,
                    "stabilizedinaxes": 3
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|Turrets|CopilotTurret|OpticsIn|Narrow [Indent level: 4],
                "narrow": {
                    "opticsdisplayname": "N",
                    "initfov": 0.02,
                    "minfov": 0.02,
                    "maxfov": 0.02,
                    "initanglex": 0,
                    "minanglex": -80,
                    "maxanglex": 20,
                    "initangley": 0,
                    "minangley": -100,
                    "maxangley": 100,
                    "visionmode": ["Normal","Ti"],
                    "thermalmode": [0,1],
                    "gunneropticscolor": [1,0,0,0],
                    "gunneropticsmodel": "a3|weapons_f|Reticle|Optics_Gunner_AAA_01_m_F.p3d",
                    "directionstabilized": 1,
                    "stabilizedinaxes": 3
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|Turrets|CopilotTurret|OpticsIn|Narrower [Indent level: 4],
                "narrower": {
                    "opticsdisplayname": "N",
                    "initfov": 0.01,
                    "minfov": 0.01,
                    "maxfov": 0.01,
                    "initanglex": 0,
                    "minanglex": -80,
                    "maxanglex": 20,
                    "initangley": 0,
                    "minangley": -100,
                    "maxangley": 100,
                    "visionmode": ["Normal","Ti"],
                    "thermalmode": [0,1],
                    "gunneropticscolor": [1,0,0,0],
                    "gunneropticsmodel": "a3|weapons_f|Reticle|Optics_Gunner_AAA_01_m_F.p3d",
                    "directionstabilized": 1,
                    "stabilizedinaxes": 3
                }
            },
            # Class: CfgVehicles|rhsusf_CH53E_USMC|Turrets|CopilotTurret|OpticsOut [Indent level: 3],
            "opticsout": {
                # Class: CfgVehicles|rhsusf_CH53E_USMC|Turrets|CopilotTurret|OpticsOut|Monocular [Indent level: 4]
                "monocular": {
                    "initanglex": 0,
                    "minanglex": -30,
                    "maxanglex": 30,
                    "initangley": 0,
                    "minangley": -100,
                    "maxangley": 100,
                    "initfov": 1.1,
                    "minfov": 0.133,
                    "maxfov": 1.1,
                    "visionmode": ["Normal","NVG"],
                    "gunneropticsmodel": "",
                    "gunneropticseffect": []
                }
            },
            # Class: CfgVehicles|rhsusf_CH53E_USMC|Turrets|CopilotTurret|Reflectors [Indent level: 3],
            "reflectors": {
                # Class: CfgVehicles|rhsusf_CH53E_USMC|Turrets|CopilotTurret|Reflectors|cabin [Indent level: 4]
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
                    # Class: CfgVehicles|rhsusf_CH53E_USMC|Turrets|CopilotTurret|Reflectors|cabin|Attenuation [Indent level: 5],
                    "attenuation": {
                        "start": 0,
                        "constant": 0,
                        "linear": 1,
                        "quadratic": 50,
                        "hardlimitstart": 2,
                        "hardlimitend": 2.5
                    }
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|Turrets|CopilotTurret|Reflectors|cargo_light_1 [Indent level: 4],
                "cargo_light_1": {
                    "color": [830,100,100],
                    "position": "cargo_light_1",
                    "direction": "cargo_light_1_dir",
                    "hitpoint": "cargo_light_1",
                    "selection": "cargo_light_1",
                    "intensity": 21,
                    "useflare": 0,
                    "conefadecoef": 0.1,
                    # Class: CfgVehicles|rhsusf_CH53E_USMC|Turrets|CopilotTurret|Reflectors|cargo_light_1|Attenuation [Indent level: 5],
                    "attenuation": {
                        "start": 0,
                        "constant": 0,
                        "linear": 1,
                        "quadratic": 70,
                        "hardlimitstart": 2,
                        "hardlimitend": 3
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
                # Class: CfgVehicles|rhsusf_CH53E_USMC|Turrets|CopilotTurret|Reflectors|cargo_light_2 [Indent level: 4],
                "cargo_light_2": {
                    "position": "cargo_light_2",
                    "direction": "cargo_light_2_dir",
                    "hitpoint": "cargo_light_2",
                    "selection": "cargo_light_2",
                    "color": [830,100,100],
                    "intensity": 21,
                    "useflare": 0,
                    "conefadecoef": 0.1,
                    # Class: CfgVehicles|rhsusf_CH53E_USMC|Turrets|CopilotTurret|Reflectors|cargo_light_1|Attenuation [Indent level: 5],
                    "attenuation": {
                        "start": 0,
                        "constant": 0,
                        "linear": 1,
                        "quadratic": 70,
                        "hardlimitstart": 2,
                        "hardlimitend": 3
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
                # Class: CfgVehicles|rhsusf_CH53E_USMC|Turrets|CopilotTurret|Reflectors|cargo_light_3 [Indent level: 4],
                "cargo_light_3": {
                    "position": "cargo_light_3",
                    "direction": "cargo_light_3_dir",
                    "hitpoint": "cargo_light_3",
                    "selection": "cargo_light_3",
                    "color": [830,100,100],
                    "intensity": 21,
                    "useflare": 0,
                    "conefadecoef": 0.1,
                    # Class: CfgVehicles|rhsusf_CH53E_USMC|Turrets|CopilotTurret|Reflectors|cargo_light_1|Attenuation [Indent level: 5],
                    "attenuation": {
                        "start": 0,
                        "constant": 0,
                        "linear": 1,
                        "quadratic": 70,
                        "hardlimitstart": 2,
                        "hardlimitend": 3
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
            # Class: CfgVehicles|rhsusf_CH53E_USMC|Turrets|CopilotTurret|Components [Indent level: 3],
            "components": {
                # Class: CfgVehicles|rhsusf_CH53E_USMC|Turrets|CopilotTurret|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 4]
                "vehiclesystemsdisplaymanagercomponentleft": {
                    # Class: CfgVehicles|rhsusf_CH53E_USMC|Turrets|CopilotTurret|Components|VehicleSystemsDisplayManagerComponentLeft|Components [Indent level: 5]
                    "components": {
                        # Class: CfgVehicles|rhsusf_CH53E_USMC|Turrets|CopilotTurret|Components|VehicleSystemsDisplayManagerComponentLeft|Components|EmptyDisplay [Indent level: 6]
                        "emptydisplay": {
                            "componenttype": "EmptyDisplayComponent"
                        },
                        # Class: CfgVehicles|rhsusf_CH53E_USMC|Turrets|CopilotTurret|Components|VehicleSystemsDisplayManagerComponentLeft|Components|MinimapDisplay [Indent level: 6],
                        "minimapdisplay": {
                            "componenttype": "MinimapDisplayComponent",
                            "resource": "RscCustomInfoMiniMap"
                        },
                        # Class: CfgVehicles|rhsusf_CH53E_USMC|Turrets|CopilotTurret|Components|VehicleSystemsDisplayManagerComponentLeft|Components|CrewDisplay [Indent level: 6],
                        "crewdisplay": {
                            "componenttype": "CrewDisplayComponent",
                            "resource": "RscCustomInfoCrew"
                        },
                        # Class: CfgVehicles|rhsusf_CH53E_USMC|Turrets|CopilotTurret|Components|VehicleSystemsDisplayManagerComponentLeft|Components|SensorDisplay [Indent level: 6],
                        "sensordisplay": {
                            "componenttype": "SensorsDisplayComponent",
                            "range": [4000,8000,16000,25000],
                            "resource": "RscCustomInfoSensors"
                        },
                        # Class: CfgVehicles|rhsusf_CH53E_USMC|Turrets|CopilotTurret|Components|VehicleSystemsDisplayManagerComponentLeft|Components|VehicleGunnerDisplay [Indent level: 6],
                        "vehiclegunnerdisplay": {
                            "componenttype": "TransportFeedDisplayComponent",
                            "source": "PrimaryGunner"
                        }
                    },
                    "componenttype": "VehicleSystemsDisplayManager",
                    "left": 1,
                    "defaultdisplay": "EmptyDisplay",
                    "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,	(safezoneX + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40))])",
                    "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|Turrets|CopilotTurret|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 4],
                "vehiclesystemsdisplaymanagercomponentright": {
                    "defaultdisplay": "SensorDisplay",
                    # Class: CfgVehicles|rhsusf_CH53E_USMC|Turrets|CopilotTurret|Components|VehicleSystemsDisplayManagerComponentRight|Components [Indent level: 5],
                    "components": {
                        # Class: CfgVehicles|rhsusf_CH53E_USMC|Turrets|CopilotTurret|Components|VehicleSystemsDisplayManagerComponentRight|Components|EmptyDisplay [Indent level: 6]
                        "emptydisplay": {
                            "componenttype": "EmptyDisplayComponent"
                        },
                        # Class: CfgVehicles|rhsusf_CH53E_USMC|Turrets|CopilotTurret|Components|VehicleSystemsDisplayManagerComponentRight|Components|MinimapDisplay [Indent level: 6],
                        "minimapdisplay": {
                            "componenttype": "MinimapDisplayComponent",
                            "resource": "RscCustomInfoMiniMap"
                        },
                        # Class: CfgVehicles|rhsusf_CH53E_USMC|Turrets|CopilotTurret|Components|VehicleSystemsDisplayManagerComponentRight|Components|CrewDisplay [Indent level: 6],
                        "crewdisplay": {
                            "componenttype": "CrewDisplayComponent",
                            "resource": "RscCustomInfoCrew"
                        },
                        # Class: CfgVehicles|rhsusf_CH53E_USMC|Turrets|CopilotTurret|Components|VehicleSystemsDisplayManagerComponentRight|Components|SensorDisplay [Indent level: 6],
                        "sensordisplay": {
                            "componenttype": "SensorsDisplayComponent",
                            "range": [4000,8000,16000,25000],
                            "resource": "RscCustomInfoSensors"
                        },
                        # Class: CfgVehicles|rhsusf_CH53E_USMC|Turrets|CopilotTurret|Components|VehicleSystemsDisplayManagerComponentRight|Components|VehicleGunnerDisplay [Indent level: 6],
                        "vehiclegunnerdisplay": {
                            "componenttype": "TransportFeedDisplayComponent",
                            "source": "PrimaryGunner"
                        }
                    },
                    "componenttype": "VehicleSystemsDisplayManager",
                    "right": 1,
                    "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,	((safezoneX + safezoneW) - (		(10 * 			(			((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40)))])",
                    "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                }
            },
            "startengine": 0,
            "gunnerhasflares": 0,
            "turretcansee": "1 + 2 + 4 + 8 + 32",
            # Class: CfgVehicles|Helicopter|Turrets|MainTurret|TurretSpec [Indent level: 3],
            "turretspec": {
                "showheadphones": 1
            },
            "selectionfireanim": "zasleh",
            "castgunnershadow": 1,
            "viewgunnershadow": 1,
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
            "gunneroutopticsmodel": "",
            "gunneroutopticscolor": [0,0,0,1],
            "gunneroutopticseffect": [],
            "memorypointgunneroutoptics": "",
            "gunneroutforceoptics": 0,
            "gunneroutopticsshowcursor": 0,
            "gunnerfirealsoininternalcamera": 1,
            "gunneroutfirealsoininternalcamera": 1,
            "viewgunnershadowdiff": 1,
            "viewgunnershadowamb": 1,
            "ejectdeadgunner": 0,
            "canhidegunner": -1,
            "forcehidegunner": 0,
            "viewgunnerinexternal": 0,
            "lockwhenvehiclespeed": -1,
            "gunnercompartments": "Compartment1",
            "memorypointsgetingunnerprecise": "",
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
            "showcrewaim": 0
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC_GAU21_D|Turrets|GAU21 [Indent level: 2],
        "gau21": {
            "gunnertype": "rhsusf_usmc_marpat_d_helicrew",
            "usepip": 0,
            "iscopilot": 0,
            "showascargo": 1,
            "proxyindex": 2,
            "animationsourcebody": "mainTurret",
            "animationsourcegun": "mainGun",
            "body": "mainTurret",
            "gun": "mainGun",
            "minelev": -60,
            "maxelev": 7,
            "initelev": 0,
            "minturn": 90,
            "maxturn": 270,
            "initturn": 180,
            "lodturnedout": 1200,
            "lodturnedin": 1200,
            "lodopticsout": 1200,
            "lodopticsin": 1200,
            "soundservo": ["",0.01,1],
            "gunnerlefthandanimname": "OtocHlaven_1",
            "gunnerrighthandanimname": "OtocHlaven_1",
            "gunnerleftleganimname": "gunner_1_leg_left",
            "gunnerrightleganimname": "gunner_1_legs",
            "gunneraction": "RHS_Ch53_Gunner_Ramp",
            "gunnerinaction": "RHS_Ch53_Gunner_Ramp",
            "animationsourcehatch": "",
            "stabilizedinaxes": "StabilizedInAxesNone",
            "gunbeg": "muzzle_1",
            "gunend": "chamber_1",
            "selectionfireanim": "zasleh_1",
            "weapons": ["rhs_weap_gau21_1"],
            "magazines": ["rhs_mag_300rnd_127x99_mag_Tracer_Red","rhs_mag_300rnd_127x99_mag_Tracer_Red","rhs_mag_300rnd_127x99_mag_Tracer_Red"],
            "gunnername": "Ramp GAU-21",
            "gunneropticsmodel": "A3|weapons_f|reticle|optics_empty",
            "gunneroutopticsshowcursor": 1,
            "gunneropticsshowcursor": 1,
            "memorypointsgetingunner": "pos cargo",
            "memorypointsgetingunnerdir": "pos cargo dir",
            "gunnergetinaction": "GetInLow",
            "gunnergetoutaction": "GetOutLow",
            "precisegetinout": 0,
            "turretinfotype": "RscWeaponZeroing",
            "commanding": -2,
            "playerposition": 1,
            "primarygunner": 0,
            # Class: CfgVehicles|rhsusf_CH53E_USMC_GAU21|Turrets|GAU21|ViewOptics [Indent level: 3],
            "viewoptics": {
                "initanglex": 0,
                "initangley": 0,
                "initfov": 0.7,
                "maxanglex": 75,
                "maxangley": 100,
                "maxfov": 1.1,
                "minanglex": -75,
                "minangley": -100,
                "minfov": 0.25
            },
            # Class: CfgVehicles|rhsusf_CH53E_USMC_GAU21|Turrets|GAU21|ViewGunner [Indent level: 3],
            "viewgunner": {
                "initanglex": 0,
                "initangley": 0,
                "initfov": 0.7,
                "maxanglex": 75,
                "maxangley": 100,
                "maxfov": 1.1,
                "minanglex": -75,
                "minangley": -100,
                "minfov": 0.25,
                "visionmode": []
            },
            # Class: CfgVehicles|rhsusf_CH53E_USMC_GAU21|Turrets|GAU21|OpticsIn [Indent level: 3],
            "opticsin": {
                # Class: CfgVehicles|rhsusf_CH53E_USMC_GAU21|Turrets|GAU21|OpticsIn|ViewOptics [Indent level: 4]
                "viewoptics": {
                    "gunneropticsmodel": "A3|weapons_f|reticle|optics_empty",
                    "gunneroutopticsmodel": "A3|weapons_f|reticle|optics_empty",
                    "initanglex": 0,
                    "initangley": 0,
                    "initfov": 0.7,
                    "maxanglex": 75,
                    "maxangley": 100,
                    "maxfov": 1.1,
                    "minanglex": -75,
                    "minangley": -100,
                    "minfov": 0.25,
                    "visionmode": []
                }
            },
            "gunnercompartments": "Compartment2",
            "memorypointgun": "muzzle_1",
            "memorypointgunneroptics": "gunnerview_1",
            "soundattenuationturret": "HeliAttenuationGunner",
            # Class: CfgVehicles|rhsusf_CH53E_USMC_GAU21|Turrets|GAU21|Reflectors [Indent level: 3],
            "reflectors": {
            },
            # Class: CfgVehicles|rhsusf_CH53E_USMC_GAU21|Turrets|GAU21|Components [Indent level: 3],
            "components": {
                # Class: CfgVehicles|rhsusf_CH53E_USMC_GAU21|Turrets|GAU21|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 4]
                "vehiclesystemsdisplaymanagercomponentleft": {
                    # Class: CfgVehicles|rhsusf_CH53E_USMC_GAU21|Turrets|GAU21|Components|VehicleSystemsDisplayManagerComponentLeft|Components [Indent level: 5]
                    "components": {
                        # Class: CfgVehicles|rhsusf_CH53E_USMC_GAU21|Turrets|GAU21|Components|VehicleSystemsDisplayManagerComponentLeft|Components|EmptyDisplay [Indent level: 6]
                        "emptydisplay": {
                            "componenttype": "EmptyDisplayComponent"
                        },
                        # Class: CfgVehicles|rhsusf_CH53E_USMC_GAU21|Turrets|GAU21|Components|VehicleSystemsDisplayManagerComponentLeft|Components|CrewDisplay [Indent level: 6],
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
                # Class: CfgVehicles|rhsusf_CH53E_USMC_GAU21|Turrets|GAU21|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 4],
                "vehiclesystemsdisplaymanagercomponentright": {
                    "defaultdisplay": "SensorDisplay",
                    # Class: CfgVehicles|rhsusf_CH53E_USMC_GAU21|Turrets|GAU21|Components|VehicleSystemsDisplayManagerComponentRight|Components [Indent level: 5],
                    "components": {
                        # Class: CfgVehicles|rhsusf_CH53E_USMC_GAU21|Turrets|GAU21|Components|VehicleSystemsDisplayManagerComponentRight|Components|EmptyDisplay [Indent level: 6]
                        "emptydisplay": {
                            "componenttype": "EmptyDisplayComponent"
                        },
                        # Class: CfgVehicles|rhsusf_CH53E_USMC_GAU21|Turrets|GAU21|Components|VehicleSystemsDisplayManagerComponentRight|Components|CrewDisplay [Indent level: 6],
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
            # Class: CfgVehicles|rhsusf_CH53E_USMC_GAU21|Turrets|GAU21|Hitpoints [Indent level: 3],
            "hitpoints": {
            },
            "turretcansee": "1 + 2 + 4 + 8 + 32",
            # Class: CfgVehicles|Helicopter|Turrets|MainTurret|TurretSpec [Indent level: 3],
            "turretspec": {
                "showheadphones": 1
            },
            "startengine": 0,
            "outgunnermayfire": 1,
            "castgunnershadow": 1,
            "viewgunnershadow": 1,
            "gunnerforceoptics": 0,
            "enablemanualfire": 0,
            "caneject": 0,
            "animationsourcecamelev": "camElev",
            "proxytype": "CPGunner",
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
            "gunneropticscolor": [0,0,0,1],
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
            "memorypointsgetingunnerprecise": "",
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
            "forcenvg": 0,
            "gunnerdoor": "",
            "turretfollowfreelook": 0,
            "allowtablock": 1,
            "showalltargets": 0,
            "dontcreateai": 0,
            "disablesoundattenuation": 0,
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
            "showcrewaim": 0
        },
        # Class: CfgVehicles|Helicopter_Base_H|Turrets|MainTurret [Indent level: 2],
        "mainturret": {
            "gunneropticsmodel": "",
            "turretcansee": "1 + 2 + 4 + 8 + 32",
            # Class: CfgVehicles|Helicopter|Turrets|MainTurret|TurretSpec [Indent level: 3],
            "turretspec": {
                "showheadphones": 1
            },
            "startengine": 0,
            "outgunnermayfire": 1,
            "commanding": -1,
            "memorypointsgetingunner": "pos gunner",
            "memorypointsgetingunnerdir": "pos gunner dir",
            "gunnergetinaction": "GetInLow",
            "gunnergetoutaction": "GetOutLow",
            "memorypointgun": "machinegun",
            "memorypointgunneroptics": "gunnerview",
            "selectionfireanim": "zasleh",
            "castgunnershadow": 1,
            "viewgunnershadow": 1,
            "gunnerforceoptics": 0,
            "enablemanualfire": 0,
            "caneject": 0,
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
            "iscopilot": 0,
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
            "showcrewaim": 0
        }
    },
    "displayname": "CH-53E (GAU-21)",
    # Class: CfgVehicles|rhsusf_CH53E_USMC_GAU21|AnimationSources [Indent level: 1],
    "animationsources": {
        # Class: CfgVehicles|rhsusf_CH53E_USMC_GAU21|AnimationSources|hmg_hide [Indent level: 2]
        "hmg_hide": {
            "initphase": 0,
            "source": "user",
            "animperiod": 0
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC_GAU21|AnimationSources|Ramp [Indent level: 2],
        "ramp": {
            "initphase": 0.56,
            "source": "user",
            "animperiod": 4,
            "sound": "CH53_Rampsound"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC_GAU21|AnimationSources|Ramp_hmg [Indent level: 2],
        "ramp_hmg": {
            "initphase": 1,
            "source": "user",
            "animperiod": 4,
            "sound": "CH53_Rampsound"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC_GAU21|AnimationSources|muzzle_rot_hmg_1 [Indent level: 2],
        "muzzle_rot_hmg_1": {
            "weapon": "rhs_weap_gau21_1",
            "source": "ammorandom"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC_GAU21|AnimationSources|reload_hmg_1 [Indent level: 2],
        "reload_hmg_1": {
            "source": "reload",
            "weapon": "rhs_weap_gau21_1"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|AnimationSources|cargolights_hide [Indent level: 2],
        "cargolights_hide": {
            "source": "user",
            "animperiod": 1e-006,
            "initphase": 0
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|AnimationSources|cabinlights_hide [Indent level: 2],
        "cabinlights_hide": {
            "source": "user",
            "animperiod": 1e-006,
            "initphase": 0
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|AnimationSources|mainRotor_folded [Indent level: 2],
        "mainrotor_folded": {
            "source": "door",
            "animperiod": 10,
            "initphase": 0
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|AnimationSources|hide_winch [Indent level: 2],
        "hide_winch": {
            "source": "user",
            "displayname": "hide winch",
            "animperiod": 0,
            "initphase": 0
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|AnimationSources|hide_ANAAQ24 [Indent level: 2],
        "hide_anaaq24": {
            "source": "user",
            "displayname": "hide DIRCM",
            "animperiod": 0,
            "initphase": 0
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|AnimationSources|mainRotor_folded_handler [Indent level: 2],
        "mainrotor_folded_handler": {
            "animperiod": 1e-005,
            "initphase": 0,
            "mass": 1,
            "displayname": "fold rotors",
            "onphasechanged": "_this call rhsusf_fnc_ch53_fold",
            "source": "user",
            "sound": "CH53_Rampsound"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|AnimationSources|hide_cargo [Indent level: 2],
        "hide_cargo": {
            "source": "user",
            "mass": -20,
            "displayname": "hide cargo benches",
            "animperiod": 1e-005,
            "initphase": 0,
            "onphasechanged": "(_this select 0) lockCargo ((_this select 1)==1)"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|AnimationSources|HitGlass1 [Indent level: 2],
        "hitglass1": {
            "source": "Hit",
            "hitpoint": "HitGlass1",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|AnimationSources|HitGlass2 [Indent level: 2],
        "hitglass2": {
            "hitpoint": "HitGlass2",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|AnimationSources|HitGlass3 [Indent level: 2],
        "hitglass3": {
            "hitpoint": "HitGlass3",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|AnimationSources|HitGlass4 [Indent level: 2],
        "hitglass4": {
            "hitpoint": "HitGlass4",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|AnimationSources|HitGlass5 [Indent level: 2],
        "hitglass5": {
            "hitpoint": "HitGlass5",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|AnimationSources|HitGlass6 [Indent level: 2],
        "hitglass6": {
            "hitpoint": "HitGlass6",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|AnimationSources|HitGlass7 [Indent level: 2],
        "hitglass7": {
            "hitpoint": "HitGlass7",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|AnimationSources|HitGlass8 [Indent level: 2],
        "hitglass8": {
            "hitpoint": "HitGlass8",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|AnimationSources|HitGlass9 [Indent level: 2],
        "hitglass9": {
            "hitpoint": "HitGlass9",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|AnimationSources|HitGlass10 [Indent level: 2],
        "hitglass10": {
            "hitpoint": "HitGlass10",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|AnimationSources|HitGlass11 [Indent level: 2],
        "hitglass11": {
            "hitpoint": "HitGlass11",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|AnimationSources|HitGlass12 [Indent level: 2],
        "hitglass12": {
            "hitpoint": "HitGlass12",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|AnimationSources|HitGlass13 [Indent level: 2],
        "hitglass13": {
            "hitpoint": "HitGlass13",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|AnimationSources|HitGlass14 [Indent level: 2],
        "hitglass14": {
            "hitpoint": "HitGlass14",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|AnimationSources|HitGlass15 [Indent level: 2],
        "hitglass15": {
            "hitpoint": "HitGlass15",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|AnimationSources|HitGlass16 [Indent level: 2],
        "hitglass16": {
            "hitpoint": "HitGlass16",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|AnimationSources|HitGlass17 [Indent level: 2],
        "hitglass17": {
            "hitpoint": "HitGlass17",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|AnimationSources|Damper_1_source [Indent level: 2],
        "damper_1_source": {
            "source": "damper",
            "wheel": "Wheel_1"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|AnimationSources|Damper_2_source [Indent level: 2],
        "damper_2_source": {
            "source": "damper",
            "wheel": "Wheel_2"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|AnimationSources|Damper_3_source [Indent level: 2],
        "damper_3_source": {
            "source": "damper",
            "wheel": "Wheel_3"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|AnimationSources|Wheel_1_source [Indent level: 2],
        "wheel_1_source": {
            "source": "wheel",
            "wheel": "Wheel_1"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|AnimationSources|Wheel_2_source [Indent level: 2],
        "wheel_2_source": {
            "source": "wheel",
            "wheel": "Wheel_2"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|AnimationSources|Wheel_3_source [Indent level: 2],
        "wheel_3_source": {
            "source": "wheel",
            "wheel": "Wheel_3"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|AnimationSources|mainturret [Indent level: 2],
        "mainturret": {
            "source": "user",
            "animperiod": 0,
            "initphase": 0
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|AnimationSources|maingun [Indent level: 2],
        "maingun": {
            "source": "user",
            "animperiod": 0,
            "initphase": 0
        }
    },
    # Class: CfgVehicles|rhsusf_CH53E_USMC_GAU21|UVAnimations [Indent level: 1],
    "uvanimations": {
        # Class: CfgVehicles|rhsusf_CH53E_USMC_GAU21|UVAnimations|hmg_ammo_1 [Indent level: 2]
        "hmg_ammo_1": {
            "type": "translation",
            "source": "reload_hmg_1",
            "sourceaddress": "loop",
            "section": "hmg_ammo_1",
            "minvalue": 0,
            "maxvalue": 1,
            "offset0": [0,0],
            "offset1": [0.038,0]
        }
    },
    # Class: CfgVehicles|rhsusf_CH53E_USMC_GAU21|UserActions [Indent level: 1],
    "useractions": {
        # Class: CfgVehicles|rhsusf_CH53E_USMC_GAU21|UserActions|RampClose [Indent level: 2]
        "rampclose": {
            "condition": 0,
            "displayname": "Close Ramp",
            "statement": "this animate ['ramp_bottom',0];this animate ['ramp_top',0];[this] call rhs_fnc_cargoAttach",
            "position": "ramp action",
            "showwindow": 0,
            "radius": 5,
            "onlyforplayer": 0,
            "shortcut": "user12"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC_GAU21|UserActions|VehicleParadrop [Indent level: 2],
        "vehicleparadrop": {
            "condition": 0,
            "displayname": "Paradrop cargo",
            "statement": "[this] spawn rhs_fnc_vehPara",
            "shortcut": "",
            "position": "ramp action",
            "showwindow": 0,
            "radius": 5,
            "onlyforplayer": 0
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|UserActions|Pack [Indent level: 2],
        "pack": {
            "displayname": "Pack",
            "displaynamedefault": "Pack",
            "position": "PackAction",
            "radius": 10,
            "onlyforplayer": 1,
            "condition": "(!isEngineOn this) AND {(this doorPhase 'mainRotor_folded' isEqualTo 0) AND ((driver this) isEqualTo (call rhs_fnc_findPlayer)) AND (speed this == 0)}",
            "statement": "[this,1] call rhsusf_fnc_ch53_fold"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|UserActions|unPack [Indent level: 2],
        "unpack": {
            "displayname": "UnPack",
            "displaynamedefault": "Unpack",
            "position": "PackAction",
            "radius": 10,
            "onlyforplayer": 1,
            "condition": "(this doorPhase 'mainRotor_folded' isEqualTo 1) AND ((driver this) isEqualTo (call rhs_fnc_findPlayer))",
            "statement": "[this,0] call rhsusf_fnc_ch53_fold"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|UserActions|RampOpen [Indent level: 2],
        "rampopen": {
            "displayname": "Open Ramp",
            "position": "ramp action",
            "showwindow": 0,
            "radius": 5,
            "condition": "this animationPhase 'ramp_bottom' <= 0.56 && ((driver this) isEqualTo (call rhs_fnc_findPlayer));",
            "statement": "this animate ['ramp_bottom',1];this animate ['ramp_top',1];[this] call rhs_fnc_cargoDetach",
            "onlyforplayer": 0,
            "shortcut": "user12"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|UserActions|RampLevel [Indent level: 2],
        "ramplevel": {
            "displayname": "Level Ramp",
            "condition": "this animationPhase 'ramp_bottom' != 0.56 && ((driver this) isEqualTo (call rhs_fnc_findPlayer));",
            "statement": "this animate ['ramp_bottom',0.56];this animate ['ramp_top',1];",
            "shortcut": "user13",
            "position": "ramp action",
            "showwindow": 0,
            "radius": 5,
            "onlyforplayer": 0
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|UserActions|ToggleLight [Indent level: 2],
        "togglelight": {
            "displayname": "Toggle interior light",
            "position": "pos driver",
            "radius": 15,
            "showwindow": 0,
            "condition": "player in this;",
            "statement": "[this,'cargolights_hide'] call rhs_fnc_toggleIntLight",
            "onlyforplayer": 1
        }
    },
    # Class: CfgVehicles|rhsusf_CH53E_USMC_GAU21|Attributes [Indent level: 1],
    "attributes": {
        # Class: CfgVehicles|rhsusf_CH53E_USMC_GAU21|Attributes|ObjectTexture [Indent level: 2]
        "objecttexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayname": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC_GAU21|Attributes|rhs_decalNumber_type [Indent level: 2],
        "rhs_decalnumber_type": {
            "displayname": "Define font type of side number",
            "tooltip": "Define kind of font that will be drawn on vehicle",
            "property": "rhs_decalNumber_type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];[_this,[['Number', cCH53NumberPlaces, _value]]] call rhsusf_fnc_decalsInit",
            "defaultvalue": 0,
            "typename": "STRING",
            # Class: CfgVehicles|rhsusf_CH53E_USMC_GAU21|Attributes|rhs_decalNumber_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhsusf_CH53E_USMC_GAU21|Attributes|rhs_decalNumber_type|values|USMCGrey [Indent level: 4]
                "usmcgrey": {
                    "name": "USMC (Grey)",
                    "value": "USMCGrey",
                    "defaultvalue": "USMCGrey"
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC_GAU21|Attributes|rhs_decalNumber_type|values|USMCBlackShadow [Indent level: 4],
                "usmcblackshadow": {
                    "name": "USMC (Black Shadow)",
                    "value": "USMCBlackShadow"
                }
            }
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC_GAU21|Attributes|rhs_decalNumber [Indent level: 2],
        "rhs_decalnumber": {
            "displayname": "Set side number",
            "tooltip": "Set side number. 2 numbers are required. If 0, random number will be generated",
            "property": "rhs_decalNumber",
            "control": "Edit",
            "validate": "Number",
            "typename": "Number",
            "defaultvalue": "-1",
            "expression": "if( _value >= 0)then{[_this, [['Number', cCH53NumberPlaces, _this getVariable ['rhs_decalNumber_type','USMCGrey'], _value] ] ] call rhsusf_fnc_decalsInit};"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC_GAU21|Attributes|rhs_openRamp [Indent level: 2],
        "rhs_openramp": {
            "displayname": "Open rear ramp",
            "property": "rhs_openRamp",
            "control": "slider",
            "expression": "_this animate ['ramp_bottom',_value];",
            "defaultvalue": "0"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC_GAU21|Attributes|FoldHeli [Indent level: 2],
        "foldheli": {
            "control": "CheckboxNumber",
            "defaultvalue": "0",
            "displayname": "Fold helicopter rotors",
            "property": "FoldHeli",
            "expression": "[_this,_value,true] call rhsusf_fnc_ch53_fold"
        }
    },
    "rhs_decalparameters": ["['Number', cCH53NumberPlaces, _typeNum,_randomNum]"],
    "rhs_pararamp": "ramp",
    "rhs_paraoff": -15,
    "rhs_rampanim": "ramp_bottom",
    "rhs_gearanim": "Gear_Nose_1",
    "rhs_parascript": "rhs_fnc_vehPara",
    "rhs_hasnoradar": 1,
    "scope": 2,
    "model": "rhsusf|addons|rhsusf_ch53|rhsusf_ch53_e.p3d",
    "expansion": 3,
    "dlc": "RHS_USAF",
    "mapsize": 40,
    "icon": "rhsusf|addons|rhsusf_ch53|data|ui|ch53_icon_ca.paa",
    "picture": "rhsusf|addons|rhsusf_ch53|data|ui|ch53_picture_ca.paa",
    "irtarget": 1,
    "irtargetsize": 1.2,
    "visualtarget": 1,
    "visualtargetsize": 1.3,
    "radartarget": 1,
    "radartargetsize": 1.12,
    "radartype": 4,
    "lockdetectionsystem": "8",
    "incomingmissiledetectionsystem": "2 + 8 + 16",
    "lesh_canbetowed": 1,
    "lesh_towfromfront": 1,
    "lesh_axisoffsettarget": [0,9.8,0.9],
    "lesh_wheeloffset": [0,-3.6],
    "side": 1,
    "destrtype": "DestructWreck",
    "availableforsupporttypes": ["Drop","Transport"],
    "transportsoldier": 24,
    "maxspeed": 315,
    "accuracy": 0.5,
    "useprecisegetinaction": 0,
    "memorypointsgetindriverprecise": "pos driver",
    "memorypointsgetincargoprecise": ["pos cargo"],
    "precisegetinout": 0,
    "cargoprecisegetinout": [0],
    "getinaction": "GetInLow",
    "getoutaction": "GetOutLow",
    "cargogetinaction": ["GetInLow"],
    "cargogetoutaction": ["GetOutLow"],
    "driverdoor": "",
    "cargodoors": [],
    "castcargoshadow": 1,
    "driveraction": "RHS_CH53_Pilot",
    "cargoaction": ["ChopperHeavy_LP_Static_H"],
    "maximumload": 14500,
    "cargocaneject": 1,
    "drivercaneject": 0,
    "hideweaponscargo": 1,
    "cost": 1e+007,
    "fuelcapacity": 2500,
    "fuelconsumptionrate": 0.138,
    "extcameraposition": [0,5,-30],
    "threat": [0.3,0.2,0.3],
    "maxfordingdepth": 1.65,
    "waterleakiness": 0.2,
    "liftforcecoef": 1.5,
    "bodyfrictioncoef": 1,
    "cyclicasideforcecoef": 0.5,
    "cyclicforwardforcecoef": 0.3,
    "backrotorforcecoef": 0.3,
    "mainbladeradius": 6,
    "tailbladeradius": 1,
    "tailbladecenter": "mala osa",
    "mainbladecenter": "velka osa",
    "maxomega": 2000,
    # Class: CfgVehicles|rhsusf_CH53E_USMC|Wheels [Indent level: 1],
    "wheels": {
        "disablewheelswhendestroyed": 1,
        # Class: CfgVehicles|rhsusf_CH53E_USMC|Wheels|Wheel_1 [Indent level: 2],
        "wheel_1": {
            "steering": 1,
            "side": "left",
            "bonename": "damper_nose_piston",
            "suspforceapppointoffset": "wheel_nose_axis",
            "tireforceapppointoffset": "wheel_nose_axis",
            "center": "wheel_nose_axis",
            "boundary": "wheel_nose_bound",
            "susptraveldirection": [0,-1,0],
            "width": 0.637,
            "mass": 15,
            "moi": 0.768,
            "dampingrate": 0.25,
            "dampingratedamaged": 2,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 2000,
            "maxhandbraketorque": 0,
            "maxcompression": 1.05,
            "maxdroop": 0.05,
            "sprungmass": 3000,
            "springstrength": 12000,
            "springdamperrate": 1280,
            "longitudinalstiffnessperunitgravity": 5000,
            "latstiffx": 2.5,
            "latstiffy": 18,
            "frictionvsslipgraph": [[0,1],[0.5,1],[1,1]]
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|Wheels|Wheel_2 [Indent level: 2],
        "wheel_2": {
            "steering": 0,
            "side": "left",
            "bonename": "damper_left_piston",
            "suspforceapppointoffset": "wheel_left_axis",
            "tireforceapppointoffset": "wheel_left_axis",
            "center": "wheel_left_axis",
            "boundary": "wheel_left_bound",
            "maxcompression": 1.05,
            "maxdroop": 0.05,
            "susptraveldirection": [0,-1,0],
            "width": 0.637,
            "mass": 15,
            "moi": 0.768,
            "dampingrate": 0.25,
            "dampingratedamaged": 2,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 2000,
            "maxhandbraketorque": 0,
            "sprungmass": 3000,
            "springstrength": 12000,
            "springdamperrate": 1280,
            "longitudinalstiffnessperunitgravity": 5000,
            "latstiffx": 2.5,
            "latstiffy": 18,
            "frictionvsslipgraph": [[0,1],[0.5,1],[1,1]]
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|Wheels|Wheel_3 [Indent level: 2],
        "wheel_3": {
            "side": "right",
            "bonename": "damper_right_piston",
            "suspforceapppointoffset": "wheel_right_axis",
            "tireforceapppointoffset": "wheel_right_axis",
            "center": "wheel_right_axis",
            "boundary": "wheel_right_bound",
            "steering": 0,
            "maxcompression": 1.05,
            "maxdroop": 0.05,
            "susptraveldirection": [0,-1,0],
            "width": 0.637,
            "mass": 15,
            "moi": 0.768,
            "dampingrate": 0.25,
            "dampingratedamaged": 2,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 2000,
            "maxhandbraketorque": 0,
            "sprungmass": 3000,
            "springstrength": 12000,
            "springdamperrate": 1280,
            "longitudinalstiffnessperunitgravity": 5000,
            "latstiffx": 2.5,
            "latstiffy": 18,
            "frictionvsslipgraph": [[0,1],[0.5,1],[1,1]]
        }
    },
    "gearretracting": 1,
    "driveoncomponent": ["wheels"],
    "gearuptime": 3,
    "geardowntime": 3,
    "hiddenselections": ["camo","camo1","n1","n2"],
    "hiddenselectionstextures": ["rhsusf|addons|rhsusf_ch53|data|ch53_1_co.paa","rhsusf|addons|rhsusf_ch53|data|ch53_acc_co.paa","rhsusf|addons|rhsusf_decals|Data|Numbers|USMCBlackShadow|5_ca.paa","rhsusf|addons|rhsusf_decals|Data|Numbers|USMCBlackShadow|5_ca.paa"],
    # Class: CfgVehicles|rhsusf_CH53E_USMC|textureSources [Indent level: 1],
    "texturesources": {
        # Class: CfgVehicles|rhsusf_CH53E_USMC|textureSources|standard [Indent level: 2]
        "standard": {
            "displayname": "Standard",
            "textures": ["rhsusf|addons|rhsusf_ch53|data|ch53_1_co.paa","rhsusf|addons|rhsusf_ch53|data|ch53_acc_co.paa"],
            "factions": ["rhs_faction_usmc_wd","rhs_faction_usmc_d"]
        }
    },
    "texturelist": [],
    "selectionhrotorstill": "velka vrtule staticka",
    "selectionhrotormove": "velka vrtule blur",
    "selectionvrotorstill": "mala vrtule staticka",
    "selectionvrotormove": "mala vrtule blur",
    "insidesoundcoef": 0.2,
    "attenuationeffecttype": "HeliAttenuation",
    "emptysound": ["",0,1],
    "soundgeneralcollision1": ["A3|Sounds_F|vehicles|crashes|Helis|Heli_coll_default_int_1",1,1,100],
    "soundgeneralcollision2": ["A3|Sounds_F|vehicles|crashes|Helis|Heli_coll_default_int_2",1,1,100],
    "soundgeneralcollision3": ["A3|Sounds_F|vehicles|crashes|Helis|Heli_coll_default_int_3",1,1,100],
    "soundcrashes": ["soundGeneralCollision1",0.33,"soundGeneralCollision2",0.33,"soundGeneralCollision3",0.33],
    "soundlandcrashes": ["emptySound",0],
    "soundbuildingcrash": ["soundGeneralCollision1",1,"soundGeneralCollision2",1,"soundGeneralCollision3",1],
    "soundarmorcrash": ["soundGeneralCollision1",1,"soundGeneralCollision2",1,"soundGeneralCollision3",1],
    "soundwoodcrash": ["soundGeneralCollision1",1,"soundGeneralCollision2",1,"soundGeneralCollision3",1],
    "soundbushcollision1": ["A3|Sounds_F|vehicles|crashes|Helis|Heli_coll_bush_int_1",1,1,100],
    "soundbushcollision2": ["A3|Sounds_F|vehicles|crashes|Helis|Heli_coll_bush_int_2",1,1,100],
    "soundbushcollision3": ["A3|Sounds_F|vehicles|crashes|Helis|Heli_coll_bush_int_3",1,1,100],
    "soundbushcrash": ["soundBushCollision1",0.33,"soundBushCollision2",0.33,"soundBushCollision3",0.33],
    "soundwatercollision1": ["A3|Sounds_F|vehicles|crashes|Helis|Heli_coll_water_ext_1",1,1,100],
    "soundwatercollision2": ["A3|Sounds_F|vehicles|crashes|Helis|Heli_coll_water_ext_2",1,1,100],
    "soundwatercrashes": ["soundWaterCollision1",0.5,"soundWaterCollision2",0.5],
    "soundgetin": ["A3|Sounds_F|vehicles|air|Heli_Transport_02|open",1,1],
    "soundgetout": ["A3|Sounds_F|vehicles|air|Heli_Transport_02|close",1,1,50],
    "sounddammage": ["|rhsusf|addons|rhsusf_ch53|data|betty|dws_warning_beeps",10,1,20],
    "soundengineonint": ["rhsusf|addons|rhsusf_ch53|sounds|Heli_CH53_01_int_start",2,1],
    "soundengineonext": ["rhsusf|addons|rhsusf_ch53|sounds|Heli_CH53_01_ext_start",2,1,800],
    "soundengineoffint": ["rhsusf|addons|rhsusf_ch53|sounds|Heli_CH53_01_int_stop",2,1],
    "soundengineoffext": ["rhsusf|addons|rhsusf_ch53|sounds|Heli_CH53_01_ext_stop",2,1,800],
    "soundlocked": ["|A3|Sounds_F|weapons|Rockets|locked_1",1,1],
    "soundincommingmissile": ["|A3|Sounds_F|weapons|Rockets|locked_3",1,1.5],
    "occludesoundswhenin": 0.562341,
    "obstructsoundswhenin": 0.316228,
    "rotordamageint": ["A3|Sounds_F|vehicles|air|noises|Heli_damage_rotor_int_1",1,1],
    "rotordamageout": ["A3|Sounds_F|vehicles|air|noises|Heli_damage_rotor_ext_1",2.51189,1,300],
    "rotordamage": ["rotorDamageInt","rotorDamageOut"],
    "taildamageint": ["A3|Sounds_F|vehicles|air|noises|Heli_damage_tail",1,1],
    "taildamageout": ["A3|Sounds_F|vehicles|air|noises|Heli_damage_tail",1,1,300],
    "taildamage": ["tailDamageInt","tailDamageOut"],
    "landingsoundint0": ["A3|Sounds_F|vehicles|air|noises|landing_wheels_small_int1",1,1,100],
    "landingsoundint1": ["A3|Sounds_F|vehicles|air|noises|landing_wheels_small_int2",1,1,100],
    "landingsoundint": ["landingSoundInt0",0.5,"landingSoundInt1",0.5],
    "landingsoundout0": ["A3|Sounds_F|vehicles|air|noises|landing_wheels_ext1",1.77828,1,100],
    "landingsoundout1": ["A3|Sounds_F|vehicles|air|noises|landing_wheels_ext2",1.77828,1,100],
    "landingsoundout": ["landingSoundOut0",0.5,"landingSoundOut1",0.5],
    "slingcargoattach0": ["A3|Sounds_F|vehicles|air|noises|SL_engineDownEndINT",1,1],
    "slingcargoattach1": ["A3|Sounds_F|vehicles|air|noises|SL_1hookLock",1,1,80],
    "slingcargoattach": ["slingCargoAttach0","slingCargoAttach1"],
    "slingcargodetach0": ["A3|Sounds_F|vehicles|air|noises|SL_engineUpEndINT",1,1],
    "slingcargodetach1": ["A3|Sounds_F|vehicles|air|noises|SL_1hookUnlock",1,1,80],
    "slingcargodetach": ["slingCargoDetach0","slingCargoDetach1"],
    "slingcargodetachair0": ["A3|Sounds_F|vehicles|air|noises|SL_unhook_air_int",1,1],
    "slingcargodetachair1": ["A3|Sounds_F|vehicles|air|noises|SL_unhook_air_ext",1,1,80],
    "slingcargodetachair": ["slingCargoDetach0","slingCargoDetach1"],
    "slingcargoropebreak0": ["A3|Sounds_F|vehicles|air|noises|SL_rope_break_int",1,1],
    "slingcargoropebreak1": ["A3|Sounds_F|vehicles|air|noises|SL_rope_break_ext",1,1,80],
    "slingcargoropebreak": ["slingCargoDetach0","slingCargoDetach1"],
    "gearupext": ["rhsusf|addons|rhsusf_ch53|sounds|Heli_CH53_01_gear",1,1,1000],
    "gearupint": ["rhsusf|addons|rhsusf_ch53|sounds|Heli_CH53_01_gear",1,1,100],
    "gearup": ["gearUpInt","gearUpExt"],
    "geardownint": ["rhsusf|addons|rhsusf_ch53|sounds|Heli_CH53_01_gear",1,1,100],
    "geardownext": ["rhsusf|addons|rhsusf_ch53|sounds|Heli_CH53_01_gear",1,1,1000],
    "geardown": ["gearDownInt","gearDownExt"],
    # Class: CfgVehicles|rhsusf_CH53E_USMC|Sounds [Indent level: 1],
    "sounds": {
        # Class: CfgVehicles|rhsusf_CH53E_USMC|Sounds|EngineExt [Indent level: 2]
        "engineext": {
            "sound": ["A3|Sounds_F|dummysound",1.41254,1,800],
            "frequency": "rotorSpeed*(1+rotorThrust/6)*0.8",
            "volume": "camPos*((rotorSpeed-0.72)*4)"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|Sounds|RotorExt [Indent level: 2],
        "rotorext": {
            "sound": ["rhsusf|addons|rhsusf_ch53|sounds|Heli_CH53_01_ext_rotor",1,1,3500],
            "frequency": "rotorSpeed / (1-rotorThrust/5)*0.8",
            "volume": "camPos*((rotorSpeed-0.72)*6)",
            "cone": [1.6,3.14,1.6,0.95]
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|Sounds|RotorNoiseExt [Indent level: 2],
        "rotornoiseext": {
            "sound": ["A3|Sounds_F|dummysound",1,1,400],
            "frequency": 1,
            "volume": "camPos * (rotorThrust factor [0.7, 0.9])",
            "cone": [0.7,1.3,1,0]
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|Sounds|EngineInt [Indent level: 2],
        "engineint": {
            "sound": ["rhsusf|addons|rhsusf_ch53|sounds|Heli_CH53_01_int_engine",1,1],
            "frequency": "rotorSpeed*(1+rotorThrust/6)*0.8",
            "volume": "(1-camPos)*((rotorSpeed-0.75)*4)"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|Sounds|RotorInt [Indent level: 2],
        "rotorint": {
            "sound": ["A3|Sounds_F|dummysound",0.501187,1],
            "frequency": "rotorSpeed * (1-rotorThrust/5) * 1.2",
            "volume": "(1-camPos)*(0 max (rotorSpeed-0.1))*(1 + rotorThrust)*0.9"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|Sounds|TransmissionDamageExt_phase1 [Indent level: 2],
        "transmissiondamageext_phase1": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|Heli_damage_transmission_ext_1",1,1,150],
            "frequency": "0.66 + rotorSpeed / 3",
            "volume": "camPos * (transmissionDamage factor [0.3, 0.35]) * (transmissionDamage factor [0.5, 0.45]) * (rotorSpeed factor [0.2, 0.5])"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|Sounds|TransmissionDamageExt_phase2 [Indent level: 2],
        "transmissiondamageext_phase2": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|Heli_damage_transmission_ext_2",1,1,150],
            "frequency": "0.66 + rotorSpeed / 3",
            "volume": "camPos * (transmissionDamage factor [0.45, 0.5]) * (rotorSpeed factor [0.2, 0.5])"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|Sounds|TransmissionDamageInt_phase1 [Indent level: 2],
        "transmissiondamageint_phase1": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|Heli_damage_transmission_int_1",1,1,150],
            "frequency": "0.66 + rotorSpeed / 3",
            "volume": "(1 - camPos) * (transmissionDamage factor [0.3, 0.35]) * (transmissionDamage factor [0.5, 0.45]) * (rotorSpeed factor [0.2, 0.5])"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|Sounds|TransmissionDamageInt_phase2 [Indent level: 2],
        "transmissiondamageint_phase2": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|Heli_damage_transmission_int_2",1,1,150],
            "frequency": "0.66 + rotorSpeed / 3",
            "volume": "(1 - camPos) * (transmissionDamage factor [0.45, 0.5]) * (rotorSpeed factor [0.2, 0.5])"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|Sounds|damageAlarmInt [Indent level: 2],
        "damagealarmint": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|Heli_alarm_bluefor",0.316228,1],
            "frequency": 1,
            "volume": "engineOn * (1 - camPos) * ( 1 - ((transmissionDamage factor [0.61, 0.60]) * (motorDamage factor [0.61, 0.60]) * (rotorDamage factor [0.51, 0.50]))) * (rotorSpeed factor [0.0, 0.001])"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|Sounds|damageAlarmExt [Indent level: 2],
        "damagealarmext": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|Heli_alarm_bluefor",0.223872,1,20],
            "frequency": 1,
            "volume": "engineOn * camPos * ( 1 - ((transmissionDamage factor [0.61, 0.60]) * (motorDamage factor [0.61, 0.60]) * (rotorDamage factor [0.51, 0.50]))) * (rotorSpeed factor [0, 0.001])"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|Sounds|rotorLowAlarmInt [Indent level: 2],
        "rotorlowalarmint": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|Heli_alarm_rotor_low",0.316228,1],
            "frequency": 1,
            "volume": "engineOn * (1 - camPos) * (rotorSpeed factor [0.9, 0.8999]) * (rotorSpeed factor [-0.5, 1]) * (speed factor [3, 3.01])"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|Sounds|rotorLowAlarmExt [Indent level: 2],
        "rotorlowalarmext": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|Heli_alarm_rotor_low",0.223872,1,20],
            "frequency": 1,
            "volume": "engineOn * camPos * (rotorSpeed factor [0.9, 0.8999]) * (rotorSpeed factor [-0.5, 1]) * (speed factor [3, 3.01])"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|Sounds|scrubLandInt [Indent level: 2],
        "scrublandint": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|wheelsInt",1,1,100],
            "frequency": 1,
            "volume": "2 * (1-camPos) * (scrubLand factor[0.02, 0.05]) * (1 - (lateralMovement factor [0.7,1]))"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|Sounds|scrubLandExt [Indent level: 2],
        "scrublandext": {
            "sound": ["A3|Sounds_F|dummysound",1,1,100],
            "frequency": 1,
            "volume": "camPos * (scrubLand factor[0.02, 0.05]) * (1 - (lateralMovement factor [0.7,1]))"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|Sounds|scrubBuildingInt [Indent level: 2],
        "scrubbuildingint": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|wheelsInt",1,1,100],
            "frequency": 1,
            "volume": "(1-camPos) * (scrubBuilding factor[0.02, 0.05]) * (1 - (lateralMovement factor [0.7,1]))"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|Sounds|scrubBuildingExt [Indent level: 2],
        "scrubbuildingext": {
            "sound": ["A3|Sounds_F|dummysound",1,1,100],
            "frequency": 1,
            "volume": "camPos * (scrubBuilding factor[0.02, 0.05])"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|Sounds|scrubTreeInt [Indent level: 2],
        "scrubtreeint": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|scrubTreeInt",1,1,100],
            "frequency": 1,
            "volume": "(1 - camPos) * ((scrubTree) factor [0, 0.01])"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|Sounds|scrubTreeExt [Indent level: 2],
        "scrubtreeext": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|scrubTreeExt",1,1,100],
            "frequency": 1,
            "volume": "camPos * ((scrubTree) factor [0, 0.01])"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|Sounds|RainExt [Indent level: 2],
        "rainext": {
            "sound": ["A3|Sounds_F|vehicles|noises|rain1_ext",1,1,100],
            "frequency": 1,
            "volume": "camPos * (rain - rotorSpeed/2) * 2"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|Sounds|RainInt [Indent level: 2],
        "rainint": {
            "sound": ["A3|Sounds_F|vehicles|noises|rain1_int",1,1,100],
            "frequency": 1,
            "volume": "(1-camPos)*(rain - rotorSpeed/2)*2"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|Sounds|SlingLoadDownExt [Indent level: 2],
        "slingloaddownext": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineDownEXT",1,1,500],
            "frequency": 1,
            "volume": "camPos*(slingLoadActive factor [0,-1])"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|Sounds|SlingLoadUpExt [Indent level: 2],
        "slingloadupext": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineUpEXT",1,1,500],
            "frequency": 1,
            "volume": "camPos*(slingLoadActive factor [0,1])"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|Sounds|SlingLoadDownInt [Indent level: 2],
        "slingloaddownint": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineDownINT",1,1,500],
            "frequency": 1,
            "volume": "(1-camPos)*(slingLoadActive factor [0,-1])"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|Sounds|SlingLoadUpInt [Indent level: 2],
        "slingloadupint": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineUpINT",1,1,500],
            "frequency": 1,
            "volume": "(1-camPos)*(slingLoadActive factor [0,1])"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|Sounds|WindInt [Indent level: 2],
        "windint": {
            "sound": ["A3|Sounds_F|dummysound",0.707946,1,50],
            "frequency": 1,
            "volume": "(1-camPos)*(speed factor[5, 60])*(speed factor[5, 60])"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|Sounds|GStress [Indent level: 2],
        "gstress": {
            "sound": ["A3|Sounds_F|vehicles|noises|vehicle_stress2d",1.12202,1,50],
            "frequency": 1,
            "volume": "engineOn * (1-camPos) * ((gmeterZ factor[1.5, 2.5]) + (gmeterZ factor[0.5, -0.5]))"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|Sounds|SpeedStress [Indent level: 2],
        "speedstress": {
            "sound": ["A3|Sounds_F|vehicles|noises|vehicle_stress3",1,1,50],
            "frequency": 1,
            "volume": "(1-camPos)*(speed factor[40,80])"
        }
    },
    # Class: CfgVehicles|rhsusf_CH53E_USMC|SoundsExt [Indent level: 1],
    "soundsext": {
        # Class: CfgVehicles|rhsusf_CH53E_USMC|SoundsExt|SoundEvents [Indent level: 2]
        "soundevents": {
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|SoundsExt|Sounds [Indent level: 2],
        "sounds": {
            # Class: CfgVehicles|rhsusf_CH53E_USMC|SoundsExt|Sounds|EngineExt [Indent level: 3]
            "engineext": {
                "sound": ["A3|Sounds_F|dummysound",1.41254,1,800],
                "frequency": "rotorSpeed*(1+rotorThrust/6)*0.8",
                "volume": "camPos*((rotorSpeed-0.72)*4)"
            },
            # Class: CfgVehicles|rhsusf_CH53E_USMC|SoundsExt|Sounds|RotorExt [Indent level: 3],
            "rotorext": {
                "sound": ["rhsusf|addons|rhsusf_ch53|sounds|Heli_CH53_01_ext_rotor",1,1,3500],
                "frequency": "rotorSpeed / (1-rotorThrust/5)*0.8",
                "volume": "camPos*((rotorSpeed-0.72)*6)",
                "cone": [1.6,3.14,1.6,0.95]
            },
            # Class: CfgVehicles|rhsusf_CH53E_USMC|SoundsExt|Sounds|RotorNoiseExt [Indent level: 3],
            "rotornoiseext": {
                "sound": ["A3|Sounds_F|dummysound",1,1,400],
                "frequency": 1,
                "volume": "camPos * (rotorThrust factor [0.7, 0.9])",
                "cone": [0.7,1.3,1,0]
            },
            # Class: CfgVehicles|rhsusf_CH53E_USMC|SoundsExt|Sounds|EngineInt [Indent level: 3],
            "engineint": {
                "sound": ["rhsusf|addons|rhsusf_ch53|sounds|Heli_CH53_01_int_engine",1,1],
                "frequency": "rotorSpeed*(1+rotorThrust/6)*0.8",
                "volume": "(1-camPos)*((rotorSpeed-0.75)*4)"
            },
            # Class: CfgVehicles|rhsusf_CH53E_USMC|SoundsExt|Sounds|RotorInt [Indent level: 3],
            "rotorint": {
                "sound": ["A3|Sounds_F|dummysound",0.501187,1],
                "frequency": "rotorSpeed * (1-rotorThrust/5) * 1.2",
                "volume": "(1-camPos)*(0 max (rotorSpeed-0.1))*(1 + rotorThrust)*0.9"
            },
            # Class: CfgVehicles|rhsusf_CH53E_USMC|SoundsExt|Sounds|TransmissionDamageExt_phase1 [Indent level: 3],
            "transmissiondamageext_phase1": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|Heli_damage_transmission_ext_1",1,1,150],
                "frequency": "0.66 + rotorSpeed / 3",
                "volume": "camPos * (transmissionDamage factor [0.3, 0.35]) * (transmissionDamage factor [0.5, 0.45]) * (rotorSpeed factor [0.2, 0.5])"
            },
            # Class: CfgVehicles|rhsusf_CH53E_USMC|SoundsExt|Sounds|TransmissionDamageExt_phase2 [Indent level: 3],
            "transmissiondamageext_phase2": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|Heli_damage_transmission_ext_2",1,1,150],
                "frequency": "0.66 + rotorSpeed / 3",
                "volume": "camPos * (transmissionDamage factor [0.45, 0.5]) * (rotorSpeed factor [0.2, 0.5])"
            },
            # Class: CfgVehicles|rhsusf_CH53E_USMC|SoundsExt|Sounds|TransmissionDamageInt_phase1 [Indent level: 3],
            "transmissiondamageint_phase1": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|Heli_damage_transmission_int_1",1,1,150],
                "frequency": "0.66 + rotorSpeed / 3",
                "volume": "(1 - camPos) * (transmissionDamage factor [0.3, 0.35]) * (transmissionDamage factor [0.5, 0.45]) * (rotorSpeed factor [0.2, 0.5])"
            },
            # Class: CfgVehicles|rhsusf_CH53E_USMC|SoundsExt|Sounds|TransmissionDamageInt_phase2 [Indent level: 3],
            "transmissiondamageint_phase2": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|Heli_damage_transmission_int_2",1,1,150],
                "frequency": "0.66 + rotorSpeed / 3",
                "volume": "(1 - camPos) * (transmissionDamage factor [0.45, 0.5]) * (rotorSpeed factor [0.2, 0.5])"
            },
            # Class: CfgVehicles|rhsusf_CH53E_USMC|SoundsExt|Sounds|damageAlarmInt [Indent level: 3],
            "damagealarmint": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|Heli_alarm_bluefor",0.316228,1],
                "frequency": 1,
                "volume": "engineOn * (1 - camPos) * ( 1 - ((transmissionDamage factor [0.61, 0.60]) * (motorDamage factor [0.61, 0.60]) * (rotorDamage factor [0.51, 0.50]))) * (rotorSpeed factor [0.0, 0.001])"
            },
            # Class: CfgVehicles|rhsusf_CH53E_USMC|SoundsExt|Sounds|damageAlarmExt [Indent level: 3],
            "damagealarmext": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|Heli_alarm_bluefor",0.223872,1,20],
                "frequency": 1,
                "volume": "engineOn * camPos * ( 1 - ((transmissionDamage factor [0.61, 0.60]) * (motorDamage factor [0.61, 0.60]) * (rotorDamage factor [0.51, 0.50]))) * (rotorSpeed factor [0, 0.001])"
            },
            # Class: CfgVehicles|rhsusf_CH53E_USMC|SoundsExt|Sounds|rotorLowAlarmInt [Indent level: 3],
            "rotorlowalarmint": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|Heli_alarm_rotor_low",0.316228,1],
                "frequency": 1,
                "volume": "engineOn * (1 - camPos) * (rotorSpeed factor [0.9, 0.8999]) * (rotorSpeed factor [-0.5, 1]) * (speed factor [3, 3.01])"
            },
            # Class: CfgVehicles|rhsusf_CH53E_USMC|SoundsExt|Sounds|rotorLowAlarmExt [Indent level: 3],
            "rotorlowalarmext": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|Heli_alarm_rotor_low",0.223872,1,20],
                "frequency": 1,
                "volume": "engineOn * camPos * (rotorSpeed factor [0.9, 0.8999]) * (rotorSpeed factor [-0.5, 1]) * (speed factor [3, 3.01])"
            },
            # Class: CfgVehicles|rhsusf_CH53E_USMC|SoundsExt|Sounds|scrubLandInt [Indent level: 3],
            "scrublandint": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|wheelsInt",1,1,100],
                "frequency": 1,
                "volume": "2 * (1-camPos) * (scrubLand factor[0.02, 0.05]) * (1 - (lateralMovement factor [0.7,1]))"
            },
            # Class: CfgVehicles|rhsusf_CH53E_USMC|SoundsExt|Sounds|scrubLandExt [Indent level: 3],
            "scrublandext": {
                "sound": ["A3|Sounds_F|dummysound",1,1,100],
                "frequency": 1,
                "volume": "camPos * (scrubLand factor[0.02, 0.05]) * (1 - (lateralMovement factor [0.7,1]))"
            },
            # Class: CfgVehicles|rhsusf_CH53E_USMC|SoundsExt|Sounds|scrubBuildingInt [Indent level: 3],
            "scrubbuildingint": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|wheelsInt",1,1,100],
                "frequency": 1,
                "volume": "(1-camPos) * (scrubBuilding factor[0.02, 0.05]) * (1 - (lateralMovement factor [0.7,1]))"
            },
            # Class: CfgVehicles|rhsusf_CH53E_USMC|SoundsExt|Sounds|scrubBuildingExt [Indent level: 3],
            "scrubbuildingext": {
                "sound": ["A3|Sounds_F|dummysound",1,1,100],
                "frequency": 1,
                "volume": "camPos * (scrubBuilding factor[0.02, 0.05])"
            },
            # Class: CfgVehicles|rhsusf_CH53E_USMC|SoundsExt|Sounds|scrubTreeInt [Indent level: 3],
            "scrubtreeint": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|scrubTreeInt",1,1,100],
                "frequency": 1,
                "volume": "(1 - camPos) * ((scrubTree) factor [0, 0.01])"
            },
            # Class: CfgVehicles|rhsusf_CH53E_USMC|SoundsExt|Sounds|scrubTreeExt [Indent level: 3],
            "scrubtreeext": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|scrubTreeExt",1,1,100],
                "frequency": 1,
                "volume": "camPos * ((scrubTree) factor [0, 0.01])"
            },
            # Class: CfgVehicles|rhsusf_CH53E_USMC|SoundsExt|Sounds|RainExt [Indent level: 3],
            "rainext": {
                "sound": ["A3|Sounds_F|vehicles|noises|rain1_ext",1,1,100],
                "frequency": 1,
                "volume": "camPos * (rain - rotorSpeed/2) * 2"
            },
            # Class: CfgVehicles|rhsusf_CH53E_USMC|SoundsExt|Sounds|RainInt [Indent level: 3],
            "rainint": {
                "sound": ["A3|Sounds_F|vehicles|noises|rain1_int",1,1,100],
                "frequency": 1,
                "volume": "(1-camPos)*(rain - rotorSpeed/2)*2"
            },
            # Class: CfgVehicles|rhsusf_CH53E_USMC|SoundsExt|Sounds|SlingLoadDownExt [Indent level: 3],
            "slingloaddownext": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineDownEXT",1,1,500],
                "frequency": 1,
                "volume": "camPos*(slingLoadActive factor [0,-1])"
            },
            # Class: CfgVehicles|rhsusf_CH53E_USMC|SoundsExt|Sounds|SlingLoadUpExt [Indent level: 3],
            "slingloadupext": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineUpEXT",1,1,500],
                "frequency": 1,
                "volume": "camPos*(slingLoadActive factor [0,1])"
            },
            # Class: CfgVehicles|rhsusf_CH53E_USMC|SoundsExt|Sounds|SlingLoadDownInt [Indent level: 3],
            "slingloaddownint": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineDownINT",1,1,500],
                "frequency": 1,
                "volume": "(1-camPos)*(slingLoadActive factor [0,-1])"
            },
            # Class: CfgVehicles|rhsusf_CH53E_USMC|SoundsExt|Sounds|SlingLoadUpInt [Indent level: 3],
            "slingloadupint": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineUpINT",1,1,500],
                "frequency": 1,
                "volume": "(1-camPos)*(slingLoadActive factor [0,1])"
            },
            # Class: CfgVehicles|rhsusf_CH53E_USMC|SoundsExt|Sounds|WindInt [Indent level: 3],
            "windint": {
                "sound": ["A3|Sounds_F|dummysound",0.707946,1,50],
                "frequency": 1,
                "volume": "(1-camPos)*(speed factor[5, 60])*(speed factor[5, 60])"
            },
            # Class: CfgVehicles|rhsusf_CH53E_USMC|SoundsExt|Sounds|GStress [Indent level: 3],
            "gstress": {
                "sound": ["A3|Sounds_F|vehicles|noises|vehicle_stress2d",1.12202,1,50],
                "frequency": 1,
                "volume": "engineOn * (1-camPos) * ((gmeterZ factor[1.5, 2.5]) + (gmeterZ factor[0.5, -0.5]))"
            },
            # Class: CfgVehicles|rhsusf_CH53E_USMC|SoundsExt|Sounds|SpeedStress [Indent level: 3],
            "speedstress": {
                "sound": ["A3|Sounds_F|vehicles|noises|vehicle_stress3",1,1,50],
                "frequency": 1,
                "volume": "(1-camPos)*(speed factor[40,80])"
            }
        }
    },
    "armor": 40,
    "armorstructural": 20,
    "hulldamagecauseexplosion": 1,
    "hullexplosiondelay": [10,20],
    "damageresistance": 0.001,
    # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints [Indent level: 1],
    "hitpoints": {
        # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitHull [Indent level: 2]
        "hithull": {
            "simulation": "RHS_Hull_Helicopter",
            "armor": -100,
            "minimalhit": -0.2,
            "explosionshielding": 2,
            "radius": 0.4,
            "armorcomponent": "Hit_Hull",
            "name": "NEtrup",
            "visual": "zbytek",
            "passthrough": 1,
            # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitHull|DestructionEffects [Indent level: 3],
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
        # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitEngine1 [Indent level: 2],
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
        # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitEngine2 [Indent level: 2],
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
        # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitEngine [Indent level: 2],
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
        # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitFuel [Indent level: 2],
        "hitfuel": {
            "armor": -70,
            "explosionshielding": 0.5,
            "passthrough": 0.1,
            "minimalhit": -0.1,
            "radius": 0.4,
            "armorcomponent": "hit_fuel_1",
            "name": "hit_fuel_1",
            "visual": "palivo"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitFuel2 [Indent level: 2],
        "hitfuel2": {
            "armor": -70,
            "explosionshielding": 0.5,
            "passthrough": 0.1,
            "minimalhit": -0.1,
            "radius": 0.4,
            "armorcomponent": "hit_fuel_2",
            "name": "hit_fuel_2",
            "visual": "palivo"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitAvionics [Indent level: 2],
        "hitavionics": {
            "armor": 0.15,
            "minimalhit": -0.1,
            "name": "elektronika",
            "visual": "elektronika",
            "passthrough": 1,
            "convexcomponent": "avionics_hit",
            "explosionshielding": 1,
            "material": 51
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitTail [Indent level: 2],
        "hittail": {
            "armor": -80,
            "explosionshielding": 3,
            "passthrough": 0.5,
            "minimalhit": -0.2,
            "radius": 0.3,
            "armorcomponent": "Hit_Tail",
            "name": "tail_rotor_hit",
            "visual": "Vis_Tail",
            "simulation": "RHS_Hull_Helicopter"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitVRotor [Indent level: 2],
        "hitvrotor": {
            "armor": -80,
            "minimalhit": -0.1,
            "name": "mala vrtule",
            "visual": "mala vrtule staticka",
            "passthrough": 0,
            "armorcomponent": "Hit_Rotor_Rear",
            "depends": "HitTail",
            "convexcomponent": "tail_rotor_hit",
            "explosionshielding": 1,
            "material": 51
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitHRotor [Indent level: 2],
        "hithrotor": {
            "armor": -80,
            "minimalhit": -0.1,
            "name": "velka vrtule",
            "visual": "velka vrtule staticka",
            "passthrough": 0,
            "armorcomponent": "Hit_Rotor_Main",
            "convexcomponent": "main_rotor_hit",
            "explosionshielding": 1,
            "material": 51
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass1 [Indent level: 2],
        "hitglass1": {
            "name": "glass1",
            "visual": "glass1",
            "radius": 0.37,
            "armor": -5,
            "explosionshielding": 2,
            "minimalhit": -0.025,
            "passthrough": 0,
            "armorcomponent": "glass1",
            # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass1|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass1|DestructionEffects|BrokenGlass1 [Indent level: 4],
                "brokenglass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass1|DestructionEffects|BrokenGlass2 [Indent level: 4],
                "brokenglass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass1|DestructionEffects|BrokenGlass3 [Indent level: 4],
                "brokenglass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass1|DestructionEffects|BrokenGlass4 [Indent level: 4],
                "brokenglass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass1|DestructionEffects|BrokenGlass5 [Indent level: 4],
                "brokenglass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass1|DestructionEffects|BrokenGlass1S [Indent level: 4],
                "brokenglass1s": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass1|DestructionEffects|BrokenGlass2S [Indent level: 4],
                "brokenglass2s": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass1|DestructionEffects|BrokenGlass3S [Indent level: 4],
                "brokenglass3s": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass1|DestructionEffects|BrokenGlass4S [Indent level: 4],
                "brokenglass4s": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass1|DestructionEffects|BrokenGlass5S [Indent level: 4],
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
        # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass2 [Indent level: 2],
        "hitglass2": {
            "name": "glass2",
            "visual": "glass2",
            "radius": 0.37,
            "armor": -5,
            "explosionshielding": 1.5,
            "minimalhit": -0.025,
            "passthrough": 0,
            "armorcomponent": "glass2",
            # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass2|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass2|DestructionEffects|BrokenGlass1 [Indent level: 4],
                "brokenglass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects2",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass2|DestructionEffects|BrokenGlass2 [Indent level: 4],
                "brokenglass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects2",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass2|DestructionEffects|BrokenGlass3 [Indent level: 4],
                "brokenglass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects2",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass2|DestructionEffects|BrokenGlass4 [Indent level: 4],
                "brokenglass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects2",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass2|DestructionEffects|BrokenGlass5 [Indent level: 4],
                "brokenglass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects2",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass2|DestructionEffects|BrokenGlass1S [Indent level: 4],
                "brokenglass1s": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects2",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass2|DestructionEffects|BrokenGlass2S [Indent level: 4],
                "brokenglass2s": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects2",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass2|DestructionEffects|BrokenGlass3S [Indent level: 4],
                "brokenglass3s": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects2",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass2|DestructionEffects|BrokenGlass4S [Indent level: 4],
                "brokenglass4s": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects2",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass2|DestructionEffects|BrokenGlass5S [Indent level: 4],
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
        # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass3 [Indent level: 2],
        "hitglass3": {
            "name": "glass3",
            "visual": "glass3",
            "radius": 0.25,
            "armor": -5,
            "explosionshielding": 1.5,
            "minimalhit": -0.025,
            "passthrough": 0,
            "armorcomponent": "glass3",
            # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass3|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass3|DestructionEffects|BrokenGlass1 [Indent level: 4],
                "brokenglass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects3",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass3|DestructionEffects|BrokenGlass2 [Indent level: 4],
                "brokenglass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects3",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass3|DestructionEffects|BrokenGlass3 [Indent level: 4],
                "brokenglass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects3",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass3|DestructionEffects|BrokenGlass4 [Indent level: 4],
                "brokenglass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects3",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass3|DestructionEffects|BrokenGlass5 [Indent level: 4],
                "brokenglass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects3",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass3|DestructionEffects|BrokenGlass1S [Indent level: 4],
                "brokenglass1s": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects3",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass3|DestructionEffects|BrokenGlass2S [Indent level: 4],
                "brokenglass2s": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects3",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass3|DestructionEffects|BrokenGlass3S [Indent level: 4],
                "brokenglass3s": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects3",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass3|DestructionEffects|BrokenGlass4S [Indent level: 4],
                "brokenglass4s": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects3",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass3|DestructionEffects|BrokenGlass5S [Indent level: 4],
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
        # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass4 [Indent level: 2],
        "hitglass4": {
            "name": "glass4",
            "visual": "glass4",
            "radius": 0.25,
            "armor": -5,
            "explosionshielding": 1.5,
            "minimalhit": -0.025,
            "passthrough": 0,
            "armorcomponent": "glass4",
            # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass4|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass4|DestructionEffects|BrokenGlass1 [Indent level: 4],
                "brokenglass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects4",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass4|DestructionEffects|BrokenGlass2 [Indent level: 4],
                "brokenglass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects4",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass4|DestructionEffects|BrokenGlass3 [Indent level: 4],
                "brokenglass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects4",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass4|DestructionEffects|BrokenGlass4 [Indent level: 4],
                "brokenglass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects4",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass4|DestructionEffects|BrokenGlass5 [Indent level: 4],
                "brokenglass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects4",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass4|DestructionEffects|BrokenGlass1S [Indent level: 4],
                "brokenglass1s": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects4",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass4|DestructionEffects|BrokenGlass2S [Indent level: 4],
                "brokenglass2s": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects4",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass4|DestructionEffects|BrokenGlass3S [Indent level: 4],
                "brokenglass3s": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects4",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass4|DestructionEffects|BrokenGlass4S [Indent level: 4],
                "brokenglass4s": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects4",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass4|DestructionEffects|BrokenGlass5S [Indent level: 4],
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
        # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass5 [Indent level: 2],
        "hitglass5": {
            "name": "glass5",
            "visual": "glass5",
            "radius": 0.34,
            "armor": -5,
            "explosionshielding": 2,
            "minimalhit": -0.025,
            "passthrough": 0,
            "armorcomponent": "glass5",
            # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass5|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass5|DestructionEffects|BrokenGlass1 [Indent level: 4],
                "brokenglass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects5",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass5|DestructionEffects|BrokenGlass2 [Indent level: 4],
                "brokenglass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects5",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass5|DestructionEffects|BrokenGlass3 [Indent level: 4],
                "brokenglass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects5",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass5|DestructionEffects|BrokenGlass4 [Indent level: 4],
                "brokenglass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects5",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass5|DestructionEffects|BrokenGlass5 [Indent level: 4],
                "brokenglass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects5",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass5|DestructionEffects|BrokenGlass1S [Indent level: 4],
                "brokenglass1s": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects5",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass5|DestructionEffects|BrokenGlass2S [Indent level: 4],
                "brokenglass2s": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects5",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass5|DestructionEffects|BrokenGlass3S [Indent level: 4],
                "brokenglass3s": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects5",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass5|DestructionEffects|BrokenGlass4S [Indent level: 4],
                "brokenglass4s": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects5",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass5|DestructionEffects|BrokenGlass5S [Indent level: 4],
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
        # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass6 [Indent level: 2],
        "hitglass6": {
            "name": "glass6",
            "visual": "glass6",
            "radius": 0.34,
            "armor": -5,
            "explosionshielding": 1.5,
            "minimalhit": -0.025,
            "passthrough": 0,
            "armorcomponent": "glass6",
            # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass6|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass6|DestructionEffects|BrokenGlass1 [Indent level: 4],
                "brokenglass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects6",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass6|DestructionEffects|BrokenGlass2 [Indent level: 4],
                "brokenglass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects6",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass6|DestructionEffects|BrokenGlass3 [Indent level: 4],
                "brokenglass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects6",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass6|DestructionEffects|BrokenGlass4 [Indent level: 4],
                "brokenglass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects6",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass6|DestructionEffects|BrokenGlass5 [Indent level: 4],
                "brokenglass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects6",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass6|DestructionEffects|BrokenGlass1S [Indent level: 4],
                "brokenglass1s": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects6",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass6|DestructionEffects|BrokenGlass2S [Indent level: 4],
                "brokenglass2s": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects6",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass6|DestructionEffects|BrokenGlass3S [Indent level: 4],
                "brokenglass3s": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects6",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass6|DestructionEffects|BrokenGlass4S [Indent level: 4],
                "brokenglass4s": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects6",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass6|DestructionEffects|BrokenGlass5S [Indent level: 4],
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
        # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass7 [Indent level: 2],
        "hitglass7": {
            "name": "glass7",
            "visual": "glass7",
            "radius": 0.34,
            "armor": -5,
            "explosionshielding": 1.5,
            "minimalhit": -0.025,
            "passthrough": 0,
            "armorcomponent": "glass7",
            # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass7|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass7|DestructionEffects|BrokenGlass1 [Indent level: 4],
                "brokenglass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects7",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass7|DestructionEffects|BrokenGlass2 [Indent level: 4],
                "brokenglass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects7",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass7|DestructionEffects|BrokenGlass3 [Indent level: 4],
                "brokenglass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects7",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass7|DestructionEffects|BrokenGlass4 [Indent level: 4],
                "brokenglass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects7",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass7|DestructionEffects|BrokenGlass5 [Indent level: 4],
                "brokenglass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects7",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass7|DestructionEffects|BrokenGlass1S [Indent level: 4],
                "brokenglass1s": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects7",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass7|DestructionEffects|BrokenGlass2S [Indent level: 4],
                "brokenglass2s": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects7",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass7|DestructionEffects|BrokenGlass3S [Indent level: 4],
                "brokenglass3s": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects7",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass7|DestructionEffects|BrokenGlass4S [Indent level: 4],
                "brokenglass4s": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects7",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass7|DestructionEffects|BrokenGlass5S [Indent level: 4],
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
        # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass8 [Indent level: 2],
        "hitglass8": {
            "name": "glass8",
            "visual": "glass8",
            "radius": 0.34,
            "armor": -5,
            "explosionshielding": 1.5,
            "minimalhit": -0.025,
            "passthrough": 0,
            "armorcomponent": "glass8",
            # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass8|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass8|DestructionEffects|BrokenGlass1 [Indent level: 4],
                "brokenglass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects8",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass8|DestructionEffects|BrokenGlass2 [Indent level: 4],
                "brokenglass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects8",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass8|DestructionEffects|BrokenGlass3 [Indent level: 4],
                "brokenglass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects8",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass8|DestructionEffects|BrokenGlass4 [Indent level: 4],
                "brokenglass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects8",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass8|DestructionEffects|BrokenGlass5 [Indent level: 4],
                "brokenglass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects8",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass8|DestructionEffects|BrokenGlass1S [Indent level: 4],
                "brokenglass1s": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects8",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass8|DestructionEffects|BrokenGlass2S [Indent level: 4],
                "brokenglass2s": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects8",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass8|DestructionEffects|BrokenGlass3S [Indent level: 4],
                "brokenglass3s": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects8",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass8|DestructionEffects|BrokenGlass4S [Indent level: 4],
                "brokenglass4s": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects8",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass8|DestructionEffects|BrokenGlass5S [Indent level: 4],
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
        # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass9 [Indent level: 2],
        "hitglass9": {
            "name": "glass9",
            "visual": "glass9",
            "radius": 0.24,
            "armor": -5,
            "explosionshielding": 1,
            "minimalhit": -0.025,
            "passthrough": 0,
            "armorcomponent": "glass9",
            # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass9|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass9|DestructionEffects|BrokenGlass1 [Indent level: 4],
                "brokenglass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects9",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass9|DestructionEffects|BrokenGlass2 [Indent level: 4],
                "brokenglass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects9",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass9|DestructionEffects|BrokenGlass3 [Indent level: 4],
                "brokenglass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects9",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass9|DestructionEffects|BrokenGlass4 [Indent level: 4],
                "brokenglass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects9",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass9|DestructionEffects|BrokenGlass5 [Indent level: 4],
                "brokenglass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects9",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass9|DestructionEffects|BrokenGlass1S [Indent level: 4],
                "brokenglass1s": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects9",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass9|DestructionEffects|BrokenGlass2S [Indent level: 4],
                "brokenglass2s": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects9",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass9|DestructionEffects|BrokenGlass3S [Indent level: 4],
                "brokenglass3s": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects9",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass9|DestructionEffects|BrokenGlass4S [Indent level: 4],
                "brokenglass4s": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects9",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass9|DestructionEffects|BrokenGlass5S [Indent level: 4],
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
        # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass10 [Indent level: 2],
        "hitglass10": {
            "name": "glass10",
            "visual": "glass10",
            "radius": 0.24,
            "armor": -5,
            "explosionshielding": 1,
            "minimalhit": -0.025,
            "passthrough": 0,
            "armorcomponent": "glass10",
            # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass10|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass10|DestructionEffects|BrokenGlass1 [Indent level: 4],
                "brokenglass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects10",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass10|DestructionEffects|BrokenGlass2 [Indent level: 4],
                "brokenglass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects10",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass10|DestructionEffects|BrokenGlass3 [Indent level: 4],
                "brokenglass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects10",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass10|DestructionEffects|BrokenGlass4 [Indent level: 4],
                "brokenglass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects10",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass10|DestructionEffects|BrokenGlass5 [Indent level: 4],
                "brokenglass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects10",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass10|DestructionEffects|BrokenGlass1S [Indent level: 4],
                "brokenglass1s": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects10",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass10|DestructionEffects|BrokenGlass2S [Indent level: 4],
                "brokenglass2s": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects10",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass10|DestructionEffects|BrokenGlass3S [Indent level: 4],
                "brokenglass3s": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects10",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass10|DestructionEffects|BrokenGlass4S [Indent level: 4],
                "brokenglass4s": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects10",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass10|DestructionEffects|BrokenGlass5S [Indent level: 4],
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
        # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass11 [Indent level: 2],
        "hitglass11": {
            "name": "glass11",
            "visual": "glass11",
            "radius": 0.24,
            "armor": -5,
            "explosionshielding": 1,
            "minimalhit": -0.025,
            "passthrough": 0,
            "armorcomponent": "glass11",
            # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass11|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass11|DestructionEffects|BrokenGlass1 [Indent level: 4],
                "brokenglass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects11",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass11|DestructionEffects|BrokenGlass2 [Indent level: 4],
                "brokenglass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects11",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass11|DestructionEffects|BrokenGlass3 [Indent level: 4],
                "brokenglass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects11",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass11|DestructionEffects|BrokenGlass4 [Indent level: 4],
                "brokenglass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects11",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass11|DestructionEffects|BrokenGlass5 [Indent level: 4],
                "brokenglass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects11",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass11|DestructionEffects|BrokenGlass1S [Indent level: 4],
                "brokenglass1s": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects11",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass11|DestructionEffects|BrokenGlass2S [Indent level: 4],
                "brokenglass2s": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects11",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass11|DestructionEffects|BrokenGlass3S [Indent level: 4],
                "brokenglass3s": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects11",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass11|DestructionEffects|BrokenGlass4S [Indent level: 4],
                "brokenglass4s": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects11",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass11|DestructionEffects|BrokenGlass5S [Indent level: 4],
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
        # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass12 [Indent level: 2],
        "hitglass12": {
            "name": "glass12",
            "visual": "glass12",
            "radius": 0.24,
            "armor": -5,
            "explosionshielding": 1,
            "minimalhit": -0.025,
            "passthrough": 0,
            "armorcomponent": "glass12",
            # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass12|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass12|DestructionEffects|BrokenGlass1 [Indent level: 4],
                "brokenglass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects12",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass12|DestructionEffects|BrokenGlass2 [Indent level: 4],
                "brokenglass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects12",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass12|DestructionEffects|BrokenGlass3 [Indent level: 4],
                "brokenglass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects12",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass12|DestructionEffects|BrokenGlass4 [Indent level: 4],
                "brokenglass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects12",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass12|DestructionEffects|BrokenGlass5 [Indent level: 4],
                "brokenglass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects12",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass12|DestructionEffects|BrokenGlass1S [Indent level: 4],
                "brokenglass1s": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects12",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass12|DestructionEffects|BrokenGlass2S [Indent level: 4],
                "brokenglass2s": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects12",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass12|DestructionEffects|BrokenGlass3S [Indent level: 4],
                "brokenglass3s": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects12",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass12|DestructionEffects|BrokenGlass4S [Indent level: 4],
                "brokenglass4s": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects12",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass12|DestructionEffects|BrokenGlass5S [Indent level: 4],
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
        # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass13 [Indent level: 2],
        "hitglass13": {
            "name": "glass13",
            "visual": "glass13",
            "radius": 0.24,
            "armor": -5,
            "explosionshielding": 1,
            "minimalhit": -0.025,
            "passthrough": 0,
            "armorcomponent": "glass13",
            # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass13|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass13|DestructionEffects|BrokenGlass1 [Indent level: 4],
                "brokenglass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects13",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass13|DestructionEffects|BrokenGlass2 [Indent level: 4],
                "brokenglass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects13",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass13|DestructionEffects|BrokenGlass3 [Indent level: 4],
                "brokenglass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects13",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass13|DestructionEffects|BrokenGlass4 [Indent level: 4],
                "brokenglass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects13",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass13|DestructionEffects|BrokenGlass5 [Indent level: 4],
                "brokenglass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects13",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass13|DestructionEffects|BrokenGlass1S [Indent level: 4],
                "brokenglass1s": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects13",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass13|DestructionEffects|BrokenGlass2S [Indent level: 4],
                "brokenglass2s": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects13",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass13|DestructionEffects|BrokenGlass3S [Indent level: 4],
                "brokenglass3s": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects13",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass13|DestructionEffects|BrokenGlass4S [Indent level: 4],
                "brokenglass4s": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects13",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass13|DestructionEffects|BrokenGlass5S [Indent level: 4],
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
        # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass14 [Indent level: 2],
        "hitglass14": {
            "name": "glass14",
            "visual": "glass14",
            "radius": 0.24,
            "armor": -5,
            "explosionshielding": 1,
            "minimalhit": -0.025,
            "passthrough": 0,
            "armorcomponent": "glass14",
            # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass14|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass14|DestructionEffects|BrokenGlass1 [Indent level: 4],
                "brokenglass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects14",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass14|DestructionEffects|BrokenGlass2 [Indent level: 4],
                "brokenglass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects14",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass14|DestructionEffects|BrokenGlass3 [Indent level: 4],
                "brokenglass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects14",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass14|DestructionEffects|BrokenGlass4 [Indent level: 4],
                "brokenglass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects14",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass14|DestructionEffects|BrokenGlass5 [Indent level: 4],
                "brokenglass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects14",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass14|DestructionEffects|BrokenGlass1S [Indent level: 4],
                "brokenglass1s": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects14",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass14|DestructionEffects|BrokenGlass2S [Indent level: 4],
                "brokenglass2s": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects14",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass14|DestructionEffects|BrokenGlass3S [Indent level: 4],
                "brokenglass3s": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects14",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass14|DestructionEffects|BrokenGlass4S [Indent level: 4],
                "brokenglass4s": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects14",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass14|DestructionEffects|BrokenGlass5S [Indent level: 4],
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
        # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass15 [Indent level: 2],
        "hitglass15": {
            "name": "glass15",
            "visual": "glass15",
            "radius": 0.24,
            "armor": -5,
            "explosionshielding": 1,
            "minimalhit": -0.025,
            "passthrough": 0,
            "armorcomponent": "glass15",
            # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass15|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass15|DestructionEffects|BrokenGlass1 [Indent level: 4],
                "brokenglass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects15",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass15|DestructionEffects|BrokenGlass2 [Indent level: 4],
                "brokenglass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects15",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass15|DestructionEffects|BrokenGlass3 [Indent level: 4],
                "brokenglass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects15",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass15|DestructionEffects|BrokenGlass4 [Indent level: 4],
                "brokenglass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects15",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass15|DestructionEffects|BrokenGlass5 [Indent level: 4],
                "brokenglass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects15",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass15|DestructionEffects|BrokenGlass1S [Indent level: 4],
                "brokenglass1s": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects15",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass15|DestructionEffects|BrokenGlass2S [Indent level: 4],
                "brokenglass2s": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects15",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass15|DestructionEffects|BrokenGlass3S [Indent level: 4],
                "brokenglass3s": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects15",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass15|DestructionEffects|BrokenGlass4S [Indent level: 4],
                "brokenglass4s": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects15",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass15|DestructionEffects|BrokenGlass5S [Indent level: 4],
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
        # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass16 [Indent level: 2],
        "hitglass16": {
            "name": "glass16",
            "visual": "glass16",
            "radius": 0.24,
            "armor": -5,
            "explosionshielding": 1,
            "minimalhit": -0.025,
            "passthrough": 0,
            "armorcomponent": "glass16",
            # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass16|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass16|DestructionEffects|BrokenGlass1 [Indent level: 4],
                "brokenglass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects16",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass16|DestructionEffects|BrokenGlass2 [Indent level: 4],
                "brokenglass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects16",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass16|DestructionEffects|BrokenGlass3 [Indent level: 4],
                "brokenglass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects16",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass16|DestructionEffects|BrokenGlass4 [Indent level: 4],
                "brokenglass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects16",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass16|DestructionEffects|BrokenGlass5 [Indent level: 4],
                "brokenglass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects16",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass16|DestructionEffects|BrokenGlass1S [Indent level: 4],
                "brokenglass1s": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects16",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass16|DestructionEffects|BrokenGlass2S [Indent level: 4],
                "brokenglass2s": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects16",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass16|DestructionEffects|BrokenGlass3S [Indent level: 4],
                "brokenglass3s": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects16",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass16|DestructionEffects|BrokenGlass4S [Indent level: 4],
                "brokenglass4s": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects16",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass16|DestructionEffects|BrokenGlass5S [Indent level: 4],
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
        # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass17 [Indent level: 2],
        "hitglass17": {
            "name": "glass17",
            "visual": "glass17",
            "radius": 0.24,
            "armor": -5,
            "explosionshielding": 1,
            "minimalhit": -0.025,
            "passthrough": 0,
            "armorcomponent": "glass17",
            # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass17|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass17|DestructionEffects|BrokenGlass1 [Indent level: 4],
                "brokenglass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects17",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass17|DestructionEffects|BrokenGlass2 [Indent level: 4],
                "brokenglass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects17",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass17|DestructionEffects|BrokenGlass3 [Indent level: 4],
                "brokenglass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects17",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass17|DestructionEffects|BrokenGlass4 [Indent level: 4],
                "brokenglass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects17",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass17|DestructionEffects|BrokenGlass5 [Indent level: 4],
                "brokenglass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects17",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass17|DestructionEffects|BrokenGlass1S [Indent level: 4],
                "brokenglass1s": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects17",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass17|DestructionEffects|BrokenGlass2S [Indent level: 4],
                "brokenglass2s": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects17",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass17|DestructionEffects|BrokenGlass3S [Indent level: 4],
                "brokenglass3s": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects17",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass17|DestructionEffects|BrokenGlass4S [Indent level: 4],
                "brokenglass4s": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects17",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|HitPoints|HitGlass17|DestructionEffects|BrokenGlass5S [Indent level: 4],
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
    # Class: CfgVehicles|rhsusf_CH53E_USMC|Damage [Indent level: 1],
    "damage": {
        "tex": [],
        "mat": ["rhsusf|addons|rhsusf_ch53|data|ch53_1.rvmat","rhsusf|addons|rhsusf_ch53|data|ch53_1_damage.rvmat","rhsusf|addons|rhsusf_ch53|data|ch53_1_destruct.rvmat","rhsusf|addons|rhsusf_ch53|data|ch53_2.rvmat","rhsusf|addons|rhsusf_ch53|data|ch53_2_damage.rvmat","rhsusf|addons|rhsusf_ch53|data|ch53_2_destruct.rvmat","rhsusf|addons|rhsusf_ch53|data|glass.rvmat","rhsusf|addons|rhsusf_ch53|data|glass_damage.rvmat","rhsusf|addons|rhsusf_ch53|data|glass_damage.rvmat","rhsusf|addons|rhsusf_ch53|data|glassint.rvmat","rhsusf|addons|rhsusf_ch53|data|glassint_damage.rvmat","rhsusf|addons|rhsusf_ch53|data|glassint_damage.rvmat"]
    },
    # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD [Indent level: 1],
    "mfd": {
        # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1 [Indent level: 2]
        "rhsusf_ch53_hud_1": {
            "topleft": "HUD_top_left",
            "topright": "HUD_top_right",
            "bottomleft": "HUD_bottom_left",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0.15,1,0.15,1],
            "enableparallax": 0,
            # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Bones [Indent level: 3],
            "bones": {
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Bones|Velocity [Indent level: 4]
                "velocity": {
                    "type": "vector",
                    "source": "velocity",
                    "pos0": [0.5,0.5],
                    "pos10": [0.65,0.65]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Bones|Velocity_slip [Indent level: 4],
                "velocity_slip": {
                    "type": "vector",
                    "source": "velocity",
                    "pos0": [0.5,0.845],
                    "pos10": [0.53,0.845]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Bones|VspeedBone [Indent level: 4],
                "vspeedbone": {
                    "type": "linear",
                    "source": "vspeed",
                    "sourcescale": 1,
                    "min": -10,
                    "max": 10,
                    "minpos": [0.93,0.2],
                    "maxpos": [0.93,0.8]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Bones|RadarAltitudeBone [Indent level: 4],
                "radaraltitudebone": {
                    "type": "linear",
                    "source": "altitudeAGL",
                    "sourcescale": 1,
                    "min": 0,
                    "max": 60,
                    "minpos": [0.965,0.2],
                    "maxpos": [0.965,0.8]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Bones|HorizonBankRot [Indent level: 4],
                "horizonbankrot": {
                    "type": "rotational",
                    "source": "horizonBank",
                    "center": [0.5,0.5],
                    "min": -3.1416,
                    "max": 3.1416,
                    "minangle": -180,
                    "maxangle": 180,
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Bones|ForwardVec [Indent level: 4],
                "forwardvec": {
                    "type": "vector",
                    "source": "forward",
                    "pos0": [0,0],
                    "pos10": [0.25,0.25]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Bones|Level0 [Indent level: 4],
                "level0": {
                    "type": "horizon",
                    "pos0": [0.5,0.5],
                    "pos10": [0.78,0.78],
                    "angle": 0
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Bones|LevelP5 [Indent level: 4],
                "levelp5": {
                    "angle": 5,
                    "type": "horizon",
                    "pos0": [0.5,0.5],
                    "pos10": [0.78,0.78]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Bones|LevelM5 [Indent level: 4],
                "levelm5": {
                    "angle": -5,
                    "type": "horizon",
                    "pos0": [0.5,0.5],
                    "pos10": [0.78,0.78]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Bones|LevelP10 [Indent level: 4],
                "levelp10": {
                    "angle": 10,
                    "type": "horizon",
                    "pos0": [0.5,0.5],
                    "pos10": [0.78,0.78]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Bones|LevelM10 [Indent level: 4],
                "levelm10": {
                    "angle": -10,
                    "type": "horizon",
                    "pos0": [0.5,0.5],
                    "pos10": [0.78,0.78]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Bones|LevelP15 [Indent level: 4],
                "levelp15": {
                    "angle": 15,
                    "type": "horizon",
                    "pos0": [0.5,0.5],
                    "pos10": [0.78,0.78]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Bones|LevelM15 [Indent level: 4],
                "levelm15": {
                    "angle": -15,
                    "type": "horizon",
                    "pos0": [0.5,0.5],
                    "pos10": [0.78,0.78]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Bones|LevelP20 [Indent level: 4],
                "levelp20": {
                    "angle": 20,
                    "type": "horizon",
                    "pos0": [0.5,0.5],
                    "pos10": [0.78,0.78]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Bones|LevelM20 [Indent level: 4],
                "levelm20": {
                    "angle": -20,
                    "type": "horizon",
                    "pos0": [0.5,0.5],
                    "pos10": [0.78,0.78]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Bones|LevelP25 [Indent level: 4],
                "levelp25": {
                    "angle": 25,
                    "type": "horizon",
                    "pos0": [0.5,0.5],
                    "pos10": [0.78,0.78]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Bones|LevelM25 [Indent level: 4],
                "levelm25": {
                    "angle": -25,
                    "type": "horizon",
                    "pos0": [0.5,0.5],
                    "pos10": [0.78,0.78]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Bones|LevelP30 [Indent level: 4],
                "levelp30": {
                    "angle": 30,
                    "type": "horizon",
                    "pos0": [0.5,0.5],
                    "pos10": [0.78,0.78]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Bones|LevelM30 [Indent level: 4],
                "levelm30": {
                    "angle": -30,
                    "type": "horizon",
                    "pos0": [0.5,0.5],
                    "pos10": [0.78,0.78]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Bones|LevelP35 [Indent level: 4],
                "levelp35": {
                    "angle": 35,
                    "type": "horizon",
                    "pos0": [0.5,0.5],
                    "pos10": [0.78,0.78]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Bones|LevelM35 [Indent level: 4],
                "levelm35": {
                    "angle": -35,
                    "type": "horizon",
                    "pos0": [0.5,0.5],
                    "pos10": [0.78,0.78]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Bones|LevelP40 [Indent level: 4],
                "levelp40": {
                    "angle": 40,
                    "type": "horizon",
                    "pos0": [0.5,0.5],
                    "pos10": [0.78,0.78]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Bones|LevelM40 [Indent level: 4],
                "levelm40": {
                    "angle": -40,
                    "type": "horizon",
                    "pos0": [0.5,0.5],
                    "pos10": [0.78,0.78]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Bones|LevelP45 [Indent level: 4],
                "levelp45": {
                    "angle": 45,
                    "type": "horizon",
                    "pos0": [0.5,0.5],
                    "pos10": [0.78,0.78]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Bones|LevelM45 [Indent level: 4],
                "levelm45": {
                    "angle": -45,
                    "type": "horizon",
                    "pos0": [0.5,0.5],
                    "pos10": [0.78,0.78]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Bones|LevelP50 [Indent level: 4],
                "levelp50": {
                    "angle": 50,
                    "type": "horizon",
                    "pos0": [0.5,0.5],
                    "pos10": [0.78,0.78]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Bones|LevelM50 [Indent level: 4],
                "levelm50": {
                    "angle": -50,
                    "type": "horizon",
                    "pos0": [0.5,0.5],
                    "pos10": [0.78,0.78]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Bones|LevelP55 [Indent level: 4],
                "levelp55": {
                    "angle": 55,
                    "type": "horizon",
                    "pos0": [0.5,0.5],
                    "pos10": [0.78,0.78]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Bones|LevelM55 [Indent level: 4],
                "levelm55": {
                    "angle": -55,
                    "type": "horizon",
                    "pos0": [0.5,0.5],
                    "pos10": [0.78,0.78]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Bones|LevelP60 [Indent level: 4],
                "levelp60": {
                    "angle": 60,
                    "type": "horizon",
                    "pos0": [0.5,0.5],
                    "pos10": [0.78,0.78]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Bones|LevelM60 [Indent level: 4],
                "levelm60": {
                    "angle": -60,
                    "type": "horizon",
                    "pos0": [0.5,0.5],
                    "pos10": [0.78,0.78]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Bones|LevelP65 [Indent level: 4],
                "levelp65": {
                    "angle": 65,
                    "type": "horizon",
                    "pos0": [0.5,0.5],
                    "pos10": [0.78,0.78]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Bones|LevelM65 [Indent level: 4],
                "levelm65": {
                    "angle": -65,
                    "type": "horizon",
                    "pos0": [0.5,0.5],
                    "pos10": [0.78,0.78]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Bones|LevelP70 [Indent level: 4],
                "levelp70": {
                    "angle": 70,
                    "type": "horizon",
                    "pos0": [0.5,0.5],
                    "pos10": [0.78,0.78]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Bones|LevelM70 [Indent level: 4],
                "levelm70": {
                    "angle": -70,
                    "type": "horizon",
                    "pos0": [0.5,0.5],
                    "pos10": [0.78,0.78]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Bones|LevelP75 [Indent level: 4],
                "levelp75": {
                    "angle": 75,
                    "type": "horizon",
                    "pos0": [0.5,0.5],
                    "pos10": [0.78,0.78]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Bones|LevelM75 [Indent level: 4],
                "levelm75": {
                    "angle": -75,
                    "type": "horizon",
                    "pos0": [0.5,0.5],
                    "pos10": [0.78,0.78]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Bones|LevelP80 [Indent level: 4],
                "levelp80": {
                    "angle": 80,
                    "type": "horizon",
                    "pos0": [0.5,0.5],
                    "pos10": [0.78,0.78]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Bones|LevelM80 [Indent level: 4],
                "levelm80": {
                    "angle": -80,
                    "type": "horizon",
                    "pos0": [0.5,0.5],
                    "pos10": [0.78,0.78]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Bones|LevelP85 [Indent level: 4],
                "levelp85": {
                    "angle": 85,
                    "type": "horizon",
                    "pos0": [0.5,0.5],
                    "pos10": [0.78,0.78]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Bones|LevelM85 [Indent level: 4],
                "levelm85": {
                    "angle": -85,
                    "type": "horizon",
                    "pos0": [0.5,0.5],
                    "pos10": [0.78,0.78]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Bones|LevelP90 [Indent level: 4],
                "levelp90": {
                    "angle": 90,
                    "type": "horizon",
                    "pos0": [0.5,0.5],
                    "pos10": [0.78,0.78]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Bones|LevelM90 [Indent level: 4],
                "levelm90": {
                    "angle": -90,
                    "type": "horizon",
                    "pos0": [0.5,0.5],
                    "pos10": [0.78,0.78]
                }
            },
            # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw [Indent level: 3],
            "draw": {
                "color": [0.18,1,0.18],
                "alpha": 1,
                "condition": "on",
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|Horizont [Indent level: 4],
                "horizont": {
                    "cliptl": [0.15,0.15],
                    "clipbr": [0.85,0.85],
                    # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|Horizont|Dimmed [Indent level: 5],
                    "dimmed": {
                        # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|Horizont|Dimmed|Level0 [Indent level: 6]
                        "level0": {
                            "type": "line",
                            "points": [["Level0",[-0.42,0],1],["Level0",[-0.08,0],1],[],["Level0",[0.42,0],1],["Level0",[0.08,0],1],[]]
                        },
                        # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|Horizont|Dimmed|LevelM10 [Indent level: 6],
                        "levelm10": {
                            "type": "line",
                            "width": 3,
                            "points": [["LevelM10",[-0.2,-0.03],1],["LevelM10",[-0.2,0],1],["LevelM10",[-0.15,0],1],[],["LevelM10",[-0.1,0],1],["LevelM10",[-0.05,0],1],[],["LevelM10",[0.05,0],1],["LevelM10",[0.1,0],1],[],["LevelM10",[0.15,0],1],["LevelM10",[0.2,0],1],["LevelM10",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|Horizont|Dimmed|VALM_1_10 [Indent level: 6],
                        "valm_1_10": {
                            "type": "text",
                            "source": "static",
                            "text": -10,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM10",[-0.21,-0.05],1],
                            "right": ["LevelM10",[-0.16,-0.05],1],
                            "down": ["LevelM10",[-0.21,0],1]
                        },
                        # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|Horizont|Dimmed|VALM_2_10 [Indent level: 6],
                        "valm_2_10": {
                            "align": "right",
                            "pos": ["LevelM10",[0.21,-0.05],1],
                            "right": ["LevelM10",[0.26,-0.05],1],
                            "down": ["LevelM10",[0.21,0],1],
                            "type": "text",
                            "source": "static",
                            "text": -10,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|Horizont|Dimmed|LevelP10 [Indent level: 6],
                        "levelp10": {
                            "type": "line",
                            "width": 3,
                            "points": [["LevelP10",[-0.2,0.03],1],["LevelP10",[-0.2,0],1],["LevelP10",[-0.05,0],1],[],["LevelP10",[0.05,0],1],["LevelP10",[0.2,0],1],["LevelP10",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|Horizont|Dimmed|VALP_1_10 [Indent level: 6],
                        "valp_1_10": {
                            "type": "text",
                            "source": "static",
                            "text": "10",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP10",[-0.21,0],1],
                            "right": ["LevelP10",[-0.16,0],1],
                            "down": ["LevelP10",[-0.21,0.05],1]
                        },
                        # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|Horizont|Dimmed|VALP_2_10 [Indent level: 6],
                        "valp_2_10": {
                            "align": "right",
                            "pos": ["LevelP10",[0.21,0],1],
                            "right": ["LevelP10",[0.26,0],1],
                            "down": ["LevelP10",[0.21,0.05],1],
                            "type": "text",
                            "source": "static",
                            "text": "10",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|Horizont|Dimmed|LevelM20 [Indent level: 6],
                        "levelm20": {
                            "type": "line",
                            "width": 3,
                            "points": [["LevelM20",[-0.2,-0.03],1],["LevelM20",[-0.2,0],1],["LevelM20",[-0.15,0],1],[],["LevelM20",[-0.1,0],1],["LevelM20",[-0.05,0],1],[],["LevelM20",[0.05,0],1],["LevelM20",[0.1,0],1],[],["LevelM20",[0.15,0],1],["LevelM20",[0.2,0],1],["LevelM20",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|Horizont|Dimmed|VALM_1_20 [Indent level: 6],
                        "valm_1_20": {
                            "type": "text",
                            "source": "static",
                            "text": -20,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM20",[-0.21,-0.05],1],
                            "right": ["LevelM20",[-0.16,-0.05],1],
                            "down": ["LevelM20",[-0.21,0],1]
                        },
                        # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|Horizont|Dimmed|VALM_2_20 [Indent level: 6],
                        "valm_2_20": {
                            "align": "right",
                            "pos": ["LevelM20",[0.21,-0.05],1],
                            "right": ["LevelM20",[0.26,-0.05],1],
                            "down": ["LevelM20",[0.21,0],1],
                            "type": "text",
                            "source": "static",
                            "text": -20,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|Horizont|Dimmed|LevelP20 [Indent level: 6],
                        "levelp20": {
                            "type": "line",
                            "width": 3,
                            "points": [["LevelP20",[-0.2,0.03],1],["LevelP20",[-0.2,0],1],["LevelP20",[-0.05,0],1],[],["LevelP20",[0.05,0],1],["LevelP20",[0.2,0],1],["LevelP20",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|Horizont|Dimmed|VALP_1_20 [Indent level: 6],
                        "valp_1_20": {
                            "type": "text",
                            "source": "static",
                            "text": "20",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP20",[-0.21,0],1],
                            "right": ["LevelP20",[-0.16,0],1],
                            "down": ["LevelP20",[-0.21,0.05],1]
                        },
                        # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|Horizont|Dimmed|VALP_2_20 [Indent level: 6],
                        "valp_2_20": {
                            "align": "right",
                            "pos": ["LevelP20",[0.21,0],1],
                            "right": ["LevelP20",[0.26,0],1],
                            "down": ["LevelP20",[0.21,0.05],1],
                            "type": "text",
                            "source": "static",
                            "text": "20",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|Horizont|Dimmed|LevelM30 [Indent level: 6],
                        "levelm30": {
                            "type": "line",
                            "width": 3,
                            "points": [["LevelM30",[-0.2,-0.03],1],["LevelM30",[-0.2,0],1],["LevelM30",[-0.15,0],1],[],["LevelM30",[-0.1,0],1],["LevelM30",[-0.05,0],1],[],["LevelM30",[0.05,0],1],["LevelM30",[0.1,0],1],[],["LevelM30",[0.15,0],1],["LevelM30",[0.2,0],1],["LevelM30",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|Horizont|Dimmed|VALM_1_30 [Indent level: 6],
                        "valm_1_30": {
                            "type": "text",
                            "source": "static",
                            "text": -30,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM30",[-0.21,-0.05],1],
                            "right": ["LevelM30",[-0.16,-0.05],1],
                            "down": ["LevelM30",[-0.21,0],1]
                        },
                        # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|Horizont|Dimmed|VALM_2_30 [Indent level: 6],
                        "valm_2_30": {
                            "align": "right",
                            "pos": ["LevelM30",[0.21,-0.05],1],
                            "right": ["LevelM30",[0.26,-0.05],1],
                            "down": ["LevelM30",[0.21,0],1],
                            "type": "text",
                            "source": "static",
                            "text": -30,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|Horizont|Dimmed|LevelP30 [Indent level: 6],
                        "levelp30": {
                            "type": "line",
                            "width": 3,
                            "points": [["LevelP30",[-0.2,0.03],1],["LevelP30",[-0.2,0],1],["LevelP30",[-0.05,0],1],[],["LevelP30",[0.05,0],1],["LevelP30",[0.2,0],1],["LevelP30",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|Horizont|Dimmed|VALP_1_30 [Indent level: 6],
                        "valp_1_30": {
                            "type": "text",
                            "source": "static",
                            "text": "30",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP30",[-0.21,0],1],
                            "right": ["LevelP30",[-0.16,0],1],
                            "down": ["LevelP30",[-0.21,0.05],1]
                        },
                        # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|Horizont|Dimmed|VALP_2_30 [Indent level: 6],
                        "valp_2_30": {
                            "align": "right",
                            "pos": ["LevelP30",[0.21,0],1],
                            "right": ["LevelP30",[0.26,0],1],
                            "down": ["LevelP30",[0.21,0.05],1],
                            "type": "text",
                            "source": "static",
                            "text": "30",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|Horizont|Dimmed|LevelM40 [Indent level: 6],
                        "levelm40": {
                            "type": "line",
                            "width": 3,
                            "points": [["LevelM40",[-0.2,-0.03],1],["LevelM40",[-0.2,0],1],["LevelM40",[-0.15,0],1],[],["LevelM40",[-0.1,0],1],["LevelM40",[-0.05,0],1],[],["LevelM40",[0.05,0],1],["LevelM40",[0.1,0],1],[],["LevelM40",[0.15,0],1],["LevelM40",[0.2,0],1],["LevelM40",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|Horizont|Dimmed|VALM_1_40 [Indent level: 6],
                        "valm_1_40": {
                            "type": "text",
                            "source": "static",
                            "text": -40,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM40",[-0.21,-0.05],1],
                            "right": ["LevelM40",[-0.16,-0.05],1],
                            "down": ["LevelM40",[-0.21,0],1]
                        },
                        # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|Horizont|Dimmed|VALM_2_40 [Indent level: 6],
                        "valm_2_40": {
                            "align": "right",
                            "pos": ["LevelM40",[0.21,-0.05],1],
                            "right": ["LevelM40",[0.26,-0.05],1],
                            "down": ["LevelM40",[0.21,0],1],
                            "type": "text",
                            "source": "static",
                            "text": -40,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|Horizont|Dimmed|LevelP40 [Indent level: 6],
                        "levelp40": {
                            "type": "line",
                            "width": 3,
                            "points": [["LevelP40",[-0.2,0.03],1],["LevelP40",[-0.2,0],1],["LevelP40",[-0.05,0],1],[],["LevelP40",[0.05,0],1],["LevelP40",[0.2,0],1],["LevelP40",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|Horizont|Dimmed|VALP_1_40 [Indent level: 6],
                        "valp_1_40": {
                            "type": "text",
                            "source": "static",
                            "text": "40",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP40",[-0.21,0],1],
                            "right": ["LevelP40",[-0.16,0],1],
                            "down": ["LevelP40",[-0.21,0.05],1]
                        },
                        # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|Horizont|Dimmed|VALP_2_40 [Indent level: 6],
                        "valp_2_40": {
                            "align": "right",
                            "pos": ["LevelP40",[0.21,0],1],
                            "right": ["LevelP40",[0.26,0],1],
                            "down": ["LevelP40",[0.21,0.05],1],
                            "type": "text",
                            "source": "static",
                            "text": "40",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|Horizont|Dimmed|LevelM50 [Indent level: 6],
                        "levelm50": {
                            "type": "line",
                            "width": 3,
                            "points": [["LevelM50",[-0.2,-0.03],1],["LevelM50",[-0.2,0],1],["LevelM50",[-0.15,0],1],[],["LevelM50",[-0.1,0],1],["LevelM50",[-0.05,0],1],[],["LevelM50",[0.05,0],1],["LevelM50",[0.1,0],1],[],["LevelM50",[0.15,0],1],["LevelM50",[0.2,0],1],["LevelM50",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|Horizont|Dimmed|VALM_1_50 [Indent level: 6],
                        "valm_1_50": {
                            "type": "text",
                            "source": "static",
                            "text": -50,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM50",[-0.21,-0.05],1],
                            "right": ["LevelM50",[-0.16,-0.05],1],
                            "down": ["LevelM50",[-0.21,0],1]
                        },
                        # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|Horizont|Dimmed|VALM_2_50 [Indent level: 6],
                        "valm_2_50": {
                            "align": "right",
                            "pos": ["LevelM50",[0.21,-0.05],1],
                            "right": ["LevelM50",[0.26,-0.05],1],
                            "down": ["LevelM50",[0.21,0],1],
                            "type": "text",
                            "source": "static",
                            "text": -50,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|Horizont|Dimmed|LevelP50 [Indent level: 6],
                        "levelp50": {
                            "type": "line",
                            "width": 3,
                            "points": [["LevelP50",[-0.2,0.03],1],["LevelP50",[-0.2,0],1],["LevelP50",[-0.05,0],1],[],["LevelP50",[0.05,0],1],["LevelP50",[0.2,0],1],["LevelP50",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|Horizont|Dimmed|VALP_1_50 [Indent level: 6],
                        "valp_1_50": {
                            "type": "text",
                            "source": "static",
                            "text": "50",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP50",[-0.21,0],1],
                            "right": ["LevelP50",[-0.16,0],1],
                            "down": ["LevelP50",[-0.21,0.05],1]
                        },
                        # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|Horizont|Dimmed|VALP_2_50 [Indent level: 6],
                        "valp_2_50": {
                            "align": "right",
                            "pos": ["LevelP50",[0.21,0],1],
                            "right": ["LevelP50",[0.26,0],1],
                            "down": ["LevelP50",[0.21,0.05],1],
                            "type": "text",
                            "source": "static",
                            "text": "50",
                            "scale": 1,
                            "sourcescale": 1
                        }
                    }
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|StaticBank [Indent level: 4],
                "staticbank": {
                    "type": "line",
                    "width": 3,
                    "points": [[[0.4782,0.251],1],[[0.4773,0.241],1],[],[[0.4566,0.2538],1],[[0.4549,0.2439],1],[],[[0.4353,0.2585],1],[[0.4301,0.2392],1],[],[[0.4145,0.2651],1],[[0.4111,0.2557],1],[],[[0.3943,0.2734],1],[[0.3901,0.2644],1],[],[[0.375,0.2835],1],[[0.365,0.2662],1],[],[[0.3232,0.3232],1],[[0.3091,0.3091],1],[],[[0.2835,0.375],1],[[0.2662,0.365],1],[],[["0.5 + (0.5- 0.4782)",0.251],1],[["0.5 + (0.5- 0.4773)",0.241],1],[],[["0.5 + (0.5- 0.4566)",0.2538],1],[["0.5 + (0.5- 0.4549)",0.2439],1],[],[["0.5 + (0.5- 0.4353)",0.2585],1],[["0.5 + (0.5- 0.4301)",0.2392],1],[],[["0.5 + (0.5- 0.4145)",0.2651],1],[["0.5 + (0.5- 0.4111)",0.2557],1],[],[["0.5 + (0.5- 0.3943)",0.2734],1],[["0.5 + (0.5- 0.3901)",0.2644],1],[],[["0.5 + (0.5- 0.3750)",0.2835],1],[["0.5 + (0.5- 0.3650)",0.2662],1],[],[["0.5 + (0.5- 0.3232)",0.3232],1],[["0.5 + (0.5- 0.3091)",0.3091],1],[],[["0.5 + (0.5- 0.2835)",0.375],1],[["0.5 + (0.5- 0.2662)",0.365],1],[],[[0.5,"0.5 - 0.25"],1],[[0.5,"0.5 - 0.28"],1]]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|HorizonBankRot [Indent level: 4],
                "horizonbankrot": {
                    "type": "line",
                    "width": 3,
                    "points": [["HorizonBankRot",[0,0.25],1],["HorizonBankRot",[-0.01,0.23],1],["HorizonBankRot",[0.01,0.23],1],["HorizonBankRot",[0,0.25],1]]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|Waterline [Indent level: 4],
                "waterline": {
                    "type": "line",
                    "width": 7,
                    "points": [[[0.45,0.5],1],[[0.48,0.5],1],[[0.49,0.525],1],[[0.5,0.5],1],[[0.51,0.525],1],[[0.52,0.5],1],[[0.55,0.5],1]]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|Slip_ball_group [Indent level: 4],
                "slip_ball_group": {
                    # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|Slip_ball_group|Slip_bars [Indent level: 5]
                    "slip_bars": {
                        "type": "line",
                        "width": 4,
                        "points": [[["0.5-0.018","0.9-0.04"],1],[["0.5-0.018","0.9-0.075"],1],[],[["0.5+0.018","0.9-0.04"],1],[["0.5+0.018","0.9-0.075"],1],[],[["0.5+0.2","0.9-0.04"],1],[["0.5-0.2","0.9-0.04"],1]]
                    },
                    # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|Slip_ball_group|Slip_ball [Indent level: 5],
                    "slip_ball": {
                        "type": "line",
                        "width": 6,
                        "points": [["Velocity_slip",1,["0 * 0.75","-0.02 * 0.75"],1],["Velocity_slip",1,["0.0099999998 * 0.75","-0.01732 * 0.75"],1],["Velocity_slip",1,["0.01732 * 0.75","-0.0099999998 * 0.75"],1],["Velocity_slip",1,["0.02 * 0.75","0 * 0.75"],1],["Velocity_slip",1,["0.01732 * 0.75","0.0099999998 * 0.75"],1],["Velocity_slip",1,["0.0099999998 * 0.75","0.01732 * 0.75"],1],["Velocity_slip",1,["0 * 0.75","0.02 * 0.75"],1],["Velocity_slip",1,["-0.0099999998 * 0.75","0.01732 * 0.75"],1],["Velocity_slip",1,["-0.01732 * 0.75","0.0099999998 * 0.75"],1],["Velocity_slip",1,["-0.02 * 0.75","0 * 0.75"],1],["Velocity_slip",1,["-0.01732 * 0.75","-0.0099999998 * 0.75"],1],["Velocity_slip",1,["-0.0099999998 * 0.75","-0.01732 * 0.75"],1],["Velocity_slip",1,["0 * 0.75","-0.02 * 0.75"],1],[],["Velocity_slip",1,["0 * 0.6","-0.02 * 0.6"],1],["Velocity_slip",1,["0.0099999998 * 0.6","-0.01732 * 0.6"],1],["Velocity_slip",1,["0.01732 * 0.6","-0.0099999998 * 0.6"],1],["Velocity_slip",1,["0.02 * 0.6","0 * 0.6"],1],["Velocity_slip",1,["0.01732 * 0.6","0.0099999998 * 0.6"],1],["Velocity_slip",1,["0.0099999998 * 0.6","0.01732 * 0.6"],1],["Velocity_slip",1,["0 * 0.6","0.02 * 0.6"],1],["Velocity_slip",1,["-0.0099999998 * 0.6","0.01732 * 0.6"],1],["Velocity_slip",1,["-0.01732 * 0.6","0.0099999998 * 0.6"],1],["Velocity_slip",1,["-0.02 * 0.6","0 * 0.6"],1],["Velocity_slip",1,["-0.01732 * 0.6","-0.0099999998 * 0.6"],1],["Velocity_slip",1,["-0.0099999998 * 0.6","-0.01732 * 0.6"],1],["Velocity_slip",1,["0 * 0.6","-0.02 * 0.6"],1],[],["Velocity_slip",1,["0 * 0.5","-0.02 * 0.5"],1],["Velocity_slip",1,["0.0099999998 * 0.5","-0.01732 * 0.5"],1],["Velocity_slip",1,["0.01732 * 0.5","-0.0099999998 * 0.5"],1],["Velocity_slip",1,["0.02 * 0.5","0 * 0.5"],1],["Velocity_slip",1,["0.01732 * 0.5","0.0099999998 * 0.5"],1],["Velocity_slip",1,["0.0099999998 * 0.5","0.01732 * 0.5"],1],["Velocity_slip",1,["0 * 0.5","0.02 * 0.5"],1],["Velocity_slip",1,["-0.0099999998 * 0.5","0.01732 * 0.5"],1],["Velocity_slip",1,["-0.01732 * 0.5","0.0099999998 * 0.5"],1],["Velocity_slip",1,["-0.02 * 0.5","0 * 0.5"],1],["Velocity_slip",1,["-0.01732 * 0.5","-0.0099999998 * 0.5"],1],["Velocity_slip",1,["-0.0099999998 * 0.5","-0.01732 * 0.5"],1],["Velocity_slip",1,["0 * 0.5","-0.02 * 0.5"],1],[],["Velocity_slip",1,["0 * 0.4","-0.02 * 0.4"],1],["Velocity_slip",1,["0.0099999998 * 0.4","-0.01732 * 0.4"],1],["Velocity_slip",1,["0.01732 * 0.4","-0.0099999998 * 0.4"],1],["Velocity_slip",1,["0.02 * 0.4","0 * 0.4"],1],["Velocity_slip",1,["0.01732 * 0.4","0.0099999998 * 0.4"],1],["Velocity_slip",1,["0.0099999998 * 0.4","0.01732 * 0.4"],1],["Velocity_slip",1,["0 * 0.4","0.02 * 0.4"],1],["Velocity_slip",1,["-0.0099999998 * 0.4","0.01732 * 0.4"],1],["Velocity_slip",1,["-0.01732 * 0.4","0.0099999998 * 0.4"],1],["Velocity_slip",1,["-0.02 * 0.4","0 * 0.4"],1],["Velocity_slip",1,["-0.01732 * 0.4","-0.0099999998 * 0.4"],1],["Velocity_slip",1,["-0.0099999998 * 0.4","-0.01732 * 0.4"],1],["Velocity_slip",1,["0 * 0.4","-0.02 * 0.4"],1],[],["Velocity_slip",1,["0 * 0.30","-0.02 * 0.30"],1],["Velocity_slip",1,["0.0099999998 * 0.30","-0.01732 * 0.30"],1],["Velocity_slip",1,["0.01732 * 0.30","-0.0099999998 * 0.30"],1],["Velocity_slip",1,["0.02 * 0.30","0 * 0.30"],1],["Velocity_slip",1,["0.01732 * 0.30","0.0099999998 * 0.30"],1],["Velocity_slip",1,["0.0099999998 * 0.30","0.01732 * 0.30"],1],["Velocity_slip",1,["0 * 0.30","0.02 * 0.30"],1],["Velocity_slip",1,["-0.0099999998 * 0.30","0.01732 * 0.30"],1],["Velocity_slip",1,["-0.01732 * 0.30","0.0099999998 * 0.30"],1],["Velocity_slip",1,["-0.02 * 0.30","0 * 0.30"],1],["Velocity_slip",1,["-0.01732 * 0.30","-0.0099999998 * 0.30"],1],["Velocity_slip",1,["-0.0099999998 * 0.30","-0.01732 * 0.30"],1],["Velocity_slip",1,["0 * 0.30","-0.02 * 0.30"],1],[],["Velocity_slip",1,["0 * 0.20","-0.02 * 0.20"],1],["Velocity_slip",1,["0.0099999998 * 0.20","-0.01732 * 0.20"],1],["Velocity_slip",1,["0.01732 * 0.20","-0.0099999998 * 0.20"],1],["Velocity_slip",1,["0.02 * 0.20","0 * 0.20"],1],["Velocity_slip",1,["0.01732 * 0.20","0.0099999998 * 0.20"],1],["Velocity_slip",1,["0.0099999998 * 0.20","0.01732 * 0.20"],1],["Velocity_slip",1,["0 * 0.20","0.02 * 0.20"],1],["Velocity_slip",1,["-0.0099999998 * 0.20","0.01732 * 0.20"],1],["Velocity_slip",1,["-0.01732 * 0.20","0.0099999998 * 0.20"],1],["Velocity_slip",1,["-0.02 * 0.20","0 * 0.20"],1],["Velocity_slip",1,["-0.01732 * 0.20","-0.0099999998 * 0.20"],1],["Velocity_slip",1,["-0.0099999998 * 0.20","-0.01732 * 0.20"],1],["Velocity_slip",1,["0 * 0.20","-0.02 * 0.20"],1],[],["Velocity_slip",1,["0 * 0.1","-0.02 * 0.1"],1],["Velocity_slip",1,["0.0099999998 * 0.1","-0.01732 * 0.1"],1],["Velocity_slip",1,["0.01732 * 0.1","-0.0099999998 * 0.1"],1],["Velocity_slip",1,["0.02 * 0.1","0 * 0.1"],1],["Velocity_slip",1,["0.01732 * 0.1","0.0099999998 * 0.1"],1],["Velocity_slip",1,["0.0099999998 * 0.1","0.01732 * 0.1"],1],["Velocity_slip",1,["0 * 0.1","0.02 * 0.1"],1],["Velocity_slip",1,["-0.0099999998 * 0.1","0.01732 * 0.1"],1],["Velocity_slip",1,["-0.01732 * 0.1","0.0099999998 * 0.1"],1],["Velocity_slip",1,["-0.02 * 0.1","0 * 0.1"],1],["Velocity_slip",1,["-0.01732 * 0.1","-0.0099999998 * 0.1"],1],["Velocity_slip",1,["-0.0099999998 * 0.1","-0.01732 * 0.1"],1],["Velocity_slip",1,["0 * 0.1","-0.02 * 0.1"],1]]
                    }
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|LightsGroup [Indent level: 4],
                "lightsgroup": {
                    "type": "group",
                    "condition": "lights",
                    # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|LightsGroup|LightsText [Indent level: 5],
                    "lightstext": {
                        "type": "text",
                        "source": "static",
                        "text": "LIGHTS",
                        "align": "right",
                        "scale": 1,
                        "pos": [[0.03,"0.53 + 0.055"],1],
                        "right": [[0.07,"0.53 + 0.055"],1],
                        "down": [[0.03,"0.53 + 0.095"],1]
                    }
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|CollisionLightsGroup [Indent level: 4],
                "collisionlightsgroup": {
                    "type": "group",
                    "condition": "collisionlights",
                    # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|CollisionLightsGroup|CollisionLightsText [Indent level: 5],
                    "collisionlightstext": {
                        "type": "text",
                        "source": "static",
                        "text": "A-COL",
                        "align": "right",
                        "scale": 1,
                        "pos": [[0.03,"0.53 + 0.105"],1],
                        "right": [[0.07,"0.53 + 0.105"],1],
                        "down": [[0.03,"0.53 + 0.145"],1]
                    }
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|GearGroup [Indent level: 4],
                "geargroup": {
                    "type": "group",
                    "condition": "ils",
                    # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|GearGroup|GearText [Indent level: 5],
                    "geartext": {
                        "type": "text",
                        "source": "static",
                        "text": "GEAR",
                        "align": "right",
                        "scale": 1,
                        "pos": [[0.03,"0.53 + 0.155"],1],
                        "right": [[0.07,"0.53 + 0.155"],1],
                        "down": [[0.03,"0.53 + 0.195"],1]
                    }
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|SpeedNumber [Indent level: 4],
                "speednumber": {
                    "type": "text",
                    "align": "right",
                    "scale": 1,
                    "source": "speed",
                    "sourcescale": 3.6,
                    "pos": [[0.03,0.475],1],
                    "right": [[0.08,0.475],1],
                    "down": [[0.03,0.525],1]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|TorqueNumber [Indent level: 4],
                "torquenumber": {
                    "condition": "simulRTD",
                    # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|TorqueNumber|Torque_number [Indent level: 5],
                    "torque_number": {
                        "type": "text",
                        "align": "left",
                        "scale": 1,
                        "source": "rtdRotorTorque",
                        "sourcescale": 488,
                        "pos": [[0.065,0.175],1],
                        "right": [[0.115,0.175],1],
                        "down": [[0.065,0.225],1]
                    },
                    # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|TorqueNumber|Torquetext [Indent level: 5],
                    "torquetext": {
                        "type": "text",
                        "source": "static",
                        "text": "%",
                        "align": "right",
                        "scale": 1,
                        "pos": [[0.07,0.175],1],
                        "right": [[0.12,0.175],1],
                        "down": [[0.07,0.225],1]
                    }
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|AltNumber [Indent level: 4],
                "altnumber": {
                    "align": "right",
                    "source": "altitudeAGL",
                    "sourcescale": 1,
                    "pos": [[0.83,0.475],1],
                    "right": [[0.88,0.475],1],
                    "down": [[0.83,0.525],1],
                    "type": "text",
                    "scale": 1
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|ASLNumber [Indent level: 4],
                "aslnumber": {
                    "type": "text",
                    "source": "altitudeASL",
                    "sourcescale": 1,
                    "align": "right",
                    "scale": 1,
                    "pos": [[0.835,0.18],1],
                    "right": [[0.875,0.18],1],
                    "down": [[0.835,0.22],1]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|VspeedScalePosta [Indent level: 4],
                "vspeedscaleposta": {
                    "type": "line",
                    "width": 5,
                    "points": [[[0.98,0.2],1],[[1,0.2],1],[],[[0.93,0.2],1],[[0.95,0.2],1],[],[[0.98,0.35],1],[[1,0.35],1],[],[[0.93,0.35],1],[[0.95,0.35],1],[],[[0.94,0.38],1],[[0.95,0.38],1],[],[[0.94,0.41],1],[[0.95,0.41],1],[],[[0.94,0.44],1],[[0.95,0.44],1],[],[[0.94,0.47],1],[[0.95,0.47],1],[],[[0.98,0.5],1],[[1,0.5],1],[],[[0.93,0.5],1],[[0.95,0.5],1],[],[[0.94,0.53],1],[[0.95,0.53],1],[],[[0.94,0.56],1],[[0.95,0.56],1],[],[[0.94,0.59],1],[[0.95,0.59],1],[],[[0.94,0.62],1],[[0.95,0.62],1],[],[[0.98,0.65],1],[[1,0.65],1],[],[[0.93,0.65],1],[[0.95,0.65],1],[],[[0.99,0.68],1],[[0.98,0.68],1],[],[[0.99,0.71],1],[[0.98,0.71],1],[],[[0.99,0.74],1],[[0.98,0.74],1],[],[[0.99,0.77],1],[[0.98,0.77],1],[],[[0.98,0.8],1],[[1,0.8],1],[],[[0.93,0.8],1],[[0.95,0.8],1],[]]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|RadarAltitudeBand [Indent level: 4],
                "radaraltitudeband": {
                    "cliptl": [0,0.2],
                    "clipbr": [1,0.8],
                    # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|RadarAltitudeBand|radarbanda [Indent level: 5],
                    "radarbanda": {
                        "type": "line",
                        "width": 17,
                        "points": [["RadarAltitudeBone",[0,0],1],["RadarAltitudeBone",[0,0.6],1]]
                    }
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|VspeedBand [Indent level: 4],
                "vspeedband": {
                    "type": "line",
                    "width": 3,
                    "points": [["VspeedBone",[-0.01,0],1],["VspeedBone",[-0.025,-0.015],1],["VspeedBone",[-0.025,0.015],1],["VspeedBone",[-0.01,0],1],[]]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|HeadingNumber [Indent level: 4],
                "headingnumber": {
                    "source": "heading",
                    "sourcescale": 1,
                    "align": "center",
                    "pos": [[0.5,0.045],1],
                    "right": [[0.56,0.045],1],
                    "down": [[0.5,"0.045 + 0.06"],1],
                    "type": "text",
                    "scale": 1
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|Center_box [Indent level: 4],
                "center_box": {
                    "type": "line",
                    "width": 1.5,
                    "points": [[[0.45,"0.02 + 0.085 - 0.06"],1],[["0.45 + 0.10","0.02 + 0.085 - 0.06"],1],[["0.45 + 0.10","0.02 + 0.085"],1],[[0.45,"0.02 + 0.085"],1],[[0.45,"0.02 + 0.085 - 0.06"],1]]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|HeadingArrow [Indent level: 4],
                "headingarrow": {
                    "type": "line",
                    "width": 7,
                    "points": [[["0.5","0.128 + 0.03"],1],[[0.5,0.128],1]]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|HeadingScale_LEFT [Indent level: 4],
                "headingscale_left": {
                    "cliptl": [0,0],
                    "clipbr": [0.45,1],
                    # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|HeadingScale_LEFT|Heading_group [Indent level: 5],
                    "heading_group": {
                        "type": "scale",
                        "horizontal": 1,
                        "source": "heading",
                        "sourcescale": 1,
                        "width": 5,
                        "top": 0.12,
                        "center": 0.5,
                        "bottom": 0.88,
                        "linexleft": "0.03 + 0.085",
                        "lineyright": "0.02 + 0.085",
                        "linexleftmajor": "0.04 + 0.085",
                        "lineyrightmajor": "0.02 + 0.085",
                        "majorlineeach": 3,
                        "numbereach": 3,
                        "step": 10,
                        "stepsize": "0.05",
                        "align": "center",
                        "scale": 1,
                        "pos": [0.12,"0.0 + 0.065"],
                        "right": [0.16,"0.0 + 0.065"],
                        "down": [0.12,"0.04 + 0.065"]
                    }
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|HeadingScale_RIGHT [Indent level: 4],
                "headingscale_right": {
                    "cliptl": [0.55,0],
                    "clipbr": [1,1],
                    # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|HeadingScale_RIGHT|Heading_group [Indent level: 5],
                    "heading_group": {
                        "type": "scale",
                        "horizontal": 1,
                        "source": "heading",
                        "sourcescale": 1,
                        "width": 5,
                        "top": 0.12,
                        "center": 0.5,
                        "bottom": 0.88,
                        "linexleft": "0.03 + 0.085",
                        "lineyright": "0.02 + 0.085",
                        "linexleftmajor": "0.04 + 0.085",
                        "lineyrightmajor": "0.02 + 0.085",
                        "majorlineeach": 3,
                        "numbereach": 3,
                        "step": 10,
                        "stepsize": "0.05",
                        "align": "center",
                        "scale": 1,
                        "pos": [0.12,"0.0 + 0.065"],
                        "right": [0.16,"0.0 + 0.065"],
                        "down": [0.12,"0.04 + 0.065"]
                    }
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|HeadingScale_BOTTOM [Indent level: 4],
                "headingscale_bottom": {
                    "cliptl": [0.45,"0.02 + 0.085"],
                    "clipbr": ["0.45 + 0.10",1],
                    # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|HeadingScale_BOTTOM|Heading_group [Indent level: 5],
                    "heading_group": {
                        "type": "scale",
                        "horizontal": 1,
                        "source": "heading",
                        "sourcescale": 1,
                        "width": 5,
                        "top": 0.12,
                        "center": 0.5,
                        "bottom": 0.88,
                        "linexleft": "0.03 + 0.085",
                        "lineyright": "0.02 + 0.085",
                        "linexleftmajor": "0.04 + 0.085",
                        "lineyrightmajor": "0.02 + 0.085",
                        "majorlineeach": 3,
                        "numbereach": 3,
                        "step": 10,
                        "stepsize": "0.05",
                        "align": "center",
                        "scale": 1,
                        "pos": [0.12,"0.0 + 0.065"],
                        "right": [0.16,"0.0 + 0.065"],
                        "down": [0.12,"0.04 + 0.065"]
                    }
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|Fuel_Text [Indent level: 4],
                "fuel_text": {
                    "type": "text",
                    "source": "static",
                    "text": "Fuel",
                    "align": "right",
                    "scale": 1,
                    "pos": [[0.85,0.86],1],
                    "right": [[0.89,0.86],1],
                    "down": [[0.85,0.9],1]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_1|Draw|Fuel_Number [Indent level: 4],
                "fuel_number": {
                    "type": "text",
                    "source": "fuel",
                    "sourcescale": 100,
                    "align": "right",
                    "scale": 1,
                    "pos": [[0.92,0.86],1],
                    "right": [[0.96,0.86],1],
                    "down": [[0.92,0.9],1]
                }
            },
            "helmetmounteddisplay": 1,
            "helmetposition": [-0.04,0.04,0.1],
            "helmetright": [0.08,0,0],
            "helmetdown": [0,-0.08,0]
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_2 [Indent level: 2],
        "rhsusf_ch53_hud_2": {
            "topleft": "HUD_top_left",
            "topright": "HUD_top_right",
            "bottomleft": "HUD_bottom_left",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0.15,1,0.15,1],
            "enableparallax": 0,
            # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_2|Bones [Indent level: 3],
            "bones": {
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_2|Bones|Velocity [Indent level: 4]
                "velocity": {
                    "type": "vector",
                    "source": "velocity",
                    "pos0": [0.5,0.5],
                    "pos10": [0.75,0.75]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_2|Bones|ForwardVec1 [Indent level: 4],
                "forwardvec1": {
                    "type": "vector",
                    "source": "forward",
                    "pos0": [0,0],
                    "pos10": [0.25,0.25]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_2|Bones|ForwardVec [Indent level: 4],
                "forwardvec": {
                    "type": "vector",
                    "source": "forward",
                    "pos0": [0,0],
                    "pos10": [0.253,0.253]
                }
            },
            # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_2|Draw [Indent level: 3],
            "draw": {
                "color": [0.18,1,0.18],
                "alpha": 1,
                "condition": "on",
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_2|Draw|PlaneMovementCrosshair [Indent level: 4],
                "planemovementcrosshair": {
                    "type": "line",
                    "width": 7,
                    "points": [["ForwardVec1",1,"Velocity",1,[0,-0.02],1],["ForwardVec1",1,"Velocity",1,[0.01,-0.01732],1],["ForwardVec1",1,"Velocity",1,[0.01732,-0.01],1],["ForwardVec1",1,"Velocity",1,[0.02,0],1],["ForwardVec1",1,"Velocity",1,[0.01732,0.01],1],["ForwardVec1",1,"Velocity",1,[0.01,0.01732],1],["ForwardVec1",1,"Velocity",1,[0,0.02],1],["ForwardVec1",1,"Velocity",1,[-0.01,0.01732],1],["ForwardVec1",1,"Velocity",1,[-0.01732,0.01],1],["ForwardVec1",1,"Velocity",1,[-0.02,0],1],["ForwardVec1",1,"Velocity",1,[-0.01732,-0.01],1],["ForwardVec1",1,"Velocity",1,[-0.01,-0.01732],1],["ForwardVec1",1,"Velocity",1,[0,-0.02],1],[],["ForwardVec1",1,"Velocity",1,[0.04,0],1],["ForwardVec1",1,"Velocity",1,[0.02,0],1],[],["ForwardVec1",1,"Velocity",1,[-0.04,0],1],["ForwardVec1",1,"Velocity",1,[-0.02,0],1],[],["ForwardVec1",1,"Velocity",1,[0,-0.04],1],["ForwardVec1",1,"Velocity",1,[0,-0.02],1]]
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_2|Draw|AC_Centerline [Indent level: 4],
                "ac_centerline": {
                    "type": "group",
                    "condition": "on",
                    # Class: CfgVehicles|rhsusf_CH53E_USMC|MFD|rhsusf_CH53_HUD_2|Draw|AC_Centerline|AC_Cross [Indent level: 5],
                    "ac_cross": {
                        "type": "line",
                        "width": 4,
                        "points": [["ForwardVec",1,[" -0.006 + 0.5","0 + 0.5"],1],["ForwardVec",1,[" 0.006 + 0.5","0 + 0.5"],1],[],["ForwardVec",1,[" -0.0 + 0.5","0.006 + 0.5"],1],["ForwardVec",1,[" 0.0 + 0.5","-0.006 + 0.5"],1]]
                    }
                }
            },
            "helmetmounteddisplay": 1,
            "helmetposition": [-0.035,0.035,0.1],
            "helmetright": [0.07,0,0],
            "helmetdown": [0,-0.07,0]
        }
    },
    # Class: CfgVehicles|rhsusf_CH53E_USMC|Reflectors [Indent level: 1],
    "reflectors": {
        # Class: CfgVehicles|rhsusf_CH53E_USMC|Reflectors|Left [Indent level: 2]
        "left": {
            "color": [7000,7500,10000,1],
            "ambient": [100,100,100,0],
            "intensity": 50,
            "size": 1,
            "innerangle": 5,
            "outerangle": 75,
            "conefadecoef": 10,
            "position": "LandLeft",
            "direction": "LandLeftDir",
            "hitpoint": "LandLeft",
            "selection": "LandLeft",
            "useflare": 1,
            "flaresize": 8,
            "flaremaxdistance": 300,
            "daylight": 0,
            # Class: CfgVehicles|rhsusf_CH53E_USMC|Reflectors|Left|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 0,
                "hardlimitstart": 200,
                "hardlimitend": 250
            }
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|Reflectors|Right [Indent level: 2],
        "right": {
            "position": "LandRight",
            "direction": "LandRightDir",
            "hitpoint": "LandRight",
            "selection": "LandRight",
            "color": [7000,7500,10000,1],
            "ambient": [100,100,100,0],
            "intensity": 50,
            "size": 1,
            "innerangle": 5,
            "outerangle": 75,
            "conefadecoef": 10,
            "useflare": 1,
            "flaresize": 8,
            "flaremaxdistance": 300,
            "daylight": 0,
            # Class: CfgVehicles|rhsusf_CH53E_USMC|Reflectors|Left|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 0,
                "hardlimitstart": 200,
                "hardlimitend": 250
            }
        }
    },
    # Class: CfgVehicles|rhsusf_CH53E_USMC|Exhausts [Indent level: 1],
    "exhausts": {
        # Class: CfgVehicles|rhsusf_CH53E_USMC|Exhausts|Exhaust1 [Indent level: 2]
        "exhaust1": {
            "position": "exhaust_1_pos",
            "direction": "exhaust_1_dir",
            "effect": "ExhaustsEffectHeliBig"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|Exhausts|Exhaust2 [Indent level: 2],
        "exhaust2": {
            "position": "exhaust_2_pos",
            "direction": "exhaust_2_dir",
            "effect": "ExhaustsEffectHeliBig"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|Exhausts|Exhaust3 [Indent level: 2],
        "exhaust3": {
            "position": "exhaust_3_pos",
            "direction": "exhaust_3_dir",
            "effect": "ExhaustsEffectHeliBig"
        }
    },
    "simulation": "helicopterrtd",
    # Class: CfgVehicles|rhsusf_CH53E_USMC|RotorLibHelicopterProperties [Indent level: 1],
    "rotorlibhelicopterproperties": {
        "rtdconfig": "rhsusf|addons|rhsusf_c_ch53|RTD_CH53E2.xml",
        "autohovercorrection": [4.7,3.8,0],
        "defaultcollective": 0.665,
        "retreatbladestallwarningspeed": 87.4556,
        "maxtorque": 4900,
        "stressdamagepersec": 0.00333333,
        "maxhorizontalstabilizerleftstress": 10000,
        "maxhorizontalstabilizerrightstress": 10000,
        "maxverticalstabilizerstress": 10000,
        "horizontalwingsanglecollmin": 0,
        "horizontalwingsanglecollmax": 0,
        "maxmainrotorstress": 570000,
        "maxtailrotorstress": 120000,
        "rtd_center": "rtd_center",
        "hasapu": 0,
        "vrsshakepowercoef": 1
    },
    # Class: CfgVehicles|rhsusf_CH53E_USMC|Eventhandlers [Indent level: 1],
    "eventhandlers": {
        # Class: CfgVehicles|rhsusf_CH53E_USMC|Eventhandlers|RHSUSF_EventHandlers [Indent level: 2]
        "rhsusf_eventhandlers": {
            "init": "_this call rhsusf_fnc_ch53_init"
        },
        "fired": "",
        "init": "",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');"
    },
    "weapons": ["rhsusf_weap_ANAAQ24"],
    "magazines": ["rhsusf_mag_DIRCM","rhsusf_mag_DIRCM","rhsusf_mag_DIRCM","rhsusf_mag_DIRCM","rhsusf_mag_DIRCM","rhsusf_mag_DIRCM","rhsusf_mag_DIRCM","rhsusf_mag_DIRCM","rhsusf_mag_DIRCM","rhsusf_mag_DIRCM"],
    "numberphysicalwheels": 3,
    "unitinfotype": "RHSUSF_RscUnitInfoAir",
    "unitinfotypertd": "RscUnitInfoAirRTDFullDigital",
    # Class: CfgVehicles|rhsusf_CH53E_USMC|Components [Indent level: 1],
    "components": {
        # Class: CfgVehicles|rhsusf_CH53E_USMC|Components|TransportPylonsComponent [Indent level: 2]
        "transportpylonscomponent": {
            "uipicture": "rhsusf|addons|rhsusf_ch53|data|loadouts|RHS_CH53_EDEN_CA.paa",
            # Class: CfgVehicles|rhsusf_CH53E_USMC|Components|TransportPylonsComponent|pylons [Indent level: 3],
            "pylons": {
                # Class: CfgVehicles|rhsusf_CH53E_USMC|Components|TransportPylonsComponent|pylons|cmDispenser [Indent level: 4]
                "cmdispenser": {
                    "hardpoints": ["RHSUSF_cm_ANALE39","RHSUSF_cm_ANALE39_x2"],
                    "priority": 1,
                    "attachment": "rhsusf_ANALE39_CMFlare_Chaff_Magazine_x2",
                    "maxweight": 800,
                    "uiposition": [0.33,0]
                }
            }
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|Components|SensorsManagerComponent [Indent level: 2],
        "sensorsmanagercomponent": {
            # Class: CfgVehicles|rhsusf_CH53E_USMC|Components|SensorsManagerComponent|Components [Indent level: 3]
            "components": {
                # Class: CfgVehicles|rhsusf_CH53E_USMC|Components|SensorsManagerComponent|Components|IRSensorComponent [Indent level: 4]
                "irsensorcomponent": {
                    # Class: CfgVehicles|rhsusf_CH53E_USMC|Components|SensorsManagerComponent|Components|IRSensorComponent|AirTarget [Indent level: 5]
                    "airtarget": {
                        "minrange": 500,
                        "maxrange": 7000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": 1
                    },
                    # Class: CfgVehicles|rhsusf_CH53E_USMC|Components|SensorsManagerComponent|Components|IRSensorComponent|GroundTarget [Indent level: 5],
                    "groundtarget": {
                        "minrange": 500,
                        "maxrange": 7000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": 1
                    },
                    "animdirection": "ObsGun",
                    "anglerangehorizontal": 98,
                    "anglerangevertical": 72,
                    "typerecognitiondistance": -1,
                    "minspeedthreshold": 0,
                    "maxspeedthreshold": 0,
                    "maxfogseethrough": 0.95,
                    "mintrackablespeed": 0,
                    "maxtrackablespeed": 695,
                    "componenttype": "IRSensorComponent",
                    "color": [1,0,0,1],
                    "allowsmarking": 1,
                    "groundnoisedistancecoef": -1,
                    "maxgroundnoisedistance": -1,
                    "aimdown": 0,
                    "mintrackableatl": -1e+010,
                    "maxtrackableatl": 1e+010
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|Components|SensorsManagerComponent|Components|VisualSensorComponent [Indent level: 4],
                "visualsensorcomponent": {
                    # Class: CfgVehicles|rhsusf_CH53E_USMC|Components|SensorsManagerComponent|Components|VisualSensorComponent|AirTarget [Indent level: 5]
                    "airtarget": {
                        "minrange": 500,
                        "maxrange": 4000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": 1
                    },
                    # Class: CfgVehicles|rhsusf_CH53E_USMC|Components|SensorsManagerComponent|Components|VisualSensorComponent|GroundTarget [Indent level: 5],
                    "groundtarget": {
                        "minrange": 500,
                        "maxrange": 4000,
                        "objectdistancelimitcoef": 1,
                        "viewdistancelimitcoef": 1
                    },
                    "maxtrackablespeed": 70,
                    "animdirection": "ObsGun",
                    "anglerangehorizontal": 98,
                    "anglerangevertical": 72,
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
                    "aimdown": 0,
                    "mintrackablespeed": -1e+010,
                    "mintrackableatl": -1e+010,
                    "maxtrackableatl": 1e+010
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|Components|SensorsManagerComponent|Components|LaserSensorComponent [Indent level: 4],
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
                # Class: CfgVehicles|rhsusf_CH53E_USMC|Components|SensorsManagerComponent|Components|PassiveRadarSensorComponent [Indent level: 4],
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
        # Class: CfgVehicles|rhsusf_CH53E_USMC|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 2],
        "vehiclesystemsdisplaymanagercomponentleft": {
            # Class: CfgVehicles|rhsusf_CH53E_USMC|Components|VehicleSystemsDisplayManagerComponentLeft|Components [Indent level: 3]
            "components": {
                # Class: CfgVehicles|rhsusf_CH53E_USMC|Components|VehicleSystemsDisplayManagerComponentLeft|Components|EmptyDisplay [Indent level: 4]
                "emptydisplay": {
                    "componenttype": "EmptyDisplayComponent"
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|Components|VehicleSystemsDisplayManagerComponentLeft|Components|MinimapDisplay [Indent level: 4],
                "minimapdisplay": {
                    "componenttype": "MinimapDisplayComponent",
                    "resource": "RscCustomInfoMiniMap"
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|Components|VehicleSystemsDisplayManagerComponentLeft|Components|CrewDisplay [Indent level: 4],
                "crewdisplay": {
                    "componenttype": "CrewDisplayComponent",
                    "resource": "RscCustomInfoCrew"
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|Components|VehicleSystemsDisplayManagerComponentLeft|Components|SlingLoadDisplay [Indent level: 4],
                "slingloaddisplay": {
                    "componenttype": "SlingLoadDisplayComponent",
                    "resource": "RscCustomInfoSlingLoad"
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|Components|VehicleSystemsDisplayManagerComponentLeft|Components|SensorDisplay [Indent level: 4],
                "sensordisplay": {
                    "componenttype": "SensorsDisplayComponent",
                    "resource": "RscCustomInfoSensors",
                    "range": [3000,8000,16000,35000]
                },
                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|MineDetectorDisplay [Indent level: 1],
                "minedetectordisplay": {
                    "componenttype": "MineDetectorDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|UAVDisplay [Indent level: 1],
                "uavdisplay": {
                    "componenttype": "UAVFeedDisplayComponent"
                }
            },
            "componenttype": "VehicleSystemsDisplayManager",
            "left": 1,
            "defaultdisplay": "EmptyDisplay",
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,	(safezoneX + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 2],
        "vehiclesystemsdisplaymanagercomponentright": {
            "defaultdisplay": "SensorDisplay",
            # Class: CfgVehicles|rhsusf_CH53E_USMC|Components|VehicleSystemsDisplayManagerComponentRight|Components [Indent level: 3],
            "components": {
                # Class: CfgVehicles|rhsusf_CH53E_USMC|Components|VehicleSystemsDisplayManagerComponentRight|Components|EmptyDisplay [Indent level: 4]
                "emptydisplay": {
                    "componenttype": "EmptyDisplayComponent"
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|Components|VehicleSystemsDisplayManagerComponentRight|Components|MinimapDisplay [Indent level: 4],
                "minimapdisplay": {
                    "componenttype": "MinimapDisplayComponent",
                    "resource": "RscCustomInfoMiniMap"
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|Components|VehicleSystemsDisplayManagerComponentRight|Components|CrewDisplay [Indent level: 4],
                "crewdisplay": {
                    "componenttype": "CrewDisplayComponent",
                    "resource": "RscCustomInfoCrew"
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|Components|VehicleSystemsDisplayManagerComponentRight|Components|SlingLoadDisplay [Indent level: 4],
                "slingloaddisplay": {
                    "componenttype": "SlingLoadDisplayComponent",
                    "resource": "RscCustomInfoSlingLoad"
                },
                # Class: CfgVehicles|rhsusf_CH53E_USMC|Components|VehicleSystemsDisplayManagerComponentRight|Components|SensorDisplay [Indent level: 4],
                "sensordisplay": {
                    "componenttype": "SensorsDisplayComponent",
                    "resource": "RscCustomInfoSensors",
                    "range": [3000,8000,16000,35000]
                },
                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|MineDetectorDisplay [Indent level: 1],
                "minedetectordisplay": {
                    "componenttype": "MineDetectorDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|UAVDisplay [Indent level: 1],
                "uavdisplay": {
                    "componenttype": "UAVFeedDisplayComponent"
                }
            },
            "componenttype": "VehicleSystemsDisplayManager",
            "right": 1,
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,	((safezoneX + safezoneW) - (		(10 * 			(			((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40)))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|Components|TransportCountermeasuresComponent [Indent level: 2],
        "transportcountermeasurescomponent": {
        }
    },
    "cargocompartments": ["Compartment2"],
    # Class: CfgVehicles|rhsusf_CH53E_USMC|pilotCamera [Indent level: 1],
    "pilotcamera": {
        # Class: CfgVehicles|rhsusf_CH53E_USMC|pilotCamera|OpticsIn [Indent level: 2]
        "opticsin": {
            # Class: CfgVehicles|rhsusf_CH53E_USMC|pilotCamera|OpticsIn|Wide [Indent level: 3]
            "wide": {
                "opticsdisplayname": "W",
                "initanglex": 0,
                "minanglex": 0,
                "maxanglex": 0,
                "initangley": 0,
                "minangley": 0,
                "maxangley": 0,
                "initfov": 0.5,
                "minfov": 0.5,
                "maxfov": 0.5,
                "directionstabilized": 1,
                "visionmode": ["Normal","NVG"],
                "thermalmode": [0,1],
                "gunneropticsmodel": "A3|drones_f|Weapons_F_Gamma|Reticle|UAV_Optics_Gunner_wide_F.p3d"
            },
            "showminimapinoptics": 0,
            "showuavviewpinoptics": 0,
            "showslingloadmanagerinoptics": 1
        },
        "minturn": 0,
        "maxturn": 0,
        "initturn": 0,
        "minelev": 80,
        "maxelev": 80,
        "initelev": 80,
        "maxxrotspeed": 0.5,
        "maxyrotspeed": 0.5,
        "pilotopticsshowcursor": 1,
        "controllable": 0
    },
    "memorypointdriveroptics": "slingCamera",
    "slingloadmaxcargomass": 14000,
    # Class: CfgVehicles|rhsusf_CH53E_USMC|MarkerLights [Indent level: 1],
    "markerlights": {
        # Class: CfgVehicles|rhsusf_CH53E_USMC|MarkerLights|PositionRed [Indent level: 2]
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
            # Class: CfgVehicles|rhsusf_CH53E_USMC|MarkerLights|PositionRed|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardlimitstart": 0.75,
                "hardlimitend": 1
            }
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|MarkerLights|PositionGreen [Indent level: 2],
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
            # Class: CfgVehicles|rhsusf_CH53E_USMC|MarkerLights|PositionRed|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardlimitstart": 0.75,
                "hardlimitend": 1
            }
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|MarkerLights|PositionWhite [Indent level: 2],
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
            # Class: CfgVehicles|rhsusf_CH53E_USMC|MarkerLights|PositionRed|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardlimitstart": 0.75,
                "hardlimitend": 1
            }
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|MarkerLights|CollisionRed [Indent level: 2],
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
            # Class: CfgVehicles|rhsusf_CH53E_USMC|MarkerLights|PositionRed|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardlimitstart": 0.75,
                "hardlimitend": 1
            }
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|MarkerLights|CollisionWhite [Indent level: 2],
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
            # Class: CfgVehicles|rhsusf_CH53E_USMC|MarkerLights|PositionRed|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardlimitstart": 0.75,
                "hardlimitend": 1
            }
        },
        # Class: CfgVehicles|rhsusf_CH53E_USMC|MarkerLights|InteriorBlue [Indent level: 2],
        "interiorblue": {
            "name": "light_interior_blue",
            "color": [0.07,0.99,0.89],
            "ambient": [0.007,0.099,0.089],
            "intensity": 75,
            "blinking": 0,
            "drawlightsize": 0.25,
            "drawlightcentersize": 0.08,
            # Class: CfgVehicles|rhsusf_CH53E_USMC|MarkerLights|InteriorBlue|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardlimitstart": 2.25,
                "hardlimitend": 3
            }
        }
    },
    "ace_cargo_hascargo": 1,
    "ace_cargo_space": 16,
    # Class: CfgVehicles|rhsusf_CH53E_USMC|VehicleTransport [Indent level: 1],
    "vehicletransport": {
        # Class: CfgVehicles|rhsusf_CH53E_USMC|VehicleTransport|Carrier [Indent level: 2]
        "carrier": {
            "cargobaydimensions": ["VTV_limit_1","VTV_limit_2"],
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
    "_generalmacro": "Helicopter_Base_H",
    "irscanrangemin": 0,
    "irscanrangemax": 0,
    "irscantoeyefactor": 1,
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
    "transportmaxbackpacks": 24,
    "supplyradius": -1,
    "memorypointsupply": "doplnovani",
    # Class: CfgVehicles|Helicopter_Base_H|TransportBackpacks [Indent level: 1],
    "transportbackpacks": {
    },
    # Class: CfgVehicles|Helicopter_Base_H|TransportMagazines [Indent level: 1],
    "transportmagazines": {
    },
    # Class: CfgVehicles|Helicopter_Base_H|TransportWeapons [Indent level: 1],
    "transportweapons": {
    },
    # Class: CfgVehicles|Helicopter_Base_H|TransportItems [Indent level: 1],
    "transportitems": {
        # Class: CfgVehicles|Helicopter_Base_H|TransportItems|_xx_FirstAidKit [Indent level: 2]
        "_xx_firstaidkit": {
            "name": "FirstAidKit",
            "count": 4
        },
        # Class: CfgVehicles|Helicopter_Base_H|TransportItems|_xx_Toolkit [Indent level: 2],
        "_xx_toolkit": {
            "name": "Toolkit",
            "count": 1
        },
        # Class: CfgVehicles|Helicopter_Base_H|TransportItems|_xx_ItemGPS [Indent level: 2],
        "_xx_itemgps": {
            "name": "ItemGPS",
            "count": 1
        },
        # Class: CfgVehicles|Helicopter_Base_H|TransportItems|_xx_ItemRadio [Indent level: 2],
        "_xx_itemradio": {
            "name": "ItemRadio",
            "count": 1
        }
    },
    "drivercansee": "1 + 2 + 4 + 8 + 32",
    "gunnercansee": "1 + 2 + 4 + 8 + 32",
    "commandercansee": "1 + 2 + 4 + 8 + 32",
    "washdownstrength": "1.0f",
    "washdowndiameter": "40.0f",
    "minsmokedamage": 0.3,
    "maxsmokedamage": 0.99,
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
    "unitinfotypelite": "RscUnitInfoAirRTDBasic",
    "dusteffect": "HeliDust",
    "watereffect": "HeliWater",
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
    "mainrotorspeed": 1,
    "backrotorspeed": 1.5,
    "startduration": 20,
    "maxmainrotordive": 0,
    "maxbackrotordive": 0,
    "minmainrotordive": 0,
    "minbackrotordive": 0,
    "neutralbackrotordive": 0,
    "neutralmainrotordive": 0,
    "memorypointlmissile": "L strela",
    "memorypointrmissile": "P strela",
    "memorypointlrocket": "L raketa",
    "memorypointrrocket": "P raketa",
    "memorypointgun": "",
    "memorypointpilot": "pilot",
    "_mainbladecenter": "rotor_center",
    "selectionfireanim": "zasleh",
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
    "editorsubcategory": "EdSubcat_Helicopters",
    "extcameraparams": [-1],
    "textsingular": "helicopter",
    "textplural": "helicopters",
    "namesound": "veh_air_helicopter_s",
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
    "altfullforce": 2000,
    "altnoforce": 6000,
    "outsidesoundfilter": 1,
    "nightvision": 0,
    "drivercompartments": 0,
    "getinradius": 5,
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
    "waterresistance": 1,
    "impacteffectssea": "ImpactEffectsAir",
    "flarevelocity": 100,
    "enableradio": 1,
    "memorypointcm": ["flare_launcher1","flare_launcher2"],
    "memorypointcmdir": ["flare_launcher1_dir","flare_launcher2_dir"],
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
    "memorypointsgetincargo": "pos cargo",
    "memorypointsgetincargodir": "pos cargo dir",
    "memorypointsgetincodriver": "pos codriver",
    "memorypointsgetincodriverdir": "pos codriver dir",
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
    "enablemanualfire": 1,
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
    "cargoiscodriver": [0],
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