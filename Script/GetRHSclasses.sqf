//Script to get a list of RHS classes in the following cfgs:
//Get all classes in CfgPatches
// sortFactions = {
// 	params ["_array", "_numFactions"];

// 	//_newArray = [];
// 	//_newArray resize (_numFactions - 1);

// 	//Get array offsets to sort each subarray
// 	for "_i" from 0 to (_numFactions - 1) do {
// 		_array set [_i, (_array select _i) arrayIntersect (_array select _i)];
// 	};

// 	//Return sorted array
// 	_array
// };

// // _sides = [["RHS_AFRF"],["RHS_USAF"],["RHS_GREF"],["RHS_SAF"]];
// _cfgPatches           = configProperties [configFile >> "CfgPatches"];
// _rhsWeapons           = [["RHS_AFRF"],["RHS_USAF"],["RHS_GREF"],["RHS_SAF"]];
// _rhsMagazines         = [["RHS_AFRF"],["RHS_USAF"],["RHS_GREF"],["RHS_SAF"]];
// _rhsLaunchers         = [["RHS_AFRF"],["RHS_USAF"],["RHS_GREF"],["RHS_SAF"]];
// _rhsLauncherMagazines = [["RHS_AFRF"],["RHS_USAF"],["RHS_GREF"],["RHS_SAF"]];
// _rhsVehicleWeapons    = [["RHS_AFRF"],["RHS_USAF"],["RHS_GREF"],["RHS_SAF"]];
// _rhsVehicleMagazines  = [["RHS_AFRF"],["RHS_USAF"],["RHS_GREF"],["RHS_SAF"]];
// _i = 0;
// {
// 	//If class is for RHS
// 	_currentCfgPatch = _cfgPatches select _i;
// 	_strCurrentCfgPatch = str _currentCfgPatch;
// 	_cfgPatchClass = ((str _x) splitString "\/") select 3;
// 	if (getText(_currentCfgPatch >> "author") == "Red Hammer Studios") then {
// 		//Get weapons array from rhs cfgPatches class
// 		//diag_log(format["cfgPatch: %1", _cfgPatchClass]);
// 		_weaponsArray = getArray (configFile >> "CfgPatches" >> _cfgPatchClass >> "weapons");

// 		//If the array actually has any values, do:
// 		if (count _weaponsArray > 0) then {
// 			_mod = getArray(configFile >> "CfgPatches" >> _cfgPatchClass >> "requiredAddons");

// 			_modIndex = 0;
// 			switch (_mod select 0) do {
// 				case "rhs_main": {_modIndex = 0};
// 				case "rhsusf_main": {_modIndex = 1};
// 				case "rhsusf_c_heavyweapons": {_modIndex = 1};
// 				case "rhsgref_main": {_modIndex = 2};
// 				case "rhssaf_main": {_modIndex = 3};
// 			};

// 			diag_log(format["_i = %1 - %2", _i, _strCurrentCfgPatch]);
// 			{
// 				_weapMagazines = [_x] call BIS_fnc_compatibleMagazines;
// 				_itemType = _x call BIS_fnc_itemType;

// 				if (_itemType select 0 == "Weapon") then {
// 					if ((_itemType select 1 == "MissileLauncher") || (_itemType select 1 == "RocketLauncher")) then {
// 						(_rhsLaunchers select _modIndex) pushBack _x;
// 						diag_log(format["Launcher added: %1", _x]);
// 						(_rhsLauncherMagazines select _modIndex) append _weapMagazines;
// 					};
// 					if (["rhs_weap_pkt","rhs_weap_nsvt","rhs_weap_dshkm","rhs_weap_kpvt","RHS_M2","RHS_M2_offroad","RHS_M2_M1117","rhs_weap_m240veh","rhs_weap_m240_abrams","rhs_weap_m240_m113","rhs_weap_m240_abrams_coax","RHS_MK19","rhs_weap_M320"] find _x != -1) then {
// 						_itemType = ["VehicleWeapon"];
// 					} else {
// 						(_rhsWeapons select _modIndex) pushBack _x;
// 						diag_log(format["Weapon added: %1", _x]);
// 						(_rhsMagazines select _modIndex) append _weapMagazines;
// 					};
// 				};
// 				if (_itemType select 0 == "VehicleWeapon") then {
// 					(_rhsVehicleWeapons select _modIndex) pushBack _x;
// 					diag_log(format["vWeapon added: %1", _x]);
// 					(_rhsVehicleMagazines select _modIndex) append _weapMagazines;
// 				};
// 			} forEach _weaponsArray;
// 		};
// 	};
// 	_i = _i + 1;
// } forEach _cfgPatches;

// _rhsWeapons           = [_rhsWeapons, count _rhsWeapons] call sortFactions;
// _rhsMagazines         = [_rhsMagazines, count _rhsMagazines] call sortFactions;
// _rhsLaunchers         = [_rhsLaunchers, count _rhsLaunchers] call sortFactions;
// _rhsLauncherMagazines = [_rhsLauncherMagazines, count _rhsLauncherMagazines] call sortFactions;
// _rhsVehicleWeapons    = [_rhsVehicleWeapons, count _rhsVehicleWeapons] call sortFactions;
// _rhsVehicleMagazines  = [_rhsVehicleMagazines, count _rhsVehicleMagazines] call sortFactions;

// "make_file" callExtension ("E:\USBBACKUP\GitHub\Arma-Class-Exporter\Script\autotest\rhsWeapons.txt"           + "|" + str _rhsWeapons);
// "make_file" callExtension ("E:\USBBACKUP\GitHub\Arma-Class-Exporter\Script\autotest\rhsMagazines.txt"         + "|" + str _rhsMagazines);
// "make_file" callExtension ("E:\USBBACKUP\GitHub\Arma-Class-Exporter\Script\autotest\rhsLaunchers.txt"         + "|" + str _rhsLaunchers);
// "make_file" callExtension ("E:\USBBACKUP\GitHub\Arma-Class-Exporter\Script\autotest\rhsLauncherMagazines.txt" + "|" + str _rhsLauncherMagazines);
// "make_file" callExtension ("E:\USBBACKUP\GitHub\Arma-Class-Exporter\Script\autotest\rhsVehicleWeapons.txt"    + "|" + str _rhsVehicleWeapons);
// "make_file" callExtension ("E:\USBBACKUP\GitHub\Arma-Class-Exporter\Script\autotest\rhsVehicleMagazines.txt"  + "|" + str _rhsVehicleMagazines);

// for "_i" from 0 to ((count _rhsWeapons) - 1) do {
// 	{
// 		player addWeapon _x;
// 		_loadout = getUnitLoadout [player, true];

// 		if ((_loadout select 0) select 0 != _x) then {
// 			diag_log("NOT an infantry weapon: " + _x);
// 		};
// 	} foreach (_rhsWeapons select _i);
// };