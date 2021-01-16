rhs_su25_vvs_base = {
    "editorpreview": "rhsafrf|addons|rhs_editorPreviews|data|rhs_Su25_VVS_Base.paa",
    "accuracy": 0.5,
    "side": 0,
    "faction": "rhs_faction_vvs_c",
    "vehicleclass": "rhs_vehclass_aircraft",
    "dlc": "RHS_AFRF",
    "rhs_decalparameters": ["['Number',cRHSAIRSU25NumberPlaces,'AviaRed']","['Label', cRHSAIRSU25NosePlaces, 'Su25NoseArt']","['Label', cRHSAIRSU25SidePlaces, 'Su25Ex']"],
    "irtarget": 1,
    "irtargetsize": 1,
    "visualtarget": 1,
    "visualtargetsize": 0.9,
    "radartarget": 1,
    "radartargetsize": 1,
    "lesh_canbetowed": 1,
    "lesh_towfromfront": 1,
    "lesh_axisoffsettarget": [0,6.8,-2.04],
    "lesh_wheeloffset": [0,-0.7],
    "category": "Air",
    "crew": "rhs_pilot",
    "typicalcargo": ["rhs_pilot"],
    "scope": 0,
    "availableforsupporttypes": ["CAS_Bombing"],
    "model": "rhsafrf|addons|rhs_a2port_air|su25|su25",
    "picture": "rhsafrf|addons|rhs_a2port_air|data|ico|rhs_su25sm_pic_ca.paa",
    "icon": "rhsafrf|addons|rhs_a2port_air|data|map_ico|icomap_su25.paa",
    "mapsize": 20,
    "textsingular": "Su25",
    "displayname": "Su-25",
    "driveraction": "rhs_su25_pilot",
    "driverlefthandanimname": "lever_pilot",
    "driverrighthandanimname": "stick_pilot",
    "driverleftleganimname": "pedal_L",
    "driverrightleganimname": "pedal_R",
    "memorypointsgetindriver": "pos driver",
    "memorypointsgetindriverdir": "pos driver dir",
    "memorypointsgetindriverprecise": "pos driver",
    "unitinfotype": "RHS_RscUnitInfoAir_Su25",
    "driverweaponsinfotype": "RHS_RscOptics_Su25_KlenPS",
    "headaimdown": 6,
    "headgforceleaningfactor": [0.005,0.001,0.015],
    "camshakecoef": 0.7,
    "drivercansee": "2+4+8+16",
    "allowtablock": 0,
    "drivercaneject": 1,
    "drivercompartments": 1,
    # Class: CfgVehicles|RHS_su25_base|EjectionSystem [Indent level: 1],
    "ejectionsystem": {
    },
    "ejectdamagelimit": 1,
    "memorypointdriveroptics": "pilotCamera",
    # Class: CfgVehicles|RHS_su25_base|PilotCamera [Indent level: 1],
    "pilotcamera": {
        # Class: CfgVehicles|RHS_su25_base|PilotCamera|OpticsIn [Indent level: 2]
        "opticsin": {
            # Class: CfgVehicles|RHS_su25_base|PilotCamera|OpticsIn|Wide [Indent level: 3]
            "wide": {
                "opticsdisplayname": "WFOV",
                "initanglex": 0,
                "minanglex": 0,
                "maxanglex": 0,
                "initangley": 0,
                "minangley": 0,
                "maxangley": 0,
                "initfov": "(10 / 120)",
                "minfov": "(60 / 120)",
                "maxfov": "(60 / 120)",
                "directionstabilized": 1,
                "visionmode": ["Normal"],
                "gunneropticsmodel": "",
                "opticsppeffects": ["OpticsCHAbera2","OpticsBlur2"]
            }
        },
        "minturn": -12,
        "maxturn": 12,
        "initturn": 0,
        "minelev": -6,
        "maxelev": 16,
        "initelev": 0,
        "maxxrotspeed": 1,
        "maxyrotspeed": 1,
        "maxmousexrotspeed": 0.5,
        "maxmouseyrotspeed": 0.5,
        "pilotopticsshowcursor": 1,
        "controllable": 1
    },
    # Class: CfgVehicles|RHS_su25_base|ViewPilot [Indent level: 1],
    "viewpilot": {
        "initanglex": -0,
        "initfov": 0.75,
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
    "weapons": ["rhs_weap_MASTERSAFE","rhs_weap_klen_ps","rhs_weap_GSh302"],
    "magazines": ["rhs_lasermag","rhs_mag_gsh30_bt_250"],
    "weaponsgroup1": 128,
    "weaponsgroup4": 64,
    "memorypointgun": ["kulomet","kulomet2"],
    "gunbeg": ["muzzle_1","muzzle_2"],
    "gunend": ["chamber_1","chamber_2"],
    "selectionfireanim": "zasleh",
    "memorypointldust": "levy prach",
    "memorypointrdust": "pravy prach",
    "memorypointlrocket": "rocket_1",
    "memorypointrrocket": "rocket_2",
    "memorypointlmissile": "missile_1",
    "memorypointrmissile": "missile_2",
    "memorypointcm": ["flare_launcher1","flare_launcher2"],
    "memorypointcmdir": ["flare_launcher1_dir","flare_launcher2_dir"],
    "selectiondamage": "trup",
    "selectionshowdamage": "poskozeni",
    "armor": 60,
    "damageresistance": 0.0048,
    "armorstructural": 2,
    "epeimpulsedamagecoef": 1,
    # Class: CfgVehicles|RHS_su25_base|Hitpoints [Indent level: 1],
    "hitpoints": {
        # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitHull [Indent level: 2]
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
        # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitAvionics [Indent level: 2],
        "hitavionics": {
            "armor": 1,
            "explosionshielding": 0.6,
            "passthrough": 0.05,
            "minimalhit": 0.1,
            "radius": 0.08,
            "material": -1,
            "name": "hit_avionics",
            "visual": "vis_avionics",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitEngine [Indent level: 2],
        "hitengine": {
            "armor": 1,
            "explosionshielding": 0.25,
            "passthrough": 0.2,
            "minimalhit": 0.01,
            "radius": 0.07,
            "material": -1,
            "name": "hit_engine_l",
            "visual": "vis_engine_l",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitEngine2 [Indent level: 2],
        "hitengine2": {
            "armor": 1,
            "explosionshielding": 0.25,
            "passthrough": 0.2,
            "minimalhit": 0.01,
            "radius": 0.07,
            "material": -1,
            "name": "hit_engine_r",
            "visual": "vis_engine_r",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitFuel [Indent level: 2],
        "hitfuel": {
            "armor": 1.4,
            "explosionshielding": 0.2,
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "radius": 0.1,
            "material": -1,
            "name": "hit_fuel",
            "visual": "vis_fuel",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitFuel_left [Indent level: 2],
        "hitfuel_left": {
            "armor": 1,
            "explosionshielding": 0.6,
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "radius": 0.1,
            "material": -1,
            "name": "hit_fuel_wing_l",
            "visual": "vis_wing_l",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitFuel_right [Indent level: 2],
        "hitfuel_right": {
            "armor": 1,
            "explosionshielding": 0.6,
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "radius": 0.1,
            "material": -1,
            "name": "hit_fuel_wing_r",
            "visual": "vis_wing_r",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitFuel2 [Indent level: 2],
        "hitfuel2": {
            "armor": 999,
            "explosionshielding": 0,
            "passthrough": 0.1,
            "minimalhit": 1,
            "radius": 0.01,
            "material": -1,
            "name": "hit_fuel",
            "visual": "ind_fuel_r",
            "depends": "(HitFuel_left+HitFuel_right)*0.5"
        },
        # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitLAileron_link [Indent level: 2],
        "hitlaileron_link": {
            "armor": 0.6,
            "explosionshielding": 0.6,
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "radius": 0.12,
            "material": -1,
            "name": "hit_aileron_link_l",
            "visual": "-",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitRAileron_link [Indent level: 2],
        "hitraileron_link": {
            "armor": 0.6,
            "explosionshielding": 0.6,
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "radius": 0.12,
            "material": -1,
            "name": "hit_aileron_link_r",
            "visual": "-",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitLAileron [Indent level: 2],
        "hitlaileron": {
            "armor": 0.6,
            "explosionshielding": 0.5,
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "radius": 0.13,
            "material": -1,
            "name": "hit_aileron_l",
            "visual": "vis_wing_l",
            "depends": "HitLAileron_link*0.7"
        },
        # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitRAileron [Indent level: 2],
        "hitraileron": {
            "armor": 0.6,
            "explosionshielding": 0.5,
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "radius": 0.13,
            "material": -1,
            "name": "hit_aileron_r",
            "visual": "vis_wing_r",
            "depends": "HitRAileron_link*0.7"
        },
        # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitControlRear [Indent level: 2],
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
        # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitLCElevator [Indent level: 2],
        "hitlcelevator": {
            "armor": 0.6,
            "explosionshielding": 0.6,
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "radius": 0.12,
            "material": -1,
            "name": "hit_elevator_l",
            "visual": "vis_elevator_l",
            "depends": "HitControlRear"
        },
        # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitRElevator [Indent level: 2],
        "hitrelevator": {
            "armor": 0.6,
            "explosionshielding": 0.6,
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "radius": 0.12,
            "material": -1,
            "name": "hit_elevator_r",
            "visual": "vis_elevator_r",
            "depends": "HitControlRear"
        },
        # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitLCRudder [Indent level: 2],
        "hitlcrudder": {
            "armor": 0.6,
            "explosionshielding": 0.6,
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "radius": 0.12,
            "material": -1,
            "name": "hit_rudder",
            "visual": "vis_rudder",
            "depends": "HitControlRear"
        },
        # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitGlass1 [Indent level: 2],
        "hitglass1": {
            "armor": 0.5,
            "explosionshielding": 0.6,
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "radius": 0.3,
            "material": -1,
            "name": "glass1",
            "visual": "glass1",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitGlass2 [Indent level: 2],
        "hitglass2": {
            "armor": 0.5,
            "explosionshielding": 0.6,
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "radius": 0.3,
            "material": -1,
            "name": "glass2",
            "visual": "glass2",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_su25_base|Hitpoints|Ind_Fire1 [Indent level: 2],
        "ind_fire1": {
            "armor": 999,
            "explosionshielding": 0,
            "passthrough": 0,
            "minimalhit": 1,
            "radius": 0.01,
            "material": -1,
            "name": "hit_fuel",
            "visual": "ind_fire",
            "depends": "HitEngine*0.5"
        },
        # Class: CfgVehicles|RHS_su25_base|Hitpoints|Ind_Fire2 [Indent level: 2],
        "ind_fire2": {
            "armor": 999,
            "explosionshielding": 0,
            "passthrough": 0,
            "minimalhit": 1,
            "radius": 0.01,
            "material": -1,
            "name": "hit_fuel",
            "visual": "ind_fire",
            "depends": "HitEngine2*0.5"
        },
        # Class: CfgVehicles|RHS_su25_base|Hitpoints|Ind_Hydr_L [Indent level: 2],
        "ind_hydr_l": {
            "armor": 999,
            "explosionshielding": 0,
            "passthrough": 0,
            "minimalhit": 1,
            "radius": 0.01,
            "material": -1,
            "name": "hit_fuel",
            "visual": "ind_hydr_l",
            "depends": "(HitLAileron+HitLCElevator+HitLCRudder)*0.5"
        },
        # Class: CfgVehicles|RHS_su25_base|Hitpoints|Ind_Hydr_R [Indent level: 2],
        "ind_hydr_r": {
            "armor": 999,
            "explosionshielding": 0,
            "passthrough": 0,
            "minimalhit": 1,
            "radius": 0.01,
            "material": -1,
            "name": "hit_fuel",
            "visual": "ind_hydr_r",
            "depends": "(HitRAileron+HitRElevator)*0.5"
        },
        # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon1 [Indent level: 2],
        "hitpylon1": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_1",
            "passthrough": 0,
            "minimalhit": -0.1,
            "explosionshielding": 0.1,
            "radius": 0.75,
            "visual": "-",
            # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon1|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon1|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "rhs_pylon_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon1|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "rhs_pylon_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_1",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon1|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "rhs_pylon_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_1",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon1|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
                "rhs_pylon_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_1",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon2 [Indent level: 2],
        "hitpylon2": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_2",
            "passthrough": 0,
            "minimalhit": -0.1,
            "explosionshielding": 0.1,
            "radius": 0.75,
            "visual": "-",
            # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon2|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon2|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "rhs_pylon_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_2",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon2|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "rhs_pylon_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_2",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon2|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "rhs_pylon_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_2",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon2|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
                "rhs_pylon_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_2",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon3 [Indent level: 2],
        "hitpylon3": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_3",
            "passthrough": 0,
            "minimalhit": -0.1,
            "explosionshielding": 0.1,
            "radius": 0.75,
            "visual": "-",
            # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon3|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon3|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "rhs_pylon_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_3",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon3|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "rhs_pylon_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_3",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon3|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "rhs_pylon_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_3",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon3|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
                "rhs_pylon_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_3",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon4 [Indent level: 2],
        "hitpylon4": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_4",
            "passthrough": 0,
            "minimalhit": -0.1,
            "explosionshielding": 0.1,
            "radius": 0.75,
            "visual": "-",
            # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon4|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon4|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "rhs_pylon_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_4",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon4|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "rhs_pylon_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_4",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon4|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "rhs_pylon_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_4",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon4|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
                "rhs_pylon_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_4",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon5 [Indent level: 2],
        "hitpylon5": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_5",
            "passthrough": 0,
            "minimalhit": -0.1,
            "explosionshielding": 0.1,
            "radius": 0.75,
            "visual": "-",
            # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon5|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon5|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "rhs_pylon_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_5",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon5|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "rhs_pylon_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_5",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon5|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "rhs_pylon_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_5",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon5|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
                "rhs_pylon_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_5",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon6 [Indent level: 2],
        "hitpylon6": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_6",
            "passthrough": 0,
            "minimalhit": -0.1,
            "explosionshielding": 0.1,
            "radius": 0.75,
            "visual": "-",
            # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon6|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon6|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "rhs_pylon_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_6",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon6|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "rhs_pylon_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_6",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon6|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "rhs_pylon_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_6",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon6|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
                "rhs_pylon_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_6",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon7 [Indent level: 2],
        "hitpylon7": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_7",
            "passthrough": 0,
            "minimalhit": -0.1,
            "explosionshielding": 0.1,
            "radius": 0.75,
            "visual": "-",
            # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon7|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon7|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "rhs_pylon_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_7",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon7|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "rhs_pylon_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_7",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon7|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "rhs_pylon_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_7",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon7|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
                "rhs_pylon_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_7",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon8 [Indent level: 2],
        "hitpylon8": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_8",
            "passthrough": 0,
            "minimalhit": -0.1,
            "explosionshielding": 0.1,
            "radius": 0.75,
            "visual": "-",
            # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon8|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon8|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "rhs_pylon_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_8",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon8|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "rhs_pylon_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_8",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon8|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "rhs_pylon_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_8",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon8|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
                "rhs_pylon_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_8",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon9 [Indent level: 2],
        "hitpylon9": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_9",
            "passthrough": 0,
            "minimalhit": -0.1,
            "explosionshielding": 0.1,
            "radius": 0.75,
            "visual": "-",
            # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon9|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon9|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "rhs_pylon_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_9",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon9|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "rhs_pylon_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_9",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon9|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "rhs_pylon_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_9",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon9|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
                "rhs_pylon_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_9",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon10 [Indent level: 2],
        "hitpylon10": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_10",
            "passthrough": 0,
            "minimalhit": -0.1,
            "explosionshielding": 0.1,
            "radius": 0.75,
            "visual": "-",
            # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon10|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon10|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "rhs_pylon_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_10",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon10|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "rhs_pylon_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_10",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon10|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "rhs_pylon_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_10",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_su25_base|Hitpoints|HitPylon10|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
                "rhs_pylon_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_10",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        }
    },
    "incomingmissiledetectionsystem": 8,
    "lockdetectionsystem": 8,
    "hiddenselections": ["camo1","camo2","n1","n2","i1","i2","tail_decals"],
    "hiddenselectionstextures": ["|rhsafrf|addons|rhs_a2port_air|su25|data|su25_body1_rus_co.paa","|rhsafrf|addons|rhs_a2port_air|su25|data|su25_body2_rus_co.paa","a3|data_f|clear_empty.paa","a3|data_f|clear_empty.paa","a3|data_f|clear_empty.paa","a3|data_f|clear_empty.paa","rhsafrf|addons|rhs_decals|data|labels|aviation|vvs_ca.paa"],
    # Class: CfgVehicles|RHS_su25_base|textureSources [Indent level: 1],
    "texturesources": {
        # Class: CfgVehicles|RHS_su25_base|textureSources|standard [Indent level: 2]
        "standard": {
            "displayname": "Blue",
            "author": "Red Hammer Studios",
            "textures": ["|rhsafrf|addons|rhs_a2port_air|su25|data|su25_body1_alt_co.paa","|rhsafrf|addons|rhs_a2port_air|su25|data|su25_body2_alt_co.paa"],
            "factions": ["rhs_faction_vvs"]
        },
        # Class: CfgVehicles|RHS_su25_base|textureSources|standard2 [Indent level: 2],
        "standard2": {
            "displayname": "Grey",
            "author": "Red Hammer Studios",
            "textures": ["|rhsafrf|addons|rhs_a2port_air|su25|data|su25_body1_co.paa","|rhsafrf|addons|rhs_a2port_air|su25|data|su25_body2_co.paa"],
            "factions": ["rhs_faction_vvs"]
        },
        # Class: CfgVehicles|RHS_su25_base|textureSources|Camo [Indent level: 2],
        "camo": {
            "displayname": "Camo #1",
            "author": "Red Hammer Studios",
            "textures": ["|rhsafrf|addons|rhs_a2port_air|su25|data|su25_body1_rus_co.paa","|rhsafrf|addons|rhs_a2port_air|su25|data|su25_body2_rus_co.paa"],
            "factions": ["rhs_faction_vvs_c"]
        },
        # Class: CfgVehicles|RHS_su25_base|textureSources|Camo1 [Indent level: 2],
        "camo1": {
            "displayname": "Camo #2",
            "author": "Red Hammer Studios",
            "textures": ["|rhsafrf|addons|rhs_a2port_air|su25|data|camo|su25_body1_camo1_co.paa","|rhsafrf|addons|rhs_a2port_air|su25|data|camo|su25_body2_camo1_co.paa"],
            "factions": ["rhs_faction_vvs_c"]
        },
        # Class: CfgVehicles|RHS_su25_base|textureSources|Camo2 [Indent level: 2],
        "camo2": {
            "displayname": "CDF",
            "author": "Red Hammer Studios",
            "textures": ["|rhsafrf|addons|rhs_a2port_air|su25|data|su25_body1_cdf_co.paa","|rhsafrf|addons|rhs_a2port_air|su25|data|su25_body2_cdf_co.paa"],
            "factions": ["rhs_faction_vvs"]
        }
    },
    "texturelist": [],
    # Class: CfgVehicles|RHS_su25_base|Components [Indent level: 1],
    "components": {
        # Class: CfgVehicles|RHS_su25_base|Components|TransportPylonsComponent [Indent level: 2]
        "transportpylonscomponent": {
            "uipicture": "rhsafrf|addons|rhs_a2port_air|data|loadouts|RHS_Su25_EDEN_CA.paa",
            # Class: CfgVehicles|RHS_su25_base|Components|TransportPylonsComponent|pylons [Indent level: 3],
            "pylons": {
                # Class: CfgVehicles|RHS_su25_base|Components|TransportPylonsComponent|pylons|pylon1 [Indent level: 4]
                "pylon1": {
                    "hardpoints": ["RHS_HP_KH29","RHS_HP_FAB100","RHS_HP_FAB100_MBD3_U4T","RHS_HP_FAB100_MBD3_U6","RHS_HP_FAB250","RHS_HP_FAB500","RHS_HP_KMGU2","RHS_HP_O25L","RHS_HP_APU68M3_S24","RHS_HP_B13L","RHS_HP_B8M1","RHS_HP_UB16","RHS_HP_UB32","RHS_HP_R73"],
                    "priority": 9,
                    "attachment": "rhs_mag_fab250",
                    "hitpoint": "HitPylon1",
                    "maxweight": 1200,
                    "uiposition": [0.32,0.35]
                },
                # Class: CfgVehicles|RHS_su25_base|Components|TransportPylonsComponent|pylons|pylon2 [Indent level: 4],
                "pylon2": {
                    "uiposition": [0.32,0.2],
                    "mirroredmissilepos": 1,
                    "hitpoint": "HitPylon2",
                    "hardpoints": ["RHS_HP_KH29","RHS_HP_FAB100","RHS_HP_FAB100_MBD3_U4T","RHS_HP_FAB100_MBD3_U6","RHS_HP_FAB250","RHS_HP_FAB500","RHS_HP_KMGU2","RHS_HP_O25L","RHS_HP_APU68M3_S24","RHS_HP_B13L","RHS_HP_B8M1","RHS_HP_UB16","RHS_HP_UB32","RHS_HP_R73"],
                    "priority": 9,
                    "attachment": "rhs_mag_fab250",
                    "maxweight": 1200
                },
                # Class: CfgVehicles|RHS_su25_base|Components|TransportPylonsComponent|pylons|pylon3 [Indent level: 4],
                "pylon3": {
                    "hardpoints": ["RHS_HP_KH25","RHS_HP_FAB100","RHS_HP_FAB100_MBD3_U4T","RHS_HP_FAB100_MBD3_U6","RHS_HP_FAB250","RHS_HP_FAB500","RHS_HP_KMGU2","RHS_HP_O25L","RHS_HP_APU68M3_S24","RHS_HP_B13L","RHS_HP_B8M1","RHS_HP_UB16","RHS_HP_UB32","RHS_HP_R73"],
                    "priority": 7,
                    "hitpoint": "HitPylon3",
                    "uiposition": [0.33,0.4],
                    "attachment": "rhs_mag_fab250",
                    "maxweight": 1200
                },
                # Class: CfgVehicles|RHS_su25_base|Components|TransportPylonsComponent|pylons|pylon4 [Indent level: 4],
                "pylon4": {
                    "uiposition": [0.33,0.15],
                    "mirroredmissilepos": 3,
                    "hitpoint": "HitPylon4",
                    "hardpoints": ["RHS_HP_KH25","RHS_HP_FAB100","RHS_HP_FAB100_MBD3_U4T","RHS_HP_FAB100_MBD3_U6","RHS_HP_FAB250","RHS_HP_FAB500","RHS_HP_KMGU2","RHS_HP_O25L","RHS_HP_APU68M3_S24","RHS_HP_B13L","RHS_HP_B8M1","RHS_HP_UB16","RHS_HP_UB32","RHS_HP_R73"],
                    "priority": 7,
                    "attachment": "rhs_mag_fab250",
                    "maxweight": 1200
                },
                # Class: CfgVehicles|RHS_su25_base|Components|TransportPylonsComponent|pylons|pylon5 [Indent level: 4],
                "pylon5": {
                    "hardpoints": ["RHS_HP_KH25","RHS_HP_FAB100","RHS_HP_FAB100_MBD3_U4T","RHS_HP_FAB100_MBD3_U6","RHS_HP_FAB250","RHS_HP_FAB500","RHS_HP_KMGU2","RHS_HP_O25L","RHS_HP_APU68M3_S24","RHS_HP_B13L","RHS_HP_B8M1","RHS_HP_UB16","RHS_HP_UB32","RHS_HP_R73"],
                    "priority": 10,
                    "attachment": "rhs_mag_b8m1_s8kom",
                    "hitpoint": "HitPylon5",
                    "maxweight": 1200,
                    "uiposition": [0.34,0.45]
                },
                # Class: CfgVehicles|RHS_su25_base|Components|TransportPylonsComponent|pylons|pylon6 [Indent level: 4],
                "pylon6": {
                    "uiposition": [0.34,0.1],
                    "mirroredmissilepos": 5,
                    "hitpoint": "HitPylon6",
                    "hardpoints": ["RHS_HP_KH25","RHS_HP_FAB100","RHS_HP_FAB100_MBD3_U4T","RHS_HP_FAB100_MBD3_U6","RHS_HP_FAB250","RHS_HP_FAB500","RHS_HP_KMGU2","RHS_HP_O25L","RHS_HP_APU68M3_S24","RHS_HP_B13L","RHS_HP_B8M1","RHS_HP_UB16","RHS_HP_UB32","RHS_HP_R73"],
                    "priority": 10,
                    "attachment": "rhs_mag_b8m1_s8kom",
                    "maxweight": 1200
                },
                # Class: CfgVehicles|RHS_su25_base|Components|TransportPylonsComponent|pylons|pylon7 [Indent level: 4],
                "pylon7": {
                    "hardpoints": ["RHS_HP_FAB100","RHS_HP_FAB100_MBD3_U4T","RHS_HP_FAB100_MBD3_U6","RHS_HP_FAB250","RHS_HP_FAB500","RHS_HP_KMGU2","RHS_HP_O25L","RHS_HP_APU68M3_S24","RHS_HP_B13L","RHS_HP_B8M1","RHS_HP_UB16","RHS_HP_UB32","RHS_HP_R73"],
                    "priority": 11,
                    "attachment": "rhs_mag_b8m1_s8df",
                    "hitpoint": "HitPylon7",
                    "maxweight": 1200,
                    "uiposition": [0.35,0.5]
                },
                # Class: CfgVehicles|RHS_su25_base|Components|TransportPylonsComponent|pylons|pylon8 [Indent level: 4],
                "pylon8": {
                    "uiposition": [0.35,0.05],
                    "mirroredmissilepos": 7,
                    "hitpoint": "HitPylon8",
                    "hardpoints": ["RHS_HP_FAB100","RHS_HP_FAB100_MBD3_U4T","RHS_HP_FAB100_MBD3_U6","RHS_HP_FAB250","RHS_HP_FAB500","RHS_HP_KMGU2","RHS_HP_O25L","RHS_HP_APU68M3_S24","RHS_HP_B13L","RHS_HP_B8M1","RHS_HP_UB16","RHS_HP_UB32","RHS_HP_R73"],
                    "priority": 11,
                    "attachment": "rhs_mag_b8m1_s8df",
                    "maxweight": 1200
                },
                # Class: CfgVehicles|RHS_su25_base|Components|TransportPylonsComponent|pylons|pylon9 [Indent level: 4],
                "pylon9": {
                    "hardpoints": ["RHS_HP_R60"],
                    "priority": 12,
                    "attachment": "rhs_mag_R60M",
                    "hitpoint": "HitPylon9",
                    "maxweight": 1200,
                    "uiposition": [0.36,0.55]
                },
                # Class: CfgVehicles|RHS_su25_base|Components|TransportPylonsComponent|pylons|pylon10 [Indent level: 4],
                "pylon10": {
                    "uiposition": [0.36,0],
                    "mirroredmissilepos": 9,
                    "hitpoint": "HitPylon10",
                    "hardpoints": ["RHS_HP_R60"],
                    "priority": 12,
                    "attachment": "rhs_mag_R60M",
                    "maxweight": 1200
                },
                # Class: CfgVehicles|RHS_su25_base|Components|TransportPylonsComponent|pylons|cmDispenser [Indent level: 4],
                "cmdispenser": {
                    "hardpoints": ["RHS_cm_ASO2","RHS_cm_ASO2_x2","RHS_cm_ASO2_x4"],
                    "priority": 1,
                    "attachment": "rhs_ASO2_CMFlare_Chaff_Magazine_x4",
                    "maxweight": 800,
                    "uiposition": [0.625,0.275]
                }
            },
            # Class: CfgVehicles|RHS_su25_base|Components|TransportPylonsComponent|Presets [Indent level: 3],
            "presets": {
                # Class: CfgVehicles|RHS_su25_base|Components|TransportPylonsComponent|Presets|CAS [Indent level: 4]
                "cas": {
                    "attachment": ["rhs_mag_b8m1_s8kom","rhs_mag_b8m1_s8kom","rhs_mag_b8m1_s8kom","rhs_mag_b8m1_s8kom","rhs_mag_b8m1_s8df","rhs_mag_b8m1_s8df","rhs_mag_b8m1_s8df","rhs_mag_b8m1_s8df","rhs_mag_R60M","rhs_mag_R60M","rhs_ASO2_CMFlare_Chaff_Magazine_x4"],
                    "displayname": "Close Air Support"
                },
                # Class: CfgVehicles|RHS_su25_base|Components|TransportPylonsComponent|Presets|HeavyCAS [Indent level: 4],
                "heavycas": {
                    "attachment": ["rhs_mag_b13l_s13b","rhs_mag_b13l_s13b","rhs_mag_b13l_s13t","rhs_mag_b13l_s13t","rhs_mag_b8m1_s8df","rhs_mag_b8m1_s8df","rhs_mag_b8m1_s8df","rhs_mag_b8m1_s8df","rhs_mag_R60M","rhs_mag_R60M","rhs_ASO2_CMFlare_Chaff_Magazine_x4"],
                    "displayname": "Close Air Support (S-13)"
                },
                # Class: CfgVehicles|RHS_su25_base|Components|TransportPylonsComponent|Presets|GroundSupress_S24B [Indent level: 4],
                "groundsupress_s24b": {
                    "attachment": ["rhs_mag_apu68m3_s24b","rhs_mag_apu68m3_s24b","rhs_mag_apu68m3_s24b","rhs_mag_apu68m3_s24b","rhs_mag_apu68m3_s24b","rhs_mag_apu68m3_s24b","rhs_mag_apu68m3_s24b","rhs_mag_apu68m3_s24b","rhs_mag_R60M","rhs_mag_R60M","rhs_ASO2_CMFlare_Chaff_Magazine_x4"],
                    "displayname": "Ground Supress (S-24B)"
                },
                # Class: CfgVehicles|RHS_su25_base|Components|TransportPylonsComponent|Presets|Bomb [Indent level: 4],
                "bomb": {
                    "attachment": ["rhs_mag_fab250","rhs_mag_fab250","rhs_mag_fab250","rhs_mag_fab250","rhs_mag_b8m1_s8kom","rhs_mag_b8m1_s8kom","rhs_mag_b8m1_s8df","rhs_mag_b8m1_s8df","rhs_mag_R60M","rhs_mag_R60M","rhs_ASO2_CMFlare_Chaff_Magazine_x4"],
                    "displayname": "Bomb (FAB-250)"
                },
                # Class: CfgVehicles|RHS_su25_base|Components|TransportPylonsComponent|Presets|HeavyBomb [Indent level: 4],
                "heavybomb": {
                    "attachment": ["rhs_mag_fab500","rhs_mag_fab500","rhs_mag_fab500","rhs_mag_fab500","rhs_mag_b8m1_s8kom","rhs_mag_b8m1_s8kom","rhs_mag_b8m1_s8df","rhs_mag_b8m1_s8df","rhs_mag_R60M","rhs_mag_R60M","rhs_ASO2_CMFlare_Chaff_Magazine_x4"],
                    "displayname": "Bomb (FAB-500)"
                },
                # Class: CfgVehicles|RHS_su25_base|Components|TransportPylonsComponent|Presets|AT [Indent level: 4],
                "at": {
                    "attachment": ["rhs_mag_fab250","rhs_mag_fab250","rhs_mag_kh25ML","rhs_mag_kh25ML","rhs_mag_kh25ML","rhs_mag_kh25ML","rhs_mag_b8m1_s8df","rhs_mag_b8m1_s8df","rhs_mag_R60M","rhs_mag_R60M","rhs_ASO2_CMFlare_Chaff_Magazine_x4"],
                    "displayname": "Anti Tank (Kh-25ML)"
                },
                # Class: CfgVehicles|RHS_su25_base|Components|TransportPylonsComponent|Presets|HeavyAT [Indent level: 4],
                "heavyat": {
                    "attachment": ["rhs_mag_kh29ML","rhs_mag_kh29ML","rhs_mag_fab250","rhs_mag_fab250","rhs_mag_b8m1_s8kom","rhs_mag_b8m1_s8kom","rhs_mag_b8m1_s8kom","rhs_mag_b8m1_s8kom","rhs_mag_R60M","rhs_mag_R60M","rhs_ASO2_CMFlare_Chaff_Magazine_x4"],
                    "displayname": "Anti Tank (Kh-29ML)"
                },
                # Class: CfgVehicles|RHS_su25_base|Components|TransportPylonsComponent|Presets|HeavyATMix [Indent level: 4],
                "heavyatmix": {
                    "attachment": ["rhs_mag_kh29ML","rhs_mag_kh29ML","rhs_mag_kh25ML","rhs_mag_kh25ML","rhs_mag_kh25ML","rhs_mag_kh25ML","rhs_mag_b8m1_s8kom","rhs_mag_b8m1_s8kom","rhs_mag_R60M","rhs_mag_R60M","rhs_ASO2_CMFlare_Chaff_Magazine_x4"],
                    "displayname": "Anti Tank (Mixed)"
                },
                # Class: CfgVehicles|RHS_su25_base|Components|TransportPylonsComponent|Presets|Cluster [Indent level: 4],
                "cluster": {
                    "attachment": ["rhs_mag_rbk250_ao1","rhs_mag_rbk250_ao1","rhs_mag_rbk250_ao1","rhs_mag_rbk250_ao1","rhs_mag_b8m1_s8kom","rhs_mag_b8m1_s8kom","rhs_mag_b8m1_s8df","rhs_mag_b8m1_s8df","rhs_mag_R60M","rhs_mag_R60M","rhs_ASO2_CMFlare_Chaff_Magazine_x4"],
                    "displayname": "Heavy CAS (S-13)"
                },
                # Class: CfgVehicles|RHS_su25_base|Components|TransportPylonsComponent|Presets|KMGU [Indent level: 4],
                "kmgu": {
                    "attachment": ["rhs_mag_kmgu2_ao25","rhs_mag_kmgu2_ao25","rhs_mag_kmgu2_ao25","rhs_mag_kmgu2_ao25","rhs_mag_b8m1_s8kom","rhs_mag_b8m1_s8kom","rhs_mag_b8m1_s8df","rhs_mag_b8m1_s8df","rhs_mag_R60M","rhs_mag_R60M","rhs_ASO2_CMFlare_Chaff_Magazine_x4"],
                    "displayname": "KMGU-2"
                }
            }
        },
        # Class: CfgVehicles|RHS_su25_base|Components|SensorsManagerComponent [Indent level: 2],
        "sensorsmanagercomponent": {
            # Class: CfgVehicles|RHS_su25_base|Components|SensorsManagerComponent|Components [Indent level: 3]
            "components": {
                # Class: CfgVehicles|RHS_su25_base|Components|SensorsManagerComponent|Components|PassiveRadarSensorComponent [Indent level: 4]
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
        # Class: CfgVehicles|RHS_su25_base|Components|TransportCountermeasuresComponent [Indent level: 2],
        "transportcountermeasurescomponent": {
        }
    },
    # Class: CfgVehicles|RHS_su25_base|Attributes [Indent level: 1],
    "attributes": {
        # Class: CfgVehicles|RHS_su25_base|Attributes|ObjectTexture [Indent level: 2]
        "objecttexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayname": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        # Class: CfgVehicles|RHS_su25_base|Attributes|rhs_decalNumber_type [Indent level: 2],
        "rhs_decalnumber_type": {
            "displayname": "Define font type of side number",
            "tooltip": "Define kind of font that will be drawn on vehicle",
            "property": "rhs_decalNumber_type",
            "control": "Combo",
            "expression": "if(_value != 'NoChange')then{ _this setVariable ['%s', _value];[_this,[['Number', cRHSAIRSU25NumberPlaces, _value]]] call rhs_fnc_decalsInit}",
            "defaultvalue": 0,
            "typename": "STRING",
            # Class: CfgVehicles|RHS_su25_base|Attributes|rhs_decalNumber_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|RHS_su25_base|Attributes|rhs_decalNumber_type|values|NoChange [Indent level: 4]
                "nochange": {
                    "name": "Default",
                    "value": "NoChange"
                },
                # Class: CfgVehicles|RHS_su25_base|Attributes|rhs_decalNumber_type|values|AviaYellow [Indent level: 4],
                "aviayellow": {
                    "name": "Aviation Yellow",
                    "value": "AviaYellow"
                },
                # Class: CfgVehicles|RHS_su25_base|Attributes|rhs_decalNumber_type|values|AviaBlue [Indent level: 4],
                "aviablue": {
                    "name": "Aviation Blue",
                    "value": "AviaBlue",
                    "defaultvalue": "AviaBlue"
                },
                # Class: CfgVehicles|RHS_su25_base|Attributes|rhs_decalNumber_type|values|AviaRed [Indent level: 4],
                "aviared": {
                    "name": "Aviation Red",
                    "value": "AviaRed"
                },
                # Class: CfgVehicles|RHS_su25_base|Attributes|rhs_decalNumber_type|values|AviaWhiteOut [Indent level: 4],
                "aviawhiteout": {
                    "name": "Aviation White Out",
                    "value": "AviaWhiteOut"
                },
                # Class: CfgVehicles|RHS_su25_base|Attributes|rhs_decalNumber_type|values|AviaCDF [Indent level: 4],
                "aviacdf": {
                    "name": "Aviation CDF",
                    "value": "AviaCDF"
                },
                # Class: CfgVehicles|RHS_su25_base|Attributes|rhs_decalNumber_type|values|Default [Indent level: 4],
                "default": {
                    "name": "Default (White)",
                    "value": "Default"
                },
                # Class: CfgVehicles|RHS_su25_base|Attributes|rhs_decalNumber_type|values|DefaultRed [Indent level: 4],
                "defaultred": {
                    "name": "Default (Red)",
                    "value": "DefaultRed"
                },
                # Class: CfgVehicles|RHS_su25_base|Attributes|rhs_decalNumber_type|values|BoldRed [Indent level: 4],
                "boldred": {
                    "name": "Bold Red",
                    "value": "BoldRed"
                },
                # Class: CfgVehicles|RHS_su25_base|Attributes|rhs_decalNumber_type|values|CDF [Indent level: 4],
                "cdf": {
                    "name": "CDF",
                    "value": "CDF"
                },
                # Class: CfgVehicles|RHS_su25_base|Attributes|rhs_decalNumber_type|values|Handpaint [Indent level: 4],
                "handpaint": {
                    "name": "Handpaint",
                    "value": "Handpaint"
                },
                # Class: CfgVehicles|RHS_su25_base|Attributes|rhs_decalNumber_type|values|HandpaintBlack [Indent level: 4],
                "handpaintblack": {
                    "name": "Handpaint Black",
                    "value": "HandpaintBlack"
                },
                # Class: CfgVehicles|RHS_su25_base|Attributes|rhs_decalNumber_type|values|Iraqi [Indent level: 4],
                "iraqi": {
                    "name": "Iraqi",
                    "value": "Iraqi"
                }
            }
        },
        # Class: CfgVehicles|RHS_su25_base|Attributes|rhs_decalNumber [Indent level: 2],
        "rhs_decalnumber": {
            "displayname": "Set side number",
            "tooltip": "Set side number. 2 numbers are required. Type 0 to hide numbers completly",
            "property": "rhs_decalNumber",
            "control": "Edit",
            "validate": "Number",
            "defaultvalue": "-1",
            "typename": "Number",
            "expression": "if(_value >= 0)then{if(_value == 0)then{{[_this setobjectTexture [_x,'a3|data_f|clear_empty.paa']]}foreach cRHSAIRSU25NumberPlaces}else{[_this, [['Number', cRHSAIRSU25NumberPlaces, _this getVariable ['rhs_decalNumber_type','AviaYellow'], _value] ] ] call rhs_fnc_decalsInit}};"
        },
        # Class: CfgVehicles|RHS_su25_base|Attributes|rhs_decalNoseArt [Indent level: 2],
        "rhs_decalnoseart": {
            "displayname": "Define Nose Art",
            "tooltip": "Define Nose Art texture located near the cabin. Appears on both sides",
            "property": "rhs_decalNoseArt",
            "control": "Combo",
            "expression": "if(_value >= 0)then{ [_this, [ [ 'Label', cRHSAIRSU25NosePlaces, 'Su25NoseArt',_value] ] ] call rhs_fnc_decalsInit};",
            "defaultvalue": "-1",
            "typename": "Number",
            # Class: CfgVehicles|RHS_su25_base|Attributes|rhs_decalNoseArt|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|RHS_su25_base|Attributes|rhs_decalNoseArt|values|Random [Indent level: 4]
                "random": {
                    "name": "Random",
                    "value": -1,
                    "defaultvalue": -1
                },
                # Class: CfgVehicles|RHS_su25_base|Attributes|rhs_decalNoseArt|values|Empty [Indent level: 4],
                "empty": {
                    "name": "Empty",
                    "value": 0
                },
                # Class: CfgVehicles|RHS_su25_base|Attributes|rhs_decalNoseArt|values|Arrows [Indent level: 4],
                "arrows": {
                    "name": "Aviation emblem",
                    "value": 1
                },
                # Class: CfgVehicles|RHS_su25_base|Attributes|rhs_decalNoseArt|values|Thunders [Indent level: 4],
                "thunders": {
                    "name": "Thunders",
                    "value": 2
                },
                # Class: CfgVehicles|RHS_su25_base|Attributes|rhs_decalNoseArt|values|Eyes [Indent level: 4],
                "eyes": {
                    "name": "Eyes",
                    "value": 3
                },
                # Class: CfgVehicles|RHS_su25_base|Attributes|rhs_decalNoseArt|values|Stars [Indent level: 4],
                "stars": {
                    "name": "Stars",
                    "value": 4
                }
            }
        },
        # Class: CfgVehicles|RHS_su25_base|Attributes|rhs_decalSideArt [Indent level: 2],
        "rhs_decalsideart": {
            "displayname": "Define Side Art",
            "tooltip": "Define Side Art texture located near the jet intake. Appears on both sides",
            "property": "rhs_decalSideArt",
            "expression": "if(_value >= 0)then{ [_this, [ [ 'Label', cRHSAIRSU25SidePlaces, 'Su25Ex',_value] ] ] call rhs_fnc_decalsInit};",
            # Class: CfgVehicles|RHS_su25_base|Attributes|rhs_decalSideArt|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|RHS_su25_base|Attributes|rhs_decalSideArt|values|Random [Indent level: 4]
                "random": {
                    "name": "Random",
                    "value": -1,
                    "defaultvalue": -1
                },
                # Class: CfgVehicles|RHS_su25_base|Attributes|rhs_decalSideArt|values|Empty [Indent level: 4],
                "empty": {
                    "name": "Empty",
                    "value": 0
                },
                # Class: CfgVehicles|RHS_su25_base|Attributes|rhs_decalSideArt|values|Crow [Indent level: 4],
                "crow": {
                    "name": "Crow",
                    "value": 1
                },
                # Class: CfgVehicles|RHS_su25_base|Attributes|rhs_decalSideArt|values|Russia [Indent level: 4],
                "russia": {
                    "name": "Russia emblem",
                    "value": 2
                }
            },
            "control": "Combo",
            "defaultvalue": "-1",
            "typename": "Number"
        },
        # Class: CfgVehicles|RHS_su25_base|Attributes|rhs_decalTail [Indent level: 2],
        "rhs_decaltail": {
            "displayname": "Define tail decal",
            "tooltip": "Define tail decal that will be drawn on vehicle",
            "property": "rhs_decalTail",
            "control": "Combo",
            "expression": "[_this,[['Label', cRHSAIRSU25TailPlaces, 'Aviation',_value]]] call rhs_fnc_decalsInit",
            "defaultvalue": -1,
            "typename": "Number",
            # Class: CfgVehicles|RHS_su25_base|Attributes|rhs_decalTail|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|RHS_su25_base|Attributes|rhs_decalTail|values|Default [Indent level: 4]
                "default": {
                    "name": "Default",
                    "value": -1
                },
                # Class: CfgVehicles|RHS_su25_base|Attributes|rhs_decalTail|values|Empty [Indent level: 4],
                "empty": {
                    "name": "Empty",
                    "value": 0
                },
                # Class: CfgVehicles|RHS_su25_base|Attributes|rhs_decalTail|values|VVS [Indent level: 4],
                "vvs": {
                    "name": "VVS Russia",
                    "value": 3,
                    "defaultvalue": 3
                }
            }
        }
    },
    # Class: CfgVehicles|RHS_su25_base|Exhausts [Indent level: 1],
    "exhausts": {
        # Class: CfgVehicles|RHS_su25_base|Exhausts|Exhaust1 [Indent level: 2]
        "exhaust1": {
            "position": "exhaust1",
            "direction": "exhaust1_dir",
            "effect": "ExhaustsEffectPlaneHP",
            "engineindex": 0
        },
        # Class: CfgVehicles|RHS_su25_base|Exhausts|Exhaust2 [Indent level: 2],
        "exhaust2": {
            "position": "exhaust2",
            "direction": "exhaust2_dir",
            "effect": "ExhaustsEffectPlaneHP",
            "engineindex": 1
        }
    },
    # Class: CfgVehicles|RHS_su25_base|RenderTargets [Indent level: 1],
    "rendertargets": {
        # Class: CfgVehicles|RHS_su25_base|RenderTargets|Periscope [Indent level: 2]
        "periscope": {
            "rendertarget": "rendertarget0",
            # Class: CfgVehicles|RHS_su25_base|RenderTargets|Periscope|CameraView1 [Indent level: 3],
            "cameraview1": {
                "pointposition": "PIP0_pos",
                "pointdirection": "PIP0_dir",
                "rendervisionmode": 0,
                "renderquality": 2,
                "fov": 0.5
            }
        }
    },
    # Class: CfgVehicles|RHS_su25_base|compartmentsLights [Indent level: 1],
    "compartmentslights": {
        # Class: CfgVehicles|RHS_su25_base|compartmentsLights|Comp1 [Indent level: 2]
        "comp1": {
            # Class: CfgVehicles|RHS_su25_base|compartmentsLights|Comp1|Light_General [Indent level: 3]
            "light_general": {
                "color": [40,20,20],
                "ambient": [0,0,0],
                "intensity": 2.5,
                "size": 0,
                "useflare": 0,
                "flaresize": 0,
                "flaremaxdistance": 0,
                "daylight": 0,
                "blinking": 0,
                # Class: CfgVehicles|RHS_su25_base|compartmentsLights|Comp1|Light_General|Attenuation [Indent level: 4],
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
    # Class: CfgVehicles|RHS_su25_base|Reflectors [Indent level: 1],
    "reflectors": {
        # Class: CfgVehicles|RHS_su25_base|Reflectors|Left [Indent level: 2]
        "left": {
            "ambient": [100,100,100,0],
            "color": [7000,7500,10000,1],
            "conefadecoef": 10,
            "daylight": 0,
            "direction": "konec l svetla",
            "flaresize": 4,
            "hitpoint": "l svetlo",
            "innerangle": 20,
            "intensity": 50,
            "outerangle": 60,
            "position": "l svetlo",
            "selection": "l svetlo",
            "size": 1,
            "useflare": 1,
            # Class: CfgVehicles|RHS_su25_base|Reflectors|Left|Attenuation [Indent level: 3],
            "attenuation": {
                "constant": 0,
                "linear": 0,
                "quadratic": 4,
                "start": 1
            }
        },
        # Class: CfgVehicles|RHS_su25_base|Reflectors|Left_Flare [Indent level: 2],
        "left_flare": {
            "intensity": 0.5,
            "useflare": 1,
            "innerangle": 5,
            "outerangle": 175,
            "ambient": [100,100,100,0],
            "color": [7000,7500,10000,1],
            "conefadecoef": 10,
            "daylight": 0,
            "direction": "konec l svetla",
            "flaresize": 4,
            "hitpoint": "l svetlo",
            "position": "l svetlo",
            "selection": "l svetlo",
            "size": 1,
            # Class: CfgVehicles|RHS_su25_base|Reflectors|Left|Attenuation [Indent level: 3],
            "attenuation": {
                "constant": 0,
                "linear": 0,
                "quadratic": 4,
                "start": 1
            }
        },
        # Class: CfgVehicles|RHS_su25_base|Reflectors|Right [Indent level: 2],
        "right": {
            "position": "p svetlo",
            "direction": "konec p svetla",
            "hitpoint": "p svetlo",
            "selection": "p svetlo",
            "ambient": [100,100,100,0],
            "color": [7000,7500,10000,1],
            "conefadecoef": 10,
            "daylight": 0,
            "flaresize": 4,
            "innerangle": 20,
            "intensity": 50,
            "outerangle": 60,
            "size": 1,
            "useflare": 1,
            # Class: CfgVehicles|RHS_su25_base|Reflectors|Left|Attenuation [Indent level: 3],
            "attenuation": {
                "constant": 0,
                "linear": 0,
                "quadratic": 4,
                "start": 1
            }
        },
        # Class: CfgVehicles|RHS_su25_base|Reflectors|Right_Flare [Indent level: 2],
        "right_flare": {
            "intensity": 0.5,
            "useflare": 1,
            "innerangle": 5,
            "outerangle": 175,
            "position": "p svetlo",
            "direction": "konec p svetla",
            "hitpoint": "p svetlo",
            "selection": "p svetlo",
            "ambient": [100,100,100,0],
            "color": [7000,7500,10000,1],
            "conefadecoef": 10,
            "daylight": 0,
            "flaresize": 4,
            "size": 1,
            # Class: CfgVehicles|RHS_su25_base|Reflectors|Left|Attenuation [Indent level: 3],
            "attenuation": {
                "constant": 0,
                "linear": 0,
                "quadratic": 4,
                "start": 1
            }
        }
    },
    "aggregatereflectors": [["Left","Left_Flare"],["Right","Right_Flare"]],
    # Class: CfgVehicles|RHS_su25_base|markerlights [Indent level: 1],
    "markerlights": {
        # Class: CfgVehicles|RHS_su25_base|markerlights|GreenStill [Indent level: 2]
        "greenstill": {
            "activelight": 0,
            "color": [0,0.8,0],
            "ambient": [0,0.08,0],
            "intensity": 55,
            "blinking": 0,
            "brightness": 0.01,
            "flaresize": 0.5,
            "name": "zeleny pozicni",
            "useflare": 1,
            "drawlight": 1,
            "drawlightsize": 0.25,
            "drawlightcentersize": 0.08
        },
        # Class: CfgVehicles|RHS_su25_base|markerlights|RedStill [Indent level: 2],
        "redstill": {
            "color": [0.8,0,0],
            "ambient": [0.08,0,0],
            "name": "cerveny pozicni",
            "activelight": 0,
            "intensity": 55,
            "blinking": 0,
            "brightness": 0.01,
            "flaresize": 0.5,
            "useflare": 1,
            "drawlight": 1,
            "drawlightsize": 0.25,
            "drawlightcentersize": 0.08
        },
        # Class: CfgVehicles|RHS_su25_base|markerlights|WhiteStill [Indent level: 2],
        "whitestill": {
            "color": [1,1,1],
            "ambient": [0.1,0.1,0.1],
            "name": "bily pozicni",
            "activelight": 0,
            "intensity": 55,
            "blinking": 0,
            "brightness": 0.01,
            "flaresize": 0.5,
            "useflare": 1,
            "drawlight": 1,
            "drawlightsize": 0.25,
            "drawlightcentersize": 0.08
        },
        # Class: CfgVehicles|RHS_su25_base|markerlights|WhiteBlicking [Indent level: 2],
        "whiteblicking": {
            "color": [1,1,1],
            "ambient": [0.1,0.1,0.1],
            "blinking": 1,
            "name": "bily pozicni blik",
            "activelight": 0,
            "intensity": 55,
            "brightness": 0.01,
            "flaresize": 0.5,
            "useflare": 1,
            "drawlight": 1,
            "drawlightsize": 0.25,
            "drawlightcentersize": 0.08
        },
        # Class: CfgVehicles|RHS_su25_base|markerlights|RedBlinking [Indent level: 2],
        "redblinking": {
            "color": [0.9,0.15,0.1],
            "ambient": [0.09,0.015,0.01],
            "name": "cerveny pozicni blik",
            "blinking": 1,
            "activelight": 0,
            "intensity": 55,
            "brightness": 0.01,
            "flaresize": 0.5,
            "useflare": 1,
            "drawlight": 1,
            "drawlightsize": 0.25,
            "drawlightcentersize": 0.08
        }
    },
    # Class: CfgVehicles|RHS_su25_base|Damage [Indent level: 1],
    "damage": {
        "tex": ["rhsafrf|addons|rhs_a2port_air|su25|data|rhs_su25_warningLights_empty_ca.paa","rhsafrf|addons|rhs_a2port_air|su25|data|rhs_su25_warningLights_ca.paa"],
        "mat": ["rhsafrf|addons|rhs_a2port_air|su25|data|su25_glass.rvmat","rhsafrf|addons|rhs_a2port_air|su25|data|su25_glass_damage.rvmat","rhsafrf|addons|rhs_a2port_air|su25|data|su25_glass_damage.rvmat","rhsafrf|addons|rhs_a2port_air|su25|data|su25_glass_in.rvmat","rhsafrf|addons|rhs_a2port_air|su25|data|su25_glass_in_damage.rvmat","rhsafrf|addons|rhs_a2port_air|su25|data|su25_glass_in_damage.rvmat","rhsafrf|addons|rhs_a2port_air|su25|data|su25_body1.rvmat","rhsafrf|addons|rhs_a2port_air|su25|data|su25_body1_damage.rvmat","rhsafrf|addons|rhs_a2port_air|su25|data|su25_body1_destruct.rvmat","rhsafrf|addons|rhs_a2port_air|su25|data|su25_body2.rvmat","rhsafrf|addons|rhs_a2port_air|su25|data|su25_body2_damage.rvmat","rhsafrf|addons|rhs_a2port_air|su25|data|su25_body2_destruct.rvmat","rhsafrf|addons|rhs_a2port_air|su25|data|su25_glass.rvmat","rhsafrf|addons|rhs_a2port_air|su25|data|su25_glass_damage.rvmat","rhsafrf|addons|rhs_a2port_air|su25|data|su25_glass_destruct.rvmat","a3|data_f|default.rvmat","a3|data_f|default.rvmat","a3|data_f|default_destruct.rvmat"]
    },
    # Class: CfgVehicles|RHS_su25_base|AnimationSources [Indent level: 1],
    "animationsources": {
        # Class: CfgVehicles|RHS_su25_base|AnimationSources|eject [Indent level: 2]
        "eject": {
            "source": "door",
            "animperiod": 0.6,
            "initphase": 0
        },
        # Class: CfgVehicles|RHS_su25_base|AnimationSources|eject_hide [Indent level: 2],
        "eject_hide": {
            "source": "user",
            "animperiod": 0.6,
            "initphase": 0
        },
        # Class: CfgVehicles|RHS_su25_base|AnimationSources|throttle_source [Indent level: 2],
        "throttle_source": {
            "animperiod": 10,
            "source": "user",
            "initphase": 0
        },
        # Class: CfgVehicles|RHS_su25_base|AnimationSources|rwr_lights_lock [Indent level: 2],
        "rwr_lights_lock": {
            "source": "user",
            "initphase": 0,
            "animperiod": 8
        },
        # Class: CfgVehicles|RHS_su25_base|AnimationSources|rwr_lock_dir_primary [Indent level: 2],
        "rwr_lock_dir_primary": {
            "animperiod": 0.1,
            "source": "user",
            "initphase": 0
        },
        # Class: CfgVehicles|RHS_su25_base|AnimationSources|rwr_lock_primary [Indent level: 2],
        "rwr_lock_primary": {
            "animperiod": 1e-007,
            "source": "user",
            "initphase": 0
        },
        # Class: CfgVehicles|RHS_su25_base|AnimationSources|rwr_signal_strenght [Indent level: 2],
        "rwr_signal_strenght": {
            "animperiod": 1e-007,
            "source": "user",
            "initphase": 0
        },
        # Class: CfgVehicles|RHS_su25_base|AnimationSources|rwr_lights [Indent level: 2],
        "rwr_lights": {
            "animperiod": 1e-007,
            "source": "user",
            "initphase": 0
        },
        # Class: CfgVehicles|RHS_su25_base|AnimationSources|hit_pylon_1_source [Indent level: 2],
        "hit_pylon_1_source": {
            "source": "Hit",
            "hitpoint": "HitPylon1"
        },
        # Class: CfgVehicles|RHS_su25_base|AnimationSources|hit_pylon_2_source [Indent level: 2],
        "hit_pylon_2_source": {
            "source": "Hit",
            "hitpoint": "HitPylon2"
        },
        # Class: CfgVehicles|RHS_su25_base|AnimationSources|hit_pylon_3_source [Indent level: 2],
        "hit_pylon_3_source": {
            "source": "Hit",
            "hitpoint": "HitPylon3"
        },
        # Class: CfgVehicles|RHS_su25_base|AnimationSources|hit_pylon_4_source [Indent level: 2],
        "hit_pylon_4_source": {
            "source": "Hit",
            "hitpoint": "HitPylon4"
        },
        # Class: CfgVehicles|RHS_su25_base|AnimationSources|hit_pylon_5_source [Indent level: 2],
        "hit_pylon_5_source": {
            "source": "Hit",
            "hitpoint": "HitPylon5"
        },
        # Class: CfgVehicles|RHS_su25_base|AnimationSources|hit_pylon_6_source [Indent level: 2],
        "hit_pylon_6_source": {
            "source": "Hit",
            "hitpoint": "HitPylon6"
        },
        # Class: CfgVehicles|RHS_su25_base|AnimationSources|hit_pylon_7_source [Indent level: 2],
        "hit_pylon_7_source": {
            "source": "Hit",
            "hitpoint": "HitPylon7"
        },
        # Class: CfgVehicles|RHS_su25_base|AnimationSources|hit_pylon_8_source [Indent level: 2],
        "hit_pylon_8_source": {
            "source": "Hit",
            "hitpoint": "HitPylon8"
        },
        # Class: CfgVehicles|RHS_su25_base|AnimationSources|hit_pylon_9_source [Indent level: 2],
        "hit_pylon_9_source": {
            "source": "Hit",
            "hitpoint": "HitPylon9"
        },
        # Class: CfgVehicles|RHS_su25_base|AnimationSources|hit_pylon_10_source [Indent level: 2],
        "hit_pylon_10_source": {
            "source": "Hit",
            "hitpoint": "HitPylon10"
        },
        # Class: CfgVehicles|Plane_CAS_02_base_F|AnimationSources|Cannon_30mm_ammorandom [Indent level: 2],
        "cannon_30mm_ammorandom": {
            "source": "ammorandom",
            "weapon": "Cannon_30mm_Plane_CAS_02_F"
        },
        # Class: CfgVehicles|Plane_CAS_02_base_F|AnimationSources|Cannon_30mm_revolving [Indent level: 2],
        "cannon_30mm_revolving": {
            "source": "revolving",
            "weapon": "Cannon_30mm_Plane_CAS_02_F"
        },
        # Class: CfgVehicles|Plane_CAS_02_base_F|AnimationSources|Missile_AA_03_revolving [Indent level: 2],
        "missile_aa_03_revolving": {
            "source": "revolving",
            "weapon": "Missile_AA_03_Plane_CAS_02_F"
        },
        # Class: CfgVehicles|Plane_CAS_02_base_F|AnimationSources|Missile_AGM_01_revolving [Indent level: 2],
        "missile_agm_01_revolving": {
            "source": "revolving",
            "weapon": "Missile_AGM_01_Plane_CAS_02_F"
        },
        # Class: CfgVehicles|Plane_CAS_02_base_F|AnimationSources|Rocket_03_HE_revolving [Indent level: 2],
        "rocket_03_he_revolving": {
            "source": "revolving",
            "weapon": "Rocket_03_HE_Plane_CAS_02_F"
        },
        # Class: CfgVehicles|Plane_CAS_02_base_F|AnimationSources|Rocket_03_AP_revolving [Indent level: 2],
        "rocket_03_ap_revolving": {
            "source": "revolving",
            "weapon": "Rocket_03_AP_Plane_CAS_02_F"
        },
        # Class: CfgVehicles|Plane_CAS_02_base_F|AnimationSources|Bomb_03_revolving [Indent level: 2],
        "bomb_03_revolving": {
            "source": "revolving",
            "weapon": "Bomb_03_Plane_CAS_02_F"
        },
        # Class: CfgVehicles|Plane_CAS_02_base_F|AnimationSources|Damper_1_source [Indent level: 2],
        "damper_1_source": {
            "source": "damper",
            "wheel": "Wheel_1"
        },
        # Class: CfgVehicles|Plane_CAS_02_base_F|AnimationSources|Damper_2_source [Indent level: 2],
        "damper_2_source": {
            "source": "damper",
            "wheel": "Wheel_2"
        },
        # Class: CfgVehicles|Plane_CAS_02_base_F|AnimationSources|Damper_3_source [Indent level: 2],
        "damper_3_source": {
            "source": "damper",
            "wheel": "Wheel_3"
        },
        # Class: CfgVehicles|Plane_CAS_02_base_F|AnimationSources|Wheel_1_source [Indent level: 2],
        "wheel_1_source": {
            "source": "wheel",
            "wheel": "Wheel_1"
        },
        # Class: CfgVehicles|Plane_CAS_02_base_F|AnimationSources|Wheel_2_source [Indent level: 2],
        "wheel_2_source": {
            "source": "wheel",
            "wheel": "Wheel_2"
        },
        # Class: CfgVehicles|Plane_CAS_02_base_F|AnimationSources|Wheel_3_source [Indent level: 2],
        "wheel_3_source": {
            "source": "wheel",
            "wheel": "Wheel_3"
        },
        # Class: CfgVehicles|Plane_CAS_02_base_F|AnimationSources|HitAvionics [Indent level: 2],
        "hitavionics": {
            "source": "Hit",
            "hitpoint": "HitAvionics",
            "raw": 1
        },
        # Class: CfgVehicles|Plane_CAS_02_base_F|AnimationSources|HideWeapons [Indent level: 2],
        "hideweapons": {
            "source": "user",
            "animperiod": 1e-006,
            "initphase": 0
        },
        # Class: CfgVehicles|Plane_CAS_02_base_F|AnimationSources|canopy_hide [Indent level: 2],
        "canopy_hide": {
            "source": "user",
            "animperiod": 0.001,
            "initphase": 0
        },
        # Class: CfgVehicles|Plane_CAS_02_base_F|AnimationSources|ejection_seat_hide [Indent level: 2],
        "ejection_seat_hide": {
            "source": "user",
            "animperiod": 0.001,
            "initphase": 0
        },
        # Class: CfgVehicles|Plane_CAS_02_base_F|AnimationSources|ejection_seat_motion [Indent level: 2],
        "ejection_seat_motion": {
            "source": "user",
            "animperiod": 0.25,
            "initphase": 0
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
    # Class: CfgVehicles|RHS_su25_base|WingVortices [Indent level: 1],
    "wingvortices": {
        # Class: CfgVehicles|RHS_su25_base|WingVortices|WingTipLeft [Indent level: 2]
        "wingtipleft": {
            "effectname": "WingVortices",
            "position": "cerveny pozicni"
        },
        # Class: CfgVehicles|RHS_su25_base|WingVortices|WingTipRight [Indent level: 2],
        "wingtipright": {
            "effectname": "WingVortices",
            "position": "zeleny pozicni"
        },
        # Class: CfgVehicles|RHS_su25_base|WingVortices|BodyLeft [Indent level: 2],
        "bodyleft": {
            "effectname": "BodyVortices",
            "position": "body_vapour_L_S"
        },
        # Class: CfgVehicles|RHS_su25_base|WingVortices|BodyRight [Indent level: 2],
        "bodyright": {
            "effectname": "BodyVortices",
            "position": "body_vapour_R_S"
        }
    },
    "threat": [1,1,1],
    "driveoncomponent": ["gear_f1","gear_l1","gear_r1"],
    "defaultusermfdvalues": [0,0,0,0,0,0],
    # Class: CfgVehicles|RHS_su25_base|MFD [Indent level: 1],
    "mfd": {
        # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD [Indent level: 2]
        "airplanehud": {
            "enableparallax": 1,
            "topleft": "HUD LH",
            "topright": "HUD PH",
            "bottomleft": "HUD LD",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Pos10Vector [Indent level: 3],
            "pos10vector": {
                "pos0": [0.52,0.03],
                "pos10": [2.02,1.23],
                "type": "vector"
            },
            "color": [0,1,0,0.1],
            # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones [Indent level: 3],
            "bones": {
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones|PlaneW [Indent level: 4]
                "planew": {
                    "pos": [0.5,0.5],
                    "type": "fixed"
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones|HorizonBankMGun [Indent level: 4],
                "horizonbankmgun": {
                    "center": [0,0],
                    "type": "rotational",
                    "source": "HorizonBank",
                    "min": -6.28319,
                    "max": 6.28319,
                    "minangle": -360,
                    "maxangle": 360,
                    "aspectratio": 0.8
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones|HorizonBankReverted [Indent level: 4],
                "horizonbankreverted": {
                    "pos0": [-0,-0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "HorizonBank",
                    "min": -6.28319,
                    "max": 6.28319,
                    "minangle": 360,
                    "maxangle": -360,
                    "aspectratio": 0.8
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones|ImpactPoint [Indent level: 4],
                "impactpoint": {
                    "type": "vector",
                    "source": "ImpactPoint",
                    "pos0": [0.5,0.23],
                    "pos10": [1.38,1.46]
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones|TargetingPodDir [Indent level: 4],
                "targetingpoddir": {
                    "type": "vector",
                    "source": "pilotcamera",
                    "pos0": ["0.50+0.034","0.27-0.0455"],
                    "pos10": [2.02,1.47]
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones|TargetingPodTarget [Indent level: 4],
                "targetingpodtarget": {
                    "type": "vector",
                    "source": "pilotcamera",
                    "pos0": ["0.50+0.034","0.27-0.0455"],
                    "pos10": [2.02,1.47]
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot1 [Indent level: 4],
                "missileflighttimerot1": {
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 2.5,
                    "center": [0,0],
                    "min": 0,
                    "max": 0.5,
                    "minangle": 0,
                    "maxangle": 18,
                    "aspectratio": 0.840909
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot2 [Indent level: 4],
                "missileflighttimerot2": {
                    "maxangle": 37,
                    "max": 6,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 2.5,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.840909
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot3 [Indent level: 4],
                "missileflighttimerot3": {
                    "maxangle": 55.5,
                    "max": 9,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 2.5,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.840909
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot4 [Indent level: 4],
                "missileflighttimerot4": {
                    "maxangle": 74,
                    "max": 12,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 2.5,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.840909
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot5 [Indent level: 4],
                "missileflighttimerot5": {
                    "maxangle": 92.5,
                    "max": 15,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 2.5,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.840909
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot6 [Indent level: 4],
                "missileflighttimerot6": {
                    "maxangle": 111,
                    "max": 18,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 2.5,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.840909
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot7 [Indent level: 4],
                "missileflighttimerot7": {
                    "maxangle": 129.5,
                    "max": 21,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 2.5,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.840909
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot8 [Indent level: 4],
                "missileflighttimerot8": {
                    "maxangle": 148,
                    "max": 24,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 2.5,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.840909
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot9 [Indent level: 4],
                "missileflighttimerot9": {
                    "maxangle": 166.5,
                    "max": 27,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 2.5,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.840909
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot10 [Indent level: 4],
                "missileflighttimerot10": {
                    "maxangle": 185,
                    "max": 30,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 2.5,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.840909
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot11 [Indent level: 4],
                "missileflighttimerot11": {
                    "maxangle": 203.5,
                    "max": 33,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 2.5,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.840909
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot12 [Indent level: 4],
                "missileflighttimerot12": {
                    "maxangle": 222,
                    "max": 36,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 2.5,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.840909
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot13 [Indent level: 4],
                "missileflighttimerot13": {
                    "maxangle": 240.5,
                    "max": 39,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 2.5,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.840909
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot14 [Indent level: 4],
                "missileflighttimerot14": {
                    "maxangle": 259,
                    "max": 42,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 2.5,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.840909
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot15 [Indent level: 4],
                "missileflighttimerot15": {
                    "maxangle": 277.5,
                    "max": 45,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 2.5,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.840909
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot16 [Indent level: 4],
                "missileflighttimerot16": {
                    "maxangle": 296,
                    "max": 48,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 2.5,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.840909
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot17 [Indent level: 4],
                "missileflighttimerot17": {
                    "maxangle": 314.5,
                    "max": 51,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 2.5,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.840909
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot18 [Indent level: 4],
                "missileflighttimerot18": {
                    "maxangle": 333,
                    "max": 54,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 2.5,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.840909
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot19 [Indent level: 4],
                "missileflighttimerot19": {
                    "maxangle": 351.5,
                    "max": 57,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 2.5,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.840909
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot20 [Indent level: 4],
                "missileflighttimerot20": {
                    "maxangle": 370,
                    "max": 60,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 2.5,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.840909
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones|UserRot1 [Indent level: 4],
                "userrot1": {
                    "type": "rotational",
                    "source": "user",
                    "sourceindex": 4,
                    "sourcescale": 0.004,
                    "center": [0,0],
                    "min": 0,
                    "max": 0.5,
                    "minangle": 0,
                    "maxangle": 18,
                    "aspectratio": 0.840909
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones|UserRot2 [Indent level: 4],
                "userrot2": {
                    "maxangle": 37,
                    "max": 6,
                    "type": "rotational",
                    "source": "user",
                    "sourceindex": 4,
                    "sourcescale": 0.004,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.840909
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones|UserRot3 [Indent level: 4],
                "userrot3": {
                    "maxangle": 55.5,
                    "max": 9,
                    "type": "rotational",
                    "source": "user",
                    "sourceindex": 4,
                    "sourcescale": 0.004,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.840909
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones|UserRot4 [Indent level: 4],
                "userrot4": {
                    "maxangle": 74,
                    "max": 12,
                    "type": "rotational",
                    "source": "user",
                    "sourceindex": 4,
                    "sourcescale": 0.004,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.840909
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones|UserRot5 [Indent level: 4],
                "userrot5": {
                    "maxangle": 92.5,
                    "max": 15,
                    "type": "rotational",
                    "source": "user",
                    "sourceindex": 4,
                    "sourcescale": 0.004,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.840909
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones|UserRot6 [Indent level: 4],
                "userrot6": {
                    "maxangle": 111,
                    "max": 18,
                    "type": "rotational",
                    "source": "user",
                    "sourceindex": 4,
                    "sourcescale": 0.004,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.840909
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones|UserRot7 [Indent level: 4],
                "userrot7": {
                    "maxangle": 129.5,
                    "max": 21,
                    "type": "rotational",
                    "source": "user",
                    "sourceindex": 4,
                    "sourcescale": 0.004,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.840909
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones|UserRot8 [Indent level: 4],
                "userrot8": {
                    "maxangle": 148,
                    "max": 24,
                    "type": "rotational",
                    "source": "user",
                    "sourceindex": 4,
                    "sourcescale": 0.004,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.840909
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones|UserRot9 [Indent level: 4],
                "userrot9": {
                    "maxangle": 166.5,
                    "max": 27,
                    "type": "rotational",
                    "source": "user",
                    "sourceindex": 4,
                    "sourcescale": 0.004,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.840909
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones|UserRot10 [Indent level: 4],
                "userrot10": {
                    "maxangle": 185,
                    "max": 30,
                    "type": "rotational",
                    "source": "user",
                    "sourceindex": 4,
                    "sourcescale": 0.004,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.840909
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones|UserRot11 [Indent level: 4],
                "userrot11": {
                    "maxangle": 203.5,
                    "max": 33,
                    "type": "rotational",
                    "source": "user",
                    "sourceindex": 4,
                    "sourcescale": 0.004,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.840909
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones|UserRot12 [Indent level: 4],
                "userrot12": {
                    "maxangle": 222,
                    "max": 36,
                    "type": "rotational",
                    "source": "user",
                    "sourceindex": 4,
                    "sourcescale": 0.004,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.840909
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones|UserRot13 [Indent level: 4],
                "userrot13": {
                    "maxangle": 240.5,
                    "max": 39,
                    "type": "rotational",
                    "source": "user",
                    "sourceindex": 4,
                    "sourcescale": 0.004,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.840909
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones|UserRot14 [Indent level: 4],
                "userrot14": {
                    "maxangle": 259,
                    "max": 42,
                    "type": "rotational",
                    "source": "user",
                    "sourceindex": 4,
                    "sourcescale": 0.004,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.840909
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones|UserRot15 [Indent level: 4],
                "userrot15": {
                    "maxangle": 277.5,
                    "max": 45,
                    "type": "rotational",
                    "source": "user",
                    "sourceindex": 4,
                    "sourcescale": 0.004,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.840909
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones|UserRot16 [Indent level: 4],
                "userrot16": {
                    "maxangle": 296,
                    "max": 48,
                    "type": "rotational",
                    "source": "user",
                    "sourceindex": 4,
                    "sourcescale": 0.004,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.840909
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones|UserRot17 [Indent level: 4],
                "userrot17": {
                    "maxangle": 314.5,
                    "max": 51,
                    "type": "rotational",
                    "source": "user",
                    "sourceindex": 4,
                    "sourcescale": 0.004,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.840909
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones|UserRot18 [Indent level: 4],
                "userrot18": {
                    "maxangle": 333,
                    "max": 54,
                    "type": "rotational",
                    "source": "user",
                    "sourceindex": 4,
                    "sourcescale": 0.004,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.840909
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones|UserRot19 [Indent level: 4],
                "userrot19": {
                    "maxangle": 351.5,
                    "max": 57,
                    "type": "rotational",
                    "source": "user",
                    "sourceindex": 4,
                    "sourcescale": 0.004,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.840909
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Bones|UserRot20 [Indent level: 4],
                "userrot20": {
                    "maxangle": 370,
                    "max": 60,
                    "type": "rotational",
                    "source": "user",
                    "sourceindex": 4,
                    "sourcescale": 0.004,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.840909
                }
            },
            # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Draw [Indent level: 3],
            "draw": {
                "color": [0.69,0.22,0],
                "alpha": 1,
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Draw|ImpactPoint [Indent level: 4],
                "impactpoint": {
                    "condition": "1 - atmissile",
                    # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Draw|ImpactPoint|Cros [Indent level: 5],
                    "cros": {
                        "type": "line",
                        "points": [["ImpactPoint",1,[0.111111,0],1],["ImpactPoint",1,[0.0277778,0],1],[],["ImpactPoint",1,[-0.111111,0],1],["ImpactPoint",1,[-0.0277778,0],1],[],["ImpactPoint",1,[0,0.0934343],1],["ImpactPoint",1,[0,0.0233586],1],[],["ImpactPoint",1,[0,-0.0934343],1],["ImpactPoint",1,[0,-0.0233586],1],[]]
                    },
                    # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Draw|ImpactPoint|Dot [Indent level: 5],
                    "dot": {
                        "type": "line",
                        "points": [["ImpactPoint",[0,0.0035],1],["ImpactPoint",[0.0035,-0],1],["ImpactPoint",[0,-0.0035],1],["ImpactPoint",[-0.0035,-0],1],["ImpactPoint",[0,0.0035],1]]
                    },
                    # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Draw|ImpactPoint|Ring [Indent level: 5],
                    "ring": {
                        "type": "line",
                        "points": [["ImpactPoint",[0.187939,0.0575216],1],["ImpactPoint",[0.193185,0.0435287],1],["ImpactPoint",[0.196962,0.0292045],1],["ImpactPoint",[0.199239,0.014658],1],["ImpactPoint",[0.2,7.35146e-009],1],["ImpactPoint",[0.199239,-0.014658],1],["ImpactPoint",[0.196962,-0.0292045],1],["ImpactPoint",[0.193185,-0.0435286],1],["ImpactPoint",[0.187939,-0.0575216],1],["ImpactPoint",[0.181262,-0.0710767],1],["ImpactPoint",[0.173205,-0.0840909],1],["ImpactPoint",[0.16383,-0.0964651],1],["ImpactPoint",[0.153209,-0.108105],1],["ImpactPoint",[0.141421,-0.118923],1],["ImpactPoint",[0.128558,-0.128835],1],["ImpactPoint",[0.114715,-0.137766],1],["ImpactPoint",[0.1,-0.14565],1],["ImpactPoint",[0.0845237,-0.152424],1],["ImpactPoint",[0.068404,-0.158039],1],["ImpactPoint",[0.0517638,-0.162451],1],["ImpactPoint",[0.0347296,-0.165627],1],["ImpactPoint",[0.0174311,-0.167542],1],["ImpactPoint",[0,-0.168182],1],[],["ImpactPoint",[0.187939,0.0575216],1],["ImpactPoint",[0.169145,0.0517694],1],[],["ImpactPoint",[0.196962,0.0292045],1],["ImpactPoint",[0.187113,0.0277442],1],[],["ImpactPoint",[0.2,7.35146e-009],1],["ImpactPoint",[0.18,6.61632e-009],1],[],["ImpactPoint",[0.196962,-0.0292045],1],["ImpactPoint",[0.187113,-0.0277442],1],[],["ImpactPoint",[0.187939,-0.0575216],1],["ImpactPoint",[0.178542,-0.0546455],1],[],["ImpactPoint",[0.173205,-0.0840909],1],["ImpactPoint",[0.155885,-0.0756818],1],[],["ImpactPoint",[0.153209,-0.108105],1],["ImpactPoint",[0.145548,-0.1027],1],[],["ImpactPoint",[0.128558,-0.128835],1],["ImpactPoint",[0.12213,-0.122393],1],[],["ImpactPoint",[0.1,-0.14565],1],["ImpactPoint",[0.09,-0.131085],1],[],["ImpactPoint",[0.068404,-0.158039],1],["ImpactPoint",[0.0649838,-0.150137],1],[],["ImpactPoint",[0.0347296,-0.165627],1],["ImpactPoint",[0.0329932,-0.157345],1],[],["ImpactPoint",[0,-0.168182],1],["ImpactPoint",[0,-0.151364],1],[]]
                    },
                    # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Draw|ImpactPoint|Triangle [Indent level: 5],
                    "triangle": {
                        "type": "line",
                        "width": 9,
                        "points": [["ImpactPoint",1,["HorizonBankReverted",0,0.192],1],["ImpactPoint",1,["HorizonBankReverted",0.01,0.177],1],["ImpactPoint",1,["HorizonBankReverted",-0.01,0.177],1],["ImpactPoint",1,["HorizonBankReverted",0,0.192],1]]
                    },
                    # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Draw|ImpactPoint|LaunchAutorization [Indent level: 5],
                    "launchautorization": {
                        "type": "line",
                        "width": 14,
                        "points": [["ImpactPoint",[0,-0.172386],1],["MissileFlightTimeRot1",[0,0.205],1,"ImpactPoint",1],["MissileFlightTimeRot2",[0,0.205],1,"ImpactPoint",1],["MissileFlightTimeRot3",[0,0.205],1,"ImpactPoint",1],["MissileFlightTimeRot4",[0,0.205],1,"ImpactPoint",1],["MissileFlightTimeRot5",[0,0.205],1,"ImpactPoint",1],["MissileFlightTimeRot6",[0,0.205],1,"ImpactPoint",1]]
                    },
                    # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Draw|ImpactPoint|LaunchAutorizationBig [Indent level: 5],
                    "launchautorizationbig": {
                        "type": "line",
                        "width": 24,
                        "points": [["MissileFlightTimeRot1",[0,0.215],1,"ImpactPoint",1],["MissileFlightTimeRot2",[0,0.215],1,"ImpactPoint",1],["MissileFlightTimeRot3",[0,0.215],1,"ImpactPoint",1],["MissileFlightTimeRot4",[0,0.215],1,"ImpactPoint",1],["MissileFlightTimeRot5",[0,0.215],1,"ImpactPoint",1]]
                    }
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Draw|TargetingPod [Indent level: 4],
                "targetingpod": {
                    "condition": "atmissile-pilotcameralock",
                    # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Draw|TargetingPod|Cros [Indent level: 5],
                    "cros": {
                        "type": "line",
                        "points": [["TargetingPodDir",1,[0.111111,0],1],["TargetingPodDir",1,[0.0277778,0],1],[],["TargetingPodDir",1,[-0.111111,0],1],["TargetingPodDir",1,[-0.0277778,0],1],[],["TargetingPodDir",1,[0,0.0934343],1],["TargetingPodDir",1,[0,0.0233586],1],[],["TargetingPodDir",1,[0,-0.0934343],1],["TargetingPodDir",1,[0,-0.0233586],1],[]]
                    },
                    # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Draw|TargetingPod|Dot [Indent level: 5],
                    "dot": {
                        "type": "line",
                        "points": [["TargetingPodDir",[0,0.0035],1],["TargetingPodDir",[0.0035,-0],1],["TargetingPodDir",[0,-0.0035],1],["TargetingPodDir",[-0.0035,-0],1],["TargetingPodDir",[0,0.0035],1]]
                    },
                    # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Draw|TargetingPod|Ring [Indent level: 5],
                    "ring": {
                        "type": "line",
                        "points": [["TargetingPodDir",[0.187939,0.0575216],1],["TargetingPodDir",[0.193185,0.0435287],1],["TargetingPodDir",[0.196962,0.0292045],1],["TargetingPodDir",[0.199239,0.014658],1],["TargetingPodDir",[0.2,7.35146e-009],1],["TargetingPodDir",[0.199239,-0.014658],1],["TargetingPodDir",[0.196962,-0.0292045],1],["TargetingPodDir",[0.193185,-0.0435286],1],["TargetingPodDir",[0.187939,-0.0575216],1],["TargetingPodDir",[0.181262,-0.0710767],1],["TargetingPodDir",[0.173205,-0.0840909],1],["TargetingPodDir",[0.16383,-0.0964651],1],["TargetingPodDir",[0.153209,-0.108105],1],["TargetingPodDir",[0.141421,-0.118923],1],["TargetingPodDir",[0.128558,-0.128835],1],["TargetingPodDir",[0.114715,-0.137766],1],["TargetingPodDir",[0.1,-0.14565],1],["TargetingPodDir",[0.0845237,-0.152424],1],["TargetingPodDir",[0.068404,-0.158039],1],["TargetingPodDir",[0.0517638,-0.162451],1],["TargetingPodDir",[0.0347296,-0.165627],1],["TargetingPodDir",[0.0174311,-0.167542],1],["TargetingPodDir",[0,-0.168182],1],[],["TargetingPodDir",[0.187939,0.0575216],1],["TargetingPodDir",[0.169145,0.0517694],1],[],["TargetingPodDir",[0.196962,0.0292045],1],["TargetingPodDir",[0.187113,0.0277442],1],[],["TargetingPodDir",[0.2,7.35146e-009],1],["TargetingPodDir",[0.18,6.61632e-009],1],[],["TargetingPodDir",[0.196962,-0.0292045],1],["TargetingPodDir",[0.187113,-0.0277442],1],[],["TargetingPodDir",[0.187939,-0.0575216],1],["TargetingPodDir",[0.178542,-0.0546455],1],[],["TargetingPodDir",[0.173205,-0.0840909],1],["TargetingPodDir",[0.155885,-0.0756818],1],[],["TargetingPodDir",[0.153209,-0.108105],1],["TargetingPodDir",[0.145548,-0.1027],1],[],["TargetingPodDir",[0.128558,-0.128835],1],["TargetingPodDir",[0.12213,-0.122393],1],[],["TargetingPodDir",[0.1,-0.14565],1],["TargetingPodDir",[0.09,-0.131085],1],[],["TargetingPodDir",[0.068404,-0.158039],1],["TargetingPodDir",[0.0649838,-0.150137],1],[],["TargetingPodDir",[0.0347296,-0.165627],1],["TargetingPodDir",[0.0329932,-0.157345],1],[],["TargetingPodDir",[0,-0.168182],1],["TargetingPodDir",[0,-0.151364],1],[]]
                    },
                    # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Draw|TargetingPod|Triangle [Indent level: 5],
                    "triangle": {
                        "type": "line",
                        "width": 9,
                        "points": [["TargetingPodDir",1,["HorizonBankReverted",0,0.192],1],["TargetingPodDir",1,["HorizonBankReverted",0.01,0.177],1],["TargetingPodDir",1,["HorizonBankReverted",-0.01,0.177],1],["TargetingPodDir",1,["HorizonBankReverted",0,0.192],1]]
                    },
                    # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Draw|TargetingPod|LaunchAutorization [Indent level: 5],
                    "launchautorization": {
                        "type": "line",
                        "width": 14,
                        "points": [["TargetingPodDir",[0,-0.172386],1],["UserRot1",[0,0.205],1,"TargetingPodDir",1],["UserRot2",[0,0.205],1,"TargetingPodDir",1],["UserRot3",[0,0.205],1,"TargetingPodDir",1],["UserRot4",[0,0.205],1,"TargetingPodDir",1],["UserRot5",[0,0.205],1,"TargetingPodDir",1],["UserRot6",[0,0.205],1,"TargetingPodDir",1]]
                    },
                    # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Draw|TargetingPod|LaunchAutorizationBig [Indent level: 5],
                    "launchautorizationbig": {
                        "type": "line",
                        "width": 24,
                        "points": [["UserRot1",[0,0.215],1,"TargetingPodDir",1],["UserRot2",[0,0.215],1,"TargetingPodDir",1],["UserRot3",[0,0.215],1,"TargetingPodDir",1],["UserRot4",[0,0.215],1,"TargetingPodDir",1],["UserRot5",[0,0.215],1,"TargetingPodDir",1]]
                    }
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Draw|TargetingPodTarget [Indent level: 4],
                "targetingpodtarget": {
                    "condition": "(atmissile)*(pilotcameralock>=0)*laseron",
                    # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Draw|TargetingPodTarget|Cros [Indent level: 5],
                    "cros": {
                        "type": "line",
                        "points": [["TargetingPodTarget",1,[0.111111,0],1],["TargetingPodTarget",1,[0.0277778,0],1],[],["TargetingPodTarget",1,[-0.111111,0],1],["TargetingPodTarget",1,[-0.0277778,0],1],[],["TargetingPodTarget",1,[0,0.0934343],1],["TargetingPodTarget",1,[0,0.0233586],1],[],["TargetingPodTarget",1,[0,-0.0934343],1],["TargetingPodTarget",1,[0,-0.0233586],1],[]]
                    },
                    # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Draw|TargetingPodTarget|Dot [Indent level: 5],
                    "dot": {
                        "type": "line",
                        "points": [["TargetingPodTarget",[0,0.0035],1],["TargetingPodTarget",[0.0035,-0],1],["TargetingPodTarget",[0,-0.0035],1],["TargetingPodTarget",[-0.0035,-0],1],["TargetingPodTarget",[0,0.0035],1]]
                    },
                    # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Draw|TargetingPodTarget|Ring [Indent level: 5],
                    "ring": {
                        "type": "line",
                        "points": [["TargetingPodTarget",[0.187939,0.0575216],1],["TargetingPodTarget",[0.193185,0.0435287],1],["TargetingPodTarget",[0.196962,0.0292045],1],["TargetingPodTarget",[0.199239,0.014658],1],["TargetingPodTarget",[0.2,7.35146e-009],1],["TargetingPodTarget",[0.199239,-0.014658],1],["TargetingPodTarget",[0.196962,-0.0292045],1],["TargetingPodTarget",[0.193185,-0.0435286],1],["TargetingPodTarget",[0.187939,-0.0575216],1],["TargetingPodTarget",[0.181262,-0.0710767],1],["TargetingPodTarget",[0.173205,-0.0840909],1],["TargetingPodTarget",[0.16383,-0.0964651],1],["TargetingPodTarget",[0.153209,-0.108105],1],["TargetingPodTarget",[0.141421,-0.118923],1],["TargetingPodTarget",[0.128558,-0.128835],1],["TargetingPodTarget",[0.114715,-0.137766],1],["TargetingPodTarget",[0.1,-0.14565],1],["TargetingPodTarget",[0.0845237,-0.152424],1],["TargetingPodTarget",[0.068404,-0.158039],1],["TargetingPodTarget",[0.0517638,-0.162451],1],["TargetingPodTarget",[0.0347296,-0.165627],1],["TargetingPodTarget",[0.0174311,-0.167542],1],["TargetingPodTarget",[0,-0.168182],1],[],["TargetingPodTarget",[0.187939,0.0575216],1],["TargetingPodTarget",[0.169145,0.0517694],1],[],["TargetingPodTarget",[0.196962,0.0292045],1],["TargetingPodTarget",[0.187113,0.0277442],1],[],["TargetingPodTarget",[0.2,7.35146e-009],1],["TargetingPodTarget",[0.18,6.61632e-009],1],[],["TargetingPodTarget",[0.196962,-0.0292045],1],["TargetingPodTarget",[0.187113,-0.0277442],1],[],["TargetingPodTarget",[0.187939,-0.0575216],1],["TargetingPodTarget",[0.178542,-0.0546455],1],[],["TargetingPodTarget",[0.173205,-0.0840909],1],["TargetingPodTarget",[0.155885,-0.0756818],1],[],["TargetingPodTarget",[0.153209,-0.108105],1],["TargetingPodTarget",[0.145548,-0.1027],1],[],["TargetingPodTarget",[0.128558,-0.128835],1],["TargetingPodTarget",[0.12213,-0.122393],1],[],["TargetingPodTarget",[0.1,-0.14565],1],["TargetingPodTarget",[0.09,-0.131085],1],[],["TargetingPodTarget",[0.068404,-0.158039],1],["TargetingPodTarget",[0.0649838,-0.150137],1],[],["TargetingPodTarget",[0.0347296,-0.165627],1],["TargetingPodTarget",[0.0329932,-0.157345],1],[],["TargetingPodTarget",[0,-0.168182],1],["TargetingPodTarget",[0,-0.151364],1],[]]
                    },
                    # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Draw|TargetingPodTarget|Triangle [Indent level: 5],
                    "triangle": {
                        "type": "line",
                        "width": 9,
                        "points": [["TargetingPodTarget",1,["HorizonBankReverted",0,0.192],1],["TargetingPodTarget",1,["HorizonBankReverted",0.01,0.177],1],["TargetingPodTarget",1,["HorizonBankReverted",-0.01,0.177],1],["TargetingPodTarget",1,["HorizonBankReverted",0,0.192],1]]
                    },
                    # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Draw|TargetingPodTarget|LaunchAutorization [Indent level: 5],
                    "launchautorization": {
                        "type": "line",
                        "width": 14,
                        "points": [["TargetingPodTarget",[0,-0.172386],1],["UserRot1",[0,0.205],1,"TargetingPodTarget",1],["UserRot2",[0,0.205],1,"TargetingPodTarget",1],["UserRot3",[0,0.205],1,"TargetingPodTarget",1],["UserRot4",[0,0.205],1,"TargetingPodTarget",1],["UserRot5",[0,0.205],1,"TargetingPodTarget",1],["UserRot6",[0,0.205],1,"TargetingPodTarget",1]]
                    },
                    # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Draw|TargetingPodTarget|LaunchAutorizationBig [Indent level: 5],
                    "launchautorizationbig": {
                        "type": "line",
                        "width": 24,
                        "points": [["UserRot1",[0,0.215],1,"TargetingPodTarget",1],["UserRot2",[0,0.215],1,"TargetingPodTarget",1],["UserRot3",[0,0.215],1,"TargetingPodTarget",1],["UserRot4",[0,0.215],1,"TargetingPodTarget",1],["UserRot5",[0,0.215],1,"TargetingPodTarget",1]]
                    }
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Draw|StaticReticle [Indent level: 4],
                "staticreticle": {
                    "condition": "user5",
                    # Class: CfgVehicles|RHS_su25_base|MFD|AirplaneHUD|Draw|StaticReticle|Shape [Indent level: 5],
                    "shape": {
                        "type": "polygon",
                        "texture": "rhsafrf|addons|rhs_c_a2port_air|Su25|rhs_su25_reticle_static_ca.paa",
                        "points": [[[[0.055,0.145],1],[[0.955,0.145],1],[[0.955,0.845],1],[[0.055,0.845],1]]]
                    }
                }
            }
        },
        # Class: CfgVehicles|RHS_su25_base|MFD|MFD_1 [Indent level: 2],
        "mfd_1": {
            "topleft": "MFD_WS_TL",
            "topright": "MFD_WS_TR",
            "bottomleft": "MFD_WS_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0.15,1,0.15,1],
            "enableparallax": 0,
            "font": "PuristaMedium",
            # Class: CfgVehicles|RHS_su25_base|MFD|MFD_1|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|RHS_su25_base|MFD|MFD_1|Draw [Indent level: 3],
            "draw": {
                "alpha": 0.5,
                "color": [1,1,1],
                # Class: CfgVehicles|RHS_su25_base|MFD|MFD_1|Draw|MgunAmmo [Indent level: 4],
                "mgunammo": {
                    "condition": "ammo2>=1",
                    # Class: CfgVehicles|RHS_su25_base|MFD|MFD_1|Draw|MgunAmmo|BlackBackground [Indent level: 5],
                    "blackbackground": {
                        "color": [0,0,0],
                        "alpha": 1,
                        # Class: CfgVehicles|RHS_su25_base|MFD|MFD_1|Draw|MgunAmmo|BlackBackground|AmmoBox [Indent level: 6],
                        "ammobox": {
                            "type": "polygon",
                            "width": 4,
                            "points": [[[[0.838,0.825],1],[[0.922,0.825],1],[[0.922,0.975],1],[[0.838,0.975],1]]]
                        }
                    },
                    # Class: CfgVehicles|RHS_su25_base|MFD|MFD_1|Draw|MgunAmmo|Full [Indent level: 5],
                    "full": {
                        "condition": "ammo2>=212",
                        # Class: CfgVehicles|RHS_su25_base|MFD|MFD_1|Draw|MgunAmmo|Full|AmmoText [Indent level: 6],
                        "ammotext": {
                            "type": "text",
                            "source": "static",
                            "text": "К",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "center",
                            "pos": [[0.875,0.82],1],
                            "right": [[0.91,0.82],1],
                            "down": [[0.875,0.96],1]
                        }
                    },
                    # Class: CfgVehicles|RHS_su25_base|MFD|MFD_1|Draw|MgunAmmo|AlmostFull [Indent level: 5],
                    "almostfull": {
                        "condition": "(ammo2>=137)*(ammo2<=211)",
                        # Class: CfgVehicles|RHS_su25_base|MFD|MFD_1|Draw|MgunAmmo|AlmostFull|AmmoText [Indent level: 6],
                        "ammotext": {
                            "type": "text",
                            "source": "static",
                            "text": "3/4",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "center",
                            "pos": [[0.875,0.82],1],
                            "right": [[0.91,0.82],1],
                            "down": [[0.875,0.96],1]
                        }
                    },
                    # Class: CfgVehicles|RHS_su25_base|MFD|MFD_1|Draw|MgunAmmo|Half [Indent level: 5],
                    "half": {
                        "condition": "(ammo2>=63)*(ammo2<=136)",
                        # Class: CfgVehicles|RHS_su25_base|MFD|MFD_1|Draw|MgunAmmo|Half|AmmoText [Indent level: 6],
                        "ammotext": {
                            "type": "text",
                            "source": "static",
                            "text": "1/2",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "center",
                            "pos": [[0.875,0.82],1],
                            "right": [[0.91,0.82],1],
                            "down": [[0.875,0.96],1]
                        }
                    },
                    # Class: CfgVehicles|RHS_su25_base|MFD|MFD_1|Draw|MgunAmmo|AlmostEmpty [Indent level: 5],
                    "almostempty": {
                        "condition": "(ammo2<=62)",
                        # Class: CfgVehicles|RHS_su25_base|MFD|MFD_1|Draw|MgunAmmo|AlmostEmpty|AmmoText [Indent level: 6],
                        "ammotext": {
                            "type": "text",
                            "source": "static",
                            "text": "1/4",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "center",
                            "pos": [[0.875,0.82],1],
                            "right": [[0.91,0.82],1],
                            "down": [[0.875,0.96],1]
                        }
                    }
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|MFD_1|Draw|WeaponTypeRocket [Indent level: 4],
                "weapontyperocket": {
                    "condition": "rocket",
                    # Class: CfgVehicles|RHS_su25_base|MFD|MFD_1|Draw|WeaponTypeRocket|BlackBackground [Indent level: 5],
                    "blackbackground": {
                        "color": [0,0,0],
                        "alpha": 1,
                        # Class: CfgVehicles|RHS_su25_base|MFD|MFD_1|Draw|WeaponTypeRocket|BlackBackground|AmmoBox [Indent level: 6],
                        "ammobox": {
                            "type": "polygon",
                            "width": 4,
                            "points": [[[[0.838,0.125],1],[[0.922,0.125],1],[[0.922,0.275],1],[[0.838,0.275],1]]]
                        }
                    },
                    # Class: CfgVehicles|RHS_su25_base|MFD|MFD_1|Draw|WeaponTypeRocket|AmmoText [Indent level: 5],
                    "ammotext": {
                        "type": "text",
                        "source": "static",
                        "text": "НРС",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": [[0.875,0.11],1],
                        "right": [[0.91,0.11],1],
                        "down": [[0.875,0.25],1]
                    }
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|MFD_1|Draw|WeaponTypeMissiles [Indent level: 4],
                "weapontypemissiles": {
                    "condition": "missile",
                    # Class: CfgVehicles|RHS_su25_base|MFD|MFD_1|Draw|WeaponTypeMissiles|BlackBackground [Indent level: 5],
                    "blackbackground": {
                        # Class: CfgVehicles|RHS_su25_base|MFD|MFD_1|Draw|WeaponTypeMissiles|BlackBackground|AmmoBox [Indent level: 6]
                        "ammobox": {
                            "type": "polygon",
                            "width": 4,
                            "points": [[[[0.838,0.125],1],[[0.922,0.125],1],[[0.922,0.275],1],[[0.838,0.275],1]]]
                        },
                        "color": [0,0,0],
                        "alpha": 1
                    },
                    # Class: CfgVehicles|RHS_su25_base|MFD|MFD_1|Draw|WeaponTypeMissiles|AmmoText [Indent level: 5],
                    "ammotext": {
                        "type": "text",
                        "source": "static",
                        "text": "УР",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": [[0.875,0.11],1],
                        "right": [[0.91,0.11],1],
                        "down": [[0.875,0.25],1]
                    }
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|MFD_1|Draw|WeaponTypeBombs [Indent level: 4],
                "weapontypebombs": {
                    "condition": "bomb",
                    # Class: CfgVehicles|RHS_su25_base|MFD|MFD_1|Draw|WeaponTypeBombs|BlackBackground [Indent level: 5],
                    "blackbackground": {
                        # Class: CfgVehicles|RHS_su25_base|MFD|MFD_1|Draw|WeaponTypeBombs|BlackBackground|AmmoBox [Indent level: 6]
                        "ammobox": {
                            "type": "polygon",
                            "width": 4,
                            "points": [[[[0.838,0.125],1],[[0.922,0.125],1],[[0.922,0.275],1],[[0.838,0.275],1]]]
                        },
                        "color": [0,0,0],
                        "alpha": 1
                    },
                    # Class: CfgVehicles|RHS_su25_base|MFD|MFD_1|Draw|WeaponTypeBombs|AmmoText [Indent level: 5],
                    "ammotext": {
                        "type": "text",
                        "source": "static",
                        "text": "Б",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": [[0.875,0.11],1],
                        "right": [[0.91,0.11],1],
                        "down": [[0.875,0.25],1]
                    }
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|MFD_1|Draw|WeaponTypeMgun [Indent level: 4],
                "weapontypemgun": {
                    "condition": "mgun",
                    # Class: CfgVehicles|RHS_su25_base|MFD|MFD_1|Draw|WeaponTypeMgun|BlackBackground [Indent level: 5],
                    "blackbackground": {
                        # Class: CfgVehicles|RHS_su25_base|MFD|MFD_1|Draw|WeaponTypeMgun|BlackBackground|AmmoBox [Indent level: 6]
                        "ammobox": {
                            "type": "polygon",
                            "width": 4,
                            "points": [[[[0.838,0.125],1],[[0.922,0.125],1],[[0.922,0.275],1],[[0.838,0.275],1]]]
                        },
                        "color": [0,0,0],
                        "alpha": 1
                    },
                    # Class: CfgVehicles|RHS_su25_base|MFD|MFD_1|Draw|WeaponTypeMgun|AmmoText [Indent level: 5],
                    "ammotext": {
                        "type": "text",
                        "source": "static",
                        "text": "ВПУ",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": [[0.875,0.11],1],
                        "right": [[0.91,0.11],1],
                        "down": [[0.875,0.25],1]
                    }
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|MFD_1|Draw|Pylon1 [Indent level: 4],
                "pylon1": {
                    "type": "pylonicon",
                    "pos": [[0.345,0.34],1],
                    "pylon": 1,
                    "name": "rhs_su25_box"
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|MFD_1|Draw|Pylon2 [Indent level: 4],
                "pylon2": {
                    "pylon": 2,
                    "pos": [[0.405,0.32],1],
                    "type": "pylonicon",
                    "name": "rhs_su25_box"
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|MFD_1|Draw|Pylon3 [Indent level: 4],
                "pylon3": {
                    "pylon": 3,
                    "pos": [[0.281,0.32],1],
                    "type": "pylonicon",
                    "name": "rhs_su25_box"
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|MFD_1|Draw|Pylon4 [Indent level: 4],
                "pylon4": {
                    "pylon": 4,
                    "pos": [[0.469,0.32],1],
                    "type": "pylonicon",
                    "name": "rhs_su25_box"
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|MFD_1|Draw|Pylon5 [Indent level: 4],
                "pylon5": {
                    "pylon": 5,
                    "pos": [[0.217,0.32],1],
                    "type": "pylonicon",
                    "name": "rhs_su25_box"
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|MFD_1|Draw|Pylon6 [Indent level: 4],
                "pylon6": {
                    "pylon": 6,
                    "pos": [[0.533,0.32],1],
                    "type": "pylonicon",
                    "name": "rhs_su25_box"
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|MFD_1|Draw|Pylon7 [Indent level: 4],
                "pylon7": {
                    "pylon": 7,
                    "pos": [[0.153,0.32],1],
                    "type": "pylonicon",
                    "name": "rhs_su25_box"
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|MFD_1|Draw|Pylon8 [Indent level: 4],
                "pylon8": {
                    "pylon": 8,
                    "pos": [[0.597,0.32],1],
                    "type": "pylonicon",
                    "name": "rhs_su25_box"
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|MFD_1|Draw|Pylon9 [Indent level: 4],
                "pylon9": {
                    "pylon": 9,
                    "pos": [[0.094,0.32],1],
                    "type": "pylonicon",
                    "name": "rhs_su25_box"
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|MFD_1|Draw|Pylon10 [Indent level: 4],
                "pylon10": {
                    "pylon": 10,
                    "pos": [[0.661,0.32],1],
                    "type": "pylonicon",
                    "name": "rhs_su25_box"
                }
            }
        },
        # Class: CfgVehicles|RHS_su25_base|MFD|MFD_2 [Indent level: 2],
        "mfd_2": {
            "topleft": "MFD_Lights_TL",
            "topright": "MFD_Lights_TR",
            "bottomleft": "MFD_Lights_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0.15,1,0.15,1],
            "enableparallax": 0,
            # Class: CfgVehicles|RHS_su25_base|MFD|MFD_2|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|RHS_su25_base|MFD|MFD_2|Draw [Indent level: 3],
            "draw": {
                "alpha": 1,
                "color": [1,1,1],
                # Class: CfgVehicles|RHS_su25_base|MFD|MFD_2|Draw|Launch_Authorized [Indent level: 4],
                "launch_authorized": {
                    "condition": "((impactDistance/LarTop)>=LarAmmoMin)*((impactDistance/LarTop)<=LarAmmoMax)+(user1>=1)+missilelocked",
                    "color": [0.69,0.22,0],
                    "alpha": 0.2,
                    # Class: CfgVehicles|RHS_su25_base|MFD|MFD_2|Draw|Launch_Authorized|Bulb [Indent level: 5],
                    "bulb": {
                        "type": "polygon",
                        "texture": "a3|Data_f|light_flare_ca.paa",
                        "points": [[[[0.898,0.085],1],[[0.982,0.085],1],[[0.982,0.515],1],[[0.898,0.515],1]]]
                    }
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|MFD_2|Draw|Laser_Active [Indent level: 4],
                "laser_active": {
                    "color": [0,0.49,0],
                    "alpha": 0.1,
                    "condition": "laseron",
                    # Class: CfgVehicles|RHS_su25_base|MFD|MFD_2|Draw|Laser_Active|Bulb [Indent level: 5],
                    "bulb": {
                        "type": "polygon",
                        "texture": "a3|Data_f|light_flare_ca.paa",
                        "points": [[[[0.018,0.085],1],[[0.102,0.085],1],[[0.102,0.515],1],[[0.018,0.515],1]]]
                    }
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|MFD_2|Draw|Laser_Cooldown [Indent level: 4],
                "laser_cooldown": {
                    "condition": "user0",
                    "blinkingpattern": [0.3,0.3],
                    "blinkingstartson": 1,
                    # Class: CfgVehicles|RHS_su25_base|MFD|MFD_2|Draw|Laser_Cooldown|Bulb [Indent level: 5],
                    "bulb": {
                        "type": "polygon",
                        "texture": "a3|Data_f|light_flare_ca.paa",
                        "points": [[[[0.018,0.085],1],[[0.102,0.085],1],[[0.102,0.515],1],[[0.018,0.515],1]]]
                    },
                    "color": [0,0.49,0],
                    "alpha": 0.1
                },
                # Class: CfgVehicles|RHS_su25_base|MFD|MFD_2|Draw|Launch_Disengage [Indent level: 4],
                "launch_disengage": {
                    "condition": "(((impactDistance/LarTop)<=LarAmmoMin)+((impactDistance/LarTop)>=LarAmmoMax))*rocket+(user1<=-1)",
                    "color": [0.94,0.01,0],
                    "alpha": 0.07,
                    # Class: CfgVehicles|RHS_su25_base|MFD|MFD_2|Draw|Launch_Disengage|Bulb [Indent level: 5],
                    "bulb": {
                        "type": "polygon",
                        "texture": "a3|Data_f|light_flare_ca.paa",
                        "points": [[[[0.018,0.485],1],[[0.102,0.485],1],[[0.102,0.915],1],[[0.018,0.915],1]]]
                    }
                }
            }
        }
    },
    "maxomega": 2000,
    "enginemoi": 16,
    # Class: CfgVehicles|RHS_su25_base|Wheels [Indent level: 1],
    "wheels": {
        "disablewheelswhendestroyed": 1,
        # Class: CfgVehicles|RHS_su25_base|Wheels|Wheel_1 [Indent level: 2],
        "wheel_1": {
            "side": "left",
            "bonename": "Wheel_1",
            "center": "Wheel_1_center",
            "boundary": "Wheel_1_rim",
            "suspforceapppointoffset": "Wheel_1_center",
            "tireforceapppointoffset": "Wheel_1_center",
            "susptraveldirection": [0,-1,0],
            "steering": 1,
            "width": 0.16,
            "mass": 150,
            "moi": 40,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 21500,
            "maxhandbraketorque": 0,
            "maxcompression": 0.2105,
            "maxdroop": 0.015,
            "sprungmass": 4066,
            "springstrength": 56600,
            "springdamperrate": 215570,
            "longitudinalstiffnessperunitgravity": 8000,
            "latstiffx": 25,
            "latstiffy": 180,
            "frictionvsslipgraph": [[0,1],[0.5,1],[1,1]]
        },
        # Class: CfgVehicles|RHS_su25_base|Wheels|Wheel_1_fake [Indent level: 2],
        "wheel_1_fake": {
            "side": "left",
            "bonename": "Wheel_1",
            "center": "Wheel_1_center",
            "boundary": "Wheel_1_rim",
            "suspforceapppointoffset": "Wheel_1_center",
            "tireforceapppointoffset": "Wheel_1_center",
            "susptraveldirection": [0,-1,0],
            "steering": 1,
            "width": 0.16,
            "mass": 150,
            "moi": 40,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 21500,
            "maxhandbraketorque": 0,
            "maxcompression": 0.2105,
            "maxdroop": 0.015,
            "sprungmass": 4066,
            "springstrength": 56600,
            "springdamperrate": 215570,
            "longitudinalstiffnessperunitgravity": 8000,
            "latstiffx": 25,
            "latstiffy": 180,
            "frictionvsslipgraph": [[0,1],[0.5,1],[1,1]]
        },
        # Class: CfgVehicles|RHS_su25_base|Wheels|Wheel_2 [Indent level: 2],
        "wheel_2": {
            "bonename": "Wheel_2",
            "steering": 0,
            "center": "Wheel_2_center",
            "boundary": "Wheel_2_rim",
            "width": 0.28,
            "springdamperrate": 220570,
            "sprungmass": 6652,
            "springstrength": 151000,
            "suspforceapppointoffset": "Wheel_2_center",
            "tireforceapppointoffset": "Wheel_2_center",
            "side": "left",
            "susptraveldirection": [0,-1,0],
            "mass": 150,
            "moi": 40,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 21500,
            "maxhandbraketorque": 0,
            "maxcompression": 0.2105,
            "maxdroop": 0.015,
            "longitudinalstiffnessperunitgravity": 8000,
            "latstiffx": 25,
            "latstiffy": 180,
            "frictionvsslipgraph": [[0,1],[0.5,1],[1,1]]
        },
        # Class: CfgVehicles|RHS_su25_base|Wheels|Wheel_3 [Indent level: 2],
        "wheel_3": {
            "bonename": "Wheel_3",
            "side": "right",
            "center": "Wheel_3_center",
            "boundary": "Wheel_3_rim",
            "suspforceapppointoffset": "Wheel_3_center",
            "tireforceapppointoffset": "Wheel_3_center",
            "steering": 0,
            "width": 0.28,
            "springdamperrate": 220570,
            "sprungmass": 6652,
            "springstrength": 151000,
            "susptraveldirection": [0,-1,0],
            "mass": 150,
            "moi": 40,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 21500,
            "maxhandbraketorque": 0,
            "maxcompression": 0.2105,
            "maxdroop": 0.015,
            "longitudinalstiffnessperunitgravity": 8000,
            "latstiffx": 25,
            "latstiffy": 180,
            "frictionvsslipgraph": [[0,1],[0.5,1],[1,1]]
        }
    },
    "maxspeed": 900,
    "landingaoa": 0.113446,
    "landingspeed": 250,
    "stallspeed": 190,
    "stallwarningtreshold": 0.07,
    "wheelsteeringsensitivity": 1.3,
    "airbrake": 1,
    "airbrakefrictioncoef": 2.2,
    "flaps": 1,
    "flapsfrictioncoef": 0.32,
    "gearsupfrictioncoef": 0.55,
    "airfrictioncoefs0": [0,0,0],
    "airfrictioncoefs1": [0.1,0.52,0.0067],
    "airfrictioncoefs2": [0.001,0.0054,7e-005],
    "angleofindicence": -0.00872665,
    "envelope": [0,0.07,0.28,0.83,1.11,1.74,2.51,3.41,4.46,5.64,6.96,8.42,8.8,9.11,9.38,9.45,9.43,9,8,7,6],
    "altnoforce": 15000,
    "altfullforce": 4000,
    "thrustcoef": [1.28,1.33,1.77,1.4,1.41,1.39,1.36,1.33,1.29,1.25,1.2,1.15,1.05,0.5,0,0,0,0,0],
    "aileronsensitivity": 0.85,
    "aileroncoef": [0,0.1,0.3,0.6,0.8,0.95,1,1.02,1.03,1.04,1.04,1,0.9,0.7,0.3,0.2,0.15,0.1,0.1],
    "elevatorsensitivity": 0.95,
    "elevatorcoef": [0,0.2,0.95,0.8,0.75,0.7,0.65,0.6,0.55,0.5,0.46,0.32,0.29,0.16,0.14,0.12,0.1,0.09,0.08],
    "rudderinfluence": 0.966,
    "ruddercoef": [0,0.6,1.2,1.5,1.8,2,3.2,3.4,3.45,3.5,3.55,3.6,2.2,1.3,0.3,0.2,0.15,0.1,0.1],
    "aileroncontrolssensitivitycoef": 3.6,
    "elevatorcontrolssensitivitycoef": 3.4,
    "ruddercontrolssensitivitycoef": 3.4,
    "draconicforcexcoef": 13,
    "draconicforceycoef": 1.3,
    "draconicforcezcoef": 1,
    "draconictorquexcoef": [4.8,5,5.5,6.2,6.6,7.4,8,8.5,8,8.4,8.6,8.7,8.8,8.9,9,9.1],
    "draconictorqueycoef": [12,7.5,4,1.5,0.1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    "soundincommingmissile": ["|rhsafrf|addons|rhs_c_a2port_air|sounds|alarm_beep",1.09811,1],
    "soundlocked": ["",1.58489,1],
    # Class: CfgVehicles|RHS_su25_base|UserActions [Indent level: 1],
    "useractions": {
        # Class: CfgVehicles|RHS_su25_base|UserActions|SAFEMODE [Indent level: 2]
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
        },
        # Class: CfgVehicles|RHS_su25_base|UserActions|RETICLE [Indent level: 2],
        "reticle": {
            "displayname": "<t color='#FBB829'>Toggle reticle</t>",
            "position": "",
            "radius": 10,
            "priority": 10.5,
            "onlyforplayer": 1,
            "showwindow": 0,
            "hideonuse": 1,
            "condition": "(call rhs_fnc_findPlayer) in this",
            "shortcut": "user10",
            "statement": "if(((getUserMFDvalue this) select 5) isEqualTo 0)then{this setUserMFDvalue [5,1];}else{this setUserMFDvalue [5,0];};"
        }
    },
    # Class: CfgVehicles|RHS_su25_base|EventHandlers [Indent level: 1],
    "eventhandlers": {
        "hit": "",
        # Class: CfgVehicles|RHS_su25_base|EventHandlers|RHS_EventHandlers [Indent level: 2],
        "rhs_eventhandlers": {
            "hit": "_this call RHS_fnc_AI_eject",
            "init": "_this call rhs_fnc_air_init",
            "getout": "[_this select 0, _this select 2,'rhs_su25_canopy'] call rhs_fnc_K36D_seatEjection",
            "engine": "[_this select 0,_this select 1,10] call rhs_fnc_engineStartupDelay;_this call rhs_fnc_addParachutes;"
        },
        "init": "",
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');",
        # Class: DefaultEventHandlers|RHS_DefaultEventhandlers [Indent level: 0],
        "rhs_defaulteventhandlers": {
            "hitpart": "_this call rhs_fnc_hitPart"
        }
    },
    "author": "Bohemia Interactive",
    # Class: CfgVehicles|O_Plane_CAS_02_F|SimpleObject [Indent level: 1],
    "simpleobject": {
        "eden": 0,
        "animate": [["airintake_1_front_rot",0.07],["airintake_2_front_rot",0.07],["airintake_1_top_1_rot",0.07],["airintake_2_top_1_rot",0.07],["airintake_1_top_2_move",0.07],["airintake_2_top_2_move",0.07],["rotor_1_1_rot",0],["rotor_1_2_rot",0],["rotor_2_1_rot",0],["rotor_2_2_rot",0],["aileron_1_rot_1",0],["aileron_2_rot_1",0],["airbrake_rot_1",0],["airbrake_piston_1_move_1",0],["airbrake_piston_2_rot_1",0],["elevator_1_rot",0],["elevator_2_rot",0],["flap_1_rot",0],["flap_2_rot",0],["slat_1_1_rot",0],["slat_1_2_rot",0],["slat_2_1_rot",0],["slat_2_2_rot",0],["rudder_rot",0],["wheel_1_rot",0],["wheel_2_rot",0],["wheel_3_rot",0],["gear_1_rot",0],["gear_1_hatch_1_rot",0],["gear_1_hatch_2_rot",0],["gear_1_hatch_3_rot",0],["gear_1_hatch_4_rot",0],["gear_1_hatch_5_rot",0],["gear_1_steering_rot",0],["gear_1_damper_move",0],["gear_1_stabil_1_rot",0],["gear_1_stabil_2_rot",0],["gear_2_rot",0],["gear_2_hatch_1_rot",0],["gear_2_hatch_2_rot",0],["gear_2_hatch_3_rot",0],["gear_2_piston_1_rot",0],["gear_2_stabil_1_rot",0],["gear_2_stabil_2_rot",0],["gear_2_damper_move",0],["gear_3_rot",0],["gear_3_hatch_1_rot",0],["gear_3_hatch_2_rot",0],["gear_3_hatch_3_rot",0],["gear_3_piston_1_rot",0],["gear_3_stabil_1_rot",0],["gear_3_stabil_2_rot",0],["gear_3_damper_move",0],["canopy_rot",0],["ladder_hatch_l_rot",0],["ladder_hatch_r_rot",0],["display_off_hide",0],["avionics_damage",0],["display_cannon_rot",1],["display_cannon_rot_1",0],["display_cannon_rot_2",0],["display_missile_aa_1_rot",1],["display_missile_aa_1_rot_1",0],["display_missile_aa_1_rot_2",0],["display_missile_aa_2_rot",1],["display_missile_aa_2_rot_1",0],["display_missile_aa_2_rot_2",0],["display_missile_agm_2_1_rot",1],["display_missile_agm_2_1_rot_1",0],["display_missile_agm_2_1_rot_2",0],["display_missile_agm_1_1_rot",1],["display_missile_agm_1_1_rot_1",0],["display_missile_agm_1_1_rot_2",0],["display_missile_agm_2_2_rot",1],["display_missile_agm_2_2_rot_1",0],["display_missile_agm_2_2_rot_2",0],["display_missile_agm_1_2_rot",1],["display_missile_agm_1_2_rot_1",0],["display_missile_agm_1_2_rot_2",0],["display_rocketpod_2_rot",1],["display_rocketpod_2_rot_1",0],["display_rocketpod_2_rot_2",0],["display_rocketpod_1_rot",1],["display_rocketpod_1_rot_1",0],["display_rocketpod_1_rot_2",0],["display_bomb_1_rot",1],["display_bomb_1_rot_1",0],["display_bomb_1_rot_2",0],["display_bomb_2_rot",1],["display_bomb_2_rot_1",0],["display_bomb_2_rot_2",0],["display_cannon_slider_move",1],["display_rocketpod_1_slider_move",1],["display_rocketpod_2_slider_move",1],["display_horizon_rot_1",-0.03],["display_horizon_rot_2",0],["display_speed_rot",0],["display_compass_rot",0],["display_altitude_large_rot",7.98],["display_altitude_small_rot",7.98],["display_climb_rot",0],["display_engine_1_rot",0],["display_engine_2_rot",0],["display_engine_1_slider_move",0],["display_engine_2_slider_move",0],["display_gear_down_move",0],["display_gear_up_move",0],["controlstick_pitch_rot",0],["controlstick_roll_rot",0],["compass_rot",0],["cannon_muzzleflash_rot",514],["positionlights",0],["collisionlight_red_blinking",0],["pilotcamera_h",0],["pilotcamera_v",0.26],["unhidemfd",0]],
        "hide": ["clan","cannon_muzzleflash","gear_2_light_1_hide","gear_2_light_2_hide","gear_3_light_1_hide","gear_3_light_2_hide","gear_1_light_1_hide","gear_1_light_2_hide","zadni svetlo","podsvit pristroju","poskozeni"],
        "verticaloffset": 2.872,
        "verticaloffsetworld": -0.108,
        "init": "[this, '', []] call bis_fnc_initVehicle"
    },
    "_generalmacro": "O_Plane_CAS_02_F",
    "features": "Randomization: No						<br />Camo selections: 2 - the main body, wings lower part of body						<br />Script door sources: None						<br />Script animations: None						<br />Executed scripts: None 						<br />Firing from vehicles: No						<br />Slingload: Slingloadable						<br />Cargo proxy indexes: None",
    "editorsubcategory": "EdSubcat_Planes",
    "destrtype": "DestructWreck",
    "memorypointtaskmarker": "TaskMarker_1_pos",
    "slingloadcargomemorypoints": ["SlingLoadCargo1","SlingLoadCargo2","SlingLoadCargo3","SlingLoadCargo4"],
    # Class: CfgVehicles|Plane_CAS_02_base_F|Library [Indent level: 1],
    "library": {
        "libtextdesc": "The To-199 Neophron is a new addition to CSAT air forces. An agile single-seat aircraft is used for close air support but can also take down air threats. It cannot carry as much payload as NATO's A-164 and has to rearm more often, but it can take-off from even the roughest terrain, not being so dependent on air bases or aircraft carriers. Neophron in CAS variant is fitted with 30 mm Cannon, Sahr-3 short range air-to-air missiles, Sharur air-to-ground missiles, Tratnyr rockets (HE and AP variants) and LOM-250G bombs."
    },
    "getinaction": "pilot_plane_cas_02_Enter",
    "getoutaction": "pilot_plane_cas_02_Exit",
    "precisegetinout": 1,
    "viewdrivershadowdiff": 0.5,
    "viewdrivershadowamb": 0.5,
    # Class: CfgVehicles|Plane_CAS_02_base_F|Turrets [Indent level: 1],
    "turrets": {
    },
    # Class: CfgVehicles|Plane_CAS_02_base_F|TransportItems [Indent level: 1],
    "transportitems": {
    },
    "attenuationeffecttype": "PlaneAttenuation",
    "soundgetin": ["A3|Sounds_F_EPC|CAS_02|TO_getin",1,1],
    "soundgetout": ["A3|Sounds_F_EPC|CAS_02|getout",1,1,40],
    "cabinopensound": ["A3|Sounds_F|air|noises|Plane_CAS02_CabinOpen",3.16228,1,40],
    "cabinclosesound": ["A3|Sounds_F|air|noises|Plane_CAS02_CabinClose",3.16228,1,40],
    "cabinopensoundinternal": ["A3|Sounds_F|air|noises|Plane_CAS02_CabinOpen",10,1,40],
    "cabinclosesoundinternal": ["A3|Sounds_F|air|noises|Plane_CAS02_CabinClose",10,1,40],
    "sounddammage": ["",0.562341,1],
    "soundengineonint": ["A3|Sounds_F_EPC|CAS_02|CAS_02_start_int",0.794328,1],
    "soundengineonext": ["A3|Sounds_F_EPC|CAS_02|CAS_02_start_ext",1,1,500],
    "soundengineoffint": ["A3|Sounds_F_EPC|CAS_02|CAS_02_stop_int",0.794328,1],
    "soundengineoffext": ["A3|Sounds_F_EPC|CAS_02|CAS_02_stop_ext",1,1,500],
    "soundgearup": ["A3|Sounds_F_EPC|CAS_02|gear_up",0.794328,1,150],
    "soundgeardown": ["A3|Sounds_F_EPC|CAS_02|gear_down",0.794328,1,150],
    "soundflapsup": ["A3|Sounds_F_EPC|CAS_02|Flaps_Up",0.630957,1,100],
    "soundflapsdown": ["A3|Sounds_F_EPC|CAS_02|Flaps_Down",0.630957,1,100],
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
    # Class: CfgVehicles|Plane_CAS_02_base_F|scrubLandInt [Indent level: 1],
    "scrublandint": {
        "sound": ["A3|Sounds_F|vehicles|air|noises|wheelsInt",1,1,100],
        "frequency": 1,
        "volume": "(scrubLand factor[0.01, 0.20])"
    },
    # Class: CfgVehicles|Plane_CAS_02_base_F|Sounds [Indent level: 1],
    "sounds": {
        # Class: CfgVehicles|Plane_CAS_02_base_F|Sounds|EngineLowOut [Indent level: 2]
        "enginelowout": {
            "sound": ["A3|Sounds_F_EPC|CAS_02|CAS_02_engine_idle_ext",1,1,2100],
            "frequency": "1.0 min (rpm + 0.5)",
            "volume": "camPos*2*(rpm factor[0.95, 0])*(rpm factor[0, 0.95])"
        },
        # Class: CfgVehicles|Plane_CAS_02_base_F|Sounds|EngineHighOut [Indent level: 2],
        "enginehighout": {
            "sound": ["A3|Sounds_F_EPC|CAS_02|CAS_02_engine_max_ext",1,1.2,2500],
            "frequency": "1",
            "volume": "camPos*4*(rpm factor[0.5, 1.1])*(rpm factor[1.1, 0.5])"
        },
        # Class: CfgVehicles|Plane_CAS_02_base_F|Sounds|ForsageOut [Indent level: 2],
        "forsageout": {
            "sound": ["A3|Sounds_F_EPC|CAS_02|CAS_02_forsage_ext",1.41254,1.2,2800],
            "frequency": "1",
            "volume": "engineOn*camPos*(thrust factor[0.6, 1.0])",
            "cone": [3.14,3.92,2,0.5]
        },
        # Class: CfgVehicles|Plane_CAS_02_base_F|Sounds|WindNoiseOut [Indent level: 2],
        "windnoiseout": {
            "sound": ["A3|Sounds_F_EPC|CAS_02|noise",0.562341,1,150],
            "frequency": "(0.1+(1.2*(speed factor[1, 150])))",
            "volume": "camPos*(speed factor[1, 150])"
        },
        # Class: CfgVehicles|Plane_CAS_02_base_F|Sounds|EngineLowIn [Indent level: 2],
        "enginelowin": {
            "sound": ["A3|Sounds_F_EPC|CAS_02|CAS_02_engine_idle_int",0.562341,1],
            "frequency": "1.0 min (rpm + 0.5)",
            "volume": "(1-camPos)*((rpm factor[0.7, 0.1])*(rpm factor[0.1, 0.7]))"
        },
        # Class: CfgVehicles|Plane_CAS_02_base_F|Sounds|EngineHighIn [Indent level: 2],
        "enginehighin": {
            "sound": ["A3|Sounds_F_EPC|CAS_02|CAS_02_engine_max_int",0.316228,1.2],
            "frequency": "1",
            "volume": "(1-camPos)*(rpm factor[0.85, 1.0])"
        },
        # Class: CfgVehicles|Plane_CAS_02_base_F|Sounds|ForsageIn [Indent level: 2],
        "forsagein": {
            "sound": ["A3|Sounds_F_EPC|CAS_02|CAS_02_forsage_int",0.501187,1.2],
            "frequency": "1",
            "volume": "(1-camPos)*(engineOn*(thrust factor[0.6, 1.0]))"
        },
        # Class: CfgVehicles|Plane_CAS_02_base_F|Sounds|WindNoiseIn [Indent level: 2],
        "windnoisein": {
            "sound": ["A3|Sounds_F|air|Plane_Fighter_03|noise_int",0.316228,1],
            "frequency": "(0.1+(1.2*(speed factor[1, 150])))",
            "volume": "(1-camPos)*(speed factor[1, 150])"
        },
        # Class: CfgVehicles|Plane_CAS_02_base_F|Sounds|RainExt [Indent level: 2],
        "rainext": {
            "sound": ["A3|Sounds_F|vehicles|noises|rain1_ext",1.77828,1,100],
            "frequency": 1,
            "volume": "camPos * rain * (speed factor[50, 0])"
        },
        # Class: CfgVehicles|Plane_CAS_02_base_F|Sounds|RainInt [Indent level: 2],
        "rainint": {
            "sound": ["A3|Sounds_F|vehicles|noises|rain1_int",1,1,100],
            "frequency": 1,
            "volume": "(1-camPos) * rain * (speed factor[50, 0])"
        },
        # Class: CfgVehicles|Plane_CAS_02_base_F|Sounds|Waternoise_ext [Indent level: 2],
        "waternoise_ext": {
            "sound": ["A3|Sounds_F|vehicles|noises|air_driving_in_water",0.707946,1,300],
            "frequency": "1",
            "volume": "(speed factor[0, 5]) * water * camPos + (speed factor[-0.1, -5]) * water * camPos"
        },
        # Class: CfgVehicles|Plane_CAS_02_base_F|Sounds|Waternoise_int [Indent level: 2],
        "waternoise_int": {
            "sound": ["A3|Sounds_F|vehicles|noises|soft_driving_in_water_int",0.562341,1,100],
            "frequency": "1",
            "volume": "(speed factor[0, 5]) * water * (1-camPos) + (speed factor[-0.1, -5]) * water * (1-camPos)"
        }
    },
    "clutchstrength": 100,
    "dampingratefullthrottle": 0.4,
    "irscanrangemin": 500,
    "irscanrangemax": 5000,
    "irscantoeyefactor": 2,
    "laserscanner": 1,
    "showalltargets": 4,
    "minfiretime": 30,
    "gunaimdown": 0,
    "extcameraposition": [0,4.1,-20],
    "cabinopening": 1,
    "explosionshielding": 1,
    "armorlights": 0.1,
    "waterleakiness": 1.5,
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
    "durationgetin": 0.99,
    "durationgetout": 0.99,
    "vtol": 0,
    "tailhook": 0,
    "lightongear": 1,
    "gearuptime": 3.33,
    "geardowntime": 2,
    "cost": 2e+006,
    "simulation": "airplanex",
    "mingunelev": 0,
    "maxgunelev": 0,
    "mingunturn": 0,
    "maxgunturn": 0,
    "vtolyawinfluence": 2,
    "vtolpitchinfluence": 2,
    "vtolrollinfluence": 2,
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
    "textplural": "fast movers",
    "namesound": "veh_air_plane_s",
    "type": 2,
    "fuelexplosionpower": 10,
    "crewcrashprotection": 0.15,
    "damageeffect": "AirDestructionEffects",
    "cargogetinaction": ["GetInHigh"],
    "cargogetoutaction": ["GetOutHigh"],
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
    "mintotaldamagethreshold": 0.005,
    # Class: CfgVehicles|Plane|DestructionEffects [Indent level: 1],
    "destructioneffects": {
    },
    "formationtime": 10,
    "fuelcapacity": 1000,
    "insidesoundcoef": 0.0316228,
    "outsidesoundfilter": 1,
    "occludesoundswhenin": 0.316228,
    "obstructsoundswhenin": 0.316228,
    "nightvision": 0,
    "cargocompartments": [0],
    "enablegps": 1,
    "weaponsgroup2": 4,
    "weaponsgroup3": "8 + 	16 + 	32",
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
    "memorypointsgetincargo": "pos cargo",
    "memorypointsgetincargodir": "pos cargo dir",
    "memorypointsgetincodriver": "pos codriver",
    "memorypointsgetincodriverdir": "pos codriver dir",
    "memorypointsgetincargoprecise": ["pos cargo"],
    "memorypointsleftwatereffect": "waterEffectL",
    "memorypointsrightwatereffect": "waterEffectR",
    "selectionclan": "clan",
    "selectiondashboard": "podsvit pristroju",
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
    "insidedetectcoef": 0.05,
}