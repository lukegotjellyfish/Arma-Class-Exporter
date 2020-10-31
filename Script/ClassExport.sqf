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
	//vehicle magazine matrix
	[
		//BluFor
		[
			"BluFor\VehicleMagazines",
			"CfgMagazines",
			"rhs_mag_1150Rnd_30x173_mixed",
			"rhsusf_mag_L8A3_8"
		],
		//OpFor
		[
			"OpFor\VehicleMagazines",
			"CfgMagazines",
			"rhs_mag_127x108mm_1SLT_1470",
			"RHS_mag_VOG30_30"
		]
	]
];


//
// getClass:
//  This is a function that adds a found class and it's properties to _classBody
//   which is then returned.
//
//  Notes:
//   - Remove _classBody param and instead use _classBody = _classBody + [] call getClass
//      as there is no reason for _classBody to be passed to this function.
//
getClass = {
	params ["_property", "_classBody", "_addComma", "_propertyNameLast", "_configCategory"];

		//diag_log(format["Class here: %1", _property]);

		//Class here: bin\config.bin/CfgWeapons/SMG_01_Base/Burst"
		_splitClass = str _property splitString "\/";
		//Remove "bin" and "config.bin"
		_splitClass deleteRange [0, 2];

		_countSplitClass = count _splitClass;
		//Add comment showing class
		_classBody = _classBody + format["%1    # Class: %2 [Indent level: %3]", _addComma, (_splitClass joinString "|"), str (_countSplitClass - 2)];
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
			_propertyName =  str _x splitString "\" joinString "|";
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
			_classBody = _classBody + format["%1    # %2: %3 [Indent level: %4]", _addComma, _ammoType, (_splitClass joinString "|"), str (_countSplitClass - 2)];
			//Classes with "ammo" first will not have a ,\n for whatever reason - adding it here
			if (_addComma find ",\n" == -1) then {_addComma = ",\n" + _addComma};
			_classBody = _classBody + format['%1    "%2": {%3        "_dictAmmoName": "%4"', _addComma, _propertyNameLast, _addComma splitString "," joinString "", ((getText _property) splitString "\" joinString "|") splitString '"' joinString "`"];

			_ammoProperties = configProperties [configFile >> "CfgAmmo" >> _ammoName];
			{
				_addition = [_x, _addComma + "    ", _configCategory, (((str _x) splitString "\") joinString "|"), _i] call getPropertyValue;
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
		else {_i = _i + 1; _classBody = _classBody + format['%1    "%2": "%3"', _addComma, _propertyNameLast, ((getText _property) splitString "\" joinString "|") splitString '"' joinString "`"];};
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
			{
				if (typeName _x == "STRING") then {
					diag_log(format["%1 = `%2`", _ammoType, _x]);

					//Class here: bin\config.bin/CfgWeapons/SMG_01_Base/Burst"
					_splitClass = str _property splitString "\/";
					//Remove "bin" and "config.bin"
					_splitClass deleteRange [0, 2];

					_countSplitClass = count _splitClass;
					//Add comment showing class
					_classBody = _classBody + format["%1    # %2: %3 [Indent level: %4]", _addComma, _ammoType, (_splitClass joinString "|"), str (_countSplitClass - 2)];
					//Classes with "ammo" first will not have a ,\n for whatever reason - adding it here
					if (_addComma find ",\n" == -1) then {_addComma = ",\n" + _addComma};
					_classBody = _classBody + format['%1    "%2": {%3        "_dictAmmoName": "%4"', _addComma, "submunitionammo" +  str _y, _addComma splitString "," joinString "", _x];

					_ammoProperties = configProperties [configFile >> "CfgAmmo" >> _x];
					{
						_addition = [_x, _addComma + "    ", _configCategory, (((str _x) splitString "\") joinString "|"), _i] call getPropertyValue;
						_classBody = _classBody + _addition;
						_i = _i + 1;
					} forEach _ammoProperties;
					_classBody = _classBody + _addComma + "    }";

					_y = _y + 1;
				};
			} forEach _ammoName;
		}
		else {_classBody = _classBody + format['%1    "%2": %3', _addComma, _propertyNameLast, (str getArray _property) splitString "\" joinString "|"]; }
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
		_propertyName =  str _x splitString "\" joinString "|";

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


_basePath = "E:\USBBACKUP\GitHub\Arma-Class-Exporter\Exports\";
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
		_combinedPath = _basePath + _folder + "/" + _folderCategoryName + ".py";

		diag_log(format["_basePath           = %1", _basePath]);
		diag_log(format["_folder             = %1", _folder]);
		diag_log(format["_folderCategoryName = %1", _folderCategoryName]);
		diag_log(format["Trying to write to %1", _combinedPath]);
	} foreach _x; //For each side in category
} foreach _sideMatrix;  //For each category in sidematmarix


//TODO: Add more comments