put = {
    "scope": 1,
    "value": 0,
    "type": 0,
    "candrop": 0,
    "muzzles": ["DemoChargeMuzzle","PipeBombMuzzle","MineMuzzle","DirectionalMineRemoteMuzzle","ClassicMineRangeMuzzle","BoundingMineRangeMuzzle","DirectionalMineRangeMuzzle","ClassicMineWireMuzzle","APERSMineDispenserMuzzle","TrainingMineMuzzle","Drone_explosive_muzzle","Drone_explosive_muzzle_dummy","Rhs_Mine_Muzzle","Rhsusf_MineMuzzle","rhsusf_m112_muzzle","rhsusf_m112x4_muzzle","Rhs_SmallMine_Muzzle","rhsgref_Mine_Muzzle","Rhssaf_Mine_Muzzle","rhssaf_tm100_muzzle","rhssaf_tm200_muzzle","rhssaf_tm500_muzzle"],
    # Class: CfgWeapons|Put|PutMuzzle [Indent level: 1],
    "putmuzzle": {
        "sound": ["",0.000316228,1],
        "reloadsound": ["",0.000316228,1],
        "enableattack": 0,
        "optics": 0,
        "showempty": 0,
        "canlock": 0,
        "primary": 10,
        "minrange": 0,
        "minrangeprobab": 0.1,
        "midrange": 3,
        "midrangeprobab": 0.9,
        "maxrange": 15,
        "maxrangeprobab": 0.04,
        "movetointernal": 0,
        "opticszoommin": 0.25,
        "opticszoommax": 1.25,
        "opticszoominit": 0.75,
        "access": 3,
        "scope": 0,
        "value": 2,
        "picture": "",
        "uipicture": "",
        "ammo": "",
        "cursor": "",
        "cursoraim": "",
        "cursorsize": 1,
        "showaimcursorinternal": 1,
        "cursoraimon": "",
        "laser": 0,
        "hiddenselections": [],
        "hiddenselectionstextures": [],
        "hiddenunderwaterselections": [],
        "shownunderwaterselections": [],
        "hiddenunderwaterselectionstextures": [],
        "simulation": "Weapon",
        "type": 65536,
        "displayname": "",
        "namesound": "",
        "count": 0,
        "multiplier": 1,
        "burst": 1,
        "magazinereloadtime": 0,
        "reloadtime": 1,
        "magazinereloadswitchphase": 1,
        "soundbegin": ["sound",1],
        "soundbeginwater": ["sound",1],
        "soundclosure": ["sound",1],
        "soundend": ["sound",1],
        "soundloop": ["sound",1],
        "soundcontinuous": 0,
        "weaponsoundeffect": "",
        "soundburst": 1,
        "drysound": ["",1,1],
        "zeroingsound": ["",1,1],
        "changefiremodesound": ["",1,1],
        "reloadmagazinesound": ["",1,1],
        "emptysound": ["",1,1],
        "soundbullet": ["emptySound",1],
        "initspeed": 0,
        "ballisticscomputer": 0,
        "irdistance": 0,
        "irdotintensity": 0.001,
        "dispersion": 0.002,
        "aidispersioncoefx": 1,
        "aidispersioncoefy": 1,
        "lockacquire": 1,
        "ffmagnitude": 0,
        "fffrequency": 1,
        "ffcount": 1,
        # Recoil Array: recoil,
        "recoil": [],
        "recoil": "empty",
        "recoilprone": "",
        "maxrecoilsway": 0.008,
        "swaydecayspeed": 2,
        "model": "",
        "modelspecial": "",
        "modelmagazine": "",
        "muzzlepos": "usti hlavne",
        "muzzleend": "konec hlavne",
        "irlaserpos": "laser pos",
        "irlaserend": "laser dir",
        "cartridgepos": "nabojnicestart",
        "cartridgevel": "nabojniceend",
        "selectionfireanim": "zasleh",
        "memorypointcamera": "eye",
        "firespreadangle": 3,
        "usemodeloptics": 1,
        "opticsid": 0,
        "modeloptics": "",
        "opticsppeffects": [],
        "opticsflare": 1,
        "forceoptics": 0,
        "useasbinocular": 0,
        "opticsdisableperipherialvision": 0.67,
        "distancezoommin": 400,
        "distancezoommax": 400,
        "showswitchaction": 0,
        "autofire": 0,
        "autoreload": 1,
        "showtoplayer": 1,
        "canshootinwater": 0,
        "airateoffire": 5,
        "airateoffiredistance": 500,
        "airateoffiredispersion": 0,
        "firelightduration": 0.05,
        "firelightintensity": 0.2,
        "firelightdiffuse": [0.937,0.631,0.259],
        "firelightambient": [0,0,0],
        # Class: CfgWeapons|Default|Eventhandlers [Indent level: 1],
        "eventhandlers": {
        },
        "backgroundreload": 0,
        "reloadaction": "",
        "muzzles": ["this"],
        "magazines": [],
        "modes": ["this"],
        "useaction": 0,
        "useactiontitle": "",
        "candrop": 1,
        "weaponlockdelay": 0,
        "weaponlocksystem": 0,
        "cmimmunity": 1,
        "weight": 0,
        "handanim": [],
        "lockingtargetsound": ["",0.000316228,2],
        "lockedtargetsound": ["",0.000316228,6],
        "detectrange": 0,
        "artillerydispersion": 1,
        "artillerycharge": 1,
        "fireanims": [],
        # Class: CfgWeapons|Default|Library [Indent level: 1],
        "library": {
            "libtextdesc": ""
        },
        "descriptionshort": "",
        # Class: CfgWeapons|Default|GunFire [Indent level: 1],
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
            "cloudletdensitycoef": -1,
            "interval": -0.01,
            "size": 3,
            "sourcesize": 0.5,
            "timetolive": 0,
            "initt": 4500,
            "deltat": -3000,
            # Class: CfgWeapons|Default|GunFire|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunFire|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [0.82,0.95,0.93,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T1 [Indent level: 3],
                "t1": {
                    "maxt": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T2 [Indent level: 3],
                "t2": {
                    "maxt": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T3 [Indent level: 3],
                "t3": {
                    "maxt": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T4 [Indent level: 3],
                "t4": {
                    "maxt": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T5 [Indent level: 3],
                "t5": {
                    "maxt": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T6 [Indent level: 3],
                "t6": {
                    "maxt": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T7 [Indent level: 3],
                "t7": {
                    "maxt": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T8 [Indent level: 3],
                "t8": {
                    "maxt": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T9 [Indent level: 3],
                "t9": {
                    "maxt": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T10 [Indent level: 3],
                "t10": {
                    "maxt": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T11 [Indent level: 3],
                "t11": {
                    "maxt": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T12 [Indent level: 3],
                "t12": {
                    "maxt": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T13 [Indent level: 3],
                "t13": {
                    "maxt": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T14 [Indent level: 3],
                "t14": {
                    "maxt": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T15 [Indent level: 3],
                "t15": {
                    "maxt": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T16 [Indent level: 3],
                "t16": {
                    "maxt": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T17 [Indent level: 3],
                "t17": {
                    "maxt": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T18 [Indent level: 3],
                "t18": {
                    "maxt": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T19 [Indent level: 3],
                "t19": {
                    "maxt": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T20 [Indent level: 3],
                "t20": {
                    "maxt": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T21 [Indent level: 3],
                "t21": {
                    "maxt": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T22 [Indent level: 3],
                "t22": {
                    "maxt": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgWeapons|Default|GunClouds [Indent level: 1],
        "gunclouds": {
            "access": 0,
            "cloudletgrowup": 0.05,
            "cloudletfadein": 0,
            "cloudletfadeout": 0.1,
            "cloudletduration": 0.05,
            "cloudletalpha": 0.3,
            "cloudletaccy": 0,
            "cloudletminyspeed": -100,
            "cloudletmaxyspeed": 100,
            "interval": -0.02,
            "size": 0.3,
            "sourcesize": 0.02,
            "cloudletanimperiod": 1,
            "cloudletsize": 1,
            "cloudletshape": "cloudletClouds",
            "cloudletcolor": [1,1,1,0],
            "timetolive": 0,
            "initt": 0,
            "deltat": 0,
            # Class: CfgWeapons|Default|GunClouds|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunClouds|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        "texturetype": "default",
        "inertia": 0.5,
        "aimtransitionspeed": 1
    },
    # Class: CfgWeapons|Put|TimeBombMuzzle [Indent level: 1],
    "timebombmuzzle": {
        "displayname": "Charge",
        # Compatible Magazines: magazines parameter (+ inherited),
        "magazines": [
            "democharge_remote_mag","iedurbansmall_remote_mag","iedlandsmall_remote_mag","satchelcharge_remote_mag",
            "iedurbanbig_remote_mag","iedlandbig_remote_mag","atmine_range_mag","claymoredirectionalmine_remote_mag",
            "apersmine_range_mag","apersboundingmine_range_mag","slamdirectionalmine_wire_mag","aperstripmine_wire_mag",
            "apersminedispenser_mag","trainingmine_mag","rhs_mine_pmn2_mag","rhs_mine_tm62m_mag",
            "rhs_mine_msk40p_white_mag","rhs_mine_msk40p_red_mag","rhs_mine_msk40p_green_mag","rhs_mine_msk40p_blue_mag",
            "rhs_mine_sm320_white_mag","rhs_mine_sm320_red_mag","rhs_mine_sm320_green_mag","rhs_mine_ozm72_a_mag",
            "rhs_mine_ozm72_b_mag","rhs_mine_ozm72_c_mag","rhs_ec75_mag","rhs_ec200_mag",
            "rhs_ec400_mag","rhs_ec75_sand_mag","rhs_ec200_sand_mag","rhs_ec400_sand_mag",
            "rhs_mine_m19_mag","rhsusf_mine_m14_mag","rhsusf_mine_m49a1_3m_mag","rhsusf_mine_m49a1_6m_mag",
            "rhsusf_mine_m49a1_10m_mag","rhsusf_m112_mag","rhsusf_m112x4_mag","rhs_mag_mine_pfm1",
            "rhs_mag_mine_ptm1","rhs_mine_smine35_press_mag","rhs_mine_smine35_trip_mag","rhs_mine_smine44_press_mag",
            "rhs_mine_smine44_trip_mag","rhs_mine_glasmine43_hz_mag","rhs_mine_glasmine43_bz_mag","rhs_mine_stockmine43_2m_mag",
            "rhs_mine_stockmine43_4m_mag","rhs_mine_a200_bz_mag","rhs_mine_a200_dz35_mag","rhs_mine_tm43_mag",
            "rhs_mine_m2a3b_press_mag","rhs_mine_m2a3b_trip_mag","rhs_mine_m3_pressure_mag","rhs_mine_mk2_pressure_mag",
            "rhs_mine_m3_tripwire_mag","rhs_mine_mk2_tripwire_mag","rhs_mine_m7a2_mag","rhs_charge_m2tet_x2_mag",
            "rhssaf_mine_pma3_mag","rhssaf_mine_tma4_mag","rhssaf_mine_mrud_a_mag","rhssaf_mine_mrud_b_mag",
            "rhssaf_mine_mrud_c_mag","rhssaf_mine_mrud_d_mag","rhssaf_tm100_mag","rhssaf_tm200_mag",
            "rhssaf_tm500_mag",],
        "enableattack": 1,
        "sound": ["",0.000316228,1],
        "reloadsound": ["",0.000316228,1],
        "optics": 0,
        "showempty": 0,
        "canlock": 0,
        "primary": 10,
        "minrange": 0,
        "minrangeprobab": 0.1,
        "midrange": 3,
        "midrangeprobab": 0.9,
        "maxrange": 15,
        "maxrangeprobab": 0.04,
        "movetointernal": 0,
        "opticszoommin": 0.25,
        "opticszoommax": 1.25,
        "opticszoominit": 0.75,
        "access": 3,
        "scope": 0,
        "value": 2,
        "picture": "",
        "uipicture": "",
        "ammo": "",
        "cursor": "",
        "cursoraim": "",
        "cursorsize": 1,
        "showaimcursorinternal": 1,
        "cursoraimon": "",
        "laser": 0,
        "hiddenselections": [],
        "hiddenselectionstextures": [],
        "hiddenunderwaterselections": [],
        "shownunderwaterselections": [],
        "hiddenunderwaterselectionstextures": [],
        "simulation": "Weapon",
        "type": 65536,
        "namesound": "",
        "count": 0,
        "multiplier": 1,
        "burst": 1,
        "magazinereloadtime": 0,
        "reloadtime": 1,
        "magazinereloadswitchphase": 1,
        "soundbegin": ["sound",1],
        "soundbeginwater": ["sound",1],
        "soundclosure": ["sound",1],
        "soundend": ["sound",1],
        "soundloop": ["sound",1],
        "soundcontinuous": 0,
        "weaponsoundeffect": "",
        "soundburst": 1,
        "drysound": ["",1,1],
        "zeroingsound": ["",1,1],
        "changefiremodesound": ["",1,1],
        "reloadmagazinesound": ["",1,1],
        "emptysound": ["",1,1],
        "soundbullet": ["emptySound",1],
        "initspeed": 0,
        "ballisticscomputer": 0,
        "irdistance": 0,
        "irdotintensity": 0.001,
        "dispersion": 0.002,
        "aidispersioncoefx": 1,
        "aidispersioncoefy": 1,
        "lockacquire": 1,
        "ffmagnitude": 0,
        "fffrequency": 1,
        "ffcount": 1,
        # Recoil Array: recoil,
        "recoil": [],
        "recoil": "empty",
        "recoilprone": "",
        "maxrecoilsway": 0.008,
        "swaydecayspeed": 2,
        "model": "",
        "modelspecial": "",
        "modelmagazine": "",
        "muzzlepos": "usti hlavne",
        "muzzleend": "konec hlavne",
        "irlaserpos": "laser pos",
        "irlaserend": "laser dir",
        "cartridgepos": "nabojnicestart",
        "cartridgevel": "nabojniceend",
        "selectionfireanim": "zasleh",
        "memorypointcamera": "eye",
        "firespreadangle": 3,
        "usemodeloptics": 1,
        "opticsid": 0,
        "modeloptics": "",
        "opticsppeffects": [],
        "opticsflare": 1,
        "forceoptics": 0,
        "useasbinocular": 0,
        "opticsdisableperipherialvision": 0.67,
        "distancezoommin": 400,
        "distancezoommax": 400,
        "showswitchaction": 0,
        "autofire": 0,
        "autoreload": 1,
        "showtoplayer": 1,
        "canshootinwater": 0,
        "airateoffire": 5,
        "airateoffiredistance": 500,
        "airateoffiredispersion": 0,
        "firelightduration": 0.05,
        "firelightintensity": 0.2,
        "firelightdiffuse": [0.937,0.631,0.259],
        "firelightambient": [0,0,0],
        # Class: CfgWeapons|Default|Eventhandlers [Indent level: 1],
        "eventhandlers": {
        },
        "backgroundreload": 0,
        "reloadaction": "",
        "muzzles": ["this"],
        "modes": ["this"],
        "useaction": 0,
        "useactiontitle": "",
        "candrop": 1,
        "weaponlockdelay": 0,
        "weaponlocksystem": 0,
        "cmimmunity": 1,
        "weight": 0,
        "handanim": [],
        "lockingtargetsound": ["",0.000316228,2],
        "lockedtargetsound": ["",0.000316228,6],
        "detectrange": 0,
        "artillerydispersion": 1,
        "artillerycharge": 1,
        "fireanims": [],
        # Class: CfgWeapons|Default|Library [Indent level: 1],
        "library": {
            "libtextdesc": ""
        },
        "descriptionshort": "",
        # Class: CfgWeapons|Default|GunFire [Indent level: 1],
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
            "cloudletdensitycoef": -1,
            "interval": -0.01,
            "size": 3,
            "sourcesize": 0.5,
            "timetolive": 0,
            "initt": 4500,
            "deltat": -3000,
            # Class: CfgWeapons|Default|GunFire|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunFire|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [0.82,0.95,0.93,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T1 [Indent level: 3],
                "t1": {
                    "maxt": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T2 [Indent level: 3],
                "t2": {
                    "maxt": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T3 [Indent level: 3],
                "t3": {
                    "maxt": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T4 [Indent level: 3],
                "t4": {
                    "maxt": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T5 [Indent level: 3],
                "t5": {
                    "maxt": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T6 [Indent level: 3],
                "t6": {
                    "maxt": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T7 [Indent level: 3],
                "t7": {
                    "maxt": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T8 [Indent level: 3],
                "t8": {
                    "maxt": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T9 [Indent level: 3],
                "t9": {
                    "maxt": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T10 [Indent level: 3],
                "t10": {
                    "maxt": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T11 [Indent level: 3],
                "t11": {
                    "maxt": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T12 [Indent level: 3],
                "t12": {
                    "maxt": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T13 [Indent level: 3],
                "t13": {
                    "maxt": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T14 [Indent level: 3],
                "t14": {
                    "maxt": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T15 [Indent level: 3],
                "t15": {
                    "maxt": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T16 [Indent level: 3],
                "t16": {
                    "maxt": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T17 [Indent level: 3],
                "t17": {
                    "maxt": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T18 [Indent level: 3],
                "t18": {
                    "maxt": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T19 [Indent level: 3],
                "t19": {
                    "maxt": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T20 [Indent level: 3],
                "t20": {
                    "maxt": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T21 [Indent level: 3],
                "t21": {
                    "maxt": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T22 [Indent level: 3],
                "t22": {
                    "maxt": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgWeapons|Default|GunClouds [Indent level: 1],
        "gunclouds": {
            "access": 0,
            "cloudletgrowup": 0.05,
            "cloudletfadein": 0,
            "cloudletfadeout": 0.1,
            "cloudletduration": 0.05,
            "cloudletalpha": 0.3,
            "cloudletaccy": 0,
            "cloudletminyspeed": -100,
            "cloudletmaxyspeed": 100,
            "interval": -0.02,
            "size": 0.3,
            "sourcesize": 0.02,
            "cloudletanimperiod": 1,
            "cloudletsize": 1,
            "cloudletshape": "cloudletClouds",
            "cloudletcolor": [1,1,1,0],
            "timetolive": 0,
            "initt": 0,
            "deltat": 0,
            # Class: CfgWeapons|Default|GunClouds|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunClouds|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        "texturetype": "default",
        "inertia": 0.5,
        "aimtransitionspeed": 1
    },
    # Class: CfgWeapons|Put|PipeBombMuzzle [Indent level: 1],
    "pipebombmuzzle": {
        # Compatible Magazines: magazines parameter (+ inherited)
        "magazines": [
            "democharge_remote_mag","iedurbansmall_remote_mag","iedlandsmall_remote_mag","satchelcharge_remote_mag"
            "iedurbanbig_remote_mag","iedlandbig_remote_mag","atmine_range_mag","claymoredirectionalmine_remote_mag"
            "apersmine_range_mag","apersboundingmine_range_mag","slamdirectionalmine_wire_mag","aperstripmine_wire_mag"
            "apersminedispenser_mag","trainingmine_mag","rhs_mine_pmn2_mag","rhs_mine_tm62m_mag"
            "rhs_mine_msk40p_white_mag","rhs_mine_msk40p_red_mag","rhs_mine_msk40p_green_mag","rhs_mine_msk40p_blue_mag"
            "rhs_mine_sm320_white_mag","rhs_mine_sm320_red_mag","rhs_mine_sm320_green_mag","rhs_mine_ozm72_a_mag"
            "rhs_mine_ozm72_b_mag","rhs_mine_ozm72_c_mag","rhs_ec75_mag","rhs_ec200_mag"
            "rhs_ec400_mag","rhs_ec75_sand_mag","rhs_ec200_sand_mag","rhs_ec400_sand_mag"
            "rhs_mine_m19_mag","rhsusf_mine_m14_mag","rhsusf_mine_m49a1_3m_mag","rhsusf_mine_m49a1_6m_mag"
            "rhsusf_mine_m49a1_10m_mag","rhsusf_m112_mag","rhsusf_m112x4_mag","rhs_mag_mine_pfm1"
            "rhs_mag_mine_ptm1","rhs_mine_smine35_press_mag","rhs_mine_smine35_trip_mag","rhs_mine_smine44_press_mag"
            "rhs_mine_smine44_trip_mag","rhs_mine_glasmine43_hz_mag","rhs_mine_glasmine43_bz_mag","rhs_mine_stockmine43_2m_mag"
            "rhs_mine_stockmine43_4m_mag","rhs_mine_a200_bz_mag","rhs_mine_a200_dz35_mag","rhs_mine_tm43_mag"
            "rhs_mine_m2a3b_press_mag","rhs_mine_m2a3b_trip_mag","rhs_mine_m3_pressure_mag","rhs_mine_mk2_pressure_mag"
            "rhs_mine_m3_tripwire_mag","rhs_mine_mk2_tripwire_mag","rhs_mine_m7a2_mag","rhs_charge_m2tet_x2_mag"
            "rhssaf_mine_pma3_mag","rhssaf_mine_tma4_mag","rhssaf_mine_mrud_a_mag","rhssaf_mine_mrud_b_mag"
            "rhssaf_mine_mrud_c_mag","rhssaf_mine_mrud_d_mag","rhssaf_tm100_mag","rhssaf_tm200_mag"
            "rhssaf_tm500_mag",],
        "autoreload": 0,
        "displayname": "Explosive Satchel",
        "enableattack": 1,
        "showtoplayer": 0,
        "sound": ["",0.000316228,1],
        "reloadsound": ["",0.000316228,1],
        "optics": 0,
        "showempty": 0,
        "canlock": 0,
        "primary": 10,
        "minrange": 0,
        "minrangeprobab": 0.1,
        "midrange": 3,
        "midrangeprobab": 0.9,
        "maxrange": 15,
        "maxrangeprobab": 0.04,
        "movetointernal": 0,
        "opticszoommin": 0.25,
        "opticszoommax": 1.25,
        "opticszoominit": 0.75,
        "access": 3,
        "scope": 0,
        "value": 2,
        "picture": "",
        "uipicture": "",
        "ammo": "",
        "cursor": "",
        "cursoraim": "",
        "cursorsize": 1,
        "showaimcursorinternal": 1,
        "cursoraimon": "",
        "laser": 0,
        "hiddenselections": [],
        "hiddenselectionstextures": [],
        "hiddenunderwaterselections": [],
        "shownunderwaterselections": [],
        "hiddenunderwaterselectionstextures": [],
        "simulation": "Weapon",
        "type": 65536,
        "namesound": "",
        "count": 0,
        "multiplier": 1,
        "burst": 1,
        "magazinereloadtime": 0,
        "reloadtime": 1,
        "magazinereloadswitchphase": 1,
        "soundbegin": ["sound",1],
        "soundbeginwater": ["sound",1],
        "soundclosure": ["sound",1],
        "soundend": ["sound",1],
        "soundloop": ["sound",1],
        "soundcontinuous": 0,
        "weaponsoundeffect": "",
        "soundburst": 1,
        "drysound": ["",1,1],
        "zeroingsound": ["",1,1],
        "changefiremodesound": ["",1,1],
        "reloadmagazinesound": ["",1,1],
        "emptysound": ["",1,1],
        "soundbullet": ["emptySound",1],
        "initspeed": 0,
        "ballisticscomputer": 0,
        "irdistance": 0,
        "irdotintensity": 0.001,
        "dispersion": 0.002,
        "aidispersioncoefx": 1,
        "aidispersioncoefy": 1,
        "lockacquire": 1,
        "ffmagnitude": 0,
        "fffrequency": 1,
        "ffcount": 1,
        # Recoil Array: recoil,
        "recoil": [],
        "recoil": "empty",
        "recoilprone": "",
        "maxrecoilsway": 0.008,
        "swaydecayspeed": 2,
        "model": "",
        "modelspecial": "",
        "modelmagazine": "",
        "muzzlepos": "usti hlavne",
        "muzzleend": "konec hlavne",
        "irlaserpos": "laser pos",
        "irlaserend": "laser dir",
        "cartridgepos": "nabojnicestart",
        "cartridgevel": "nabojniceend",
        "selectionfireanim": "zasleh",
        "memorypointcamera": "eye",
        "firespreadangle": 3,
        "usemodeloptics": 1,
        "opticsid": 0,
        "modeloptics": "",
        "opticsppeffects": [],
        "opticsflare": 1,
        "forceoptics": 0,
        "useasbinocular": 0,
        "opticsdisableperipherialvision": 0.67,
        "distancezoommin": 400,
        "distancezoommax": 400,
        "showswitchaction": 0,
        "autofire": 0,
        "canshootinwater": 0,
        "airateoffire": 5,
        "airateoffiredistance": 500,
        "airateoffiredispersion": 0,
        "firelightduration": 0.05,
        "firelightintensity": 0.2,
        "firelightdiffuse": [0.937,0.631,0.259],
        "firelightambient": [0,0,0],
        # Class: CfgWeapons|Default|Eventhandlers [Indent level: 1],
        "eventhandlers": {
        },
        "backgroundreload": 0,
        "reloadaction": "",
        "muzzles": ["this"],
        "modes": ["this"],
        "useaction": 0,
        "useactiontitle": "",
        "candrop": 1,
        "weaponlockdelay": 0,
        "weaponlocksystem": 0,
        "cmimmunity": 1,
        "weight": 0,
        "handanim": [],
        "lockingtargetsound": ["",0.000316228,2],
        "lockedtargetsound": ["",0.000316228,6],
        "detectrange": 0,
        "artillerydispersion": 1,
        "artillerycharge": 1,
        "fireanims": [],
        # Class: CfgWeapons|Default|Library [Indent level: 1],
        "library": {
            "libtextdesc": ""
        },
        "descriptionshort": "",
        # Class: CfgWeapons|Default|GunFire [Indent level: 1],
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
            "cloudletdensitycoef": -1,
            "interval": -0.01,
            "size": 3,
            "sourcesize": 0.5,
            "timetolive": 0,
            "initt": 4500,
            "deltat": -3000,
            # Class: CfgWeapons|Default|GunFire|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunFire|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [0.82,0.95,0.93,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T1 [Indent level: 3],
                "t1": {
                    "maxt": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T2 [Indent level: 3],
                "t2": {
                    "maxt": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T3 [Indent level: 3],
                "t3": {
                    "maxt": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T4 [Indent level: 3],
                "t4": {
                    "maxt": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T5 [Indent level: 3],
                "t5": {
                    "maxt": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T6 [Indent level: 3],
                "t6": {
                    "maxt": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T7 [Indent level: 3],
                "t7": {
                    "maxt": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T8 [Indent level: 3],
                "t8": {
                    "maxt": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T9 [Indent level: 3],
                "t9": {
                    "maxt": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T10 [Indent level: 3],
                "t10": {
                    "maxt": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T11 [Indent level: 3],
                "t11": {
                    "maxt": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T12 [Indent level: 3],
                "t12": {
                    "maxt": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T13 [Indent level: 3],
                "t13": {
                    "maxt": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T14 [Indent level: 3],
                "t14": {
                    "maxt": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T15 [Indent level: 3],
                "t15": {
                    "maxt": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T16 [Indent level: 3],
                "t16": {
                    "maxt": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T17 [Indent level: 3],
                "t17": {
                    "maxt": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T18 [Indent level: 3],
                "t18": {
                    "maxt": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T19 [Indent level: 3],
                "t19": {
                    "maxt": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T20 [Indent level: 3],
                "t20": {
                    "maxt": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T21 [Indent level: 3],
                "t21": {
                    "maxt": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T22 [Indent level: 3],
                "t22": {
                    "maxt": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgWeapons|Default|GunClouds [Indent level: 1],
        "gunclouds": {
            "access": 0,
            "cloudletgrowup": 0.05,
            "cloudletfadein": 0,
            "cloudletfadeout": 0.1,
            "cloudletduration": 0.05,
            "cloudletalpha": 0.3,
            "cloudletaccy": 0,
            "cloudletminyspeed": -100,
            "cloudletmaxyspeed": 100,
            "interval": -0.02,
            "size": 0.3,
            "sourcesize": 0.02,
            "cloudletanimperiod": 1,
            "cloudletsize": 1,
            "cloudletshape": "cloudletClouds",
            "cloudletcolor": [1,1,1,0],
            "timetolive": 0,
            "initt": 0,
            "deltat": 0,
            # Class: CfgWeapons|Default|GunClouds|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunClouds|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        "texturetype": "default",
        "inertia": 0.5,
        "aimtransitionspeed": 1
    },
    # Class: CfgWeapons|Put|MineMuzzle [Indent level: 1],
    "minemuzzle": {
        # Compatible Magazines: magazines parameter (+ inherited)
        "magazines": [
            "democharge_remote_mag","iedurbansmall_remote_mag","iedlandsmall_remote_mag","satchelcharge_remote_mag"
            "iedurbanbig_remote_mag","iedlandbig_remote_mag","atmine_range_mag","claymoredirectionalmine_remote_mag"
            "apersmine_range_mag","apersboundingmine_range_mag","slamdirectionalmine_wire_mag","aperstripmine_wire_mag"
            "apersminedispenser_mag","trainingmine_mag","rhs_mine_pmn2_mag","rhs_mine_tm62m_mag"
            "rhs_mine_msk40p_white_mag","rhs_mine_msk40p_red_mag","rhs_mine_msk40p_green_mag","rhs_mine_msk40p_blue_mag"
            "rhs_mine_sm320_white_mag","rhs_mine_sm320_red_mag","rhs_mine_sm320_green_mag","rhs_mine_ozm72_a_mag"
            "rhs_mine_ozm72_b_mag","rhs_mine_ozm72_c_mag","rhs_ec75_mag","rhs_ec200_mag"
            "rhs_ec400_mag","rhs_ec75_sand_mag","rhs_ec200_sand_mag","rhs_ec400_sand_mag"
            "rhs_mine_m19_mag","rhsusf_mine_m14_mag","rhsusf_mine_m49a1_3m_mag","rhsusf_mine_m49a1_6m_mag"
            "rhsusf_mine_m49a1_10m_mag","rhsusf_m112_mag","rhsusf_m112x4_mag","rhs_mag_mine_pfm1"
            "rhs_mag_mine_ptm1","rhs_mine_smine35_press_mag","rhs_mine_smine35_trip_mag","rhs_mine_smine44_press_mag"
            "rhs_mine_smine44_trip_mag","rhs_mine_glasmine43_hz_mag","rhs_mine_glasmine43_bz_mag","rhs_mine_stockmine43_2m_mag"
            "rhs_mine_stockmine43_4m_mag","rhs_mine_a200_bz_mag","rhs_mine_a200_dz35_mag","rhs_mine_tm43_mag"
            "rhs_mine_m2a3b_press_mag","rhs_mine_m2a3b_trip_mag","rhs_mine_m3_pressure_mag","rhs_mine_mk2_pressure_mag"
            "rhs_mine_m3_tripwire_mag","rhs_mine_mk2_tripwire_mag","rhs_mine_m7a2_mag","rhs_charge_m2tet_x2_mag"
            "rhssaf_mine_pma3_mag","rhssaf_mine_tma4_mag","rhssaf_mine_mrud_a_mag","rhssaf_mine_mrud_b_mag"
            "rhssaf_mine_mrud_c_mag","rhssaf_mine_mrud_d_mag","rhssaf_tm100_mag","rhssaf_tm200_mag"
            "rhssaf_tm500_mag",],
        "autoreload": 0,
        "enableattack": 1,
        "displayname": "AT Mine",
        "picture": "A3|Weapons_F|Data|clear_empty.paa",
        "showtoplayer": 0,
        "sound": ["",0.000316228,1],
        "reloadsound": ["",0.000316228,1],
        "optics": 0,
        "showempty": 0,
        "canlock": 0,
        "primary": 10,
        "minrange": 0,
        "minrangeprobab": 0.1,
        "midrange": 3,
        "midrangeprobab": 0.9,
        "maxrange": 15,
        "maxrangeprobab": 0.04,
        "movetointernal": 0,
        "opticszoommin": 0.25,
        "opticszoommax": 1.25,
        "opticszoominit": 0.75,
        "access": 3,
        "scope": 0,
        "value": 2,
        "uipicture": "",
        "ammo": "",
        "cursor": "",
        "cursoraim": "",
        "cursorsize": 1,
        "showaimcursorinternal": 1,
        "cursoraimon": "",
        "laser": 0,
        "hiddenselections": [],
        "hiddenselectionstextures": [],
        "hiddenunderwaterselections": [],
        "shownunderwaterselections": [],
        "hiddenunderwaterselectionstextures": [],
        "simulation": "Weapon",
        "type": 65536,
        "namesound": "",
        "count": 0,
        "multiplier": 1,
        "burst": 1,
        "magazinereloadtime": 0,
        "reloadtime": 1,
        "magazinereloadswitchphase": 1,
        "soundbegin": ["sound",1],
        "soundbeginwater": ["sound",1],
        "soundclosure": ["sound",1],
        "soundend": ["sound",1],
        "soundloop": ["sound",1],
        "soundcontinuous": 0,
        "weaponsoundeffect": "",
        "soundburst": 1,
        "drysound": ["",1,1],
        "zeroingsound": ["",1,1],
        "changefiremodesound": ["",1,1],
        "reloadmagazinesound": ["",1,1],
        "emptysound": ["",1,1],
        "soundbullet": ["emptySound",1],
        "initspeed": 0,
        "ballisticscomputer": 0,
        "irdistance": 0,
        "irdotintensity": 0.001,
        "dispersion": 0.002,
        "aidispersioncoefx": 1,
        "aidispersioncoefy": 1,
        "lockacquire": 1,
        "ffmagnitude": 0,
        "fffrequency": 1,
        "ffcount": 1,
        # Recoil Array: recoil,
        "recoil": [],
        "recoil": "empty",
        "recoilprone": "",
        "maxrecoilsway": 0.008,
        "swaydecayspeed": 2,
        "model": "",
        "modelspecial": "",
        "modelmagazine": "",
        "muzzlepos": "usti hlavne",
        "muzzleend": "konec hlavne",
        "irlaserpos": "laser pos",
        "irlaserend": "laser dir",
        "cartridgepos": "nabojnicestart",
        "cartridgevel": "nabojniceend",
        "selectionfireanim": "zasleh",
        "memorypointcamera": "eye",
        "firespreadangle": 3,
        "usemodeloptics": 1,
        "opticsid": 0,
        "modeloptics": "",
        "opticsppeffects": [],
        "opticsflare": 1,
        "forceoptics": 0,
        "useasbinocular": 0,
        "opticsdisableperipherialvision": 0.67,
        "distancezoommin": 400,
        "distancezoommax": 400,
        "showswitchaction": 0,
        "autofire": 0,
        "canshootinwater": 0,
        "airateoffire": 5,
        "airateoffiredistance": 500,
        "airateoffiredispersion": 0,
        "firelightduration": 0.05,
        "firelightintensity": 0.2,
        "firelightdiffuse": [0.937,0.631,0.259],
        "firelightambient": [0,0,0],
        # Class: CfgWeapons|Default|Eventhandlers [Indent level: 1],
        "eventhandlers": {
        },
        "backgroundreload": 0,
        "reloadaction": "",
        "muzzles": ["this"],
        "modes": ["this"],
        "useaction": 0,
        "useactiontitle": "",
        "candrop": 1,
        "weaponlockdelay": 0,
        "weaponlocksystem": 0,
        "cmimmunity": 1,
        "weight": 0,
        "handanim": [],
        "lockingtargetsound": ["",0.000316228,2],
        "lockedtargetsound": ["",0.000316228,6],
        "detectrange": 0,
        "artillerydispersion": 1,
        "artillerycharge": 1,
        "fireanims": [],
        # Class: CfgWeapons|Default|Library [Indent level: 1],
        "library": {
            "libtextdesc": ""
        },
        "descriptionshort": "",
        # Class: CfgWeapons|Default|GunFire [Indent level: 1],
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
            "cloudletdensitycoef": -1,
            "interval": -0.01,
            "size": 3,
            "sourcesize": 0.5,
            "timetolive": 0,
            "initt": 4500,
            "deltat": -3000,
            # Class: CfgWeapons|Default|GunFire|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunFire|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [0.82,0.95,0.93,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T1 [Indent level: 3],
                "t1": {
                    "maxt": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T2 [Indent level: 3],
                "t2": {
                    "maxt": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T3 [Indent level: 3],
                "t3": {
                    "maxt": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T4 [Indent level: 3],
                "t4": {
                    "maxt": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T5 [Indent level: 3],
                "t5": {
                    "maxt": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T6 [Indent level: 3],
                "t6": {
                    "maxt": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T7 [Indent level: 3],
                "t7": {
                    "maxt": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T8 [Indent level: 3],
                "t8": {
                    "maxt": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T9 [Indent level: 3],
                "t9": {
                    "maxt": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T10 [Indent level: 3],
                "t10": {
                    "maxt": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T11 [Indent level: 3],
                "t11": {
                    "maxt": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T12 [Indent level: 3],
                "t12": {
                    "maxt": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T13 [Indent level: 3],
                "t13": {
                    "maxt": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T14 [Indent level: 3],
                "t14": {
                    "maxt": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T15 [Indent level: 3],
                "t15": {
                    "maxt": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T16 [Indent level: 3],
                "t16": {
                    "maxt": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T17 [Indent level: 3],
                "t17": {
                    "maxt": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T18 [Indent level: 3],
                "t18": {
                    "maxt": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T19 [Indent level: 3],
                "t19": {
                    "maxt": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T20 [Indent level: 3],
                "t20": {
                    "maxt": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T21 [Indent level: 3],
                "t21": {
                    "maxt": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T22 [Indent level: 3],
                "t22": {
                    "maxt": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgWeapons|Default|GunClouds [Indent level: 1],
        "gunclouds": {
            "access": 0,
            "cloudletgrowup": 0.05,
            "cloudletfadein": 0,
            "cloudletfadeout": 0.1,
            "cloudletduration": 0.05,
            "cloudletalpha": 0.3,
            "cloudletaccy": 0,
            "cloudletminyspeed": -100,
            "cloudletmaxyspeed": 100,
            "interval": -0.02,
            "size": 0.3,
            "sourcesize": 0.02,
            "cloudletanimperiod": 1,
            "cloudletsize": 1,
            "cloudletshape": "cloudletClouds",
            "cloudletcolor": [1,1,1,0],
            "timetolive": 0,
            "initt": 0,
            "deltat": 0,
            # Class: CfgWeapons|Default|GunClouds|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunClouds|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        "texturetype": "default",
        "inertia": 0.5,
        "aimtransitionspeed": 1
    },
    # Class: CfgWeapons|Put|ClassicMineRangeMuzzle [Indent level: 1],
    "classicminerangemuzzle": {
        "autoreload": 0,
        "enableattack": 1,
        # Compatible Magazines: magazines parameter (+ inherited),
        "magazines": [
            "democharge_remote_mag","iedurbansmall_remote_mag","iedlandsmall_remote_mag","satchelcharge_remote_mag",
            "iedurbanbig_remote_mag","iedlandbig_remote_mag","atmine_range_mag","claymoredirectionalmine_remote_mag",
            "apersmine_range_mag","apersboundingmine_range_mag","slamdirectionalmine_wire_mag","aperstripmine_wire_mag",
            "apersminedispenser_mag","trainingmine_mag","rhs_mine_pmn2_mag","rhs_mine_tm62m_mag",
            "rhs_mine_msk40p_white_mag","rhs_mine_msk40p_red_mag","rhs_mine_msk40p_green_mag","rhs_mine_msk40p_blue_mag",
            "rhs_mine_sm320_white_mag","rhs_mine_sm320_red_mag","rhs_mine_sm320_green_mag","rhs_mine_ozm72_a_mag",
            "rhs_mine_ozm72_b_mag","rhs_mine_ozm72_c_mag","rhs_ec75_mag","rhs_ec200_mag",
            "rhs_ec400_mag","rhs_ec75_sand_mag","rhs_ec200_sand_mag","rhs_ec400_sand_mag",
            "rhs_mine_m19_mag","rhsusf_mine_m14_mag","rhsusf_mine_m49a1_3m_mag","rhsusf_mine_m49a1_6m_mag",
            "rhsusf_mine_m49a1_10m_mag","rhsusf_m112_mag","rhsusf_m112x4_mag","rhs_mag_mine_pfm1",
            "rhs_mag_mine_ptm1","rhs_mine_smine35_press_mag","rhs_mine_smine35_trip_mag","rhs_mine_smine44_press_mag",
            "rhs_mine_smine44_trip_mag","rhs_mine_glasmine43_hz_mag","rhs_mine_glasmine43_bz_mag","rhs_mine_stockmine43_2m_mag",
            "rhs_mine_stockmine43_4m_mag","rhs_mine_a200_bz_mag","rhs_mine_a200_dz35_mag","rhs_mine_tm43_mag",
            "rhs_mine_m2a3b_press_mag","rhs_mine_m2a3b_trip_mag","rhs_mine_m3_pressure_mag","rhs_mine_mk2_pressure_mag",
            "rhs_mine_m3_tripwire_mag","rhs_mine_mk2_tripwire_mag","rhs_mine_m7a2_mag","rhs_charge_m2tet_x2_mag",
            "rhssaf_mine_pma3_mag","rhssaf_mine_tma4_mag","rhssaf_mine_mrud_a_mag","rhssaf_mine_mrud_b_mag",
            "rhssaf_mine_mrud_c_mag","rhssaf_mine_mrud_d_mag","rhssaf_tm100_mag","rhssaf_tm200_mag",
            "rhssaf_tm500_mag",],
        "displayname": "APERS Mine",
        "picture": "A3|Weapons_F|Data|clear_empty.paa",
        "showtoplayer": 0,
        # Class: CfgWeapons|Put|ClassicMineRangeMuzzle|EventHandlers [Indent level: 2],
        "eventhandlers": {
            "fired": "['firedMine',_this] call bis_fnc_showLawOfWar;"
        },
        "sound": ["",0.000316228,1],
        "reloadsound": ["",0.000316228,1],
        "optics": 0,
        "showempty": 0,
        "canlock": 0,
        "primary": 10,
        "minrange": 0,
        "minrangeprobab": 0.1,
        "midrange": 3,
        "midrangeprobab": 0.9,
        "maxrange": 15,
        "maxrangeprobab": 0.04,
        "movetointernal": 0,
        "opticszoommin": 0.25,
        "opticszoommax": 1.25,
        "opticszoominit": 0.75,
        "access": 3,
        "scope": 0,
        "value": 2,
        "uipicture": "",
        "ammo": "",
        "cursor": "",
        "cursoraim": "",
        "cursorsize": 1,
        "showaimcursorinternal": 1,
        "cursoraimon": "",
        "laser": 0,
        "hiddenselections": [],
        "hiddenselectionstextures": [],
        "hiddenunderwaterselections": [],
        "shownunderwaterselections": [],
        "hiddenunderwaterselectionstextures": [],
        "simulation": "Weapon",
        "type": 65536,
        "namesound": "",
        "count": 0,
        "multiplier": 1,
        "burst": 1,
        "magazinereloadtime": 0,
        "reloadtime": 1,
        "magazinereloadswitchphase": 1,
        "soundbegin": ["sound",1],
        "soundbeginwater": ["sound",1],
        "soundclosure": ["sound",1],
        "soundend": ["sound",1],
        "soundloop": ["sound",1],
        "soundcontinuous": 0,
        "weaponsoundeffect": "",
        "soundburst": 1,
        "drysound": ["",1,1],
        "zeroingsound": ["",1,1],
        "changefiremodesound": ["",1,1],
        "reloadmagazinesound": ["",1,1],
        "emptysound": ["",1,1],
        "soundbullet": ["emptySound",1],
        "initspeed": 0,
        "ballisticscomputer": 0,
        "irdistance": 0,
        "irdotintensity": 0.001,
        "dispersion": 0.002,
        "aidispersioncoefx": 1,
        "aidispersioncoefy": 1,
        "lockacquire": 1,
        "ffmagnitude": 0,
        "fffrequency": 1,
        "ffcount": 1,
        # Recoil Array: recoil,
        "recoil": [],
        "recoil": "empty",
        "recoilprone": "",
        "maxrecoilsway": 0.008,
        "swaydecayspeed": 2,
        "model": "",
        "modelspecial": "",
        "modelmagazine": "",
        "muzzlepos": "usti hlavne",
        "muzzleend": "konec hlavne",
        "irlaserpos": "laser pos",
        "irlaserend": "laser dir",
        "cartridgepos": "nabojnicestart",
        "cartridgevel": "nabojniceend",
        "selectionfireanim": "zasleh",
        "memorypointcamera": "eye",
        "firespreadangle": 3,
        "usemodeloptics": 1,
        "opticsid": 0,
        "modeloptics": "",
        "opticsppeffects": [],
        "opticsflare": 1,
        "forceoptics": 0,
        "useasbinocular": 0,
        "opticsdisableperipherialvision": 0.67,
        "distancezoommin": 400,
        "distancezoommax": 400,
        "showswitchaction": 0,
        "autofire": 0,
        "canshootinwater": 0,
        "airateoffire": 5,
        "airateoffiredistance": 500,
        "airateoffiredispersion": 0,
        "firelightduration": 0.05,
        "firelightintensity": 0.2,
        "firelightdiffuse": [0.937,0.631,0.259],
        "firelightambient": [0,0,0],
        "backgroundreload": 0,
        "reloadaction": "",
        "muzzles": ["this"],
        "modes": ["this"],
        "useaction": 0,
        "useactiontitle": "",
        "candrop": 1,
        "weaponlockdelay": 0,
        "weaponlocksystem": 0,
        "cmimmunity": 1,
        "weight": 0,
        "handanim": [],
        "lockingtargetsound": ["",0.000316228,2],
        "lockedtargetsound": ["",0.000316228,6],
        "detectrange": 0,
        "artillerydispersion": 1,
        "artillerycharge": 1,
        "fireanims": [],
        # Class: CfgWeapons|Default|Library [Indent level: 1],
        "library": {
            "libtextdesc": ""
        },
        "descriptionshort": "",
        # Class: CfgWeapons|Default|GunFire [Indent level: 1],
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
            "cloudletdensitycoef": -1,
            "interval": -0.01,
            "size": 3,
            "sourcesize": 0.5,
            "timetolive": 0,
            "initt": 4500,
            "deltat": -3000,
            # Class: CfgWeapons|Default|GunFire|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunFire|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [0.82,0.95,0.93,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T1 [Indent level: 3],
                "t1": {
                    "maxt": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T2 [Indent level: 3],
                "t2": {
                    "maxt": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T3 [Indent level: 3],
                "t3": {
                    "maxt": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T4 [Indent level: 3],
                "t4": {
                    "maxt": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T5 [Indent level: 3],
                "t5": {
                    "maxt": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T6 [Indent level: 3],
                "t6": {
                    "maxt": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T7 [Indent level: 3],
                "t7": {
                    "maxt": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T8 [Indent level: 3],
                "t8": {
                    "maxt": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T9 [Indent level: 3],
                "t9": {
                    "maxt": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T10 [Indent level: 3],
                "t10": {
                    "maxt": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T11 [Indent level: 3],
                "t11": {
                    "maxt": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T12 [Indent level: 3],
                "t12": {
                    "maxt": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T13 [Indent level: 3],
                "t13": {
                    "maxt": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T14 [Indent level: 3],
                "t14": {
                    "maxt": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T15 [Indent level: 3],
                "t15": {
                    "maxt": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T16 [Indent level: 3],
                "t16": {
                    "maxt": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T17 [Indent level: 3],
                "t17": {
                    "maxt": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T18 [Indent level: 3],
                "t18": {
                    "maxt": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T19 [Indent level: 3],
                "t19": {
                    "maxt": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T20 [Indent level: 3],
                "t20": {
                    "maxt": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T21 [Indent level: 3],
                "t21": {
                    "maxt": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T22 [Indent level: 3],
                "t22": {
                    "maxt": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgWeapons|Default|GunClouds [Indent level: 1],
        "gunclouds": {
            "access": 0,
            "cloudletgrowup": 0.05,
            "cloudletfadein": 0,
            "cloudletfadeout": 0.1,
            "cloudletduration": 0.05,
            "cloudletalpha": 0.3,
            "cloudletaccy": 0,
            "cloudletminyspeed": -100,
            "cloudletmaxyspeed": 100,
            "interval": -0.02,
            "size": 0.3,
            "sourcesize": 0.02,
            "cloudletanimperiod": 1,
            "cloudletsize": 1,
            "cloudletshape": "cloudletClouds",
            "cloudletcolor": [1,1,1,0],
            "timetolive": 0,
            "initt": 0,
            "deltat": 0,
            # Class: CfgWeapons|Default|GunClouds|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunClouds|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        "texturetype": "default",
        "inertia": 0.5,
        "aimtransitionspeed": 1
    },
    # Class: CfgWeapons|Put|BoundingMineRangeMuzzle [Indent level: 1],
    "boundingminerangemuzzle": {
        # Compatible Magazines: magazines parameter (+ inherited)
        "magazines": [
            "democharge_remote_mag","iedurbansmall_remote_mag","iedlandsmall_remote_mag","satchelcharge_remote_mag"
            "iedurbanbig_remote_mag","iedlandbig_remote_mag","atmine_range_mag","claymoredirectionalmine_remote_mag"
            "apersmine_range_mag","apersboundingmine_range_mag","slamdirectionalmine_wire_mag","aperstripmine_wire_mag"
            "apersminedispenser_mag","trainingmine_mag","rhs_mine_pmn2_mag","rhs_mine_tm62m_mag"
            "rhs_mine_msk40p_white_mag","rhs_mine_msk40p_red_mag","rhs_mine_msk40p_green_mag","rhs_mine_msk40p_blue_mag"
            "rhs_mine_sm320_white_mag","rhs_mine_sm320_red_mag","rhs_mine_sm320_green_mag","rhs_mine_ozm72_a_mag"
            "rhs_mine_ozm72_b_mag","rhs_mine_ozm72_c_mag","rhs_ec75_mag","rhs_ec200_mag"
            "rhs_ec400_mag","rhs_ec75_sand_mag","rhs_ec200_sand_mag","rhs_ec400_sand_mag"
            "rhs_mine_m19_mag","rhsusf_mine_m14_mag","rhsusf_mine_m49a1_3m_mag","rhsusf_mine_m49a1_6m_mag"
            "rhsusf_mine_m49a1_10m_mag","rhsusf_m112_mag","rhsusf_m112x4_mag","rhs_mag_mine_pfm1"
            "rhs_mag_mine_ptm1","rhs_mine_smine35_press_mag","rhs_mine_smine35_trip_mag","rhs_mine_smine44_press_mag"
            "rhs_mine_smine44_trip_mag","rhs_mine_glasmine43_hz_mag","rhs_mine_glasmine43_bz_mag","rhs_mine_stockmine43_2m_mag"
            "rhs_mine_stockmine43_4m_mag","rhs_mine_a200_bz_mag","rhs_mine_a200_dz35_mag","rhs_mine_tm43_mag"
            "rhs_mine_m2a3b_press_mag","rhs_mine_m2a3b_trip_mag","rhs_mine_m3_pressure_mag","rhs_mine_mk2_pressure_mag"
            "rhs_mine_m3_tripwire_mag","rhs_mine_mk2_tripwire_mag","rhs_mine_m7a2_mag","rhs_charge_m2tet_x2_mag"
            "rhssaf_mine_pma3_mag","rhssaf_mine_tma4_mag","rhssaf_mine_mrud_a_mag","rhssaf_mine_mrud_b_mag"
            "rhssaf_mine_mrud_c_mag","rhssaf_mine_mrud_d_mag","rhssaf_tm100_mag","rhssaf_tm200_mag"
            "rhssaf_tm500_mag",],
        "displayname": "APERS Bounding Mine",
        "autoreload": 0,
        "enableattack": 1,
        "picture": "A3|Weapons_F|Data|clear_empty.paa",
        "showtoplayer": 0,
        # Class: CfgWeapons|Put|ClassicMineRangeMuzzle|EventHandlers [Indent level: 2],
        "eventhandlers": {
            "fired": "['firedMine',_this] call bis_fnc_showLawOfWar;"
        },
        "sound": ["",0.000316228,1],
        "reloadsound": ["",0.000316228,1],
        "optics": 0,
        "showempty": 0,
        "canlock": 0,
        "primary": 10,
        "minrange": 0,
        "minrangeprobab": 0.1,
        "midrange": 3,
        "midrangeprobab": 0.9,
        "maxrange": 15,
        "maxrangeprobab": 0.04,
        "movetointernal": 0,
        "opticszoommin": 0.25,
        "opticszoommax": 1.25,
        "opticszoominit": 0.75,
        "access": 3,
        "scope": 0,
        "value": 2,
        "uipicture": "",
        "ammo": "",
        "cursor": "",
        "cursoraim": "",
        "cursorsize": 1,
        "showaimcursorinternal": 1,
        "cursoraimon": "",
        "laser": 0,
        "hiddenselections": [],
        "hiddenselectionstextures": [],
        "hiddenunderwaterselections": [],
        "shownunderwaterselections": [],
        "hiddenunderwaterselectionstextures": [],
        "simulation": "Weapon",
        "type": 65536,
        "namesound": "",
        "count": 0,
        "multiplier": 1,
        "burst": 1,
        "magazinereloadtime": 0,
        "reloadtime": 1,
        "magazinereloadswitchphase": 1,
        "soundbegin": ["sound",1],
        "soundbeginwater": ["sound",1],
        "soundclosure": ["sound",1],
        "soundend": ["sound",1],
        "soundloop": ["sound",1],
        "soundcontinuous": 0,
        "weaponsoundeffect": "",
        "soundburst": 1,
        "drysound": ["",1,1],
        "zeroingsound": ["",1,1],
        "changefiremodesound": ["",1,1],
        "reloadmagazinesound": ["",1,1],
        "emptysound": ["",1,1],
        "soundbullet": ["emptySound",1],
        "initspeed": 0,
        "ballisticscomputer": 0,
        "irdistance": 0,
        "irdotintensity": 0.001,
        "dispersion": 0.002,
        "aidispersioncoefx": 1,
        "aidispersioncoefy": 1,
        "lockacquire": 1,
        "ffmagnitude": 0,
        "fffrequency": 1,
        "ffcount": 1,
        # Recoil Array: recoil,
        "recoil": [],
        "recoil": "empty",
        "recoilprone": "",
        "maxrecoilsway": 0.008,
        "swaydecayspeed": 2,
        "model": "",
        "modelspecial": "",
        "modelmagazine": "",
        "muzzlepos": "usti hlavne",
        "muzzleend": "konec hlavne",
        "irlaserpos": "laser pos",
        "irlaserend": "laser dir",
        "cartridgepos": "nabojnicestart",
        "cartridgevel": "nabojniceend",
        "selectionfireanim": "zasleh",
        "memorypointcamera": "eye",
        "firespreadangle": 3,
        "usemodeloptics": 1,
        "opticsid": 0,
        "modeloptics": "",
        "opticsppeffects": [],
        "opticsflare": 1,
        "forceoptics": 0,
        "useasbinocular": 0,
        "opticsdisableperipherialvision": 0.67,
        "distancezoommin": 400,
        "distancezoommax": 400,
        "showswitchaction": 0,
        "autofire": 0,
        "canshootinwater": 0,
        "airateoffire": 5,
        "airateoffiredistance": 500,
        "airateoffiredispersion": 0,
        "firelightduration": 0.05,
        "firelightintensity": 0.2,
        "firelightdiffuse": [0.937,0.631,0.259],
        "firelightambient": [0,0,0],
        "backgroundreload": 0,
        "reloadaction": "",
        "muzzles": ["this"],
        "modes": ["this"],
        "useaction": 0,
        "useactiontitle": "",
        "candrop": 1,
        "weaponlockdelay": 0,
        "weaponlocksystem": 0,
        "cmimmunity": 1,
        "weight": 0,
        "handanim": [],
        "lockingtargetsound": ["",0.000316228,2],
        "lockedtargetsound": ["",0.000316228,6],
        "detectrange": 0,
        "artillerydispersion": 1,
        "artillerycharge": 1,
        "fireanims": [],
        # Class: CfgWeapons|Default|Library [Indent level: 1],
        "library": {
            "libtextdesc": ""
        },
        "descriptionshort": "",
        # Class: CfgWeapons|Default|GunFire [Indent level: 1],
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
            "cloudletdensitycoef": -1,
            "interval": -0.01,
            "size": 3,
            "sourcesize": 0.5,
            "timetolive": 0,
            "initt": 4500,
            "deltat": -3000,
            # Class: CfgWeapons|Default|GunFire|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunFire|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [0.82,0.95,0.93,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T1 [Indent level: 3],
                "t1": {
                    "maxt": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T2 [Indent level: 3],
                "t2": {
                    "maxt": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T3 [Indent level: 3],
                "t3": {
                    "maxt": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T4 [Indent level: 3],
                "t4": {
                    "maxt": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T5 [Indent level: 3],
                "t5": {
                    "maxt": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T6 [Indent level: 3],
                "t6": {
                    "maxt": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T7 [Indent level: 3],
                "t7": {
                    "maxt": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T8 [Indent level: 3],
                "t8": {
                    "maxt": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T9 [Indent level: 3],
                "t9": {
                    "maxt": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T10 [Indent level: 3],
                "t10": {
                    "maxt": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T11 [Indent level: 3],
                "t11": {
                    "maxt": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T12 [Indent level: 3],
                "t12": {
                    "maxt": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T13 [Indent level: 3],
                "t13": {
                    "maxt": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T14 [Indent level: 3],
                "t14": {
                    "maxt": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T15 [Indent level: 3],
                "t15": {
                    "maxt": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T16 [Indent level: 3],
                "t16": {
                    "maxt": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T17 [Indent level: 3],
                "t17": {
                    "maxt": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T18 [Indent level: 3],
                "t18": {
                    "maxt": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T19 [Indent level: 3],
                "t19": {
                    "maxt": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T20 [Indent level: 3],
                "t20": {
                    "maxt": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T21 [Indent level: 3],
                "t21": {
                    "maxt": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T22 [Indent level: 3],
                "t22": {
                    "maxt": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgWeapons|Default|GunClouds [Indent level: 1],
        "gunclouds": {
            "access": 0,
            "cloudletgrowup": 0.05,
            "cloudletfadein": 0,
            "cloudletfadeout": 0.1,
            "cloudletduration": 0.05,
            "cloudletalpha": 0.3,
            "cloudletaccy": 0,
            "cloudletminyspeed": -100,
            "cloudletmaxyspeed": 100,
            "interval": -0.02,
            "size": 0.3,
            "sourcesize": 0.02,
            "cloudletanimperiod": 1,
            "cloudletsize": 1,
            "cloudletshape": "cloudletClouds",
            "cloudletcolor": [1,1,1,0],
            "timetolive": 0,
            "initt": 0,
            "deltat": 0,
            # Class: CfgWeapons|Default|GunClouds|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunClouds|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        "texturetype": "default",
        "inertia": 0.5,
        "aimtransitionspeed": 1
    },
    # Class: CfgWeapons|Put|DirectionalMineRangeMuzzle [Indent level: 1],
    "directionalminerangemuzzle": {
        # Compatible Magazines: magazines parameter (+ inherited)
        "magazines": [
            "democharge_remote_mag","iedurbansmall_remote_mag","iedlandsmall_remote_mag","satchelcharge_remote_mag"
            "iedurbanbig_remote_mag","iedlandbig_remote_mag","atmine_range_mag","claymoredirectionalmine_remote_mag"
            "apersmine_range_mag","apersboundingmine_range_mag","slamdirectionalmine_wire_mag","aperstripmine_wire_mag"
            "apersminedispenser_mag","trainingmine_mag","rhs_mine_pmn2_mag","rhs_mine_tm62m_mag"
            "rhs_mine_msk40p_white_mag","rhs_mine_msk40p_red_mag","rhs_mine_msk40p_green_mag","rhs_mine_msk40p_blue_mag"
            "rhs_mine_sm320_white_mag","rhs_mine_sm320_red_mag","rhs_mine_sm320_green_mag","rhs_mine_ozm72_a_mag"
            "rhs_mine_ozm72_b_mag","rhs_mine_ozm72_c_mag","rhs_ec75_mag","rhs_ec200_mag"
            "rhs_ec400_mag","rhs_ec75_sand_mag","rhs_ec200_sand_mag","rhs_ec400_sand_mag"
            "rhs_mine_m19_mag","rhsusf_mine_m14_mag","rhsusf_mine_m49a1_3m_mag","rhsusf_mine_m49a1_6m_mag"
            "rhsusf_mine_m49a1_10m_mag","rhsusf_m112_mag","rhsusf_m112x4_mag","rhs_mag_mine_pfm1"
            "rhs_mag_mine_ptm1","rhs_mine_smine35_press_mag","rhs_mine_smine35_trip_mag","rhs_mine_smine44_press_mag"
            "rhs_mine_smine44_trip_mag","rhs_mine_glasmine43_hz_mag","rhs_mine_glasmine43_bz_mag","rhs_mine_stockmine43_2m_mag"
            "rhs_mine_stockmine43_4m_mag","rhs_mine_a200_bz_mag","rhs_mine_a200_dz35_mag","rhs_mine_tm43_mag"
            "rhs_mine_m2a3b_press_mag","rhs_mine_m2a3b_trip_mag","rhs_mine_m3_pressure_mag","rhs_mine_mk2_pressure_mag"
            "rhs_mine_m3_tripwire_mag","rhs_mine_mk2_tripwire_mag","rhs_mine_m7a2_mag","rhs_charge_m2tet_x2_mag"
            "rhssaf_mine_pma3_mag","rhssaf_mine_tma4_mag","rhssaf_mine_mrud_a_mag","rhssaf_mine_mrud_b_mag"
            "rhssaf_mine_mrud_c_mag","rhssaf_mine_mrud_d_mag","rhssaf_tm100_mag","rhssaf_tm200_mag"
            "rhssaf_tm500_mag",],
        "displayname": "M6 SLAM Mine",
        "autoreload": 0,
        "enableattack": 1,
        "picture": "A3|Weapons_F|Data|clear_empty.paa",
        "showtoplayer": 0,
        # Class: CfgWeapons|Put|ClassicMineRangeMuzzle|EventHandlers [Indent level: 2],
        "eventhandlers": {
            "fired": "['firedMine',_this] call bis_fnc_showLawOfWar;"
        },
        "sound": ["",0.000316228,1],
        "reloadsound": ["",0.000316228,1],
        "optics": 0,
        "showempty": 0,
        "canlock": 0,
        "primary": 10,
        "minrange": 0,
        "minrangeprobab": 0.1,
        "midrange": 3,
        "midrangeprobab": 0.9,
        "maxrange": 15,
        "maxrangeprobab": 0.04,
        "movetointernal": 0,
        "opticszoommin": 0.25,
        "opticszoommax": 1.25,
        "opticszoominit": 0.75,
        "access": 3,
        "scope": 0,
        "value": 2,
        "uipicture": "",
        "ammo": "",
        "cursor": "",
        "cursoraim": "",
        "cursorsize": 1,
        "showaimcursorinternal": 1,
        "cursoraimon": "",
        "laser": 0,
        "hiddenselections": [],
        "hiddenselectionstextures": [],
        "hiddenunderwaterselections": [],
        "shownunderwaterselections": [],
        "hiddenunderwaterselectionstextures": [],
        "simulation": "Weapon",
        "type": 65536,
        "namesound": "",
        "count": 0,
        "multiplier": 1,
        "burst": 1,
        "magazinereloadtime": 0,
        "reloadtime": 1,
        "magazinereloadswitchphase": 1,
        "soundbegin": ["sound",1],
        "soundbeginwater": ["sound",1],
        "soundclosure": ["sound",1],
        "soundend": ["sound",1],
        "soundloop": ["sound",1],
        "soundcontinuous": 0,
        "weaponsoundeffect": "",
        "soundburst": 1,
        "drysound": ["",1,1],
        "zeroingsound": ["",1,1],
        "changefiremodesound": ["",1,1],
        "reloadmagazinesound": ["",1,1],
        "emptysound": ["",1,1],
        "soundbullet": ["emptySound",1],
        "initspeed": 0,
        "ballisticscomputer": 0,
        "irdistance": 0,
        "irdotintensity": 0.001,
        "dispersion": 0.002,
        "aidispersioncoefx": 1,
        "aidispersioncoefy": 1,
        "lockacquire": 1,
        "ffmagnitude": 0,
        "fffrequency": 1,
        "ffcount": 1,
        # Recoil Array: recoil,
        "recoil": [],
        "recoil": "empty",
        "recoilprone": "",
        "maxrecoilsway": 0.008,
        "swaydecayspeed": 2,
        "model": "",
        "modelspecial": "",
        "modelmagazine": "",
        "muzzlepos": "usti hlavne",
        "muzzleend": "konec hlavne",
        "irlaserpos": "laser pos",
        "irlaserend": "laser dir",
        "cartridgepos": "nabojnicestart",
        "cartridgevel": "nabojniceend",
        "selectionfireanim": "zasleh",
        "memorypointcamera": "eye",
        "firespreadangle": 3,
        "usemodeloptics": 1,
        "opticsid": 0,
        "modeloptics": "",
        "opticsppeffects": [],
        "opticsflare": 1,
        "forceoptics": 0,
        "useasbinocular": 0,
        "opticsdisableperipherialvision": 0.67,
        "distancezoommin": 400,
        "distancezoommax": 400,
        "showswitchaction": 0,
        "autofire": 0,
        "canshootinwater": 0,
        "airateoffire": 5,
        "airateoffiredistance": 500,
        "airateoffiredispersion": 0,
        "firelightduration": 0.05,
        "firelightintensity": 0.2,
        "firelightdiffuse": [0.937,0.631,0.259],
        "firelightambient": [0,0,0],
        "backgroundreload": 0,
        "reloadaction": "",
        "muzzles": ["this"],
        "modes": ["this"],
        "useaction": 0,
        "useactiontitle": "",
        "candrop": 1,
        "weaponlockdelay": 0,
        "weaponlocksystem": 0,
        "cmimmunity": 1,
        "weight": 0,
        "handanim": [],
        "lockingtargetsound": ["",0.000316228,2],
        "lockedtargetsound": ["",0.000316228,6],
        "detectrange": 0,
        "artillerydispersion": 1,
        "artillerycharge": 1,
        "fireanims": [],
        # Class: CfgWeapons|Default|Library [Indent level: 1],
        "library": {
            "libtextdesc": ""
        },
        "descriptionshort": "",
        # Class: CfgWeapons|Default|GunFire [Indent level: 1],
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
            "cloudletdensitycoef": -1,
            "interval": -0.01,
            "size": 3,
            "sourcesize": 0.5,
            "timetolive": 0,
            "initt": 4500,
            "deltat": -3000,
            # Class: CfgWeapons|Default|GunFire|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunFire|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [0.82,0.95,0.93,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T1 [Indent level: 3],
                "t1": {
                    "maxt": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T2 [Indent level: 3],
                "t2": {
                    "maxt": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T3 [Indent level: 3],
                "t3": {
                    "maxt": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T4 [Indent level: 3],
                "t4": {
                    "maxt": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T5 [Indent level: 3],
                "t5": {
                    "maxt": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T6 [Indent level: 3],
                "t6": {
                    "maxt": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T7 [Indent level: 3],
                "t7": {
                    "maxt": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T8 [Indent level: 3],
                "t8": {
                    "maxt": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T9 [Indent level: 3],
                "t9": {
                    "maxt": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T10 [Indent level: 3],
                "t10": {
                    "maxt": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T11 [Indent level: 3],
                "t11": {
                    "maxt": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T12 [Indent level: 3],
                "t12": {
                    "maxt": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T13 [Indent level: 3],
                "t13": {
                    "maxt": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T14 [Indent level: 3],
                "t14": {
                    "maxt": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T15 [Indent level: 3],
                "t15": {
                    "maxt": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T16 [Indent level: 3],
                "t16": {
                    "maxt": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T17 [Indent level: 3],
                "t17": {
                    "maxt": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T18 [Indent level: 3],
                "t18": {
                    "maxt": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T19 [Indent level: 3],
                "t19": {
                    "maxt": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T20 [Indent level: 3],
                "t20": {
                    "maxt": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T21 [Indent level: 3],
                "t21": {
                    "maxt": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T22 [Indent level: 3],
                "t22": {
                    "maxt": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgWeapons|Default|GunClouds [Indent level: 1],
        "gunclouds": {
            "access": 0,
            "cloudletgrowup": 0.05,
            "cloudletfadein": 0,
            "cloudletfadeout": 0.1,
            "cloudletduration": 0.05,
            "cloudletalpha": 0.3,
            "cloudletaccy": 0,
            "cloudletminyspeed": -100,
            "cloudletmaxyspeed": 100,
            "interval": -0.02,
            "size": 0.3,
            "sourcesize": 0.02,
            "cloudletanimperiod": 1,
            "cloudletsize": 1,
            "cloudletshape": "cloudletClouds",
            "cloudletcolor": [1,1,1,0],
            "timetolive": 0,
            "initt": 0,
            "deltat": 0,
            # Class: CfgWeapons|Default|GunClouds|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunClouds|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        "texturetype": "default",
        "inertia": 0.5,
        "aimtransitionspeed": 1
    },
    # Class: CfgWeapons|Put|ClassicMineWireMuzzle [Indent level: 1],
    "classicminewiremuzzle": {
        # Compatible Magazines: magazines parameter (+ inherited)
        "magazines": [
            "democharge_remote_mag","iedurbansmall_remote_mag","iedlandsmall_remote_mag","satchelcharge_remote_mag"
            "iedurbanbig_remote_mag","iedlandbig_remote_mag","atmine_range_mag","claymoredirectionalmine_remote_mag"
            "apersmine_range_mag","apersboundingmine_range_mag","slamdirectionalmine_wire_mag","aperstripmine_wire_mag"
            "apersminedispenser_mag","trainingmine_mag","rhs_mine_pmn2_mag","rhs_mine_tm62m_mag"
            "rhs_mine_msk40p_white_mag","rhs_mine_msk40p_red_mag","rhs_mine_msk40p_green_mag","rhs_mine_msk40p_blue_mag"
            "rhs_mine_sm320_white_mag","rhs_mine_sm320_red_mag","rhs_mine_sm320_green_mag","rhs_mine_ozm72_a_mag"
            "rhs_mine_ozm72_b_mag","rhs_mine_ozm72_c_mag","rhs_ec75_mag","rhs_ec200_mag"
            "rhs_ec400_mag","rhs_ec75_sand_mag","rhs_ec200_sand_mag","rhs_ec400_sand_mag"
            "rhs_mine_m19_mag","rhsusf_mine_m14_mag","rhsusf_mine_m49a1_3m_mag","rhsusf_mine_m49a1_6m_mag"
            "rhsusf_mine_m49a1_10m_mag","rhsusf_m112_mag","rhsusf_m112x4_mag","rhs_mag_mine_pfm1"
            "rhs_mag_mine_ptm1","rhs_mine_smine35_press_mag","rhs_mine_smine35_trip_mag","rhs_mine_smine44_press_mag"
            "rhs_mine_smine44_trip_mag","rhs_mine_glasmine43_hz_mag","rhs_mine_glasmine43_bz_mag","rhs_mine_stockmine43_2m_mag"
            "rhs_mine_stockmine43_4m_mag","rhs_mine_a200_bz_mag","rhs_mine_a200_dz35_mag","rhs_mine_tm43_mag"
            "rhs_mine_m2a3b_press_mag","rhs_mine_m2a3b_trip_mag","rhs_mine_m3_pressure_mag","rhs_mine_mk2_pressure_mag"
            "rhs_mine_m3_tripwire_mag","rhs_mine_mk2_tripwire_mag","rhs_mine_m7a2_mag","rhs_charge_m2tet_x2_mag"
            "rhssaf_mine_pma3_mag","rhssaf_mine_tma4_mag","rhssaf_mine_mrud_a_mag","rhssaf_mine_mrud_b_mag"
            "rhssaf_mine_mrud_c_mag","rhssaf_mine_mrud_d_mag","rhssaf_tm100_mag","rhssaf_tm200_mag"
            "rhssaf_tm500_mag",],
        "displayname": "APERS Tripwire Mine",
        "autoreload": 0,
        "enableattack": 1,
        "picture": "A3|Weapons_F|Data|clear_empty.paa",
        "showtoplayer": 0,
        # Class: CfgWeapons|Put|ClassicMineRangeMuzzle|EventHandlers [Indent level: 2],
        "eventhandlers": {
            "fired": "['firedMine',_this] call bis_fnc_showLawOfWar;"
        },
        "sound": ["",0.000316228,1],
        "reloadsound": ["",0.000316228,1],
        "optics": 0,
        "showempty": 0,
        "canlock": 0,
        "primary": 10,
        "minrange": 0,
        "minrangeprobab": 0.1,
        "midrange": 3,
        "midrangeprobab": 0.9,
        "maxrange": 15,
        "maxrangeprobab": 0.04,
        "movetointernal": 0,
        "opticszoommin": 0.25,
        "opticszoommax": 1.25,
        "opticszoominit": 0.75,
        "access": 3,
        "scope": 0,
        "value": 2,
        "uipicture": "",
        "ammo": "",
        "cursor": "",
        "cursoraim": "",
        "cursorsize": 1,
        "showaimcursorinternal": 1,
        "cursoraimon": "",
        "laser": 0,
        "hiddenselections": [],
        "hiddenselectionstextures": [],
        "hiddenunderwaterselections": [],
        "shownunderwaterselections": [],
        "hiddenunderwaterselectionstextures": [],
        "simulation": "Weapon",
        "type": 65536,
        "namesound": "",
        "count": 0,
        "multiplier": 1,
        "burst": 1,
        "magazinereloadtime": 0,
        "reloadtime": 1,
        "magazinereloadswitchphase": 1,
        "soundbegin": ["sound",1],
        "soundbeginwater": ["sound",1],
        "soundclosure": ["sound",1],
        "soundend": ["sound",1],
        "soundloop": ["sound",1],
        "soundcontinuous": 0,
        "weaponsoundeffect": "",
        "soundburst": 1,
        "drysound": ["",1,1],
        "zeroingsound": ["",1,1],
        "changefiremodesound": ["",1,1],
        "reloadmagazinesound": ["",1,1],
        "emptysound": ["",1,1],
        "soundbullet": ["emptySound",1],
        "initspeed": 0,
        "ballisticscomputer": 0,
        "irdistance": 0,
        "irdotintensity": 0.001,
        "dispersion": 0.002,
        "aidispersioncoefx": 1,
        "aidispersioncoefy": 1,
        "lockacquire": 1,
        "ffmagnitude": 0,
        "fffrequency": 1,
        "ffcount": 1,
        # Recoil Array: recoil,
        "recoil": [],
        "recoil": "empty",
        "recoilprone": "",
        "maxrecoilsway": 0.008,
        "swaydecayspeed": 2,
        "model": "",
        "modelspecial": "",
        "modelmagazine": "",
        "muzzlepos": "usti hlavne",
        "muzzleend": "konec hlavne",
        "irlaserpos": "laser pos",
        "irlaserend": "laser dir",
        "cartridgepos": "nabojnicestart",
        "cartridgevel": "nabojniceend",
        "selectionfireanim": "zasleh",
        "memorypointcamera": "eye",
        "firespreadangle": 3,
        "usemodeloptics": 1,
        "opticsid": 0,
        "modeloptics": "",
        "opticsppeffects": [],
        "opticsflare": 1,
        "forceoptics": 0,
        "useasbinocular": 0,
        "opticsdisableperipherialvision": 0.67,
        "distancezoommin": 400,
        "distancezoommax": 400,
        "showswitchaction": 0,
        "autofire": 0,
        "canshootinwater": 0,
        "airateoffire": 5,
        "airateoffiredistance": 500,
        "airateoffiredispersion": 0,
        "firelightduration": 0.05,
        "firelightintensity": 0.2,
        "firelightdiffuse": [0.937,0.631,0.259],
        "firelightambient": [0,0,0],
        "backgroundreload": 0,
        "reloadaction": "",
        "muzzles": ["this"],
        "modes": ["this"],
        "useaction": 0,
        "useactiontitle": "",
        "candrop": 1,
        "weaponlockdelay": 0,
        "weaponlocksystem": 0,
        "cmimmunity": 1,
        "weight": 0,
        "handanim": [],
        "lockingtargetsound": ["",0.000316228,2],
        "lockedtargetsound": ["",0.000316228,6],
        "detectrange": 0,
        "artillerydispersion": 1,
        "artillerycharge": 1,
        "fireanims": [],
        # Class: CfgWeapons|Default|Library [Indent level: 1],
        "library": {
            "libtextdesc": ""
        },
        "descriptionshort": "",
        # Class: CfgWeapons|Default|GunFire [Indent level: 1],
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
            "cloudletdensitycoef": -1,
            "interval": -0.01,
            "size": 3,
            "sourcesize": 0.5,
            "timetolive": 0,
            "initt": 4500,
            "deltat": -3000,
            # Class: CfgWeapons|Default|GunFire|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunFire|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [0.82,0.95,0.93,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T1 [Indent level: 3],
                "t1": {
                    "maxt": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T2 [Indent level: 3],
                "t2": {
                    "maxt": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T3 [Indent level: 3],
                "t3": {
                    "maxt": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T4 [Indent level: 3],
                "t4": {
                    "maxt": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T5 [Indent level: 3],
                "t5": {
                    "maxt": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T6 [Indent level: 3],
                "t6": {
                    "maxt": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T7 [Indent level: 3],
                "t7": {
                    "maxt": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T8 [Indent level: 3],
                "t8": {
                    "maxt": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T9 [Indent level: 3],
                "t9": {
                    "maxt": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T10 [Indent level: 3],
                "t10": {
                    "maxt": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T11 [Indent level: 3],
                "t11": {
                    "maxt": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T12 [Indent level: 3],
                "t12": {
                    "maxt": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T13 [Indent level: 3],
                "t13": {
                    "maxt": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T14 [Indent level: 3],
                "t14": {
                    "maxt": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T15 [Indent level: 3],
                "t15": {
                    "maxt": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T16 [Indent level: 3],
                "t16": {
                    "maxt": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T17 [Indent level: 3],
                "t17": {
                    "maxt": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T18 [Indent level: 3],
                "t18": {
                    "maxt": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T19 [Indent level: 3],
                "t19": {
                    "maxt": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T20 [Indent level: 3],
                "t20": {
                    "maxt": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T21 [Indent level: 3],
                "t21": {
                    "maxt": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T22 [Indent level: 3],
                "t22": {
                    "maxt": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgWeapons|Default|GunClouds [Indent level: 1],
        "gunclouds": {
            "access": 0,
            "cloudletgrowup": 0.05,
            "cloudletfadein": 0,
            "cloudletfadeout": 0.1,
            "cloudletduration": 0.05,
            "cloudletalpha": 0.3,
            "cloudletaccy": 0,
            "cloudletminyspeed": -100,
            "cloudletmaxyspeed": 100,
            "interval": -0.02,
            "size": 0.3,
            "sourcesize": 0.02,
            "cloudletanimperiod": 1,
            "cloudletsize": 1,
            "cloudletshape": "cloudletClouds",
            "cloudletcolor": [1,1,1,0],
            "timetolive": 0,
            "initt": 0,
            "deltat": 0,
            # Class: CfgWeapons|Default|GunClouds|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunClouds|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        "texturetype": "default",
        "inertia": 0.5,
        "aimtransitionspeed": 1
    },
    # Class: CfgWeapons|Put|DirectionalMineRemoteMuzzle [Indent level: 1],
    "directionalmineremotemuzzle": {
        "autoreload": 0,
        "enableattack": 1,
        # Compatible Magazines: magazines parameter (+ inherited),
        "magazines": [
            "democharge_remote_mag","iedurbansmall_remote_mag","iedlandsmall_remote_mag","satchelcharge_remote_mag",
            "iedurbanbig_remote_mag","iedlandbig_remote_mag","atmine_range_mag","claymoredirectionalmine_remote_mag",
            "apersmine_range_mag","apersboundingmine_range_mag","slamdirectionalmine_wire_mag","aperstripmine_wire_mag",
            "apersminedispenser_mag","trainingmine_mag","rhs_mine_pmn2_mag","rhs_mine_tm62m_mag",
            "rhs_mine_msk40p_white_mag","rhs_mine_msk40p_red_mag","rhs_mine_msk40p_green_mag","rhs_mine_msk40p_blue_mag",
            "rhs_mine_sm320_white_mag","rhs_mine_sm320_red_mag","rhs_mine_sm320_green_mag","rhs_mine_ozm72_a_mag",
            "rhs_mine_ozm72_b_mag","rhs_mine_ozm72_c_mag","rhs_ec75_mag","rhs_ec200_mag",
            "rhs_ec400_mag","rhs_ec75_sand_mag","rhs_ec200_sand_mag","rhs_ec400_sand_mag",
            "rhs_mine_m19_mag","rhsusf_mine_m14_mag","rhsusf_mine_m49a1_3m_mag","rhsusf_mine_m49a1_6m_mag",
            "rhsusf_mine_m49a1_10m_mag","rhsusf_m112_mag","rhsusf_m112x4_mag","rhs_mag_mine_pfm1",
            "rhs_mag_mine_ptm1","rhs_mine_smine35_press_mag","rhs_mine_smine35_trip_mag","rhs_mine_smine44_press_mag",
            "rhs_mine_smine44_trip_mag","rhs_mine_glasmine43_hz_mag","rhs_mine_glasmine43_bz_mag","rhs_mine_stockmine43_2m_mag",
            "rhs_mine_stockmine43_4m_mag","rhs_mine_a200_bz_mag","rhs_mine_a200_dz35_mag","rhs_mine_tm43_mag",
            "rhs_mine_m2a3b_press_mag","rhs_mine_m2a3b_trip_mag","rhs_mine_m3_pressure_mag","rhs_mine_mk2_pressure_mag",
            "rhs_mine_m3_tripwire_mag","rhs_mine_mk2_tripwire_mag","rhs_mine_m7a2_mag","rhs_charge_m2tet_x2_mag",
            "rhssaf_mine_pma3_mag","rhssaf_mine_tma4_mag","rhssaf_mine_mrud_a_mag","rhssaf_mine_mrud_b_mag",
            "rhssaf_mine_mrud_c_mag","rhssaf_mine_mrud_d_mag","rhssaf_tm100_mag","rhssaf_tm200_mag",
            "rhssaf_tm500_mag",],
        "displayname": "Claymore Charge",
        "picture": "A3|Weapons_F|Data|clear_empty.paa",
        "showtoplayer": 0,
        "sound": ["",0.000316228,1],
        "reloadsound": ["",0.000316228,1],
        "optics": 0,
        "showempty": 0,
        "canlock": 0,
        "primary": 10,
        "minrange": 0,
        "minrangeprobab": 0.1,
        "midrange": 3,
        "midrangeprobab": 0.9,
        "maxrange": 15,
        "maxrangeprobab": 0.04,
        "movetointernal": 0,
        "opticszoommin": 0.25,
        "opticszoommax": 1.25,
        "opticszoominit": 0.75,
        "access": 3,
        "scope": 0,
        "value": 2,
        "uipicture": "",
        "ammo": "",
        "cursor": "",
        "cursoraim": "",
        "cursorsize": 1,
        "showaimcursorinternal": 1,
        "cursoraimon": "",
        "laser": 0,
        "hiddenselections": [],
        "hiddenselectionstextures": [],
        "hiddenunderwaterselections": [],
        "shownunderwaterselections": [],
        "hiddenunderwaterselectionstextures": [],
        "simulation": "Weapon",
        "type": 65536,
        "namesound": "",
        "count": 0,
        "multiplier": 1,
        "burst": 1,
        "magazinereloadtime": 0,
        "reloadtime": 1,
        "magazinereloadswitchphase": 1,
        "soundbegin": ["sound",1],
        "soundbeginwater": ["sound",1],
        "soundclosure": ["sound",1],
        "soundend": ["sound",1],
        "soundloop": ["sound",1],
        "soundcontinuous": 0,
        "weaponsoundeffect": "",
        "soundburst": 1,
        "drysound": ["",1,1],
        "zeroingsound": ["",1,1],
        "changefiremodesound": ["",1,1],
        "reloadmagazinesound": ["",1,1],
        "emptysound": ["",1,1],
        "soundbullet": ["emptySound",1],
        "initspeed": 0,
        "ballisticscomputer": 0,
        "irdistance": 0,
        "irdotintensity": 0.001,
        "dispersion": 0.002,
        "aidispersioncoefx": 1,
        "aidispersioncoefy": 1,
        "lockacquire": 1,
        "ffmagnitude": 0,
        "fffrequency": 1,
        "ffcount": 1,
        # Recoil Array: recoil,
        "recoil": [],
        "recoil": "empty",
        "recoilprone": "",
        "maxrecoilsway": 0.008,
        "swaydecayspeed": 2,
        "model": "",
        "modelspecial": "",
        "modelmagazine": "",
        "muzzlepos": "usti hlavne",
        "muzzleend": "konec hlavne",
        "irlaserpos": "laser pos",
        "irlaserend": "laser dir",
        "cartridgepos": "nabojnicestart",
        "cartridgevel": "nabojniceend",
        "selectionfireanim": "zasleh",
        "memorypointcamera": "eye",
        "firespreadangle": 3,
        "usemodeloptics": 1,
        "opticsid": 0,
        "modeloptics": "",
        "opticsppeffects": [],
        "opticsflare": 1,
        "forceoptics": 0,
        "useasbinocular": 0,
        "opticsdisableperipherialvision": 0.67,
        "distancezoommin": 400,
        "distancezoommax": 400,
        "showswitchaction": 0,
        "autofire": 0,
        "canshootinwater": 0,
        "airateoffire": 5,
        "airateoffiredistance": 500,
        "airateoffiredispersion": 0,
        "firelightduration": 0.05,
        "firelightintensity": 0.2,
        "firelightdiffuse": [0.937,0.631,0.259],
        "firelightambient": [0,0,0],
        # Class: CfgWeapons|Default|Eventhandlers [Indent level: 1],
        "eventhandlers": {
        },
        "backgroundreload": 0,
        "reloadaction": "",
        "muzzles": ["this"],
        "modes": ["this"],
        "useaction": 0,
        "useactiontitle": "",
        "candrop": 1,
        "weaponlockdelay": 0,
        "weaponlocksystem": 0,
        "cmimmunity": 1,
        "weight": 0,
        "handanim": [],
        "lockingtargetsound": ["",0.000316228,2],
        "lockedtargetsound": ["",0.000316228,6],
        "detectrange": 0,
        "artillerydispersion": 1,
        "artillerycharge": 1,
        "fireanims": [],
        # Class: CfgWeapons|Default|Library [Indent level: 1],
        "library": {
            "libtextdesc": ""
        },
        "descriptionshort": "",
        # Class: CfgWeapons|Default|GunFire [Indent level: 1],
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
            "cloudletdensitycoef": -1,
            "interval": -0.01,
            "size": 3,
            "sourcesize": 0.5,
            "timetolive": 0,
            "initt": 4500,
            "deltat": -3000,
            # Class: CfgWeapons|Default|GunFire|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunFire|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [0.82,0.95,0.93,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T1 [Indent level: 3],
                "t1": {
                    "maxt": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T2 [Indent level: 3],
                "t2": {
                    "maxt": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T3 [Indent level: 3],
                "t3": {
                    "maxt": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T4 [Indent level: 3],
                "t4": {
                    "maxt": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T5 [Indent level: 3],
                "t5": {
                    "maxt": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T6 [Indent level: 3],
                "t6": {
                    "maxt": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T7 [Indent level: 3],
                "t7": {
                    "maxt": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T8 [Indent level: 3],
                "t8": {
                    "maxt": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T9 [Indent level: 3],
                "t9": {
                    "maxt": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T10 [Indent level: 3],
                "t10": {
                    "maxt": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T11 [Indent level: 3],
                "t11": {
                    "maxt": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T12 [Indent level: 3],
                "t12": {
                    "maxt": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T13 [Indent level: 3],
                "t13": {
                    "maxt": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T14 [Indent level: 3],
                "t14": {
                    "maxt": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T15 [Indent level: 3],
                "t15": {
                    "maxt": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T16 [Indent level: 3],
                "t16": {
                    "maxt": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T17 [Indent level: 3],
                "t17": {
                    "maxt": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T18 [Indent level: 3],
                "t18": {
                    "maxt": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T19 [Indent level: 3],
                "t19": {
                    "maxt": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T20 [Indent level: 3],
                "t20": {
                    "maxt": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T21 [Indent level: 3],
                "t21": {
                    "maxt": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T22 [Indent level: 3],
                "t22": {
                    "maxt": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgWeapons|Default|GunClouds [Indent level: 1],
        "gunclouds": {
            "access": 0,
            "cloudletgrowup": 0.05,
            "cloudletfadein": 0,
            "cloudletfadeout": 0.1,
            "cloudletduration": 0.05,
            "cloudletalpha": 0.3,
            "cloudletaccy": 0,
            "cloudletminyspeed": -100,
            "cloudletmaxyspeed": 100,
            "interval": -0.02,
            "size": 0.3,
            "sourcesize": 0.02,
            "cloudletanimperiod": 1,
            "cloudletsize": 1,
            "cloudletshape": "cloudletClouds",
            "cloudletcolor": [1,1,1,0],
            "timetolive": 0,
            "initt": 0,
            "deltat": 0,
            # Class: CfgWeapons|Default|GunClouds|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunClouds|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        "texturetype": "default",
        "inertia": 0.5,
        "aimtransitionspeed": 1
    },
    # Class: CfgWeapons|Put|DemoChargeMuzzle [Indent level: 1],
    "demochargemuzzle": {
        "autoreload": 0,
        "displayname": "Explosive Charge",
        # Compatible Magazines: magazines parameter (+ inherited),
        "magazines": [
            "democharge_remote_mag","iedurbansmall_remote_mag","iedlandsmall_remote_mag","satchelcharge_remote_mag",
            "iedurbanbig_remote_mag","iedlandbig_remote_mag","atmine_range_mag","claymoredirectionalmine_remote_mag",
            "apersmine_range_mag","apersboundingmine_range_mag","slamdirectionalmine_wire_mag","aperstripmine_wire_mag",
            "apersminedispenser_mag","trainingmine_mag","rhs_mine_pmn2_mag","rhs_mine_tm62m_mag",
            "rhs_mine_msk40p_white_mag","rhs_mine_msk40p_red_mag","rhs_mine_msk40p_green_mag","rhs_mine_msk40p_blue_mag",
            "rhs_mine_sm320_white_mag","rhs_mine_sm320_red_mag","rhs_mine_sm320_green_mag","rhs_mine_ozm72_a_mag",
            "rhs_mine_ozm72_b_mag","rhs_mine_ozm72_c_mag","rhs_ec75_mag","rhs_ec200_mag",
            "rhs_ec400_mag","rhs_ec75_sand_mag","rhs_ec200_sand_mag","rhs_ec400_sand_mag",
            "rhs_mine_m19_mag","rhsusf_mine_m14_mag","rhsusf_mine_m49a1_3m_mag","rhsusf_mine_m49a1_6m_mag",
            "rhsusf_mine_m49a1_10m_mag","rhsusf_m112_mag","rhsusf_m112x4_mag","rhs_mag_mine_pfm1",
            "rhs_mag_mine_ptm1","rhs_mine_smine35_press_mag","rhs_mine_smine35_trip_mag","rhs_mine_smine44_press_mag",
            "rhs_mine_smine44_trip_mag","rhs_mine_glasmine43_hz_mag","rhs_mine_glasmine43_bz_mag","rhs_mine_stockmine43_2m_mag",
            "rhs_mine_stockmine43_4m_mag","rhs_mine_a200_bz_mag","rhs_mine_a200_dz35_mag","rhs_mine_tm43_mag",
            "rhs_mine_m2a3b_press_mag","rhs_mine_m2a3b_trip_mag","rhs_mine_m3_pressure_mag","rhs_mine_mk2_pressure_mag",
            "rhs_mine_m3_tripwire_mag","rhs_mine_mk2_tripwire_mag","rhs_mine_m7a2_mag","rhs_charge_m2tet_x2_mag",
            "rhssaf_mine_pma3_mag","rhssaf_mine_tma4_mag","rhssaf_mine_mrud_a_mag","rhssaf_mine_mrud_b_mag",
            "rhssaf_mine_mrud_c_mag","rhssaf_mine_mrud_d_mag","rhssaf_tm100_mag","rhssaf_tm200_mag",
            "rhssaf_tm500_mag",],
        "enableattack": 1,
        "showtoplayer": 0,
        "sound": ["",0.000316228,1],
        "reloadsound": ["",0.000316228,1],
        "optics": 0,
        "showempty": 0,
        "canlock": 0,
        "primary": 10,
        "minrange": 0,
        "minrangeprobab": 0.1,
        "midrange": 3,
        "midrangeprobab": 0.9,
        "maxrange": 15,
        "maxrangeprobab": 0.04,
        "movetointernal": 0,
        "opticszoommin": 0.25,
        "opticszoommax": 1.25,
        "opticszoominit": 0.75,
        "access": 3,
        "scope": 0,
        "value": 2,
        "picture": "",
        "uipicture": "",
        "ammo": "",
        "cursor": "",
        "cursoraim": "",
        "cursorsize": 1,
        "showaimcursorinternal": 1,
        "cursoraimon": "",
        "laser": 0,
        "hiddenselections": [],
        "hiddenselectionstextures": [],
        "hiddenunderwaterselections": [],
        "shownunderwaterselections": [],
        "hiddenunderwaterselectionstextures": [],
        "simulation": "Weapon",
        "type": 65536,
        "namesound": "",
        "count": 0,
        "multiplier": 1,
        "burst": 1,
        "magazinereloadtime": 0,
        "reloadtime": 1,
        "magazinereloadswitchphase": 1,
        "soundbegin": ["sound",1],
        "soundbeginwater": ["sound",1],
        "soundclosure": ["sound",1],
        "soundend": ["sound",1],
        "soundloop": ["sound",1],
        "soundcontinuous": 0,
        "weaponsoundeffect": "",
        "soundburst": 1,
        "drysound": ["",1,1],
        "zeroingsound": ["",1,1],
        "changefiremodesound": ["",1,1],
        "reloadmagazinesound": ["",1,1],
        "emptysound": ["",1,1],
        "soundbullet": ["emptySound",1],
        "initspeed": 0,
        "ballisticscomputer": 0,
        "irdistance": 0,
        "irdotintensity": 0.001,
        "dispersion": 0.002,
        "aidispersioncoefx": 1,
        "aidispersioncoefy": 1,
        "lockacquire": 1,
        "ffmagnitude": 0,
        "fffrequency": 1,
        "ffcount": 1,
        # Recoil Array: recoil,
        "recoil": [],
        "recoil": "empty",
        "recoilprone": "",
        "maxrecoilsway": 0.008,
        "swaydecayspeed": 2,
        "model": "",
        "modelspecial": "",
        "modelmagazine": "",
        "muzzlepos": "usti hlavne",
        "muzzleend": "konec hlavne",
        "irlaserpos": "laser pos",
        "irlaserend": "laser dir",
        "cartridgepos": "nabojnicestart",
        "cartridgevel": "nabojniceend",
        "selectionfireanim": "zasleh",
        "memorypointcamera": "eye",
        "firespreadangle": 3,
        "usemodeloptics": 1,
        "opticsid": 0,
        "modeloptics": "",
        "opticsppeffects": [],
        "opticsflare": 1,
        "forceoptics": 0,
        "useasbinocular": 0,
        "opticsdisableperipherialvision": 0.67,
        "distancezoommin": 400,
        "distancezoommax": 400,
        "showswitchaction": 0,
        "autofire": 0,
        "canshootinwater": 0,
        "airateoffire": 5,
        "airateoffiredistance": 500,
        "airateoffiredispersion": 0,
        "firelightduration": 0.05,
        "firelightintensity": 0.2,
        "firelightdiffuse": [0.937,0.631,0.259],
        "firelightambient": [0,0,0],
        # Class: CfgWeapons|Default|Eventhandlers [Indent level: 1],
        "eventhandlers": {
        },
        "backgroundreload": 0,
        "reloadaction": "",
        "muzzles": ["this"],
        "modes": ["this"],
        "useaction": 0,
        "useactiontitle": "",
        "candrop": 1,
        "weaponlockdelay": 0,
        "weaponlocksystem": 0,
        "cmimmunity": 1,
        "weight": 0,
        "handanim": [],
        "lockingtargetsound": ["",0.000316228,2],
        "lockedtargetsound": ["",0.000316228,6],
        "detectrange": 0,
        "artillerydispersion": 1,
        "artillerycharge": 1,
        "fireanims": [],
        # Class: CfgWeapons|Default|Library [Indent level: 1],
        "library": {
            "libtextdesc": ""
        },
        "descriptionshort": "",
        # Class: CfgWeapons|Default|GunFire [Indent level: 1],
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
            "cloudletdensitycoef": -1,
            "interval": -0.01,
            "size": 3,
            "sourcesize": 0.5,
            "timetolive": 0,
            "initt": 4500,
            "deltat": -3000,
            # Class: CfgWeapons|Default|GunFire|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunFire|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [0.82,0.95,0.93,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T1 [Indent level: 3],
                "t1": {
                    "maxt": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T2 [Indent level: 3],
                "t2": {
                    "maxt": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T3 [Indent level: 3],
                "t3": {
                    "maxt": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T4 [Indent level: 3],
                "t4": {
                    "maxt": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T5 [Indent level: 3],
                "t5": {
                    "maxt": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T6 [Indent level: 3],
                "t6": {
                    "maxt": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T7 [Indent level: 3],
                "t7": {
                    "maxt": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T8 [Indent level: 3],
                "t8": {
                    "maxt": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T9 [Indent level: 3],
                "t9": {
                    "maxt": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T10 [Indent level: 3],
                "t10": {
                    "maxt": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T11 [Indent level: 3],
                "t11": {
                    "maxt": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T12 [Indent level: 3],
                "t12": {
                    "maxt": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T13 [Indent level: 3],
                "t13": {
                    "maxt": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T14 [Indent level: 3],
                "t14": {
                    "maxt": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T15 [Indent level: 3],
                "t15": {
                    "maxt": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T16 [Indent level: 3],
                "t16": {
                    "maxt": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T17 [Indent level: 3],
                "t17": {
                    "maxt": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T18 [Indent level: 3],
                "t18": {
                    "maxt": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T19 [Indent level: 3],
                "t19": {
                    "maxt": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T20 [Indent level: 3],
                "t20": {
                    "maxt": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T21 [Indent level: 3],
                "t21": {
                    "maxt": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T22 [Indent level: 3],
                "t22": {
                    "maxt": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgWeapons|Default|GunClouds [Indent level: 1],
        "gunclouds": {
            "access": 0,
            "cloudletgrowup": 0.05,
            "cloudletfadein": 0,
            "cloudletfadeout": 0.1,
            "cloudletduration": 0.05,
            "cloudletalpha": 0.3,
            "cloudletaccy": 0,
            "cloudletminyspeed": -100,
            "cloudletmaxyspeed": 100,
            "interval": -0.02,
            "size": 0.3,
            "sourcesize": 0.02,
            "cloudletanimperiod": 1,
            "cloudletsize": 1,
            "cloudletshape": "cloudletClouds",
            "cloudletcolor": [1,1,1,0],
            "timetolive": 0,
            "initt": 0,
            "deltat": 0,
            # Class: CfgWeapons|Default|GunClouds|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunClouds|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        "texturetype": "default",
        "inertia": 0.5,
        "aimtransitionspeed": 1
    },
    # Class: CfgWeapons|Put|APERSMineDispenserMuzzle [Indent level: 1],
    "apersminedispensermuzzle": {
        "displayname": "APERS Mine Dispenser",
        # Compatible Magazines: magazines parameter (+ inherited),
        "magazines": [
            "democharge_remote_mag","iedurbansmall_remote_mag","iedlandsmall_remote_mag","satchelcharge_remote_mag",
            "iedurbanbig_remote_mag","iedlandbig_remote_mag","atmine_range_mag","claymoredirectionalmine_remote_mag",
            "apersmine_range_mag","apersboundingmine_range_mag","slamdirectionalmine_wire_mag","aperstripmine_wire_mag",
            "apersminedispenser_mag","trainingmine_mag","rhs_mine_pmn2_mag","rhs_mine_tm62m_mag",
            "rhs_mine_msk40p_white_mag","rhs_mine_msk40p_red_mag","rhs_mine_msk40p_green_mag","rhs_mine_msk40p_blue_mag",
            "rhs_mine_sm320_white_mag","rhs_mine_sm320_red_mag","rhs_mine_sm320_green_mag","rhs_mine_ozm72_a_mag",
            "rhs_mine_ozm72_b_mag","rhs_mine_ozm72_c_mag","rhs_ec75_mag","rhs_ec200_mag",
            "rhs_ec400_mag","rhs_ec75_sand_mag","rhs_ec200_sand_mag","rhs_ec400_sand_mag",
            "rhs_mine_m19_mag","rhsusf_mine_m14_mag","rhsusf_mine_m49a1_3m_mag","rhsusf_mine_m49a1_6m_mag",
            "rhsusf_mine_m49a1_10m_mag","rhsusf_m112_mag","rhsusf_m112x4_mag","rhs_mag_mine_pfm1",
            "rhs_mag_mine_ptm1","rhs_mine_smine35_press_mag","rhs_mine_smine35_trip_mag","rhs_mine_smine44_press_mag",
            "rhs_mine_smine44_trip_mag","rhs_mine_glasmine43_hz_mag","rhs_mine_glasmine43_bz_mag","rhs_mine_stockmine43_2m_mag",
            "rhs_mine_stockmine43_4m_mag","rhs_mine_a200_bz_mag","rhs_mine_a200_dz35_mag","rhs_mine_tm43_mag",
            "rhs_mine_m2a3b_press_mag","rhs_mine_m2a3b_trip_mag","rhs_mine_m3_pressure_mag","rhs_mine_mk2_pressure_mag",
            "rhs_mine_m3_tripwire_mag","rhs_mine_mk2_tripwire_mag","rhs_mine_m7a2_mag","rhs_charge_m2tet_x2_mag",
            "rhssaf_mine_pma3_mag","rhssaf_mine_tma4_mag","rhssaf_mine_mrud_a_mag","rhssaf_mine_mrud_b_mag",
            "rhssaf_mine_mrud_c_mag","rhssaf_mine_mrud_d_mag","rhssaf_tm100_mag","rhssaf_tm200_mag",
            "rhssaf_tm500_mag",],
        "showtoplayer": 0,
        "enableattack": 1,
        "autoreload": 0,
        "sound": ["",0.000316228,1],
        "reloadsound": ["",0.000316228,1],
        "optics": 0,
        "showempty": 0,
        "canlock": 0,
        "primary": 10,
        "minrange": 0,
        "minrangeprobab": 0.1,
        "midrange": 3,
        "midrangeprobab": 0.9,
        "maxrange": 15,
        "maxrangeprobab": 0.04,
        "movetointernal": 0,
        "opticszoommin": 0.25,
        "opticszoommax": 1.25,
        "opticszoominit": 0.75,
        "access": 3,
        "scope": 0,
        "value": 2,
        "picture": "",
        "uipicture": "",
        "ammo": "",
        "cursor": "",
        "cursoraim": "",
        "cursorsize": 1,
        "showaimcursorinternal": 1,
        "cursoraimon": "",
        "laser": 0,
        "hiddenselections": [],
        "hiddenselectionstextures": [],
        "hiddenunderwaterselections": [],
        "shownunderwaterselections": [],
        "hiddenunderwaterselectionstextures": [],
        "simulation": "Weapon",
        "type": 65536,
        "namesound": "",
        "count": 0,
        "multiplier": 1,
        "burst": 1,
        "magazinereloadtime": 0,
        "reloadtime": 1,
        "magazinereloadswitchphase": 1,
        "soundbegin": ["sound",1],
        "soundbeginwater": ["sound",1],
        "soundclosure": ["sound",1],
        "soundend": ["sound",1],
        "soundloop": ["sound",1],
        "soundcontinuous": 0,
        "weaponsoundeffect": "",
        "soundburst": 1,
        "drysound": ["",1,1],
        "zeroingsound": ["",1,1],
        "changefiremodesound": ["",1,1],
        "reloadmagazinesound": ["",1,1],
        "emptysound": ["",1,1],
        "soundbullet": ["emptySound",1],
        "initspeed": 0,
        "ballisticscomputer": 0,
        "irdistance": 0,
        "irdotintensity": 0.001,
        "dispersion": 0.002,
        "aidispersioncoefx": 1,
        "aidispersioncoefy": 1,
        "lockacquire": 1,
        "ffmagnitude": 0,
        "fffrequency": 1,
        "ffcount": 1,
        # Recoil Array: recoil,
        "recoil": [],
        "recoil": "empty",
        "recoilprone": "",
        "maxrecoilsway": 0.008,
        "swaydecayspeed": 2,
        "model": "",
        "modelspecial": "",
        "modelmagazine": "",
        "muzzlepos": "usti hlavne",
        "muzzleend": "konec hlavne",
        "irlaserpos": "laser pos",
        "irlaserend": "laser dir",
        "cartridgepos": "nabojnicestart",
        "cartridgevel": "nabojniceend",
        "selectionfireanim": "zasleh",
        "memorypointcamera": "eye",
        "firespreadangle": 3,
        "usemodeloptics": 1,
        "opticsid": 0,
        "modeloptics": "",
        "opticsppeffects": [],
        "opticsflare": 1,
        "forceoptics": 0,
        "useasbinocular": 0,
        "opticsdisableperipherialvision": 0.67,
        "distancezoommin": 400,
        "distancezoommax": 400,
        "showswitchaction": 0,
        "autofire": 0,
        "canshootinwater": 0,
        "airateoffire": 5,
        "airateoffiredistance": 500,
        "airateoffiredispersion": 0,
        "firelightduration": 0.05,
        "firelightintensity": 0.2,
        "firelightdiffuse": [0.937,0.631,0.259],
        "firelightambient": [0,0,0],
        # Class: CfgWeapons|Default|Eventhandlers [Indent level: 1],
        "eventhandlers": {
        },
        "backgroundreload": 0,
        "reloadaction": "",
        "muzzles": ["this"],
        "modes": ["this"],
        "useaction": 0,
        "useactiontitle": "",
        "candrop": 1,
        "weaponlockdelay": 0,
        "weaponlocksystem": 0,
        "cmimmunity": 1,
        "weight": 0,
        "handanim": [],
        "lockingtargetsound": ["",0.000316228,2],
        "lockedtargetsound": ["",0.000316228,6],
        "detectrange": 0,
        "artillerydispersion": 1,
        "artillerycharge": 1,
        "fireanims": [],
        # Class: CfgWeapons|Default|Library [Indent level: 1],
        "library": {
            "libtextdesc": ""
        },
        "descriptionshort": "",
        # Class: CfgWeapons|Default|GunFire [Indent level: 1],
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
            "cloudletdensitycoef": -1,
            "interval": -0.01,
            "size": 3,
            "sourcesize": 0.5,
            "timetolive": 0,
            "initt": 4500,
            "deltat": -3000,
            # Class: CfgWeapons|Default|GunFire|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunFire|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [0.82,0.95,0.93,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T1 [Indent level: 3],
                "t1": {
                    "maxt": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T2 [Indent level: 3],
                "t2": {
                    "maxt": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T3 [Indent level: 3],
                "t3": {
                    "maxt": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T4 [Indent level: 3],
                "t4": {
                    "maxt": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T5 [Indent level: 3],
                "t5": {
                    "maxt": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T6 [Indent level: 3],
                "t6": {
                    "maxt": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T7 [Indent level: 3],
                "t7": {
                    "maxt": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T8 [Indent level: 3],
                "t8": {
                    "maxt": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T9 [Indent level: 3],
                "t9": {
                    "maxt": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T10 [Indent level: 3],
                "t10": {
                    "maxt": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T11 [Indent level: 3],
                "t11": {
                    "maxt": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T12 [Indent level: 3],
                "t12": {
                    "maxt": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T13 [Indent level: 3],
                "t13": {
                    "maxt": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T14 [Indent level: 3],
                "t14": {
                    "maxt": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T15 [Indent level: 3],
                "t15": {
                    "maxt": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T16 [Indent level: 3],
                "t16": {
                    "maxt": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T17 [Indent level: 3],
                "t17": {
                    "maxt": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T18 [Indent level: 3],
                "t18": {
                    "maxt": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T19 [Indent level: 3],
                "t19": {
                    "maxt": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T20 [Indent level: 3],
                "t20": {
                    "maxt": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T21 [Indent level: 3],
                "t21": {
                    "maxt": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T22 [Indent level: 3],
                "t22": {
                    "maxt": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgWeapons|Default|GunClouds [Indent level: 1],
        "gunclouds": {
            "access": 0,
            "cloudletgrowup": 0.05,
            "cloudletfadein": 0,
            "cloudletfadeout": 0.1,
            "cloudletduration": 0.05,
            "cloudletalpha": 0.3,
            "cloudletaccy": 0,
            "cloudletminyspeed": -100,
            "cloudletmaxyspeed": 100,
            "interval": -0.02,
            "size": 0.3,
            "sourcesize": 0.02,
            "cloudletanimperiod": 1,
            "cloudletsize": 1,
            "cloudletshape": "cloudletClouds",
            "cloudletcolor": [1,1,1,0],
            "timetolive": 0,
            "initt": 0,
            "deltat": 0,
            # Class: CfgWeapons|Default|GunClouds|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunClouds|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        "texturetype": "default",
        "inertia": 0.5,
        "aimtransitionspeed": 1
    },
    # Class: CfgWeapons|Put|TrainingMineMuzzle [Indent level: 1],
    "trainingminemuzzle": {
        "displayname": "Training Mine",
        # Compatible Magazines: magazines parameter (+ inherited),
        "magazines": [
            "democharge_remote_mag","iedurbansmall_remote_mag","iedlandsmall_remote_mag","satchelcharge_remote_mag",
            "iedurbanbig_remote_mag","iedlandbig_remote_mag","atmine_range_mag","claymoredirectionalmine_remote_mag",
            "apersmine_range_mag","apersboundingmine_range_mag","slamdirectionalmine_wire_mag","aperstripmine_wire_mag",
            "apersminedispenser_mag","trainingmine_mag","rhs_mine_pmn2_mag","rhs_mine_tm62m_mag",
            "rhs_mine_msk40p_white_mag","rhs_mine_msk40p_red_mag","rhs_mine_msk40p_green_mag","rhs_mine_msk40p_blue_mag",
            "rhs_mine_sm320_white_mag","rhs_mine_sm320_red_mag","rhs_mine_sm320_green_mag","rhs_mine_ozm72_a_mag",
            "rhs_mine_ozm72_b_mag","rhs_mine_ozm72_c_mag","rhs_ec75_mag","rhs_ec200_mag",
            "rhs_ec400_mag","rhs_ec75_sand_mag","rhs_ec200_sand_mag","rhs_ec400_sand_mag",
            "rhs_mine_m19_mag","rhsusf_mine_m14_mag","rhsusf_mine_m49a1_3m_mag","rhsusf_mine_m49a1_6m_mag",
            "rhsusf_mine_m49a1_10m_mag","rhsusf_m112_mag","rhsusf_m112x4_mag","rhs_mag_mine_pfm1",
            "rhs_mag_mine_ptm1","rhs_mine_smine35_press_mag","rhs_mine_smine35_trip_mag","rhs_mine_smine44_press_mag",
            "rhs_mine_smine44_trip_mag","rhs_mine_glasmine43_hz_mag","rhs_mine_glasmine43_bz_mag","rhs_mine_stockmine43_2m_mag",
            "rhs_mine_stockmine43_4m_mag","rhs_mine_a200_bz_mag","rhs_mine_a200_dz35_mag","rhs_mine_tm43_mag",
            "rhs_mine_m2a3b_press_mag","rhs_mine_m2a3b_trip_mag","rhs_mine_m3_pressure_mag","rhs_mine_mk2_pressure_mag",
            "rhs_mine_m3_tripwire_mag","rhs_mine_mk2_tripwire_mag","rhs_mine_m7a2_mag","rhs_charge_m2tet_x2_mag",
            "rhssaf_mine_pma3_mag","rhssaf_mine_tma4_mag","rhssaf_mine_mrud_a_mag","rhssaf_mine_mrud_b_mag",
            "rhssaf_mine_mrud_c_mag","rhssaf_mine_mrud_d_mag","rhssaf_tm100_mag","rhssaf_tm200_mag",
            "rhssaf_tm500_mag",],
        "showtoplayer": 0,
        "enableattack": 1,
        "autoreload": 0,
        "sound": ["",0.000316228,1],
        "reloadsound": ["",0.000316228,1],
        "optics": 0,
        "showempty": 0,
        "canlock": 0,
        "primary": 10,
        "minrange": 0,
        "minrangeprobab": 0.1,
        "midrange": 3,
        "midrangeprobab": 0.9,
        "maxrange": 15,
        "maxrangeprobab": 0.04,
        "movetointernal": 0,
        "opticszoommin": 0.25,
        "opticszoommax": 1.25,
        "opticszoominit": 0.75,
        "access": 3,
        "scope": 0,
        "value": 2,
        "picture": "",
        "uipicture": "",
        "ammo": "",
        "cursor": "",
        "cursoraim": "",
        "cursorsize": 1,
        "showaimcursorinternal": 1,
        "cursoraimon": "",
        "laser": 0,
        "hiddenselections": [],
        "hiddenselectionstextures": [],
        "hiddenunderwaterselections": [],
        "shownunderwaterselections": [],
        "hiddenunderwaterselectionstextures": [],
        "simulation": "Weapon",
        "type": 65536,
        "namesound": "",
        "count": 0,
        "multiplier": 1,
        "burst": 1,
        "magazinereloadtime": 0,
        "reloadtime": 1,
        "magazinereloadswitchphase": 1,
        "soundbegin": ["sound",1],
        "soundbeginwater": ["sound",1],
        "soundclosure": ["sound",1],
        "soundend": ["sound",1],
        "soundloop": ["sound",1],
        "soundcontinuous": 0,
        "weaponsoundeffect": "",
        "soundburst": 1,
        "drysound": ["",1,1],
        "zeroingsound": ["",1,1],
        "changefiremodesound": ["",1,1],
        "reloadmagazinesound": ["",1,1],
        "emptysound": ["",1,1],
        "soundbullet": ["emptySound",1],
        "initspeed": 0,
        "ballisticscomputer": 0,
        "irdistance": 0,
        "irdotintensity": 0.001,
        "dispersion": 0.002,
        "aidispersioncoefx": 1,
        "aidispersioncoefy": 1,
        "lockacquire": 1,
        "ffmagnitude": 0,
        "fffrequency": 1,
        "ffcount": 1,
        # Recoil Array: recoil,
        "recoil": [],
        "recoil": "empty",
        "recoilprone": "",
        "maxrecoilsway": 0.008,
        "swaydecayspeed": 2,
        "model": "",
        "modelspecial": "",
        "modelmagazine": "",
        "muzzlepos": "usti hlavne",
        "muzzleend": "konec hlavne",
        "irlaserpos": "laser pos",
        "irlaserend": "laser dir",
        "cartridgepos": "nabojnicestart",
        "cartridgevel": "nabojniceend",
        "selectionfireanim": "zasleh",
        "memorypointcamera": "eye",
        "firespreadangle": 3,
        "usemodeloptics": 1,
        "opticsid": 0,
        "modeloptics": "",
        "opticsppeffects": [],
        "opticsflare": 1,
        "forceoptics": 0,
        "useasbinocular": 0,
        "opticsdisableperipherialvision": 0.67,
        "distancezoommin": 400,
        "distancezoommax": 400,
        "showswitchaction": 0,
        "autofire": 0,
        "canshootinwater": 0,
        "airateoffire": 5,
        "airateoffiredistance": 500,
        "airateoffiredispersion": 0,
        "firelightduration": 0.05,
        "firelightintensity": 0.2,
        "firelightdiffuse": [0.937,0.631,0.259],
        "firelightambient": [0,0,0],
        # Class: CfgWeapons|Default|Eventhandlers [Indent level: 1],
        "eventhandlers": {
        },
        "backgroundreload": 0,
        "reloadaction": "",
        "muzzles": ["this"],
        "modes": ["this"],
        "useaction": 0,
        "useactiontitle": "",
        "candrop": 1,
        "weaponlockdelay": 0,
        "weaponlocksystem": 0,
        "cmimmunity": 1,
        "weight": 0,
        "handanim": [],
        "lockingtargetsound": ["",0.000316228,2],
        "lockedtargetsound": ["",0.000316228,6],
        "detectrange": 0,
        "artillerydispersion": 1,
        "artillerycharge": 1,
        "fireanims": [],
        # Class: CfgWeapons|Default|Library [Indent level: 1],
        "library": {
            "libtextdesc": ""
        },
        "descriptionshort": "",
        # Class: CfgWeapons|Default|GunFire [Indent level: 1],
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
            "cloudletdensitycoef": -1,
            "interval": -0.01,
            "size": 3,
            "sourcesize": 0.5,
            "timetolive": 0,
            "initt": 4500,
            "deltat": -3000,
            # Class: CfgWeapons|Default|GunFire|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunFire|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [0.82,0.95,0.93,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T1 [Indent level: 3],
                "t1": {
                    "maxt": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T2 [Indent level: 3],
                "t2": {
                    "maxt": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T3 [Indent level: 3],
                "t3": {
                    "maxt": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T4 [Indent level: 3],
                "t4": {
                    "maxt": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T5 [Indent level: 3],
                "t5": {
                    "maxt": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T6 [Indent level: 3],
                "t6": {
                    "maxt": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T7 [Indent level: 3],
                "t7": {
                    "maxt": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T8 [Indent level: 3],
                "t8": {
                    "maxt": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T9 [Indent level: 3],
                "t9": {
                    "maxt": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T10 [Indent level: 3],
                "t10": {
                    "maxt": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T11 [Indent level: 3],
                "t11": {
                    "maxt": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T12 [Indent level: 3],
                "t12": {
                    "maxt": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T13 [Indent level: 3],
                "t13": {
                    "maxt": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T14 [Indent level: 3],
                "t14": {
                    "maxt": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T15 [Indent level: 3],
                "t15": {
                    "maxt": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T16 [Indent level: 3],
                "t16": {
                    "maxt": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T17 [Indent level: 3],
                "t17": {
                    "maxt": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T18 [Indent level: 3],
                "t18": {
                    "maxt": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T19 [Indent level: 3],
                "t19": {
                    "maxt": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T20 [Indent level: 3],
                "t20": {
                    "maxt": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T21 [Indent level: 3],
                "t21": {
                    "maxt": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T22 [Indent level: 3],
                "t22": {
                    "maxt": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgWeapons|Default|GunClouds [Indent level: 1],
        "gunclouds": {
            "access": 0,
            "cloudletgrowup": 0.05,
            "cloudletfadein": 0,
            "cloudletfadeout": 0.1,
            "cloudletduration": 0.05,
            "cloudletalpha": 0.3,
            "cloudletaccy": 0,
            "cloudletminyspeed": -100,
            "cloudletmaxyspeed": 100,
            "interval": -0.02,
            "size": 0.3,
            "sourcesize": 0.02,
            "cloudletanimperiod": 1,
            "cloudletsize": 1,
            "cloudletshape": "cloudletClouds",
            "cloudletcolor": [1,1,1,0],
            "timetolive": 0,
            "initt": 0,
            "deltat": 0,
            # Class: CfgWeapons|Default|GunClouds|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunClouds|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        "texturetype": "default",
        "inertia": 0.5,
        "aimtransitionspeed": 1
    },
    "displayname": "Put",
    # Class: CfgWeapons|Put|Drone_explosive_muzzle [Indent level: 1],
    "drone_explosive_muzzle": {
        "autoreload": 0,
        "enableattack": 1,
        # Compatible Magazines: magazines parameter (+ inherited),
        "magazines": [
            "democharge_remote_mag","iedurbansmall_remote_mag","iedlandsmall_remote_mag","satchelcharge_remote_mag",
            "iedurbanbig_remote_mag","iedlandbig_remote_mag","atmine_range_mag","claymoredirectionalmine_remote_mag",
            "apersmine_range_mag","apersboundingmine_range_mag","slamdirectionalmine_wire_mag","aperstripmine_wire_mag",
            "apersminedispenser_mag","trainingmine_mag","rhs_mine_pmn2_mag","rhs_mine_tm62m_mag",
            "rhs_mine_msk40p_white_mag","rhs_mine_msk40p_red_mag","rhs_mine_msk40p_green_mag","rhs_mine_msk40p_blue_mag",
            "rhs_mine_sm320_white_mag","rhs_mine_sm320_red_mag","rhs_mine_sm320_green_mag","rhs_mine_ozm72_a_mag",
            "rhs_mine_ozm72_b_mag","rhs_mine_ozm72_c_mag","rhs_ec75_mag","rhs_ec200_mag",
            "rhs_ec400_mag","rhs_ec75_sand_mag","rhs_ec200_sand_mag","rhs_ec400_sand_mag",
            "rhs_mine_m19_mag","rhsusf_mine_m14_mag","rhsusf_mine_m49a1_3m_mag","rhsusf_mine_m49a1_6m_mag",
            "rhsusf_mine_m49a1_10m_mag","rhsusf_m112_mag","rhsusf_m112x4_mag","rhs_mag_mine_pfm1",
            "rhs_mag_mine_ptm1","rhs_mine_smine35_press_mag","rhs_mine_smine35_trip_mag","rhs_mine_smine44_press_mag",
            "rhs_mine_smine44_trip_mag","rhs_mine_glasmine43_hz_mag","rhs_mine_glasmine43_bz_mag","rhs_mine_stockmine43_2m_mag",
            "rhs_mine_stockmine43_4m_mag","rhs_mine_a200_bz_mag","rhs_mine_a200_dz35_mag","rhs_mine_tm43_mag",
            "rhs_mine_m2a3b_press_mag","rhs_mine_m2a3b_trip_mag","rhs_mine_m3_pressure_mag","rhs_mine_mk2_pressure_mag",
            "rhs_mine_m3_tripwire_mag","rhs_mine_mk2_tripwire_mag","rhs_mine_m7a2_mag","rhs_charge_m2tet_x2_mag",
            "rhssaf_mine_pma3_mag","rhssaf_mine_tma4_mag","rhssaf_mine_mrud_a_mag","rhssaf_mine_mrud_b_mag",
            "rhssaf_mine_mrud_c_mag","rhssaf_mine_mrud_d_mag","rhssaf_tm100_mag","rhssaf_tm200_mag",
            "rhssaf_tm500_mag",],
        "displayname": "Drone Mine Muzzle",
        "picture": "A3|Weapons_F|Data|clear_empty.paa",
        "showtoplayer": 0,
        "sound": ["",0.000316228,1],
        "reloadsound": ["",0.000316228,1],
        "optics": 0,
        "showempty": 0,
        "canlock": 0,
        "primary": 10,
        "minrange": 0,
        "minrangeprobab": 0.1,
        "midrange": 3,
        "midrangeprobab": 0.9,
        "maxrange": 15,
        "maxrangeprobab": 0.04,
        "movetointernal": 0,
        "opticszoommin": 0.25,
        "opticszoommax": 1.25,
        "opticszoominit": 0.75,
        "access": 3,
        "scope": 0,
        "value": 2,
        "uipicture": "",
        "ammo": "",
        "cursor": "",
        "cursoraim": "",
        "cursorsize": 1,
        "showaimcursorinternal": 1,
        "cursoraimon": "",
        "laser": 0,
        "hiddenselections": [],
        "hiddenselectionstextures": [],
        "hiddenunderwaterselections": [],
        "shownunderwaterselections": [],
        "hiddenunderwaterselectionstextures": [],
        "simulation": "Weapon",
        "type": 65536,
        "namesound": "",
        "count": 0,
        "multiplier": 1,
        "burst": 1,
        "magazinereloadtime": 0,
        "reloadtime": 1,
        "magazinereloadswitchphase": 1,
        "soundbegin": ["sound",1],
        "soundbeginwater": ["sound",1],
        "soundclosure": ["sound",1],
        "soundend": ["sound",1],
        "soundloop": ["sound",1],
        "soundcontinuous": 0,
        "weaponsoundeffect": "",
        "soundburst": 1,
        "drysound": ["",1,1],
        "zeroingsound": ["",1,1],
        "changefiremodesound": ["",1,1],
        "reloadmagazinesound": ["",1,1],
        "emptysound": ["",1,1],
        "soundbullet": ["emptySound",1],
        "initspeed": 0,
        "ballisticscomputer": 0,
        "irdistance": 0,
        "irdotintensity": 0.001,
        "dispersion": 0.002,
        "aidispersioncoefx": 1,
        "aidispersioncoefy": 1,
        "lockacquire": 1,
        "ffmagnitude": 0,
        "fffrequency": 1,
        "ffcount": 1,
        # Recoil Array: recoil,
        "recoil": [],
        "recoil": "empty",
        "recoilprone": "",
        "maxrecoilsway": 0.008,
        "swaydecayspeed": 2,
        "model": "",
        "modelspecial": "",
        "modelmagazine": "",
        "muzzlepos": "usti hlavne",
        "muzzleend": "konec hlavne",
        "irlaserpos": "laser pos",
        "irlaserend": "laser dir",
        "cartridgepos": "nabojnicestart",
        "cartridgevel": "nabojniceend",
        "selectionfireanim": "zasleh",
        "memorypointcamera": "eye",
        "firespreadangle": 3,
        "usemodeloptics": 1,
        "opticsid": 0,
        "modeloptics": "",
        "opticsppeffects": [],
        "opticsflare": 1,
        "forceoptics": 0,
        "useasbinocular": 0,
        "opticsdisableperipherialvision": 0.67,
        "distancezoommin": 400,
        "distancezoommax": 400,
        "showswitchaction": 0,
        "autofire": 0,
        "canshootinwater": 0,
        "airateoffire": 5,
        "airateoffiredistance": 500,
        "airateoffiredispersion": 0,
        "firelightduration": 0.05,
        "firelightintensity": 0.2,
        "firelightdiffuse": [0.937,0.631,0.259],
        "firelightambient": [0,0,0],
        # Class: CfgWeapons|Default|Eventhandlers [Indent level: 1],
        "eventhandlers": {
        },
        "backgroundreload": 0,
        "reloadaction": "",
        "muzzles": ["this"],
        "modes": ["this"],
        "useaction": 0,
        "useactiontitle": "",
        "candrop": 1,
        "weaponlockdelay": 0,
        "weaponlocksystem": 0,
        "cmimmunity": 1,
        "weight": 0,
        "handanim": [],
        "lockingtargetsound": ["",0.000316228,2],
        "lockedtargetsound": ["",0.000316228,6],
        "detectrange": 0,
        "artillerydispersion": 1,
        "artillerycharge": 1,
        "fireanims": [],
        # Class: CfgWeapons|Default|Library [Indent level: 1],
        "library": {
            "libtextdesc": ""
        },
        "descriptionshort": "",
        # Class: CfgWeapons|Default|GunFire [Indent level: 1],
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
            "cloudletdensitycoef": -1,
            "interval": -0.01,
            "size": 3,
            "sourcesize": 0.5,
            "timetolive": 0,
            "initt": 4500,
            "deltat": -3000,
            # Class: CfgWeapons|Default|GunFire|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunFire|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [0.82,0.95,0.93,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T1 [Indent level: 3],
                "t1": {
                    "maxt": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T2 [Indent level: 3],
                "t2": {
                    "maxt": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T3 [Indent level: 3],
                "t3": {
                    "maxt": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T4 [Indent level: 3],
                "t4": {
                    "maxt": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T5 [Indent level: 3],
                "t5": {
                    "maxt": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T6 [Indent level: 3],
                "t6": {
                    "maxt": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T7 [Indent level: 3],
                "t7": {
                    "maxt": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T8 [Indent level: 3],
                "t8": {
                    "maxt": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T9 [Indent level: 3],
                "t9": {
                    "maxt": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T10 [Indent level: 3],
                "t10": {
                    "maxt": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T11 [Indent level: 3],
                "t11": {
                    "maxt": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T12 [Indent level: 3],
                "t12": {
                    "maxt": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T13 [Indent level: 3],
                "t13": {
                    "maxt": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T14 [Indent level: 3],
                "t14": {
                    "maxt": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T15 [Indent level: 3],
                "t15": {
                    "maxt": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T16 [Indent level: 3],
                "t16": {
                    "maxt": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T17 [Indent level: 3],
                "t17": {
                    "maxt": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T18 [Indent level: 3],
                "t18": {
                    "maxt": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T19 [Indent level: 3],
                "t19": {
                    "maxt": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T20 [Indent level: 3],
                "t20": {
                    "maxt": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T21 [Indent level: 3],
                "t21": {
                    "maxt": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T22 [Indent level: 3],
                "t22": {
                    "maxt": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgWeapons|Default|GunClouds [Indent level: 1],
        "gunclouds": {
            "access": 0,
            "cloudletgrowup": 0.05,
            "cloudletfadein": 0,
            "cloudletfadeout": 0.1,
            "cloudletduration": 0.05,
            "cloudletalpha": 0.3,
            "cloudletaccy": 0,
            "cloudletminyspeed": -100,
            "cloudletmaxyspeed": 100,
            "interval": -0.02,
            "size": 0.3,
            "sourcesize": 0.02,
            "cloudletanimperiod": 1,
            "cloudletsize": 1,
            "cloudletshape": "cloudletClouds",
            "cloudletcolor": [1,1,1,0],
            "timetolive": 0,
            "initt": 0,
            "deltat": 0,
            # Class: CfgWeapons|Default|GunClouds|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunClouds|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        "texturetype": "default",
        "inertia": 0.5,
        "aimtransitionspeed": 1
    },
    # Class: CfgWeapons|Put|Drone_explosive_muzzle_dummy [Indent level: 1],
    "drone_explosive_muzzle_dummy": {
        # Compatible Magazines: magazines parameter (+ inherited)
        "magazines": [
            "democharge_remote_mag","iedurbansmall_remote_mag","iedlandsmall_remote_mag","satchelcharge_remote_mag"
            "iedurbanbig_remote_mag","iedlandbig_remote_mag","atmine_range_mag","claymoredirectionalmine_remote_mag"
            "apersmine_range_mag","apersboundingmine_range_mag","slamdirectionalmine_wire_mag","aperstripmine_wire_mag"
            "apersminedispenser_mag","trainingmine_mag","rhs_mine_pmn2_mag","rhs_mine_tm62m_mag"
            "rhs_mine_msk40p_white_mag","rhs_mine_msk40p_red_mag","rhs_mine_msk40p_green_mag","rhs_mine_msk40p_blue_mag"
            "rhs_mine_sm320_white_mag","rhs_mine_sm320_red_mag","rhs_mine_sm320_green_mag","rhs_mine_ozm72_a_mag"
            "rhs_mine_ozm72_b_mag","rhs_mine_ozm72_c_mag","rhs_ec75_mag","rhs_ec200_mag"
            "rhs_ec400_mag","rhs_ec75_sand_mag","rhs_ec200_sand_mag","rhs_ec400_sand_mag"
            "rhs_mine_m19_mag","rhsusf_mine_m14_mag","rhsusf_mine_m49a1_3m_mag","rhsusf_mine_m49a1_6m_mag"
            "rhsusf_mine_m49a1_10m_mag","rhsusf_m112_mag","rhsusf_m112x4_mag","rhs_mag_mine_pfm1"
            "rhs_mag_mine_ptm1","rhs_mine_smine35_press_mag","rhs_mine_smine35_trip_mag","rhs_mine_smine44_press_mag"
            "rhs_mine_smine44_trip_mag","rhs_mine_glasmine43_hz_mag","rhs_mine_glasmine43_bz_mag","rhs_mine_stockmine43_2m_mag"
            "rhs_mine_stockmine43_4m_mag","rhs_mine_a200_bz_mag","rhs_mine_a200_dz35_mag","rhs_mine_tm43_mag"
            "rhs_mine_m2a3b_press_mag","rhs_mine_m2a3b_trip_mag","rhs_mine_m3_pressure_mag","rhs_mine_mk2_pressure_mag"
            "rhs_mine_m3_tripwire_mag","rhs_mine_mk2_tripwire_mag","rhs_mine_m7a2_mag","rhs_charge_m2tet_x2_mag"
            "rhssaf_mine_pma3_mag","rhssaf_mine_tma4_mag","rhssaf_mine_mrud_a_mag","rhssaf_mine_mrud_b_mag"
            "rhssaf_mine_mrud_c_mag","rhssaf_mine_mrud_d_mag","rhssaf_tm100_mag","rhssaf_tm200_mag"
            "rhssaf_tm500_mag",],
        "displayname": "Drone Mine Muzzle Dummy",
        "autoreload": 0,
        "enableattack": 1,
        "picture": "A3|Weapons_F|Data|clear_empty.paa",
        "showtoplayer": 0,
        "sound": ["",0.000316228,1],
        "reloadsound": ["",0.000316228,1],
        "optics": 0,
        "showempty": 0,
        "canlock": 0,
        "primary": 10,
        "minrange": 0,
        "minrangeprobab": 0.1,
        "midrange": 3,
        "midrangeprobab": 0.9,
        "maxrange": 15,
        "maxrangeprobab": 0.04,
        "movetointernal": 0,
        "opticszoommin": 0.25,
        "opticszoommax": 1.25,
        "opticszoominit": 0.75,
        "access": 3,
        "scope": 0,
        "value": 2,
        "uipicture": "",
        "ammo": "",
        "cursor": "",
        "cursoraim": "",
        "cursorsize": 1,
        "showaimcursorinternal": 1,
        "cursoraimon": "",
        "laser": 0,
        "hiddenselections": [],
        "hiddenselectionstextures": [],
        "hiddenunderwaterselections": [],
        "shownunderwaterselections": [],
        "hiddenunderwaterselectionstextures": [],
        "simulation": "Weapon",
        "type": 65536,
        "namesound": "",
        "count": 0,
        "multiplier": 1,
        "burst": 1,
        "magazinereloadtime": 0,
        "reloadtime": 1,
        "magazinereloadswitchphase": 1,
        "soundbegin": ["sound",1],
        "soundbeginwater": ["sound",1],
        "soundclosure": ["sound",1],
        "soundend": ["sound",1],
        "soundloop": ["sound",1],
        "soundcontinuous": 0,
        "weaponsoundeffect": "",
        "soundburst": 1,
        "drysound": ["",1,1],
        "zeroingsound": ["",1,1],
        "changefiremodesound": ["",1,1],
        "reloadmagazinesound": ["",1,1],
        "emptysound": ["",1,1],
        "soundbullet": ["emptySound",1],
        "initspeed": 0,
        "ballisticscomputer": 0,
        "irdistance": 0,
        "irdotintensity": 0.001,
        "dispersion": 0.002,
        "aidispersioncoefx": 1,
        "aidispersioncoefy": 1,
        "lockacquire": 1,
        "ffmagnitude": 0,
        "fffrequency": 1,
        "ffcount": 1,
        # Recoil Array: recoil,
        "recoil": [],
        "recoil": "empty",
        "recoilprone": "",
        "maxrecoilsway": 0.008,
        "swaydecayspeed": 2,
        "model": "",
        "modelspecial": "",
        "modelmagazine": "",
        "muzzlepos": "usti hlavne",
        "muzzleend": "konec hlavne",
        "irlaserpos": "laser pos",
        "irlaserend": "laser dir",
        "cartridgepos": "nabojnicestart",
        "cartridgevel": "nabojniceend",
        "selectionfireanim": "zasleh",
        "memorypointcamera": "eye",
        "firespreadangle": 3,
        "usemodeloptics": 1,
        "opticsid": 0,
        "modeloptics": "",
        "opticsppeffects": [],
        "opticsflare": 1,
        "forceoptics": 0,
        "useasbinocular": 0,
        "opticsdisableperipherialvision": 0.67,
        "distancezoommin": 400,
        "distancezoommax": 400,
        "showswitchaction": 0,
        "autofire": 0,
        "canshootinwater": 0,
        "airateoffire": 5,
        "airateoffiredistance": 500,
        "airateoffiredispersion": 0,
        "firelightduration": 0.05,
        "firelightintensity": 0.2,
        "firelightdiffuse": [0.937,0.631,0.259],
        "firelightambient": [0,0,0],
        # Class: CfgWeapons|Default|Eventhandlers [Indent level: 1],
        "eventhandlers": {
        },
        "backgroundreload": 0,
        "reloadaction": "",
        "muzzles": ["this"],
        "modes": ["this"],
        "useaction": 0,
        "useactiontitle": "",
        "candrop": 1,
        "weaponlockdelay": 0,
        "weaponlocksystem": 0,
        "cmimmunity": 1,
        "weight": 0,
        "handanim": [],
        "lockingtargetsound": ["",0.000316228,2],
        "lockedtargetsound": ["",0.000316228,6],
        "detectrange": 0,
        "artillerydispersion": 1,
        "artillerycharge": 1,
        "fireanims": [],
        # Class: CfgWeapons|Default|Library [Indent level: 1],
        "library": {
            "libtextdesc": ""
        },
        "descriptionshort": "",
        # Class: CfgWeapons|Default|GunFire [Indent level: 1],
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
            "cloudletdensitycoef": -1,
            "interval": -0.01,
            "size": 3,
            "sourcesize": 0.5,
            "timetolive": 0,
            "initt": 4500,
            "deltat": -3000,
            # Class: CfgWeapons|Default|GunFire|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunFire|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [0.82,0.95,0.93,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T1 [Indent level: 3],
                "t1": {
                    "maxt": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T2 [Indent level: 3],
                "t2": {
                    "maxt": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T3 [Indent level: 3],
                "t3": {
                    "maxt": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T4 [Indent level: 3],
                "t4": {
                    "maxt": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T5 [Indent level: 3],
                "t5": {
                    "maxt": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T6 [Indent level: 3],
                "t6": {
                    "maxt": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T7 [Indent level: 3],
                "t7": {
                    "maxt": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T8 [Indent level: 3],
                "t8": {
                    "maxt": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T9 [Indent level: 3],
                "t9": {
                    "maxt": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T10 [Indent level: 3],
                "t10": {
                    "maxt": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T11 [Indent level: 3],
                "t11": {
                    "maxt": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T12 [Indent level: 3],
                "t12": {
                    "maxt": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T13 [Indent level: 3],
                "t13": {
                    "maxt": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T14 [Indent level: 3],
                "t14": {
                    "maxt": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T15 [Indent level: 3],
                "t15": {
                    "maxt": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T16 [Indent level: 3],
                "t16": {
                    "maxt": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T17 [Indent level: 3],
                "t17": {
                    "maxt": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T18 [Indent level: 3],
                "t18": {
                    "maxt": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T19 [Indent level: 3],
                "t19": {
                    "maxt": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T20 [Indent level: 3],
                "t20": {
                    "maxt": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T21 [Indent level: 3],
                "t21": {
                    "maxt": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T22 [Indent level: 3],
                "t22": {
                    "maxt": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgWeapons|Default|GunClouds [Indent level: 1],
        "gunclouds": {
            "access": 0,
            "cloudletgrowup": 0.05,
            "cloudletfadein": 0,
            "cloudletfadeout": 0.1,
            "cloudletduration": 0.05,
            "cloudletalpha": 0.3,
            "cloudletaccy": 0,
            "cloudletminyspeed": -100,
            "cloudletmaxyspeed": 100,
            "interval": -0.02,
            "size": 0.3,
            "sourcesize": 0.02,
            "cloudletanimperiod": 1,
            "cloudletsize": 1,
            "cloudletshape": "cloudletClouds",
            "cloudletcolor": [1,1,1,0],
            "timetolive": 0,
            "initt": 0,
            "deltat": 0,
            # Class: CfgWeapons|Default|GunClouds|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunClouds|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        "texturetype": "default",
        "inertia": 0.5,
        "aimtransitionspeed": 1
    },
    # Class: CfgWeapons|Put|Rhs_Mine_Muzzle [Indent level: 1],
    "rhs_mine_muzzle": {
        # Compatible Magazines: magazines parameter (+ inherited)
        "magazines": [
            "democharge_remote_mag","iedurbansmall_remote_mag","iedlandsmall_remote_mag","satchelcharge_remote_mag"
            "iedurbanbig_remote_mag","iedlandbig_remote_mag","atmine_range_mag","claymoredirectionalmine_remote_mag"
            "apersmine_range_mag","apersboundingmine_range_mag","slamdirectionalmine_wire_mag","aperstripmine_wire_mag"
            "apersminedispenser_mag","trainingmine_mag","rhs_mine_pmn2_mag","rhs_mine_tm62m_mag"
            "rhs_mine_msk40p_white_mag","rhs_mine_msk40p_red_mag","rhs_mine_msk40p_green_mag","rhs_mine_msk40p_blue_mag"
            "rhs_mine_sm320_white_mag","rhs_mine_sm320_red_mag","rhs_mine_sm320_green_mag","rhs_mine_ozm72_a_mag"
            "rhs_mine_ozm72_b_mag","rhs_mine_ozm72_c_mag","rhs_ec75_mag","rhs_ec200_mag"
            "rhs_ec400_mag","rhs_ec75_sand_mag","rhs_ec200_sand_mag","rhs_ec400_sand_mag"
            "rhs_mine_m19_mag","rhsusf_mine_m14_mag","rhsusf_mine_m49a1_3m_mag","rhsusf_mine_m49a1_6m_mag"
            "rhsusf_mine_m49a1_10m_mag","rhsusf_m112_mag","rhsusf_m112x4_mag","rhs_mag_mine_pfm1"
            "rhs_mag_mine_ptm1","rhs_mine_smine35_press_mag","rhs_mine_smine35_trip_mag","rhs_mine_smine44_press_mag"
            "rhs_mine_smine44_trip_mag","rhs_mine_glasmine43_hz_mag","rhs_mine_glasmine43_bz_mag","rhs_mine_stockmine43_2m_mag"
            "rhs_mine_stockmine43_4m_mag","rhs_mine_a200_bz_mag","rhs_mine_a200_dz35_mag","rhs_mine_tm43_mag"
            "rhs_mine_m2a3b_press_mag","rhs_mine_m2a3b_trip_mag","rhs_mine_m3_pressure_mag","rhs_mine_mk2_pressure_mag"
            "rhs_mine_m3_tripwire_mag","rhs_mine_mk2_tripwire_mag","rhs_mine_m7a2_mag","rhs_charge_m2tet_x2_mag"
            "rhssaf_mine_pma3_mag","rhssaf_mine_tma4_mag","rhssaf_mine_mrud_a_mag","rhssaf_mine_mrud_b_mag"
            "rhssaf_mine_mrud_c_mag","rhssaf_mine_mrud_d_mag","rhssaf_tm100_mag","rhssaf_tm200_mag"
            "rhssaf_tm500_mag",],
        "sound": ["",0.000316228,1],
        "reloadsound": ["",0.000316228,1],
        "enableattack": 0,
        "optics": 0,
        "showempty": 0,
        "canlock": 0,
        "primary": 10,
        "minrange": 0,
        "minrangeprobab": 0.1,
        "midrange": 3,
        "midrangeprobab": 0.9,
        "maxrange": 15,
        "maxrangeprobab": 0.04,
        "movetointernal": 0,
        "opticszoommin": 0.25,
        "opticszoommax": 1.25,
        "opticszoominit": 0.75,
        "access": 3,
        "scope": 0,
        "value": 2,
        "picture": "",
        "uipicture": "",
        "ammo": "",
        "cursor": "",
        "cursoraim": "",
        "cursorsize": 1,
        "showaimcursorinternal": 1,
        "cursoraimon": "",
        "laser": 0,
        "hiddenselections": [],
        "hiddenselectionstextures": [],
        "hiddenunderwaterselections": [],
        "shownunderwaterselections": [],
        "hiddenunderwaterselectionstextures": [],
        "simulation": "Weapon",
        "type": 65536,
        "displayname": "",
        "namesound": "",
        "count": 0,
        "multiplier": 1,
        "burst": 1,
        "magazinereloadtime": 0,
        "reloadtime": 1,
        "magazinereloadswitchphase": 1,
        "soundbegin": ["sound",1],
        "soundbeginwater": ["sound",1],
        "soundclosure": ["sound",1],
        "soundend": ["sound",1],
        "soundloop": ["sound",1],
        "soundcontinuous": 0,
        "weaponsoundeffect": "",
        "soundburst": 1,
        "drysound": ["",1,1],
        "zeroingsound": ["",1,1],
        "changefiremodesound": ["",1,1],
        "reloadmagazinesound": ["",1,1],
        "emptysound": ["",1,1],
        "soundbullet": ["emptySound",1],
        "initspeed": 0,
        "ballisticscomputer": 0,
        "irdistance": 0,
        "irdotintensity": 0.001,
        "dispersion": 0.002,
        "aidispersioncoefx": 1,
        "aidispersioncoefy": 1,
        "lockacquire": 1,
        "ffmagnitude": 0,
        "fffrequency": 1,
        "ffcount": 1,
        # Recoil Array: recoil,
        "recoil": [],
        "recoil": "empty",
        "recoilprone": "",
        "maxrecoilsway": 0.008,
        "swaydecayspeed": 2,
        "model": "",
        "modelspecial": "",
        "modelmagazine": "",
        "muzzlepos": "usti hlavne",
        "muzzleend": "konec hlavne",
        "irlaserpos": "laser pos",
        "irlaserend": "laser dir",
        "cartridgepos": "nabojnicestart",
        "cartridgevel": "nabojniceend",
        "selectionfireanim": "zasleh",
        "memorypointcamera": "eye",
        "firespreadangle": 3,
        "usemodeloptics": 1,
        "opticsid": 0,
        "modeloptics": "",
        "opticsppeffects": [],
        "opticsflare": 1,
        "forceoptics": 0,
        "useasbinocular": 0,
        "opticsdisableperipherialvision": 0.67,
        "distancezoommin": 400,
        "distancezoommax": 400,
        "showswitchaction": 0,
        "autofire": 0,
        "autoreload": 1,
        "showtoplayer": 1,
        "canshootinwater": 0,
        "airateoffire": 5,
        "airateoffiredistance": 500,
        "airateoffiredispersion": 0,
        "firelightduration": 0.05,
        "firelightintensity": 0.2,
        "firelightdiffuse": [0.937,0.631,0.259],
        "firelightambient": [0,0,0],
        # Class: CfgWeapons|Default|Eventhandlers [Indent level: 1],
        "eventhandlers": {
        },
        "backgroundreload": 0,
        "reloadaction": "",
        "muzzles": ["this"],
        "modes": ["this"],
        "useaction": 0,
        "useactiontitle": "",
        "candrop": 1,
        "weaponlockdelay": 0,
        "weaponlocksystem": 0,
        "cmimmunity": 1,
        "weight": 0,
        "handanim": [],
        "lockingtargetsound": ["",0.000316228,2],
        "lockedtargetsound": ["",0.000316228,6],
        "detectrange": 0,
        "artillerydispersion": 1,
        "artillerycharge": 1,
        "fireanims": [],
        # Class: CfgWeapons|Default|Library [Indent level: 1],
        "library": {
            "libtextdesc": ""
        },
        "descriptionshort": "",
        # Class: CfgWeapons|Default|GunFire [Indent level: 1],
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
            "cloudletdensitycoef": -1,
            "interval": -0.01,
            "size": 3,
            "sourcesize": 0.5,
            "timetolive": 0,
            "initt": 4500,
            "deltat": -3000,
            # Class: CfgWeapons|Default|GunFire|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunFire|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [0.82,0.95,0.93,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T1 [Indent level: 3],
                "t1": {
                    "maxt": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T2 [Indent level: 3],
                "t2": {
                    "maxt": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T3 [Indent level: 3],
                "t3": {
                    "maxt": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T4 [Indent level: 3],
                "t4": {
                    "maxt": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T5 [Indent level: 3],
                "t5": {
                    "maxt": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T6 [Indent level: 3],
                "t6": {
                    "maxt": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T7 [Indent level: 3],
                "t7": {
                    "maxt": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T8 [Indent level: 3],
                "t8": {
                    "maxt": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T9 [Indent level: 3],
                "t9": {
                    "maxt": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T10 [Indent level: 3],
                "t10": {
                    "maxt": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T11 [Indent level: 3],
                "t11": {
                    "maxt": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T12 [Indent level: 3],
                "t12": {
                    "maxt": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T13 [Indent level: 3],
                "t13": {
                    "maxt": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T14 [Indent level: 3],
                "t14": {
                    "maxt": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T15 [Indent level: 3],
                "t15": {
                    "maxt": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T16 [Indent level: 3],
                "t16": {
                    "maxt": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T17 [Indent level: 3],
                "t17": {
                    "maxt": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T18 [Indent level: 3],
                "t18": {
                    "maxt": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T19 [Indent level: 3],
                "t19": {
                    "maxt": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T20 [Indent level: 3],
                "t20": {
                    "maxt": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T21 [Indent level: 3],
                "t21": {
                    "maxt": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T22 [Indent level: 3],
                "t22": {
                    "maxt": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgWeapons|Default|GunClouds [Indent level: 1],
        "gunclouds": {
            "access": 0,
            "cloudletgrowup": 0.05,
            "cloudletfadein": 0,
            "cloudletfadeout": 0.1,
            "cloudletduration": 0.05,
            "cloudletalpha": 0.3,
            "cloudletaccy": 0,
            "cloudletminyspeed": -100,
            "cloudletmaxyspeed": 100,
            "interval": -0.02,
            "size": 0.3,
            "sourcesize": 0.02,
            "cloudletanimperiod": 1,
            "cloudletsize": 1,
            "cloudletshape": "cloudletClouds",
            "cloudletcolor": [1,1,1,0],
            "timetolive": 0,
            "initt": 0,
            "deltat": 0,
            # Class: CfgWeapons|Default|GunClouds|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunClouds|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        "texturetype": "default",
        "inertia": 0.5,
        "aimtransitionspeed": 1
    },
    # Class: CfgWeapons|Put|Rhsusf_MineMuzzle [Indent level: 1],
    "rhsusf_minemuzzle": {
        # Compatible Magazines: magazines parameter (+ inherited)
        "magazines": [
            "democharge_remote_mag","iedurbansmall_remote_mag","iedlandsmall_remote_mag","satchelcharge_remote_mag"
            "iedurbanbig_remote_mag","iedlandbig_remote_mag","atmine_range_mag","claymoredirectionalmine_remote_mag"
            "apersmine_range_mag","apersboundingmine_range_mag","slamdirectionalmine_wire_mag","aperstripmine_wire_mag"
            "apersminedispenser_mag","trainingmine_mag","rhs_mine_pmn2_mag","rhs_mine_tm62m_mag"
            "rhs_mine_msk40p_white_mag","rhs_mine_msk40p_red_mag","rhs_mine_msk40p_green_mag","rhs_mine_msk40p_blue_mag"
            "rhs_mine_sm320_white_mag","rhs_mine_sm320_red_mag","rhs_mine_sm320_green_mag","rhs_mine_ozm72_a_mag"
            "rhs_mine_ozm72_b_mag","rhs_mine_ozm72_c_mag","rhs_ec75_mag","rhs_ec200_mag"
            "rhs_ec400_mag","rhs_ec75_sand_mag","rhs_ec200_sand_mag","rhs_ec400_sand_mag"
            "rhs_mine_m19_mag","rhsusf_mine_m14_mag","rhsusf_mine_m49a1_3m_mag","rhsusf_mine_m49a1_6m_mag"
            "rhsusf_mine_m49a1_10m_mag","rhsusf_m112_mag","rhsusf_m112x4_mag","rhs_mag_mine_pfm1"
            "rhs_mag_mine_ptm1","rhs_mine_smine35_press_mag","rhs_mine_smine35_trip_mag","rhs_mine_smine44_press_mag"
            "rhs_mine_smine44_trip_mag","rhs_mine_glasmine43_hz_mag","rhs_mine_glasmine43_bz_mag","rhs_mine_stockmine43_2m_mag"
            "rhs_mine_stockmine43_4m_mag","rhs_mine_a200_bz_mag","rhs_mine_a200_dz35_mag","rhs_mine_tm43_mag"
            "rhs_mine_m2a3b_press_mag","rhs_mine_m2a3b_trip_mag","rhs_mine_m3_pressure_mag","rhs_mine_mk2_pressure_mag"
            "rhs_mine_m3_tripwire_mag","rhs_mine_mk2_tripwire_mag","rhs_mine_m7a2_mag","rhs_charge_m2tet_x2_mag"
            "rhssaf_mine_pma3_mag","rhssaf_mine_tma4_mag","rhssaf_mine_mrud_a_mag","rhssaf_mine_mrud_b_mag"
            "rhssaf_mine_mrud_c_mag","rhssaf_mine_mrud_d_mag","rhssaf_tm100_mag","rhssaf_tm200_mag"
            "rhssaf_tm500_mag",],
        "sound": ["",0.000316228,1],
        "reloadsound": ["",0.000316228,1],
        "enableattack": 0,
        "optics": 0,
        "showempty": 0,
        "canlock": 0,
        "primary": 10,
        "minrange": 0,
        "minrangeprobab": 0.1,
        "midrange": 3,
        "midrangeprobab": 0.9,
        "maxrange": 15,
        "maxrangeprobab": 0.04,
        "movetointernal": 0,
        "opticszoommin": 0.25,
        "opticszoommax": 1.25,
        "opticszoominit": 0.75,
        "access": 3,
        "scope": 0,
        "value": 2,
        "picture": "",
        "uipicture": "",
        "ammo": "",
        "cursor": "",
        "cursoraim": "",
        "cursorsize": 1,
        "showaimcursorinternal": 1,
        "cursoraimon": "",
        "laser": 0,
        "hiddenselections": [],
        "hiddenselectionstextures": [],
        "hiddenunderwaterselections": [],
        "shownunderwaterselections": [],
        "hiddenunderwaterselectionstextures": [],
        "simulation": "Weapon",
        "type": 65536,
        "displayname": "",
        "namesound": "",
        "count": 0,
        "multiplier": 1,
        "burst": 1,
        "magazinereloadtime": 0,
        "reloadtime": 1,
        "magazinereloadswitchphase": 1,
        "soundbegin": ["sound",1],
        "soundbeginwater": ["sound",1],
        "soundclosure": ["sound",1],
        "soundend": ["sound",1],
        "soundloop": ["sound",1],
        "soundcontinuous": 0,
        "weaponsoundeffect": "",
        "soundburst": 1,
        "drysound": ["",1,1],
        "zeroingsound": ["",1,1],
        "changefiremodesound": ["",1,1],
        "reloadmagazinesound": ["",1,1],
        "emptysound": ["",1,1],
        "soundbullet": ["emptySound",1],
        "initspeed": 0,
        "ballisticscomputer": 0,
        "irdistance": 0,
        "irdotintensity": 0.001,
        "dispersion": 0.002,
        "aidispersioncoefx": 1,
        "aidispersioncoefy": 1,
        "lockacquire": 1,
        "ffmagnitude": 0,
        "fffrequency": 1,
        "ffcount": 1,
        # Recoil Array: recoil,
        "recoil": [],
        "recoil": "empty",
        "recoilprone": "",
        "maxrecoilsway": 0.008,
        "swaydecayspeed": 2,
        "model": "",
        "modelspecial": "",
        "modelmagazine": "",
        "muzzlepos": "usti hlavne",
        "muzzleend": "konec hlavne",
        "irlaserpos": "laser pos",
        "irlaserend": "laser dir",
        "cartridgepos": "nabojnicestart",
        "cartridgevel": "nabojniceend",
        "selectionfireanim": "zasleh",
        "memorypointcamera": "eye",
        "firespreadangle": 3,
        "usemodeloptics": 1,
        "opticsid": 0,
        "modeloptics": "",
        "opticsppeffects": [],
        "opticsflare": 1,
        "forceoptics": 0,
        "useasbinocular": 0,
        "opticsdisableperipherialvision": 0.67,
        "distancezoommin": 400,
        "distancezoommax": 400,
        "showswitchaction": 0,
        "autofire": 0,
        "autoreload": 1,
        "showtoplayer": 1,
        "canshootinwater": 0,
        "airateoffire": 5,
        "airateoffiredistance": 500,
        "airateoffiredispersion": 0,
        "firelightduration": 0.05,
        "firelightintensity": 0.2,
        "firelightdiffuse": [0.937,0.631,0.259],
        "firelightambient": [0,0,0],
        # Class: CfgWeapons|Default|Eventhandlers [Indent level: 1],
        "eventhandlers": {
        },
        "backgroundreload": 0,
        "reloadaction": "",
        "muzzles": ["this"],
        "modes": ["this"],
        "useaction": 0,
        "useactiontitle": "",
        "candrop": 1,
        "weaponlockdelay": 0,
        "weaponlocksystem": 0,
        "cmimmunity": 1,
        "weight": 0,
        "handanim": [],
        "lockingtargetsound": ["",0.000316228,2],
        "lockedtargetsound": ["",0.000316228,6],
        "detectrange": 0,
        "artillerydispersion": 1,
        "artillerycharge": 1,
        "fireanims": [],
        # Class: CfgWeapons|Default|Library [Indent level: 1],
        "library": {
            "libtextdesc": ""
        },
        "descriptionshort": "",
        # Class: CfgWeapons|Default|GunFire [Indent level: 1],
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
            "cloudletdensitycoef": -1,
            "interval": -0.01,
            "size": 3,
            "sourcesize": 0.5,
            "timetolive": 0,
            "initt": 4500,
            "deltat": -3000,
            # Class: CfgWeapons|Default|GunFire|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunFire|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [0.82,0.95,0.93,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T1 [Indent level: 3],
                "t1": {
                    "maxt": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T2 [Indent level: 3],
                "t2": {
                    "maxt": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T3 [Indent level: 3],
                "t3": {
                    "maxt": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T4 [Indent level: 3],
                "t4": {
                    "maxt": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T5 [Indent level: 3],
                "t5": {
                    "maxt": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T6 [Indent level: 3],
                "t6": {
                    "maxt": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T7 [Indent level: 3],
                "t7": {
                    "maxt": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T8 [Indent level: 3],
                "t8": {
                    "maxt": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T9 [Indent level: 3],
                "t9": {
                    "maxt": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T10 [Indent level: 3],
                "t10": {
                    "maxt": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T11 [Indent level: 3],
                "t11": {
                    "maxt": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T12 [Indent level: 3],
                "t12": {
                    "maxt": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T13 [Indent level: 3],
                "t13": {
                    "maxt": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T14 [Indent level: 3],
                "t14": {
                    "maxt": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T15 [Indent level: 3],
                "t15": {
                    "maxt": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T16 [Indent level: 3],
                "t16": {
                    "maxt": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T17 [Indent level: 3],
                "t17": {
                    "maxt": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T18 [Indent level: 3],
                "t18": {
                    "maxt": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T19 [Indent level: 3],
                "t19": {
                    "maxt": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T20 [Indent level: 3],
                "t20": {
                    "maxt": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T21 [Indent level: 3],
                "t21": {
                    "maxt": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T22 [Indent level: 3],
                "t22": {
                    "maxt": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgWeapons|Default|GunClouds [Indent level: 1],
        "gunclouds": {
            "access": 0,
            "cloudletgrowup": 0.05,
            "cloudletfadein": 0,
            "cloudletfadeout": 0.1,
            "cloudletduration": 0.05,
            "cloudletalpha": 0.3,
            "cloudletaccy": 0,
            "cloudletminyspeed": -100,
            "cloudletmaxyspeed": 100,
            "interval": -0.02,
            "size": 0.3,
            "sourcesize": 0.02,
            "cloudletanimperiod": 1,
            "cloudletsize": 1,
            "cloudletshape": "cloudletClouds",
            "cloudletcolor": [1,1,1,0],
            "timetolive": 0,
            "initt": 0,
            "deltat": 0,
            # Class: CfgWeapons|Default|GunClouds|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunClouds|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        "texturetype": "default",
        "inertia": 0.5,
        "aimtransitionspeed": 1
    },
    # Class: CfgWeapons|Put|rhsusf_m112_muzzle [Indent level: 1],
    "rhsusf_m112_muzzle": {
        "autoreload": 0,
        "displayname": "M112 charge",
        # Compatible Magazines: magazines parameter (+ inherited),
        "magazines": [
            "democharge_remote_mag","iedurbansmall_remote_mag","iedlandsmall_remote_mag","satchelcharge_remote_mag",
            "iedurbanbig_remote_mag","iedlandbig_remote_mag","atmine_range_mag","claymoredirectionalmine_remote_mag",
            "apersmine_range_mag","apersboundingmine_range_mag","slamdirectionalmine_wire_mag","aperstripmine_wire_mag",
            "apersminedispenser_mag","trainingmine_mag","rhs_mine_pmn2_mag","rhs_mine_tm62m_mag",
            "rhs_mine_msk40p_white_mag","rhs_mine_msk40p_red_mag","rhs_mine_msk40p_green_mag","rhs_mine_msk40p_blue_mag",
            "rhs_mine_sm320_white_mag","rhs_mine_sm320_red_mag","rhs_mine_sm320_green_mag","rhs_mine_ozm72_a_mag",
            "rhs_mine_ozm72_b_mag","rhs_mine_ozm72_c_mag","rhs_ec75_mag","rhs_ec200_mag",
            "rhs_ec400_mag","rhs_ec75_sand_mag","rhs_ec200_sand_mag","rhs_ec400_sand_mag",
            "rhs_mine_m19_mag","rhsusf_mine_m14_mag","rhsusf_mine_m49a1_3m_mag","rhsusf_mine_m49a1_6m_mag",
            "rhsusf_mine_m49a1_10m_mag","rhsusf_m112_mag","rhsusf_m112x4_mag","rhs_mag_mine_pfm1",
            "rhs_mag_mine_ptm1","rhs_mine_smine35_press_mag","rhs_mine_smine35_trip_mag","rhs_mine_smine44_press_mag",
            "rhs_mine_smine44_trip_mag","rhs_mine_glasmine43_hz_mag","rhs_mine_glasmine43_bz_mag","rhs_mine_stockmine43_2m_mag",
            "rhs_mine_stockmine43_4m_mag","rhs_mine_a200_bz_mag","rhs_mine_a200_dz35_mag","rhs_mine_tm43_mag",
            "rhs_mine_m2a3b_press_mag","rhs_mine_m2a3b_trip_mag","rhs_mine_m3_pressure_mag","rhs_mine_mk2_pressure_mag",
            "rhs_mine_m3_tripwire_mag","rhs_mine_mk2_tripwire_mag","rhs_mine_m7a2_mag","rhs_charge_m2tet_x2_mag",
            "rhssaf_mine_pma3_mag","rhssaf_mine_tma4_mag","rhssaf_mine_mrud_a_mag","rhssaf_mine_mrud_b_mag",
            "rhssaf_mine_mrud_c_mag","rhssaf_mine_mrud_d_mag","rhssaf_tm100_mag","rhssaf_tm200_mag",
            "rhssaf_tm500_mag",],
        "enableattack": 1,
        "showtoplayer": 0,
        "sound": ["",0.000316228,1],
        "reloadsound": ["",0.000316228,1],
        "optics": 0,
        "showempty": 0,
        "canlock": 0,
        "primary": 10,
        "minrange": 0,
        "minrangeprobab": 0.1,
        "midrange": 3,
        "midrangeprobab": 0.9,
        "maxrange": 15,
        "maxrangeprobab": 0.04,
        "movetointernal": 0,
        "opticszoommin": 0.25,
        "opticszoommax": 1.25,
        "opticszoominit": 0.75,
        "access": 3,
        "scope": 0,
        "value": 2,
        "picture": "",
        "uipicture": "",
        "ammo": "",
        "cursor": "",
        "cursoraim": "",
        "cursorsize": 1,
        "showaimcursorinternal": 1,
        "cursoraimon": "",
        "laser": 0,
        "hiddenselections": [],
        "hiddenselectionstextures": [],
        "hiddenunderwaterselections": [],
        "shownunderwaterselections": [],
        "hiddenunderwaterselectionstextures": [],
        "simulation": "Weapon",
        "type": 65536,
        "namesound": "",
        "count": 0,
        "multiplier": 1,
        "burst": 1,
        "magazinereloadtime": 0,
        "reloadtime": 1,
        "magazinereloadswitchphase": 1,
        "soundbegin": ["sound",1],
        "soundbeginwater": ["sound",1],
        "soundclosure": ["sound",1],
        "soundend": ["sound",1],
        "soundloop": ["sound",1],
        "soundcontinuous": 0,
        "weaponsoundeffect": "",
        "soundburst": 1,
        "drysound": ["",1,1],
        "zeroingsound": ["",1,1],
        "changefiremodesound": ["",1,1],
        "reloadmagazinesound": ["",1,1],
        "emptysound": ["",1,1],
        "soundbullet": ["emptySound",1],
        "initspeed": 0,
        "ballisticscomputer": 0,
        "irdistance": 0,
        "irdotintensity": 0.001,
        "dispersion": 0.002,
        "aidispersioncoefx": 1,
        "aidispersioncoefy": 1,
        "lockacquire": 1,
        "ffmagnitude": 0,
        "fffrequency": 1,
        "ffcount": 1,
        # Recoil Array: recoil,
        "recoil": [],
        "recoil": "empty",
        "recoilprone": "",
        "maxrecoilsway": 0.008,
        "swaydecayspeed": 2,
        "model": "",
        "modelspecial": "",
        "modelmagazine": "",
        "muzzlepos": "usti hlavne",
        "muzzleend": "konec hlavne",
        "irlaserpos": "laser pos",
        "irlaserend": "laser dir",
        "cartridgepos": "nabojnicestart",
        "cartridgevel": "nabojniceend",
        "selectionfireanim": "zasleh",
        "memorypointcamera": "eye",
        "firespreadangle": 3,
        "usemodeloptics": 1,
        "opticsid": 0,
        "modeloptics": "",
        "opticsppeffects": [],
        "opticsflare": 1,
        "forceoptics": 0,
        "useasbinocular": 0,
        "opticsdisableperipherialvision": 0.67,
        "distancezoommin": 400,
        "distancezoommax": 400,
        "showswitchaction": 0,
        "autofire": 0,
        "canshootinwater": 0,
        "airateoffire": 5,
        "airateoffiredistance": 500,
        "airateoffiredispersion": 0,
        "firelightduration": 0.05,
        "firelightintensity": 0.2,
        "firelightdiffuse": [0.937,0.631,0.259],
        "firelightambient": [0,0,0],
        # Class: CfgWeapons|Default|Eventhandlers [Indent level: 1],
        "eventhandlers": {
        },
        "backgroundreload": 0,
        "reloadaction": "",
        "muzzles": ["this"],
        "modes": ["this"],
        "useaction": 0,
        "useactiontitle": "",
        "candrop": 1,
        "weaponlockdelay": 0,
        "weaponlocksystem": 0,
        "cmimmunity": 1,
        "weight": 0,
        "handanim": [],
        "lockingtargetsound": ["",0.000316228,2],
        "lockedtargetsound": ["",0.000316228,6],
        "detectrange": 0,
        "artillerydispersion": 1,
        "artillerycharge": 1,
        "fireanims": [],
        # Class: CfgWeapons|Default|Library [Indent level: 1],
        "library": {
            "libtextdesc": ""
        },
        "descriptionshort": "",
        # Class: CfgWeapons|Default|GunFire [Indent level: 1],
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
            "cloudletdensitycoef": -1,
            "interval": -0.01,
            "size": 3,
            "sourcesize": 0.5,
            "timetolive": 0,
            "initt": 4500,
            "deltat": -3000,
            # Class: CfgWeapons|Default|GunFire|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunFire|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [0.82,0.95,0.93,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T1 [Indent level: 3],
                "t1": {
                    "maxt": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T2 [Indent level: 3],
                "t2": {
                    "maxt": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T3 [Indent level: 3],
                "t3": {
                    "maxt": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T4 [Indent level: 3],
                "t4": {
                    "maxt": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T5 [Indent level: 3],
                "t5": {
                    "maxt": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T6 [Indent level: 3],
                "t6": {
                    "maxt": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T7 [Indent level: 3],
                "t7": {
                    "maxt": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T8 [Indent level: 3],
                "t8": {
                    "maxt": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T9 [Indent level: 3],
                "t9": {
                    "maxt": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T10 [Indent level: 3],
                "t10": {
                    "maxt": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T11 [Indent level: 3],
                "t11": {
                    "maxt": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T12 [Indent level: 3],
                "t12": {
                    "maxt": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T13 [Indent level: 3],
                "t13": {
                    "maxt": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T14 [Indent level: 3],
                "t14": {
                    "maxt": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T15 [Indent level: 3],
                "t15": {
                    "maxt": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T16 [Indent level: 3],
                "t16": {
                    "maxt": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T17 [Indent level: 3],
                "t17": {
                    "maxt": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T18 [Indent level: 3],
                "t18": {
                    "maxt": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T19 [Indent level: 3],
                "t19": {
                    "maxt": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T20 [Indent level: 3],
                "t20": {
                    "maxt": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T21 [Indent level: 3],
                "t21": {
                    "maxt": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T22 [Indent level: 3],
                "t22": {
                    "maxt": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgWeapons|Default|GunClouds [Indent level: 1],
        "gunclouds": {
            "access": 0,
            "cloudletgrowup": 0.05,
            "cloudletfadein": 0,
            "cloudletfadeout": 0.1,
            "cloudletduration": 0.05,
            "cloudletalpha": 0.3,
            "cloudletaccy": 0,
            "cloudletminyspeed": -100,
            "cloudletmaxyspeed": 100,
            "interval": -0.02,
            "size": 0.3,
            "sourcesize": 0.02,
            "cloudletanimperiod": 1,
            "cloudletsize": 1,
            "cloudletshape": "cloudletClouds",
            "cloudletcolor": [1,1,1,0],
            "timetolive": 0,
            "initt": 0,
            "deltat": 0,
            # Class: CfgWeapons|Default|GunClouds|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunClouds|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        "texturetype": "default",
        "inertia": 0.5,
        "aimtransitionspeed": 1
    },
    # Class: CfgWeapons|Put|rhsusf_m112x4_muzzle [Indent level: 1],
    "rhsusf_m112x4_muzzle": {
        "autoreload": 0,
        "displayname": "M112 x4 charge pack",
        # Compatible Magazines: magazines parameter (+ inherited),
        "magazines": [
            "democharge_remote_mag","iedurbansmall_remote_mag","iedlandsmall_remote_mag","satchelcharge_remote_mag",
            "iedurbanbig_remote_mag","iedlandbig_remote_mag","atmine_range_mag","claymoredirectionalmine_remote_mag",
            "apersmine_range_mag","apersboundingmine_range_mag","slamdirectionalmine_wire_mag","aperstripmine_wire_mag",
            "apersminedispenser_mag","trainingmine_mag","rhs_mine_pmn2_mag","rhs_mine_tm62m_mag",
            "rhs_mine_msk40p_white_mag","rhs_mine_msk40p_red_mag","rhs_mine_msk40p_green_mag","rhs_mine_msk40p_blue_mag",
            "rhs_mine_sm320_white_mag","rhs_mine_sm320_red_mag","rhs_mine_sm320_green_mag","rhs_mine_ozm72_a_mag",
            "rhs_mine_ozm72_b_mag","rhs_mine_ozm72_c_mag","rhs_ec75_mag","rhs_ec200_mag",
            "rhs_ec400_mag","rhs_ec75_sand_mag","rhs_ec200_sand_mag","rhs_ec400_sand_mag",
            "rhs_mine_m19_mag","rhsusf_mine_m14_mag","rhsusf_mine_m49a1_3m_mag","rhsusf_mine_m49a1_6m_mag",
            "rhsusf_mine_m49a1_10m_mag","rhsusf_m112_mag","rhsusf_m112x4_mag","rhs_mag_mine_pfm1",
            "rhs_mag_mine_ptm1","rhs_mine_smine35_press_mag","rhs_mine_smine35_trip_mag","rhs_mine_smine44_press_mag",
            "rhs_mine_smine44_trip_mag","rhs_mine_glasmine43_hz_mag","rhs_mine_glasmine43_bz_mag","rhs_mine_stockmine43_2m_mag",
            "rhs_mine_stockmine43_4m_mag","rhs_mine_a200_bz_mag","rhs_mine_a200_dz35_mag","rhs_mine_tm43_mag",
            "rhs_mine_m2a3b_press_mag","rhs_mine_m2a3b_trip_mag","rhs_mine_m3_pressure_mag","rhs_mine_mk2_pressure_mag",
            "rhs_mine_m3_tripwire_mag","rhs_mine_mk2_tripwire_mag","rhs_mine_m7a2_mag","rhs_charge_m2tet_x2_mag",
            "rhssaf_mine_pma3_mag","rhssaf_mine_tma4_mag","rhssaf_mine_mrud_a_mag","rhssaf_mine_mrud_b_mag",
            "rhssaf_mine_mrud_c_mag","rhssaf_mine_mrud_d_mag","rhssaf_tm100_mag","rhssaf_tm200_mag",
            "rhssaf_tm500_mag",],
        "enableattack": 1,
        "showtoplayer": 0,
        "sound": ["",0.000316228,1],
        "reloadsound": ["",0.000316228,1],
        "optics": 0,
        "showempty": 0,
        "canlock": 0,
        "primary": 10,
        "minrange": 0,
        "minrangeprobab": 0.1,
        "midrange": 3,
        "midrangeprobab": 0.9,
        "maxrange": 15,
        "maxrangeprobab": 0.04,
        "movetointernal": 0,
        "opticszoommin": 0.25,
        "opticszoommax": 1.25,
        "opticszoominit": 0.75,
        "access": 3,
        "scope": 0,
        "value": 2,
        "picture": "",
        "uipicture": "",
        "ammo": "",
        "cursor": "",
        "cursoraim": "",
        "cursorsize": 1,
        "showaimcursorinternal": 1,
        "cursoraimon": "",
        "laser": 0,
        "hiddenselections": [],
        "hiddenselectionstextures": [],
        "hiddenunderwaterselections": [],
        "shownunderwaterselections": [],
        "hiddenunderwaterselectionstextures": [],
        "simulation": "Weapon",
        "type": 65536,
        "namesound": "",
        "count": 0,
        "multiplier": 1,
        "burst": 1,
        "magazinereloadtime": 0,
        "reloadtime": 1,
        "magazinereloadswitchphase": 1,
        "soundbegin": ["sound",1],
        "soundbeginwater": ["sound",1],
        "soundclosure": ["sound",1],
        "soundend": ["sound",1],
        "soundloop": ["sound",1],
        "soundcontinuous": 0,
        "weaponsoundeffect": "",
        "soundburst": 1,
        "drysound": ["",1,1],
        "zeroingsound": ["",1,1],
        "changefiremodesound": ["",1,1],
        "reloadmagazinesound": ["",1,1],
        "emptysound": ["",1,1],
        "soundbullet": ["emptySound",1],
        "initspeed": 0,
        "ballisticscomputer": 0,
        "irdistance": 0,
        "irdotintensity": 0.001,
        "dispersion": 0.002,
        "aidispersioncoefx": 1,
        "aidispersioncoefy": 1,
        "lockacquire": 1,
        "ffmagnitude": 0,
        "fffrequency": 1,
        "ffcount": 1,
        # Recoil Array: recoil,
        "recoil": [],
        "recoil": "empty",
        "recoilprone": "",
        "maxrecoilsway": 0.008,
        "swaydecayspeed": 2,
        "model": "",
        "modelspecial": "",
        "modelmagazine": "",
        "muzzlepos": "usti hlavne",
        "muzzleend": "konec hlavne",
        "irlaserpos": "laser pos",
        "irlaserend": "laser dir",
        "cartridgepos": "nabojnicestart",
        "cartridgevel": "nabojniceend",
        "selectionfireanim": "zasleh",
        "memorypointcamera": "eye",
        "firespreadangle": 3,
        "usemodeloptics": 1,
        "opticsid": 0,
        "modeloptics": "",
        "opticsppeffects": [],
        "opticsflare": 1,
        "forceoptics": 0,
        "useasbinocular": 0,
        "opticsdisableperipherialvision": 0.67,
        "distancezoommin": 400,
        "distancezoommax": 400,
        "showswitchaction": 0,
        "autofire": 0,
        "canshootinwater": 0,
        "airateoffire": 5,
        "airateoffiredistance": 500,
        "airateoffiredispersion": 0,
        "firelightduration": 0.05,
        "firelightintensity": 0.2,
        "firelightdiffuse": [0.937,0.631,0.259],
        "firelightambient": [0,0,0],
        # Class: CfgWeapons|Default|Eventhandlers [Indent level: 1],
        "eventhandlers": {
        },
        "backgroundreload": 0,
        "reloadaction": "",
        "muzzles": ["this"],
        "modes": ["this"],
        "useaction": 0,
        "useactiontitle": "",
        "candrop": 1,
        "weaponlockdelay": 0,
        "weaponlocksystem": 0,
        "cmimmunity": 1,
        "weight": 0,
        "handanim": [],
        "lockingtargetsound": ["",0.000316228,2],
        "lockedtargetsound": ["",0.000316228,6],
        "detectrange": 0,
        "artillerydispersion": 1,
        "artillerycharge": 1,
        "fireanims": [],
        # Class: CfgWeapons|Default|Library [Indent level: 1],
        "library": {
            "libtextdesc": ""
        },
        "descriptionshort": "",
        # Class: CfgWeapons|Default|GunFire [Indent level: 1],
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
            "cloudletdensitycoef": -1,
            "interval": -0.01,
            "size": 3,
            "sourcesize": 0.5,
            "timetolive": 0,
            "initt": 4500,
            "deltat": -3000,
            # Class: CfgWeapons|Default|GunFire|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunFire|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [0.82,0.95,0.93,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T1 [Indent level: 3],
                "t1": {
                    "maxt": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T2 [Indent level: 3],
                "t2": {
                    "maxt": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T3 [Indent level: 3],
                "t3": {
                    "maxt": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T4 [Indent level: 3],
                "t4": {
                    "maxt": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T5 [Indent level: 3],
                "t5": {
                    "maxt": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T6 [Indent level: 3],
                "t6": {
                    "maxt": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T7 [Indent level: 3],
                "t7": {
                    "maxt": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T8 [Indent level: 3],
                "t8": {
                    "maxt": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T9 [Indent level: 3],
                "t9": {
                    "maxt": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T10 [Indent level: 3],
                "t10": {
                    "maxt": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T11 [Indent level: 3],
                "t11": {
                    "maxt": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T12 [Indent level: 3],
                "t12": {
                    "maxt": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T13 [Indent level: 3],
                "t13": {
                    "maxt": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T14 [Indent level: 3],
                "t14": {
                    "maxt": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T15 [Indent level: 3],
                "t15": {
                    "maxt": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T16 [Indent level: 3],
                "t16": {
                    "maxt": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T17 [Indent level: 3],
                "t17": {
                    "maxt": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T18 [Indent level: 3],
                "t18": {
                    "maxt": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T19 [Indent level: 3],
                "t19": {
                    "maxt": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T20 [Indent level: 3],
                "t20": {
                    "maxt": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T21 [Indent level: 3],
                "t21": {
                    "maxt": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T22 [Indent level: 3],
                "t22": {
                    "maxt": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgWeapons|Default|GunClouds [Indent level: 1],
        "gunclouds": {
            "access": 0,
            "cloudletgrowup": 0.05,
            "cloudletfadein": 0,
            "cloudletfadeout": 0.1,
            "cloudletduration": 0.05,
            "cloudletalpha": 0.3,
            "cloudletaccy": 0,
            "cloudletminyspeed": -100,
            "cloudletmaxyspeed": 100,
            "interval": -0.02,
            "size": 0.3,
            "sourcesize": 0.02,
            "cloudletanimperiod": 1,
            "cloudletsize": 1,
            "cloudletshape": "cloudletClouds",
            "cloudletcolor": [1,1,1,0],
            "timetolive": 0,
            "initt": 0,
            "deltat": 0,
            # Class: CfgWeapons|Default|GunClouds|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunClouds|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        "texturetype": "default",
        "inertia": 0.5,
        "aimtransitionspeed": 1
    },
    # Class: CfgWeapons|Put|Rhs_SmallMine_Muzzle [Indent level: 1],
    "rhs_smallmine_muzzle": {
        # Compatible Magazines: magazines parameter (+ inherited)
        "magazines": [
            "democharge_remote_mag","iedurbansmall_remote_mag","iedlandsmall_remote_mag","satchelcharge_remote_mag"
            "iedurbanbig_remote_mag","iedlandbig_remote_mag","atmine_range_mag","claymoredirectionalmine_remote_mag"
            "apersmine_range_mag","apersboundingmine_range_mag","slamdirectionalmine_wire_mag","aperstripmine_wire_mag"
            "apersminedispenser_mag","trainingmine_mag","rhs_mine_pmn2_mag","rhs_mine_tm62m_mag"
            "rhs_mine_msk40p_white_mag","rhs_mine_msk40p_red_mag","rhs_mine_msk40p_green_mag","rhs_mine_msk40p_blue_mag"
            "rhs_mine_sm320_white_mag","rhs_mine_sm320_red_mag","rhs_mine_sm320_green_mag","rhs_mine_ozm72_a_mag"
            "rhs_mine_ozm72_b_mag","rhs_mine_ozm72_c_mag","rhs_ec75_mag","rhs_ec200_mag"
            "rhs_ec400_mag","rhs_ec75_sand_mag","rhs_ec200_sand_mag","rhs_ec400_sand_mag"
            "rhs_mine_m19_mag","rhsusf_mine_m14_mag","rhsusf_mine_m49a1_3m_mag","rhsusf_mine_m49a1_6m_mag"
            "rhsusf_mine_m49a1_10m_mag","rhsusf_m112_mag","rhsusf_m112x4_mag","rhs_mag_mine_pfm1"
            "rhs_mag_mine_ptm1","rhs_mine_smine35_press_mag","rhs_mine_smine35_trip_mag","rhs_mine_smine44_press_mag"
            "rhs_mine_smine44_trip_mag","rhs_mine_glasmine43_hz_mag","rhs_mine_glasmine43_bz_mag","rhs_mine_stockmine43_2m_mag"
            "rhs_mine_stockmine43_4m_mag","rhs_mine_a200_bz_mag","rhs_mine_a200_dz35_mag","rhs_mine_tm43_mag"
            "rhs_mine_m2a3b_press_mag","rhs_mine_m2a3b_trip_mag","rhs_mine_m3_pressure_mag","rhs_mine_mk2_pressure_mag"
            "rhs_mine_m3_tripwire_mag","rhs_mine_mk2_tripwire_mag","rhs_mine_m7a2_mag","rhs_charge_m2tet_x2_mag"
            "rhssaf_mine_pma3_mag","rhssaf_mine_tma4_mag","rhssaf_mine_mrud_a_mag","rhssaf_mine_mrud_b_mag"
            "rhssaf_mine_mrud_c_mag","rhssaf_mine_mrud_d_mag","rhssaf_tm100_mag","rhssaf_tm200_mag"
            "rhssaf_tm500_mag",],
        "sound": ["",0.000316228,1],
        "reloadsound": ["",0.000316228,1],
        "enableattack": 0,
        "optics": 0,
        "showempty": 0,
        "canlock": 0,
        "primary": 10,
        "minrange": 0,
        "minrangeprobab": 0.1,
        "midrange": 3,
        "midrangeprobab": 0.9,
        "maxrange": 15,
        "maxrangeprobab": 0.04,
        "movetointernal": 0,
        "opticszoommin": 0.25,
        "opticszoommax": 1.25,
        "opticszoominit": 0.75,
        "access": 3,
        "scope": 0,
        "value": 2,
        "picture": "",
        "uipicture": "",
        "ammo": "",
        "cursor": "",
        "cursoraim": "",
        "cursorsize": 1,
        "showaimcursorinternal": 1,
        "cursoraimon": "",
        "laser": 0,
        "hiddenselections": [],
        "hiddenselectionstextures": [],
        "hiddenunderwaterselections": [],
        "shownunderwaterselections": [],
        "hiddenunderwaterselectionstextures": [],
        "simulation": "Weapon",
        "type": 65536,
        "displayname": "",
        "namesound": "",
        "count": 0,
        "multiplier": 1,
        "burst": 1,
        "magazinereloadtime": 0,
        "reloadtime": 1,
        "magazinereloadswitchphase": 1,
        "soundbegin": ["sound",1],
        "soundbeginwater": ["sound",1],
        "soundclosure": ["sound",1],
        "soundend": ["sound",1],
        "soundloop": ["sound",1],
        "soundcontinuous": 0,
        "weaponsoundeffect": "",
        "soundburst": 1,
        "drysound": ["",1,1],
        "zeroingsound": ["",1,1],
        "changefiremodesound": ["",1,1],
        "reloadmagazinesound": ["",1,1],
        "emptysound": ["",1,1],
        "soundbullet": ["emptySound",1],
        "initspeed": 0,
        "ballisticscomputer": 0,
        "irdistance": 0,
        "irdotintensity": 0.001,
        "dispersion": 0.002,
        "aidispersioncoefx": 1,
        "aidispersioncoefy": 1,
        "lockacquire": 1,
        "ffmagnitude": 0,
        "fffrequency": 1,
        "ffcount": 1,
        # Recoil Array: recoil,
        "recoil": [],
        "recoil": "empty",
        "recoilprone": "",
        "maxrecoilsway": 0.008,
        "swaydecayspeed": 2,
        "model": "",
        "modelspecial": "",
        "modelmagazine": "",
        "muzzlepos": "usti hlavne",
        "muzzleend": "konec hlavne",
        "irlaserpos": "laser pos",
        "irlaserend": "laser dir",
        "cartridgepos": "nabojnicestart",
        "cartridgevel": "nabojniceend",
        "selectionfireanim": "zasleh",
        "memorypointcamera": "eye",
        "firespreadangle": 3,
        "usemodeloptics": 1,
        "opticsid": 0,
        "modeloptics": "",
        "opticsppeffects": [],
        "opticsflare": 1,
        "forceoptics": 0,
        "useasbinocular": 0,
        "opticsdisableperipherialvision": 0.67,
        "distancezoommin": 400,
        "distancezoommax": 400,
        "showswitchaction": 0,
        "autofire": 0,
        "autoreload": 1,
        "showtoplayer": 1,
        "canshootinwater": 0,
        "airateoffire": 5,
        "airateoffiredistance": 500,
        "airateoffiredispersion": 0,
        "firelightduration": 0.05,
        "firelightintensity": 0.2,
        "firelightdiffuse": [0.937,0.631,0.259],
        "firelightambient": [0,0,0],
        # Class: CfgWeapons|Default|Eventhandlers [Indent level: 1],
        "eventhandlers": {
        },
        "backgroundreload": 0,
        "reloadaction": "",
        "muzzles": ["this"],
        "modes": ["this"],
        "useaction": 0,
        "useactiontitle": "",
        "candrop": 1,
        "weaponlockdelay": 0,
        "weaponlocksystem": 0,
        "cmimmunity": 1,
        "weight": 0,
        "handanim": [],
        "lockingtargetsound": ["",0.000316228,2],
        "lockedtargetsound": ["",0.000316228,6],
        "detectrange": 0,
        "artillerydispersion": 1,
        "artillerycharge": 1,
        "fireanims": [],
        # Class: CfgWeapons|Default|Library [Indent level: 1],
        "library": {
            "libtextdesc": ""
        },
        "descriptionshort": "",
        # Class: CfgWeapons|Default|GunFire [Indent level: 1],
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
            "cloudletdensitycoef": -1,
            "interval": -0.01,
            "size": 3,
            "sourcesize": 0.5,
            "timetolive": 0,
            "initt": 4500,
            "deltat": -3000,
            # Class: CfgWeapons|Default|GunFire|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunFire|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [0.82,0.95,0.93,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T1 [Indent level: 3],
                "t1": {
                    "maxt": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T2 [Indent level: 3],
                "t2": {
                    "maxt": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T3 [Indent level: 3],
                "t3": {
                    "maxt": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T4 [Indent level: 3],
                "t4": {
                    "maxt": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T5 [Indent level: 3],
                "t5": {
                    "maxt": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T6 [Indent level: 3],
                "t6": {
                    "maxt": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T7 [Indent level: 3],
                "t7": {
                    "maxt": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T8 [Indent level: 3],
                "t8": {
                    "maxt": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T9 [Indent level: 3],
                "t9": {
                    "maxt": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T10 [Indent level: 3],
                "t10": {
                    "maxt": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T11 [Indent level: 3],
                "t11": {
                    "maxt": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T12 [Indent level: 3],
                "t12": {
                    "maxt": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T13 [Indent level: 3],
                "t13": {
                    "maxt": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T14 [Indent level: 3],
                "t14": {
                    "maxt": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T15 [Indent level: 3],
                "t15": {
                    "maxt": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T16 [Indent level: 3],
                "t16": {
                    "maxt": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T17 [Indent level: 3],
                "t17": {
                    "maxt": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T18 [Indent level: 3],
                "t18": {
                    "maxt": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T19 [Indent level: 3],
                "t19": {
                    "maxt": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T20 [Indent level: 3],
                "t20": {
                    "maxt": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T21 [Indent level: 3],
                "t21": {
                    "maxt": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T22 [Indent level: 3],
                "t22": {
                    "maxt": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgWeapons|Default|GunClouds [Indent level: 1],
        "gunclouds": {
            "access": 0,
            "cloudletgrowup": 0.05,
            "cloudletfadein": 0,
            "cloudletfadeout": 0.1,
            "cloudletduration": 0.05,
            "cloudletalpha": 0.3,
            "cloudletaccy": 0,
            "cloudletminyspeed": -100,
            "cloudletmaxyspeed": 100,
            "interval": -0.02,
            "size": 0.3,
            "sourcesize": 0.02,
            "cloudletanimperiod": 1,
            "cloudletsize": 1,
            "cloudletshape": "cloudletClouds",
            "cloudletcolor": [1,1,1,0],
            "timetolive": 0,
            "initt": 0,
            "deltat": 0,
            # Class: CfgWeapons|Default|GunClouds|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunClouds|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        "texturetype": "default",
        "inertia": 0.5,
        "aimtransitionspeed": 1
    },
    # Class: CfgWeapons|Put|rhsgref_Mine_Muzzle [Indent level: 1],
    "rhsgref_mine_muzzle": {
        # Compatible Magazines: magazines parameter (+ inherited)
        "magazines": [
            "democharge_remote_mag","iedurbansmall_remote_mag","iedlandsmall_remote_mag","satchelcharge_remote_mag"
            "iedurbanbig_remote_mag","iedlandbig_remote_mag","atmine_range_mag","claymoredirectionalmine_remote_mag"
            "apersmine_range_mag","apersboundingmine_range_mag","slamdirectionalmine_wire_mag","aperstripmine_wire_mag"
            "apersminedispenser_mag","trainingmine_mag","rhs_mine_pmn2_mag","rhs_mine_tm62m_mag"
            "rhs_mine_msk40p_white_mag","rhs_mine_msk40p_red_mag","rhs_mine_msk40p_green_mag","rhs_mine_msk40p_blue_mag"
            "rhs_mine_sm320_white_mag","rhs_mine_sm320_red_mag","rhs_mine_sm320_green_mag","rhs_mine_ozm72_a_mag"
            "rhs_mine_ozm72_b_mag","rhs_mine_ozm72_c_mag","rhs_ec75_mag","rhs_ec200_mag"
            "rhs_ec400_mag","rhs_ec75_sand_mag","rhs_ec200_sand_mag","rhs_ec400_sand_mag"
            "rhs_mine_m19_mag","rhsusf_mine_m14_mag","rhsusf_mine_m49a1_3m_mag","rhsusf_mine_m49a1_6m_mag"
            "rhsusf_mine_m49a1_10m_mag","rhsusf_m112_mag","rhsusf_m112x4_mag","rhs_mag_mine_pfm1"
            "rhs_mag_mine_ptm1","rhs_mine_smine35_press_mag","rhs_mine_smine35_trip_mag","rhs_mine_smine44_press_mag"
            "rhs_mine_smine44_trip_mag","rhs_mine_glasmine43_hz_mag","rhs_mine_glasmine43_bz_mag","rhs_mine_stockmine43_2m_mag"
            "rhs_mine_stockmine43_4m_mag","rhs_mine_a200_bz_mag","rhs_mine_a200_dz35_mag","rhs_mine_tm43_mag"
            "rhs_mine_m2a3b_press_mag","rhs_mine_m2a3b_trip_mag","rhs_mine_m3_pressure_mag","rhs_mine_mk2_pressure_mag"
            "rhs_mine_m3_tripwire_mag","rhs_mine_mk2_tripwire_mag","rhs_mine_m7a2_mag","rhs_charge_m2tet_x2_mag"
            "rhssaf_mine_pma3_mag","rhssaf_mine_tma4_mag","rhssaf_mine_mrud_a_mag","rhssaf_mine_mrud_b_mag"
            "rhssaf_mine_mrud_c_mag","rhssaf_mine_mrud_d_mag","rhssaf_tm100_mag","rhssaf_tm200_mag"
            "rhssaf_tm500_mag",],
        "sound": ["",0.000316228,1],
        "reloadsound": ["",0.000316228,1],
        "enableattack": 0,
        "optics": 0,
        "showempty": 0,
        "canlock": 0,
        "primary": 10,
        "minrange": 0,
        "minrangeprobab": 0.1,
        "midrange": 3,
        "midrangeprobab": 0.9,
        "maxrange": 15,
        "maxrangeprobab": 0.04,
        "movetointernal": 0,
        "opticszoommin": 0.25,
        "opticszoommax": 1.25,
        "opticszoominit": 0.75,
        "access": 3,
        "scope": 0,
        "value": 2,
        "picture": "",
        "uipicture": "",
        "ammo": "",
        "cursor": "",
        "cursoraim": "",
        "cursorsize": 1,
        "showaimcursorinternal": 1,
        "cursoraimon": "",
        "laser": 0,
        "hiddenselections": [],
        "hiddenselectionstextures": [],
        "hiddenunderwaterselections": [],
        "shownunderwaterselections": [],
        "hiddenunderwaterselectionstextures": [],
        "simulation": "Weapon",
        "type": 65536,
        "displayname": "",
        "namesound": "",
        "count": 0,
        "multiplier": 1,
        "burst": 1,
        "magazinereloadtime": 0,
        "reloadtime": 1,
        "magazinereloadswitchphase": 1,
        "soundbegin": ["sound",1],
        "soundbeginwater": ["sound",1],
        "soundclosure": ["sound",1],
        "soundend": ["sound",1],
        "soundloop": ["sound",1],
        "soundcontinuous": 0,
        "weaponsoundeffect": "",
        "soundburst": 1,
        "drysound": ["",1,1],
        "zeroingsound": ["",1,1],
        "changefiremodesound": ["",1,1],
        "reloadmagazinesound": ["",1,1],
        "emptysound": ["",1,1],
        "soundbullet": ["emptySound",1],
        "initspeed": 0,
        "ballisticscomputer": 0,
        "irdistance": 0,
        "irdotintensity": 0.001,
        "dispersion": 0.002,
        "aidispersioncoefx": 1,
        "aidispersioncoefy": 1,
        "lockacquire": 1,
        "ffmagnitude": 0,
        "fffrequency": 1,
        "ffcount": 1,
        # Recoil Array: recoil,
        "recoil": [],
        "recoil": "empty",
        "recoilprone": "",
        "maxrecoilsway": 0.008,
        "swaydecayspeed": 2,
        "model": "",
        "modelspecial": "",
        "modelmagazine": "",
        "muzzlepos": "usti hlavne",
        "muzzleend": "konec hlavne",
        "irlaserpos": "laser pos",
        "irlaserend": "laser dir",
        "cartridgepos": "nabojnicestart",
        "cartridgevel": "nabojniceend",
        "selectionfireanim": "zasleh",
        "memorypointcamera": "eye",
        "firespreadangle": 3,
        "usemodeloptics": 1,
        "opticsid": 0,
        "modeloptics": "",
        "opticsppeffects": [],
        "opticsflare": 1,
        "forceoptics": 0,
        "useasbinocular": 0,
        "opticsdisableperipherialvision": 0.67,
        "distancezoommin": 400,
        "distancezoommax": 400,
        "showswitchaction": 0,
        "autofire": 0,
        "autoreload": 1,
        "showtoplayer": 1,
        "canshootinwater": 0,
        "airateoffire": 5,
        "airateoffiredistance": 500,
        "airateoffiredispersion": 0,
        "firelightduration": 0.05,
        "firelightintensity": 0.2,
        "firelightdiffuse": [0.937,0.631,0.259],
        "firelightambient": [0,0,0],
        # Class: CfgWeapons|Default|Eventhandlers [Indent level: 1],
        "eventhandlers": {
        },
        "backgroundreload": 0,
        "reloadaction": "",
        "muzzles": ["this"],
        "modes": ["this"],
        "useaction": 0,
        "useactiontitle": "",
        "candrop": 1,
        "weaponlockdelay": 0,
        "weaponlocksystem": 0,
        "cmimmunity": 1,
        "weight": 0,
        "handanim": [],
        "lockingtargetsound": ["",0.000316228,2],
        "lockedtargetsound": ["",0.000316228,6],
        "detectrange": 0,
        "artillerydispersion": 1,
        "artillerycharge": 1,
        "fireanims": [],
        # Class: CfgWeapons|Default|Library [Indent level: 1],
        "library": {
            "libtextdesc": ""
        },
        "descriptionshort": "",
        # Class: CfgWeapons|Default|GunFire [Indent level: 1],
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
            "cloudletdensitycoef": -1,
            "interval": -0.01,
            "size": 3,
            "sourcesize": 0.5,
            "timetolive": 0,
            "initt": 4500,
            "deltat": -3000,
            # Class: CfgWeapons|Default|GunFire|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunFire|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [0.82,0.95,0.93,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T1 [Indent level: 3],
                "t1": {
                    "maxt": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T2 [Indent level: 3],
                "t2": {
                    "maxt": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T3 [Indent level: 3],
                "t3": {
                    "maxt": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T4 [Indent level: 3],
                "t4": {
                    "maxt": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T5 [Indent level: 3],
                "t5": {
                    "maxt": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T6 [Indent level: 3],
                "t6": {
                    "maxt": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T7 [Indent level: 3],
                "t7": {
                    "maxt": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T8 [Indent level: 3],
                "t8": {
                    "maxt": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T9 [Indent level: 3],
                "t9": {
                    "maxt": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T10 [Indent level: 3],
                "t10": {
                    "maxt": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T11 [Indent level: 3],
                "t11": {
                    "maxt": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T12 [Indent level: 3],
                "t12": {
                    "maxt": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T13 [Indent level: 3],
                "t13": {
                    "maxt": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T14 [Indent level: 3],
                "t14": {
                    "maxt": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T15 [Indent level: 3],
                "t15": {
                    "maxt": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T16 [Indent level: 3],
                "t16": {
                    "maxt": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T17 [Indent level: 3],
                "t17": {
                    "maxt": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T18 [Indent level: 3],
                "t18": {
                    "maxt": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T19 [Indent level: 3],
                "t19": {
                    "maxt": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T20 [Indent level: 3],
                "t20": {
                    "maxt": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T21 [Indent level: 3],
                "t21": {
                    "maxt": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T22 [Indent level: 3],
                "t22": {
                    "maxt": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgWeapons|Default|GunClouds [Indent level: 1],
        "gunclouds": {
            "access": 0,
            "cloudletgrowup": 0.05,
            "cloudletfadein": 0,
            "cloudletfadeout": 0.1,
            "cloudletduration": 0.05,
            "cloudletalpha": 0.3,
            "cloudletaccy": 0,
            "cloudletminyspeed": -100,
            "cloudletmaxyspeed": 100,
            "interval": -0.02,
            "size": 0.3,
            "sourcesize": 0.02,
            "cloudletanimperiod": 1,
            "cloudletsize": 1,
            "cloudletshape": "cloudletClouds",
            "cloudletcolor": [1,1,1,0],
            "timetolive": 0,
            "initt": 0,
            "deltat": 0,
            # Class: CfgWeapons|Default|GunClouds|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunClouds|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        "texturetype": "default",
        "inertia": 0.5,
        "aimtransitionspeed": 1
    },
    # Class: CfgWeapons|Put|Rhssaf_Mine_Muzzle [Indent level: 1],
    "rhssaf_mine_muzzle": {
        # Compatible Magazines: magazines parameter (+ inherited)
        "magazines": [
            "democharge_remote_mag","iedurbansmall_remote_mag","iedlandsmall_remote_mag","satchelcharge_remote_mag"
            "iedurbanbig_remote_mag","iedlandbig_remote_mag","atmine_range_mag","claymoredirectionalmine_remote_mag"
            "apersmine_range_mag","apersboundingmine_range_mag","slamdirectionalmine_wire_mag","aperstripmine_wire_mag"
            "apersminedispenser_mag","trainingmine_mag","rhs_mine_pmn2_mag","rhs_mine_tm62m_mag"
            "rhs_mine_msk40p_white_mag","rhs_mine_msk40p_red_mag","rhs_mine_msk40p_green_mag","rhs_mine_msk40p_blue_mag"
            "rhs_mine_sm320_white_mag","rhs_mine_sm320_red_mag","rhs_mine_sm320_green_mag","rhs_mine_ozm72_a_mag"
            "rhs_mine_ozm72_b_mag","rhs_mine_ozm72_c_mag","rhs_ec75_mag","rhs_ec200_mag"
            "rhs_ec400_mag","rhs_ec75_sand_mag","rhs_ec200_sand_mag","rhs_ec400_sand_mag"
            "rhs_mine_m19_mag","rhsusf_mine_m14_mag","rhsusf_mine_m49a1_3m_mag","rhsusf_mine_m49a1_6m_mag"
            "rhsusf_mine_m49a1_10m_mag","rhsusf_m112_mag","rhsusf_m112x4_mag","rhs_mag_mine_pfm1"
            "rhs_mag_mine_ptm1","rhs_mine_smine35_press_mag","rhs_mine_smine35_trip_mag","rhs_mine_smine44_press_mag"
            "rhs_mine_smine44_trip_mag","rhs_mine_glasmine43_hz_mag","rhs_mine_glasmine43_bz_mag","rhs_mine_stockmine43_2m_mag"
            "rhs_mine_stockmine43_4m_mag","rhs_mine_a200_bz_mag","rhs_mine_a200_dz35_mag","rhs_mine_tm43_mag"
            "rhs_mine_m2a3b_press_mag","rhs_mine_m2a3b_trip_mag","rhs_mine_m3_pressure_mag","rhs_mine_mk2_pressure_mag"
            "rhs_mine_m3_tripwire_mag","rhs_mine_mk2_tripwire_mag","rhs_mine_m7a2_mag","rhs_charge_m2tet_x2_mag"
            "rhssaf_mine_pma3_mag","rhssaf_mine_tma4_mag","rhssaf_mine_mrud_a_mag","rhssaf_mine_mrud_b_mag"
            "rhssaf_mine_mrud_c_mag","rhssaf_mine_mrud_d_mag","rhssaf_tm100_mag","rhssaf_tm200_mag"
            "rhssaf_tm500_mag",],
        "sound": ["",0.000316228,1],
        "reloadsound": ["",0.000316228,1],
        "enableattack": 0,
        "optics": 0,
        "showempty": 0,
        "canlock": 0,
        "primary": 10,
        "minrange": 0,
        "minrangeprobab": 0.1,
        "midrange": 3,
        "midrangeprobab": 0.9,
        "maxrange": 15,
        "maxrangeprobab": 0.04,
        "movetointernal": 0,
        "opticszoommin": 0.25,
        "opticszoommax": 1.25,
        "opticszoominit": 0.75,
        "access": 3,
        "scope": 0,
        "value": 2,
        "picture": "",
        "uipicture": "",
        "ammo": "",
        "cursor": "",
        "cursoraim": "",
        "cursorsize": 1,
        "showaimcursorinternal": 1,
        "cursoraimon": "",
        "laser": 0,
        "hiddenselections": [],
        "hiddenselectionstextures": [],
        "hiddenunderwaterselections": [],
        "shownunderwaterselections": [],
        "hiddenunderwaterselectionstextures": [],
        "simulation": "Weapon",
        "type": 65536,
        "displayname": "",
        "namesound": "",
        "count": 0,
        "multiplier": 1,
        "burst": 1,
        "magazinereloadtime": 0,
        "reloadtime": 1,
        "magazinereloadswitchphase": 1,
        "soundbegin": ["sound",1],
        "soundbeginwater": ["sound",1],
        "soundclosure": ["sound",1],
        "soundend": ["sound",1],
        "soundloop": ["sound",1],
        "soundcontinuous": 0,
        "weaponsoundeffect": "",
        "soundburst": 1,
        "drysound": ["",1,1],
        "zeroingsound": ["",1,1],
        "changefiremodesound": ["",1,1],
        "reloadmagazinesound": ["",1,1],
        "emptysound": ["",1,1],
        "soundbullet": ["emptySound",1],
        "initspeed": 0,
        "ballisticscomputer": 0,
        "irdistance": 0,
        "irdotintensity": 0.001,
        "dispersion": 0.002,
        "aidispersioncoefx": 1,
        "aidispersioncoefy": 1,
        "lockacquire": 1,
        "ffmagnitude": 0,
        "fffrequency": 1,
        "ffcount": 1,
        # Recoil Array: recoil,
        "recoil": [],
        "recoil": "empty",
        "recoilprone": "",
        "maxrecoilsway": 0.008,
        "swaydecayspeed": 2,
        "model": "",
        "modelspecial": "",
        "modelmagazine": "",
        "muzzlepos": "usti hlavne",
        "muzzleend": "konec hlavne",
        "irlaserpos": "laser pos",
        "irlaserend": "laser dir",
        "cartridgepos": "nabojnicestart",
        "cartridgevel": "nabojniceend",
        "selectionfireanim": "zasleh",
        "memorypointcamera": "eye",
        "firespreadangle": 3,
        "usemodeloptics": 1,
        "opticsid": 0,
        "modeloptics": "",
        "opticsppeffects": [],
        "opticsflare": 1,
        "forceoptics": 0,
        "useasbinocular": 0,
        "opticsdisableperipherialvision": 0.67,
        "distancezoommin": 400,
        "distancezoommax": 400,
        "showswitchaction": 0,
        "autofire": 0,
        "autoreload": 1,
        "showtoplayer": 1,
        "canshootinwater": 0,
        "airateoffire": 5,
        "airateoffiredistance": 500,
        "airateoffiredispersion": 0,
        "firelightduration": 0.05,
        "firelightintensity": 0.2,
        "firelightdiffuse": [0.937,0.631,0.259],
        "firelightambient": [0,0,0],
        # Class: CfgWeapons|Default|Eventhandlers [Indent level: 1],
        "eventhandlers": {
        },
        "backgroundreload": 0,
        "reloadaction": "",
        "muzzles": ["this"],
        "modes": ["this"],
        "useaction": 0,
        "useactiontitle": "",
        "candrop": 1,
        "weaponlockdelay": 0,
        "weaponlocksystem": 0,
        "cmimmunity": 1,
        "weight": 0,
        "handanim": [],
        "lockingtargetsound": ["",0.000316228,2],
        "lockedtargetsound": ["",0.000316228,6],
        "detectrange": 0,
        "artillerydispersion": 1,
        "artillerycharge": 1,
        "fireanims": [],
        # Class: CfgWeapons|Default|Library [Indent level: 1],
        "library": {
            "libtextdesc": ""
        },
        "descriptionshort": "",
        # Class: CfgWeapons|Default|GunFire [Indent level: 1],
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
            "cloudletdensitycoef": -1,
            "interval": -0.01,
            "size": 3,
            "sourcesize": 0.5,
            "timetolive": 0,
            "initt": 4500,
            "deltat": -3000,
            # Class: CfgWeapons|Default|GunFire|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunFire|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [0.82,0.95,0.93,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T1 [Indent level: 3],
                "t1": {
                    "maxt": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T2 [Indent level: 3],
                "t2": {
                    "maxt": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T3 [Indent level: 3],
                "t3": {
                    "maxt": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T4 [Indent level: 3],
                "t4": {
                    "maxt": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T5 [Indent level: 3],
                "t5": {
                    "maxt": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T6 [Indent level: 3],
                "t6": {
                    "maxt": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T7 [Indent level: 3],
                "t7": {
                    "maxt": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T8 [Indent level: 3],
                "t8": {
                    "maxt": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T9 [Indent level: 3],
                "t9": {
                    "maxt": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T10 [Indent level: 3],
                "t10": {
                    "maxt": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T11 [Indent level: 3],
                "t11": {
                    "maxt": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T12 [Indent level: 3],
                "t12": {
                    "maxt": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T13 [Indent level: 3],
                "t13": {
                    "maxt": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T14 [Indent level: 3],
                "t14": {
                    "maxt": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T15 [Indent level: 3],
                "t15": {
                    "maxt": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T16 [Indent level: 3],
                "t16": {
                    "maxt": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T17 [Indent level: 3],
                "t17": {
                    "maxt": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T18 [Indent level: 3],
                "t18": {
                    "maxt": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T19 [Indent level: 3],
                "t19": {
                    "maxt": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T20 [Indent level: 3],
                "t20": {
                    "maxt": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T21 [Indent level: 3],
                "t21": {
                    "maxt": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T22 [Indent level: 3],
                "t22": {
                    "maxt": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgWeapons|Default|GunClouds [Indent level: 1],
        "gunclouds": {
            "access": 0,
            "cloudletgrowup": 0.05,
            "cloudletfadein": 0,
            "cloudletfadeout": 0.1,
            "cloudletduration": 0.05,
            "cloudletalpha": 0.3,
            "cloudletaccy": 0,
            "cloudletminyspeed": -100,
            "cloudletmaxyspeed": 100,
            "interval": -0.02,
            "size": 0.3,
            "sourcesize": 0.02,
            "cloudletanimperiod": 1,
            "cloudletsize": 1,
            "cloudletshape": "cloudletClouds",
            "cloudletcolor": [1,1,1,0],
            "timetolive": 0,
            "initt": 0,
            "deltat": 0,
            # Class: CfgWeapons|Default|GunClouds|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunClouds|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        "texturetype": "default",
        "inertia": 0.5,
        "aimtransitionspeed": 1
    },
    # Class: CfgWeapons|Put|rhssaf_tm100_muzzle [Indent level: 1],
    "rhssaf_tm100_muzzle": {
        "autoreload": 0,
        "displayname": "TM-100 charge",
        # Compatible Magazines: magazines parameter (+ inherited),
        "magazines": [
            "democharge_remote_mag","iedurbansmall_remote_mag","iedlandsmall_remote_mag","satchelcharge_remote_mag",
            "iedurbanbig_remote_mag","iedlandbig_remote_mag","atmine_range_mag","claymoredirectionalmine_remote_mag",
            "apersmine_range_mag","apersboundingmine_range_mag","slamdirectionalmine_wire_mag","aperstripmine_wire_mag",
            "apersminedispenser_mag","trainingmine_mag","rhs_mine_pmn2_mag","rhs_mine_tm62m_mag",
            "rhs_mine_msk40p_white_mag","rhs_mine_msk40p_red_mag","rhs_mine_msk40p_green_mag","rhs_mine_msk40p_blue_mag",
            "rhs_mine_sm320_white_mag","rhs_mine_sm320_red_mag","rhs_mine_sm320_green_mag","rhs_mine_ozm72_a_mag",
            "rhs_mine_ozm72_b_mag","rhs_mine_ozm72_c_mag","rhs_ec75_mag","rhs_ec200_mag",
            "rhs_ec400_mag","rhs_ec75_sand_mag","rhs_ec200_sand_mag","rhs_ec400_sand_mag",
            "rhs_mine_m19_mag","rhsusf_mine_m14_mag","rhsusf_mine_m49a1_3m_mag","rhsusf_mine_m49a1_6m_mag",
            "rhsusf_mine_m49a1_10m_mag","rhsusf_m112_mag","rhsusf_m112x4_mag","rhs_mag_mine_pfm1",
            "rhs_mag_mine_ptm1","rhs_mine_smine35_press_mag","rhs_mine_smine35_trip_mag","rhs_mine_smine44_press_mag",
            "rhs_mine_smine44_trip_mag","rhs_mine_glasmine43_hz_mag","rhs_mine_glasmine43_bz_mag","rhs_mine_stockmine43_2m_mag",
            "rhs_mine_stockmine43_4m_mag","rhs_mine_a200_bz_mag","rhs_mine_a200_dz35_mag","rhs_mine_tm43_mag",
            "rhs_mine_m2a3b_press_mag","rhs_mine_m2a3b_trip_mag","rhs_mine_m3_pressure_mag","rhs_mine_mk2_pressure_mag",
            "rhs_mine_m3_tripwire_mag","rhs_mine_mk2_tripwire_mag","rhs_mine_m7a2_mag","rhs_charge_m2tet_x2_mag",
            "rhssaf_mine_pma3_mag","rhssaf_mine_tma4_mag","rhssaf_mine_mrud_a_mag","rhssaf_mine_mrud_b_mag",
            "rhssaf_mine_mrud_c_mag","rhssaf_mine_mrud_d_mag","rhssaf_tm100_mag","rhssaf_tm200_mag",
            "rhssaf_tm500_mag",],
        "enableattack": 1,
        "showtoplayer": 0,
        "sound": ["",0.000316228,1],
        "reloadsound": ["",0.000316228,1],
        "optics": 0,
        "showempty": 0,
        "canlock": 0,
        "primary": 10,
        "minrange": 0,
        "minrangeprobab": 0.1,
        "midrange": 3,
        "midrangeprobab": 0.9,
        "maxrange": 15,
        "maxrangeprobab": 0.04,
        "movetointernal": 0,
        "opticszoommin": 0.25,
        "opticszoommax": 1.25,
        "opticszoominit": 0.75,
        "access": 3,
        "scope": 0,
        "value": 2,
        "picture": "",
        "uipicture": "",
        "ammo": "",
        "cursor": "",
        "cursoraim": "",
        "cursorsize": 1,
        "showaimcursorinternal": 1,
        "cursoraimon": "",
        "laser": 0,
        "hiddenselections": [],
        "hiddenselectionstextures": [],
        "hiddenunderwaterselections": [],
        "shownunderwaterselections": [],
        "hiddenunderwaterselectionstextures": [],
        "simulation": "Weapon",
        "type": 65536,
        "namesound": "",
        "count": 0,
        "multiplier": 1,
        "burst": 1,
        "magazinereloadtime": 0,
        "reloadtime": 1,
        "magazinereloadswitchphase": 1,
        "soundbegin": ["sound",1],
        "soundbeginwater": ["sound",1],
        "soundclosure": ["sound",1],
        "soundend": ["sound",1],
        "soundloop": ["sound",1],
        "soundcontinuous": 0,
        "weaponsoundeffect": "",
        "soundburst": 1,
        "drysound": ["",1,1],
        "zeroingsound": ["",1,1],
        "changefiremodesound": ["",1,1],
        "reloadmagazinesound": ["",1,1],
        "emptysound": ["",1,1],
        "soundbullet": ["emptySound",1],
        "initspeed": 0,
        "ballisticscomputer": 0,
        "irdistance": 0,
        "irdotintensity": 0.001,
        "dispersion": 0.002,
        "aidispersioncoefx": 1,
        "aidispersioncoefy": 1,
        "lockacquire": 1,
        "ffmagnitude": 0,
        "fffrequency": 1,
        "ffcount": 1,
        # Recoil Array: recoil,
        "recoil": [],
        "recoil": "empty",
        "recoilprone": "",
        "maxrecoilsway": 0.008,
        "swaydecayspeed": 2,
        "model": "",
        "modelspecial": "",
        "modelmagazine": "",
        "muzzlepos": "usti hlavne",
        "muzzleend": "konec hlavne",
        "irlaserpos": "laser pos",
        "irlaserend": "laser dir",
        "cartridgepos": "nabojnicestart",
        "cartridgevel": "nabojniceend",
        "selectionfireanim": "zasleh",
        "memorypointcamera": "eye",
        "firespreadangle": 3,
        "usemodeloptics": 1,
        "opticsid": 0,
        "modeloptics": "",
        "opticsppeffects": [],
        "opticsflare": 1,
        "forceoptics": 0,
        "useasbinocular": 0,
        "opticsdisableperipherialvision": 0.67,
        "distancezoommin": 400,
        "distancezoommax": 400,
        "showswitchaction": 0,
        "autofire": 0,
        "canshootinwater": 0,
        "airateoffire": 5,
        "airateoffiredistance": 500,
        "airateoffiredispersion": 0,
        "firelightduration": 0.05,
        "firelightintensity": 0.2,
        "firelightdiffuse": [0.937,0.631,0.259],
        "firelightambient": [0,0,0],
        # Class: CfgWeapons|Default|Eventhandlers [Indent level: 1],
        "eventhandlers": {
        },
        "backgroundreload": 0,
        "reloadaction": "",
        "muzzles": ["this"],
        "modes": ["this"],
        "useaction": 0,
        "useactiontitle": "",
        "candrop": 1,
        "weaponlockdelay": 0,
        "weaponlocksystem": 0,
        "cmimmunity": 1,
        "weight": 0,
        "handanim": [],
        "lockingtargetsound": ["",0.000316228,2],
        "lockedtargetsound": ["",0.000316228,6],
        "detectrange": 0,
        "artillerydispersion": 1,
        "artillerycharge": 1,
        "fireanims": [],
        # Class: CfgWeapons|Default|Library [Indent level: 1],
        "library": {
            "libtextdesc": ""
        },
        "descriptionshort": "",
        # Class: CfgWeapons|Default|GunFire [Indent level: 1],
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
            "cloudletdensitycoef": -1,
            "interval": -0.01,
            "size": 3,
            "sourcesize": 0.5,
            "timetolive": 0,
            "initt": 4500,
            "deltat": -3000,
            # Class: CfgWeapons|Default|GunFire|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunFire|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [0.82,0.95,0.93,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T1 [Indent level: 3],
                "t1": {
                    "maxt": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T2 [Indent level: 3],
                "t2": {
                    "maxt": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T3 [Indent level: 3],
                "t3": {
                    "maxt": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T4 [Indent level: 3],
                "t4": {
                    "maxt": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T5 [Indent level: 3],
                "t5": {
                    "maxt": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T6 [Indent level: 3],
                "t6": {
                    "maxt": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T7 [Indent level: 3],
                "t7": {
                    "maxt": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T8 [Indent level: 3],
                "t8": {
                    "maxt": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T9 [Indent level: 3],
                "t9": {
                    "maxt": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T10 [Indent level: 3],
                "t10": {
                    "maxt": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T11 [Indent level: 3],
                "t11": {
                    "maxt": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T12 [Indent level: 3],
                "t12": {
                    "maxt": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T13 [Indent level: 3],
                "t13": {
                    "maxt": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T14 [Indent level: 3],
                "t14": {
                    "maxt": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T15 [Indent level: 3],
                "t15": {
                    "maxt": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T16 [Indent level: 3],
                "t16": {
                    "maxt": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T17 [Indent level: 3],
                "t17": {
                    "maxt": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T18 [Indent level: 3],
                "t18": {
                    "maxt": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T19 [Indent level: 3],
                "t19": {
                    "maxt": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T20 [Indent level: 3],
                "t20": {
                    "maxt": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T21 [Indent level: 3],
                "t21": {
                    "maxt": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T22 [Indent level: 3],
                "t22": {
                    "maxt": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgWeapons|Default|GunClouds [Indent level: 1],
        "gunclouds": {
            "access": 0,
            "cloudletgrowup": 0.05,
            "cloudletfadein": 0,
            "cloudletfadeout": 0.1,
            "cloudletduration": 0.05,
            "cloudletalpha": 0.3,
            "cloudletaccy": 0,
            "cloudletminyspeed": -100,
            "cloudletmaxyspeed": 100,
            "interval": -0.02,
            "size": 0.3,
            "sourcesize": 0.02,
            "cloudletanimperiod": 1,
            "cloudletsize": 1,
            "cloudletshape": "cloudletClouds",
            "cloudletcolor": [1,1,1,0],
            "timetolive": 0,
            "initt": 0,
            "deltat": 0,
            # Class: CfgWeapons|Default|GunClouds|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunClouds|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        "texturetype": "default",
        "inertia": 0.5,
        "aimtransitionspeed": 1
    },
    # Class: CfgWeapons|Put|rhssaf_tm200_muzzle [Indent level: 1],
    "rhssaf_tm200_muzzle": {
        "autoreload": 0,
        "displayname": "TM-200 charge",
        # Compatible Magazines: magazines parameter (+ inherited),
        "magazines": [
            "democharge_remote_mag","iedurbansmall_remote_mag","iedlandsmall_remote_mag","satchelcharge_remote_mag",
            "iedurbanbig_remote_mag","iedlandbig_remote_mag","atmine_range_mag","claymoredirectionalmine_remote_mag",
            "apersmine_range_mag","apersboundingmine_range_mag","slamdirectionalmine_wire_mag","aperstripmine_wire_mag",
            "apersminedispenser_mag","trainingmine_mag","rhs_mine_pmn2_mag","rhs_mine_tm62m_mag",
            "rhs_mine_msk40p_white_mag","rhs_mine_msk40p_red_mag","rhs_mine_msk40p_green_mag","rhs_mine_msk40p_blue_mag",
            "rhs_mine_sm320_white_mag","rhs_mine_sm320_red_mag","rhs_mine_sm320_green_mag","rhs_mine_ozm72_a_mag",
            "rhs_mine_ozm72_b_mag","rhs_mine_ozm72_c_mag","rhs_ec75_mag","rhs_ec200_mag",
            "rhs_ec400_mag","rhs_ec75_sand_mag","rhs_ec200_sand_mag","rhs_ec400_sand_mag",
            "rhs_mine_m19_mag","rhsusf_mine_m14_mag","rhsusf_mine_m49a1_3m_mag","rhsusf_mine_m49a1_6m_mag",
            "rhsusf_mine_m49a1_10m_mag","rhsusf_m112_mag","rhsusf_m112x4_mag","rhs_mag_mine_pfm1",
            "rhs_mag_mine_ptm1","rhs_mine_smine35_press_mag","rhs_mine_smine35_trip_mag","rhs_mine_smine44_press_mag",
            "rhs_mine_smine44_trip_mag","rhs_mine_glasmine43_hz_mag","rhs_mine_glasmine43_bz_mag","rhs_mine_stockmine43_2m_mag",
            "rhs_mine_stockmine43_4m_mag","rhs_mine_a200_bz_mag","rhs_mine_a200_dz35_mag","rhs_mine_tm43_mag",
            "rhs_mine_m2a3b_press_mag","rhs_mine_m2a3b_trip_mag","rhs_mine_m3_pressure_mag","rhs_mine_mk2_pressure_mag",
            "rhs_mine_m3_tripwire_mag","rhs_mine_mk2_tripwire_mag","rhs_mine_m7a2_mag","rhs_charge_m2tet_x2_mag",
            "rhssaf_mine_pma3_mag","rhssaf_mine_tma4_mag","rhssaf_mine_mrud_a_mag","rhssaf_mine_mrud_b_mag",
            "rhssaf_mine_mrud_c_mag","rhssaf_mine_mrud_d_mag","rhssaf_tm100_mag","rhssaf_tm200_mag",
            "rhssaf_tm500_mag",],
        "enableattack": 1,
        "showtoplayer": 0,
        "sound": ["",0.000316228,1],
        "reloadsound": ["",0.000316228,1],
        "optics": 0,
        "showempty": 0,
        "canlock": 0,
        "primary": 10,
        "minrange": 0,
        "minrangeprobab": 0.1,
        "midrange": 3,
        "midrangeprobab": 0.9,
        "maxrange": 15,
        "maxrangeprobab": 0.04,
        "movetointernal": 0,
        "opticszoommin": 0.25,
        "opticszoommax": 1.25,
        "opticszoominit": 0.75,
        "access": 3,
        "scope": 0,
        "value": 2,
        "picture": "",
        "uipicture": "",
        "ammo": "",
        "cursor": "",
        "cursoraim": "",
        "cursorsize": 1,
        "showaimcursorinternal": 1,
        "cursoraimon": "",
        "laser": 0,
        "hiddenselections": [],
        "hiddenselectionstextures": [],
        "hiddenunderwaterselections": [],
        "shownunderwaterselections": [],
        "hiddenunderwaterselectionstextures": [],
        "simulation": "Weapon",
        "type": 65536,
        "namesound": "",
        "count": 0,
        "multiplier": 1,
        "burst": 1,
        "magazinereloadtime": 0,
        "reloadtime": 1,
        "magazinereloadswitchphase": 1,
        "soundbegin": ["sound",1],
        "soundbeginwater": ["sound",1],
        "soundclosure": ["sound",1],
        "soundend": ["sound",1],
        "soundloop": ["sound",1],
        "soundcontinuous": 0,
        "weaponsoundeffect": "",
        "soundburst": 1,
        "drysound": ["",1,1],
        "zeroingsound": ["",1,1],
        "changefiremodesound": ["",1,1],
        "reloadmagazinesound": ["",1,1],
        "emptysound": ["",1,1],
        "soundbullet": ["emptySound",1],
        "initspeed": 0,
        "ballisticscomputer": 0,
        "irdistance": 0,
        "irdotintensity": 0.001,
        "dispersion": 0.002,
        "aidispersioncoefx": 1,
        "aidispersioncoefy": 1,
        "lockacquire": 1,
        "ffmagnitude": 0,
        "fffrequency": 1,
        "ffcount": 1,
        # Recoil Array: recoil,
        "recoil": [],
        "recoil": "empty",
        "recoilprone": "",
        "maxrecoilsway": 0.008,
        "swaydecayspeed": 2,
        "model": "",
        "modelspecial": "",
        "modelmagazine": "",
        "muzzlepos": "usti hlavne",
        "muzzleend": "konec hlavne",
        "irlaserpos": "laser pos",
        "irlaserend": "laser dir",
        "cartridgepos": "nabojnicestart",
        "cartridgevel": "nabojniceend",
        "selectionfireanim": "zasleh",
        "memorypointcamera": "eye",
        "firespreadangle": 3,
        "usemodeloptics": 1,
        "opticsid": 0,
        "modeloptics": "",
        "opticsppeffects": [],
        "opticsflare": 1,
        "forceoptics": 0,
        "useasbinocular": 0,
        "opticsdisableperipherialvision": 0.67,
        "distancezoommin": 400,
        "distancezoommax": 400,
        "showswitchaction": 0,
        "autofire": 0,
        "canshootinwater": 0,
        "airateoffire": 5,
        "airateoffiredistance": 500,
        "airateoffiredispersion": 0,
        "firelightduration": 0.05,
        "firelightintensity": 0.2,
        "firelightdiffuse": [0.937,0.631,0.259],
        "firelightambient": [0,0,0],
        # Class: CfgWeapons|Default|Eventhandlers [Indent level: 1],
        "eventhandlers": {
        },
        "backgroundreload": 0,
        "reloadaction": "",
        "muzzles": ["this"],
        "modes": ["this"],
        "useaction": 0,
        "useactiontitle": "",
        "candrop": 1,
        "weaponlockdelay": 0,
        "weaponlocksystem": 0,
        "cmimmunity": 1,
        "weight": 0,
        "handanim": [],
        "lockingtargetsound": ["",0.000316228,2],
        "lockedtargetsound": ["",0.000316228,6],
        "detectrange": 0,
        "artillerydispersion": 1,
        "artillerycharge": 1,
        "fireanims": [],
        # Class: CfgWeapons|Default|Library [Indent level: 1],
        "library": {
            "libtextdesc": ""
        },
        "descriptionshort": "",
        # Class: CfgWeapons|Default|GunFire [Indent level: 1],
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
            "cloudletdensitycoef": -1,
            "interval": -0.01,
            "size": 3,
            "sourcesize": 0.5,
            "timetolive": 0,
            "initt": 4500,
            "deltat": -3000,
            # Class: CfgWeapons|Default|GunFire|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunFire|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [0.82,0.95,0.93,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T1 [Indent level: 3],
                "t1": {
                    "maxt": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T2 [Indent level: 3],
                "t2": {
                    "maxt": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T3 [Indent level: 3],
                "t3": {
                    "maxt": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T4 [Indent level: 3],
                "t4": {
                    "maxt": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T5 [Indent level: 3],
                "t5": {
                    "maxt": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T6 [Indent level: 3],
                "t6": {
                    "maxt": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T7 [Indent level: 3],
                "t7": {
                    "maxt": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T8 [Indent level: 3],
                "t8": {
                    "maxt": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T9 [Indent level: 3],
                "t9": {
                    "maxt": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T10 [Indent level: 3],
                "t10": {
                    "maxt": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T11 [Indent level: 3],
                "t11": {
                    "maxt": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T12 [Indent level: 3],
                "t12": {
                    "maxt": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T13 [Indent level: 3],
                "t13": {
                    "maxt": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T14 [Indent level: 3],
                "t14": {
                    "maxt": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T15 [Indent level: 3],
                "t15": {
                    "maxt": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T16 [Indent level: 3],
                "t16": {
                    "maxt": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T17 [Indent level: 3],
                "t17": {
                    "maxt": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T18 [Indent level: 3],
                "t18": {
                    "maxt": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T19 [Indent level: 3],
                "t19": {
                    "maxt": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T20 [Indent level: 3],
                "t20": {
                    "maxt": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T21 [Indent level: 3],
                "t21": {
                    "maxt": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T22 [Indent level: 3],
                "t22": {
                    "maxt": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgWeapons|Default|GunClouds [Indent level: 1],
        "gunclouds": {
            "access": 0,
            "cloudletgrowup": 0.05,
            "cloudletfadein": 0,
            "cloudletfadeout": 0.1,
            "cloudletduration": 0.05,
            "cloudletalpha": 0.3,
            "cloudletaccy": 0,
            "cloudletminyspeed": -100,
            "cloudletmaxyspeed": 100,
            "interval": -0.02,
            "size": 0.3,
            "sourcesize": 0.02,
            "cloudletanimperiod": 1,
            "cloudletsize": 1,
            "cloudletshape": "cloudletClouds",
            "cloudletcolor": [1,1,1,0],
            "timetolive": 0,
            "initt": 0,
            "deltat": 0,
            # Class: CfgWeapons|Default|GunClouds|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunClouds|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        "texturetype": "default",
        "inertia": 0.5,
        "aimtransitionspeed": 1
    },
    # Class: CfgWeapons|Put|rhssaf_tm500_muzzle [Indent level: 1],
    "rhssaf_tm500_muzzle": {
        "autoreload": 0,
        "displayname": "TM-500 charge",
        # Compatible Magazines: magazines parameter (+ inherited),
        "magazines": [
            "democharge_remote_mag","iedurbansmall_remote_mag","iedlandsmall_remote_mag","satchelcharge_remote_mag",
            "iedurbanbig_remote_mag","iedlandbig_remote_mag","atmine_range_mag","claymoredirectionalmine_remote_mag",
            "apersmine_range_mag","apersboundingmine_range_mag","slamdirectionalmine_wire_mag","aperstripmine_wire_mag",
            "apersminedispenser_mag","trainingmine_mag","rhs_mine_pmn2_mag","rhs_mine_tm62m_mag",
            "rhs_mine_msk40p_white_mag","rhs_mine_msk40p_red_mag","rhs_mine_msk40p_green_mag","rhs_mine_msk40p_blue_mag",
            "rhs_mine_sm320_white_mag","rhs_mine_sm320_red_mag","rhs_mine_sm320_green_mag","rhs_mine_ozm72_a_mag",
            "rhs_mine_ozm72_b_mag","rhs_mine_ozm72_c_mag","rhs_ec75_mag","rhs_ec200_mag",
            "rhs_ec400_mag","rhs_ec75_sand_mag","rhs_ec200_sand_mag","rhs_ec400_sand_mag",
            "rhs_mine_m19_mag","rhsusf_mine_m14_mag","rhsusf_mine_m49a1_3m_mag","rhsusf_mine_m49a1_6m_mag",
            "rhsusf_mine_m49a1_10m_mag","rhsusf_m112_mag","rhsusf_m112x4_mag","rhs_mag_mine_pfm1",
            "rhs_mag_mine_ptm1","rhs_mine_smine35_press_mag","rhs_mine_smine35_trip_mag","rhs_mine_smine44_press_mag",
            "rhs_mine_smine44_trip_mag","rhs_mine_glasmine43_hz_mag","rhs_mine_glasmine43_bz_mag","rhs_mine_stockmine43_2m_mag",
            "rhs_mine_stockmine43_4m_mag","rhs_mine_a200_bz_mag","rhs_mine_a200_dz35_mag","rhs_mine_tm43_mag",
            "rhs_mine_m2a3b_press_mag","rhs_mine_m2a3b_trip_mag","rhs_mine_m3_pressure_mag","rhs_mine_mk2_pressure_mag",
            "rhs_mine_m3_tripwire_mag","rhs_mine_mk2_tripwire_mag","rhs_mine_m7a2_mag","rhs_charge_m2tet_x2_mag",
            "rhssaf_mine_pma3_mag","rhssaf_mine_tma4_mag","rhssaf_mine_mrud_a_mag","rhssaf_mine_mrud_b_mag",
            "rhssaf_mine_mrud_c_mag","rhssaf_mine_mrud_d_mag","rhssaf_tm100_mag","rhssaf_tm200_mag",
            "rhssaf_tm500_mag",],
        "enableattack": 1,
        "showtoplayer": 0,
        "sound": ["",0.000316228,1],
        "reloadsound": ["",0.000316228,1],
        "optics": 0,
        "showempty": 0,
        "canlock": 0,
        "primary": 10,
        "minrange": 0,
        "minrangeprobab": 0.1,
        "midrange": 3,
        "midrangeprobab": 0.9,
        "maxrange": 15,
        "maxrangeprobab": 0.04,
        "movetointernal": 0,
        "opticszoommin": 0.25,
        "opticszoommax": 1.25,
        "opticszoominit": 0.75,
        "access": 3,
        "scope": 0,
        "value": 2,
        "picture": "",
        "uipicture": "",
        "ammo": "",
        "cursor": "",
        "cursoraim": "",
        "cursorsize": 1,
        "showaimcursorinternal": 1,
        "cursoraimon": "",
        "laser": 0,
        "hiddenselections": [],
        "hiddenselectionstextures": [],
        "hiddenunderwaterselections": [],
        "shownunderwaterselections": [],
        "hiddenunderwaterselectionstextures": [],
        "simulation": "Weapon",
        "type": 65536,
        "namesound": "",
        "count": 0,
        "multiplier": 1,
        "burst": 1,
        "magazinereloadtime": 0,
        "reloadtime": 1,
        "magazinereloadswitchphase": 1,
        "soundbegin": ["sound",1],
        "soundbeginwater": ["sound",1],
        "soundclosure": ["sound",1],
        "soundend": ["sound",1],
        "soundloop": ["sound",1],
        "soundcontinuous": 0,
        "weaponsoundeffect": "",
        "soundburst": 1,
        "drysound": ["",1,1],
        "zeroingsound": ["",1,1],
        "changefiremodesound": ["",1,1],
        "reloadmagazinesound": ["",1,1],
        "emptysound": ["",1,1],
        "soundbullet": ["emptySound",1],
        "initspeed": 0,
        "ballisticscomputer": 0,
        "irdistance": 0,
        "irdotintensity": 0.001,
        "dispersion": 0.002,
        "aidispersioncoefx": 1,
        "aidispersioncoefy": 1,
        "lockacquire": 1,
        "ffmagnitude": 0,
        "fffrequency": 1,
        "ffcount": 1,
        # Recoil Array: recoil,
        "recoil": [],
        "recoil": "empty",
        "recoilprone": "",
        "maxrecoilsway": 0.008,
        "swaydecayspeed": 2,
        "model": "",
        "modelspecial": "",
        "modelmagazine": "",
        "muzzlepos": "usti hlavne",
        "muzzleend": "konec hlavne",
        "irlaserpos": "laser pos",
        "irlaserend": "laser dir",
        "cartridgepos": "nabojnicestart",
        "cartridgevel": "nabojniceend",
        "selectionfireanim": "zasleh",
        "memorypointcamera": "eye",
        "firespreadangle": 3,
        "usemodeloptics": 1,
        "opticsid": 0,
        "modeloptics": "",
        "opticsppeffects": [],
        "opticsflare": 1,
        "forceoptics": 0,
        "useasbinocular": 0,
        "opticsdisableperipherialvision": 0.67,
        "distancezoommin": 400,
        "distancezoommax": 400,
        "showswitchaction": 0,
        "autofire": 0,
        "canshootinwater": 0,
        "airateoffire": 5,
        "airateoffiredistance": 500,
        "airateoffiredispersion": 0,
        "firelightduration": 0.05,
        "firelightintensity": 0.2,
        "firelightdiffuse": [0.937,0.631,0.259],
        "firelightambient": [0,0,0],
        # Class: CfgWeapons|Default|Eventhandlers [Indent level: 1],
        "eventhandlers": {
        },
        "backgroundreload": 0,
        "reloadaction": "",
        "muzzles": ["this"],
        "modes": ["this"],
        "useaction": 0,
        "useactiontitle": "",
        "candrop": 1,
        "weaponlockdelay": 0,
        "weaponlocksystem": 0,
        "cmimmunity": 1,
        "weight": 0,
        "handanim": [],
        "lockingtargetsound": ["",0.000316228,2],
        "lockedtargetsound": ["",0.000316228,6],
        "detectrange": 0,
        "artillerydispersion": 1,
        "artillerycharge": 1,
        "fireanims": [],
        # Class: CfgWeapons|Default|Library [Indent level: 1],
        "library": {
            "libtextdesc": ""
        },
        "descriptionshort": "",
        # Class: CfgWeapons|Default|GunFire [Indent level: 1],
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
            "cloudletdensitycoef": -1,
            "interval": -0.01,
            "size": 3,
            "sourcesize": 0.5,
            "timetolive": 0,
            "initt": 4500,
            "deltat": -3000,
            # Class: CfgWeapons|Default|GunFire|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunFire|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [0.82,0.95,0.93,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T1 [Indent level: 3],
                "t1": {
                    "maxt": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T2 [Indent level: 3],
                "t2": {
                    "maxt": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T3 [Indent level: 3],
                "t3": {
                    "maxt": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T4 [Indent level: 3],
                "t4": {
                    "maxt": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T5 [Indent level: 3],
                "t5": {
                    "maxt": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T6 [Indent level: 3],
                "t6": {
                    "maxt": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T7 [Indent level: 3],
                "t7": {
                    "maxt": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T8 [Indent level: 3],
                "t8": {
                    "maxt": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T9 [Indent level: 3],
                "t9": {
                    "maxt": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T10 [Indent level: 3],
                "t10": {
                    "maxt": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T11 [Indent level: 3],
                "t11": {
                    "maxt": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T12 [Indent level: 3],
                "t12": {
                    "maxt": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T13 [Indent level: 3],
                "t13": {
                    "maxt": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T14 [Indent level: 3],
                "t14": {
                    "maxt": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T15 [Indent level: 3],
                "t15": {
                    "maxt": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T16 [Indent level: 3],
                "t16": {
                    "maxt": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T17 [Indent level: 3],
                "t17": {
                    "maxt": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T18 [Indent level: 3],
                "t18": {
                    "maxt": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T19 [Indent level: 3],
                "t19": {
                    "maxt": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T20 [Indent level: 3],
                "t20": {
                    "maxt": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T21 [Indent level: 3],
                "t21": {
                    "maxt": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T22 [Indent level: 3],
                "t22": {
                    "maxt": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgWeapons|Default|GunClouds [Indent level: 1],
        "gunclouds": {
            "access": 0,
            "cloudletgrowup": 0.05,
            "cloudletfadein": 0,
            "cloudletfadeout": 0.1,
            "cloudletduration": 0.05,
            "cloudletalpha": 0.3,
            "cloudletaccy": 0,
            "cloudletminyspeed": -100,
            "cloudletmaxyspeed": 100,
            "interval": -0.02,
            "size": 0.3,
            "sourcesize": 0.02,
            "cloudletanimperiod": 1,
            "cloudletsize": 1,
            "cloudletshape": "cloudletClouds",
            "cloudletcolor": [1,1,1,0],
            "timetolive": 0,
            "initt": 0,
            "deltat": 0,
            # Class: CfgWeapons|Default|GunClouds|Table [Indent level: 2],
            "table": {
                # Class: CfgWeapons|Default|GunClouds|Table|T0 [Indent level: 3]
                "t0": {
                    "maxt": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        "texturetype": "default",
        "inertia": 0.5,
        "aimtransitionspeed": 1
    },
    "access": 3,
    "picture": "",
    "uipicture": "",
    "ammo": "",
    "cursor": "",
    "cursoraim": "",
    "cursorsize": 1,
    "showaimcursorinternal": 1,
    "cursoraimon": "",
    "laser": 0,
    "hiddenselections": [],
    "hiddenselectionstextures": [],
    "hiddenunderwaterselections": [],
    "shownunderwaterselections": [],
    "hiddenunderwaterselectionstextures": [],
    "simulation": "Weapon",
    "namesound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazinereloadtime": 0,
    "reloadtime": 1,
    "magazinereloadswitchphase": 1,
    "sound": ["",1,1],
    "soundbegin": ["sound",1],
    "soundbeginwater": ["sound",1],
    "soundclosure": ["sound",1],
    "soundend": ["sound",1],
    "soundloop": ["sound",1],
    "soundcontinuous": 0,
    "weaponsoundeffect": "",
    "soundburst": 1,
    "drysound": ["",1,1],
    "zeroingsound": ["",1,1],
    "reloadsound": ["",1,1],
    "changefiremodesound": ["",1,1],
    "reloadmagazinesound": ["",1,1],
    "emptysound": ["",1,1],
    "soundbullet": ["emptySound",1],
    "initspeed": 0,
    "ballisticscomputer": 0,
    "irdistance": 0,
    "irdotintensity": 0.001,
    "dispersion": 0.002,
    "aidispersioncoefx": 1,
    "aidispersioncoefy": 1,
    "canlock": 2,
    "lockacquire": 1,
    "enableattack": 1,
    "ffmagnitude": 0,
    "fffrequency": 1,
    "ffcount": 1,
    # Recoil Array: recoil,
    "recoil": [],
    "recoil": "empty",
    "recoilprone": "",
    "maxrecoilsway": 0.008,
    "swaydecayspeed": 2,
    "model": "",
    "modelspecial": "",
    "modelmagazine": "",
    "muzzlepos": "usti hlavne",
    "muzzleend": "konec hlavne",
    "irlaserpos": "laser pos",
    "irlaserend": "laser dir",
    "cartridgepos": "nabojnicestart",
    "cartridgevel": "nabojniceend",
    "selectionfireanim": "zasleh",
    "memorypointcamera": "eye",
    "firespreadangle": 3,
    "usemodeloptics": 1,
    "opticsid": 0,
    "modeloptics": "",
    "opticsppeffects": [],
    "opticsflare": 1,
    "optics": 1,
    "forceoptics": 0,
    "useasbinocular": 0,
    "opticsdisableperipherialvision": 0.67,
    "opticszoommin": 0.25,
    "opticszoommax": 1.25,
    "opticszoominit": 0.75,
    "distancezoommin": 400,
    "distancezoommax": 400,
    "primary": 10,
    "showswitchaction": 0,
    "showempty": 1,
    "autofire": 0,
    "autoreload": 1,
    "showtoplayer": 1,
    "canshootinwater": 0,
    "airateoffire": 5,
    "airateoffiredistance": 500,
    "airateoffiredispersion": 0,
    "firelightduration": 0.05,
    "firelightintensity": 0.2,
    "firelightdiffuse": [0.937,0.631,0.259],
    "firelightambient": [0,0,0],
    # Class: CfgWeapons|Default|Eventhandlers [Indent level: 1],
    "eventhandlers": {
    },
    "backgroundreload": 0,
    "reloadaction": "",
    "magazines": [],
    "modes": ["this"],
    "useaction": 0,
    "useactiontitle": "",
    "weaponlockdelay": 0,
    "weaponlocksystem": 0,
    "cmimmunity": 1,
    "weight": 0,
    "minrange": 1,
    "minrangeprobab": 0.3,
    "midrange": 150,
    "midrangeprobab": 0.58,
    "maxrange": 500,
    "maxrangeprobab": 0.04,
    "handanim": [],
    "lockingtargetsound": ["",0.000316228,2],
    "lockedtargetsound": ["",0.000316228,6],
    "detectrange": 0,
    "artillerydispersion": 1,
    "artillerycharge": 1,
    "fireanims": [],
    # Class: CfgWeapons|Default|Library [Indent level: 1],
    "library": {
        "libtextdesc": ""
    },
    "descriptionshort": "",
    # Class: CfgWeapons|Default|GunFire [Indent level: 1],
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
        "cloudletdensitycoef": -1,
        "interval": -0.01,
        "size": 3,
        "sourcesize": 0.5,
        "timetolive": 0,
        "initt": 4500,
        "deltat": -3000,
        # Class: CfgWeapons|Default|GunFire|Table [Indent level: 2],
        "table": {
            # Class: CfgWeapons|Default|GunFire|Table|T0 [Indent level: 3]
            "t0": {
                "maxt": 0,
                "color": [0.82,0.95,0.93,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T1 [Indent level: 3],
            "t1": {
                "maxt": 200,
                "color": [0.75,0.77,0.9,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T2 [Indent level: 3],
            "t2": {
                "maxt": 400,
                "color": [0.56,0.62,0.67,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T3 [Indent level: 3],
            "t3": {
                "maxt": 600,
                "color": [0.39,0.46,0.47,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T4 [Indent level: 3],
            "t4": {
                "maxt": 800,
                "color": [0.24,0.31,0.31,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T5 [Indent level: 3],
            "t5": {
                "maxt": 1000,
                "color": [0.23,0.31,0.29,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T6 [Indent level: 3],
            "t6": {
                "maxt": 1500,
                "color": [0.21,0.29,0.27,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T7 [Indent level: 3],
            "t7": {
                "maxt": 2000,
                "color": [0.19,0.23,0.21,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T8 [Indent level: 3],
            "t8": {
                "maxt": 2300,
                "color": [0.22,0.19,0.1,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T9 [Indent level: 3],
            "t9": {
                "maxt": 2500,
                "color": [0.35,0.2,0.02,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T10 [Indent level: 3],
            "t10": {
                "maxt": 2600,
                "color": [0.62,0.29,0.03,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T11 [Indent level: 3],
            "t11": {
                "maxt": 2650,
                "color": [0.59,0.35,0.05,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T12 [Indent level: 3],
            "t12": {
                "maxt": 2700,
                "color": [0.75,0.37,0.03,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T13 [Indent level: 3],
            "t13": {
                "maxt": 2750,
                "color": [0.88,0.34,0.03,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T14 [Indent level: 3],
            "t14": {
                "maxt": 2800,
                "color": [0.91,0.5,0.17,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T15 [Indent level: 3],
            "t15": {
                "maxt": 2850,
                "color": [1,0.6,0.2,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T16 [Indent level: 3],
            "t16": {
                "maxt": 2900,
                "color": [1,0.71,0.3,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T17 [Indent level: 3],
            "t17": {
                "maxt": 2950,
                "color": [0.98,0.83,0.41,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T18 [Indent level: 3],
            "t18": {
                "maxt": 3000,
                "color": [0.98,0.91,0.54,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T19 [Indent level: 3],
            "t19": {
                "maxt": 3100,
                "color": [0.98,0.99,0.6,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T20 [Indent level: 3],
            "t20": {
                "maxt": 3300,
                "color": [0.96,0.99,0.72,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T21 [Indent level: 3],
            "t21": {
                "maxt": 3600,
                "color": [1,0.98,0.91,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T22 [Indent level: 3],
            "t22": {
                "maxt": 4200,
                "color": [1,1,1,0]
            }
        }
    },
    # Class: CfgWeapons|Default|GunClouds [Indent level: 1],
    "gunclouds": {
        "access": 0,
        "cloudletgrowup": 0.05,
        "cloudletfadein": 0,
        "cloudletfadeout": 0.1,
        "cloudletduration": 0.05,
        "cloudletalpha": 0.3,
        "cloudletaccy": 0,
        "cloudletminyspeed": -100,
        "cloudletmaxyspeed": 100,
        "interval": -0.02,
        "size": 0.3,
        "sourcesize": 0.02,
        "cloudletanimperiod": 1,
        "cloudletsize": 1,
        "cloudletshape": "cloudletClouds",
        "cloudletcolor": [1,1,1,0],
        "timetolive": 0,
        "initt": 0,
        "deltat": 0,
        # Class: CfgWeapons|Default|GunClouds|Table [Indent level: 2],
        "table": {
            # Class: CfgWeapons|Default|GunClouds|Table|T0 [Indent level: 3]
            "t0": {
                "maxt": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "texturetype": "default",
    "inertia": 0.5,
    "aimtransitionspeed": 1,
}