# -*- coding: utf-8 -*-
from ExportList import ExportList

bluForScopes = [
    "rhsusf_acc_premier_mrds",
    "rhsusf_acc_m8541_low",
    "rhsusf_acc_eotech_552",
    "rhsusf_acc_eotech_xps3",
]

mod = "RHS"  # Folder name of RHS Export
with open("#CSV_Exports/"+mod+"/bluForScopeExport.csv", "w", newline='\n') as csvfile:
    bluForScopeExport = ExportList(mod,bluForScopes,csvfile)
    bluForScopeExport.setFov(0.75,5) # Default Arma FOV is 0.75
    bluForScopeExport.exportList("Scope",0)

#with open("#CSV_Exports/"+mod+"/opForWeaponExport.csv", "w", newline='\n') as csvfile:
#    opForWeaponExport = ExportList(mod,opForWeapons,csvfile)
#    opForWeaponExport.hitRanges = [100,200,300,400,500,1000,1500,2000]
#    opForWeaponExport.exportList("Weapon")