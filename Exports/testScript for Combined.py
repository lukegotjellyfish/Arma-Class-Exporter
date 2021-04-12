# -*- coding: utf-8 -*-
import CombinedBluFor
import CombinedOpFor
import re

match      = r"([^,]*),([^,]*),([^,]*),"
substitute = r'\1,\2,\3,\n	'

b = "BluFor"
o = "OpFor"
weps = [[b,"rhs_weap_sr25"],[b,"rhs_weap_m14ebrri"]]
for weapon in weps:
	_cla = weapon[0] + "Weapons"
	print(weapon[1]+ ":\n" +
		"	Recoil: "           + str(CombinedBluFor.BluFor[_cla][weapon[1]]["recoil"]).replace(" ", "").replace(",'", ",\n	")+
		"\n	SingleNormal: "   + re.sub(match, substitute, str(CombinedBluFor.BluFor[_cla][weapon[1]]["single"]["recoil"]).replace(" ", ""))        +
		"\n	 SingleProne: "   + re.sub(match, substitute, str(CombinedBluFor.BluFor[_cla][weapon[1]]["single"]["recoilprone"]).replace(" ", ""))   +
		"\n	  AutoNormal: "   + re.sub(match, substitute, str(CombinedBluFor.BluFor[_cla][weapon[1]]["fullauto"]["recoil"]).replace(" ", ""))      +
		"\n	   AutoProne: "   + re.sub(match, substitute, str(CombinedBluFor.BluFor[_cla][weapon[1]]["fullauto"]["recoilprone"]).replace(" ", "")) + "\n")


# re.sub(match, substitute, 


# text = re.sub("(?:r|l)", "w", text)
