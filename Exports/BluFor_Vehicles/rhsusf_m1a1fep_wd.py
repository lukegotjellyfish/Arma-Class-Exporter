rhsusf_m1a1fep_wd = {
    "editorPreview": "rhsusf|addons|rhsusf_editorPreviews|data|rhsusf_m1a1fep_wd.paa",
    "scope": 2,
    "displayName": "M1A1FEP",
    "faction": "rhs_faction_usmc_wd",
    "vehicleClass": "rhs_vehclass_tank",
    "crew": "rhsusf_usmc_marpat_wd_crewman",
    "rhs_decalParameters": ["['Label', cM1PlnSymPlaces, 'ArmyPlt_Abrams_WD']","['Label', cM1BarrelSymPlaces, 'BarrelArt_Abrams_WD']"],
    "author": "Red Hammer Studios",
    "hiddenSelectionsTextures": ["rhsusf|addons|rhsusf_m1a1|data|rhsusf_m1a1aim_01_co.paa","rhsusf|addons|rhsusf_m1a1|data|rhsusf_m1a1aim_02_co.paa","rhsusf|addons|rhsusf_m1a1|data|rhsusf_m1a1aim_03_co.paa","rhsusf|addons|rhsusf_m1a1|loaderspintle|data|loaderspintle_wd_co.paa","rhsusf|addons|rhsusf_m1a1|duke|data|duke_antennae_wd_co.paa"],
    # Class: CfgVehicles\rhsusf_m1a1fep_wd\AnimationSources,
    "AnimationSources": {
        # Class: CfgVehicles\rhsusf_m1a1fep_wd\AnimationSources\DUKE_Hide
        "DUKE_Hide": {
            "initPhase": 1,
            "displayName": "hide DUKE antennas",
            "author": "Red Hammer Studios",
            "onPhaseChanged": "_this + ([[0,0]]) call rhs_fnc_duke_vg;",
            "source": "user",
            "animPeriod": 1e-005,
            "mass": -20
        },
        # Class: CfgVehicles\rhsusf_m1a1fep_d\AnimationSources\smoke_revolving_source,
        "smoke_revolving_source": {
            "source": "revolving",
            "weapon": "rhsusf_weap_M257"
        },
        # Class: CfgVehicles\rhsusf_m1a1fep_d\AnimationSources\HitDuke1,
        "HitDuke1": {
            "source": "Hit",
            "hitpoint": "HitDuke1"
        },
        # Class: CfgVehicles\rhsusf_m1a1fep_d\AnimationSources\HitDuke2,
        "HitDuke2": {
            "hitpoint": "HitDuke2",
            "source": "Hit"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\AnimationSources\IFF_Panels_Hide,
        "IFF_Panels_Hide": {
            "author": "Red Hammer Studios",
            "source": "user",
            "animPeriod": 1e-005,
            "initPhase": 0,
            "displayName": "hide IFF panels",
            "mass": -20
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\AnimationSources\Miles_Hide,
        "Miles_Hide": {
            "author": "Red Hammer Studios",
            "displayName": "hide MILES panels",
            "source": "user",
            "animPeriod": 1e-005,
            "initPhase": 0,
            "mass": -20
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\AnimationSources\muzzle_rot_CoaxMG,
        "muzzle_rot_CoaxMG": {
            "source": "ammorandom",
            "weapon": "rhs_weap_m240_abrams_coax"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\AnimationSources\muzzle_rot_hmg,
        "muzzle_rot_hmg": {
            "source": "ammorandom",
            "weapon": "RHS_M2_Abrams_Commander"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\AnimationSources\muzzle_rot_cannon,
        "muzzle_rot_cannon": {
            "source": "ammorandom",
            "weapon": "rhs_weap_m256"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\AnimationSources\recoil_source,
        "recoil_source": {
            "source": "reload",
            "weapon": "rhs_weap_m256"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\AnimationSources\muzzle_rot_HMG2,
        "muzzle_rot_HMG2": {
            "source": "ammorandom",
            "weapon": "rhs_weap_m240_abrams"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\AnimationSources\reload1,
        "reload1": {
            "source": "reload",
            "weapon": "rhs_weap_m240_abrams"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\AnimationSources\ReloadMagazine1,
        "ReloadMagazine1": {
            "source": "reloadmagazine",
            "weapon": "rhs_weap_m240_abrams"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\AnimationSources\Revolving1,
        "Revolving1": {
            "source": "revolving",
            "weapon": "rhs_weap_m240_abrams"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\AnimationSources\muzzle_hide_cannon,
        "muzzle_hide_cannon": {
            "source": "reload",
            "weapon": "rhs_weap_m256"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\AnimationSources\elev,
        "elev": {
            "source": "user",
            "animperiod": 0.0016
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\AnimationSources\elev_bank,
        "elev_bank": {
            "source": "user",
            "animperiod": 0.0016
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\AnimationSources\lead,
        "lead": {
            "source": "user",
            "animperiod": 0.001
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\AnimationSources\offset,
        "offset": {
            "source": "user",
            "animperiod": 0.0002
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\AnimationSources\HatchC,
        "HatchC": {
            "source": "door",
            "animPeriod": 2.1
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\AnimationSources\HatchL,
        "HatchL": {
            "source": "door",
            "animPeriod": 2.1
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\AnimationSources\HatchD,
        "HatchD": {
            "source": "door",
            "animPeriod": 2.1
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\AnimationSources\Unhide_vis_optic_d_ComCWSS,
        "Unhide_vis_optic_d_ComCWSS": {
            "source": "hit",
            "hitpoint": "Hit_Optic_ComCWSS"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\AnimationSources\Unhide_vis_optic_d_ComM2,
        "Unhide_vis_optic_d_ComM2": {
            "source": "hit",
            "hitpoint": "Hit_Optic_ComM2"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\AnimationSources\Unhide_vis_optic_d_ComPeriscope,
        "Unhide_vis_optic_d_ComPeriscope": {
            "source": "hit",
            "hitpoint": "Hit_Optic_ComPeriscope"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\AnimationSources\Unhide_vis_optic_d_GPS,
        "Unhide_vis_optic_d_GPS": {
            "source": "hit",
            "hitpoint": "Hit_Optic_GPS"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\AnimationSources\Unhide_vis_optic_d_GPS_TI,
        "Unhide_vis_optic_d_GPS_TI": {
            "source": "hit",
            "hitpoint": "Hit_Optic_GPS_TI"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\AnimationSources\Unhide_vis_optic_d_Driver,
        "Unhide_vis_optic_d_Driver": {
            "source": "hit",
            "hitpoint": "Hit_Optic_Driver"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\AnimationSources\Unhide_vis_optic_d_LoaderPeriscope,
        "Unhide_vis_optic_d_LoaderPeriscope": {
            "source": "hit",
            "hitpoint": "Hit_Optic_LoaderPeriscope"
        }
    },
    # Class: CfgVehicles\rhsusf_m1a1fep_wd\Attributes,
    "Attributes": {
        # Class: CfgVehicles\rhsusf_m1a1fep_wd\Attributes\ObjectTexture
        "ObjectTexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayName": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        # Class: CfgVehicles\rhsusf_m1a1fep_wd\Attributes\rhs_hideIFFPanel,
        "rhs_hideIFFPanel": {
            "displayName": "Hide IFF Panel",
            "property": "rhs_hideIFFPanel",
            "control": "CheckboxNumber",
            "expression": "_this animate ['IFF_Panels_Hide',_value,true]",
            "defaultValue": "0"
        },
        # Class: CfgVehicles\rhsusf_m1a1fep_wd\Attributes\rhs_hideDUKE,
        "rhs_hideDUKE": {
            "defaultValue": 1,
            "displayName": "hide DUKE antennas",
            "property": "rhs_hideDUKE",
            "expression": "_this animate ['DUKE_Hide',_value,true];if(_value isEqualTo 1)then{_this removeWeaponTurret ['rhsusf_weap_duke',[0,0]]}",
            "control": "CheckboxNumber"
        },
        # Class: CfgVehicles\rhsusf_m1a1fep_wd\Attributes\rhs_decalBarrel_type,
        "rhs_decalBarrel_type": {
            "displayName": "Define type of barrel art",
            "tooltip": "Define type of barrel art. You can choose between desert & Woodland variants",
            "property": "rhs_decalBarrel_type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultValue": 0,
            "typeName": "STRING",
            # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_decalBarrel_type\values,
            "values": {
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_decalBarrel_type\values\BarrelArt_Abrams_D
                "BarrelArt_Abrams_D": {
                    "name": "Desert",
                    "value": "BarrelArt_Abrams_D",
                    "defaultValue": "BarrelArt_Abrams_D"
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_decalBarrel_type\values\BarrelArt_Abrams_WD,
                "BarrelArt_Abrams_WD": {
                    "name": "Woodland",
                    "value": "BarrelArt_Abrams_WD"
                }
            }
        },
        # Class: CfgVehicles\rhsusf_m1a1fep_wd\Attributes\rhs_decalBarrel,
        "rhs_decalBarrel": {
            "displayName": "Define barrel art",
            "tooltip": "Define barrel art. Available numbers from 0 to 55, type number above 55 to clear that place",
            "property": "rhs_decalBarrel",
            "control": "Edit",
            "expression": "if(_value >= 0)then{ [_this, [ [ 'Label', cM1BarrelSymPlaces,  _this getVariable ['rhs_decalBarrel_type','BarrelArt_Abrams_WD'],_value] ] ] call rhsusf_fnc_decalsInit;};",
            "defaultValue": "-1",
            "validate": "NUMBER",
            "typeName": "NUMBER"
        },
        # Class: CfgVehicles\rhsusf_m1a1fep_wd\Attributes\rhs_decalPlatoon_type,
        "rhs_decalPlatoon_type": {
            "displayName": "Define type of platoon symbol",
            "tooltip": "Define type of platoon symbol. You can choose between desert & Woodland variants",
            "property": "rhs_decalPlatoon_type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultValue": 0,
            "typeName": "STRING",
            # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_decalPlatoon_type\values,
            "values": {
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_decalPlatoon_type\values\ArmyPlt_Abrams_D
                "ArmyPlt_Abrams_D": {
                    "name": "Desert",
                    "value": "ArmyPlt_Abrams_D",
                    "defaultValue": "ArmyPlt_Abrams_D"
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_decalPlatoon_type\values\ArmyPlt_Abrams_WD,
                "ArmyPlt_Abrams_WD": {
                    "name": "Woodland",
                    "value": "ArmyPlt_Abrams_WD"
                }
            }
        },
        # Class: CfgVehicles\rhsusf_m1a1fep_wd\Attributes\rhs_decalPlatoon,
        "rhs_decalPlatoon": {
            "displayName": "Define platoon symbol",
            "tooltip": "Define platoon symbol",
            "property": "rhs_decalPlatoon",
            "control": "Combo",
            "expression": "if(_value >= 0)then{ [_this, [ [ 'Label', cM1PlnSymPlaces,  _this getVariable ['rhs_decalPlatoon_type','ArmyPlt_Abrams_D'],_value] ] ] call rhsusf_fnc_decalsInit};",
            "defaultValue": "-1",
            "typeName": "Number",
            # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_decalPlatoon\values,
            "values": {
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_decalPlatoon\values\Random
                "Random": {
                    "name": "Random",
                    "value": -1,
                    "defaultValue": -1
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_decalPlatoon\values\Empty,
                "Empty": {
                    "name": "Empty",
                    "value": 0,
                    "defaultValue": 0
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_decalPlatoon\values\Setting1,
                "Setting1": {
                    "name": "1st Platoon, 1st Vehicle",
                    "value": 1,
                    "defaultValue": 1
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_decalPlatoon\values\Setting2,
                "Setting2": {
                    "name": "1st Platoon, 2nd Vehicle",
                    "value": 2,
                    "defaultValue": 2
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_decalPlatoon\values\Setting3,
                "Setting3": {
                    "name": "1st Platoon, 3rd Vehicle",
                    "value": 3,
                    "defaultValue": 3
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_decalPlatoon\values\Setting4,
                "Setting4": {
                    "name": "1st Platoon, 4th Vehicle",
                    "value": 4,
                    "defaultValue": 4
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_decalPlatoon\values\Setting5,
                "Setting5": {
                    "name": "2nd Platoon, 1st Vehicle",
                    "value": 5,
                    "defaultValue": 5
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_decalPlatoon\values\Setting6,
                "Setting6": {
                    "name": "2nd Platoon, 2nd Vehicle",
                    "value": 6,
                    "defaultValue": 6
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_decalPlatoon\values\Setting7,
                "Setting7": {
                    "name": "2nd Platoon, 3rd Vehicle",
                    "value": 7,
                    "defaultValue": 7
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_decalPlatoon\values\Setting8,
                "Setting8": {
                    "name": "2nd Platoon, 4th Vehicle",
                    "value": 8,
                    "defaultValue": 8
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_decalPlatoon\values\Setting9,
                "Setting9": {
                    "name": "3rd Platoon, 1st Vehicle",
                    "value": 9,
                    "defaultValue": 9
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_decalPlatoon\values\Setting10,
                "Setting10": {
                    "name": "3rd Platoon, 2nd Vehicle",
                    "value": 10,
                    "defaultValue": 10
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_decalPlatoon\values\Setting11,
                "Setting11": {
                    "name": "3rd Platoon, 3rd Vehicle",
                    "value": 11,
                    "defaultValue": 11
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_decalPlatoon\values\Setting12,
                "Setting12": {
                    "name": "3rd Platoon, 4th Vehicle",
                    "value": 12,
                    "defaultValue": 12
                }
            }
        },
        # Class: CfgVehicles\rhsusf_m1a1fep_wd\Attributes\rhs_ammoslot_1_type,
        "rhs_ammoslot_1_type": {
            "displayName": "Ammo slot #1 type",
            "tooltip": "Define type of shell for #1 slot",
            "property": "rhs_ammoslot_1_type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultValue": 0,
            "typeName": "STRING",
            # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_ammoslot_1_type\values,
            "values": {
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_ammoslot_1_type\values\rhs_mag_M829A3
                "rhs_mag_M829A3": {
                    "name": "M829A3 APFSDS-T",
                    "value": "rhs_mag_M829A3",
                    "defaultValue": "rhs_mag_M829A3"
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_ammoslot_1_type\values\rhs_mag_M829A2,
                "rhs_mag_M829A2": {
                    "name": "M829A2 APFSDS-T",
                    "value": "rhs_mag_M829A2"
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_ammoslot_1_type\values\rhs_mag_M829A1,
                "rhs_mag_M829A1": {
                    "name": "M829A1 APFSDS-T",
                    "value": "rhs_mag_M829A1"
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_ammoslot_1_type\values\rhs_mag_M829,
                "rhs_mag_M829": {
                    "name": "M829 APFSDS-T",
                    "value": "rhs_mag_M829"
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_ammoslot_1_type\values\rhs_mag_M830,
                "rhs_mag_M830": {
                    "name": "M830 HEAT-FS",
                    "value": "rhs_mag_M830"
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_ammoslot_1_type\values\rhs_mag_M830A1,
                "rhs_mag_M830A1": {
                    "name": "M830A1 MPAT",
                    "value": "rhs_mag_M830A1"
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_ammoslot_1_type\values\rhs_mag_M1028,
                "rhs_mag_M1028": {
                    "name": "M1028 Canister",
                    "value": "rhs_mag_M1028"
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_ammoslot_1_type\values\rhs_mag_M1147,
                "rhs_mag_M1147": {
                    "name": "M1147 HE-FRAG",
                    "value": "rhs_mag_M1147"
                }
            }
        },
        # Class: CfgVehicles\rhsusf_m1a1fep_wd\Attributes\rhs_ammoslot_1,
        "rhs_ammoslot_1": {
            "displayName": "Ammo slot #1 count",
            "tooltip": "Define number of rounds stored inside of type #1. Max 36. Leave -1 for default loadout",
            "property": "rhs_ammoslot_1",
            "control": "Edit",
            "expression": "if(_value >= 0)then{ [_this,_value,'%s'] spawn rhs_fnc_m1_defineLoadout};",
            "defaultValue": "-1",
            "validate": "NUMBER",
            "typeName": "NUMBER"
        },
        # Class: CfgVehicles\rhsusf_m1a1fep_wd\Attributes\rhs_ammoslot_2_type,
        "rhs_ammoslot_2_type": {
            "displayName": "Ammo slot #2 type",
            "tooltip": "Define type of shell for #2 slot",
            "property": "rhs_ammoslot_2_type",
            "defaultValue": "0",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "typeName": "STRING",
            # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_ammoslot_1_type\values,
            "values": {
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_ammoslot_1_type\values\rhs_mag_M829A3
                "rhs_mag_M829A3": {
                    "name": "M829A3 APFSDS-T",
                    "value": "rhs_mag_M829A3",
                    "defaultValue": "rhs_mag_M829A3"
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_ammoslot_1_type\values\rhs_mag_M829A2,
                "rhs_mag_M829A2": {
                    "name": "M829A2 APFSDS-T",
                    "value": "rhs_mag_M829A2"
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_ammoslot_1_type\values\rhs_mag_M829A1,
                "rhs_mag_M829A1": {
                    "name": "M829A1 APFSDS-T",
                    "value": "rhs_mag_M829A1"
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_ammoslot_1_type\values\rhs_mag_M829,
                "rhs_mag_M829": {
                    "name": "M829 APFSDS-T",
                    "value": "rhs_mag_M829"
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_ammoslot_1_type\values\rhs_mag_M830,
                "rhs_mag_M830": {
                    "name": "M830 HEAT-FS",
                    "value": "rhs_mag_M830"
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_ammoslot_1_type\values\rhs_mag_M830A1,
                "rhs_mag_M830A1": {
                    "name": "M830A1 MPAT",
                    "value": "rhs_mag_M830A1"
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_ammoslot_1_type\values\rhs_mag_M1028,
                "rhs_mag_M1028": {
                    "name": "M1028 Canister",
                    "value": "rhs_mag_M1028"
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_ammoslot_1_type\values\rhs_mag_M1147,
                "rhs_mag_M1147": {
                    "name": "M1147 HE-FRAG",
                    "value": "rhs_mag_M1147"
                }
            }
        },
        # Class: CfgVehicles\rhsusf_m1a1fep_wd\Attributes\rhs_ammoslot_2,
        "rhs_ammoslot_2": {
            "displayName": "Ammo slot #2 count",
            "tooltip": "Define number of rounds stored inside of type #2. Max 36. Leave -1 for default loadout",
            "property": "rhs_ammoslot_2",
            "control": "Edit",
            "expression": "if(_value >= 0)then{ [_this,_value,'%s'] spawn rhs_fnc_m1_defineLoadout};",
            "defaultValue": "-1",
            "validate": "NUMBER",
            "typeName": "NUMBER"
        },
        # Class: CfgVehicles\rhsusf_m1a1fep_wd\Attributes\rhs_ammoslot_3_type,
        "rhs_ammoslot_3_type": {
            "displayName": "Ammo slot #3 type",
            "tooltip": "Define type of shell for #3 slot",
            "property": "rhs_ammoslot_3_type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultValue": 0,
            "typeName": "STRING",
            # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_ammoslot_1_type\values,
            "values": {
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_ammoslot_1_type\values\rhs_mag_M829A3
                "rhs_mag_M829A3": {
                    "name": "M829A3 APFSDS-T",
                    "value": "rhs_mag_M829A3",
                    "defaultValue": "rhs_mag_M829A3"
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_ammoslot_1_type\values\rhs_mag_M829A2,
                "rhs_mag_M829A2": {
                    "name": "M829A2 APFSDS-T",
                    "value": "rhs_mag_M829A2"
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_ammoslot_1_type\values\rhs_mag_M829A1,
                "rhs_mag_M829A1": {
                    "name": "M829A1 APFSDS-T",
                    "value": "rhs_mag_M829A1"
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_ammoslot_1_type\values\rhs_mag_M829,
                "rhs_mag_M829": {
                    "name": "M829 APFSDS-T",
                    "value": "rhs_mag_M829"
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_ammoslot_1_type\values\rhs_mag_M830,
                "rhs_mag_M830": {
                    "name": "M830 HEAT-FS",
                    "value": "rhs_mag_M830"
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_ammoslot_1_type\values\rhs_mag_M830A1,
                "rhs_mag_M830A1": {
                    "name": "M830A1 MPAT",
                    "value": "rhs_mag_M830A1"
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_ammoslot_1_type\values\rhs_mag_M1028,
                "rhs_mag_M1028": {
                    "name": "M1028 Canister",
                    "value": "rhs_mag_M1028"
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_ammoslot_1_type\values\rhs_mag_M1147,
                "rhs_mag_M1147": {
                    "name": "M1147 HE-FRAG",
                    "value": "rhs_mag_M1147"
                }
            }
        },
        # Class: CfgVehicles\rhsusf_m1a1fep_wd\Attributes\rhs_ammoslot_3,
        "rhs_ammoslot_3": {
            "displayName": "Ammo slot #3 count",
            "tooltip": "Define number of rounds stored inside of type #3. Max 36. Leave -1 for default loadout",
            "property": "rhs_ammoslot_3",
            "control": "Edit",
            "expression": "if(_value >= 0)then{ [_this,_value,'%s'] spawn rhs_fnc_m1_defineLoadout};",
            "defaultValue": "-1",
            "validate": "NUMBER",
            "typeName": "NUMBER"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Attributes\rhs_hideMiles,
        "rhs_hideMiles": {
            "displayName": "Hide Miles Panel",
            "property": "rhs_hideMiles",
            "control": "CheckboxNumber",
            "expression": "_this animate ['Miles_Hide',_value,true]",
            "defaultValue": "0"
        }
    },
    "model": "rhsusf|addons|rhsusf_m1a1|m1a1fep",
    "rhs_duke_type": "rhsusf_duke_m1a2",
    "hiddenSelections": ["camo1","camo2","camo3","camo4","duke_tex","","","n1","n2","n3","i1","i2","i3"],
    # Class: CfgVehicles\rhsusf_m1a1fep_d\textureSources,
    "textureSources": {
        # Class: CfgVehicles\rhsusf_m1a1fep_d\textureSources\woodland
        "woodland": {
            "displayName": "Woodland",
            "author": "Red Hammer Studios",
            "textures": ["rhsusf|addons|rhsusf_m1a1|data|rhsusf_m1a1aim_01_co.paa","rhsusf|addons|rhsusf_m1a1|data|rhsusf_m1a1aim_02_co.paa","rhsusf|addons|rhsusf_m1a1|data|rhsusf_m1a1aim_03_co.paa","rhsusf|addons|rhsusf_m1a1|loaderspintle|data|loaderspintle_wd_co.paa","rhsusf|addons|rhsusf_m1a1|duke|data|duke_antennae_wd_co.paa"]
        },
        # Class: CfgVehicles\rhsusf_m1a1fep_d\textureSources\desert,
        "desert": {
            "displayName": "Desert",
            "author": "Red Hammer Studios",
            "textures": ["rhsusf|addons|rhsusf_m1a1|data|rhsusf_m1a1aim_d_01_co.paa","rhsusf|addons|rhsusf_m1a1|data|rhsusf_m1a1aim_d_02_co.paa","rhsusf|addons|rhsusf_m1a1|data|rhsusf_m1a1aim_d_03_co.paa","rhsusf|addons|rhsusf_m1a1|loaderspintle|data|loaderspintle_d_co.paa","rhsusf|addons|rhsusf_m1a1|duke|data|duke_antennae_d_co.paa"]
        },
        # Class: CfgVehicles\rhsusf_m1a1fep_d\textureSources\OD,
        "OD": {
            "displayName": "Olive Drab",
            "author": "Red Hammer Studios",
            "textures": ["rhsusf|addons|rhsusf_m1a1|data|rhsusf_m1a1fep_od_01_co.paa","rhsusf|addons|rhsusf_m1a1|data|rhsusf_m1a1fep_od_02_co.paa","rhsusf|addons|rhsusf_m1a1|data|rhsusf_m1a1aim_03_co.paa","rhsusf|addons|rhsusf_m1a1|loaderspintle|data|loaderspintle_wd_co.paa","rhsusf|addons|rhsusf_m1a1|duke|data|duke_antennae_wd_co.paa"]
        }
    },
    "textureList": [],
    # Class: CfgVehicles\rhsusf_m1a1fep_d\Turrets,
    "Turrets": {
        # Class: CfgVehicles\rhsusf_m1a1fep_d\Turrets\MainTurret
        "MainTurret": {
            "weapons": ["rhs_weap_m256","rhs_weap_m240_abrams_coax","rhs_weap_fcs"],
            "magazines": ["rhs_mag_M829A3","rhs_mag_M830A1","rhs_mag_762x51_M240_1200","rhs_mag_762x51_M240_1200","rhs_mag_762x51_M240_1200","rhs_mag_762x51_M240_1200","rhs_mag_762x51_M240_1200","rhs_mag_762x51_M240_1200","rhs_mag_762x51_M240_1200","rhs_mag_762x51_M240_1200","rhs_mag_762x51_M240_1200","rhs_laserfcsmag","rhs_laserfcsmag"],
            # Class: CfgVehicles\rhsusf_m1a1fep_d\Turrets\MainTurret\Turrets,
            "Turrets": {
                # Class: CfgVehicles\rhsusf_m1a1fep_d\Turrets\MainTurret\Turrets\CommanderOptics
                "CommanderOptics": {
                    "weapons": ["RHS_M2_Abrams_Commander","rhsusf_weap_M257","rhsusf_weap_duke"],
                    "magazines": ["rhs_mag_100rnd_127x99_mag_Tracer_Red","rhs_mag_100rnd_127x99_mag_Tracer_Red","rhs_mag_100rnd_127x99_mag_Tracer_Red","rhs_mag_100rnd_127x99_mag_Tracer_Red","rhs_mag_100rnd_127x99_mag_Tracer_Red","rhs_mag_100rnd_127x99_mag_Tracer_Red","rhs_mag_100rnd_127x99_mag_Tracer_Red","rhs_mag_100rnd_127x99_mag_Tracer_Red","rhs_mag_100rnd_127x99_mag_Tracer_Red","rhs_mag_100rnd_127x99_mag_Tracer_Red","rhsusf_mag_L8A3_16","rhsusf_mag_duke"],
                    "discreteDistance": [400],
                    "discreteDistanceInitIndex": 0,
                    "turretInfoType": "RHS_RscCWSS",
                    # Class: CfgVehicles\rhsusf_m1a1fep_d\Turrets\MainTurret\Turrets\CommanderOptics\OpticsIn,
                    "OpticsIn": {
                        # Class: CfgVehicles\rhsusf_m1a1fep_d\Turrets\MainTurret\Turrets\CommanderOptics\OpticsIn\CWSS
                        "CWSS": {
                            "camPos": "commanderview_cwss",
                            "opticsDisplayName": "CWSS",
                            "initFov": 0.233333,
                            "minFov": 0.233333,
                            "maxFov": 0.233333,
                            "visionMode": ["Normal","TI"],
                            "thermalMode": [2,3],
                            "gunnerOpticsModel": "rhsusf|addons|rhsusf_optics|data|rhsusf_CWSS_Digital",
                            "gunnerOutOpticsModel": "A3|weapons_f|reticle|optics_empty",
                            "gunnerOpticsEffect": ["TankGunnerOptics1","OpticsBlur2","OpticsCHAbera2"],
                            "hitpoint": "Hit_Optic_ComCWSS",
                            "initAngleX": 0,
                            "minAngleX": -30,
                            "maxAngleX": 30,
                            "initAngleY": 0,
                            "minAngleY": -100,
                            "maxAngleY": 100,
                            "minMoveX": 0,
                            "maxMoveX": 0,
                            "minMoveY": 0,
                            "maxMoveY": 0,
                            "minMoveZ": 0,
                            "maxMoveZ": 0,
                            "speedZoomMaxSpeed": 1e+010,
                            "speedZoomMaxFOV": 0
                        },
                        # Class: CfgVehicles\rhsusf_m1a1fep_d\Turrets\MainTurret\Turrets\CommanderOptics\OpticsIn\CWSS_2x,
                        "CWSS_2x": {
                            "initFov": 0.116667,
                            "minFov": 0.116667,
                            "maxFov": 0.116667,
                            "camPos": "commanderview_cwss",
                            "opticsDisplayName": "CWSS",
                            "visionMode": ["Normal","TI"],
                            "thermalMode": [2,3],
                            "gunnerOpticsModel": "rhsusf|addons|rhsusf_optics|data|rhsusf_CWSS_Digital",
                            "gunnerOutOpticsModel": "A3|weapons_f|reticle|optics_empty",
                            "gunnerOpticsEffect": ["TankGunnerOptics1","OpticsBlur2","OpticsCHAbera2"],
                            "hitpoint": "Hit_Optic_ComCWSS",
                            "initAngleX": 0,
                            "minAngleX": -30,
                            "maxAngleX": 30,
                            "initAngleY": 0,
                            "minAngleY": -100,
                            "maxAngleY": 100,
                            "minMoveX": 0,
                            "maxMoveX": 0,
                            "minMoveY": 0,
                            "maxMoveY": 0,
                            "minMoveZ": 0,
                            "maxMoveZ": 0,
                            "speedZoomMaxSpeed": 1e+010,
                            "speedZoomMaxFOV": 0
                        },
                        # Class: CfgVehicles\rhsusf_m1a1fep_d\Turrets\MainTurret\Turrets\CommanderOptics\OpticsIn\CWSS_3x,
                        "CWSS_3x": {
                            "initFov": 0.0777778,
                            "minFov": 0.0777778,
                            "maxFov": 0.0777778,
                            "camPos": "commanderview_cwss",
                            "opticsDisplayName": "CWSS",
                            "visionMode": ["Normal","TI"],
                            "thermalMode": [2,3],
                            "gunnerOpticsModel": "rhsusf|addons|rhsusf_optics|data|rhsusf_CWSS_Digital",
                            "gunnerOutOpticsModel": "A3|weapons_f|reticle|optics_empty",
                            "gunnerOpticsEffect": ["TankGunnerOptics1","OpticsBlur2","OpticsCHAbera2"],
                            "hitpoint": "Hit_Optic_ComCWSS",
                            "initAngleX": 0,
                            "minAngleX": -30,
                            "maxAngleX": 30,
                            "initAngleY": 0,
                            "minAngleY": -100,
                            "maxAngleY": 100,
                            "minMoveX": 0,
                            "maxMoveX": 0,
                            "minMoveY": 0,
                            "maxMoveY": 0,
                            "minMoveZ": 0,
                            "maxMoveZ": 0,
                            "speedZoomMaxSpeed": 1e+010,
                            "speedZoomMaxFOV": 0
                        },
                        # Class: CfgVehicles\rhsusf_m1a1fep_d\Turrets\MainTurret\Turrets\CommanderOptics\OpticsIn\Periscope,
                        "Periscope": {
                            "camPos": "commanderview2",
                            "opticsDisplayName": "PERISCOPE",
                            "initFov": 0.7,
                            "minFov": 0.7,
                            "maxFov": 0.7,
                            "visionMode": ["Normal"],
                            "gunnerOpticsModel": "rhsusf|addons|rhsusf_optics|data|rhs_periscope_BISType",
                            "gunnerOpticsEffect": ["TankGunnerOptics1","OpticsBlur2","OpticsCHAbera2"],
                            "hitpoint": "Hit_Optic_ComPeriscope",
                            "initAngleX": 0,
                            "minAngleX": -30,
                            "maxAngleX": 30,
                            "initAngleY": 0,
                            "minAngleY": -100,
                            "maxAngleY": 100,
                            "thermalMode": [2,3],
                            "minMoveX": 0,
                            "maxMoveX": 0,
                            "minMoveY": 0,
                            "maxMoveY": 0,
                            "minMoveZ": 0,
                            "maxMoveZ": 0,
                            "speedZoomMaxSpeed": 1e+010,
                            "speedZoomMaxFOV": 0
                        },
                        # Class: CfgVehicles\rhsusf_m1a1fep_d\Turrets\MainTurret\Turrets\CommanderOptics\OpticsIn\CWS,
                        "CWS": {
                            "camPos": "commanderview",
                            "opticsDisplayName": "CWS",
                            "gunnerOpticsModel": "rhsusf|addons|rhsusf_optics|data|rhsusf_CWSS",
                            "visionMode": ["Normal","NVG"],
                            "hitpoint": "Hit_Optic_ComM2",
                            "initFov": 0.233333,
                            "minFov": 0.233333,
                            "maxFov": 0.233333,
                            "thermalMode": [2,3],
                            "gunnerOutOpticsModel": "A3|weapons_f|reticle|optics_empty",
                            "gunnerOpticsEffect": ["TankGunnerOptics1","OpticsBlur2","OpticsCHAbera2"],
                            "initAngleX": 0,
                            "minAngleX": -30,
                            "maxAngleX": 30,
                            "initAngleY": 0,
                            "minAngleY": -100,
                            "maxAngleY": 100,
                            "minMoveX": 0,
                            "maxMoveX": 0,
                            "minMoveY": 0,
                            "maxMoveY": 0,
                            "minMoveZ": 0,
                            "maxMoveZ": 0,
                            "speedZoomMaxSpeed": 1e+010,
                            "speedZoomMaxFOV": 0
                        }
                    },
                    "body": "obsTurret",
                    "gun": "obsGun",
                    "animationSourceBody": "obsTurret",
                    "animationSourceGun": "obsGun",
                    "maxHorizontalRotSpeed": 1.8,
                    "maxVerticalRotSpeed": 0.18,
                    "stabilizedInAxes": 3,
                    "soundServo": ["A3|Sounds_F|vehicles|armor|noises|servo_armor_comm",1,1,30],
                    "soundServoVertical": ["A3|Sounds_F|vehicles|armor|noises|servo_armor_comm",1,1,30],
                    "minElev": -10,
                    "maxElev": 45,
                    "initElev": 0,
                    "minTurn": -360,
                    "maxTurn": 360,
                    "initTurn": 0,
                    "memoryPointGun": "usti hlavne3",
                    "gunBeg": "usti hlavne3",
                    "gunEnd": "konec hlavne3",
                    "canUseScanners": 0,
                    "showCrewAim": 0,
                    "allowTabLock": 0,
                    "memoryPointGunnerOutOptics": "commanderview",
                    "memoryPointGunnerOptics": "commanderview",
                    "gunnerOpticsModel": "A3|weapons_f|reticle|Optics_Commander_02_F",
                    "gunnerOutOpticsModel": "",
                    "gunnerOpticsEffect": [],
                    "gunnerHasFlares": 1,
                    "gunnerForceOptics": 1,
                    # Class: CfgVehicles\rhsusf_m1a1tank_base\Turrets\MainTurret\Turrets\CommanderOptics\ViewOptics,
                    "ViewOptics": {
                        "initFov": 0.155,
                        "minFov": 0.034,
                        "maxFov": 0.155,
                        "visionMode": ["Normal","NVG"],
                        "initAngleX": 0,
                        "minAngleX": -30,
                        "maxAngleX": 30,
                        "initAngleY": 0,
                        "minAngleY": -100,
                        "maxAngleY": 100,
                        "thermalMode": [2,3],
                        "minMoveX": 0,
                        "maxMoveX": 0,
                        "minMoveY": 0,
                        "maxMoveY": 0,
                        "minMoveZ": 0,
                        "maxMoveZ": 0,
                        "speedZoomMaxSpeed": 1e+010,
                        "speedZoomMaxFOV": 0
                    },
                    "LodTurnedOut": 0,
                    "gunnerAction": "mbt2_slot2b_out",
                    "gunnerInAction": "RHS_M1A1_Commander",
                    "gunnerGetInAction": "GetInHigh",
                    "gunnerGetOutAction": "GetOutHigh",
                    "gunnerDoor": "hatchC",
                    "startEngine": 0,
                    "viewGunnerInExternal": 1,
                    "outGunnerMayFire": 0,
                    "inGunnerMayFire": 1,
                    # Class: CfgVehicles\rhsusf_m1a1tank_base\Turrets\MainTurret\Turrets\CommanderOptics\HitPoints,
                    "HitPoints": {
                        # Class: CfgVehicles\rhsusf_m1a1tank_base\Turrets\MainTurret\Turrets\CommanderOptics\HitPoints\HitTurretCom
                        "HitTurretCom": {
                            "armor": 0.3,
                            "material": -1,
                            "name": "vezVelitele",
                            "visual": "vezVelitele",
                            "passThrough": 0,
                            "minimalHit": 0.03,
                            "explosionShielding": 0.6,
                            "radius": 0.25,
                            "isTurret": 1
                        },
                        # Class: CfgVehicles\rhsusf_m1a1tank_base\Turrets\MainTurret\Turrets\CommanderOptics\HitPoints\HitGunCom,
                        "HitGunCom": {
                            "armor": 0.3,
                            "material": -1,
                            "name": "zbranVelitele",
                            "visual": "zbranVelitele",
                            "passThrough": 0,
                            "minimalHit": 0.03,
                            "explosionShielding": 0.6,
                            "radius": 0.25,
                            "isGun": 1
                        },
                        # Class: CfgVehicles\rhsusf_m1a1tank_base\Turrets\MainTurret\Turrets\CommanderOptics\HitPoints\Hit_Optic_ComPeriscope,
                        "Hit_Optic_ComPeriscope": {
                            "armor": -40,
                            "explosionShielding": 0,
                            "name": "",
                            "visual": "vis_optic_ComPeriscope",
                            "armorComponent": "Hit_Optic_ComPeriscope",
                            "passThrough": 0
                        },
                        # Class: CfgVehicles\rhsusf_m1a1tank_base\Turrets\MainTurret\Turrets\CommanderOptics\HitPoints\Hit_Optic_ComM2,
                        "Hit_Optic_ComM2": {
                            "visual": "vis_optic_ComM2",
                            "armorComponent": "Hit_Optic_ComM2",
                            "armor": -40,
                            "explosionShielding": 0,
                            "name": "",
                            "passThrough": 0
                        },
                        # Class: CfgVehicles\rhsusf_m1a1tank_base\Turrets\MainTurret\Turrets\CommanderOptics\HitPoints\Hit_Optic_ComCWSS,
                        "Hit_Optic_ComCWSS": {
                            "visual": "vis_optic_ComCWSS",
                            "armorComponent": "Hit_Optic_ComCWSS",
                            "armor": -40,
                            "explosionShielding": 0,
                            "name": "",
                            "passThrough": 0
                        }
                    },
                    "selectionFireAnim": "zasleh3",
                    "turretFollowFreeLook": 2,
                    "usePip": 2,
                    "animationSourceStickX": "com_turret_control_x",
                    "animationSourceStickY": "com_turret_control_y",
                    "gunnerRightHandAnimName": "com_turret_control",
                    "LODTurnedIn": 1100,
                    "LODOpticsIn": 0,
                    "viewGunnerShadowAmb": 0.5,
                    "viewGunnerShadowDiff": 0.05,
                    "isPersonTurret": 1,
                    "personTurretAction": "vehicle_turnout_2",
                    "minOutElev": -10,
                    "maxOutElev": 25,
                    "initOutElev": 0,
                    "minOutTurn": -95,
                    "maxOutTurn": 95,
                    "initOutTurn": 0,
                    # Class: CfgVehicles\MBT_01_base_F\Turrets\MainTurret\Turrets\CommanderOptics\ViewGunner,
                    "ViewGunner": {
                        "initAngleX": -10,
                        "initAngleY": 0,
                        "initFov": 0.9,
                        "minFov": 0.25,
                        "maxFov": 1.25,
                        "minAngleX": -65,
                        "maxAngleX": 85,
                        "minAngleY": -150,
                        "maxAngleY": 150,
                        "minMoveX": -0.075,
                        "maxMoveX": 0.075,
                        "minMoveY": -0.075,
                        "maxMoveY": 0.075,
                        "minMoveZ": -0.075,
                        "maxMoveZ": 0.1,
                        "speedZoomMaxSpeed": 1e+010,
                        "speedZoomMaxFOV": 0
                    },
                    # Class: CfgVehicles\Tank_F\Turrets\MainTurret\Turrets\CommanderOptics\Components,
                    "Components": {
                        # Class: CfgVehicles\Tank_F\Turrets\MainTurret\Turrets\CommanderOptics\Components\VehicleSystemsDisplayManagerComponentLeft
                        "VehicleSystemsDisplayManagerComponentLeft": {
                            # Class: VehicleSystemsTemplateLeftCommander\Components
                            "Components": {
                                # Class: VehicleSystemsTemplateLeftCommander\Components\VehicleDriverDisplay
                                "VehicleDriverDisplay": {
                                    "componentType": "TransportFeedDisplayComponent",
                                    "source": "Driver"
                                },
                                # Class: VehicleSystemsTemplateLeftCommander\Components\VehiclePrimaryGunnerDisplay,
                                "VehiclePrimaryGunnerDisplay": {
                                    "componentType": "TransportFeedDisplayComponent",
                                    "source": "PrimaryGunner"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\EmptyDisplay,
                                "EmptyDisplay": {
                                    "componentType": "EmptyDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\MinimapDisplay,
                                "MinimapDisplay": {
                                    "componentType": "MinimapDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\MineDetectorDisplay,
                                "MineDetectorDisplay": {
                                    "componentType": "MineDetectorDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\CrewDisplay,
                                "CrewDisplay": {
                                    "componentType": "CrewDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\UAVDisplay,
                                "UAVDisplay": {
                                    "componentType": "UAVFeedDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\SlingLoadDisplay,
                                "SlingLoadDisplay": {
                                    "componentType": "SlingLoadDisplayComponent"
                                }
                            },
                            "componentType": "VehicleSystemsDisplayManager",
                            "left": 1,
                            "defaultDisplay": "EmptyDisplay",
                            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,	(safezoneX + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40))])",
                            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                        },
                        # Class: CfgVehicles\Tank_F\Turrets\MainTurret\Turrets\CommanderOptics\Components\VehicleSystemsDisplayManagerComponentRight,
                        "VehicleSystemsDisplayManagerComponentRight": {
                            # Class: VehicleSystemsTemplateRightCommander\Components
                            "Components": {
                                # Class: VehicleSystemsTemplateRightCommander\Components\VehicleDriverDisplay
                                "VehicleDriverDisplay": {
                                    "componentType": "TransportFeedDisplayComponent",
                                    "source": "Driver"
                                },
                                # Class: VehicleSystemsTemplateRightCommander\Components\VehiclePrimaryGunnerDisplay,
                                "VehiclePrimaryGunnerDisplay": {
                                    "componentType": "TransportFeedDisplayComponent",
                                    "source": "PrimaryGunner"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight\Components\EmptyDisplay,
                                "EmptyDisplay": {
                                    "componentType": "EmptyDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight\Components\MinimapDisplay,
                                "MinimapDisplay": {
                                    "componentType": "MinimapDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight\Components\MineDetectorDisplay,
                                "MineDetectorDisplay": {
                                    "componentType": "MineDetectorDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight\Components\CrewDisplay,
                                "CrewDisplay": {
                                    "componentType": "CrewDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight\Components\UAVDisplay,
                                "UAVDisplay": {
                                    "componentType": "UAVFeedDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight\Components\SlingLoadDisplay,
                                "SlingLoadDisplay": {
                                    "componentType": "SlingLoadDisplayComponent"
                                }
                            },
                            "componentType": "VehicleSystemsDisplayManager",
                            "right": 1,
                            "defaultDisplay": "EmptyDisplay",
                            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,	((safezoneX + safezoneW) - (		(10 * 			(			((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40)))])",
                            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                        }
                    },
                    "proxyType": "CPCommander",
                    "proxyIndex": 1,
                    "gunnerName": "Commander",
                    "primaryGunner": 0,
                    "primaryObserver": 1,
                    "animationSourceHatch": "hatchCommander",
                    "animationSourceCamElev": "camElev",
                    "commanding": 2,
                    "gunnerOutOpticsColor": [0,0,0,1],
                    "gunnerOutForceOptics": 0,
                    "gunnerOutOpticsShowCursor": 0,
                    "gunnerOutOpticsEffect": [],
                    "memoryPointsGetInGunner": "pos commander",
                    "memoryPointsGetInGunnerDir": "pos commander dir",
                    "gunnerType": "",
                    "soundElevation": ["",0.00316228,1],
                    "minCamElev": -90,
                    "maxCamElev": 90,
                    "initCamElev": 0,
                    "primary": 1,
                    "hasGunner": 1,
                    "turretCanSee": 0,
                    # Class: CfgVehicles\AllVehicles\NewTurret\TurretSpec,
                    "TurretSpec": {
                        "showHeadPhones": 0
                    },
                    "gunnerOpticsColor": [0,0,0,1],
                    "gunnerOpticsShowCursor": 0,
                    "gunnerFireAlsoInInternalCamera": 1,
                    "gunnerOutFireAlsoInInternalCamera": 1,
                    "gunnerUsesPilotView": 0,
                    "castGunnerShadow": 0,
                    "viewGunnerShadow": 1,
                    "ejectDeadGunner": 0,
                    "hideWeaponsGunner": 1,
                    "canHideGunner": -1,
                    "forceHideGunner": 0,
                    "showHMD": 0,
                    "lockWhenDriverOut": 0,
                    "lockWhenVehicleSpeed": -1,
                    "gunnerCompartments": "Compartment1",
                    "memoryPointsGetInGunnerPrecise": "",
                    "missileBeg": "spice rakety",
                    "missileEnd": "konec rakety",
                    "armorLights": 0.4,
                    # Class: CfgVehicles\AllVehicles\NewTurret\Reflectors,
                    "Reflectors": {
                    },
                    "aggregateReflectors": [],
                    # Class: CfgVehicles\AllVehicles\NewTurret\GunFire,
                    "GunFire": {
                        "access": 0,
                        "cloudletDuration": 0.2,
                        "cloudletAnimPeriod": 1,
                        "cloudletSize": 1,
                        "cloudletAlpha": 1,
                        "cloudletGrowUp": 0.2,
                        "cloudletFadeIn": 0.01,
                        "cloudletFadeOut": 0.5,
                        "cloudletAccY": 0,
                        "cloudletMinYSpeed": -100,
                        "cloudletMaxYSpeed": 100,
                        "cloudletShape": "cloudletFire",
                        "cloudletColor": [1,1,1,0],
                        "interval": 0.01,
                        "size": 3,
                        "sourceSize": 0.5,
                        "timeToLive": 0,
                        "initT": 4500,
                        "deltaT": -3000,
                        # Class: WeaponFireGun\Table,
                        "Table": {
                            # Class: WeaponFireGun\Table\T0
                            "T0": {
                                "maxT": 0,
                                "color": [0.82,0.95,0.93,0]
                            },
                            # Class: WeaponFireGun\Table\T1,
                            "T1": {
                                "maxT": 200,
                                "color": [0.75,0.77,0.9,0]
                            },
                            # Class: WeaponFireGun\Table\T2,
                            "T2": {
                                "maxT": 400,
                                "color": [0.56,0.62,0.67,0]
                            },
                            # Class: WeaponFireGun\Table\T3,
                            "T3": {
                                "maxT": 600,
                                "color": [0.39,0.46,0.47,0]
                            },
                            # Class: WeaponFireGun\Table\T4,
                            "T4": {
                                "maxT": 800,
                                "color": [0.24,0.31,0.31,0]
                            },
                            # Class: WeaponFireGun\Table\T5,
                            "T5": {
                                "maxT": 1000,
                                "color": [0.23,0.31,0.29,0]
                            },
                            # Class: WeaponFireGun\Table\T6,
                            "T6": {
                                "maxT": 1500,
                                "color": [0.21,0.29,0.27,0]
                            },
                            # Class: WeaponFireGun\Table\T7,
                            "T7": {
                                "maxT": 2000,
                                "color": [0.19,0.23,0.21,0]
                            },
                            # Class: WeaponFireGun\Table\T8,
                            "T8": {
                                "maxT": 2300,
                                "color": [0.22,0.19,0.1,0]
                            },
                            # Class: WeaponFireGun\Table\T9,
                            "T9": {
                                "maxT": 2500,
                                "color": [0.35,0.2,0.02,0]
                            },
                            # Class: WeaponFireGun\Table\T10,
                            "T10": {
                                "maxT": 2600,
                                "color": [0.62,0.29,0.03,0]
                            },
                            # Class: WeaponFireGun\Table\T11,
                            "T11": {
                                "maxT": 2650,
                                "color": [0.59,0.35,0.05,0]
                            },
                            # Class: WeaponFireGun\Table\T12,
                            "T12": {
                                "maxT": 2700,
                                "color": [0.75,0.37,0.03,0]
                            },
                            # Class: WeaponFireGun\Table\T13,
                            "T13": {
                                "maxT": 2750,
                                "color": [0.88,0.34,0.03,0]
                            },
                            # Class: WeaponFireGun\Table\T14,
                            "T14": {
                                "maxT": 2800,
                                "color": [0.91,0.5,0.17,0]
                            },
                            # Class: WeaponFireGun\Table\T15,
                            "T15": {
                                "maxT": 2850,
                                "color": [1,0.6,0.2,0]
                            },
                            # Class: WeaponFireGun\Table\T16,
                            "T16": {
                                "maxT": 2900,
                                "color": [1,0.71,0.3,0]
                            },
                            # Class: WeaponFireGun\Table\T17,
                            "T17": {
                                "maxT": 2950,
                                "color": [0.98,0.83,0.41,0]
                            },
                            # Class: WeaponFireGun\Table\T18,
                            "T18": {
                                "maxT": 3000,
                                "color": [0.98,0.91,0.54,0]
                            },
                            # Class: WeaponFireGun\Table\T19,
                            "T19": {
                                "maxT": 3100,
                                "color": [0.98,0.99,0.6,0]
                            },
                            # Class: WeaponFireGun\Table\T20,
                            "T20": {
                                "maxT": 3300,
                                "color": [0.96,0.99,0.72,0]
                            },
                            # Class: WeaponFireGun\Table\T21,
                            "T21": {
                                "maxT": 3600,
                                "color": [1,0.98,0.91,0]
                            },
                            # Class: WeaponFireGun\Table\T22,
                            "T22": {
                                "maxT": 4200,
                                "color": [1,1,1,0]
                            }
                        }
                    },
                    # Class: CfgVehicles\AllVehicles\NewTurret\GunClouds,
                    "GunClouds": {
                        "access": 0,
                        "cloudletDuration": 0.3,
                        "cloudletAnimPeriod": 1,
                        "cloudletSize": 1,
                        "cloudletAlpha": 1,
                        "cloudletGrowUp": 1,
                        "cloudletFadeIn": 0.01,
                        "cloudletFadeOut": 1,
                        "cloudletAccY": 0.4,
                        "cloudletMinYSpeed": 0.2,
                        "cloudletMaxYSpeed": 0.8,
                        "cloudletShape": "cloudletClouds",
                        "cloudletColor": [1,1,1,0],
                        "interval": 0.05,
                        "size": 3,
                        "sourceSize": 0.5,
                        "timeToLive": 0,
                        "initT": 0,
                        "deltaT": 0,
                        # Class: WeaponCloudsGun\Table,
                        "Table": {
                            # Class: WeaponCloudsGun\Table\T0
                            "T0": {
                                "maxT": 0,
                                "color": [1,1,1,0]
                            }
                        }
                    },
                    # Class: CfgVehicles\AllVehicles\NewTurret\MGunClouds,
                    "MGunClouds": {
                        "access": 0,
                        "cloudletGrowUp": 0.05,
                        "cloudletFadeIn": 0,
                        "cloudletFadeOut": 0.1,
                        "cloudletDuration": 0.05,
                        "cloudletAnimPeriod": 1,
                        "cloudletSize": 1,
                        "cloudletAlpha": 0.3,
                        "cloudletAccY": 0,
                        "cloudletMinYSpeed": -100,
                        "cloudletMaxYSpeed": 100,
                        "cloudletShape": "cloudletClouds",
                        "cloudletColor": [1,1,1,0],
                        "timeToLive": 0,
                        "interval": 0.02,
                        "size": 0.3,
                        "sourceSize": 0.02,
                        "initT": 0,
                        "deltaT": 0,
                        # Class: WeaponCloudsMGun\Table,
                        "Table": {
                            # Class: WeaponCloudsMGun\Table\T0
                            "T0": {
                                "maxT": 0,
                                "color": [1,1,1,0]
                            }
                        }
                    },
                    # Class: CfgVehicles\AllVehicles\NewTurret\Turrets,
                    "Turrets": {
                    },
                    "forceNVG": 0,
                    "isCopilot": 0,
                    "canEject": 1,
                    "gunnerLeftHandAnimName": "",
                    "gunnerLeftLegAnimName": "",
                    "gunnerRightLegAnimName": "",
                    "preciseGetInOut": 0,
                    "showAllTargets": 0,
                    "dontCreateAI": 0,
                    "disableSoundAttenuation": 0,
                    "slingLoadOperator": 0,
                    "playerPosition": 0,
                    "allowLauncherIn": 0,
                    "allowLauncherOut": 0,
                    # Class: CfgVehicles\AllVehicles\NewTurret\TurnIn,
                    "TurnIn": {
                        "turnOffset": 0
                    },
                    # Class: CfgVehicles\AllVehicles\NewTurret\TurnOut,
                    "TurnOut": {
                        "turnOffset": 0
                    }
                },
                # Class: CfgVehicles\rhsusf_m1a1fep_d\Turrets\MainTurret\Turrets\Loader,
                "Loader": {
                    # Class: CfgVehicles\rhsusf_m1a1tank_base\Turrets\MainTurret\Turrets\Loader\HitPoints
                    "HitPoints": {
                        # Class: CfgVehicles\rhsusf_m1a1tank_base\Turrets\MainTurret\Turrets\Loader\HitPoints\Hit_Optic_LoaderPeriscope
                        "Hit_Optic_LoaderPeriscope": {
                            "armor": -40,
                            "explosionShielding": 0,
                            "name": "",
                            "visual": "vis_optic_LoaderPeriscope",
                            "armorComponent": "Hit_Optic_LoaderPeriscope",
                            "passThrough": 0
                        }
                    },
                    "isPersonTurret": 0,
                    "lockWhenDriverOut": 0,
                    "lodTurnedOut": 1200,
                    "minTurn": -34,
                    "maxTurn": 140,
                    "discreteDistance": [100,200,300,400,500,600,700,800,900],
                    "discreteDistanceInitIndex": 2,
                    "turretInfoType": "RHS_RscWeaponZeroing",
                    "weapons": ["rhs_weap_m240_abrams"],
                    "magazines": ["rhs_mag_762x51_M240_200","rhs_mag_762x51_M240_200","rhs_mag_762x51_M240_200"],
                    "stabilizedInAxes": 0,
                    "memoryPointGunnerOutOptics": "loader_out_view",
                    "memoryPointGunnerOptics": "loaderview",
                    "gunnerLeftHandAnimName": "Loader_Gun",
                    "gunnerRightHandAnimName": "Loader_Gun",
                    "gunnerAction": "RHS_M1A2_CommanderOUT",
                    "gunnerInAction": "RHS_M1A1_Loader",
                    "gunnerOutForceOptics": 0,
                    "gunnerOutOpticsModel": "A3|weapons_f|reticle|optics_empty",
                    "inGunnerMayFire": 0,
                    "outGunnerMayFire": 1,
                    "memoryPointGun": "usti hlavne5",
                    "gunBeg": "usti hlavne5",
                    "gunEnd": "konec hlavne5",
                    "selectionFireAnim": "zasleh5",
                    "soundAttenuationTurret": "HeliAttenuationGunner",
                    "disableSoundAttenuation": 0,
                    "animationSourceHatch": "HatchGunner",
                    "body": "LoaderTurret",
                    "gun": "LoaderGun",
                    "animationSourceBody": "LoaderTurret",
                    "animationSourceGun": "LoaderGun",
                    "commanding": -3,
                    "primaryObserver": 0,
                    "memoryPointsGetInGunner": "pos gunner",
                    "memoryPointsGetInGunnerDir": "pos gunner dir",
                    "gunnername": "Loader",
                    "gunnerDoor": "hatchL",
                    "proxyindex": 2,
                    # Class: CfgVehicles\rhsusf_m1a1tank_base\Turrets\MainTurret\Turrets\Loader\OpticsIn,
                    "OpticsIn": {
                        # Class: CfgVehicles\rhsusf_m1a1tank_base\Turrets\MainTurret\Turrets\Loader\OpticsIn\Periscope
                        "Periscope": {
                            "initFov": 0.7,
                            "minFov": 0.7,
                            "maxFov": 0.7,
                            "visionMode": ["Normal"],
                            "gunnerOpticsModel": "rhsusf|addons|rhsusf_optics|data|rhs_periscope_BISType",
                            "hitpoint": "Hit_Optic_LoaderPeriscope",
                            "initAngleX": 0,
                            "minAngleX": -30,
                            "maxAngleX": 30,
                            "initAngleY": 0,
                            "minAngleY": -100,
                            "maxAngleY": 100,
                            "thermalMode": [2,3],
                            "minMoveX": 0,
                            "maxMoveX": 0,
                            "minMoveY": 0,
                            "maxMoveY": 0,
                            "minMoveZ": 0,
                            "maxMoveZ": 0,
                            "speedZoomMaxSpeed": 1e+010,
                            "speedZoomMaxFOV": 0
                        }
                    },
                    "maxHorizontalRotSpeed": 1.8,
                    "maxVerticalRotSpeed": 0.18,
                    "soundServo": ["A3|Sounds_F|vehicles|armor|noises|servo_armor_comm",1,1,30],
                    "soundServoVertical": ["A3|Sounds_F|vehicles|armor|noises|servo_armor_comm",1,1,30],
                    "minElev": -10,
                    "maxElev": 45,
                    "initElev": 0,
                    "initTurn": 0,
                    "canUseScanners": 0,
                    "showCrewAim": 0,
                    "allowTabLock": 0,
                    "gunnerOpticsModel": "A3|weapons_f|reticle|Optics_Commander_02_F",
                    "gunnerOpticsEffect": [],
                    "gunnerHasFlares": 1,
                    "gunnerForceOptics": 1,
                    # Class: CfgVehicles\rhsusf_m1a1tank_base\Turrets\MainTurret\Turrets\CommanderOptics\ViewOptics,
                    "ViewOptics": {
                        "initFov": 0.155,
                        "minFov": 0.034,
                        "maxFov": 0.155,
                        "visionMode": ["Normal","NVG"],
                        "initAngleX": 0,
                        "minAngleX": -30,
                        "maxAngleX": 30,
                        "initAngleY": 0,
                        "minAngleY": -100,
                        "maxAngleY": 100,
                        "thermalMode": [2,3],
                        "minMoveX": 0,
                        "maxMoveX": 0,
                        "minMoveY": 0,
                        "maxMoveY": 0,
                        "minMoveZ": 0,
                        "maxMoveZ": 0,
                        "speedZoomMaxSpeed": 1e+010,
                        "speedZoomMaxFOV": 0
                    },
                    "gunnerGetInAction": "GetInHigh",
                    "gunnerGetOutAction": "GetOutHigh",
                    "startEngine": 0,
                    "viewGunnerInExternal": 1,
                    "turretFollowFreeLook": 2,
                    "usePip": 2,
                    "animationSourceStickX": "com_turret_control_x",
                    "animationSourceStickY": "com_turret_control_y",
                    "LODTurnedIn": 1100,
                    "LODOpticsIn": 0,
                    "viewGunnerShadowAmb": 0.5,
                    "viewGunnerShadowDiff": 0.05,
                    "personTurretAction": "vehicle_turnout_2",
                    "minOutElev": -10,
                    "maxOutElev": 25,
                    "initOutElev": 0,
                    "minOutTurn": -95,
                    "maxOutTurn": 95,
                    "initOutTurn": 0,
                    # Class: CfgVehicles\MBT_01_base_F\Turrets\MainTurret\Turrets\CommanderOptics\ViewGunner,
                    "ViewGunner": {
                        "initAngleX": -10,
                        "initAngleY": 0,
                        "initFov": 0.9,
                        "minFov": 0.25,
                        "maxFov": 1.25,
                        "minAngleX": -65,
                        "maxAngleX": 85,
                        "minAngleY": -150,
                        "maxAngleY": 150,
                        "minMoveX": -0.075,
                        "maxMoveX": 0.075,
                        "minMoveY": -0.075,
                        "maxMoveY": 0.075,
                        "minMoveZ": -0.075,
                        "maxMoveZ": 0.1,
                        "speedZoomMaxSpeed": 1e+010,
                        "speedZoomMaxFOV": 0
                    },
                    # Class: CfgVehicles\Tank_F\Turrets\MainTurret\Turrets\CommanderOptics\Components,
                    "Components": {
                        # Class: CfgVehicles\Tank_F\Turrets\MainTurret\Turrets\CommanderOptics\Components\VehicleSystemsDisplayManagerComponentLeft
                        "VehicleSystemsDisplayManagerComponentLeft": {
                            # Class: VehicleSystemsTemplateLeftCommander\Components
                            "Components": {
                                # Class: VehicleSystemsTemplateLeftCommander\Components\VehicleDriverDisplay
                                "VehicleDriverDisplay": {
                                    "componentType": "TransportFeedDisplayComponent",
                                    "source": "Driver"
                                },
                                # Class: VehicleSystemsTemplateLeftCommander\Components\VehiclePrimaryGunnerDisplay,
                                "VehiclePrimaryGunnerDisplay": {
                                    "componentType": "TransportFeedDisplayComponent",
                                    "source": "PrimaryGunner"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\EmptyDisplay,
                                "EmptyDisplay": {
                                    "componentType": "EmptyDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\MinimapDisplay,
                                "MinimapDisplay": {
                                    "componentType": "MinimapDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\MineDetectorDisplay,
                                "MineDetectorDisplay": {
                                    "componentType": "MineDetectorDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\CrewDisplay,
                                "CrewDisplay": {
                                    "componentType": "CrewDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\UAVDisplay,
                                "UAVDisplay": {
                                    "componentType": "UAVFeedDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\SlingLoadDisplay,
                                "SlingLoadDisplay": {
                                    "componentType": "SlingLoadDisplayComponent"
                                }
                            },
                            "componentType": "VehicleSystemsDisplayManager",
                            "left": 1,
                            "defaultDisplay": "EmptyDisplay",
                            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,	(safezoneX + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40))])",
                            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                        },
                        # Class: CfgVehicles\Tank_F\Turrets\MainTurret\Turrets\CommanderOptics\Components\VehicleSystemsDisplayManagerComponentRight,
                        "VehicleSystemsDisplayManagerComponentRight": {
                            # Class: VehicleSystemsTemplateRightCommander\Components
                            "Components": {
                                # Class: VehicleSystemsTemplateRightCommander\Components\VehicleDriverDisplay
                                "VehicleDriverDisplay": {
                                    "componentType": "TransportFeedDisplayComponent",
                                    "source": "Driver"
                                },
                                # Class: VehicleSystemsTemplateRightCommander\Components\VehiclePrimaryGunnerDisplay,
                                "VehiclePrimaryGunnerDisplay": {
                                    "componentType": "TransportFeedDisplayComponent",
                                    "source": "PrimaryGunner"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight\Components\EmptyDisplay,
                                "EmptyDisplay": {
                                    "componentType": "EmptyDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight\Components\MinimapDisplay,
                                "MinimapDisplay": {
                                    "componentType": "MinimapDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight\Components\MineDetectorDisplay,
                                "MineDetectorDisplay": {
                                    "componentType": "MineDetectorDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight\Components\CrewDisplay,
                                "CrewDisplay": {
                                    "componentType": "CrewDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight\Components\UAVDisplay,
                                "UAVDisplay": {
                                    "componentType": "UAVFeedDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight\Components\SlingLoadDisplay,
                                "SlingLoadDisplay": {
                                    "componentType": "SlingLoadDisplayComponent"
                                }
                            },
                            "componentType": "VehicleSystemsDisplayManager",
                            "right": 1,
                            "defaultDisplay": "EmptyDisplay",
                            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,	((safezoneX + safezoneW) - (		(10 * 			(			((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40)))])",
                            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                        }
                    },
                    "proxyType": "CPCommander",
                    "primaryGunner": 0,
                    "animationSourceCamElev": "camElev",
                    "gunnerOutOpticsColor": [0,0,0,1],
                    "gunnerOutOpticsShowCursor": 0,
                    "gunnerOutOpticsEffect": [],
                    "gunnerType": "",
                    "soundElevation": ["",0.00316228,1],
                    "minCamElev": -90,
                    "maxCamElev": 90,
                    "initCamElev": 0,
                    "primary": 1,
                    "hasGunner": 1,
                    "turretCanSee": 0,
                    # Class: CfgVehicles\AllVehicles\NewTurret\TurretSpec,
                    "TurretSpec": {
                        "showHeadPhones": 0
                    },
                    "gunnerOpticsColor": [0,0,0,1],
                    "gunnerOpticsShowCursor": 0,
                    "gunnerFireAlsoInInternalCamera": 1,
                    "gunnerOutFireAlsoInInternalCamera": 1,
                    "gunnerUsesPilotView": 0,
                    "castGunnerShadow": 0,
                    "viewGunnerShadow": 1,
                    "ejectDeadGunner": 0,
                    "hideWeaponsGunner": 1,
                    "canHideGunner": -1,
                    "forceHideGunner": 0,
                    "showHMD": 0,
                    "lockWhenVehicleSpeed": -1,
                    "gunnerCompartments": "Compartment1",
                    "memoryPointsGetInGunnerPrecise": "",
                    "missileBeg": "spice rakety",
                    "missileEnd": "konec rakety",
                    "armorLights": 0.4,
                    # Class: CfgVehicles\AllVehicles\NewTurret\Reflectors,
                    "Reflectors": {
                    },
                    "aggregateReflectors": [],
                    # Class: CfgVehicles\AllVehicles\NewTurret\GunFire,
                    "GunFire": {
                        "access": 0,
                        "cloudletDuration": 0.2,
                        "cloudletAnimPeriod": 1,
                        "cloudletSize": 1,
                        "cloudletAlpha": 1,
                        "cloudletGrowUp": 0.2,
                        "cloudletFadeIn": 0.01,
                        "cloudletFadeOut": 0.5,
                        "cloudletAccY": 0,
                        "cloudletMinYSpeed": -100,
                        "cloudletMaxYSpeed": 100,
                        "cloudletShape": "cloudletFire",
                        "cloudletColor": [1,1,1,0],
                        "interval": 0.01,
                        "size": 3,
                        "sourceSize": 0.5,
                        "timeToLive": 0,
                        "initT": 4500,
                        "deltaT": -3000,
                        # Class: WeaponFireGun\Table,
                        "Table": {
                            # Class: WeaponFireGun\Table\T0
                            "T0": {
                                "maxT": 0,
                                "color": [0.82,0.95,0.93,0]
                            },
                            # Class: WeaponFireGun\Table\T1,
                            "T1": {
                                "maxT": 200,
                                "color": [0.75,0.77,0.9,0]
                            },
                            # Class: WeaponFireGun\Table\T2,
                            "T2": {
                                "maxT": 400,
                                "color": [0.56,0.62,0.67,0]
                            },
                            # Class: WeaponFireGun\Table\T3,
                            "T3": {
                                "maxT": 600,
                                "color": [0.39,0.46,0.47,0]
                            },
                            # Class: WeaponFireGun\Table\T4,
                            "T4": {
                                "maxT": 800,
                                "color": [0.24,0.31,0.31,0]
                            },
                            # Class: WeaponFireGun\Table\T5,
                            "T5": {
                                "maxT": 1000,
                                "color": [0.23,0.31,0.29,0]
                            },
                            # Class: WeaponFireGun\Table\T6,
                            "T6": {
                                "maxT": 1500,
                                "color": [0.21,0.29,0.27,0]
                            },
                            # Class: WeaponFireGun\Table\T7,
                            "T7": {
                                "maxT": 2000,
                                "color": [0.19,0.23,0.21,0]
                            },
                            # Class: WeaponFireGun\Table\T8,
                            "T8": {
                                "maxT": 2300,
                                "color": [0.22,0.19,0.1,0]
                            },
                            # Class: WeaponFireGun\Table\T9,
                            "T9": {
                                "maxT": 2500,
                                "color": [0.35,0.2,0.02,0]
                            },
                            # Class: WeaponFireGun\Table\T10,
                            "T10": {
                                "maxT": 2600,
                                "color": [0.62,0.29,0.03,0]
                            },
                            # Class: WeaponFireGun\Table\T11,
                            "T11": {
                                "maxT": 2650,
                                "color": [0.59,0.35,0.05,0]
                            },
                            # Class: WeaponFireGun\Table\T12,
                            "T12": {
                                "maxT": 2700,
                                "color": [0.75,0.37,0.03,0]
                            },
                            # Class: WeaponFireGun\Table\T13,
                            "T13": {
                                "maxT": 2750,
                                "color": [0.88,0.34,0.03,0]
                            },
                            # Class: WeaponFireGun\Table\T14,
                            "T14": {
                                "maxT": 2800,
                                "color": [0.91,0.5,0.17,0]
                            },
                            # Class: WeaponFireGun\Table\T15,
                            "T15": {
                                "maxT": 2850,
                                "color": [1,0.6,0.2,0]
                            },
                            # Class: WeaponFireGun\Table\T16,
                            "T16": {
                                "maxT": 2900,
                                "color": [1,0.71,0.3,0]
                            },
                            # Class: WeaponFireGun\Table\T17,
                            "T17": {
                                "maxT": 2950,
                                "color": [0.98,0.83,0.41,0]
                            },
                            # Class: WeaponFireGun\Table\T18,
                            "T18": {
                                "maxT": 3000,
                                "color": [0.98,0.91,0.54,0]
                            },
                            # Class: WeaponFireGun\Table\T19,
                            "T19": {
                                "maxT": 3100,
                                "color": [0.98,0.99,0.6,0]
                            },
                            # Class: WeaponFireGun\Table\T20,
                            "T20": {
                                "maxT": 3300,
                                "color": [0.96,0.99,0.72,0]
                            },
                            # Class: WeaponFireGun\Table\T21,
                            "T21": {
                                "maxT": 3600,
                                "color": [1,0.98,0.91,0]
                            },
                            # Class: WeaponFireGun\Table\T22,
                            "T22": {
                                "maxT": 4200,
                                "color": [1,1,1,0]
                            }
                        }
                    },
                    # Class: CfgVehicles\AllVehicles\NewTurret\GunClouds,
                    "GunClouds": {
                        "access": 0,
                        "cloudletDuration": 0.3,
                        "cloudletAnimPeriod": 1,
                        "cloudletSize": 1,
                        "cloudletAlpha": 1,
                        "cloudletGrowUp": 1,
                        "cloudletFadeIn": 0.01,
                        "cloudletFadeOut": 1,
                        "cloudletAccY": 0.4,
                        "cloudletMinYSpeed": 0.2,
                        "cloudletMaxYSpeed": 0.8,
                        "cloudletShape": "cloudletClouds",
                        "cloudletColor": [1,1,1,0],
                        "interval": 0.05,
                        "size": 3,
                        "sourceSize": 0.5,
                        "timeToLive": 0,
                        "initT": 0,
                        "deltaT": 0,
                        # Class: WeaponCloudsGun\Table,
                        "Table": {
                            # Class: WeaponCloudsGun\Table\T0
                            "T0": {
                                "maxT": 0,
                                "color": [1,1,1,0]
                            }
                        }
                    },
                    # Class: CfgVehicles\AllVehicles\NewTurret\MGunClouds,
                    "MGunClouds": {
                        "access": 0,
                        "cloudletGrowUp": 0.05,
                        "cloudletFadeIn": 0,
                        "cloudletFadeOut": 0.1,
                        "cloudletDuration": 0.05,
                        "cloudletAnimPeriod": 1,
                        "cloudletSize": 1,
                        "cloudletAlpha": 0.3,
                        "cloudletAccY": 0,
                        "cloudletMinYSpeed": -100,
                        "cloudletMaxYSpeed": 100,
                        "cloudletShape": "cloudletClouds",
                        "cloudletColor": [1,1,1,0],
                        "timeToLive": 0,
                        "interval": 0.02,
                        "size": 0.3,
                        "sourceSize": 0.02,
                        "initT": 0,
                        "deltaT": 0,
                        # Class: WeaponCloudsMGun\Table,
                        "Table": {
                            # Class: WeaponCloudsMGun\Table\T0
                            "T0": {
                                "maxT": 0,
                                "color": [1,1,1,0]
                            }
                        }
                    },
                    # Class: CfgVehicles\AllVehicles\NewTurret\Turrets,
                    "Turrets": {
                    },
                    "forceNVG": 0,
                    "isCopilot": 0,
                    "canEject": 1,
                    "gunnerLeftLegAnimName": "",
                    "gunnerRightLegAnimName": "",
                    "preciseGetInOut": 0,
                    "showAllTargets": 0,
                    "dontCreateAI": 0,
                    "slingLoadOperator": 0,
                    "playerPosition": 0,
                    "allowLauncherIn": 0,
                    "allowLauncherOut": 0,
                    # Class: CfgVehicles\AllVehicles\NewTurret\TurnIn,
                    "TurnIn": {
                        "turnOffset": 0
                    },
                    # Class: CfgVehicles\AllVehicles\NewTurret\TurnOut,
                    "TurnOut": {
                        "turnOffset": 0
                    }
                }
            },
            "lockWhenDriverOut": 1,
            "animationSourceHatch": "",
            "memoryPointGun": "usti hlavne2",
            "selectionFireAnim": "zaslehCoax",
            "gunBeg": "usti hlavne",
            "gunEnd": "konec hlavne",
            "minElev": -10,
            "maxElev": 22,
            "initElev": 5,
            # Class: CfgVehicles\rhsusf_m1a1tank_base\Turrets\MainTurret\TurnIn,
            "TurnIn": {
                "limitsArrayTop": [[22,-180],[22,180]],
                "limitsArrayBottom": [[1.4,-180],[0.7,-134.687],[-9.3683,-133.687],[-10,0],[-9.7173,133.637],[0.7,134.687],[1.4,180]]
            },
            "soundServo": ["rhsusf|addons|rhsusf_m1a1|sounds|traverse",15,1,20],
            "maxhorizontalrotspeed": 0.7,
            "maxverticalrotspeed": 0.44,
            "turretInfoType": "RHS_RscWeaponM1_FCS",
            "discreteDistance": [],
            "canUseScanners": 0,
            "showCrewAim": 0,
            "allowTabLock": 0,
            "memoryPointsGetInGunner": "pos commander",
            "memoryPointsGetInGunnerDir": "pos commander dir",
            "memoryPointGunnerOptics": "gunnerview",
            "gunnerOutOpticsModel": "",
            "gunnerOutOpticsEffect": [],
            "gunnerOpticsEffect": [],
            "gunnerForceOptics": 1,
            # Class: CfgVehicles\rhsusf_m1a1tank_base\Turrets\MainTurret\OpticsIn,
            "OpticsIn": {
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Turrets\MainTurret\OpticsIn\Wide
                "Wide": {
                    "initAngleX": 0,
                    "minAngleX": -30,
                    "maxAngleX": 30,
                    "initAngleY": 0,
                    "minAngleY": -100,
                    "maxAngleY": 100,
                    "initFov": 0.233333,
                    "minFov": 0.233333,
                    "maxFov": 0.233333,
                    "visionMode": ["Normal"],
                    "thermalMode": [2,3],
                    "gunnerOpticsModel": "rhsusf|addons|rhsusf_m1a1|gunnerOptics_M1A2",
                    "hitpoint": "Hit_Optic_GPS",
                    "minMoveX": 0,
                    "maxMoveX": 0,
                    "minMoveY": 0,
                    "maxMoveY": 0,
                    "minMoveZ": 0,
                    "maxMoveZ": 0,
                    "speedZoomMaxSpeed": 1e+010,
                    "speedZoomMaxFOV": 0
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Turrets\MainTurret\OpticsIn\Medium,
                "Medium": {
                    "gunnerOpticsModel": "rhsusf|addons|rhsusf_m1a1|gunnerOptics_M1A1_2",
                    "initFov": 0.07,
                    "minFov": 0.07,
                    "maxFov": 0.07,
                    "initAngleX": 0,
                    "minAngleX": -30,
                    "maxAngleX": 30,
                    "initAngleY": 0,
                    "minAngleY": -100,
                    "maxAngleY": 100,
                    "visionMode": ["Normal"],
                    "thermalMode": [2,3],
                    "hitpoint": "Hit_Optic_GPS",
                    "minMoveX": 0,
                    "maxMoveX": 0,
                    "minMoveY": 0,
                    "maxMoveY": 0,
                    "minMoveZ": 0,
                    "maxMoveZ": 0,
                    "speedZoomMaxSpeed": 1e+010,
                    "speedZoomMaxFOV": 0
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Turrets\MainTurret\OpticsIn\Wide_TI,
                "Wide_TI": {
                    "gunnerOpticsModel": "rhsusf|addons|rhsusf_m1a1|gunnerOptics_M1A2_ti",
                    "visionMode": ["Ti"],
                    "initFov": 0.233333,
                    "minFov": 0.233333,
                    "maxFov": 0.233333,
                    "hitpoint": "Hit_Optic_GPS_TI",
                    "initAngleX": 0,
                    "minAngleX": -30,
                    "maxAngleX": 30,
                    "initAngleY": 0,
                    "minAngleY": -100,
                    "maxAngleY": 100,
                    "thermalMode": [2,3],
                    "minMoveX": 0,
                    "maxMoveX": 0,
                    "minMoveY": 0,
                    "maxMoveY": 0,
                    "minMoveZ": 0,
                    "maxMoveZ": 0,
                    "speedZoomMaxSpeed": 1e+010,
                    "speedZoomMaxFOV": 0
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Turrets\MainTurret\OpticsIn\Wide2_TI,
                "Wide2_TI": {
                    "initFov": 0.116667,
                    "minFov": 0.116667,
                    "maxFov": 0.116667,
                    "gunnerOpticsModel": "rhsusf|addons|rhsusf_m1a1|gunnerOptics_M1A2_ti",
                    "visionMode": ["Ti"],
                    "hitpoint": "Hit_Optic_GPS_TI",
                    "initAngleX": 0,
                    "minAngleX": -30,
                    "maxAngleX": 30,
                    "initAngleY": 0,
                    "minAngleY": -100,
                    "maxAngleY": 100,
                    "thermalMode": [2,3],
                    "minMoveX": 0,
                    "maxMoveX": 0,
                    "minMoveY": 0,
                    "maxMoveY": 0,
                    "minMoveZ": 0,
                    "maxMoveZ": 0,
                    "speedZoomMaxSpeed": 1e+010,
                    "speedZoomMaxFOV": 0
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Turrets\MainTurret\OpticsIn\Medium_TI,
                "Medium_TI": {
                    "gunnerOpticsModel": "rhsusf|addons|rhsusf_m1a1|gunnerOptics_M1A2_2",
                    "initFov": 0.0538462,
                    "minFov": 0.0538462,
                    "maxFov": 0.0538462,
                    "visionMode": ["Ti"],
                    "hitpoint": "Hit_Optic_GPS_TI",
                    "initAngleX": 0,
                    "minAngleX": -30,
                    "maxAngleX": 30,
                    "initAngleY": 0,
                    "minAngleY": -100,
                    "maxAngleY": 100,
                    "thermalMode": [2,3],
                    "minMoveX": 0,
                    "maxMoveX": 0,
                    "minMoveY": 0,
                    "maxMoveY": 0,
                    "minMoveZ": 0,
                    "maxMoveZ": 0,
                    "speedZoomMaxSpeed": 1e+010,
                    "speedZoomMaxFOV": 0
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Turrets\MainTurret\OpticsIn\Medium2_TI,
                "Medium2_TI": {
                    "gunnerOpticsModel": "rhsusf|addons|rhsusf_m1a1|gunnerOptics_M1A2_3",
                    "initFov": 0.028,
                    "minFov": 0.028,
                    "maxFov": 0.028,
                    "visionMode": ["Ti"],
                    "hitpoint": "Hit_Optic_GPS_TI",
                    "initAngleX": 0,
                    "minAngleX": -30,
                    "maxAngleX": 30,
                    "initAngleY": 0,
                    "minAngleY": -100,
                    "maxAngleY": 100,
                    "thermalMode": [2,3],
                    "minMoveX": 0,
                    "maxMoveX": 0,
                    "minMoveY": 0,
                    "maxMoveY": 0,
                    "minMoveZ": 0,
                    "maxMoveZ": 0,
                    "speedZoomMaxSpeed": 1e+010,
                    "speedZoomMaxFOV": 0
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Turrets\MainTurret\OpticsIn\Narrow_TI,
                "Narrow_TI": {
                    "gunnerOpticsModel": "rhsusf|addons|rhsusf_m1a1|gunnerOptics_M1A2_4",
                    "initFov": 0.014,
                    "minFov": 0.014,
                    "maxFov": 0.014,
                    "visionMode": ["Ti"],
                    "hitpoint": "Hit_Optic_GPS_TI",
                    "initAngleX": 0,
                    "minAngleX": -30,
                    "maxAngleX": 30,
                    "initAngleY": 0,
                    "minAngleY": -100,
                    "maxAngleY": 100,
                    "thermalMode": [2,3],
                    "minMoveX": 0,
                    "maxMoveX": 0,
                    "minMoveY": 0,
                    "maxMoveY": 0,
                    "minMoveZ": 0,
                    "maxMoveZ": 0,
                    "speedZoomMaxSpeed": 1e+010,
                    "speedZoomMaxFOV": 0
                }
            },
            "gunnerAction": "mbt2_slot2a_out",
            "gunnerInAction": "RHS_M1A1_Gunner",
            "gunnerDoor": "hatchC",
            "forceHideGunner": 1,
            "inGunnerMayFire": 1,
            "viewGunnerInExternal": 1,
            "startEngine": 0,
            "LodTurnedOut": 0,
            # Class: CfgVehicles\rhsusf_m1a1tank_base\Turrets\MainTurret\HitPoints,
            "HitPoints": {
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Turrets\MainTurret\HitPoints\HitTurret
                "HitTurret": {
                    "armor": -160,
                    "name": "vez",
                    "armorComponent": "Hit_Turret",
                    "visual": "vez",
                    "passThrough": 0,
                    "minimalHit": -0.24,
                    "explosionShielding": 0.001,
                    "radius": 0.18,
                    "isTurret": 1
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Turrets\MainTurret\HitPoints\HitGun,
                "HitGun": {
                    "armor": -160,
                    "name": "zbran",
                    "armorComponent": "Hit_Gun",
                    "visual": "-",
                    "passThrough": 0,
                    "minimalHit": -0.15,
                    "explosionShielding": 0,
                    "radius": 0.12,
                    "isGun": 1
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Turrets\MainTurret\HitPoints\Hit_GPS_HeadMirror,
                "Hit_GPS_HeadMirror": {
                    "armor": -40,
                    "explosionShielding": 0,
                    "name": "",
                    "visual": "-",
                    "armorComponent": "Hit_HeadMirror",
                    "passThrough": 0
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Turrets\MainTurret\HitPoints\Hit_GPS_Optical,
                "Hit_GPS_Optical": {
                    "visual": "vis_optic_GPS",
                    "armorComponent": "Hit_Optic_GPS",
                    "armor": -40,
                    "explosionShielding": 0,
                    "name": "",
                    "passThrough": 0
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Turrets\MainTurret\HitPoints\Hit_GPS_TIS,
                "Hit_GPS_TIS": {
                    "visual": "vis_optic_GPS_TI",
                    "armorComponent": "Hit_Optic_GPS_TI",
                    "armor": -40,
                    "explosionShielding": 0,
                    "name": "",
                    "passThrough": 0
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Turrets\MainTurret\HitPoints\Hit_Optic_GPS,
                "Hit_Optic_GPS": {
                    "visual": "-",
                    "armorComponent": "-",
                    "depends": "Hit_GPS_HeadMirror max Hit_GPS_Optical",
                    "armor": -40,
                    "explosionShielding": 0,
                    "name": "",
                    "passThrough": 0
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\Turrets\MainTurret\HitPoints\Hit_Optic_GPS_TI,
                "Hit_Optic_GPS_TI": {
                    "visual": "-",
                    "armorComponent": "-",
                    "depends": "Hit_GPS_HeadMirror max Hit_GPS_TIS",
                    "armor": -40,
                    "explosionShielding": 0,
                    "name": "",
                    "passThrough": 0
                }
            },
            # Class: CfgVehicles\MBT_01_base_F\Turrets\MainTurret\ViewGunner,
            "ViewGunner": {
                "initAngleX": -17,
                "initAngleY": 0,
                "initFov": 0.9,
                "minFov": 0.25,
                "maxFov": 1.25,
                "minAngleX": -65,
                "maxAngleX": 85,
                "minAngleY": -150,
                "maxAngleY": 150,
                "minMoveX": 0,
                "maxMoveX": 0,
                "minMoveY": 0,
                "maxMoveY": 0,
                "minMoveZ": 0,
                "maxMoveZ": 0,
                "continuous": 0,
                "speedZoomMaxSpeed": 1e+010,
                "speedZoomMaxFOV": 0
            },
            "usePip": 2,
            "LODTurnedIn": 1100,
            "LODOpticsIn": 0,
            "animationSourceStickX": "turret_control_x",
            "animationSourceStickY": "turret_control_y",
            "gunnerLeftHandAnimName": "turret_control_y",
            "gunnerRightHandAnimName": "turret_control_y",
            "viewGunnerShadowAmb": 0.5,
            "viewGunnerShadowDiff": 0.05,
            "gunnerGetInAction": "GetInLow",
            "gunnerGetOutAction": "GetOutLow",
            "soundServoVertical": ["A3|Sounds_F|vehicles|armor|noises|servo_armor_gunner_vertical",0.158489,1,50],
            "discreteDistanceInitIndex": 5,
            "commanding": 1,
            "gunnerOpticsModel": "A3|weapons_f|reticle|optics_empty",
            "primaryGunner": 1,
            # Class: CfgVehicles\Tank_F\Turrets\MainTurret\Components,
            "Components": {
                # Class: CfgVehicles\Tank_F\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentLeft
                "VehicleSystemsDisplayManagerComponentLeft": {
                    # Class: VehicleSystemsTemplateLeftGunner\Components
                    "Components": {
                        # Class: VehicleSystemsTemplateLeftGunner\Components\VehicleDriverDisplay
                        "VehicleDriverDisplay": {
                            "componentType": "TransportFeedDisplayComponent",
                            "source": "Driver"
                        },
                        # Class: VehicleSystemsTemplateLeftGunner\Components\VehicleCommanderDisplay,
                        "VehicleCommanderDisplay": {
                            "componentType": "TransportFeedDisplayComponent",
                            "source": "Commander"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\EmptyDisplay,
                        "EmptyDisplay": {
                            "componentType": "EmptyDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\MinimapDisplay,
                        "MinimapDisplay": {
                            "componentType": "MinimapDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\MineDetectorDisplay,
                        "MineDetectorDisplay": {
                            "componentType": "MineDetectorDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\CrewDisplay,
                        "CrewDisplay": {
                            "componentType": "CrewDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\UAVDisplay,
                        "UAVDisplay": {
                            "componentType": "UAVFeedDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\SlingLoadDisplay,
                        "SlingLoadDisplay": {
                            "componentType": "SlingLoadDisplayComponent"
                        }
                    },
                    "componentType": "VehicleSystemsDisplayManager",
                    "left": 1,
                    "defaultDisplay": "EmptyDisplay",
                    "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,	(safezoneX + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40))])",
                    "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                },
                # Class: CfgVehicles\Tank_F\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentRight,
                "VehicleSystemsDisplayManagerComponentRight": {
                    # Class: VehicleSystemsTemplateRightGunner\Components
                    "Components": {
                        # Class: VehicleSystemsTemplateRightGunner\Components\VehicleDriverDisplay
                        "VehicleDriverDisplay": {
                            "componentType": "TransportFeedDisplayComponent",
                            "source": "Driver"
                        },
                        # Class: VehicleSystemsTemplateRightGunner\Components\VehicleCommanderDisplay,
                        "VehicleCommanderDisplay": {
                            "componentType": "TransportFeedDisplayComponent",
                            "source": "Commander"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerRight\Components\EmptyDisplay,
                        "EmptyDisplay": {
                            "componentType": "EmptyDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerRight\Components\MinimapDisplay,
                        "MinimapDisplay": {
                            "componentType": "MinimapDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerRight\Components\MineDetectorDisplay,
                        "MineDetectorDisplay": {
                            "componentType": "MineDetectorDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerRight\Components\CrewDisplay,
                        "CrewDisplay": {
                            "componentType": "CrewDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerRight\Components\UAVDisplay,
                        "UAVDisplay": {
                            "componentType": "UAVFeedDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerRight\Components\SlingLoadDisplay,
                        "SlingLoadDisplay": {
                            "componentType": "SlingLoadDisplayComponent"
                        }
                    },
                    "componentType": "VehicleSystemsDisplayManager",
                    "right": 1,
                    "defaultDisplay": "EmptyDisplay",
                    "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,	((safezoneX + safezoneW) - (		(10 * 			(			((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40)))])",
                    "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                }
            },
            "body": "mainTurret",
            "gun": "mainGun",
            "animationSourceBody": "mainTurret",
            "animationSourceGun": "mainGun",
            "animationSourceCamElev": "camElev",
            "proxyType": "CPGunner",
            "proxyIndex": 1,
            "gunnerName": "Gunner",
            "gunnerType": "",
            "primaryObserver": 0,
            "soundElevation": ["",0.00316228,1],
            "minTurn": -360,
            "maxTurn": 360,
            "initTurn": 0,
            "minOutElev": -4,
            "maxOutElev": 20,
            "initOutElev": 0,
            "minOutTurn": -60,
            "maxOutTurn": 60,
            "initOutTurn": 0,
            "minCamElev": -90,
            "maxCamElev": 90,
            "initCamElev": 0,
            "stabilizedInAxes": 3,
            "primary": 1,
            "hasGunner": 1,
            "turretCanSee": 0,
            # Class: CfgVehicles\AllVehicles\NewTurret\TurretSpec,
            "TurretSpec": {
                "showHeadPhones": 0
            },
            "gunnerOpticsColor": [0,0,0,1],
            "gunnerOpticsShowCursor": 0,
            "gunnerOutOpticsColor": [0,0,0,1],
            "memoryPointGunnerOutOptics": "",
            "gunnerOutForceOptics": 0,
            "gunnerOutOpticsShowCursor": 0,
            "gunnerFireAlsoInInternalCamera": 1,
            "gunnerOutFireAlsoInInternalCamera": 1,
            "gunnerUsesPilotView": 0,
            "castGunnerShadow": 0,
            "viewGunnerShadow": 1,
            "ejectDeadGunner": 0,
            "hideWeaponsGunner": 1,
            "canHideGunner": -1,
            "outGunnerMayFire": 0,
            "showHMD": 0,
            "lockWhenVehicleSpeed": -1,
            "gunnerCompartments": "Compartment1",
            "memoryPointsGetInGunnerPrecise": "",
            "missileBeg": "spice rakety",
            "missileEnd": "konec rakety",
            "armorLights": 0.4,
            # Class: CfgVehicles\AllVehicles\NewTurret\Reflectors,
            "Reflectors": {
            },
            "aggregateReflectors": [],
            # Class: CfgVehicles\AllVehicles\NewTurret\GunFire,
            "GunFire": {
                "access": 0,
                "cloudletDuration": 0.2,
                "cloudletAnimPeriod": 1,
                "cloudletSize": 1,
                "cloudletAlpha": 1,
                "cloudletGrowUp": 0.2,
                "cloudletFadeIn": 0.01,
                "cloudletFadeOut": 0.5,
                "cloudletAccY": 0,
                "cloudletMinYSpeed": -100,
                "cloudletMaxYSpeed": 100,
                "cloudletShape": "cloudletFire",
                "cloudletColor": [1,1,1,0],
                "interval": 0.01,
                "size": 3,
                "sourceSize": 0.5,
                "timeToLive": 0,
                "initT": 4500,
                "deltaT": -3000,
                # Class: WeaponFireGun\Table,
                "Table": {
                    # Class: WeaponFireGun\Table\T0
                    "T0": {
                        "maxT": 0,
                        "color": [0.82,0.95,0.93,0]
                    },
                    # Class: WeaponFireGun\Table\T1,
                    "T1": {
                        "maxT": 200,
                        "color": [0.75,0.77,0.9,0]
                    },
                    # Class: WeaponFireGun\Table\T2,
                    "T2": {
                        "maxT": 400,
                        "color": [0.56,0.62,0.67,0]
                    },
                    # Class: WeaponFireGun\Table\T3,
                    "T3": {
                        "maxT": 600,
                        "color": [0.39,0.46,0.47,0]
                    },
                    # Class: WeaponFireGun\Table\T4,
                    "T4": {
                        "maxT": 800,
                        "color": [0.24,0.31,0.31,0]
                    },
                    # Class: WeaponFireGun\Table\T5,
                    "T5": {
                        "maxT": 1000,
                        "color": [0.23,0.31,0.29,0]
                    },
                    # Class: WeaponFireGun\Table\T6,
                    "T6": {
                        "maxT": 1500,
                        "color": [0.21,0.29,0.27,0]
                    },
                    # Class: WeaponFireGun\Table\T7,
                    "T7": {
                        "maxT": 2000,
                        "color": [0.19,0.23,0.21,0]
                    },
                    # Class: WeaponFireGun\Table\T8,
                    "T8": {
                        "maxT": 2300,
                        "color": [0.22,0.19,0.1,0]
                    },
                    # Class: WeaponFireGun\Table\T9,
                    "T9": {
                        "maxT": 2500,
                        "color": [0.35,0.2,0.02,0]
                    },
                    # Class: WeaponFireGun\Table\T10,
                    "T10": {
                        "maxT": 2600,
                        "color": [0.62,0.29,0.03,0]
                    },
                    # Class: WeaponFireGun\Table\T11,
                    "T11": {
                        "maxT": 2650,
                        "color": [0.59,0.35,0.05,0]
                    },
                    # Class: WeaponFireGun\Table\T12,
                    "T12": {
                        "maxT": 2700,
                        "color": [0.75,0.37,0.03,0]
                    },
                    # Class: WeaponFireGun\Table\T13,
                    "T13": {
                        "maxT": 2750,
                        "color": [0.88,0.34,0.03,0]
                    },
                    # Class: WeaponFireGun\Table\T14,
                    "T14": {
                        "maxT": 2800,
                        "color": [0.91,0.5,0.17,0]
                    },
                    # Class: WeaponFireGun\Table\T15,
                    "T15": {
                        "maxT": 2850,
                        "color": [1,0.6,0.2,0]
                    },
                    # Class: WeaponFireGun\Table\T16,
                    "T16": {
                        "maxT": 2900,
                        "color": [1,0.71,0.3,0]
                    },
                    # Class: WeaponFireGun\Table\T17,
                    "T17": {
                        "maxT": 2950,
                        "color": [0.98,0.83,0.41,0]
                    },
                    # Class: WeaponFireGun\Table\T18,
                    "T18": {
                        "maxT": 3000,
                        "color": [0.98,0.91,0.54,0]
                    },
                    # Class: WeaponFireGun\Table\T19,
                    "T19": {
                        "maxT": 3100,
                        "color": [0.98,0.99,0.6,0]
                    },
                    # Class: WeaponFireGun\Table\T20,
                    "T20": {
                        "maxT": 3300,
                        "color": [0.96,0.99,0.72,0]
                    },
                    # Class: WeaponFireGun\Table\T21,
                    "T21": {
                        "maxT": 3600,
                        "color": [1,0.98,0.91,0]
                    },
                    # Class: WeaponFireGun\Table\T22,
                    "T22": {
                        "maxT": 4200,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles\AllVehicles\NewTurret\GunClouds,
            "GunClouds": {
                "access": 0,
                "cloudletDuration": 0.3,
                "cloudletAnimPeriod": 1,
                "cloudletSize": 1,
                "cloudletAlpha": 1,
                "cloudletGrowUp": 1,
                "cloudletFadeIn": 0.01,
                "cloudletFadeOut": 1,
                "cloudletAccY": 0.4,
                "cloudletMinYSpeed": 0.2,
                "cloudletMaxYSpeed": 0.8,
                "cloudletShape": "cloudletClouds",
                "cloudletColor": [1,1,1,0],
                "interval": 0.05,
                "size": 3,
                "sourceSize": 0.5,
                "timeToLive": 0,
                "initT": 0,
                "deltaT": 0,
                # Class: WeaponCloudsGun\Table,
                "Table": {
                    # Class: WeaponCloudsGun\Table\T0
                    "T0": {
                        "maxT": 0,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles\AllVehicles\NewTurret\MGunClouds,
            "MGunClouds": {
                "access": 0,
                "cloudletGrowUp": 0.05,
                "cloudletFadeIn": 0,
                "cloudletFadeOut": 0.1,
                "cloudletDuration": 0.05,
                "cloudletAnimPeriod": 1,
                "cloudletSize": 1,
                "cloudletAlpha": 0.3,
                "cloudletAccY": 0,
                "cloudletMinYSpeed": -100,
                "cloudletMaxYSpeed": 100,
                "cloudletShape": "cloudletClouds",
                "cloudletColor": [1,1,1,0],
                "timeToLive": 0,
                "interval": 0.02,
                "size": 0.3,
                "sourceSize": 0.02,
                "initT": 0,
                "deltaT": 0,
                # Class: WeaponCloudsMGun\Table,
                "Table": {
                    # Class: WeaponCloudsMGun\Table\T0
                    "T0": {
                        "maxT": 0,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles\AllVehicles\NewTurret\ViewOptics,
            "ViewOptics": {
                "initAngleX": 0,
                "minAngleX": -30,
                "maxAngleX": 30,
                "initAngleY": 0,
                "minAngleY": -100,
                "maxAngleY": 100,
                "initFov": 0.3,
                "minFov": 0.07,
                "maxFov": 0.35,
                "minMoveX": 0,
                "maxMoveX": 0,
                "minMoveY": 0,
                "maxMoveY": 0,
                "minMoveZ": 0,
                "maxMoveZ": 0,
                "speedZoomMaxSpeed": 1e+010,
                "speedZoomMaxFOV": 0
            },
            "forceNVG": 0,
            "isCopilot": 0,
            "canEject": 1,
            "gunnerLeftLegAnimName": "",
            "gunnerRightLegAnimName": "",
            "preciseGetInOut": 0,
            "turretFollowFreeLook": 0,
            "showAllTargets": 0,
            "dontCreateAI": 0,
            "disableSoundAttenuation": 0,
            "slingLoadOperator": 0,
            "playerPosition": 0,
            "allowLauncherIn": 0,
            "allowLauncherOut": 0,
            # Class: CfgVehicles\AllVehicles\NewTurret\TurnOut,
            "TurnOut": {
                "turnOffset": 0
            }
        }
    },
    # Class: CfgVehicles\rhsusf_m1a1fep_d\Damage,
    "Damage": {
        "tex": [],
        "mat": ["rhsusf|addons|rhsusf_m1a1|data|rhsusf_m1a1aim_01.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_dam_m1a1aim_01.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_destr_m1a1aim_01.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_m1a1aim_02.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_dam_m1a1aim_02.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_destr_m1a1aim_02.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_m1a1fep_od_01.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_dam_m1a1fep_od_01.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_destr_m1a1aim_01.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_m1a1fep_od_02.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_dam_m1a1fep_od_02.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_destr_m1a1aim_02.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_m1a1aim_03.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_dam_m1a1aim_03.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_destr_m1a1aim_03.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_m1a1aim_d_01.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_dam_m1a1aim_d_01.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_destr_m1a1aim_d_01.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_m1a1aim_d_02.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_dam_m1a1aim_d_02.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_destr_m1a1aim_d_02.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_m1a1aim_d_03.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_dam_m1a1aim_d_03.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_destr_m1a1aim_d_03.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_m1a1aimtusk_d_01.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_dam_m1a1aimtusk_d_01.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_destr_m1a1aimtusk_d_01.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_m1a1aimtusk_d_02.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_dam_m1a1aimtusk_d_02.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_destr_m1a1aimtusk_d_02.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_m1a1aimtusk_wd_01.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_dam_m1a1aimtusk_wd_01.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_destr_m1a1aimtusk_wd_01.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_m1a1aimtusk_wd_02.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_dam_m1a1aimtusk_wd_02.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_destr_m1a1aimtusk_wd_02.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_m1a1aim_t.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_dam_m1a1aim_t.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_destr_m1a1aim_t.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_tuski_d.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_dam_tuski_d.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_destr_tuski_d.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_tuski_wd.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_dam_tuski_wd.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_destr_tuski_wd.rvmat","a3|data_f|default.rvmat","a3|data_f|default.rvmat","a3|data_f|default_destruct.rvmat","rhsusf|addons|rhsusf_m1a1|data|opticsglass.rvmat","rhsusf|addons|rhsusf_m1a1|data|opticsglass_damage.rvmat","rhsusf|addons|rhsusf_m1a1|data|opticsglass_damage.rvmat"]
    },
    # Class: CfgVehicles\rhsusf_m1a1fep_d\HitPoints,
    "HitPoints": {
        # Class: CfgVehicles\rhsusf_m1a1fep_d\HitPoints\HitDuke1
        "HitDuke1": {
            "armor": 0.75,
            "material": -1,
            "name": "duke1",
            "visual": "-",
            "passThrough": 0,
            "MinimalHit": 0.05,
            "explosionShielding": 0.01,
            "radius": 0.15
        },
        # Class: CfgVehicles\rhsusf_m1a1fep_d\HitPoints\HitDuke2,
        "HitDuke2": {
            "name": "duke2",
            "visual": "-",
            "armor": 0.75,
            "material": -1,
            "passThrough": 0,
            "MinimalHit": 0.05,
            "explosionShielding": 0.01,
            "radius": 0.15
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\HitPoints\Armor_Composite_40,
        "Armor_Composite_40": {
            "armor": 999,
            "material": -1,
            "name": "Armor_CE_40_Hit",
            "armorComponent": "Armor_CE_40",
            "simulation": "RHS_Composite_40",
            "passThrough": 0,
            "minimalHit": 1,
            "explosionShielding": 0,
            "radius": 0.001,
            "visual": "-"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\HitPoints\Armor_Composite_50,
        "Armor_Composite_50": {
            "armor": 999,
            "material": -1,
            "name": "Armor_CE_50_Hit",
            "armorComponent": "Armor_CE_50",
            "simulation": "RHS_Composite_50",
            "passThrough": 0,
            "minimalHit": 1,
            "explosionShielding": 0,
            "radius": 0.001,
            "visual": "-"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\HitPoints\Armor_Composite_60,
        "Armor_Composite_60": {
            "armor": 999,
            "material": -1,
            "name": "Armor_CE_60_Hit",
            "armorComponent": "Armor_CE_60",
            "simulation": "RHS_Composite_60",
            "passThrough": 0,
            "minimalHit": 1,
            "explosionShielding": 0,
            "radius": 0.001,
            "visual": "-"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\HitPoints\Armor_Composite_80,
        "Armor_Composite_80": {
            "armor": 999,
            "material": -1,
            "name": "Armor_CE_80_Hit",
            "armorComponent": "Armor_CE_80",
            "simulation": "RHS_Composite_80",
            "passThrough": 0,
            "minimalHit": 1,
            "explosionShielding": 0,
            "radius": 0.001,
            "visual": "-"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\HitPoints\Armor_Composite_85,
        "Armor_Composite_85": {
            "armor": 999,
            "material": -1,
            "name": "Armor_CE_85_Hit",
            "armorComponent": "Armor_CE_85",
            "simulation": "RHS_Composite_85",
            "passThrough": 0,
            "minimalHit": 1,
            "explosionShielding": 0,
            "radius": 0.001,
            "visual": "-"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\HitPoints\HitFuelTank_Left,
        "HitFuelTank_Left": {
            "armor": -80,
            "material": -1,
            "name": "Hit_FuelTank_Left",
            "armorComponent": "Hit_FuelTank_Left",
            "visual": "-",
            "passThrough": 0,
            "minimalHit": -0.2,
            "explosionShielding": 0,
            "radius": 0.1
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\HitPoints\HitFuelTank_Right,
        "HitFuelTank_Right": {
            "name": "Hit_FuelTank_Right",
            "armorComponent": "Hit_FuelTank_Right",
            "armor": -80,
            "material": -1,
            "visual": "-",
            "passThrough": 0,
            "minimalHit": -0.2,
            "explosionShielding": 0,
            "radius": 0.1
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\HitPoints\HitFuel,
        "HitFuel": {
            "armor": 999,
            "material": -1,
            "name": "Hit_Fuel",
            "visual": "-",
            "passThrough": 0,
            "minimalHit": 1,
            "explosionShielding": 0,
            "radius": 0.01,
            "depends": "(HitFuelTank_Left+HitFuelTank_Right)*0.5"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\HitPoints\HitAmmoHull,
        "HitAmmoHull": {
            "name": "Hit_AmmoHull",
            "armorComponent": "Hit_AmmoHull",
            "armor": -100,
            "material": -1,
            "passThrough": 0,
            "minimalHit": 0.14,
            "explosionShielding": 0,
            "radius": 0.15
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\HitPoints\HitAmmo,
        "HitAmmo": {
            "name": "Hit_Ammo",
            "armorComponent": "Hit_AmmoTurret",
            "armor": -100,
            "material": -1,
            "passThrough": 0,
            "minimalHit": 0.14,
            "explosionShielding": 0,
            "radius": 0.15
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\HitPoints\HitHull,
        "HitHull": {
            "armor": 0.8,
            "material": -1,
            "name": "Hit_Hull",
            "visual": "zbytek",
            "passThrough": 0,
            "minimalHit": 0.14,
            "explosionShielding": 0,
            "radius": 0.21,
            "depends": "(HitAmmo factor [0.9,1])+(HitAmmoHull factor [0.9,1])",
            "armorComponent": "hit_hull"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\HitPoints\HitEngine,
        "HitEngine": {
            "armor": -100,
            "material": -1,
            "name": "Hit_Engine",
            "armorComponent": "Hit_Engine",
            "visual": "zbytek",
            "passThrough": 0,
            "minimalHit": 0.14,
            "explosionShielding": 0.01,
            "radius": 0.18,
            # Class: CfgVehicles\rhsusf_m1a1tank_base\HitPoints\HitEngine\DestructionEffects,
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\rhsusf_m1a1tank_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Smoke,
                "RHS_Engine_Smoke": {
                    "simulation": "particles",
                    "type": "SmallWreckSmoke",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Fire,
                "RHS_Engine_Fire": {
                    "type": "SmallFireFPlace",
                    "simulation": "particles",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Sparks,
                "RHS_Engine_Sparks": {
                    "type": "RHS_FireSparks",
                    "simulation": "particles",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Sounds,
                "RHS_Engine_Sounds": {
                    "simulation": "sound",
                    "type": "Fire",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Smoke_small1,
                "RHS_Engine_Smoke_small1": {
                    "type": "WeaponWreckSmoke",
                    "position": "engine_smoke2",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Smoke_small2,
                "RHS_Engine_Smoke_small2": {
                    "position": "engine_smoke3",
                    "type": "WeaponWreckSmoke",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\rhsusf_m1a1tank_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Smoke_small3,
                "RHS_Engine_Smoke_small3": {
                    "position": "engine_smoke4",
                    "type": "WeaponWreckSmoke",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                }
            }
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\HitPoints\HitLTrack,
        "HitLTrack": {
            "armor": -150,
            "armorComponent": "Hit_TrackL",
            "name": "Hit_TrackL",
            "passThrough": 0,
            "material": -1,
            "minimalHit": -0.25,
            "explosionShielding": 0.5,
            "radius": 0.3,
            "visual": "-"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\HitPoints\HitRTrack,
        "HitRTrack": {
            "armor": -150,
            "armorComponent": "Hit_TrackR",
            "name": "Hit_TrackR",
            "material": -1,
            "passThrough": 0,
            "minimalHit": -0.25,
            "explosionShielding": 0.5,
            "radius": 0.3,
            "visual": "-"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\HitPoints\Hit_Optic_Driver,
        "Hit_Optic_Driver": {
            "armor": -40,
            "explosionShielding": 0,
            "name": "",
            "visual": "vis_optic_Driver",
            "armorComponent": "Hit_Optic_Driver",
            "passThrough": 0
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\HitPoints\Hit_Optic_DVEA,
        "Hit_Optic_DVEA": {
            "visual": "vis_optic_DVEA",
            "armorComponent": "Hit_Optic_DVEA",
            "armor": -40,
            "explosionShielding": 0,
            "name": "",
            "passThrough": 0
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\HitPoints\Hit_Optic_Driver_Rear,
        "Hit_Optic_Driver_Rear": {
            "visual": "vis_optic_Driver_Rear",
            "armorComponent": "Hit_Optic_Driver_Rear",
            "armor": -40,
            "explosionShielding": 0,
            "name": "",
            "passThrough": 0
        }
    },
    # Class: CfgVehicles\rhsusf_m1a1fep_d\EventHandlers,
    "EventHandlers": {
        # Class: CfgVehicles\rhsusf_m1a1fep_d\EventHandlers\rhs_duke
        "rhs_duke": {
            "handleDamage": "_this call rhs_fnc_duke_destruction"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\EventHandlers\RHSUSF_EventHandlers,
        "RHSUSF_EventHandlers": {
            "init": "_this call RHS_fnc_M1_init",
            "engine": "[_this select 0,_this select 1,20] call rhs_fnc_engineStartupDelay"
        },
        "init": "",
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');",
        # Class: DefaultEventHandlers\RHS_DefaultEventhandlers,
        "RHS_DefaultEventhandlers": {
            "hitpart": "_this call rhs_fnc_hitPart"
        }
    },
    "category": "Armored",
    "destrType": "DestructDefault",
    "accuracy": 0.3,
    "picture": "rhsusf|addons|rhsusf_m1a1|icons|M1A1SIDE_ca.paa",
    "Icon": "rhsusf|addons|rhsusf_m1a1|icons|M1A1AIM.paa",
    "typicalCargo": [],
    "side": 1,
    "unitInfoType": "RHSUSF_RscUnitInfoWestTank",
    "driverOpticsModel": "rhsusf|addons|rhsusf_optics|data|rhs_m1_triplex",
    "getInAction": "GetInLow",
    "getOutAction": "GetOutLow",
    "cargoGetInAction": ["GetInLow"],
    "cargoGetOutAction": ["GetOutLow"],
    "cargoAction": ["passenger_flatground_leanleft"],
    "transportSoldier": 0,
    "weapons": ["rhs_weap_smokegen"],
    "magazines": ["rhs_mag_smokegen"],
    "simulation": "tankX",
    "normalSpeedForwardCoef": 0.6,
    "slowSpeedForwardCoef": 0.45,
    "fuelCapacity": 20,
    "maxSpeed": 66,
    "tankTurnForce": 750000,
    "tankTurnForceAngMinSpd": 0.7,
    "tankTurnForceAngSpd": 0.72,
    "accelAidForceCoef": 3.5,
    "accelAidForceYOffset": -3,
    "accelAidForceSpd": 2.83,
    "maxFordingDepth": 0,
    "waterResistance": 0,
    "waterDamageEngine": 0.2,
    "waterLeakiness": 10,
    "torqueCurve": [[0.333333,1],[1,0.701027]],
    "engineMOI": 15,
    "enginePower": 1120,
    "peakTorque": 5355,
    "minOmega": 100,
    "maxOmega": 314.16,
    "idleRPM": 1000,
    "redRPM": 3000,
    "antiRollbarForceCoef": 24,
    "antiRollbarForceLimit": 42,
    "antiRollbarSpeedMin": 30,
    "antiRollbarSpeedMax": 75,
    "thrustDelay": 0,
    "clutchStrength": 35,
    "engineLosses": 25,
    "transmissionLosses": 15,
    "latency": 1.3,
    "switchTime": 0,
    "changeGearType": "rpmratio",
    "changeGearOmegaRatios": [1,0.333333,0.333333,0,0.993333,0.333333,0.993333,0.633333,0.983333,0.733333,0.983333,0.766667,0.983333,0.733333],
    # Class: CfgVehicles\rhsusf_m1a1tank_base\complexGearbox,
    "complexGearbox": {
        "GearboxRatios": ["R1",-1.67,"N",0,"D1",4.85,"D2",2.65,"D3",1.48,"D4",1,"D5",0.79],
        "TransmissionRatios": ["High",12],
        "gearBoxMode": "auto",
        "moveOffGear": 1,
        "driveString": "D",
        "neutralString": "N",
        "reverseString": "R",
        "transmissionDelay": 0.1
    },
    # Class: CfgVehicles\rhsusf_m1a1tank_base\Wheels,
    "Wheels": {
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Wheels\L2
        "L2": {
            "suspTravelDirection": [-0.125,-1,0],
            "boneName": "wheel_podkoloL1",
            "center": "wheel_1_2_axis",
            "boundary": "wheel_1_2_bound",
            "side": "left",
            "steering": 0,
            "width": 0.477,
            "mass": 150,
            "MOI": 10.83,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "maxBrakeTorque": 9000,
            "sprungMass": 4642.86,
            "springStrength": 584000,
            "springDamperRate": 15000,
            "dampingRate": 205,
            "dampingRateInAir": 205,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 60000,
            "frictionVsSlipGraph": [[0,0.75],[0.18,1],[0.7,0.5]]
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Wheels\L3,
        "L3": {
            "boneName": "wheel_podkolol2",
            "center": "wheel_1_3_axis",
            "boundary": "wheel_1_3_bound",
            "suspTravelDirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.477,
            "mass": 150,
            "MOI": 10.83,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "maxBrakeTorque": 9000,
            "sprungMass": 4642.86,
            "springStrength": 584000,
            "springDamperRate": 15000,
            "dampingRate": 205,
            "dampingRateInAir": 205,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 60000,
            "frictionVsSlipGraph": [[0,0.75],[0.18,1],[0.7,0.5]]
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Wheels\L4,
        "L4": {
            "boneName": "wheel_podkolol3",
            "center": "wheel_1_4_axis",
            "boundary": "wheel_1_4_bound",
            "suspTravelDirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.477,
            "mass": 150,
            "MOI": 10.83,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "maxBrakeTorque": 9000,
            "sprungMass": 4642.86,
            "springStrength": 584000,
            "springDamperRate": 15000,
            "dampingRate": 205,
            "dampingRateInAir": 205,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 60000,
            "frictionVsSlipGraph": [[0,0.75],[0.18,1],[0.7,0.5]]
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Wheels\L5,
        "L5": {
            "boneName": "wheel_podkolol4",
            "center": "wheel_1_5_axis",
            "boundary": "wheel_1_5_bound",
            "suspTravelDirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.477,
            "mass": 150,
            "MOI": 10.83,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "maxBrakeTorque": 9000,
            "sprungMass": 4642.86,
            "springStrength": 584000,
            "springDamperRate": 15000,
            "dampingRate": 205,
            "dampingRateInAir": 205,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 60000,
            "frictionVsSlipGraph": [[0,0.75],[0.18,1],[0.7,0.5]]
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Wheels\L6,
        "L6": {
            "boneName": "wheel_podkolol5",
            "center": "wheel_1_6_axis",
            "boundary": "wheel_1_6_bound",
            "suspTravelDirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.477,
            "mass": 150,
            "MOI": 10.83,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "maxBrakeTorque": 9000,
            "sprungMass": 4642.86,
            "springStrength": 584000,
            "springDamperRate": 15000,
            "dampingRate": 205,
            "dampingRateInAir": 205,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 60000,
            "frictionVsSlipGraph": [[0,0.75],[0.18,1],[0.7,0.5]]
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Wheels\L7,
        "L7": {
            "boneName": "wheel_podkolol6",
            "center": "wheel_1_7_axis",
            "boundary": "wheel_1_7_bound",
            "suspTravelDirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.477,
            "mass": 150,
            "MOI": 10.83,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "maxBrakeTorque": 9000,
            "sprungMass": 4642.86,
            "springStrength": 584000,
            "springDamperRate": 15000,
            "dampingRate": 205,
            "dampingRateInAir": 205,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 60000,
            "frictionVsSlipGraph": [[0,0.75],[0.18,1],[0.7,0.5]]
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Wheels\L8,
        "L8": {
            "boneName": "wheel_podkolol7",
            "center": "wheel_1_8_axis",
            "boundary": "wheel_1_8_bound",
            "suspTravelDirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.477,
            "mass": 150,
            "MOI": 10.83,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "maxBrakeTorque": 9000,
            "sprungMass": 4642.86,
            "springStrength": 584000,
            "springDamperRate": 15000,
            "dampingRate": 205,
            "dampingRateInAir": 205,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 60000,
            "frictionVsSlipGraph": [[0,0.75],[0.18,1],[0.7,0.5]]
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Wheels\L9,
        "L9": {
            "boneName": "wheel_podkolol9",
            "center": "wheel_1_9_axis",
            "boundary": "wheel_1_9_bound",
            "maxDroop": 0,
            "maxCompression": 0,
            "suspTravelDirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.477,
            "mass": 150,
            "MOI": 10.83,
            "maxBrakeTorque": 9000,
            "sprungMass": 4642.86,
            "springStrength": 584000,
            "springDamperRate": 15000,
            "dampingRate": 205,
            "dampingRateInAir": 205,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 60000,
            "frictionVsSlipGraph": [[0,0.75],[0.18,1],[0.7,0.5]]
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Wheels\L1,
        "L1": {
            "boneName": "",
            "center": "wheel_1_1_axis",
            "boundary": "wheel_1_1_bound",
            "maxDroop": 0,
            "maxCompression": 0,
            "suspTravelDirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.477,
            "mass": 150,
            "MOI": 10.83,
            "maxBrakeTorque": 9000,
            "sprungMass": 4642.86,
            "springStrength": 584000,
            "springDamperRate": 15000,
            "dampingRate": 205,
            "dampingRateInAir": 205,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 60000,
            "frictionVsSlipGraph": [[0,0.75],[0.18,1],[0.7,0.5]]
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Wheels\R2,
        "R2": {
            "suspTravelDirection": [0.125,-1,0],
            "boneName": "wheel_podkolop1",
            "center": "wheel_2_2_axis",
            "boundary": "wheel_2_2_bound",
            "side": "right",
            "steering": 0,
            "width": 0.477,
            "mass": 150,
            "MOI": 10.83,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "maxBrakeTorque": 9000,
            "sprungMass": 4642.86,
            "springStrength": 584000,
            "springDamperRate": 15000,
            "dampingRate": 205,
            "dampingRateInAir": 205,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 60000,
            "frictionVsSlipGraph": [[0,0.75],[0.18,1],[0.7,0.5]]
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Wheels\R3,
        "R3": {
            "boneName": "wheel_podkolop2",
            "center": "wheel_2_3_axis",
            "boundary": "wheel_2_3_bound",
            "suspTravelDirection": [0.125,-1,0],
            "side": "right",
            "steering": 0,
            "width": 0.477,
            "mass": 150,
            "MOI": 10.83,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "maxBrakeTorque": 9000,
            "sprungMass": 4642.86,
            "springStrength": 584000,
            "springDamperRate": 15000,
            "dampingRate": 205,
            "dampingRateInAir": 205,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 60000,
            "frictionVsSlipGraph": [[0,0.75],[0.18,1],[0.7,0.5]]
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Wheels\R4,
        "R4": {
            "boneName": "wheel_podkolop3",
            "center": "wheel_2_4_axis",
            "boundary": "wheel_2_4_bound",
            "suspTravelDirection": [0.125,-1,0],
            "side": "right",
            "steering": 0,
            "width": 0.477,
            "mass": 150,
            "MOI": 10.83,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "maxBrakeTorque": 9000,
            "sprungMass": 4642.86,
            "springStrength": 584000,
            "springDamperRate": 15000,
            "dampingRate": 205,
            "dampingRateInAir": 205,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 60000,
            "frictionVsSlipGraph": [[0,0.75],[0.18,1],[0.7,0.5]]
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Wheels\R5,
        "R5": {
            "boneName": "wheel_podkolop4",
            "center": "wheel_2_5_axis",
            "boundary": "wheel_2_5_bound",
            "suspTravelDirection": [0.125,-1,0],
            "side": "right",
            "steering": 0,
            "width": 0.477,
            "mass": 150,
            "MOI": 10.83,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "maxBrakeTorque": 9000,
            "sprungMass": 4642.86,
            "springStrength": 584000,
            "springDamperRate": 15000,
            "dampingRate": 205,
            "dampingRateInAir": 205,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 60000,
            "frictionVsSlipGraph": [[0,0.75],[0.18,1],[0.7,0.5]]
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Wheels\R6,
        "R6": {
            "boneName": "wheel_podkolop5",
            "center": "wheel_2_6_axis",
            "boundary": "wheel_2_6_bound",
            "suspTravelDirection": [0.125,-1,0],
            "side": "right",
            "steering": 0,
            "width": 0.477,
            "mass": 150,
            "MOI": 10.83,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "maxBrakeTorque": 9000,
            "sprungMass": 4642.86,
            "springStrength": 584000,
            "springDamperRate": 15000,
            "dampingRate": 205,
            "dampingRateInAir": 205,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 60000,
            "frictionVsSlipGraph": [[0,0.75],[0.18,1],[0.7,0.5]]
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Wheels\R7,
        "R7": {
            "boneName": "wheel_podkolop6",
            "center": "wheel_2_7_axis",
            "boundary": "wheel_2_7_bound",
            "suspTravelDirection": [0.125,-1,0],
            "side": "right",
            "steering": 0,
            "width": 0.477,
            "mass": 150,
            "MOI": 10.83,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "maxBrakeTorque": 9000,
            "sprungMass": 4642.86,
            "springStrength": 584000,
            "springDamperRate": 15000,
            "dampingRate": 205,
            "dampingRateInAir": 205,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 60000,
            "frictionVsSlipGraph": [[0,0.75],[0.18,1],[0.7,0.5]]
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Wheels\R8,
        "R8": {
            "boneName": "wheel_podkolop7",
            "center": "wheel_2_8_axis",
            "boundary": "wheel_2_8_bound",
            "suspTravelDirection": [0.125,-1,0],
            "side": "right",
            "steering": 0,
            "width": 0.477,
            "mass": 150,
            "MOI": 10.83,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "maxBrakeTorque": 9000,
            "sprungMass": 4642.86,
            "springStrength": 584000,
            "springDamperRate": 15000,
            "dampingRate": 205,
            "dampingRateInAir": 205,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 60000,
            "frictionVsSlipGraph": [[0,0.75],[0.18,1],[0.7,0.5]]
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Wheels\R9,
        "R9": {
            "boneName": "wheel_podkolop9",
            "center": "wheel_2_9_axis",
            "boundary": "wheel_2_9_bound",
            "maxDroop": 0,
            "maxCompression": 0,
            "suspTravelDirection": [0.125,-1,0],
            "side": "right",
            "steering": 0,
            "width": 0.477,
            "mass": 150,
            "MOI": 10.83,
            "maxBrakeTorque": 9000,
            "sprungMass": 4642.86,
            "springStrength": 584000,
            "springDamperRate": 15000,
            "dampingRate": 205,
            "dampingRateInAir": 205,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 60000,
            "frictionVsSlipGraph": [[0,0.75],[0.18,1],[0.7,0.5]]
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Wheels\R1,
        "R1": {
            "boneName": "",
            "center": "wheel_2_1_axis",
            "boundary": "wheel_2_1_bound",
            "maxDroop": 0,
            "maxCompression": 0,
            "suspTravelDirection": [0.125,-1,0],
            "side": "right",
            "steering": 0,
            "width": 0.477,
            "mass": 150,
            "MOI": 10.83,
            "maxBrakeTorque": 9000,
            "sprungMass": 4642.86,
            "springStrength": 584000,
            "springDamperRate": 15000,
            "dampingRate": 205,
            "dampingRateInAir": 205,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 60000,
            "frictionVsSlipGraph": [[0,0.75],[0.18,1],[0.7,0.5]]
        }
    },
    "soundEngineOnInt": ["rhsusf|addons|rhsusf_m1a1|sounds|m1start",1.41254,1,200],
    "soundEngineOffInt": ["rhsusf|addons|rhsusf_m1a1|sounds|ABRAMS_engine_int_stop",1.41254,1,200],
    "soundEngineOnExt": ["rhsusf|addons|rhsusf_m1a1|sounds|m1start",3.16228,1,200],
    "soundEngineOffExt": ["rhsusf|addons|rhsusf_m1a1|sounds|ABRAMS_engine_ext_stop",3.16228,1,200],
    # Class: CfgVehicles\rhsusf_m1a1tank_base\Sounds,
    "Sounds": {
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Sounds\Idle_ext
        "Idle_ext": {
            "sound": ["rhsusf|addons|rhsusf_m1a1|sounds|ABRAMS_engine_ext_rpm1",2.81838,1,150],
            "frequency": "0.9	+	((rpm/	3000) factor[(850/	3000),(1200/	3000)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	3000) factor[(750/	3000),(990/	3000)])	*	((rpm/	3000) factor[(1100/	3000),(1000/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Sounds\Engine,
        "Engine": {
            "sound": ["rhsusf|addons|rhsusf_m1a1|sounds|ABRAMS_engine_int_rpm2",3.54813,1,200],
            "frequency": "0.8	+	((rpm/	3000) factor[(1000/	3000),(1400/	3000)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	3000) factor[(970/	3000),(1200/	3000)])	*	((rpm/	3000) factor[(1450/	3000),(1300/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Sounds\Engine1_ext,
        "Engine1_ext": {
            "sound": ["rhsusf|addons|rhsusf_m1a1|sounds|ABRAMS_engine_int_rpm3",2.81838,1,240],
            "frequency": "0.8	+		((rpm/	3000) factor[(1300/	3000),(1500/	3000)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	3000) factor[(1350/	3000),(1550/	3000)])	*	((rpm/	3000) factor[(2000/	3000),(1750/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Sounds\Engine2_ext,
        "Engine2_ext": {
            "sound": ["rhsusf|addons|rhsusf_m1a1|sounds|ABRAMS_engine_int_rpm4",2.51189,1,280],
            "frequency": "0.8	+	((rpm/	3000) factor[(1400/	3000),(1900/	3000)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	3000) factor[(1750/	3000),(2050/	3000)])	*	((rpm/	3000) factor[(2450/	3000),(2300/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Sounds\Engine3_ext,
        "Engine3_ext": {
            "sound": ["rhsusf|addons|rhsusf_m1a1|sounds|ABRAMS_engine_int_rpm5",2.23872,1,320],
            "frequency": "0.8	+	((rpm/	3000) factor[(2300/	3000),(2700/	3000)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	3000) factor[(2350/	3000),(2550/	3000)])	*	((rpm/	3000) factor[(2770/	3000),(2600/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Sounds\Engine4_ext,
        "Engine4_ext": {
            "sound": ["rhsusf|addons|rhsusf_m1a1|sounds|ABRAMS_engine_int_rpm6",1.99526,1,360],
            "frequency": "0.8	+	((rpm/	3000) factor[(2600/	3000),(3000/	3000)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	3000) factor[(2550/	3000),(2800/	3000)])	*	((rpm/	3000) factor[(3050/	3000),(2950/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Sounds\Engine5_ext,
        "Engine5_ext": {
            "sound": ["rhsusf|addons|rhsusf_m1a1|sounds|ABRAMS_engine_int_rpm7",1.77828,1,420],
            "frequency": "0.95	+	((rpm/	3000) factor[(2900/	3000),(3100/	3000)])*0.15",
            "volume": "engineOn*camPos*((rpm/	3000) factor[(2850/	3000),(3100/	3000)])"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Sounds\IdleThrust,
        "IdleThrust": {
            "sound": ["rhsusf|addons|rhsusf_m1a1|sounds|ABRAMS_exhaust_ext_rpm1",1.99526,1,200],
            "frequency": "0.9	+	((rpm/	3000) factor[(850/	3000),(1200/	3000)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	3000) factor[(750/	3000),(990/	3000)])	*	((rpm/	3000) factor[(1100/	3000),(1000/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Sounds\EngineThrust,
        "EngineThrust": {
            "sound": ["rhsusf|addons|rhsusf_m1a1|sounds|ABRAMS_exhaust_ext_rpm2",1.77828,1,250],
            "frequency": "0.8	+	((rpm/	3000) factor[(1000/	3000),(1400/	3000)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	3000) factor[(970/	3000),(1200/	3000)])	*	((rpm/	3000) factor[(1450/	3000),(1300/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Sounds\Engine1_Thrust_ext,
        "Engine1_Thrust_ext": {
            "sound": ["rhsusf|addons|rhsusf_m1a1|sounds|ABRAMS_exhaust_ext_rpm3",1.58489,1,280],
            "frequency": "0.8	+		((rpm/	3000) factor[(1300/	3000),(1500/	3000)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	3000) factor[(1350/	3000),(1550/	3000)])	*	((rpm/	3000) factor[(2000/	3000),(1750/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Sounds\Engine2_Thrust_ext,
        "Engine2_Thrust_ext": {
            "sound": ["rhsusf|addons|rhsusf_m1a1|sounds|ABRAMS_exhaust_ext_rpm4",1.41254,1,320],
            "frequency": "0.8	+	((rpm/	3000) factor[(1400/	3000),(1900/	3000)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	3000) factor[(1750/	3000),(2050/	3000)])	*	((rpm/	3000) factor[(2450/	3000),(2300/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Sounds\Engine3_Thrust_ext,
        "Engine3_Thrust_ext": {
            "sound": ["rhsusf|addons|rhsusf_m1a1|sounds|ABRAMS_exhaust_ext_rpm5",1.25893,1,360],
            "frequency": "0.8	+	((rpm/	3000) factor[(2300/	3000),(2700/	3000)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	3000) factor[(2350/	3000),(2550/	3000)])	*	((rpm/	3000) factor[(2770/	3000),(2600/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Sounds\Engine4_Thrust_ext,
        "Engine4_Thrust_ext": {
            "sound": ["rhsusf|addons|rhsusf_m1a1|sounds|ABRAMS_exhaust_ext_rpm6",1,1,400],
            "frequency": "0.8	+	((rpm/	3000) factor[(2600/	3000),(3000/	3000)])*0.3",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	3000) factor[(2550/	3000),(2800/	3000)])	*	((rpm/	3000) factor[(3050/	3000),(2950/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Sounds\Engine5_Thrust_ext,
        "Engine5_Thrust_ext": {
            "sound": ["rhsusf|addons|rhsusf_m1a1|sounds|ABRAMS_exhaust_ext_rpm7",1.25893,1,450],
            "frequency": "0.9	+	((rpm/	3000) factor[(2900/	3000),(3100/	3000)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*((rpm/	3000) factor[(2850/	3000),(3100/	3000)])"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Sounds\Idle_int,
        "Idle_int": {
            "sound": ["rhsusf|addons|rhsusf_m1a1|sounds|ABRAMS_engine_int_rpm2",2.81838,1],
            "frequency": "0.9	+	((rpm/	3000) factor[(850/	3000),(1200/	3000)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	3000) factor[(750/	3000),(990/	3000)])	*	((rpm/	3000) factor[(1100/	3000),(1000/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Sounds\Engine_int,
        "Engine_int": {
            "sound": ["rhsusf|addons|rhsusf_m1a1|sounds|ABRAMS_engine_int_rpm2",2.51189,1],
            "frequency": "0.8	+	((rpm/	3000) factor[(1000/	3000),(1400/	3000)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	3000) factor[(970/	3000),(1200/	3000)])	*	((rpm/	3000) factor[(1450/	3000),(1300/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Sounds\Engine1_int,
        "Engine1_int": {
            "sound": ["rhsusf|addons|rhsusf_m1a1|sounds|ABRAMS_engine_int_rpm2",2.51189,1],
            "frequency": "0.8	+		((rpm/	3000) factor[(1300/	3000),(1500/	3000)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	3000) factor[(1350/	3000),(1550/	3000)])	*	((rpm/	3000) factor[(2000/	3000),(1750/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Sounds\Engine2_int,
        "Engine2_int": {
            "sound": ["rhsusf|addons|rhsusf_m1a1|sounds|ABRAMS_engine_int_rpm2",2.23872,1],
            "frequency": "0.8	+	((rpm/	3000) factor[(1400/	3000),(1900/	3000)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	3000) factor[(1750/	3000),(2050/	3000)])	*	((rpm/	3000) factor[(2450/	3000),(2300/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Sounds\Engine3_int,
        "Engine3_int": {
            "sound": ["rhsusf|addons|rhsusf_m1a1|sounds|ABRAMS_engine_int_rpm2",1.99526,1],
            "frequency": "0.8	+	((rpm/	3000) factor[(2300/	3000),(2700/	3000)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	3000) factor[(2350/	3000),(2550/	3000)])	*	((rpm/	3000) factor[(2770/	3000),(2600/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Sounds\Engine4_int,
        "Engine4_int": {
            "sound": ["rhsusf|addons|rhsusf_m1a1|sounds|ABRAMS_engine_int_rpm2",1.77828,1],
            "frequency": "0.8	+	((rpm/	3000) factor[(2600/	3000),(3000/	3000)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	3000) factor[(2550/	3000),(2800/	3000)])	*	((rpm/	3000) factor[(3050/	3000),(2950/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Sounds\Engine5_int,
        "Engine5_int": {
            "sound": ["rhsusf|addons|rhsusf_m1a1|sounds|ABRAMS_engine_int_rpm3",1.77828,1],
            "frequency": "0.95	+	((rpm/	3000) factor[(2900/	3000),(3100/	3000)])*0.15",
            "volume": "engineOn*(1-camPos)*((rpm/	3000) factor[(2850/	3000),(3100/	3000)])"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Sounds\IdleThrust_int,
        "IdleThrust_int": {
            "sound": ["rhsusf|addons|rhsusf_m1a1|sounds|ABRAMS_exhaust_int_rpm1",1.99526,1],
            "frequency": "0.9	+	((rpm/	3000) factor[(850/	3000),(1200/	3000)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	3000) factor[(750/	3000),(990/	3000)])	*	((rpm/	3000) factor[(1100/	3000),(1000/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Sounds\EngineThrust_int,
        "EngineThrust_int": {
            "sound": ["rhsusf|addons|rhsusf_m1a1|sounds|ABRAMS_exhaust_int_rpm2",1.99526,1],
            "frequency": "0.8	+	((rpm/	3000) factor[(1000/	3000),(1400/	3000)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	3000) factor[(970/	3000),(1200/	3000)])	*	((rpm/	3000) factor[(1450/	3000),(1300/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Sounds\Engine1_Thrust_int,
        "Engine1_Thrust_int": {
            "sound": ["rhsusf|addons|rhsusf_m1a1|sounds|ABRAMS_exhaust_int_rpm3",1.77828,1],
            "frequency": "0.8	+		((rpm/	3000) factor[(1300/	3000),(1500/	3000)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	3000) factor[(1350/	3000),(1550/	3000)])	*	((rpm/	3000) factor[(2000/	3000),(1750/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Sounds\Engine2_Thrust_int,
        "Engine2_Thrust_int": {
            "sound": ["rhsusf|addons|rhsusf_m1a1|sounds|ABRAMS_exhaust_int_rpm4",1.58489,1],
            "frequency": "0.8	+	((rpm/	3000) factor[(1400/	3000),(1900/	3000)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	3000) factor[(1750/	3000),(2050/	3000)])	*	((rpm/	3000) factor[(2450/	3000),(2300/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Sounds\Engine3_Thrust_int,
        "Engine3_Thrust_int": {
            "sound": ["rhsusf|addons|rhsusf_m1a1|sounds|ABRAMS_exhaust_int_rpm5",1.41254,1],
            "frequency": "0.8	+	((rpm/	3000) factor[(2300/	3000),(2700/	3000)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	3000) factor[(2350/	3000),(2550/	3000)])	*	((rpm/	3000) factor[(2770/	3000),(2600/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Sounds\Engine4_Thrust_int,
        "Engine4_Thrust_int": {
            "sound": ["rhsusf|addons|rhsusf_m1a1|sounds|ABRAMS_exhaust_int_rpm6",1.41254,1],
            "frequency": "0.8	+	((rpm/	3000) factor[(2600/	3000),(3000/	3000)])*0.3",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	3000) factor[(2550/	3000),(2800/	3000)])	*	((rpm/	3000) factor[(3050/	3000),(2950/	3000)]))"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Sounds\Engine5_Thrust_int,
        "Engine5_Thrust_int": {
            "sound": ["rhsusf|addons|rhsusf_m1a1|sounds|ABRAMS_exhaust_int_rpm7",1.41254,1],
            "frequency": "0.9	+	((rpm/	3000) factor[(2900/	3000),(3100/	3000)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*((rpm/	3000) factor[(2850/	3000),(3100/	3000)])"
        },
        "soundSetsExt": ["RHSUSF_Abrams_ext_idle_SoundSet","RHSUSF_Abrams_ext_slow_SoundSet","RHSUSF_Abrams_ext_mid_SoundSet","RHSUSF_Abrams_ext_fast_SoundSet","RHSUSF_Abrams_exhaust_ext_idle_SoundSet","RHSUSF_Abrams_exhaust_ext_slow_SoundSet","RHSUSF_Abrams_exhaust_ext_mid_SoundSet","RHSUSF_Abrams_exhaust_ext_fast_SoundSet","RHSUSF_Abrams_ext_acce_soundSet","RHSUSF_Abrams_ext_acce_high_soundSet","RHSUSF_Abrams_dist_slow_SoundSet","RHSUSF_Abrams_dist_mid_SoundSet","RHSUSF_Abrams_dist_high_SoundSet","RHSUSF_Abrams_ext_tracks_slow_soundSet","RHSUSF_Abrams_ext_tracks_mid_soundSet","RHSUSF_Abrams_ext_tracks_fast_soundSet","RHSUSF_Abrams_ext_rumble_soundSet","RHSUSF_Abrams_ext_rain_soundSet","RHSUSF_trackSurfaceSound_ext_soft_soundSet","RHSUSF_trackSurfaceSound_ext_hard_soundSet","RHSUSF_trackSurfaceSound_ext_sand_soundSet"],
        "soundSetsInt": ["RHSUSF_Abrams_int_idle_SoundSet","RHSUSF_Abrams_int_slow_SoundSet","RHSUSF_Abrams_int_mid_SoundSet","RHSUSF_Abrams_int_fast_SoundSet","RHSUSF_Abrams_int_acce_soundSet","RHSUSF_Abrams_exhaust_int_idle_SoundSet","RHSUSF_Abrams_exhaust_int_slow_SoundSet","RHSUSF_Abrams_exhaust_int_mid_SoundSet","RHSUSF_Abrams_exhaust_int_fast_SoundSet","RHSUSF_tankRattling_1_soundSet","RHSUSF_Abrams_int_rain_soundSet","RHSUSF_Abrams_ext_tracks_slow_soundSet","RHSUSF_Abrams_ext_tracks_mid_soundSet","RHSUSF_Abrams_ext_tracks_fast_soundSet","RHSUSF_Abrams_ext_rumble_soundSet","RHSUSF_int_breakingStrain_soundSet","RHSUSF_curveStress_1_soundSet"]
    },
    "driveOnComponent": ["Track_L","Track_R","slide"],
    "tracksSpeed": -1.35,
    "wheelCircumference": 2.375,
    "attenuationEffectType": "TankAttenuation",
    "extCameraPosition": [0,2,-11],
    "reportOwnPosition": 1,
    "dustFrontLeftPos": "wheel_1_4_bound",
    "dustFrontRightPos": "wheel_2_4_bound",
    "dustBackLeftPos": "wheel_1_7_bound",
    "dustBackRightPos": "wheel_2_7_bound",
    "cost": 1.5e+006,
    "damageResistance": 0.02,
    "crewVulnerable": 0,
    "incomingMissileDetectionSystem": 0,
    "driverAction": "driver_apcwheeled2_out",
    "driverInAction": "RHS_M1A1_Driver",
    "driverDoor": "hatchD",
    "forceHideDriver": 0,
    "driverForceOptics": 1,
    "LODDriverTurnedIn": 0,
    "LODDriverTurnedOut": 0,
    "LODDriverOpticsIn": 0,
    "viewDriverInExternal": 1,
    "viewCargoShadow": 1,
    "viewCargoShadowDiff": 1,
    "viewCargoShadowAmb": 1,
    "armor": 600,
    "armorStructural": 400,
    "explosionShielding": 150,
    "crewExplosionProtection": 1,
    "minTotalDamageThreshold": 0.5,
    # Class: CfgVehicles\rhsusf_m1a1tank_base\TransportBackpacks,
    "TransportBackpacks": {
        # Class: CfgVehicles\rhsusf_m1a1tank_base\TransportBackpacks\_xx_rhsusf_falconii
        "_xx_rhsusf_falconii": {
            "backpack": "rhsusf_falconii",
            "count": 4
        }
    },
    # Class: CfgVehicles\rhsusf_m1a1tank_base\TransportMagazines,
    "TransportMagazines": {
        # Class: CfgVehicles\rhsusf_m1a1tank_base\TransportMagazines\_xx_rhs_mag_30Rnd_556x45_M855A1_Stanag
        "_xx_rhs_mag_30Rnd_556x45_M855A1_Stanag": {
            "magazine": "rhs_mag_30Rnd_556x45_M855A1_Stanag",
            "count": 30
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\TransportMagazines\_xx_rhsusf_mag_7x45acp_MHP,
        "_xx_rhsusf_mag_7x45acp_MHP": {
            "magazine": "rhsusf_mag_7x45acp_MHP",
            "count": 3
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\TransportMagazines\_xx_rhsusf_mag_15Rnd_9x19_FMJ,
        "_xx_rhsusf_mag_15Rnd_9x19_FMJ": {
            "magazine": "rhsusf_mag_15Rnd_9x19_FMJ",
            "count": 12
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\TransportMagazines\_xx_rhs_mag_m67,
        "_xx_rhs_mag_m67": {
            "magazine": "rhs_mag_m67",
            "count": 10
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\TransportMagazines\_xx_rhsusf_100Rnd_762x51,
        "_xx_rhsusf_100Rnd_762x51": {
            "magazine": "rhsusf_100Rnd_762x51",
            "count": 5
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\TransportMagazines\_xx_rhs_M136_mag,
        "_xx_rhs_M136_mag": {
            "magazine": "rhs_M136_mag",
            "count": 2
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\TransportMagazines\_xx_rhs_mag_m18_green,
        "_xx_rhs_mag_m18_green": {
            "magazine": "rhs_mag_m18_green",
            "count": 2
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\TransportMagazines\_xx_rhs_mag_m18_red,
        "_xx_rhs_mag_m18_red": {
            "magazine": "rhs_mag_m18_red",
            "count": 2
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\TransportMagazines\_xx_rhs_mag_m18_purple,
        "_xx_rhs_mag_m18_purple": {
            "magazine": "rhs_mag_m18_purple",
            "count": 2
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\TransportMagazines\_xx_rhs_mag_m18_yellow,
        "_xx_rhs_mag_m18_yellow": {
            "magazine": "rhs_mag_m18_yellow",
            "count": 2
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\TransportMagazines\_xx_rhs_mag_an_m8hc,
        "_xx_rhs_mag_an_m8hc": {
            "magazine": "rhs_mag_an_m8hc",
            "count": 2
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\TransportMagazines\_xx_rhs_mine_M19_mag,
        "_xx_rhs_mine_M19_mag": {
            "magazine": "rhs_mine_M19_mag",
            "count": 2
        }
    },
    # Class: CfgVehicles\rhsusf_m1a1tank_base\TransportItems,
    "TransportItems": {
        # Class: CfgVehicles\rhsusf_m1a1tank_base\TransportItems\_xx_FirstAidKit
        "_xx_FirstAidKit": {
            "name": "FirstAidKit",
            "count": 8
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\TransportItems\_xx_Medikit,
        "_xx_Medikit": {
            "name": "Medikit",
            "count": 1
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\TransportItems\_xx_Toolkit,
        "_xx_Toolkit": {
            "name": "Toolkit",
            "count": 1
        }
    },
    # Class: CfgVehicles\rhsusf_m1a1tank_base\TransportWeapons,
    "TransportWeapons": {
        # Class: CfgVehicles\rhsusf_m1a1tank_base\TransportWeapons\_xx_rhs_weap_m4_carryhandle
        "_xx_rhs_weap_m4_carryhandle": {
            "weapon": "rhs_weap_m4_carryhandle",
            "count": 2
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\TransportWeapons\_xx_rhs_weap_M136,
        "_xx_rhs_weap_M136": {
            "weapon": "rhs_weap_M136",
            "count": 2
        }
    },
    # Class: CfgVehicles\rhsusf_m1a1tank_base\ViewOptics,
    "ViewOptics": {
        "visionMode": ["Normal","TI"],
        "thermalMode": [2,3],
        "initFov": 0.7,
        "minFov": 0.7,
        "maxFov": 0.7,
        "initAngleX": 0,
        "minAngleX": -30,
        "maxAngleX": 30,
        "initAngleY": 0,
        "minAngleY": -100,
        "maxAngleY": 100,
        "minMoveX": 0,
        "maxMoveX": 0,
        "minMoveY": 0,
        "maxMoveY": 0,
        "minMoveZ": 0,
        "maxMoveZ": 0,
        "speedZoomMaxSpeed": 1e+010,
        "speedZoomMaxFOV": 0
    },
    # Class: CfgVehicles\rhsusf_m1a1tank_base\DriverOpticsIn,
    "DriverOpticsIn": {
        # Class: CfgVehicles\rhsusf_m1a1tank_base\DriverOpticsIn\Wide
        "Wide": {
            "camPos": "view_driver",
            "opticsModel": "rhsusf|addons|rhsusf_optics|data|rhs_m1_triplex",
            "visionMode": ["Normal"],
            "hitpoint": "Hit_Optic_Driver",
            "thermalMode": [2,3],
            "initFov": 0.7,
            "minFov": 0.7,
            "maxFov": 0.7,
            "initAngleX": 0,
            "minAngleX": -30,
            "maxAngleX": 30,
            "initAngleY": 0,
            "minAngleY": -100,
            "maxAngleY": 100,
            "minMoveX": 0,
            "maxMoveX": 0,
            "minMoveY": 0,
            "maxMoveY": 0,
            "minMoveZ": 0,
            "maxMoveZ": 0,
            "speedZoomMaxSpeed": 1e+010,
            "speedZoomMaxFOV": 0
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\DriverOpticsIn\DVE_Wide,
        "DVE_Wide": {
            "opticsModel": "rhsusf|addons|rhsusf_optics|data|rhsusf_DVE_4x3",
            "visionMode": ["TI"],
            "initFov": 1.07692,
            "minFov": 1.07692,
            "maxFov": 1.07692,
            "hitpoint": "Hit_Optic_DVEA",
            "camPos": "view_driver",
            "thermalMode": [2,3],
            "initAngleX": 0,
            "minAngleX": -30,
            "maxAngleX": 30,
            "initAngleY": 0,
            "minAngleY": -100,
            "maxAngleY": 100,
            "minMoveX": 0,
            "maxMoveX": 0,
            "minMoveY": 0,
            "maxMoveY": 0,
            "minMoveZ": 0,
            "maxMoveZ": 0,
            "speedZoomMaxSpeed": 1e+010,
            "speedZoomMaxFOV": 0
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\DriverOpticsIn\DVS_Rear,
        "DVS_Rear": {
            "opticsModel": "rhsusf|addons|rhsusf_optics|data|rhsusf_DVE2_4x3",
            "camPos": "view_rear",
            "camDir": "view_rear_dir",
            "hitpoint": "Hit_Optic_Driver_Rear",
            "visionMode": ["TI"],
            "initFov": 1.07692,
            "minFov": 1.07692,
            "maxFov": 1.07692,
            "thermalMode": [2,3],
            "initAngleX": 0,
            "minAngleX": -30,
            "maxAngleX": 30,
            "initAngleY": 0,
            "minAngleY": -100,
            "maxAngleY": 100,
            "minMoveX": 0,
            "maxMoveX": 0,
            "minMoveY": 0,
            "maxMoveY": 0,
            "minMoveZ": 0,
            "maxMoveZ": 0,
            "speedZoomMaxSpeed": 1e+010,
            "speedZoomMaxFOV": 0
        }
    },
    # Class: CfgVehicles\rhsusf_m1a1tank_base\Exhausts,
    "Exhausts": {
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Exhausts\Exhaust1
        "Exhaust1": {
            "position": "exhaustL1",
            "direction": "exhaustL_Dir",
            "effect": "RHS_ExhaustEffectTankGasBack"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Exhausts\Exhaust1L,
        "Exhaust1L": {
            "position": "exhaustL2",
            "direction": "exhaustL_Dir",
            "effect": "RHS_ExhaustEffectTankGasBack"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Exhausts\Exhaust2,
        "Exhaust2": {
            "position": "exhaustR1",
            "direction": "exhaustR_Dir",
            "effect": "RHS_ExhaustEffectTankGasBack"
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Exhausts\Exhaust2R,
        "Exhaust2R": {
            "position": "exhaustR2",
            "direction": "exhaustR_Dir",
            "effect": "RHS_ExhaustEffectTankGasBack"
        }
    },
    # Class: CfgVehicles\rhsusf_m1a1tank_base\Reflectors,
    "Reflectors": {
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Reflectors\Left
        "Left": {
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "position": "Light_L",
            "direction": "Light_L_end",
            "hitpoint": "Light_L",
            "selection": "Light_L",
            "size": 1,
            "innerAngle": 100,
            "outerAngle": 179,
            "coneFadeCoef": 10,
            "intensity": 1,
            "useFlare": 0,
            "dayLight": 0,
            "flareSize": 1,
            # Class: CfgVehicles\rhsusf_m1a1tank_base\Reflectors\Left\Attenuation,
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardLimitStart": 30,
                "hardLimitEnd": 60
            }
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Reflectors\Right,
        "Right": {
            "position": "Light_R",
            "direction": "Light_R_end",
            "hitpoint": "Light_R",
            "selection": "Light_R",
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "size": 1,
            "innerAngle": 100,
            "outerAngle": 179,
            "coneFadeCoef": 10,
            "intensity": 1,
            "useFlare": 0,
            "dayLight": 0,
            "flareSize": 1,
            # Class: CfgVehicles\rhsusf_m1a1tank_base\Reflectors\Left\Attenuation,
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardLimitStart": 30,
                "hardLimitEnd": 60
            }
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Reflectors\Right2,
        "Right2": {
            "position": "light_R_flare",
            "useFlare": 1,
            "direction": "Light_R_end",
            "hitpoint": "Light_R",
            "selection": "Light_R",
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "size": 1,
            "innerAngle": 100,
            "outerAngle": 179,
            "coneFadeCoef": 10,
            "intensity": 1,
            "dayLight": 0,
            "flareSize": 1,
            # Class: CfgVehicles\rhsusf_m1a1tank_base\Reflectors\Left\Attenuation,
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardLimitStart": 30,
                "hardLimitEnd": 60
            }
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\Reflectors\Left2,
        "Left2": {
            "position": "light_L_flare",
            "useFlare": 1,
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "direction": "Light_L_end",
            "hitpoint": "Light_L",
            "selection": "Light_L",
            "size": 1,
            "innerAngle": 100,
            "outerAngle": 179,
            "coneFadeCoef": 10,
            "intensity": 1,
            "dayLight": 0,
            "flareSize": 1,
            # Class: CfgVehicles\rhsusf_m1a1tank_base\Reflectors\Left\Attenuation,
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardLimitStart": 30,
                "hardLimitEnd": 60
            }
        }
    },
    "aggregateReflectors": [["Left","Left2"],["Right","Right2"]],
    "armorLights": 0.01,
    # Class: CfgVehicles\rhsusf_m1a1tank_base\RenderTargets,
    "RenderTargets": {
        # Class: CfgVehicles\rhsusf_m1a1tank_base\RenderTargets\driverView1
        "driverView1": {
            "renderTarget": "rendertarget1",
            # Class: CfgVehicles\rhsusf_m1a1tank_base\RenderTargets\driverView1\Camera,
            "Camera": {
                "pointPosition": "dVis1P",
                "pointDirection": "dVis1D",
                "renderVisionMode": 0,
                "renderQuality": 4,
                "fov": 0.5
            }
        },
        # Class: CfgVehicles\rhsusf_m1a1tank_base\RenderTargets\driverView2,
        "driverView2": {
            "renderTarget": "rendertarget0",
            # Class: CfgVehicles\rhsusf_m1a1tank_base\RenderTargets\driverView2\Camera,
            "Camera": {
                "pointPosition": "dVis2P",
                "pointDirection": "dVis2D",
                "renderVisionMode": 0,
                "renderQuality": 4,
                "fov": 0.5
            }
        }
    },
    "dlc": "RHS_USAF",
    "soundGetIn": ["A3|Sounds_F_EPB|Tracked|noises|get_in_out",0.562341,1],
    "soundGetOut": ["A3|Sounds_F_EPB|Tracked|noises|get_in_out",0.562341,1,20],
    "soundTurnIn": ["A3|Sounds_F|vehicles|noises|Turn_in_out",1.77828,1,20],
    "soundTurnOut": ["A3|Sounds_F|vehicles|noises|Turn_in_out",1.77828,1,20],
    "soundTurnInInternal": ["A3|Sounds_F|vehicles|noises|Turn_in_out",1.77828,1,20],
    "soundTurnOutInternal": ["A3|Sounds_F|vehicles|noises|Turn_in_out",1.77828,1,20],
    "soundDammage": ["",0.562341,1],
    "BushCrash1": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_Collision_Light_Bush_01",0.630957,1,100],
    "BushCrash2": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_Collision_Light_Bush_02",0.630957,1,100],
    "BushCrash3": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_Collision_Light_Bush_03",0.630957,1,100],
    "soundBushCrash": ["BushCrash1",0.33,"BushCrash2",0.33,"BushCrash3",0.33],
    "buildCrash0": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_01",3.16228,1,200],
    "buildCrash1": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_02",3.16228,1,200],
    "buildCrash2": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_03",3.16228,1,200],
    "buildCrash3": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_04",3.16228,1,200],
    "buildCrash4": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_05",3.16228,1,200],
    "buildCrash5": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_06",3.16228,1,200],
    "soundBuildingCrash": ["buildCrash0",0.166,"buildCrash1",0.166,"buildCrash2",0.166,"buildCrash3",0.166,"buildCrash4",0.166,"buildCrash5",0.166],
    "woodCrash0": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_01",3.16228,1,200],
    "woodCrash1": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_02",3.16228,1,200],
    "woodCrash2": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_03",3.16228,1,200],
    "woodCrash3": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_04",3.16228,1,200],
    "woodCrash4": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_05",3.16228,1,200],
    "woodCrash5": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_06",3.16228,1,200],
    "soundWoodCrash": ["woodCrash0",0.166,"woodCrash1",0.166,"woodCrash2",0.166,"woodCrash3",0.166,"woodCrash4",0.166,"woodCrash5",0.166],
    "ArmorCrash0": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_01",3.16228,1,200],
    "ArmorCrash1": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_02",3.16228,1,200],
    "ArmorCrash2": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_03",3.16228,1,200],
    "ArmorCrash3": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_04",3.16228,1,200],
    "ArmorCrash4": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_05",3.16228,1,200],
    "ArmorCrash5": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_06",3.16228,1,200],
    "soundArmorCrash": ["ArmorCrash0",0.166,"ArmorCrash1",0.166,"ArmorCrash2",0.166,"ArmorCrash3",0.166,"ArmorCrash4",0.166,"ArmorCrash5",0.166],
    "_generalMacro": "MBT_01_base_F",
    "brakeIdleSpeed": 0.1,
    "waterResistanceCoef": 0.25,
    "dampingRateFullThrottle": 0.3,
    "dampingRateZeroThrottleClutchEngaged": 3,
    "dampingRateZeroThrottleClutchDisengaged": 0.25,
    # Class: CfgVehicles\MBT_01_base_F\MFD,
    "MFD": {
        # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Driver_Heading
        "MFD_Driver_Heading": {
            "topLeft": "MFD_1_TL",
            "topRight": "MFD_1_TR",
            "bottomLeft": "MFD_1_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "enableParallax": 0,
            "font": "LCD14",
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Driver_Heading\material,
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Driver_Heading\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Driver_Heading\Draw,
            "Draw": {
                "color": [0.61,0.62,0],
                "alpha": 1,
                "condition": "on",
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Driver_Heading\Draw\Driver_Heading,
                "Driver_Heading": {
                    "type": "text",
                    "source": "heading",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.5,0],1],
                    "right": [[1,0],1],
                    "down": [[0.5,0.81],1]
                }
            }
        },
        # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Driver_Speed,
        "MFD_Driver_Speed": {
            "topLeft": "MFD_2_TL",
            "topRight": "MFD_2_TR",
            "bottomLeft": "MFD_2_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "enableParallax": 0,
            "font": "LCD14",
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Driver_Speed\material,
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Driver_Speed\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Driver_Speed\Draw,
            "Draw": {
                "color": [0.61,0.62,0],
                "alpha": 1,
                "condition": "on",
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Driver_Speed\Draw\Driver_Speed,
                "Driver_Speed": {
                    "type": "text",
                    "source": "speed",
                    "sourceScale": 3.6,
                    "sourceLength": 2,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.5,0],1],
                    "right": [[1,0],1],
                    "down": [[0.5,0.81],1]
                }
            }
        },
        # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Driver_Heading_text,
        "MFD_Driver_Heading_text": {
            "topLeft": "MFD_Driver_1_TL",
            "topRight": "MFD_Driver_1_TR",
            "bottomLeft": "MFD_Driver_1_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [1,1,1],
            "alpha": 0.5,
            "enableParallax": 0,
            "font": "RobotoCondensedLight",
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Driver_Heading_text\material,
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Driver_Heading_text\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Driver_Heading_text\Draw,
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Driver_Heading_text\Draw\Driver_Heading,
                "Driver_Heading": {
                    "type": "text",
                    "source": "static",
                    "text": "AZIMUTH",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.45,0.02],1],
                    "right": [[0.7,0.02],1],
                    "down": [[0.45,0.87],1]
                }
            }
        },
        # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Driver_Heading_second,
        "MFD_Driver_Heading_second": {
            "topLeft": "MFD_Driver_2_TL",
            "topRight": "MFD_Driver_2_TR",
            "bottomLeft": "MFD_Driver_2_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [1,1,1],
            "alpha": 0.5,
            "enableParallax": 0,
            "font": "RobotoCondensedLight",
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Driver_Heading_second\material,
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Driver_Heading_second\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Driver_Heading_second\Draw,
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Driver_Heading_second\Draw\Driver_Heading,
                "Driver_Heading": {
                    "type": "text",
                    "source": "heading",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.45,0],1],
                    "right": [[0.95,0],1],
                    "down": [[0.45,0.81],1]
                }
            }
        },
        # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Gunner_Ready_To_Fire,
        "MFD_Gunner_Ready_To_Fire": {
            "topLeft": "mfd_gun_cli_TL",
            "topRight": "mfd_gun_cli_TR",
            "bottomLeft": "mfd_gun_cli_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0,0,0],
            "alpha": 0.5,
            "enableParallax": 0,
            "font": "EtelkaMonospaceProBold",
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Gunner_Ready_To_Fire\material,
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Gunner_Ready_To_Fire\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Gunner_Ready_To_Fire\Draw,
            "Draw": {
                "color": [0,0,0],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Gunner_Ready_To_Fire\Draw\Top_text,
                "Top_text": {
                    "type": "text",
                    "source": "static",
                    "text": "READY TO",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.45,0.05],1],
                    "right": [[0.67,0.05],1],
                    "down": [[0.45,0.55],1]
                },
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Gunner_Ready_To_Fire\Draw\Bottom_text,
                "Bottom_text": {
                    "type": "text",
                    "source": "static",
                    "text": "FIRE",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.465,0.45],1],
                    "right": [[0.685,0.45],1],
                    "down": [[0.465,0.95],1]
                }
            }
        },
        # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Gunner_Display,
        "MFD_Gunner_Display": {
            "topLeft": "mfd_gun_TL",
            "topRight": "mfd_gun_TR",
            "bottomLeft": "mfd_gun_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [1,1,1],
            "alpha": 0.5,
            "enableParallax": 0,
            "turret": [0],
            "font": "EtelkaMonospaceProBold",
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Gunner_Display\material,
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Gunner_Display\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Gunner_Display\Draw,
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Gunner_Display\Draw\Main_armament,
                "Main_armament": {
                    "type": "text",
                    "source": "static",
                    "text": "MAIN ARMAMENT",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshRate": 0.1,
                    "pos": [[0.015,-0.003],1],
                    "right": [[0.075,-0.003],1],
                    "down": [[0.015,0.075],1]
                },
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Gunner_Display\Draw\Machinegun,
                "Machinegun": {
                    "type": "text",
                    "source": "static",
                    "text": "COAX",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshRate": 0.1,
                    "pos": [[0.015,0.31],1],
                    "right": [[0.075,0.31],1],
                    "down": [[0.015,0.388],1]
                },
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Gunner_Display\Draw\Main_armament_ammo_type,
                "Main_armament_ammo_type": {
                    "type": "text",
                    "source": "static",
                    "text": "AMMO TYPE",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.545,-0.003],1],
                    "right": [[0.605,-0.003],1],
                    "down": [[0.545,0.075],1]
                },
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Gunner_Display\Draw\Lased_distance_elevation,
                "Lased_distance_elevation": {
                    "type": "text",
                    "source": "static",
                    "text": "LASED DIST",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshRate": 0.1,
                    "pos": [[0.015,0.84],1],
                    "right": [[0.065,0.84],1],
                    "down": [[0.015,0.918],1]
                },
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Gunner_Display\Draw\Azimut,
                "Azimut": {
                    "type": "text",
                    "source": "static",
                    "text": "AZIMUTH",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshRate": 0.1,
                    "pos": [[0.015,0.915],1],
                    "right": [[0.075,0.915],1],
                    "down": [[0.015,0.993],1]
                },
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Gunner_Display\Draw\Damage,
                "Damage": {
                    "type": "text",
                    "source": "static",
                    "text": "DAMAGE",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshRate": 0.1,
                    "pos": [[0.015,0.39],1],
                    "right": [[0.075,0.39],1],
                    "down": [[0.015,0.468],1]
                },
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Gunner_Display\Draw\Heading,
                "Heading": {
                    "type": "text",
                    "source": "[x]turretworld",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 0.2,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.34,0.915],1],
                    "right": [[0.4,0.915],1],
                    "down": [[0.34,0.993],1]
                },
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Gunner_Display\Draw\Lased_Range,
                "Lased_Range": {
                    "type": "text",
                    "source": "laserDist",
                    "sourceScale": 1,
                    "sourceLength": 4,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.335,0.84],1],
                    "right": [[0.395,0.84],1],
                    "down": [[0.335,0.918],1]
                }
            }
        },
        # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Gunner_Main_Armament_Ammo_Type,
        "MFD_Gunner_Main_Armament_Ammo_Type": {
            "topLeft": "mfd_gun_TL",
            "topRight": "mfd_gun_TR",
            "bottomLeft": "mfd_gun_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "turret": [0],
            "enableParallax": 0,
            "font": "EtelkaMonospaceProBold",
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Gunner_Main_Armament_Ammo_Type\material,
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Gunner_Main_Armament_Ammo_Type\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Gunner_Main_Armament_Ammo_Type\Draw,
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Gunner_Main_Armament_Ammo_Type\Draw\Gunner_AmmoType,
                "Gunner_AmmoType": {
                    "type": "text",
                    "source": "ammoFormat",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.56,0.09],1],
                    "right": [[0.62,0.09],1],
                    "down": [[0.56,0.168],1]
                }
            }
        },
        # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Gunner_Coax_Ammo,
        "MFD_Gunner_Coax_Ammo": {
            "topLeft": "mfd_gun_TL",
            "topRight": "mfd_gun_TR",
            "bottomLeft": "mfd_gun_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "enableParallax": 0,
            "turret": [0],
            "font": "EtelkaMonospaceProBold",
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Gunner_Coax_Ammo\material,
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Gunner_Coax_Ammo\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Gunner_Coax_Ammo\Draw,
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Gunner_Coax_Ammo\Draw\Gunner_Text_1,
                "Gunner_Text_1": {
                    "type": "text",
                    "source": "ammo",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "sourceIndex": 1,
                    "align": "left",
                    "refreshRate": 0.1,
                    "pos": [[0.37,0.31],1],
                    "right": [[0.43,0.31],1],
                    "down": [[0.37,0.388],1]
                }
            }
        },
        # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Gunner_AmmoIndicator_Main_Armament,
        "MFD_Gunner_AmmoIndicator_Main_Armament": {
            "topLeft": "mfd_gun_TL",
            "topRight": "mfd_gun_TR",
            "bottomLeft": "mfd_gun_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "enableParallax": 0,
            "turret": [0],
            "font": "EtelkaMonospacePro",
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Gunner_AmmoIndicator_Main_Armament\material,
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Gunner_AmmoIndicator_Main_Armament\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Gunner_AmmoIndicator_Main_Armament\Draw,
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Gunner_AmmoIndicator_Main_Armament\Draw\Main_Armament_Ammo_Type_1,
                "Main_Armament_Ammo_Type_1": {
                    "type": "text",
                    "source": "static",
                    "text": "APFSDS-T",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshRate": 0.1,
                    "pos": [[0.015,0.065],1],
                    "right": [[0.075,0.065],1],
                    "down": [[0.015,0.143],1]
                },
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Gunner_AmmoIndicator_Main_Armament\Draw\Gunner_Text_1,
                "Gunner_Text_1": {
                    "type": "text",
                    "source": "ammo",
                    "sourceScale": 1,
                    "sourceLength": 2,
                    "sourceIndex": 1000,
                    "scale": 1,
                    "align": "left",
                    "refreshRate": 0.1,
                    "pos": [[0.385,0.065],1],
                    "right": [[0.445,0.065],1],
                    "down": [[0.385,0.143],1]
                },
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Gunner_AmmoIndicator_Main_Armament\Draw\Main_Armament_Ammo_Type_2,
                "Main_Armament_Ammo_Type_2": {
                    "type": "text",
                    "source": "static",
                    "text": "HE-T",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshRate": 0.1,
                    "pos": [[0.015,0.125],1],
                    "right": [[0.075,0.125],1],
                    "down": [[0.015,0.203],1]
                },
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Gunner_AmmoIndicator_Main_Armament\Draw\Gunner_Text_2,
                "Gunner_Text_2": {
                    "type": "text",
                    "source": "ammo",
                    "sourceScale": 1,
                    "sourceLength": 2,
                    "sourceIndex": 1001,
                    "scale": 1,
                    "align": "left",
                    "refreshRate": 0.1,
                    "pos": [[0.385,0.125],1],
                    "right": [[0.445,0.125],1],
                    "down": [[0.385,0.203],1]
                },
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Gunner_AmmoIndicator_Main_Armament\Draw\Main_Armament_Ammo_Type_3,
                "Main_Armament_Ammo_Type_3": {
                    "type": "text",
                    "source": "static",
                    "text": "HEAT-MP-T",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshRate": 0.1,
                    "pos": [[0.015,0.185],1],
                    "right": [[0.075,0.185],1],
                    "down": [[0.015,0.263],1]
                },
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Gunner_AmmoIndicator_Main_Armament\Draw\Gunner_Text_3,
                "Gunner_Text_3": {
                    "type": "text",
                    "source": "ammo",
                    "sourceScale": 1,
                    "sourceLength": 2,
                    "sourceIndex": 1002,
                    "scale": 1,
                    "align": "left",
                    "refreshRate": 0.1,
                    "pos": [[0.385,0.185],1],
                    "right": [[0.445,0.185],1],
                    "down": [[0.385,0.263],1]
                }
            }
        },
        # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Gunner_Generic1,
        "MFD_Gunner_Generic1": {
            "topLeft": "mfd_gun_generic1_TL",
            "topRight": "mfd_gun_generic1_TR",
            "bottomLeft": "mfd_gun_generic1_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "enableParallax": 0,
            "font": "PuristaMedium",
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Gunner_Generic1\material,
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Gunner_Generic1\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Gunner_Generic1\Draw,
            "Draw": {
                "color": [0.61,0.62,0],
                "alpha": 1,
                "condition": "on",
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Gunner_Generic1\Draw\Generic_Text1,
                "Generic_Text1": {
                    "type": "text",
                    "source": "static",
                    "text": "SIGHT: READY",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "right",
                    "pos": [[0.05,0.1],1],
                    "right": [[0.17,0.1],1],
                    "down": [[0.05,0.5],1]
                },
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Gunner_Generic1\Draw\Generic_Text2,
                "Generic_Text2": {
                    "type": "text",
                    "source": "static",
                    "text": "RETICLE: CALIBRATED",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "right",
                    "pos": [[0.05,0.45],1],
                    "right": [[0.17,0.45],1],
                    "down": [[0.05,0.85],1]
                }
            }
        },
        # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Display,
        "MFD_Commander_Display": {
            "topLeft": "mfd_com_TL",
            "topRight": "mfd_com_TR",
            "bottomLeft": "mfd_com_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [1,1,1],
            "alpha": 0.5,
            "enableParallax": 0,
            "turret": [0,0],
            "font": "PuristaMedium",
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Display\material,
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Display\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Display\Draw,
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Display\Draw\Main_armament,
                "Main_armament": {
                    "type": "text",
                    "source": "static",
                    "text": "MAIN ARMAMENT",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshRate": 0.1,
                    "pos": [[0.015,-0.005],1],
                    "right": [[0.075,-0.005],1],
                    "down": [[0.015,0.145],1]
                },
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Display\Draw\Machinegun,
                "Machinegun": {
                    "type": "text",
                    "source": "static",
                    "text": "COAX MG",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.51,-0.005],1],
                    "right": [[0.57,-0.005],1],
                    "down": [[0.51,0.145],1]
                },
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Display\Draw\Commander_machinegun,
                "Commander_machinegun": {
                    "type": "text",
                    "source": "static",
                    "text": "----",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "left",
                    "refreshRate": 0.1,
                    "pos": [[0.84,0.19],1],
                    "right": [[0.9,0.19],1],
                    "down": [[0.84,0.34],1]
                },
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Display\Draw\Commander_armament,
                "Commander_armament": {
                    "type": "text",
                    "source": "static",
                    "text": "COM ARMAMENT",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.785,-0.005],1],
                    "right": [[0.845,-0.005],1],
                    "down": [[0.785,0.145],1]
                },
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Display\Draw\Commander_armament_magazines,
                "Commander_armament_magazines": {
                    "type": "text",
                    "source": "static",
                    "text": "MAG",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.47,0.4],1],
                    "right": [[0.53,0.4],1],
                    "down": [[0.47,0.55],1]
                },
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Display\Draw\Main_armament_ammo_type,
                "Main_armament_ammo_type": {
                    "type": "text",
                    "source": "static",
                    "text": "AMMO TYPE",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshRate": 0.1,
                    "pos": [[0.015,0.61],1],
                    "right": [[0.075,0.61],1],
                    "down": [[0.015,0.76],1]
                },
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Display\Draw\Lased_distance_elevation,
                "Lased_distance_elevation": {
                    "type": "text",
                    "source": "static",
                    "text": "LASED DST",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.73,0.61],1],
                    "right": [[0.785,0.61],1],
                    "down": [[0.73,0.76],1]
                },
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Display\Draw\Azimut,
                "Azimut": {
                    "type": "text",
                    "source": "static",
                    "text": "AZIMUTH",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.72,0.8],1],
                    "right": [[0.78,0.8],1],
                    "down": [[0.72,0.95],1]
                },
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Display\Draw\Damage,
                "Damage": {
                    "type": "text",
                    "source": "static",
                    "text": "DAMAGE",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshRate": 0.1,
                    "pos": [[0.015,0.82],1],
                    "right": [[0.075,0.82],1],
                    "down": [[0.015,0.97],1]
                },
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Display\Draw\Heading,
                "Heading": {
                    "type": "text",
                    "source": "[x]turretworld",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 0.2,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.925,0.8],1],
                    "right": [[0.985,0.8],1],
                    "down": [[0.925,0.95],1]
                },
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Display\Draw\Lased_Range,
                "Lased_Range": {
                    "type": "text",
                    "source": "laserDist",
                    "sourceScale": 1,
                    "sourceLength": 4,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.925,0.61],1],
                    "right": [[0.985,0.61],1],
                    "down": [[0.925,0.76],1]
                }
            }
        },
        # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Generic1,
        "MFD_Commander_Generic1": {
            "topLeft": "mfd_com_generic1_TL",
            "topRight": "mfd_com_generic1_TR",
            "bottomLeft": "mfd_com_generic1_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "enableParallax": 0,
            "font": "PuristaMedium",
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Generic1\material,
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Generic1\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Generic1\Draw,
            "Draw": {
                "color": [0.61,0.62,0],
                "alpha": 1,
                "condition": "on",
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Generic1\Draw\Generic_Text1,
                "Generic_Text1": {
                    "type": "text",
                    "source": "static",
                    "text": "SIGHT: READY",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "right",
                    "pos": [[0.05,0.1],1],
                    "right": [[0.17,0.1],1],
                    "down": [[0.05,0.5],1]
                },
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Generic1\Draw\Generic_Text2,
                "Generic_Text2": {
                    "type": "text",
                    "source": "static",
                    "text": "RETICLE: CALIBRATED",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "right",
                    "pos": [[0.05,0.45],1],
                    "right": [[0.17,0.45],1],
                    "down": [[0.05,0.85],1]
                }
            }
        },
        # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Generic2,
        "MFD_Commander_Generic2": {
            "topLeft": "mfd_com_generic2_TL",
            "topRight": "mfd_com_generic2_TR",
            "bottomLeft": "mfd_com_generic2_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "enableParallax": 0,
            "font": "PuristaMedium",
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Generic2\material,
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Generic2\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Generic2\Draw,
            "Draw": {
                "color": [0.61,0.62,0],
                "alpha": 1,
                "condition": "on",
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Generic2\Draw\Generic_Text1,
                "Generic_Text1": {
                    "type": "text",
                    "source": "static",
                    "text": "BRIGHTNESS: 7",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "right",
                    "pos": [[0.05,0],1],
                    "right": [[0.2,0],1],
                    "down": [[0.05,0.5],1]
                },
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Generic2\Draw\Generic_Text2,
                "Generic_Text2": {
                    "type": "text",
                    "source": "static",
                    "text": "AUTO: ON",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "right",
                    "pos": [[0.05,0.45],1],
                    "right": [[0.2,0.45],1],
                    "down": [[0.05,0.95],1]
                }
            }
        },
        # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Ready_To_Fire,
        "MFD_Commander_Ready_To_Fire": {
            "topLeft": "mfd_com_cli_TL",
            "topRight": "mfd_com_cli_TR",
            "bottomLeft": "mfd_com_cli_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0,0,0],
            "alpha": 0.5,
            "enableParallax": 0,
            "font": "RobotoCondensedLight",
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Ready_To_Fire\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Ready_To_Fire\Draw,
            "Draw": {
                "color": [0,0,0],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Ready_To_Fire\Draw\Top_text,
                "Top_text": {
                    "type": "text",
                    "source": "static",
                    "text": "READY TO",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "center",
                    "pos": [[0.48,0.05],1],
                    "right": [[0.68,0.05],1],
                    "down": [[0.48,0.56],1]
                },
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Ready_To_Fire\Draw\Bottom_text,
                "Bottom_text": {
                    "type": "text",
                    "source": "static",
                    "text": "FIRE",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "center",
                    "pos": [[0.5,0.41],1],
                    "right": [[0.7,0.41],1],
                    "down": [[0.5,0.92],1]
                }
            }
        },
        # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Smoke_Indicator,
        "MFD_Commander_Smoke_Indicator": {
            "topLeft": "mfd_com_smoke_TL",
            "topRight": "mfd_com_smoke_TR",
            "bottomLeft": "mfd_com_smoke_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0,0,0],
            "alpha": 0.5,
            "enableParallax": 0,
            "font": "RobotoCondensedLight",
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Smoke_Indicator\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Smoke_Indicator\Draw,
            "Draw": {
                "color": [0,0,0],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Smoke_Indicator\Draw\Top_text,
                "Top_text": {
                    "type": "text",
                    "source": "static",
                    "text": "SMOKE",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "center",
                    "pos": [[0.5,0],1],
                    "right": [[0.7,0],1],
                    "down": [[0.5,0.5],1]
                },
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Smoke_Indicator\Draw\Bottom_text,
                "Bottom_text": {
                    "type": "text",
                    "source": "static",
                    "text": "SCREEN",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "center",
                    "pos": [[0.5,0.4],1],
                    "right": [[0.7,0.4],1],
                    "down": [[0.5,0.9],1]
                }
            }
        },
        # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Main_Armament_Ammo_Type,
        "MFD_Commander_Main_Armament_Ammo_Type": {
            "topLeft": "mfd_com_TL",
            "topRight": "mfd_com_TR",
            "bottomLeft": "mfd_com_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "turret": [0],
            "enableParallax": 0,
            "font": "PuristaMedium",
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Main_Armament_Ammo_Type\material,
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Main_Armament_Ammo_Type\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Main_Armament_Ammo_Type\Draw,
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Main_Armament_Ammo_Type\Draw\Gunner_AmmoType,
                "Gunner_AmmoType": {
                    "type": "text",
                    "source": "ammoFormat",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.33,0.615],1],
                    "right": [[0.39,0.615],1],
                    "down": [[0.33,0.745],1]
                }
            }
        },
        # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_AmmoIndicator_Main_Armament,
        "MFD_Commander_AmmoIndicator_Main_Armament": {
            "topLeft": "mfd_com_TL",
            "topRight": "mfd_com_TR",
            "bottomLeft": "mfd_com_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "enableParallax": 0,
            "turret": [0],
            "font": "PuristaMedium",
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_AmmoIndicator_Main_Armament\material,
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_AmmoIndicator_Main_Armament\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_AmmoIndicator_Main_Armament\Draw,
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_AmmoIndicator_Main_Armament\Draw\Main_Armament_Ammo_Type_1,
                "Main_Armament_Ammo_Type_1": {
                    "type": "text",
                    "source": "static",
                    "text": "APFSDS-T",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshRate": 0.1,
                    "pos": [[0.015,0.13],1],
                    "right": [[0.075,0.13],1],
                    "down": [[0.015,0.28],1]
                },
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_AmmoIndicator_Main_Armament\Draw\Gunner_Text_1,
                "Gunner_Text_1": {
                    "type": "text",
                    "source": "ammo",
                    "sourceScale": 1,
                    "sourceLength": 2,
                    "sourceIndex": 1000,
                    "scale": 1,
                    "align": "left",
                    "refreshRate": 0.1,
                    "pos": [[0.39,0.13],1],
                    "right": [[0.45,0.13],1],
                    "down": [[0.39,0.28],1]
                },
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_AmmoIndicator_Main_Armament\Draw\Main_Armament_Ammo_Type_2,
                "Main_Armament_Ammo_Type_2": {
                    "type": "text",
                    "source": "static",
                    "text": "HE-T",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshRate": 0.1,
                    "pos": [[0.015,0.23],1],
                    "right": [[0.075,0.23],1],
                    "down": [[0.015,0.38],1]
                },
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_AmmoIndicator_Main_Armament\Draw\Gunner_Text_2,
                "Gunner_Text_2": {
                    "type": "text",
                    "source": "ammo",
                    "sourceScale": 1,
                    "sourceLength": 2,
                    "sourceIndex": 1001,
                    "scale": 1,
                    "align": "left",
                    "refreshRate": 0.1,
                    "pos": [[0.39,0.23],1],
                    "right": [[0.45,0.23],1],
                    "down": [[0.39,0.38],1]
                },
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_AmmoIndicator_Main_Armament\Draw\Main_Armament_Ammo_Type_3,
                "Main_Armament_Ammo_Type_3": {
                    "type": "text",
                    "source": "static",
                    "text": "HEAT-MP-T",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshRate": 0.1,
                    "pos": [[0.015,0.33],1],
                    "right": [[0.075,0.33],1],
                    "down": [[0.015,0.48],1]
                },
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_AmmoIndicator_Main_Armament\Draw\Gunner_Text_3,
                "Gunner_Text_3": {
                    "type": "text",
                    "source": "ammo",
                    "sourceScale": 1,
                    "sourceLength": 2,
                    "sourceIndex": 1002,
                    "scale": 1,
                    "align": "left",
                    "refreshRate": 0.1,
                    "pos": [[0.39,0.33],1],
                    "right": [[0.45,0.33],1],
                    "down": [[0.39,0.48],1]
                }
            }
        },
        # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Coax_Ammo,
        "MFD_Commander_Coax_Ammo": {
            "topLeft": "mfd_com_ammo_count_TL",
            "topRight": "mfd_com_ammo_count_TR",
            "bottomLeft": "mfd_com_ammo_count_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "enableParallax": 0,
            "turret": [0],
            "font": "PuristaMedium",
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Coax_Ammo\material,
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Coax_Ammo\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Coax_Ammo\Draw,
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Coax_Ammo\Draw\Gunner_Text_1,
                "Gunner_Text_1": {
                    "type": "text",
                    "source": "ammo",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "sourceIndex": 1,
                    "align": "left",
                    "refreshRate": 0.1,
                    "pos": [[1.495,0.2],1],
                    "right": [[2.045,0.2],1],
                    "down": [[1.495,0.9],1]
                }
            }
        },
        # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Coax_Magazines,
        "MFD_Commander_Coax_Magazines": {
            "topLeft": "mfd_com_mag_count_TL",
            "topRight": "mfd_com_mag_count_TR",
            "bottomLeft": "mfd_com_mag_count_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "enableParallax": 0,
            "turret": [0],
            "font": "PuristaMedium",
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Coax_Magazines\material,
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Coax_Magazines\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Coax_Magazines\Draw,
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_Coax_Magazines\Draw\Gunner_Text_1,
                "Gunner_Text_1": {
                    "type": "text",
                    "source": "ammo",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "sourceIndex": 1,
                    "align": "right",
                    "refreshRate": 0.1,
                    "pos": [[-1.7,0.11],1],
                    "right": [[-0.95,0.11],1],
                    "down": [[-1.7,0.81],1]
                }
            }
        },
        # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_OnScreen,
        "MFD_Commander_OnScreen": {
            "topLeft": "PIP_COM_TL",
            "topRight": "PIP_COM_TR",
            "bottomLeft": "PIP_COM_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [1,1,1],
            "alpha": 0.5,
            "enableParallax": 0,
            "turret": [0,0],
            "font": "EtelkaMonospaceProBold",
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_OnScreen\material,
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_OnScreen\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_OnScreen\Draw,
            "Draw": {
                "color": [0.15,1,0.05],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_OnScreen\Draw\Azimuth_number,
                "Azimuth_number": {
                    "type": "text",
                    "source": "[x]turretworld",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.5,0.235],1],
                    "right": [[0.525,0.235],1],
                    "down": [[0.5,0.272],1]
                },
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_OnScreen\Draw\Elevation_Text,
                "Elevation_Text": {
                    "type": "text",
                    "source": "static",
                    "text": "E: ",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.23,0.3],1],
                    "right": [[0.255,0.3],1],
                    "down": [[0.23,0.337],1]
                },
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_OnScreen\Draw\Elevation_Number,
                "Elevation_Number": {
                    "type": "text",
                    "source": "[y]turretworld",
                    "sourceScale": 1,
                    "sourceLength": 4,
                    "sourcePrecision": 1,
                    "refreshRate": 0,
                    "align": "center",
                    "scale": 1,
                    "pos": [[0.26,0.3],1],
                    "right": [[0.285,0.3],1],
                    "down": [[0.26,0.337],1]
                },
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_OnScreen\Draw\Lased_Range,
                "Lased_Range": {
                    "type": "text",
                    "source": "laserDist",
                    "sourceScale": 1,
                    "sourceLength": 4,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.5,0.65],1],
                    "right": [[0.525,0.65],1],
                    "down": [[0.5,0.687],1]
                },
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_OnScreen\Draw\VisionMode_Text,
                "VisionMode_Text": {
                    "type": "text",
                    "source": "static",
                    "text": "WFOV",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.75,0.65],1],
                    "right": [[0.775,0.65],1],
                    "down": [[0.75,0.687],1]
                },
                # Class: CfgVehicles\MBT_01_base_F\MFD\MFD_Commander_OnScreen\Draw\VisionMode_String,
                "VisionMode_String": {
                    "type": "text",
                    "source": "visionMode",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.825,0.65],1],
                    "right": [[0.85,0.65],1],
                    "down": [[0.825,0.687],1]
                }
            }
        }
    },
    "editorSubcategory": "EdSubcat_Tanks",
    "driverInfoPanelCameraPos": "driverview_old",
    "driverLeftHandAnimName": "drivewheel",
    "driverRightHandAnimName": "drivewheel",
    "driverLeftLegAnimName": "pedal_brake",
    "driverRightLegAnimName": "pedal_thrust",
    "viewDriverShadowAmb": 0.5,
    "viewDriverShadowDiff": 0.05,
    # Class: CfgVehicles\MBT_01_base_F\ViewPilot,
    "ViewPilot": {
        "initAngleX": -3,
        "initAngleY": 0,
        "initFov": 0.9,
        "minFov": 0.25,
        "maxFov": 1.25,
        "minAngleX": -65,
        "maxAngleX": 85,
        "minAngleY": -150,
        "maxAngleY": 150,
        "minMoveX": 0,
        "maxMoveX": 0,
        "minMoveY": -0.075,
        "maxMoveY": 0.075,
        "minMoveZ": -0.075,
        "maxMoveZ": 0.1,
        "speedZoomMaxSpeed": 1e+010,
        "speedZoomMaxFOV": 0
    },
    "epeImpulseDamageCoef": 18,
    "waterPPInVehicle": 0,
    "memoryPointTaskMarker": "TaskMarker_1_pos",
    "hideWeaponsDriver": 1,
    "hideWeaponsCargo": 1,
    "animationSourceHatch": "",
    "insideSoundCoef": 0.9,
    "threat": [0.8,1,0.3],
    # Class: CfgVehicles\MBT_01_base_F\compartmentsLights,
    "compartmentsLights": {
        # Class: CfgVehicles\MBT_01_base_F\compartmentsLights\Comp1
        "Comp1": {
            # Class: CfgVehicles\MBT_01_base_F\compartmentsLights\Comp1\Light1
            "Light1": {
                "color": [13,20,20],
                "ambient": [0,0,0],
                "intensity": 2,
                "size": 0,
                "useFlare": 0,
                "flareSize": 0,
                "flareMaxDistance": 0,
                "dayLight": 0,
                "blinking": 0,
                # Class: CfgVehicles\MBT_01_base_F\compartmentsLights\Comp1\Light1\Attenuation,
                "Attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardLimitStart": 0.15,
                    "hardLimitEnd": 1.15
                },
                "point": "light_interior1"
            },
            # Class: CfgVehicles\MBT_01_base_F\compartmentsLights\Comp1\Light2,
            "Light2": {
                "point": "light_interior2",
                "color": [13,20,20],
                "ambient": [0,0,0],
                "intensity": 1.5,
                "size": 0,
                "useFlare": 0,
                "flareSize": 0,
                "flareMaxDistance": 0,
                "dayLight": 0,
                "blinking": 0,
                # Class: CfgVehicles\MBT_01_base_F\compartmentsLights\Comp1\Light1\Attenuation,
                "Attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardLimitStart": 0.15,
                    "hardLimitEnd": 1.15
                }
            },
            # Class: CfgVehicles\MBT_01_base_F\compartmentsLights\Comp1\Light3,
            "Light3": {
                "point": "light_interior3",
                "color": [13,20,20],
                "ambient": [0,0,0],
                "intensity": 1.5,
                "size": 0,
                "useFlare": 0,
                "flareSize": 0,
                "flareMaxDistance": 0,
                "dayLight": 0,
                "blinking": 0,
                # Class: CfgVehicles\MBT_01_base_F\compartmentsLights\Comp1\Light1\Attenuation,
                "Attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardLimitStart": 0.15,
                    "hardLimitEnd": 1.15
                }
            },
            # Class: CfgVehicles\MBT_01_base_F\compartmentsLights\Comp1\Light4,
            "Light4": {
                "point": "light_interior4",
                "color": [13,20,20],
                "ambient": [0,0,0],
                "intensity": 0.7,
                "size": 0,
                "useFlare": 0,
                "flareSize": 0,
                "flareMaxDistance": 0,
                "dayLight": 0,
                "blinking": 0,
                # Class: CfgVehicles\MBT_01_base_F\compartmentsLights\Comp1\Light1\Attenuation,
                "Attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardLimitStart": 0.15,
                    "hardLimitEnd": 1.15
                }
            },
            # Class: CfgVehicles\MBT_01_base_F\compartmentsLights\Comp1\Light5,
            "Light5": {
                "point": "light_interior5",
                "color": [18,20,20],
                "ambient": [0,0,0],
                "intensity": 0.2,
                "size": 0,
                "useFlare": 0,
                "flareSize": 0,
                "flareMaxDistance": 0,
                "dayLight": 0,
                "blinking": 0,
                # Class: CfgVehicles\MBT_01_base_F\compartmentsLights\Comp1\Light1\Attenuation,
                "Attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardLimitStart": 0.15,
                    "hardLimitEnd": 1.15
                }
            },
            # Class: CfgVehicles\MBT_01_base_F\compartmentsLights\Comp1\Light6,
            "Light6": {
                "point": "light_interior6",
                "color": [18,20,20],
                "ambient": [0,0,0],
                "intensity": 3,
                "size": 0,
                "useFlare": 0,
                "flareSize": 0,
                "flareMaxDistance": 0,
                "dayLight": 0,
                "blinking": 0,
                # Class: CfgVehicles\MBT_01_base_F\compartmentsLights\Comp1\Light1\Attenuation,
                "Attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardLimitStart": 0.15,
                    "hardLimitEnd": 1.15
                }
            },
            # Class: CfgVehicles\MBT_01_base_F\compartmentsLights\Comp1\Light7,
            "Light7": {
                "point": "light_interior7",
                "color": [18,20,20],
                "ambient": [0,0,0],
                "intensity": 4,
                "size": 0,
                "useFlare": 0,
                "flareSize": 0,
                "flareMaxDistance": 0,
                "dayLight": 0,
                "blinking": 0,
                # Class: CfgVehicles\MBT_01_base_F\compartmentsLights\Comp1\Light1\Attenuation,
                "Attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardLimitStart": 0.15,
                    "hardLimitEnd": 1.15
                }
            },
            # Class: CfgVehicles\MBT_01_base_F\compartmentsLights\Comp1\Light8,
            "Light8": {
                "point": "light_interior8",
                "color": [18,20,20],
                "ambient": [0,0,0],
                "intensity": 4,
                "size": 0,
                "useFlare": 0,
                "flareSize": 0,
                "flareMaxDistance": 0,
                "dayLight": 0,
                "blinking": 0,
                # Class: CfgVehicles\MBT_01_base_F\compartmentsLights\Comp1\Light1\Attenuation,
                "Attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardLimitStart": 0.15,
                    "hardLimitEnd": 1.15
                }
            }
        }
    },
    "soundLocked": ["|A3|Sounds_F|weapons|Rockets|opfor_lock_1",1,1],
    "soundIncommingMissile": ["|A3|Sounds_F|vehicles|air|noises|alarm_locked_by_missile_1",0.316228,1],
    "smokeLauncherGrenadeCount": 8,
    "smokeLauncherVelocity": 14,
    "smokeLauncherOnTurret": 1,
    "smokeLauncherAngle": 120,
    "animationList": ["showCamonetCannon",0,"showCamonetPlates1",0,"showCamonetPlates2",0,"showCamonetTurret",0,"showCamonetHull",0],
    # Class: CfgVehicles\MBT_01_base_F\Library,
    "Library": {
        "libTextDesc": "A licensed copy of an Israeli tank built in Central Europe. This tank is built for versatile use on the battlefield and maximal crew protection, which gained significant appreciation from western Europe armies in the 21st century. The M2A1 is armed with 120 mm cannon and a coaxial machinegun and can also be used as mobile artillery. This tank has proven itself in battle and thanks to heavy manufacture, it became the second most wide spread main battle tank of many countries in the world."
    },
    "occludeSoundsWhenIn": 0,
    "obstructSoundsWhenIn": 0,
    "driverCanSee": "1 + 2 + 4 + 8 + 32",
    "gunnerCanSee": "1 + 2 + 4 + 8 + 32",
    "commanderCanSee": "1 + 2 + 4 + 8 + 32",
    "sensorPosition": "gunnerView",
    "audible": 18,
    "sensitivityEar": "0.0075 /3",
    "turnCoef": 5,
    "steerAheadSimul": 0.3,
    "steerAheadPlan": 0.4,
    "brakeDistance": 5,
    "precision": 10,
    "hideProxyInCombat": 1,
    "radarTarget": 1,
    "radarTargetSize": 1.2,
    "visualTarget": 1,
    "visualTargetSize": 1,
    "irTargetSize": 1.2,
    "irScanGround": 2,
    "irScanRangeMax": 0,
    "irScanRangeMin": 0,
    "irScanToEyeFactor": 1,
    "enableRadio": 1,
    "LockDetectionSystem": 0,
    "countermeasureActivationRadius": 2000,
    "memoryPointCargoLight": "cargo light",
    "dampersBumpCoef": 4.5,
    "crewCrashProtection": 0.25,
    "secondaryExplosion": -1,
    "fuelExplosionPower": 1,
    "transportMaxWeapons": 12,
    "transportMaxMagazines": 128,
    "transportMaxBackpacks": 12,
    "maximumLoad": 3000,
    "supplyRadius": -1,
    "memoryPointSupply": "doplnovani",
    # Class: CfgVehicles\Tank_F\CamShake,
    "CamShake": {
        "power": 5,
        "frequency": 20,
        "distance": 20,
        "minSpeed": 5
    },
    "camShakeCoef": 0,
    # Class: CfgVehicles\Tank_F\Components,
    "Components": {
        # Class: CfgVehicles\Tank_F\Components\VehicleSystemsDisplayManagerComponentLeft
        "VehicleSystemsDisplayManagerComponentLeft": {
            # Class: VehicleSystemsTemplateLeftDriver\Components
            "Components": {
                # Class: VehicleSystemsTemplateLeftDriver\Components\VehiclePrimaryGunnerDisplay
                "VehiclePrimaryGunnerDisplay": {
                    "componentType": "TransportFeedDisplayComponent",
                    "source": "PrimaryGunner"
                },
                # Class: VehicleSystemsTemplateLeftDriver\Components\VehicleCommanderDisplay,
                "VehicleCommanderDisplay": {
                    "componentType": "TransportFeedDisplayComponent",
                    "source": "Commander"
                },
                # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\EmptyDisplay,
                "EmptyDisplay": {
                    "componentType": "EmptyDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\MinimapDisplay,
                "MinimapDisplay": {
                    "componentType": "MinimapDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\MineDetectorDisplay,
                "MineDetectorDisplay": {
                    "componentType": "MineDetectorDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\CrewDisplay,
                "CrewDisplay": {
                    "componentType": "CrewDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\UAVDisplay,
                "UAVDisplay": {
                    "componentType": "UAVFeedDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\SlingLoadDisplay,
                "SlingLoadDisplay": {
                    "componentType": "SlingLoadDisplayComponent"
                }
            },
            "componentType": "VehicleSystemsDisplayManager",
            "left": 1,
            "defaultDisplay": "EmptyDisplay",
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,	(safezoneX + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
        },
        # Class: CfgVehicles\Tank_F\Components\VehicleSystemsDisplayManagerComponentRight,
        "VehicleSystemsDisplayManagerComponentRight": {
            # Class: VehicleSystemsTemplateRightDriver\Components
            "Components": {
                # Class: VehicleSystemsTemplateRightDriver\Components\VehiclePrimaryGunnerDisplay
                "VehiclePrimaryGunnerDisplay": {
                    "componentType": "TransportFeedDisplayComponent",
                    "source": "PrimaryGunner"
                },
                # Class: VehicleSystemsTemplateRightDriver\Components\VehicleCommanderDisplay,
                "VehicleCommanderDisplay": {
                    "componentType": "TransportFeedDisplayComponent",
                    "source": "Commander"
                },
                # Class: DefaultVehicleSystemsDisplayManagerRight\Components\EmptyDisplay,
                "EmptyDisplay": {
                    "componentType": "EmptyDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerRight\Components\MinimapDisplay,
                "MinimapDisplay": {
                    "componentType": "MinimapDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerRight\Components\MineDetectorDisplay,
                "MineDetectorDisplay": {
                    "componentType": "MineDetectorDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerRight\Components\CrewDisplay,
                "CrewDisplay": {
                    "componentType": "CrewDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerRight\Components\UAVDisplay,
                "UAVDisplay": {
                    "componentType": "UAVFeedDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerRight\Components\SlingLoadDisplay,
                "SlingLoadDisplay": {
                    "componentType": "SlingLoadDisplayComponent"
                }
            },
            "componentType": "VehicleSystemsDisplayManager",
            "right": 1,
            "defaultDisplay": "EmptyDisplay",
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,	((safezoneX + safezoneW) - (		(10 * 			(			((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40)))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
        },
        # Class: CfgVehicles\Tank_F\Components\AITankSteeringComponent,
        "AITankSteeringComponent": {
            "steeringPIDWeights": [2.9,0.1,0.2],
            "speedPIDWeights": [0.7,0.2,0],
            "doRemapSpeed": 0,
            "remapSpeedRange": [30,70],
            "remapSpeedScalar": [1,0.35],
            "doPredictForward": 1,
            "predictForwardRange": [1,20],
            "steerAheadSaturation": [0.01,0.4],
            "speedPredictionMethod": 3,
            "wheelAngleCoef": 0.7,
            "forwardAngleCoef": 0.7,
            "steeringAngleCoef": 1,
            "differenceAngleCoef": 1,
            "stuckMaxTime": 3,
            "allowOvertaking": 1,
            "allowCollisionAvoidance": 1,
            "allowDrifting": 0,
            "maxWheelAngleDiff": 0.2616,
            "minSpeedToKeep": 0.01,
            "commandTurnFactor": 2,
            "allowTurnAroundInPoint": 1,
            "convoyPIDWeights": [1,0,0],
            "predictForwardMaxSpeed": 15
        },
        # Class: CfgVehicles\LandVehicle\Components\TransportCountermeasuresComponent,
        "TransportCountermeasuresComponent": {
        }
    },
    # Class: CfgVehicles\Tank_F\NVGMarkers,
    "NVGMarkers": {
        # Class: CfgVehicles\Tank_F\NVGMarkers\NVGMarker01
        "NVGMarker01": {
            "name": "nvg_marker",
            "color": [0.03,0.003,0.003,1],
            "ambient": [0.003,0.0003,0.0003,1],
            "brightness": 0.001,
            "blinking": 1
        }
    },
    "memoryPointDriverOptics": "driverview",
    "engineStartSpeed": 5,
    "explosionEffect": "FuelExplosionBig",
    "htMin": 60,
    "htMax": 1800,
    "afMax": 100,
    "mfMax": 80,
    "mFact": 1,
    "tBody": 250,
    "numberPhysicalWheels": 16,
    "getInRadius": 3.5,
    "hullDamageCauseExplosion": 1,
    "selectionFireAnim": "zasleh",
    "bounding": "usti hlavne",
    "fireDustEffect": "FDustEffects",
    "gearBox": [-7,0,11,8,5.7,4.2],
    "alphaTracks": 0.7,
    "textureTrackWheel": 0,
    "memoryPointTrack1L": "Stopa LL",
    "memoryPointTrack1R": "Stopa LR",
    "memoryPointTrack2L": "Stopa RL",
    "memoryPointTrack2R": "Stopa RR",
    "predictTurnSimul": 1.2,
    "predictTurnPlan": 1,
    "soundGear": ["",0.000316228,1],
    "outsideSoundFilter": 1,
    "nightVision": 0,
    "formationX": 20,
    "formationZ": 30,
    "canFloat": 0,
    "type": 1,
    "camouflage": 8,
    "driverOpticsColor": [1,1,1,1],
    # Class: CfgVehicles\Tank\CargoLight,
    "CargoLight": {
        "color": [0,0,0,0],
        "ambient": [0.6,0,0.15,1],
        "brightness": 0.007
    },
    "enableGPS": 1,
    "mapSize": 1.21,
    # Class: CfgVehicles\Tank\SpeechVariants,
    "SpeechVariants": {
        # Class: CfgVehicles\Tank\SpeechVariants\Default
        "Default": {
            "speechSingular": ["veh_vehicle_tank_s"],
            "speechPlural": ["veh_vehicle_tank_p"]
        }
    },
    "textSingular": "tank",
    "textPlural": "tanks",
    "nameSound": "veh_vehicle_tank_s",
    "memoryPointTaskMarkerOffset": [0,0.3,0],
    "rightDustEffects": [["GdtKLDirt","RDustEffects"],["GdtKLGrass1","RDustEffects"],["GdtKLGrass1","RGrassEffects"],["GdtKLGrass2","RDustEffects"],["GdtKLGrass2","RGrassEffects"],["GdtKLForestCon","RDustEffects"],["GdtKLForestDec","RDustEffects"],["GdtKlMud","RDustEffects"],["GdtKlSoil","RDustEffects"],["GdtKlTarmac","RDustEffects"],["GdtKlStubble","RDustEffects"],["GdtKlStones","RStonesEffects"],["SurfRoadDirt_Enoch","RDustEffects"],["SurfTrailDirt_Enoch","RDustEffects"],["SurfRoadTarmac1_Enoch","RDustEffects"],["SurfRoadTarmac2_Enoch","RDustEffects"],["SurfRoadTarmac3_Enoch","RDustEffects"],["GdtGrassShort","RDustEffects"],["GdtGrassShort","RGrassEffectsBig"],["GdtGrassTall","RDustEffects"],["GdtGrassTall","RGrassEffectsBig"],["GdtRedDirt","RDustEffectsRed"],["GdtField","RDustEffects"],["GdtForest","RDustEffects"],["GdtVolcano","RDustEffects"],["GdtVolcano","RStonesEffectsBig"],["GdtCliff","RDustEffects"],["GdtVolcanoBeach","RDustEffects"],["SurfRoadDirt_exp","RDustEffectsRed"],["SurfRoadConcrete_exp","RDustEffects"],["SurfRoadTarmac_exp","RDustEffects"],["GdtStratisConcrete","RDustEffects"],["GdtStratisConcrete","RDirtEffectsBig"],["GdtStratisBeach","RDustEffects"],["GdtStratisBeach","RStonesEffectsBig"],["GdtStratisDirt","RDustEffects"],["GdtStratisDirt","RDirtEffectsBig"],["GdtStratisSeabedCluttered","RDustEffects"],["GdtStratisSeabed","RDustEffects"],["GdtStratisDryGrass","RDustEffects"],["GdtStratisDryGrass","RGrassEffectsDryBig"],["GdtStratisDryGrass","RDirtEffectsBig"],["GdtStratisGreenGrass","RDustEffects"],["GdtStratisGreenGrass","RGrassEffectsBig"],["GdtStratisGreenGrass","RDirtEffectsBig"],["GdtStratisRocky","RDustEffects"],["GdtStratisRocky","RGrassEffectsBig"],["GdtStratisRocky","RDirtEffectsBig"],["GdtStratisThistles","RDustEffects"],["GdtStratisThistles","RGrassEffectsBig"],["GdtStratisThistles","RDirtEffectsBig"],["GdtConcrete","RDustEffects"],["GdtConcrete","RDirtEffectsBig"],["GdtAsphalt","RDustEffects"],["GdtAsphalt","RDirtEffectsBig"],["GdtRubble","RDustEffects"],["GdtRubble","RDirtEffectsBig"],["GdtSoil","RDustEffects"],["GdtSoil","RDirtEffectsBig"],["GdtBeach","RDustEffects"],["GdtBeach","RStonesEffectsBig"],["GdtRock","RDustEffects"],["GdtRock","RDirtEffectsBig"],["GdtDead","RDustEffects"],["GdtDead","RDirtEffectsBig"],["Default","RDustEffects"],["GdtDesert","RDustEffects"],["GdtDesert","RDirtEffectsBig"],["GdtDesert","RStonesEffects"],["GdtDesert1","RDustEffects"],["GdtDesert1","RDirtEffectsBig"],["GdtDesert1","RStonesEffectsBig"],["GdtDesert2","RDustEffects"],["GdtDesert2","RGrassEffectsBig"],["GdtDesert2","RDirtEffectsBig"],["GdtDirt","RDustEffects"],["GdtDirt","RDirtEffectsBig"],["GdtGrassGreen","RDustEffects"],["GdtGrassGreen","RGrassEffectsBig"],["GdtGrassGreen","RDirtEffectsBig"],["GdtGrassDry","RDustEffects"],["GdtGrassDry","RGrassEffectsDryBig"],["GdtGrassDry","RDirtEffectsBig"],["GdtGrassWild","RDustEffects"],["GdtGrassWild","RGrassEffectsBig"],["GdtGrassWild","RDirtEffectsBig"],["GdtWildField","RDustEffects"],["GdtWildField","RGrassEffectsBig"],["GdtWildField","RDirtEffectsBig"],["GdtWeed1","RDustEffects"],["GdtWeed1","RGrassEffectsBig"],["GdtWeed1","RDirtEffectsBig"],["GdtWeed2","RDustEffects"],["GdtWeed2","RGrassEffectsBig"],["GdtWeed2","RDirtEffectsBig"],["GdtThorn","RDustEffects"],["GdtThorn","RGrassEffectsBig"],["GdtThorn","RDirtEffectsBig"],["GdtStony","RDustEffects"],["GdtStony","RGrassEffectsBig"],["GdtStony","RDirtEffectsBig"],["GdtStonyGreen","RDustEffects"],["GdtStonyGreen","RGrassEffectsBig"],["GdtStonyGreen","RDirtEffectsBig"],["GdtStonyThistle","RDustEffects"],["GdtStonyThistle","RGrassEffectsBig"],["GdtStonyThistle","RDirtEffectsBig"],["GdtSeabedDeep","RDustEffects"],["GdtSeabed","RDustEffects"],["SurfRoadDirt","RDustEffects"],["SurfRoadConcrete","RDustEffects"],["SurfRoadTarmac","RDustEffects"],["SurfWood","RDustEffects"],["SurfMetal","RDustEffects"],["SurfRoofTin","RDustEffects"],["SurfRoofTiles","RDustEffects"],["SurfIntWood","RDustEffects"],["SurfIntConcrete","RDustEffects"],["SurfIntTiles","RDustEffects"],["SurfIntMetal","RDustEffects"],["dirtrunway","RDustEffects"]],
    "leftDustEffects": [["GdtKLDirt","LDustEffects"],["GdtKLGrass1","LDustEffects"],["GdtKLGrass1","LGrassEffects"],["GdtKLGrass2","LDustEffects"],["GdtKLGrass2","LGrassEffects"],["GdtKLForestCon","LDustEffects"],["GdtKLForestDec","LDustEffects"],["GdtKlMud","LDustEffects"],["GdtKlSoil","LDustEffects"],["GdtKlTarmac","LDustEffects"],["GdtKlStubble","LDustEffects"],["GdtKlStones","LStonesEffects"],["SurfRoadDirt_Enoch","LDustEffects"],["SurfTrailDirt_Enoch","LDustEffects"],["SurfRoadTarmac1_Enoch","LDustEffects"],["SurfRoadTarmac2_Enoch","LDustEffects"],["SurfRoadTarmac3_Enoch","LDustEffects"],["GdtGrassShort","LDustEffects"],["GdtGrassShort","LGrassEffectsBig"],["GdtGrassTall","LDustEffects"],["GdtGrassTall","LGrassEffectsBig"],["GdtRedDirt","LDustEffectsRed"],["GdtField","LDustEffects"],["GdtForest","LDustEffects"],["GdtVolcano","LDustEffects"],["GdtVolcano","LStonesEffectsBig"],["GdtCliff","LDustEffects"],["GdtVolcanoBeach","LDustEffects"],["SurfRoadDirt_exp","LDustEffectsRed"],["SurfRoadConcrete_exp","LDustEffects"],["SurfRoadTarmac_exp","LDustEffects"],["GdtStratisConcrete","LDustEffects"],["GdtStratisConcrete","LDirtEffectsBig"],["GdtStratisBeach","LDustEffects"],["GdtStratisBeach","LStonesEffectsBig"],["GdtStratisDirt","LDustEffects"],["GdtStratisDirt","LDirtEffectsBig"],["GdtStratisSeabedCluttered","LDustEffects"],["GdtStratisSeabed","LDustEffects"],["GdtStratisDryGrass","LDustEffects"],["GdtStratisDryGrass","LGrassEffectsDryBig"],["GdtStratisDryGrass","LDirtEffectsBig"],["GdtStratisGreenGrass","LDustEffects"],["GdtStratisGreenGrass","LGrassEffectsBig"],["GdtStratisGreenGrass","LDirtEffectsBig"],["GdtStratisRocky","LDustEffects"],["GdtStratisRocky","LGrassEffectsBig"],["GdtStratisRocky","LDirtEffectsBig"],["GdtStratisThistles","LDustEffects"],["GdtStratisThistles","LGrassEffectsBig"],["GdtStratisThistles","LDirtEffectsBig"],["GdtConcrete","LDustEffects"],["GdtConcrete","LDirtEffectsBig"],["GdtAsphalt","LDustEffects"],["GdtAsphalt","LDirtEffectsBig"],["GdtRubble","LDustEffects"],["GdtRubble","LGrassEffectsBig"],["GdtRubble","LDirtEffectsBig"],["GdtSoil","LDustEffects"],["GdtSoil","LDirtEffectsBig"],["GdtBeach","LDustEffects"],["GdtBeach","LStonesEffectsBig"],["GdtRock","LDustEffects"],["GdtRock","LDirtEffectsBig"],["GdtDead","LDustEffects"],["GdtDead","LDirtEffectsBig"],["Default","LDustEffects"],["GdtDesert","LDustEffects"],["GdtDesert","LDirtEffectsBig"],["GdtDesert","LStonesEffects"],["GdtDesert1","LDustEffects"],["GdtDesert1","LDirtEffectsBig"],["GdtDesert1","LStonesEffectsBig"],["GdtDesert2","LDustEffects"],["GdtDesert2","LGrassEffectsBig"],["GdtDesert2","LDirtEffectsBig"],["GdtDirt","LDustEffects"],["GdtDirt","LDirtEffectsBig"],["GdtGrassGreen","LDustEffects"],["GdtGrassGreen","LGrassEffectsBig"],["GdtGrassGreen","LDirtEffectsBig"],["GdtGrassDry","LDustEffects"],["GdtGrassDry","LGrassEffectsDryBig"],["GdtGrassDry","LDirtEffectsBig"],["GdtGrassWild","LDustEffects"],["GdtGrassWild","LGrassEffectsBig"],["GdtGrassWild","LDirtEffectsBig"],["GdtWildField","LDustEffects"],["GdtWildField","LGrassEffectsBig"],["GdtWildField","LDirtEffectsBig"],["GdtWeed1","LDustEffects"],["GdtWeed1","LGrassEffectsBig"],["GdtWeed1","LDirtEffectsBig"],["GdtWeed2","LDustEffects"],["GdtWeed2","LGrassEffectsBig"],["GdtWeed2","LDirtEffectsBig"],["GdtThorn","LDustEffects"],["GdtThorn","LGrassEffectsBig"],["GdtThorn","LDirtEffectsBig"],["GdtStony","LDustEffects"],["GdtStony","LGrassEffectsBig"],["GdtStony","LDirtEffectsBig"],["GdtStonyGreen","LDustEffects"],["GdtStonyGreen","LGrassEffectsBig"],["GdtStonyGreen","LDirtEffectsBig"],["GdtStonyThistle","LDustEffects"],["GdtStonyThistle","LGrassEffectsBig"],["GdtStonyThistle","LDirtEffectsBig"],["GdtSeabedDeep","LDustEffects"],["GdtSeabed","LDustEffects"],["SurfRoadDirt","LDustEffects"],["SurfRoadConcrete","LDustEffects"],["SurfRoadTarmac","LDustEffects"],["SurfWood","LDustEffects"],["SurfMetal","LDustEffects"],["SurfRoofTin","LDustEffects"],["SurfRoofTiles","LDustEffects"],["SurfIntWood","LDustEffects"],["SurfIntConcrete","LDustEffects"],["SurfIntTiles","LDustEffects"],["SurfIntMetal","LDustEffects"],["dirtrunway","RDustEffects"]],
    # Class: CfgVehicles\Tank\DestructionEffects,
    "DestructionEffects": {
        # Class: CfgVehicles\Tank\DestructionEffects\LightBig1
        "LightBig1": {
            "simulation": "light",
            "type": "ObjectDestructionLight",
            "position": "destructionEffect1",
            "intensity": 0.001,
            "interval": 1,
            "lifeTime": 3,
            "enabled": "distToWater"
        },
        # Class: CfgVehicles\Tank\DestructionEffects\Sound,
        "Sound": {
            "simulation": "sound",
            "position": "destructionEffect1",
            "intensity": 1,
            "interval": 1,
            "lifeTime": 1,
            "type": "Fire"
        },
        # Class: CfgVehicles\Tank\DestructionEffects\FireBig1,
        "FireBig1": {
            "simulation": "particles",
            "type": "ObjectDestructionFire1",
            "position": "destructionEffect1",
            "intensity": 0.15,
            "interval": 1,
            "lifeTime": 3
        },
        # Class: CfgVehicles\Tank\DestructionEffects\Refract1,
        "Refract1": {
            "simulation": "particles",
            "type": "ObjectDestructionRefract",
            "position": "destructionEffect1",
            "intensity": 0.15,
            "interval": 1,
            "lifeTime": 3
        },
        # Class: CfgVehicles\Tank\DestructionEffects\SmokeBig1,
        "SmokeBig1": {
            "simulation": "particles",
            "type": "ObjectDestructionSmoke",
            "position": "destructionEffect1",
            "intensity": 0.15,
            "interval": 1,
            "lifeTime": 3.5
        },
        # Class: CfgVehicles\Tank\DestructionEffects\SparksBig1,
        "SparksBig1": {
            "simulation": "particles",
            "type": "ObjectDestructionSparks",
            "position": "destructionEffect1",
            "intensity": 0,
            "interval": 1,
            "lifeTime": 0
        },
        # Class: CfgVehicles\Tank\DestructionEffects\FireSparksBig1,
        "FireSparksBig1": {
            "simulation": "particles",
            "type": "FireSparks",
            "position": "destructionEffect2",
            "intensity": 1,
            "interval": 1,
            "lifeTime": 2.8
        },
        # Class: CfgVehicles\Tank\DestructionEffects\FireBig2,
        "FireBig2": {
            "simulation": "particles",
            "type": "ObjectDestructionFire2",
            "position": "destructionEffect2",
            "intensity": 0.15,
            "interval": 1,
            "lifeTime": 3
        },
        # Class: CfgVehicles\Tank\DestructionEffects\SmokeBig1_2,
        "SmokeBig1_2": {
            "simulation": "particles",
            "type": "ObjectDestructionSmoke1_2",
            "position": "destructionEffect2",
            "intensity": 0.15,
            "interval": 1,
            "lifeTime": 3.5
        },
        # Class: CfgVehicles\Tank\DestructionEffects\SmokeBig2,
        "SmokeBig2": {
            "simulation": "particles",
            "type": "ObjectDestructionSmoke2",
            "position": "destructionEffect2",
            "intensity": 1,
            "interval": 1,
            "lifeTime": 3.2
        }
    },
    "headGforceLeaningFactor": [0.0075,0.005,0.0075],
    "selectionBrakeLights": "brzdove svetlo",
    "memoryPointMissile": ["spice rakety","usti hlavne"],
    "memoryPointMissileDir": ["konec rakety","konec hlavne"],
    "leftDustEffect": "LDustEffects",
    "rightDustEffect": "RDustEffects",
    "leftWaterEffect": "LWaterEffects",
    "rightWaterEffect": "RWaterEffects",
    "leftFastWaterEffect": "LWaterEffects",
    "rightFastWaterEffect": "RWaterEffects",
    "selectionLeftOffset": "PasOffsetL",
    "selectionRightOffset": "PasOffsetP",
    # Class: CfgVehicles\LandVehicle\CommanderOptics,
    "CommanderOptics": {
        "proxyType": "CPCommander",
        "proxyIndex": 1,
        "gunnerName": "Commander",
        "primaryGunner": 0,
        "primaryObserver": 1,
        "stabilizedInAxes": 0,
        "body": "obsTurret",
        "gun": "obsGun",
        "animationSourceBody": "obsTurret",
        "animationSourceGun": "obsGun",
        "animationSourceHatch": "hatchCommander",
        "animationSourceCamElev": "camElev",
        "soundServo": ["A3|sounds_f|dummysound",0.01,1,10],
        "gunBeg": "",
        "gunEnd": "",
        "minElev": -4,
        "maxElev": 20,
        "initElev": 0,
        "minTurn": -360,
        "maxTurn": 360,
        "initTurn": 0,
        "commanding": 2,
        "outGunnerMayFire": 1,
        "inGunnerMayFire": 1,
        "viewGunnerInExternal": 0,
        "gunnerOpticsModel": "A3|weapons_f|reticle|Optics_Commander_02_F",
        "gunnerOutOpticsModel": "A3|weapons_f|reticle|optics_empty",
        "gunnerOutOpticsColor": [0,0,0,1],
        "gunnerOutForceOptics": 0,
        "gunnerOutOpticsShowCursor": 0,
        "gunnerOpticsEffect": [],
        "gunnerOutOpticsEffect": [],
        "memoryPointGunnerOutOptics": "commander_weapon_view",
        "memoryPointGunnerOptics": "commanderview",
        "memoryPointsGetInGunner": "pos commander",
        "memoryPointsGetInGunnerDir": "pos commander dir",
        "gunnerGetInAction": "GetInHigh",
        "gunnerGetOutAction": "GetOutHigh",
        "memoryPointGun": "gun_muzzle",
        "selectionFireAnim": "zasleh_1",
        # Class: CfgVehicles\LandVehicle\CommanderOptics\ViewOptics,
        "ViewOptics": {
            "initAngleX": 0,
            "minAngleX": -30,
            "maxAngleX": 30,
            "initAngleY": 0,
            "minAngleY": -100,
            "maxAngleY": 100,
            "initFov": 0.3,
            "minFov": 0.07,
            "maxFov": 0.35,
            "minMoveX": 0,
            "maxMoveX": 0,
            "minMoveY": 0,
            "maxMoveY": 0,
            "minMoveZ": 0,
            "maxMoveZ": 0,
            "speedZoomMaxSpeed": 1e+010,
            "speedZoomMaxFOV": 0
        },
        # Class: CfgVehicles\LandVehicle\CommanderOptics\ViewGunner,
        "ViewGunner": {
            "initAngleX": 5,
            "minAngleX": -75,
            "maxAngleX": 85,
            "initAngleY": 0,
            "minAngleY": -150,
            "maxAngleY": 150,
            "minFov": 0.25,
            "maxFov": 1.25,
            "initFov": 0.75,
            "minMoveX": 0,
            "maxMoveX": 0,
            "minMoveY": 0,
            "maxMoveY": 0,
            "minMoveZ": 0,
            "maxMoveZ": 0,
            "speedZoomMaxSpeed": 1e+010,
            "speedZoomMaxFOV": 0
        },
        "gunnerType": "",
        "weapons": [],
        "magazines": [],
        "soundElevation": ["",0.00316228,1],
        "minOutElev": -4,
        "maxOutElev": 20,
        "initOutElev": 0,
        "minOutTurn": -60,
        "maxOutTurn": 60,
        "initOutTurn": 0,
        "maxHorizontalRotSpeed": 1.2,
        "maxVerticalRotSpeed": 1.2,
        "minCamElev": -90,
        "maxCamElev": 90,
        "initCamElev": 0,
        "primary": 1,
        "hasGunner": 1,
        "turretCanSee": 0,
        "canUseScanners": 1,
        # Class: CfgVehicles\AllVehicles\NewTurret\TurretSpec,
        "TurretSpec": {
            "showHeadPhones": 0
        },
        "gunnerOpticsColor": [0,0,0,1],
        "gunnerForceOptics": 1,
        "gunnerOpticsShowCursor": 0,
        "turretInfoType": "",
        "gunnerFireAlsoInInternalCamera": 1,
        "gunnerOutFireAlsoInInternalCamera": 1,
        "gunnerUsesPilotView": 0,
        "castGunnerShadow": 0,
        "viewGunnerShadow": 1,
        "viewGunnerShadowDiff": 1,
        "viewGunnerShadowAmb": 1,
        "ejectDeadGunner": 0,
        "hideWeaponsGunner": 1,
        "canHideGunner": -1,
        "forceHideGunner": 0,
        "showHMD": 0,
        "lockWhenDriverOut": 0,
        "lockWhenVehicleSpeed": -1,
        "gunnerCompartments": "Compartment1",
        "LODTurnedIn": -1,
        "LODTurnedOut": -1,
        "startEngine": 1,
        "memoryPointsGetInGunnerPrecise": "",
        "missileBeg": "spice rakety",
        "missileEnd": "konec rakety",
        "armorLights": 0.4,
        # Class: CfgVehicles\AllVehicles\NewTurret\Reflectors,
        "Reflectors": {
        },
        "aggregateReflectors": [],
        # Class: CfgVehicles\AllVehicles\NewTurret\GunFire,
        "GunFire": {
            "access": 0,
            "cloudletDuration": 0.2,
            "cloudletAnimPeriod": 1,
            "cloudletSize": 1,
            "cloudletAlpha": 1,
            "cloudletGrowUp": 0.2,
            "cloudletFadeIn": 0.01,
            "cloudletFadeOut": 0.5,
            "cloudletAccY": 0,
            "cloudletMinYSpeed": -100,
            "cloudletMaxYSpeed": 100,
            "cloudletShape": "cloudletFire",
            "cloudletColor": [1,1,1,0],
            "interval": 0.01,
            "size": 3,
            "sourceSize": 0.5,
            "timeToLive": 0,
            "initT": 4500,
            "deltaT": -3000,
            # Class: WeaponFireGun\Table,
            "Table": {
                # Class: WeaponFireGun\Table\T0
                "T0": {
                    "maxT": 0,
                    "color": [0.82,0.95,0.93,0]
                },
                # Class: WeaponFireGun\Table\T1,
                "T1": {
                    "maxT": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: WeaponFireGun\Table\T2,
                "T2": {
                    "maxT": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: WeaponFireGun\Table\T3,
                "T3": {
                    "maxT": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: WeaponFireGun\Table\T4,
                "T4": {
                    "maxT": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: WeaponFireGun\Table\T5,
                "T5": {
                    "maxT": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: WeaponFireGun\Table\T6,
                "T6": {
                    "maxT": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: WeaponFireGun\Table\T7,
                "T7": {
                    "maxT": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: WeaponFireGun\Table\T8,
                "T8": {
                    "maxT": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: WeaponFireGun\Table\T9,
                "T9": {
                    "maxT": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: WeaponFireGun\Table\T10,
                "T10": {
                    "maxT": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: WeaponFireGun\Table\T11,
                "T11": {
                    "maxT": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: WeaponFireGun\Table\T12,
                "T12": {
                    "maxT": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: WeaponFireGun\Table\T13,
                "T13": {
                    "maxT": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: WeaponFireGun\Table\T14,
                "T14": {
                    "maxT": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: WeaponFireGun\Table\T15,
                "T15": {
                    "maxT": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: WeaponFireGun\Table\T16,
                "T16": {
                    "maxT": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: WeaponFireGun\Table\T17,
                "T17": {
                    "maxT": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: WeaponFireGun\Table\T18,
                "T18": {
                    "maxT": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: WeaponFireGun\Table\T19,
                "T19": {
                    "maxT": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: WeaponFireGun\Table\T20,
                "T20": {
                    "maxT": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: WeaponFireGun\Table\T21,
                "T21": {
                    "maxT": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: WeaponFireGun\Table\T22,
                "T22": {
                    "maxT": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\GunClouds,
        "GunClouds": {
            "access": 0,
            "cloudletDuration": 0.3,
            "cloudletAnimPeriod": 1,
            "cloudletSize": 1,
            "cloudletAlpha": 1,
            "cloudletGrowUp": 1,
            "cloudletFadeIn": 0.01,
            "cloudletFadeOut": 1,
            "cloudletAccY": 0.4,
            "cloudletMinYSpeed": 0.2,
            "cloudletMaxYSpeed": 0.8,
            "cloudletShape": "cloudletClouds",
            "cloudletColor": [1,1,1,0],
            "interval": 0.05,
            "size": 3,
            "sourceSize": 0.5,
            "timeToLive": 0,
            "initT": 0,
            "deltaT": 0,
            # Class: WeaponCloudsGun\Table,
            "Table": {
                # Class: WeaponCloudsGun\Table\T0
                "T0": {
                    "maxT": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\MGunClouds,
        "MGunClouds": {
            "access": 0,
            "cloudletGrowUp": 0.05,
            "cloudletFadeIn": 0,
            "cloudletFadeOut": 0.1,
            "cloudletDuration": 0.05,
            "cloudletAnimPeriod": 1,
            "cloudletSize": 1,
            "cloudletAlpha": 0.3,
            "cloudletAccY": 0,
            "cloudletMinYSpeed": -100,
            "cloudletMaxYSpeed": 100,
            "cloudletShape": "cloudletClouds",
            "cloudletColor": [1,1,1,0],
            "timeToLive": 0,
            "interval": 0.02,
            "size": 0.3,
            "sourceSize": 0.02,
            "initT": 0,
            "deltaT": 0,
            # Class: WeaponCloudsMGun\Table,
            "Table": {
                # Class: WeaponCloudsMGun\Table\T0
                "T0": {
                    "maxT": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\HitPoints,
        "HitPoints": {
            # Class: CfgVehicles\AllVehicles\NewTurret\HitPoints\HitTurret
            "HitTurret": {
                "armor": 0.8,
                "material": 51,
                "name": "turret",
                "visual": "turret",
                "passThrough": 1,
                "explosionShielding": 1
            },
            # Class: CfgVehicles\AllVehicles\NewTurret\HitPoints\HitGun,
            "HitGun": {
                "armor": 0.6,
                "material": 52,
                "name": "gun",
                "visual": "gun",
                "passThrough": 1,
                "explosionShielding": 1
            }
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\Turrets,
        "Turrets": {
        },
        "forceNVG": 0,
        "isCopilot": 0,
        "canEject": 1,
        "gunnerLeftHandAnimName": "",
        "gunnerRightHandAnimName": "",
        "gunnerLeftLegAnimName": "",
        "gunnerRightLegAnimName": "",
        "gunnerDoor": "",
        "preciseGetInOut": 0,
        "turretFollowFreeLook": 0,
        "allowTabLock": 1,
        "showAllTargets": 0,
        "dontCreateAI": 0,
        "disableSoundAttenuation": 0,
        "slingLoadOperator": 0,
        "playerPosition": 0,
        "allowLauncherIn": 0,
        "allowLauncherOut": 0,
        # Class: CfgVehicles\AllVehicles\NewTurret\TurnIn,
        "TurnIn": {
            "turnOffset": 0
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\TurnOut,
        "TurnOut": {
            "turnOffset": 0
        },
        "gunnerInAction": "ManActTestDriver",
        "gunnerAction": "ManActTestDriver",
        "showCrewAim": 0
    },
    "wheelDamageThreshold": 0.2,
    "wheelDestroyThreshold": 0.99,
    "wheelDamageRadiusCoef": 0.9,
    "wheelDestroyRadiusCoef": 0.4,
    "weaponsGroup1": 1,
    "weaponsGroup2": "2 + 		4",
    "weaponsGroup3": "8 + 	16 + 	32",
    "weaponsGroup4": "64 + 		128",
    # Class: CfgVehicles\AllVehicles\SquadTitles,
    "SquadTitles": {
        "name": "clan_sign",
        "color": [0,0,0,0.75]
    },
    "memoryPointsGetInDriver": "pos driver",
    "memoryPointsGetInDriverDir": "pos driver dir",
    "memoryPointsGetInCargo": "pos cargo",
    "memoryPointsGetInCargoDir": "pos cargo dir",
    "memoryPointsGetInCoDriver": "pos codriver",
    "memoryPointsGetInCoDriverDir": "pos codriver dir",
    "memoryPointsGetInDriverPrecise": "pos driver",
    "memoryPointsGetInCargoPrecise": ["pos cargo"],
    "memoryPointsLeftWaterEffect": "waterEffectL",
    "memoryPointsRightWaterEffect": "waterEffectR",
    "selectionClan": "clan",
    "selectionDashboard": "podsvit pristroju",
    "selectionShowDamage": "poskozeni",
    "selectionBackLights": "zadni svetlo",
    # Class: CfgVehicles\AllVehicles\NewTurret,
    "NewTurret": {
        "body": "mainTurret",
        "gun": "mainGun",
        "animationSourceBody": "mainTurret",
        "animationSourceGun": "mainGun",
        "animationSourceHatch": "hatchGunner",
        "animationSourceCamElev": "camElev",
        "proxyType": "CPGunner",
        "proxyIndex": 1,
        "gunnerName": "Gunner",
        "gunnerType": "",
        "primaryGunner": 1,
        "primaryObserver": 0,
        "weapons": [],
        "magazines": [],
        "soundServo": ["",0.00316228,1],
        "soundElevation": ["",0.00316228,1],
        "minElev": -4,
        "maxElev": 20,
        "initElev": 0,
        "minTurn": -360,
        "maxTurn": 360,
        "initTurn": 0,
        "minOutElev": -4,
        "maxOutElev": 20,
        "initOutElev": 0,
        "minOutTurn": -60,
        "maxOutTurn": 60,
        "initOutTurn": 0,
        "maxHorizontalRotSpeed": 1.2,
        "maxVerticalRotSpeed": 1.2,
        "minCamElev": -90,
        "maxCamElev": 90,
        "initCamElev": 0,
        "stabilizedInAxes": 3,
        "primary": 1,
        "hasGunner": 1,
        "commanding": 1,
        "gunnerGetInAction": "",
        "gunnerGetOutAction": "",
        "turretCanSee": 0,
        "canUseScanners": 1,
        # Class: CfgVehicles\AllVehicles\NewTurret\ViewGunner,
        "ViewGunner": {
            "initAngleX": 5,
            "minAngleX": -75,
            "maxAngleX": 85,
            "initAngleY": 0,
            "minAngleY": -150,
            "maxAngleY": 150,
            "minFov": 0.25,
            "maxFov": 1.25,
            "initFov": 0.75,
            "minMoveX": 0,
            "maxMoveX": 0,
            "minMoveY": 0,
            "maxMoveY": 0,
            "minMoveZ": 0,
            "maxMoveZ": 0,
            "continuous": 0,
            "speedZoomMaxSpeed": 1e+010,
            "speedZoomMaxFOV": 0
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\TurretSpec,
        "TurretSpec": {
            "showHeadPhones": 0
        },
        "gunnerOpticsModel": "",
        "gunnerOpticsColor": [0,0,0,1],
        "gunnerForceOptics": 1,
        "gunnerOpticsShowCursor": 0,
        "turretInfoType": "",
        "gunnerOutOpticsModel": "",
        "gunnerOutOpticsColor": [0,0,0,1],
        "gunnerOpticsEffect": [],
        "gunnerOutOpticsEffect": [],
        "memoryPointGunnerOutOptics": "",
        "gunnerOutForceOptics": 0,
        "gunnerOutOpticsShowCursor": 0,
        "gunnerFireAlsoInInternalCamera": 1,
        "gunnerOutFireAlsoInInternalCamera": 1,
        "gunnerUsesPilotView": 0,
        "castGunnerShadow": 0,
        "viewGunnerShadow": 1,
        "viewGunnerShadowDiff": 1,
        "viewGunnerShadowAmb": 1,
        "ejectDeadGunner": 0,
        "hideWeaponsGunner": 1,
        "canHideGunner": -1,
        "forceHideGunner": 0,
        "outGunnerMayFire": 0,
        "inGunnerMayFire": 1,
        "showHMD": 0,
        "viewGunnerInExternal": 0,
        "lockWhenDriverOut": 0,
        "lockWhenVehicleSpeed": -1,
        "gunnerCompartments": "Compartment1",
        "LODTurnedIn": -1,
        "LODTurnedOut": -1,
        "startEngine": 1,
        "memoryPointsGetInGunnerPrecise": "",
        "missileBeg": "spice rakety",
        "missileEnd": "konec rakety",
        "armorLights": 0.4,
        # Class: CfgVehicles\AllVehicles\NewTurret\Reflectors,
        "Reflectors": {
        },
        "aggregateReflectors": [],
        # Class: CfgVehicles\AllVehicles\NewTurret\GunFire,
        "GunFire": {
            "access": 0,
            "cloudletDuration": 0.2,
            "cloudletAnimPeriod": 1,
            "cloudletSize": 1,
            "cloudletAlpha": 1,
            "cloudletGrowUp": 0.2,
            "cloudletFadeIn": 0.01,
            "cloudletFadeOut": 0.5,
            "cloudletAccY": 0,
            "cloudletMinYSpeed": -100,
            "cloudletMaxYSpeed": 100,
            "cloudletShape": "cloudletFire",
            "cloudletColor": [1,1,1,0],
            "interval": 0.01,
            "size": 3,
            "sourceSize": 0.5,
            "timeToLive": 0,
            "initT": 4500,
            "deltaT": -3000,
            # Class: WeaponFireGun\Table,
            "Table": {
                # Class: WeaponFireGun\Table\T0
                "T0": {
                    "maxT": 0,
                    "color": [0.82,0.95,0.93,0]
                },
                # Class: WeaponFireGun\Table\T1,
                "T1": {
                    "maxT": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: WeaponFireGun\Table\T2,
                "T2": {
                    "maxT": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: WeaponFireGun\Table\T3,
                "T3": {
                    "maxT": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: WeaponFireGun\Table\T4,
                "T4": {
                    "maxT": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: WeaponFireGun\Table\T5,
                "T5": {
                    "maxT": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: WeaponFireGun\Table\T6,
                "T6": {
                    "maxT": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: WeaponFireGun\Table\T7,
                "T7": {
                    "maxT": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: WeaponFireGun\Table\T8,
                "T8": {
                    "maxT": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: WeaponFireGun\Table\T9,
                "T9": {
                    "maxT": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: WeaponFireGun\Table\T10,
                "T10": {
                    "maxT": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: WeaponFireGun\Table\T11,
                "T11": {
                    "maxT": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: WeaponFireGun\Table\T12,
                "T12": {
                    "maxT": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: WeaponFireGun\Table\T13,
                "T13": {
                    "maxT": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: WeaponFireGun\Table\T14,
                "T14": {
                    "maxT": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: WeaponFireGun\Table\T15,
                "T15": {
                    "maxT": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: WeaponFireGun\Table\T16,
                "T16": {
                    "maxT": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: WeaponFireGun\Table\T17,
                "T17": {
                    "maxT": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: WeaponFireGun\Table\T18,
                "T18": {
                    "maxT": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: WeaponFireGun\Table\T19,
                "T19": {
                    "maxT": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: WeaponFireGun\Table\T20,
                "T20": {
                    "maxT": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: WeaponFireGun\Table\T21,
                "T21": {
                    "maxT": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: WeaponFireGun\Table\T22,
                "T22": {
                    "maxT": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\GunClouds,
        "GunClouds": {
            "access": 0,
            "cloudletDuration": 0.3,
            "cloudletAnimPeriod": 1,
            "cloudletSize": 1,
            "cloudletAlpha": 1,
            "cloudletGrowUp": 1,
            "cloudletFadeIn": 0.01,
            "cloudletFadeOut": 1,
            "cloudletAccY": 0.4,
            "cloudletMinYSpeed": 0.2,
            "cloudletMaxYSpeed": 0.8,
            "cloudletShape": "cloudletClouds",
            "cloudletColor": [1,1,1,0],
            "interval": 0.05,
            "size": 3,
            "sourceSize": 0.5,
            "timeToLive": 0,
            "initT": 0,
            "deltaT": 0,
            # Class: WeaponCloudsGun\Table,
            "Table": {
                # Class: WeaponCloudsGun\Table\T0
                "T0": {
                    "maxT": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\MGunClouds,
        "MGunClouds": {
            "access": 0,
            "cloudletGrowUp": 0.05,
            "cloudletFadeIn": 0,
            "cloudletFadeOut": 0.1,
            "cloudletDuration": 0.05,
            "cloudletAnimPeriod": 1,
            "cloudletSize": 1,
            "cloudletAlpha": 0.3,
            "cloudletAccY": 0,
            "cloudletMinYSpeed": -100,
            "cloudletMaxYSpeed": 100,
            "cloudletShape": "cloudletClouds",
            "cloudletColor": [1,1,1,0],
            "timeToLive": 0,
            "interval": 0.02,
            "size": 0.3,
            "sourceSize": 0.02,
            "initT": 0,
            "deltaT": 0,
            # Class: WeaponCloudsMGun\Table,
            "Table": {
                # Class: WeaponCloudsMGun\Table\T0
                "T0": {
                    "maxT": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\HitPoints,
        "HitPoints": {
            # Class: CfgVehicles\AllVehicles\NewTurret\HitPoints\HitTurret
            "HitTurret": {
                "armor": 0.8,
                "material": 51,
                "name": "turret",
                "visual": "turret",
                "passThrough": 1,
                "explosionShielding": 1
            },
            # Class: CfgVehicles\AllVehicles\NewTurret\HitPoints\HitGun,
            "HitGun": {
                "armor": 0.6,
                "material": 52,
                "name": "gun",
                "visual": "gun",
                "passThrough": 1,
                "explosionShielding": 1
            }
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\Turrets,
        "Turrets": {
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\ViewOptics,
        "ViewOptics": {
            "initAngleX": 0,
            "minAngleX": -30,
            "maxAngleX": 30,
            "initAngleY": 0,
            "minAngleY": -100,
            "maxAngleY": 100,
            "initFov": 0.3,
            "minFov": 0.07,
            "maxFov": 0.35,
            "minMoveX": 0,
            "maxMoveX": 0,
            "minMoveY": 0,
            "maxMoveY": 0,
            "minMoveZ": 0,
            "maxMoveZ": 0,
            "speedZoomMaxSpeed": 1e+010,
            "speedZoomMaxFOV": 0
        },
        "forceNVG": 0,
        "isCopilot": 0,
        "canEject": 1,
        "gunnerLeftHandAnimName": "",
        "gunnerRightHandAnimName": "",
        "gunnerLeftLegAnimName": "",
        "gunnerRightLegAnimName": "",
        "gunnerDoor": "",
        "preciseGetInOut": 0,
        "turretFollowFreeLook": 0,
        "allowTabLock": 1,
        "showAllTargets": 0,
        "dontCreateAI": 0,
        "disableSoundAttenuation": 0,
        "slingLoadOperator": 0,
        "playerPosition": 0,
        "allowLauncherIn": 0,
        "allowLauncherOut": 0,
        # Class: CfgVehicles\AllVehicles\NewTurret\TurnIn,
        "TurnIn": {
            "turnOffset": 0
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\TurnOut,
        "TurnOut": {
            "turnOffset": 0
        },
        "gunnerInAction": "ManActTestDriver",
        "gunnerAction": "ManActTestDriver",
        "gunBeg": "usti hlavne",
        "gunEnd": "konec hlavne",
        "memoryPointGunnerOptics": "gunnerview",
        "memoryPointsGetInGunner": "pos gunner",
        "memoryPointsGetInGunnerDir": "pos gunner dir",
        "memoryPointGun": "kulas",
        "selectionFireAnim": "zasleh",
        "showCrewAim": 0
    },
    # Class: CfgVehicles\AllVehicles\ViewCargo,
    "ViewCargo": {
        "initAngleX": 5,
        "minAngleX": -75,
        "maxAngleX": 85,
        "initAngleY": 0,
        "minAngleY": -150,
        "maxAngleY": 150,
        "minFov": 0.25,
        "maxFov": 1.25,
        "initFov": 0.75,
        "minMoveX": 0,
        "maxMoveX": 0,
        "minMoveY": 0,
        "maxMoveY": 0,
        "minMoveZ": 0,
        "maxMoveZ": 0,
        "speedZoomMaxSpeed": 1e+010,
        "speedZoomMaxFOV": 0
    },
    # Class: CfgVehicles\AllVehicles\PilotSpec,
    "PilotSpec": {
        "showHeadPhones": 0
    },
    # Class: CfgVehicles\AllVehicles\CargoSpec,
    "CargoSpec": {
        # Class: CfgVehicles\AllVehicles\CargoSpec\Cargo1
        "Cargo1": {
            "showHeadPhones": 0
        }
    },
    # Class: CfgVehicles\AllVehicles\SoundEvents,
    "SoundEvents": {
    },
    "cargoProxyIndexes": [],
    "cargoDoors": [],
    "hasTerminal": 0,
    "getInOutOnProxy": 0,
    "preciseGetInOut": 0,
    "cargoPreciseGetInOut": [0],
    "availableForSupportTypes": [],
    "impactEffectsSea": "ImpactEffectsSea",
    "impactEffectSpeedLimit": 8,
    "showCrewAim": 0,
    # Class: CfgVehicles\AllVehicles\CargoTurret,
    "CargoTurret": {
        # Class: CfgVehicles\AllVehicles\CargoTurret\ViewGunner
        "ViewGunner": {
            "initAngleX": 5,
            "minAngleX": -75,
            "maxAngleX": 85,
            "initAngleY": 0,
            "minAngleY": -150,
            "maxAngleY": 150,
            "minFov": 0.25,
            "maxFov": 1.25,
            "initFov": 0.75,
            "minMoveX": 0,
            "maxMoveX": 0,
            "minMoveY": 0,
            "maxMoveY": 0,
            "minMoveZ": 0,
            "maxMoveZ": 0,
            "speedZoomMaxSpeed": 1e+010,
            "speedZoomMaxFOV": 0
        },
        # Class: CfgVehicles\AllVehicles\CargoTurret\Hitpoints,
        "Hitpoints": {
        },
        "animationSourceBody": "",
        "animationSourceGun": "",
        "body": "",
        "canEject": 1,
        "commanding": 0,
        "dontCreateAI": 1,
        "gun": "",
        "gunnerGetInAction": "GetInLow",
        "gunnerGetOutAction": "GetOutLow",
        "gunnerName": "cargo",
        "hideWeaponsGunner": 0,
        "isCopilot": 0,
        "memoryPointsGetInGunner": "pos cargo",
        "memoryPointsGetInGunnerDir": "pos cargo dir",
        "primaryGunner": 0,
        "proxyType": "CPCargo",
        "startEngine": 0,
        "turretFollowFreeLook": 0,
        "viewGunnerInExternal": 1,
        "disableSoundAttenuation": 1,
        "outGunnerMayFire": 1,
        "isPersonTurret": 1,
        "showAsCargo": 1,
        "maxElev": 45,
        "minElev": -45,
        "maxTurn": 95,
        "minTurn": -95,
        "animationSourceHatch": "hatchGunner",
        "animationSourceCamElev": "camElev",
        "proxyIndex": 1,
        "gunnerType": "",
        "primaryObserver": 0,
        "weapons": [],
        "magazines": [],
        "soundServo": ["",0.00316228,1],
        "soundElevation": ["",0.00316228,1],
        "initElev": 0,
        "initTurn": 0,
        "minOutElev": -4,
        "maxOutElev": 20,
        "initOutElev": 0,
        "minOutTurn": -60,
        "maxOutTurn": 60,
        "initOutTurn": 0,
        "maxHorizontalRotSpeed": 1.2,
        "maxVerticalRotSpeed": 1.2,
        "minCamElev": -90,
        "maxCamElev": 90,
        "initCamElev": 0,
        "stabilizedInAxes": 3,
        "primary": 1,
        "hasGunner": 1,
        "turretCanSee": 0,
        "canUseScanners": 1,
        # Class: CfgVehicles\AllVehicles\NewTurret\TurretSpec,
        "TurretSpec": {
            "showHeadPhones": 0
        },
        "gunnerOpticsModel": "",
        "gunnerOpticsColor": [0,0,0,1],
        "gunnerForceOptics": 1,
        "gunnerOpticsShowCursor": 0,
        "turretInfoType": "",
        "gunnerOutOpticsModel": "",
        "gunnerOutOpticsColor": [0,0,0,1],
        "gunnerOpticsEffect": [],
        "gunnerOutOpticsEffect": [],
        "memoryPointGunnerOutOptics": "",
        "gunnerOutForceOptics": 0,
        "gunnerOutOpticsShowCursor": 0,
        "gunnerFireAlsoInInternalCamera": 1,
        "gunnerOutFireAlsoInInternalCamera": 1,
        "gunnerUsesPilotView": 0,
        "castGunnerShadow": 0,
        "viewGunnerShadow": 1,
        "viewGunnerShadowDiff": 1,
        "viewGunnerShadowAmb": 1,
        "ejectDeadGunner": 0,
        "canHideGunner": -1,
        "forceHideGunner": 0,
        "inGunnerMayFire": 1,
        "showHMD": 0,
        "lockWhenDriverOut": 0,
        "lockWhenVehicleSpeed": -1,
        "gunnerCompartments": "Compartment1",
        "LODTurnedIn": -1,
        "LODTurnedOut": -1,
        "memoryPointsGetInGunnerPrecise": "",
        "missileBeg": "spice rakety",
        "missileEnd": "konec rakety",
        "armorLights": 0.4,
        # Class: CfgVehicles\AllVehicles\NewTurret\Reflectors,
        "Reflectors": {
        },
        "aggregateReflectors": [],
        # Class: CfgVehicles\AllVehicles\NewTurret\GunFire,
        "GunFire": {
            "access": 0,
            "cloudletDuration": 0.2,
            "cloudletAnimPeriod": 1,
            "cloudletSize": 1,
            "cloudletAlpha": 1,
            "cloudletGrowUp": 0.2,
            "cloudletFadeIn": 0.01,
            "cloudletFadeOut": 0.5,
            "cloudletAccY": 0,
            "cloudletMinYSpeed": -100,
            "cloudletMaxYSpeed": 100,
            "cloudletShape": "cloudletFire",
            "cloudletColor": [1,1,1,0],
            "interval": 0.01,
            "size": 3,
            "sourceSize": 0.5,
            "timeToLive": 0,
            "initT": 4500,
            "deltaT": -3000,
            # Class: WeaponFireGun\Table,
            "Table": {
                # Class: WeaponFireGun\Table\T0
                "T0": {
                    "maxT": 0,
                    "color": [0.82,0.95,0.93,0]
                },
                # Class: WeaponFireGun\Table\T1,
                "T1": {
                    "maxT": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: WeaponFireGun\Table\T2,
                "T2": {
                    "maxT": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: WeaponFireGun\Table\T3,
                "T3": {
                    "maxT": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: WeaponFireGun\Table\T4,
                "T4": {
                    "maxT": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: WeaponFireGun\Table\T5,
                "T5": {
                    "maxT": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: WeaponFireGun\Table\T6,
                "T6": {
                    "maxT": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: WeaponFireGun\Table\T7,
                "T7": {
                    "maxT": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: WeaponFireGun\Table\T8,
                "T8": {
                    "maxT": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: WeaponFireGun\Table\T9,
                "T9": {
                    "maxT": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: WeaponFireGun\Table\T10,
                "T10": {
                    "maxT": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: WeaponFireGun\Table\T11,
                "T11": {
                    "maxT": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: WeaponFireGun\Table\T12,
                "T12": {
                    "maxT": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: WeaponFireGun\Table\T13,
                "T13": {
                    "maxT": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: WeaponFireGun\Table\T14,
                "T14": {
                    "maxT": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: WeaponFireGun\Table\T15,
                "T15": {
                    "maxT": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: WeaponFireGun\Table\T16,
                "T16": {
                    "maxT": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: WeaponFireGun\Table\T17,
                "T17": {
                    "maxT": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: WeaponFireGun\Table\T18,
                "T18": {
                    "maxT": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: WeaponFireGun\Table\T19,
                "T19": {
                    "maxT": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: WeaponFireGun\Table\T20,
                "T20": {
                    "maxT": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: WeaponFireGun\Table\T21,
                "T21": {
                    "maxT": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: WeaponFireGun\Table\T22,
                "T22": {
                    "maxT": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\GunClouds,
        "GunClouds": {
            "access": 0,
            "cloudletDuration": 0.3,
            "cloudletAnimPeriod": 1,
            "cloudletSize": 1,
            "cloudletAlpha": 1,
            "cloudletGrowUp": 1,
            "cloudletFadeIn": 0.01,
            "cloudletFadeOut": 1,
            "cloudletAccY": 0.4,
            "cloudletMinYSpeed": 0.2,
            "cloudletMaxYSpeed": 0.8,
            "cloudletShape": "cloudletClouds",
            "cloudletColor": [1,1,1,0],
            "interval": 0.05,
            "size": 3,
            "sourceSize": 0.5,
            "timeToLive": 0,
            "initT": 0,
            "deltaT": 0,
            # Class: WeaponCloudsGun\Table,
            "Table": {
                # Class: WeaponCloudsGun\Table\T0
                "T0": {
                    "maxT": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\MGunClouds,
        "MGunClouds": {
            "access": 0,
            "cloudletGrowUp": 0.05,
            "cloudletFadeIn": 0,
            "cloudletFadeOut": 0.1,
            "cloudletDuration": 0.05,
            "cloudletAnimPeriod": 1,
            "cloudletSize": 1,
            "cloudletAlpha": 0.3,
            "cloudletAccY": 0,
            "cloudletMinYSpeed": -100,
            "cloudletMaxYSpeed": 100,
            "cloudletShape": "cloudletClouds",
            "cloudletColor": [1,1,1,0],
            "timeToLive": 0,
            "interval": 0.02,
            "size": 0.3,
            "sourceSize": 0.02,
            "initT": 0,
            "deltaT": 0,
            # Class: WeaponCloudsMGun\Table,
            "Table": {
                # Class: WeaponCloudsMGun\Table\T0
                "T0": {
                    "maxT": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\Turrets,
        "Turrets": {
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\ViewOptics,
        "ViewOptics": {
            "initAngleX": 0,
            "minAngleX": -30,
            "maxAngleX": 30,
            "initAngleY": 0,
            "minAngleY": -100,
            "maxAngleY": 100,
            "initFov": 0.3,
            "minFov": 0.07,
            "maxFov": 0.35,
            "minMoveX": 0,
            "maxMoveX": 0,
            "minMoveY": 0,
            "maxMoveY": 0,
            "minMoveZ": 0,
            "maxMoveZ": 0,
            "speedZoomMaxSpeed": 1e+010,
            "speedZoomMaxFOV": 0
        },
        "forceNVG": 0,
        "gunnerLeftHandAnimName": "",
        "gunnerRightHandAnimName": "",
        "gunnerLeftLegAnimName": "",
        "gunnerRightLegAnimName": "",
        "gunnerDoor": "",
        "preciseGetInOut": 0,
        "allowTabLock": 1,
        "showAllTargets": 0,
        "slingLoadOperator": 0,
        "playerPosition": 0,
        "allowLauncherIn": 0,
        "allowLauncherOut": 0,
        # Class: CfgVehicles\AllVehicles\NewTurret\TurnIn,
        "TurnIn": {
            "turnOffset": 0
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\TurnOut,
        "TurnOut": {
            "turnOffset": 0
        },
        "gunnerInAction": "ManActTestDriver",
        "gunnerAction": "ManActTestDriver",
        "gunBeg": "usti hlavne",
        "gunEnd": "konec hlavne",
        "memoryPointGunnerOptics": "gunnerview",
        "memoryPointGun": "kulas",
        "selectionFireAnim": "zasleh",
        "showCrewAim": 0
    },
    "curatorInfoType": "RscDisplayAttributesVehicle",
    "curatorInfoTypeEmpty": "RscDisplayAttributesVehicleEmpty",
    "access": 0,
    "reversed": 1,
    "autocenter": 1,
    "animated": 1,
    "shadow": 1,
    "featureType": 0,
    "speechSingular": [],
    "speechPlural": [],
    "maxDetectRange": 20,
    "detectSkill": 20,
    "mineAlertIconRange": 200,
    "killFriendlyExpCoef": 1,
    "weaponSlots": 0,
    "spotableDarkNightLightsOff": 0.001,
    "spotableNightLightsOff": 0.02,
    "spotableNightLightsOn": 4,
    "accuracyDarkNightLightsOff": 0.001,
    "accuracyNightLightsOff": 0.006,
    "accuracyNightLightsOn": 0.1,
    "obstructSoundLFRatio": 0,
    "occludeSoundLFRatio": 0.25,
    "unloadInCombat": 0,
    "gunnerHasFlares": 1,
    "enableManualFire": 1,
    "sensitivity": 2.5,
    "portrait": "",
    "ghostPreview": "",
    "replaceDamaged": "",
    "replaceDamagedLimit": 0.9,
    "replaceDamagedHitpoints": [],
    "keepInEPESceneAfterDeath": 0,
    "fuelConsumptionRate": 0.01,
    "groupCameraPosition": [0,5,-30],
    "extCameraParams": [1],
    "cameraSmoothSpeed": 5,
    "minFireTime": 20,
    "indirectHitEnemyCoefAI": 10,
    "indirectHitFriendlyCoefAI": -20,
    "indirectHitCivilianCoefAI": -20,
    "indirectHitUnknownCoefAI": -0.5,
    "formationTime": 5,
    "alwaysTarget": 0,
    "irTarget": 1,
    "laserTarget": 0,
    "laserScanner": 0,
    "nvTarget": 0,
    "nvScanner": 0,
    "artilleryTarget": 0,
    "artilleryScanner": 0,
    "canUseScanners": 1,
    "preferRoads": 0,
    "unitInfoTypeLite": 0,
    "hideUnitInfo": 0,
    "radarType": 0,
    "limitedSpeedCoef": 0.22,
    "hasDriver": 1,
    "enableWatch": 0,
    "usePreciseGetInAction": 0,
    "allowTabLock": 1,
    "showAllTargets": 0,
    "waterLinearDampingCoefX": 0,
    "waterLinearDampingCoefY": 0,
    "waterAngularDampingCoef": 0,
    "showNVGDriver": 0,
    "showNVGCommander": 0,
    "showNVGGunner": 0,
    "showNVGCargo": [0],
    "soundAttenuationCargo": [1],
    "countsForScoreboard": 1,
    # Class: CfgVehicles\All\MarkerLights,
    "MarkerLights": {
    },
    # Class: CfgVehicles\All\NVGMarker,
    "NVGMarker": {
        "diffuse": [1,1,1,1],
        "ambient": [1,1,1,1],
        "brightness": 1,
        "blinking": 0,
        "onlyInNvg": 0
    },
    # Class: CfgVehicles\All\HeadLimits,
    "HeadLimits": {
        "initAngleX": 5,
        "minAngleX": -30,
        "maxAngleX": 40,
        "initAngleY": 0,
        "minAngleY": -90,
        "maxAngleY": 90,
        "minAngleZ": -45,
        "maxAngleZ": 45,
        "rotZRadius": 0.2
    },
    "transportAmmo": 0,
    "isbackpack": 0,
    "transportFuel": 0,
    "transportRepair": 0,
    "transportVehiclesCount": 0,
    "transportVehiclesMass": 0,
    "attendant": 0,
    "engineer": 0,
    "uavHacker": 0,
    "soundEngine": ["",1,1],
    "soundEnviron": ["",1,1],
    # Class: CfgVehicles\All\SoundEnvironExt,
    "SoundEnvironExt": {
    },
    # Class: CfgVehicles\All\SoundEquipment,
    "SoundEquipment": {
    },
    # Class: CfgVehicles\All\SoundBreath,
    "SoundBreath": {
    },
    # Class: CfgVehicles\All\SoundBreathSwimming,
    "SoundBreathSwimming": {
    },
    # Class: CfgVehicles\All\SoundBreathInjured,
    "SoundBreathInjured": {
    },
    # Class: CfgVehicles\All\SoundHitScream,
    "SoundHitScream": {
    },
    # Class: CfgVehicles\All\SoundInjured,
    "SoundInjured": {
    },
    # Class: CfgVehicles\All\SoundBreathAutomatic,
    "SoundBreathAutomatic": {
    },
    # Class: CfgVehicles\All\SoundDrown,
    "SoundDrown": {
    },
    # Class: CfgVehicles\All\SoundChoke,
    "SoundChoke": {
    },
    # Class: CfgVehicles\All\SoundRecovered,
    "SoundRecovered": {
    },
    # Class: CfgVehicles\All\SoundBurning,
    "SoundBurning": {
    },
    # Class: CfgVehicles\All\PulsationSound,
    "PulsationSound": {
    },
    # Class: CfgVehicles\All\SoundDrowning,
    "SoundDrowning": {
    },
    "soundCrash": ["",0.316228,1],
    "soundLandCrash": ["",1,1],
    "soundWaterCrash": ["",0.177828,1],
    "soundServo": ["",0.00316228,0.5],
    "soundElevation": ["",0.00316228,0.5],
    "sounddamage": ["",1,1],
    "soundGearUp": ["",1,1],
    "soundGearDown": ["",1,1],
    "soundFlapsUp": ["",1,1],
    "soundFlapsDown": ["",1,1],
    "cabinOpenSound": ["",1,1],
    "cabinCloseSound": ["",1,1],
    "cabinOpenSoundInternal": ["",1,1],
    "cabinCloseSoundInternal": ["",1,1],
    "soundCrashes": ["soundCrash",1],
    "soundLandCrashes": ["soundLandCrash",1],
    "soundWaterCrashes": ["soundWaterCrash",1],
    "emptySound": ["",0,1],
    "cargoIsCoDriver": [0],
    "driverCompartments": "Compartment1",
    "cargoCompartments": ["Compartment1"],
    "driverOpticsEffect": [],
    "canHideDriver": -1,
    "castDriverShadow": 0,
    "castCargoShadow": 0,
    "viewDriverShadow": 1,
    "ejectDeadDriver": 0,
    "ejectDeadCargo": 0,
    "hiddenSelectionsMaterials": [],
    "hiddenUnderwaterSelections": [],
    "shownUnderWaterSelections": [],
    "hiddenUnderwaterSelectionsTextures": [],
    # Class: CfgVehicles\All\FxExplo,
    "FxExplo": {
        "access": 1
    },
    # Class: CfgVehicles\All\GunFire,
    "GunFire": {
        "access": 0,
        "cloudletDuration": 0.2,
        "cloudletAnimPeriod": 1,
        "cloudletSize": 1,
        "cloudletAlpha": 1,
        "cloudletGrowUp": 0.2,
        "cloudletFadeIn": 0.01,
        "cloudletFadeOut": 0.5,
        "cloudletAccY": 0,
        "cloudletMinYSpeed": -100,
        "cloudletMaxYSpeed": 100,
        "cloudletShape": "cloudletFire",
        "cloudletColor": [1,1,1,0],
        "interval": 0.01,
        "size": 3,
        "sourceSize": 0.5,
        "timeToLive": 0,
        "initT": 4500,
        "deltaT": -3000,
        # Class: WeaponFireGun\Table,
        "Table": {
            # Class: WeaponFireGun\Table\T0
            "T0": {
                "maxT": 0,
                "color": [0.82,0.95,0.93,0]
            },
            # Class: WeaponFireGun\Table\T1,
            "T1": {
                "maxT": 200,
                "color": [0.75,0.77,0.9,0]
            },
            # Class: WeaponFireGun\Table\T2,
            "T2": {
                "maxT": 400,
                "color": [0.56,0.62,0.67,0]
            },
            # Class: WeaponFireGun\Table\T3,
            "T3": {
                "maxT": 600,
                "color": [0.39,0.46,0.47,0]
            },
            # Class: WeaponFireGun\Table\T4,
            "T4": {
                "maxT": 800,
                "color": [0.24,0.31,0.31,0]
            },
            # Class: WeaponFireGun\Table\T5,
            "T5": {
                "maxT": 1000,
                "color": [0.23,0.31,0.29,0]
            },
            # Class: WeaponFireGun\Table\T6,
            "T6": {
                "maxT": 1500,
                "color": [0.21,0.29,0.27,0]
            },
            # Class: WeaponFireGun\Table\T7,
            "T7": {
                "maxT": 2000,
                "color": [0.19,0.23,0.21,0]
            },
            # Class: WeaponFireGun\Table\T8,
            "T8": {
                "maxT": 2300,
                "color": [0.22,0.19,0.1,0]
            },
            # Class: WeaponFireGun\Table\T9,
            "T9": {
                "maxT": 2500,
                "color": [0.35,0.2,0.02,0]
            },
            # Class: WeaponFireGun\Table\T10,
            "T10": {
                "maxT": 2600,
                "color": [0.62,0.29,0.03,0]
            },
            # Class: WeaponFireGun\Table\T11,
            "T11": {
                "maxT": 2650,
                "color": [0.59,0.35,0.05,0]
            },
            # Class: WeaponFireGun\Table\T12,
            "T12": {
                "maxT": 2700,
                "color": [0.75,0.37,0.03,0]
            },
            # Class: WeaponFireGun\Table\T13,
            "T13": {
                "maxT": 2750,
                "color": [0.88,0.34,0.03,0]
            },
            # Class: WeaponFireGun\Table\T14,
            "T14": {
                "maxT": 2800,
                "color": [0.91,0.5,0.17,0]
            },
            # Class: WeaponFireGun\Table\T15,
            "T15": {
                "maxT": 2850,
                "color": [1,0.6,0.2,0]
            },
            # Class: WeaponFireGun\Table\T16,
            "T16": {
                "maxT": 2900,
                "color": [1,0.71,0.3,0]
            },
            # Class: WeaponFireGun\Table\T17,
            "T17": {
                "maxT": 2950,
                "color": [0.98,0.83,0.41,0]
            },
            # Class: WeaponFireGun\Table\T18,
            "T18": {
                "maxT": 3000,
                "color": [0.98,0.91,0.54,0]
            },
            # Class: WeaponFireGun\Table\T19,
            "T19": {
                "maxT": 3100,
                "color": [0.98,0.99,0.6,0]
            },
            # Class: WeaponFireGun\Table\T20,
            "T20": {
                "maxT": 3300,
                "color": [0.96,0.99,0.72,0]
            },
            # Class: WeaponFireGun\Table\T21,
            "T21": {
                "maxT": 3600,
                "color": [1,0.98,0.91,0]
            },
            # Class: WeaponFireGun\Table\T22,
            "T22": {
                "maxT": 4200,
                "color": [1,1,1,0]
            }
        }
    },
    # Class: CfgVehicles\All\GunClouds,
    "GunClouds": {
        "access": 0,
        "cloudletDuration": 0.3,
        "cloudletAnimPeriod": 1,
        "cloudletSize": 1,
        "cloudletAlpha": 1,
        "cloudletGrowUp": 1,
        "cloudletFadeIn": 0.01,
        "cloudletFadeOut": 1,
        "cloudletAccY": 0.4,
        "cloudletMinYSpeed": 0.2,
        "cloudletMaxYSpeed": 0.8,
        "cloudletShape": "cloudletClouds",
        "cloudletColor": [1,1,1,0],
        "interval": 0.05,
        "size": 3,
        "sourceSize": 0.5,
        "timeToLive": 0,
        "initT": 0,
        "deltaT": 0,
        # Class: WeaponCloudsGun\Table,
        "Table": {
            # Class: WeaponCloudsGun\Table\T0
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    # Class: CfgVehicles\All\MGunClouds,
    "MGunClouds": {
        "access": 0,
        "cloudletGrowUp": 0.05,
        "cloudletFadeIn": 0,
        "cloudletFadeOut": 0.1,
        "cloudletDuration": 0.05,
        "cloudletAnimPeriod": 1,
        "cloudletSize": 1,
        "cloudletAlpha": 0.3,
        "cloudletAccY": 0,
        "cloudletMinYSpeed": -100,
        "cloudletMaxYSpeed": 100,
        "cloudletShape": "cloudletClouds",
        "cloudletColor": [1,1,1,0],
        "timeToLive": 0,
        "interval": 0.02,
        "size": 0.3,
        "sourceSize": 0.02,
        "initT": 0,
        "deltaT": 0,
        # Class: WeaponCloudsMGun\Table,
        "Table": {
            # Class: WeaponCloudsMGun\Table\T0
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "selectionDamage": "zbytek",
    "HeadAimDown": 0,
    "cargoCanEject": 1,
    "driverCanEject": 1,
    "fireResistance": 10,
    "airCapacity": 10,
    "damageTexDelay": 0,
    "coefInside": 2,
    "coefInsideHeur": 2,
    "coefSpeedInside": 2,
    "windSockExist": 0,
    "slingLoadCargoMemoryPoints": [],
    "slingLoadCargoMemoryPointsDir": [],
    "damageHalf": [],
    "damageFull": [],
    # Class: CfgVehicles\All\camShakeGForce,
    "camShakeGForce": {
        "power": 1,
        "frequency": 20,
        "distance": 0,
        "minSpeed": 1,
        "duration": 3
    },
    "minGForce": 0.2,
    "maxGForce": 2,
    "gForceShakeAttenuation": 0.5,
    # Class: CfgVehicles\All\camShakeDamage,
    "camShakeDamage": {
        "power": 0.5,
        "frequency": 60,
        "distance": -1,
        "minSpeed": 1,
        "attenuation": 0.5,
        "duration": 3
    },
    "features": "",
    "insideDetectCoef": 0.05,
}