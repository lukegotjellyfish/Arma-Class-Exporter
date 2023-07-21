//
// _sideMatrix:
//  1. Categorise classes of the same kind to iterate through to
//      save to directories specific to each array, for ease of use.
//  2. It modular so nothing in the script is dependant on the mods
//      and can be configured easily through the array instead of
//      the rest of the script.
//  3. Classes are grouped by faction in the sub-sub array allowing for
//      ease of comprehension and addition for other sides.
//       The class list is based off of current assets in C4G KotH V14
//       but can easily be extended to all assets of the matching Cfg
//       category for the given side. This script can (12/10/2020) be
//       extended to all applicable classes in Arma + RHS to add to
//       the resulting CombinedBluFor and CombinedOpFor with CombineDicts
//       being easily altered to include more sides that are added here.
//

_sideMatrix = [
	//weapons matrix (add opfor pistols)
	[
		//BluFor
		[
			"BluFor\Weapons"         ,
			"CfgWeapons"             ,
			"rhs_weap_M590_5RD"      ,
			"rhs_weap_M107"          ,
			"rhs_weap_XM2010"        ,
			"rhs_weap_m1garand_sa43" ,
			"rhs_weap_m14ebrri"      ,
			"rhs_weap_sr25"          ,
			"rhs_weap_l1a1_base"     ,
			"rhs_weap_SCARH_STD"     ,
			"rhs_weap_m40a5"         ,
			"rhs_weap_m24sws"        ,
			"rhs_weap_kar98k"        ,
			"rhs_weap_mg42"          ,
			"rhs_weap_mosin_sbr"     ,
			"rhs_weap_m240G"         ,
			"rhs_weap_m4a1_blockII"  ,
			"rhs_weap_mk18"          ,
			"rhs_weap_m27iar"        ,
			"rhs_weap_hk416d145"     ,
			"rhs_weap_m16a4"         ,
			"rhs_weap_m4a1"          ,
			"rhs_weap_m21a"          ,
			"rhs_weap_g36kv"         ,
			"rhs_weap_m249"          ,
			"rhs_weap_m249_pip"      ,
			"rhs_weap_MP44"          ,
			"rhsusf_weap_MP7A2"      ,
			"rhsusf_weap_m9"         ,
			"rhsusf_weap_glock17g4"  ,
			"rhs_weap_m3a1_specops"  ,
			"rhsusf_weap_m1911a1"    ,
			"rhs_weap_savz61"        ,
			"rhs_weap_type94_new"
		]                                                    ,
		//OpFor
		[
			"OpFor\Weapons"         ,
			"CfgWeapons"            ,
			"rhs_weap_6p53"         ,
			"rhs_weap_ak103"        ,
			"rhs_weap_ak74"         ,
			"rhs_weap_ak74m"        ,
			"rhs_weap_ak74mr"       ,
			"rhs_weap_akmn"         ,
			"rhs_weap_aks74un"      ,
			"rhs_weap_asval_npz"    ,
			"rhs_weap_asval"        ,
			"rhs_weap_dsr1"         ,
			"rhs_weap_Izh18"        ,
			"rhs_weap_m38_rail"     ,
			"rhs_weap_m38"          ,
			"rhs_weap_m76"          ,
			"rhs_weap_m84"          ,
			"rhs_weap_makarov_pm"   ,
			"rhs_weap_pb_6p9"       ,
			"rhs_weap_pkm"          ,
			"rhs_weap_pkp"          ,
			"rhs_weap_pp2000_folded",
			"rhs_weap_pya"          ,
			"rhs_weap_savz58p_rail" ,
			"rhs_weap_savz58v_fold" ,
			"rhs_weap_svdp_npz"     ,
			"rhs_weap_svdp"         ,
			"rhs_weap_t5000"        ,
			"rhs_weap_tr8"          ,
			"rhs_weap_tt33"         ,
			"rhs_weap_vhsd2"        ,
			"rhs_weap_vss_npz"      ,
			"rhs_weap_vss"
		]
	]                                                     ,
	//magazines matrix  (add opfor pistols)
	[
		//BluFor
		[
			"BluFor\Magazines"                                  ,
			"CfgMagazines"                                      ,
			"rhs_200rnd_556x45_B_SAW"                           ,
			"rhs_mag_20Rnd_762x51_m80_fnfal"                    ,
			"rhsusf_mag_10Rnd_STD_50BMG_mk211",
			"rhs_mag_20Rnd_SCAR_762x51_m80_ball"                ,
			"rhs_mag_30Rnd_556x45_M855_Stanag"                  ,
			"rhs_mag_30Rnd_556x45_Mk262_Stanag"                 ,
			"rhs_mag_30Rnd_556x45_Mk318_Stanag"                 ,
			"rhs_mag_6x8mm_mhp"                                 ,
			"rhsgref_20rnd_765x17_vz61"                         ,
			"rhsgref_30rnd_1143x23_M1911B_SMG"                  ,
			"rhsgref_30rnd_556x45_m21"                          ,
			"rhsgref_30Rnd_792x33_SmE_StG"                      ,
			"rhsgref_50Rnd_792x57_SmE_drum"                     ,
			"rhsgref_5Rnd_762x54_m38"                           ,
			"rhsgref_5Rnd_792x57_kar98k"                        ,
			"rhsgref_8Rnd_762x63_M2B_M1rifle"                   ,
			"rhssaf_30rnd_556x45_EPR_G36"                       ,
			"Rhsusf_100Rnd_762x51"                              ,
			"rhsusf_10Rnd_762x51_m993_Mag"                      ,
			"rhsusf_20Rnd_762x51_m118_special_Mag"              ,
			"rhsusf_5Rnd_00Buck"                                ,
			"rhsusf_5Rnd_300winmag_xm2010"                      ,
			"rhsusf_5Rnd_762x51_m993_Mag"                       ,
			"rhsusf_5Rnd_Slug"                                  ,
			"rhsusf_mag_10Rnd_STD_50BMG_M33"                    ,
			"rhsusf_mag_10Rnd_STD_50BMG_mk211"                  ,
			"rhsusf_mag_15Rnd_9x19_JHP"                         ,
			"rhsusf_mag_17Rnd_9x19_JHP"                         ,
			"rhsusf_mag_40Rnd_46x30_JHP"                        ,
			"rhsusf_mag_7x45acp_MHP"
		]                                                    ,
		//OpFor
		[
			"OpFor\Magazines"               ,
			"CfgMagazines"                  ,
			"rhs_100Rnd_762x54mmR"          ,
			"rhs_10Rnd_762x54mmR_7N14"      ,
			"rhs_10rnd_9x39mm_SP5"          ,
			"rhs_18rnd_9x21mm_7N29"         ,
			"rhs_20rnd_9x39mm_SP6"          ,
			"rhs_30Rnd_545x39_7N10_AK"      ,
			"rhs_30Rnd_545x39_7N22_AK"      ,
			"rhs_30Rnd_545x39_7N6_AK"       ,
			"rhs_30Rnd_545x39_7N6M_AK"      ,
			"rhs_30Rnd_762x39mm_polymer_89" ,
			"rhs_30Rnd_762x39mm"            ,
			"rhs_5Rnd_338lapua_t5000"       ,
			"rhs_mag_762x25_8"              ,
			"rhs_mag_9x18_8_57N181S"        ,
			"rhs_mag_9x19_17"               ,
			"rhs_mag_9x19mm_7n21_20"        ,
			"rhsgref_10Rnd_792x57_m76"      ,
			"rhsgref_1Rnd_00Buck"           ,
			"rhsgref_1Rnd_Slug"             ,
			"rhsgref_30rnd_556x45_vhs2"     ,
			"rhsgref_5Rnd_762x54_m38"       ,
			"rhssaf_250Rnd_762x54R"         ,
			"rhsusf_5Rnd_762x51_m62_Mag"
		]
	]                                                     ,
	//launcher matrix
	[
		//BluFor
		[
			"BluFor\Launchers"                                  ,
			"CfgWeapons"                                        ,
			"rhs_weap_M136"                                     ,
			"rhs_weap_M136_hedp"                                ,
			"rhs_weap_m32_Base_F"                               ,
			"rhs_weap_M320"                                     ,
			"rhs_weap_m72a7"                                    ,
			"rhs_weap_maaws"                                    ,
			"rhs_weap_smaw"                                     ,
			"rhs_weap_fim92"                                    ,
			"rhs_weap_fgm148"
		]                                                    ,
		//OpFor
		[
			"OpFor\Launchers"                                   ,
			"CfgWeapons"                                        ,
			"rhs_weap_rpg26"                                    ,
			"rhs_weap_rpg7"                                     ,
			"rhs_weap_igla"                                     ,
			"rhs_weap_rshg2"
		]
	]                                                     ,
	//launcher magazine matrix
	[
		//BluFor
		[
			"BluFor\LauncherMagazines"                          ,
			"CfgMagazines"                                      ,
			"rhs_fgm148_magazine_AT"                            ,
			"rhs_fim92_mag"                                     ,
			"rhs_m136_hedp_mag"                                 ,
			"rhs_m136_mag"                                      ,
			"rhs_m72a7_mag"                                     ,
			"rhs_mag_M441_HE"                                   ,
			"rhs_mag_maaws_HE"                                  ,
			"rhs_mag_maaws_HEAT"                                ,
			"rhs_mag_smaw_HEAA"                                 ,
			"rhs_mag_smaw_HEDP"                                 ,
			"rhsusf_mag_6Rnd_M441_HE"
		]                                                    ,
		//OpFor
		[
			"OpFor\LauncherMagazines"                           ,
			"CfgMagazines"                                      ,
			"rhs_mag_9k38_rocket"                               ,
			"rhs_rpg26_mag"                                     ,
			"rhs_rpg7_OG7V_mag"                                 ,
			"rhs_rpg7_PG7VL_mag"                                ,
			"rhs_rpg7_PG7VR_mag"                                ,
			"rhs_rpg7_TBG7V_mag"                                ,
			"rhs_rshg2_mag"
		]
	]                                                     ,
	//vehicle matrix
	[
		//BluFor
		[
			"BluFor\Vehicles"                                   ,
			"CfgVehicles"                                       ,
			"B_Quadbike_01_F"                                   ,
			"RHS_M2A2_BUSKI_WD"                                 ,
			"RHS_M2A2_wd"                                       ,
			"RHS_M2A3_BUSKIII_WD"                               ,
			"RHS_M6_wd"                                         ,
			"rhsgref_cdf_b_ural_Zu23"                           ,
			"rhsusf_m1025_w"                                    ,
			"rhsusf_m1025_w_m2"                                 ,
			"rhsusf_m1025_w_Mk19"                               ,
			"rhsusf_m1045_w"                                    ,
			"rhsusf_m1117_w"                                    ,
			"rhsusf_m113_usarmy"                                ,
			"rhsusf_m113_usarmy_medical"                        ,
			"rhsusf_m113_usarmy_Mk19"                           ,
			"rhsusf_m1220_m153_m2_usarmy_wd"                    ,
			"rhsusf_M1220_MK19_usarmy_wd"                       ,
			"rhsusf_m1220_usarmy_wd"                            ,
			"rhsusf_m1232_MK19_usarmy_wd"                       ,
			"rhsusf_m1232_usarmy_wd"                            ,
			"rhsusf_m1a1aim_tuski_wd"                           ,
			"rhsusf_m1a1fep_wd"                                 ,
			"rhsusf_m1a1hc_wd"                                  ,
			"rhsusf_m1a2sep1tuskiiwd_usarmy"                    ,
			"RHS_MELB_MH6M"                                     ,
			"RHS_UH1Y_d"                                        ,
			"RHS_MELB_AH6M"                                     ,
			"RHS_CH_47F_10"                                     ,
			"RHS_AH1Z"                                          ,
			"RHS_AH64D"                                         ,
			"RHS_C130J"                                         ,
			"RHS_A10"                                           ,
			"rhsusf_f22"                                        ,
			"rhs_l159_cdf_b_CDF"                                ,
			"C_SUV_01_F"                                        ,
			"C_Hatchback_01_sport_red_F"                        ,
			"C_Kart_01_Fuel_F",
			"RHSGREF_A29B_HIDF"
		]                                                    ,
		//OpFor
		[
			"OpFor\Vehicles"                                    ,
			"CfgVehicles"                                       ,
			"B_Quadbike_01_F"                                   ,
			"RHS_UAZ_MSV_01"                                    ,
			"rhsgref_ins_uaz_dshkm"                             ,
			"rhs_tigr_3camo_msv"                                ,
			"rhsgref_cdf_b_reg_uaz_ags"                         ,
			"rhs_tigr_sts_vdv"                                  ,
			"rhsgref_ins_uaz_spg9"                              ,
			"rhsgref_BRDM2_vdv"                                 ,
			"rhsgref_BRDM2_ATGM_vdv"                            ,
			"rhs_gaz66_zu23_msv"                                ,
			"rhs_bmd1r"                                         ,
			"rhs_btr80_msv"                                     ,
			"rhsgref_ins_bmp1k"                                 ,
			"rhsgref_ins_bmp1p"                                 ,
			"rhsgref_ins_bmp2d"                                 ,
			"rhs_zsu234_aa"                                     ,
			"rhs_sprut_vdv"                                     ,
			"rhs_bmd2m"                                         ,
			"rhs_bmp3_msv"                                      ,
			"rhs_btr80a_msv"                                    ,
			"rhs_bmd4_vdv"                                      ,
			"rhs_t72bb_tv"                                      ,
			"rhs_t80bvk"                                        ,
			"rhs_t80uk"                                         ,
			"rhs_t72bc_tv"                                      ,
			"rhs_t90a_tv"                                       ,
			"rhs_bmd4ma_vdv"                                    ,
			"rhs_t90a_tv"                                       ,
			"rhs_t72bd_tv"                                      ,
			"rhs_bmp3mera_msv"                                  ,
			"rhs_t80ue1"                                        ,
			"rhs_ka60_c"                                        ,
			"RHS_Mi8MTV3_vvsc"                                  ,
			"RHS_Mi24Vt_vvsc"                                   ,
			"RHS_Mi24P_vvs"                                     ,
			"RHS_Mi24V_vvs"                                     ,
			"rhsgref_mi24g_CAS"                                 ,
			"rhs_mi28n_base"                                    ,
			"rhs_mi28n_base"                                    ,
			"RHS_Ka52_vvs"                                      ,
			"RHS_Su25SM_vvs"                                    ,
			"rhs_mig29sm_vmf"                                   ,
			"C_SUV_01_F"                                        ,
			"C_Hatchback_01_sport_red_F"                        ,
			"C_Kart_01_Fuel_F"
		]
	]                                                     ,
	//vehicle weapon matrix
	[
		//BluFor
		[
			"BluFor\VehicleWeapons"                             ,
			"CfgWeapons"                                        ,
			"RHS_M2"                                            ,
			"RHS_M2_Abrams_Gunner"                              ,
			"RHS_M2_CROWS_M153"                                 ,
			"RHS_M2_M1117"                                      ,
			"RHS_MK19"                                          ,
			"rhs_weap_2A14"                                     ,
			"rhs_weap_FFARLauncher"                             ,
			"RHS_weap_gau19"                                    ,
			"RHS_weap_gau8"                                     ,
			"rhs_weap_gbu12"                                    ,
			"rhs_weap_HellfireLauncher"                         ,
			"rhs_weap_m134_minigun_1"                           ,
			"rhs_weap_m134_minigun_2"                           ,
			"RHS_weap_m134_pylon"                               ,
			"rhs_weap_M197"                                     ,
			"rhs_weap_M230"                                     ,
			"rhs_weap_m240_abrams_coax"                         ,
			"rhs_weap_m240_bradley_coax"                        ,
			"RHS_weap_M242BC"                                   ,
			"rhs_weap_m256"                                     ,
			"rhs_weap_mk82"                                     ,
			"Rhs_weap_stinger_Launcher"                         ,
			"Rhs_weap_TOW_Launcher"                             ,
			"rhs_weap_tow_launcher_static"                      ,
			"RHS_weap_zpl20"                                    ,
			"rhsusf_weap_M257_8"                                ,
			"rhsusf_weap_M259",
			"rhs_weap_FFARLauncher_M229",
			"rhs_weap_DAGR_launcher",
			"rhs_weap_m3w_a29"
		]                                                    ,
		//OpFor
		[
			"OpFor\VehicleWeapons"                              ,
			"CfgWeapons"                                        ,
			"rhs_weap_2A14"                                     ,
			"rhs_weap_2a28"                                     ,
			"rhs_weap_2a42"                                     ,
			"rhs_weap_2a46_2"                                   ,
			"rhs_weap_2a46m_4"                                  ,
			"rhs_weap_2a46m_5"                                  ,
			"rhs_weap_2a46m"                                    ,
			"rhs_weap_2a70"                                     ,
			"rhs_weap_2a72_btr"                                 ,
			"rhs_weap_2a72"                                     ,
			"rhs_weap_2a75"                                     ,
			"rhs_weap_902a"                                     ,
			"rhs_weap_s13",
			"rhs_weap_902b"                                     ,
			"rhs_weap_9k11"                                     ,
			"rhs_weap_9k121_Launcher"                           ,
			"rhs_weap_9k133"                                    ,
			"rhs_weap_9m113"                                    ,
			"rhs_weap_9m120_launcher"                           ,
			"rhs_weap_9P148"                                    ,
			"RHS_weap_AGS30"                                    ,
			"RHS_weap_AZP23"                                    ,
			"rhs_weap_DSHKM"                                    ,
			"rhs_weap_fab250"                                   ,
			"rhs_weap_gi2"                                      ,
			"rhs_weap_gsh23l"                                   ,
			"rhs_weap_gsh30"                                    ,
			"rhs_weap_GSh302"                                   ,
			"rhs_weap_kpvt"                                     ,
			"rhs_weap_nsvt_t72"                                 ,
			"rhs_weap_pkt_bmd_coax"                             ,
			"rhs_weap_pkt_btr"                                  ,
			"rhs_weap_pkt_btr80a"                               ,
			"rhs_weap_pkt"                                      ,
			"rhs_weap_PL1"                                      ,
			"rhs_weap_s8"                                       ,
			"rhs_weap_s8df"                                     ,
			"rhs_weap_SPG9"                                     ,
			"rhs_weap_yakB",
			"rhs_weap_zt6_Launcher",
			"rhs_weap_zt3_launcher"
		]
	]                                                     ,
	//vehicle magazine matrix
	[
		//BluFor
		[
			"BluFor\VehicleMagazines"                   ,
			"CfgMagazines"                              ,
			"RHS_48Rnd_40mm_MK19_M1001"                 ,
			"rhs_mag_400rnd_127x99_SLAP_mag_Tracer_Red_Plane",
			"RHS_48Rnd_40mm_MK19_M430A1"                ,
			"RHS_96Rnd_40mm_MK19_M430A1"                ,
			"rhs_mag_100rnd_127x99_mag_Tracer_Red"      ,
			"rhs_mag_1100Rnd_762x51_M240"               ,
			"rhs_mag_1150Rnd_30x173_mixed"              ,
			"rhs_mag_1000Rnd_30x173",
			"rhs_mag_200rnd_127x99_mag_Tracer_Red"      ,
			"rhs_mag_200rnd_127x99_SLAP_mag_Tracer_Red" ,
			"rhs_mag_230Rnd_25mm_M242_HEI"              ,
			"rhs_mag_2Rnd_TOW2A"                        ,
			"rhs_mag_TOW2A"                             ,
			"rhs_mag_TOW2b"                             ,
			"rhs_mag_TOW2bb"                            ,
			"rhs_mag_2Rnd_TOW2B_AERO"                   ,
			"rhs_mag_2Rnd_TOW2B"                        ,
			"rhs_mag_2Rnd_TOW2BB"                       ,
			"rhs_mag_30x113mm_M789_HEDP_1200"           ,
			"rhs_mag_400rnd_127x99_mag_Tracer_Red"      ,
			"Rhs_mag_4Rnd_stinger"                      ,
			"rhs_mag_70Rnd_25mm_M242_APFSDS"            ,
			"rhs_mag_762x51_M240_1200"                  ,
			"rhs_mag_762x51_m80a1_4000"                 ,
			"rhs_mag_AGM114K_4"                         ,
			"rhs_mag_AGM114L_4"                         ,
			"RHS_mag_AZP23_100"                         ,
			"rhs_mag_gau19_air_base"                    ,
			"rhs_mag_gbu12"                             ,
			"rhs_mag_m134_pylon_3000"                   ,
			"rhs_mag_M151_19_green"                     ,
			"rhs_mag_M151_7_green"                      ,
			"rhs_mag_M197_750"                          ,
			"rhs_mag_M829A1"                            ,
			"rhs_mag_M829A3"                            ,
			"rhs_mag_M1069"                             ,
			"rhs_mag_M830A1"                            ,
			"rhs_mag_mk82"                              ,
			"rhs_mag_zpl20_mixed"                       ,
			"rhsusf_mag_L8A3_8",
			"rhs_mag_M229_7",
			"rhs_mag_DAGR_8"
		]                                                    ,
		//OpFor
		[
			"OpFor\VehicleMagazines"                            ,
			"CfgMagazines"                                      ,
			"rhs_mag_127x108mm_1SLT_1470"                       ,
			"rhs_mag_127x108mm_50"                              ,
			"rhs_mag_145x115mm_50"                              ,
			"rhs_mag_3bk18m_6"                                  ,
			"rhs_mag_3bk18m_8"                                  ,
			"rhs_mag_3bk29_8"                                   ,
			"rhs_mag_3bk31_3"                                   ,
			"rhs_mag_3bk31_8"                                   ,
			"rhs_mag_3bm22_14"                                  ,
			"rhs_mag_3bm42_7"                                   ,
			"rhs_mag_3bm46_10"                                  ,
			"rhs_mag_3bm46_8"                                   ,
			"rhs_mag_3d17_12"                                   ,
			"rhs_mag_3d17_6"                                    ,
			"rhs_mag_3d17"                                      ,
			"rhs_mag_3of26_5"                                   ,
			"rhs_mag_3of26_6"                                   ,
			"rhs_mag_3of26_7"                                   ,
			"rhs_mag_3ubr11_125"                                ,
			"rhs_mag_3ubr11_150"                                ,
			"rhs_mag_3ubr11_195"                                ,
			"rhs_mag_3ubr11_227"                                ,
			"rhs_mag_3ubr6_195"                                 ,
			"rhs_mag_3ubr8_120"                                 ,
			"rhs_mag_3ubr8_160"                                 ,
			"rhs_mag_3ubr8_230"                                 ,
			"rhs_mag_3UOF17_22"                                 ,
			"rhs_mag_3UOF191_22"                                ,
			"rhs_mag_3uof8_125"                                 ,
			"rhs_mag_3uof8_150"                                 ,
			"rhs_mag_3uof8_180"                                 ,
			"rhs_mag_3uof8_237"                                 ,
			"rhs_mag_3uof8_305"                                 ,
			"rhs_mag_3uof8_340"                                 ,
			"rhs_mag_3uor6_230"                                 ,
			"rhs_mag_762x54mm_2000"                             ,
			"rhs_mag_762x54mm_250"                              ,
			"rhs_mag_9m113_5"                                   ,
			"rhs_mag_9m113M"                                    ,
			"rhs_mag_9m117_8"                                   ,
			"rhs_mag_9m117m_8"                                  ,
			"rhs_mag_9m117m1_8"                                 ,
			"rhs_mag_9m119_4"                                   ,
			"rhs_mag_9m119_6"                                   ,
			"rhs_mag_9m119f_6"                                  ,
			"rhs_mag_9M120M_Mi24_2x"                            ,
			"rhs_mag_9M120M_Mi28_8x",
			"rhs_mag_b13l_s13b",
			"rhs_mag_b13l_s13t",
			"rhs_mag_9m133_2"                                   ,
			"rhs_mag_9m14m"                                     ,
			"rhs_mag_apu6_9m127m_ka52"                          ,
			"rhs_mag_AZP23_100"                                 ,
			"rhs_mag_AZP23_2000_mixed"                          ,
			"rhs_mag_AZP23_2000"                                ,
			"rhs_mag_b8m1_s8df"                                 ,
			"rhs_mag_b8m1_s8kom"                                ,
			"rhs_mag_b8v20a_ka52_s8kom"                         ,
			"rhs_mag_b8v20a_s8kom"                              ,
			"rhs_mag_fab250"                                    ,
			"rhs_mag_GI2_420_AP"                                ,
			"rhs_mag_GI2_420_HE"                                ,
			"rhs_mag_gsh30_bt_250"                              ,
			"rhs_mag_gsh30_ofzt_750"                            ,
			"rhs_mag_og15v_20"                                  ,
			"rhs_mag_OG9V"                                      ,
			"rhs_mag_pg15v_20"                                  ,
			"rhs_mag_PG9V"                                      ,
			"rhs_mag_s8_12"                                     ,
			"rhs_mag_upk23_mixed"                               ,
			"RHS_mag_VOG30_30",
			"rhs_mag_zt6_4",
			"rhs_mag_zt3_4"
		]
	]                                                     ,
	//infantry uniform matrix
	[
		//BluFor
		[
			"BluFor\Uniforms",
			"CfgWeapons",
			"H_Cap_headphones",
			"rhs_8point_marpatd",
			"rhs_8point_marpatwd",
			"rhs_Booniehat_ucp",
			"RHS_jetpilot_usaf",
			"rhs_uniform_acu_ocp",
			"rhs_uniform_acu_ucp",
			"rhs_uniform_cu_ocp",
			"rhs_uniform_cu_ucp",
			"rhs_uniform_FROG01_d",
			"rhs_uniform_FROG01_wd",
			"rhs_uniform_g3_blk",
			"rhs_uniform_g3_rgr",
			"rhs_uniform_g3_tan",
			"rhsgref_alice_webbing",
			"rhsgref_Booniehat_alpen",
			"rhsgref_uniform_alpenflage",
			"rhsusf_ach_helmet_camo_ocp",
			"rhsusf_ach_helmet_ocp",
			"rhsusf_ach_helmet_ucp",
			"rhsusf_cvc_ess",
			"rhsusf_cvc_green_ess",
			"rhsusf_hgu56p_saf",
			"rhsusf_hgu56p_visor_green",
			"rhsusf_iotv_ocp",
			"rhsusf_iotv_ocp_SAW",
			"rhsusf_iotv_ocp_Teamleader",
			"rhsusf_iotv_ucp",
			"rhsusf_iotv_ucp_SAW",
			"rhsusf_iotv_ucp_Teamleader",
			"rhsusf_lwh_helmet_marpatd_headset",
			"rhsusf_lwh_helmet_marpatwd_headset",
			"rhsusf_mbav_mg",
			"rhsusf_mich_bare_norotos_arc_semi_headset",
			"rhsusf_mich_bare_norotos_tan_headset",
			"rhsusf_opscore_bk_pelt",
			"rhsusf_opscore_mar_fg_pelt",
			"rhsusf_opscore_mar_ut_pelt",
			"rhsusf_patrolcap_ocp",
			"rhsusf_patrolcap_ucp",
			"rhsusf_spc",
			"rhsusf_spc_teamleader",
			"rhsusf_spcs_ocp",
			"rhsusf_spcs_ucp",
			"U_B_HeliPilotCoveralls",
			"U_B_PilotCoveralls",
			"U_O_FullGhillie_ard",
			"U_O_FullGhillie_lsh",
			"U_O_FullGhillie_sard",
			"V_Chestrig_khk",
			"V_PlateCarrier2_blk",
			"V_PlateCarrier2_rgr",
			"V_TacVest_khk",
			"V_TacVest_oli"
		],
		//OpFor
		[
			"OpFor\Uniforms",
			"CfgWeapons",
			"rhs_6b13_EMR_6sh92",
			"rhs_6b13_Flora_6sh92",
			"rhs_6b23",
			"rhs_6b23_6sh116_od",
			"rhs_6b23_digi_6sh92_Spetsnaz",
			"rhs_6b23_digi_6sh92_spetsnaz2",
			"rhs_6b23_digi_6sh92_Vog_Radio_Spetsnaz",
			"rhs_6b23_digi_rifleman",
			"rhs_6b23_ML_rifleman",
			"rhs_6b23_rifleman",
			"rhs_6b27m_ess",
			"rhs_6b27m_ml_ess",
			"rhs_6b28_ess",
			"rhs_6b43",
			"rhs_6b47",
			"rhs_6b5_rifleman_khaki",
			"rhs_6b7_1m_bala1_flora",
			"rhs_6b7_1m_emr_ess_bala",
			"rhs_6sh92",
			"rhs_6sh92_digi_vog_headset",
			"rhs_6sh92_vsr",
			"rhs_altyn_visordown",
			"rhs_beanie_green",
			"rhs_beret_mp1",
			"rhs_beret_vdv3",
			"rhs_Booniehat_digi",
			"rhs_fieldcap_digi2",
			"rhs_fieldcap_vsr",
			"rhs_ssh68",
			"rhs_tsh4",
			"rhs_uniform_df15",
			"rhs_uniform_df15_tan",
			"rhs_uniform_emr_patchless",
			"rhs_uniform_flora_patchless",
			"rhs_uniform_flora_patchless_alt",
			"rhs_uniform_gorka_r_g",
			"rhs_uniform_gorka_r_y",
			"rhs_uniform_m88_patchless",
			"rhs_uniform_mflora_patchless",
			"rhs_uniform_vdv_emr",
			"rhs_uniform_vdv_emr_des",
			"rhs_uniform_vdv_flora",
			"rhs_uniform_vmf_flora",
			"rhs_vest_commander",
			"rhs_vydra_3m",
			"rhs_zsh7a_alt",
			"rhs_zsh7a_mike_alt",
			"U_O_FullGhillie_ard",
			"U_O_FullGhillie_lsh",
			"U_O_FullGhillie_sard",
			"V_Chestrig_khk"
		]
	],
	//backpacks matrix
	[
		//BluFor
		[
			"BluFor\Backpacks",
			"CfgVehicles",
			"rhsusf_falconii",
			"B_Carryall_cbr"
		],
		//OpFor
		[
			"OpFor\Backpacks",
			"CfgVehicles",
			"rhs_sidor",
			"rhs_assault_umbts",
			"rhsgref_ttsko_alicepack"
		]
	],
	//glasses matrix
	[
		//BluFor
		[
			"BluFor\Glasses",
			"CfgGlasses",
			"G_Aviator",
			"G_Bandanna_blk",
			"rhs_ess_black",
			"rhsusf_shemagh_tan",
			"rhsusf_shemagh2_gogg_grn",
			"rhsusf_shemagh2_gogg_od",
			"rhsusf_shemagh2_gogg_tan"
		],
		//OpFor
		[
			"OpFor\Glasses",
			"CfgGlasses",
			"G_Bandanna_blk",
			"rhs_balaclava1_olive"
		]
	]
];


// getClass:
//  This is a function that adds a found class and it's properties to _classBody
//   which is then returned.
//
//  Notes:
//   - Remove _classBody param and instead use _classBody = _classBody + [] call getClass
//      as there is no reason for _classBody to be passed to this function.
getClass = {
	params ["_property", "_classBody", "_addComma", "_propertyNameLast", "_configCategory"];

		//diag_log(format["Class here: %1", _property]);

		//Class here: bin\config.bin/CfgWeapons/SMG_01_Base/Burst"
		_splitClass = str _property splitString "\/";
		//Remove "bin" and "config.bin"
		_splitClass deleteRange [0, 2];

		_countSplitClass = count _splitClass;
		//Add comment showing class
		_classBody = _classBody + format["%1    # Class: %2 [Indent level: %3]", _addComma, (_splitClass joinString "/"), str (_countSplitClass - 2)];
		//Classes with "ammo" first will not have a ,\n for whatever reason - adding it here
		if (_addComma find "\n" == -1) then {_addComma = ",\n" + _addComma splitString "," joinString ""};
		_classBody = _classBody + format['%1    "%2": {', _addComma, _propertyNameLast];

		//create _classProperties to assign array to
		_classProperties = [];
		switch (_countSplitClass) do {
			 case 2: {_classProperties = configProperties [configFile >> _splitClass select 0 >> _splitClass select 1]};
			 case 3: {_classProperties = configProperties [configFile >> _splitClass select 0 >> _splitClass select 1 >> _splitClass select 2]};
			 case 4: {_classProperties = configProperties [configFile >> _splitClass select 0 >> _splitClass select 1 >> _splitClass select 2 >> _splitClass select 3]};
			 case 5: {_classProperties = configProperties [configFile >> _splitClass select 0 >> _splitClass select 1 >> _splitClass select 2 >> _splitClass select 3 >> _splitClass select 4]};
			 case 6: {_classProperties = configProperties [configFile >> _splitClass select 0 >> _splitClass select 1 >> _splitClass select 2 >> _splitClass select 3 >> _splitClass select 4 >> _splitClass select 5]};
			 case 7: {_classProperties = configProperties [configFile >> _splitClass select 0 >> _splitClass select 1 >> _splitClass select 2 >> _splitClass select 3 >> _splitClass select 4 >> _splitClass select 5 >> _splitClass select 6]};
			 case 8: {_classProperties = configProperties [configFile >> _splitClass select 0 >> _splitClass select 1 >> _splitClass select 2 >> _splitClass select 3 >> _splitClass select 4 >> _splitClass select 5 >> _splitClass select 6 >> _splitClass select 7]};
			 case 9: {_classProperties = configProperties [configFile >> _splitClass select 0 >> _splitClass select 1 >> _splitClass select 2 >> _splitClass select 3 >> _splitClass select 4 >> _splitClass select 5 >> _splitClass select 6 >> _splitClass select 7 >> _splitClass select 8]};
			case 10: {_classProperties = configProperties [configFile >> _splitClass select 0 >> _splitClass select 1 >> _splitClass select 2 >> _splitClass select 3 >> _splitClass select 4 >> _splitClass select 5 >> _splitClass select 6 >> _splitClass select 7 >> _splitClass select 8 >> _splitClass select 9]};
			case 11: {_classProperties = configProperties [configFile >> _splitClass select 0 >> _splitClass select 1 >> _splitClass select 2 >> _splitClass select 3 >> _splitClass select 4 >> _splitClass select 5 >> _splitClass select 6 >> _splitClass select 7 >> _splitClass select 8 >> _splitClass select 9 >> _splitClass select 10]};
			case 12: {_classProperties = configProperties [configFile >> _splitClass select 0 >> _splitClass select 1 >> _splitClass select 2 >> _splitClass select 3 >> _splitClass select 4 >> _splitClass select 5 >> _splitClass select 6 >> _splitClass select 7 >> _splitClass select 8 >> _splitClass select 9 >> _splitClass select 10 >> _splitClass select 11]};
			case 13: {_classProperties = configProperties [configFile >> _splitClass select 0 >> _splitClass select 1 >> _splitClass select 2 >> _splitClass select 3 >> _splitClass select 4 >> _splitClass select 5 >> _splitClass select 6 >> _splitClass select 7 >> _splitClass select 8 >> _splitClass select 9 >> _splitClass select 10 >> _splitClass select 11 >> _splitClass select 12]};
			case 14: {_classProperties = configProperties [configFile >> _splitClass select 0 >> _splitClass select 1 >> _splitClass select 2 >> _splitClass select 3 >> _splitClass select 4 >> _splitClass select 5 >> _splitClass select 6 >> _splitClass select 7 >> _splitClass select 8 >> _splitClass select 9 >> _splitClass select 10 >> _splitClass select 11 >> _splitClass select 12 >> _splitClass select 13]};
			//There are more than 14 nested classes, investigate why: bug or valid value (Max seen so far was 14 for RHSUSAF)
			default {diag_log(format["count _splitClass [%1]", _countSplitClass]);};
		};

		_addComma = (_addComma splitString "," joinString "") + "    ";
		_i = 1;
		{
			//Sanitized property name for writing to file
			_propertyName =  str _x splitString "\" joinString "/";
			if (_i == 2) then { _addComma = "," + _addComma;};
			_addition = [_x, _addComma, _configCategory, _propertyName, _i] call getPropertyValue;
			_classBody = _classBody + _addition;
			_i = _i + 1;
		} foreach _classProperties;  //For each property in class
		_classBody = _classBody + "\n" + (_addComma splitString ",\n" joinString "") + "}";
		_classBody
};

getPropertyValue = {
	params ["_property", "_addComma", "_configCategory", "_propertyName", "_i"];

	private _classBody = "";

	_propertyNameArray = _propertyName splitString "/";
	_propertyNameLast = toLower (_propertyNameArray select (count _propertyNameArray - 1));

	if (isText _property) then {
		_strProperty = str _property;

		  //diag_log(format["Before if it contains ammo: _property: %1 | _propertyNameLast: %2", _property, _propertyNameLast]);

		if (((_propertyNameLast == "ammo") || (_propertyNameLast == "submunitionammo")) && getText _property != "") then {

			_ammoType = "Ammo/SubmunitionAmmo";
			if (_propertyNameLast find "submunitionammo" != -1) then {
				  //diag_log("submunitionammo");
				_ammoType = "SubmunitionAmmo";
			};
			if (_propertyNameLast find "ammo" != -1) then {
				  //diag_log("ammo");
				_ammoType = "Ammo";
			};

			  //diag_log(format["Looking for ammo | %1", _property]);

			_ammoName = getText _property;

			diag_log(format["%1 = `%2`", _ammoType, _ammoName]);

			//Class here: bin\config.bin/CfgWeapons/SMG_01_Base/Burst"
			_splitClass = str _property splitString "\/";
			//Remove "bin" and "config.bin"
			_splitClass deleteRange [0, 2];

			_countSplitClass = count _splitClass;
			//Add comment showing class
			_classBody = _classBody + format["%1    # %2: %3 [Indent level: %4]", _addComma, _ammoType, (_splitClass joinString "/"), str (_countSplitClass - 2)];
			//Classes with "ammo" first will not have a ,\n for whatever reason - adding it here
			if (_addComma find ",\n" == -1) then {_addComma = ",\n" + _addComma};
			_classBody = _classBody + format['%1    "%2": {%3        "_dictAmmoName": "%4"', _addComma, _propertyNameLast, _addComma splitString "," joinString "", ((getText _property) splitString "\" joinString "/") splitString '"' joinString "`"];

			_ammoProperties = configProperties [configFile >> "CfgAmmo" >> _ammoName];
			{
				_addition = [_x, _addComma + "    ", _configCategory, (((str _x) splitString "\") joinString "/"), _i] call getPropertyValue;
				_classBody = _classBody + _addition;
				_i = _i + 1;
			} forEach _ammoProperties;
			_classBody = _classBody + _addComma + "    }"

		};
		if ((_propertyNameLast == "recoil") || (_propertyNameLast == "recoilprone")) then {
			_configDir = configFile >> "CfgRecoils" >> getText _property;

			if (isClass _configDir) then {
				_classBody = _classBody + format["%1    # Recoil Class: %2", _addComma, _propertyNameLast];
				_classBody = [_configDir, _classBody, _addComma, _propertyNameLast, "CfgRecoils"] call getClass;
			};
			if (isArray _configDir) then {
				_classBody = _classBody + format["%1    # Recoil Array: %2", _addComma, _propertyNameLast];
				_classBody = _classBody + format['%1    "%2": %3', _addComma, _propertyNameLast, getArray _configDir];
			};
		}
		else {_i = _i + 1; _classBody = _classBody + format['%1    "%2": "%3"', _addComma, _propertyNameLast, ((getText _property) splitString "\" joinString "/") splitString '"' joinString "`"];};
	};
	if (isNumber _property) then { _classBody = _classBody + format['%1    "%2": %3', _addComma, _propertyNameLast, getNumber _property]; };
	if (isArray _property) then {
		if ((_propertyNameLast == "ammo") || (_propertyNameLast == "submunitionammo")) then {
			_ammoName = getArray _property;

			_ammoType = "Ammo/SubmunitionAmmo";
			if (_propertyNameLast find "submunitionammo" != -1) then {
				//diag_log("submunitionammo");
				_ammoType = "SubmunitionAmmo";
			};
			if (_propertyNameLast find "ammo" != -1) then {
				//diag_log("ammo");
				_ammoType = "Ammo";
			};

			diag_log("LISTING SUBMUNITIONS");
			_y = 1;
			_possibilityCount = 0;
			//diag_log(_ammoName);
			{
				if (typeName _x == "STRING") then {
					diag_log(format["%1 = `%2`", _ammoType, _x]);

					//Class here: bin\config.bin/CfgWeapons/SMG_01_Base/Burst"
					_splitClass = str _property splitString "\/";
					//Remove "bin" and "config.bin"
					_splitClass deleteRange [0, 2];

					_countSplitClass = count _splitClass;
					//Add comment showing class
					_classBody = _classBody + format["%1    # %2: %3 [Indent level: %4]", _addComma, _ammoType, (_splitClass joinString "/"), str (_countSplitClass - 2)];
					//Classes with "ammo" first will not have a ,\n for whatever reason - adding it here
					if (_addComma find ",\n" == -1) then {_addComma = ",\n" + _addComma};

					diag_log format["_ammoName: %1 | selectPos: %2 | typeName of _ammoName: %3", _ammoName, _y + _possibilityCount, typeName _ammoName];
					if (typeName (getArray _property select (_y + _possibilityCount)) == "SCALAR") then {
						diag_log(format["Submunitionammo = %1 | Chance = %2 | _y = %3", _x, (getArray _property select (_y + _possibilityCount)), str _y]);
						_classBody = _classBody + format['%1    "%2": {%3        "_dictAmmoName": "%4"%5        "_dictAmmoChance": "%6"', _addComma, "submunitionammo" +  str _y, _addComma splitString "," joinString "", _x, _addComma, (getArray _property select (_y + _possibilityCount))];
						_possibilityCount = _possibilityCount + 1;
					}
					else {
						diag_log(format["Submunitionammo = %1 | No Chance Found", _x]);
						_classBody = _classBody + format['%1    "%2": {%3        "_dictAmmoName": "%4"', _addComma, "submunitionammo" +  str _y, _addComma splitString "," joinString "", _x];
					};

					_ammoProperties = configProperties [configFile >> "CfgAmmo" >> _x];
					{
						_addition = [_x, _addComma + "    ", _configCategory, (((str _x) splitString "\") joinString "/"), _i] call getPropertyValue;
						_classBody = _classBody + _addition;
						_i = _i + 1;
					} forEach _ammoProperties;
					_classBody = _classBody + _addComma + "    }";

					_y = _y + 1;
				};
			} forEach _ammoName;
		};
		if (_propertyNameLast == "magazines") then {
			diag_log format["_property: %1", getArray _property];

			//entryClass = weapon/vehicle/etc class (im very lazy)
			_entryClass = _propertyNameArray select 2;
			_weaponCompatableMagazines = [_entryClass] call BIS_fnc_compatibleMagazines;

			if (count _weaponCompatableMagazines > 0) then {
				diag_log format["_weaponCompatableMagazines: %1 | count _weaponCompatableMagazines: %2", _weaponCompatableMagazines, count _weaponCompatableMagazines];

				//Beautify _weaponCompatableMagazines (seperate into rows)
				_newLineSpace = "        ";
				_lastMagazine = _weaponCompatableMagazines select ((count _weaponCompatableMagazines) - 1);
				_magazineRowCount = 0;
				_compatableMagazinesString = "[" + (_addComma splitString "," joinString "") + "        ";
				{
					_compatableMagazinesString = _compatableMagazinesString + '"' + _x + '"';
					_magazineRowCount = _magazineRowCount + 1;

					if (_magazineRowCount == 4) then {
						if (_x == _lastMagazine) then {_newLineSpace = "    ";};
						_compatableMagazinesString = _compatableMagazinesString + _addComma + _newLineSpace;
						_magazineRowCount = 0;
					} else {
						_compatableMagazinesString  = _compatableMagazinesString + ",";
					};
				} forEach _weaponCompatableMagazines;
				_compatableMagazinesString = _compatableMagazinesString + "]";

				//Append to _classBody
				_classBody = _classBody + format["%1    # Compatible Magazines: %2 parameter (+ inherited)", _addComma, _propertyNameLast];
				_classBody = _classBody + format['%1    "magazines": %2', _addComma, _compatableMagazinesString];
			}
			else {
				_classBody = _classBody + format['%1    "%2": %3', _addComma, _propertyNameLast, (str getArray _property) splitString "\" joinString "/"]; 
			};
		}
		//else {_classBody = _classBody + format['%1    "%2": %3', _addComma, _propertyNameLast, (str getArray _property) splitString "\" joinString "/"];}
		else {_classBody = _classBody + _addComma + '    "' + _propertyNameLast + '": ' + ((str getArray _property) splitString "\" joinString "/");}
	};
	if (isClass _property) then {
		_classBody = [_property, _classBody, _addComma, _propertyNameLast, _configCategory] call getClass;
	};
	_classBody
};


getProperties = {
	params ["_newClass", "_classBody", "_configCategory"];

	diag_log(format["Recieved %1 %2", _newClass, _configCategory]);

	//Get all sub-classes of the current class (not including sub-classes from inherited classes)
	//error ends here^
	//_configClasses = "true" configClasses (configFile >> _configCategory >> _x);

	//Get all properties not in a sub-class of the current class
	_properties = configProperties [configFile >> _configCategory >> _newClass];

	// If the class is a vehicle, find the relevant turret properties (elevation, weapon, ammuniton etc)
	// if (_configCategory == "CfgVehicles") then {
	// 	Get all properties from the sub-sub-class "MainTurret" in the "Turrets" sub-class
	// 	_properties append configProperties [configFile >> _configCategory >> _newClass >> "Turrets" >> "MainTurret"];
	// };

	_i = 1;
	_addComma = "";
	{
		//Sanitized property name for writing to file
		_propertyName =  str _x splitString "\" joinString "/";

		// //Only want to add a comma on lines before the last item
		if (_i >= 2) then { _addComma = ",\n"; };

		_addition = [_x, _addComma, _configCategory, _propertyName, _i] call getPropertyValue;
		_classBody = _classBody + _addition;

		_i = _i + 1;
	} foreach _properties;  //For each property in class
	  //diag_log("finished properties");

	//Add closing brace and return body
	  //diag_log(format["Classbody is: %1", _classBody]);
	//_classBody = _classBody + "\n    }";

	//Return _classBody
	_classBody
};


_basePath = "F:\USBBACKUP\GitHub\Arma-Class-Exporter\Exports\";
{
	{
		i = 0;
		_configCategory = "";
		_folder = "";
		_path = "";
		_array = _x;
		{
			//Create the start of the file, classname with brace for dict
			diag_log(format["On: %1", _x]);
			if (i == 1) then {_configCategory = _x; _classBody = _classBody + _folder + " = {";};
			if (i == 0) then {_folder = _x; };
			if (i > 1) then {
				_classBody = toLower _x + " = {\n";

				_classBody = [_x, _classBody, _configCategory] call getProperties;
				//Create path to write class data to
				_path = _basePath + _folder + "/" + toLower _x + ".py";

				if (_x != (_array select (count _array - 1))) then {
					_classBody = _classBody + ",";
				};


				//Write class to its own file
				diag_log(format["Wrote to %1", _path]);

				//seperate lines in .rpt by a line
				diag_log("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=");

				//add final brace
				_classBody = _classBody + "\n}";

				//KillZoneKidd's make_file_x64 .dll linked in repo
					//(Cannot write tabs to file, using spaces instead)
				"make_file" callExtension (_path + "|" + _classBody);
			};
			i = i + 1;
		} foreach _x; //for each class for the side in the category

		_folderCategoryName = (_folder splitString "\") select 1;
		//I don't know what this is v
		//_combinedPath = _basePath + _folder + "/" + _folderCategoryName + ".py";

		diag_log(format["_basePath           = %1", _basePath]);
		diag_log(format["_folder             = %1", _folder]);
		diag_log(format["_folderCategoryName = %1", _folderCategoryName]);
		//Seriously what was this v
		//diag_log(format["Trying to write to %1", _combinedPath]);
	} foreach _x; //For each side in category
} foreach _sideMatrix;  //For each category in sidematmarix


//TODO: Add more comments