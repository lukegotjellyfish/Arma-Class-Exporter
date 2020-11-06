addSpace = {
	diag_log("");
	diag_log("");
	diag_log("");
	diag_log("");
	diag_log("");
	diag_log("");
	diag_log("");
	diag_log("");
	diag_log("");
	diag_log("");
	diag_log("");
	diag_log("");
	diag_log("");
	diag_log("");
	diag_log("");
	diag_log("");
	diag_log("");
	diag_log("");
};

_mods = ["CfgVehicles","CfgWeapons","CfgGlasses","CfgMagazines"];
{
	_rhsafrf = "'@RHSAFRF' in (configSourceModList _x)" configClasses (configFile >> _x) apply {configName _x};
	_rhsusaf = "'@RHSUSAF' in (configSourceModList _x)" configClasses (configFile >> _x) apply {configName _x};
	_rhsgref = "'@RHSGREF' in (configSourceModList _x)" configClasses (configFile >> _x) apply {configName _x};
	_rhssaf  = "'@RHSSAF' in (configSourceModList _x)"  configClasses (configFile >> _x) apply {configName _x};

	_config = [];
	_config append _rhsafrf;
	_config append _rhsusaf;
	_config append _rhsgref;
	_config append _rhssaf;
	diag_log(format["START %1", _x]);
	{
		diag_log(_x);
	} forEach _config;
	call addSpace;
} forEach _mods;