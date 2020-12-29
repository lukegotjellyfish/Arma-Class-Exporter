# -*- coding: utf-8 -*-
import CombinedBluFor
import CombinedOpFor
import re

match      = r"([^,]*),([^,]*),([^,]*),"
substitute = r'\1,\2,\3,\n	'

print("M4A1 Block II:\n" +
	"	Recoil: "           + str(CombinedBluFor.BluFor["BluForWeapons"]["rhs_weap_m4a1_blockii"]["recoil"]).replace(" ", "").replace(",'", ",\n	"))#                    +
	#"\n	SingleNormal: "   + re.sub(match, substitute, str(CombinedBluFor.BluFor["BluForWeapons"]["rhs_weap_m4a1_blockii"]["single"]["recoil"]).replace(" ", ""))        +
	#"\n	 SingleProne: "   + re.sub(match, substitute, str(CombinedBluFor.BluFor["BluForWeapons"]["rhs_weap_m4a1_blockii"]["single"]["recoilprone"]).replace(" ", ""))   +
	#"\n	  AutoNormal: "   + re.sub(match, substitute, str(CombinedBluFor.BluFor["BluForWeapons"]["rhs_weap_m4a1_blockii"]["fullauto"]["recoil"]).replace(" ", ""))      +
	#"\n	   AutoProne: "   + re.sub(match, substitute, str(CombinedBluFor.BluFor["BluForWeapons"]["rhs_weap_m4a1_blockii"]["fullauto"]["recoilprone"]).replace(" ", "")) + "\n")
print("SCAR-H:\n" +
	"	Recoil: "           + str(CombinedBluFor.BluFor["BluForWeapons"]["rhs_weap_scarh_std"]["recoil"]).replace(" ", "").replace(",'", ",\n	"))#                       +
	#"\n	SingleNormal: "   + re.sub(match, substitute, str(CombinedBluFor.BluFor["BluForWeapons"]["rhs_weap_scarh_std"]["single"]["recoil"]).replace(" ", ""))           +
	#"\n	 SingleProne: "   + re.sub(match, substitute, str(CombinedBluFor.BluFor["BluForWeapons"]["rhs_weap_scarh_std"]["single"]["recoilprone"]).replace(" ", ""))      +
	#"\n	  AutoNormal: "   + re.sub(match, substitute, str(CombinedBluFor.BluFor["BluForWeapons"]["rhs_weap_scarh_std"]["fullauto"]["recoil"]).replace(" ", ""))         +
	#"\n	   AutoProne: "   + re.sub(match, substitute, str(CombinedBluFor.BluFor["BluForWeapons"]["rhs_weap_scarh_std"]["fullauto"]["recoilprone"]).replace(" ", ""))    + "\n")
print("M-14:\n" +
	"	Recoil: "           + str(CombinedBluFor.BluFor["BluForWeapons"]["rhs_weap_m14ebrri"]["recoil"]).replace(" ", "").replace(",'", ",\n	"))


print("AS Val:\n" +
	"	Recoil: "           + str(CombinedOpFor.OpFor["OpForWeapons"]["rhs_weap_asval"]["recoil"]).replace(" ", "").replace(",'", ",\n	"))#                              + 
	#"\n	SingleNormal: "   + re.sub(match, substitute, str(CombinedOpFor.OpFor["OpForWeapons"]["rhs_weap_asval"]["single"]["recoil"]).replace(" ", ""))                  +
	#"\n	 SingleProne: "   + re.sub(match, substitute, str(CombinedOpFor.OpFor["OpForWeapons"]["rhs_weap_asval"]["single"]["recoilprone"]).replace(" ", ""))             +
	#"\n	  AutoNormal: "   + re.sub(match, substitute, str(CombinedOpFor.OpFor["OpForWeapons"]["rhs_weap_asval"]["fullauto"]["recoil"]).replace(" ", ""))                +
	#"\n	   AutoProne: "   + re.sub(match, substitute, str(CombinedOpFor.OpFor["OpForWeapons"]["rhs_weap_asval"]["fullauto"]["recoilprone"]).replace(" ", "")))

# re.sub(match, substitute, 


# text = re.sub("(?:r|l)", "w", text)
