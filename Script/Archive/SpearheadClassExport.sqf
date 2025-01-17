// Step 1: Run regex replace //.*|/\*[\s\S\n]*\*/ with nothing to remove all comments because sqf doesn't like them
// Step 2: Set the folder to export to (Create this folder yourself)
// Step 3: Create the folders Magazines,Vehicles,Weapons,Glasses in this folder as well
_basePath = "C:\Users\Lukeg\Desktop\GitHub\MyRepos\Arma-Class-Exporter\Exports\SQF-Class-Exports\Spearhead_1944\";

//
// _sideMatrix:
//  1. Categorise classes of the same kind to iterate through to
//      save to directories specific to each array, for ease of use.
//  2. It modular so nothing in the script is dependant on the mods
//      and can be configured easily through the array instead of
//      the rest of the script.
//  3. Classes are grouped by faction in the sub-sub array allowing for
//      ease of comprehension and addition for other sides.

_sideMatrix = [];
_mods = [["CfgWeapons","Weapons"],["CfgMagazines","Magazines"],["CfgVehicles","Vehicles"],["CfgGlasses","Glasses"],["CfgAmmo","Ammo"]]; //["CfgWeapons","Weapons"],["CfgMagazines","Magazines"],["CfgVehicles","Vehicles"],["CfgGlasses","Glasses"]
{
    _configClass = _x select 0;
    _spearhead = "'SPE' in (configSourceModList _x)" configClasses (configFile >> _configClass) apply {configName _x};

    _config = [];
    _config append _spearhead;
    
    // All classes with no filtering:
    //_allClasses = "true" configClasses (configFile >> _configClass) apply {configName _x};
    //_config append _allClasses;

    _folder = _x select 1;
    _config insert [0,[_folder,_configClass]];

    _sideMatrix append [[_config]];
} forEach _mods;




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
    params ["_property", "_classBody", "_propertyNameLast", "_configCategory", "_exportClass"];
        //_property: 
        //_classBody: The body of the exporter class
        //_propertyNameLast: 
        //_configCategory: CfgWeapons/CfgVehicles for current export class
        //_exportClass: 



        //diag_log(format["Class here: %1", _property]);

        //Class here: bin\config.bin/CfgWeapons/SMG_01_Base/Burst"
        _splitClass = str _property splitString "\/";
        //Remove "bin" and "config.bin"
        _splitClass deleteRange [0, 2];

        _countSplitClass = count _splitClass;
        _classBody = _classBody + format['"%1": {', _propertyNameLast];

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

        _i = 1;
        {
            //Sanitized property name for writing to file
            _propertyName =  str _x splitString "\" joinString "/";
            _addition = [_x, _configCategory, _propertyName, _i, _exportClass] call getPropertyValue;
            _classBody = _classBody + _addition;
            _i = _i + 1;

        } foreach _classProperties;  //For each property in class

        _classBody = _classBody + "},";
        _classBody
};

getPropertyValue = {
    params ["_property", "_configCategory", "_propertyName", "_i", "_exportClass"];

    private _classBody = "";

    _propertyNameArray = _propertyName splitString "/";
    //_propertyNameLast is the parameter
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

            //diag_log(format["%1 = `%2`", _ammoType, _ammoName]);

            //Class here: bin\config.bin/CfgWeapons/SMG_01_Base/Burst"
            _splitClass = str _property splitString "\/";
            //Remove "bin" and "config.bin"
            _splitClass deleteRange [0, 2];

            _countSplitClass = count _splitClass;
            _classBody = _classBody + format['"%1": {"_dictAmmoName": "%2",', _propertyNameLast, ((getText _property) splitString "\" joinString "/") splitString '"' joinString "`"];

            _ammoProperties = configProperties [configFile >> "CfgAmmo" >> _ammoName];
            {
                _addition = [_x, _configCategory, (((str _x) splitString "\") joinString "/"), _i, _exportClass] call getPropertyValue;
                _classBody = _classBody + _addition;
                _i = _i + 1;
            } forEach _ammoProperties;
            _classBody = _classBody + "},"

        };
        if ((_propertyNameLast == "recoil") || (_propertyNameLast == "recoilprone")) then {
            _configDir = configFile >> "CfgRecoils" >> getText _property;

            if (isClass _configDir) then {
                _classBody = [_configDir, _classBody, _propertyNameLast, "CfgRecoils", _exportClass] call getClass;
            };
            if (isArray _configDir) then {
                _classBody = _classBody + format['"%1": %2,', _propertyNameLast, getArray _configDir];
            };
        };
        if ((_propertyNameLast == "vehicleclass") && ((getText _property == "rhs_vehclass_aircraft") || (getText _property == "rhs_vehclass_helicopter"))) then {
            _vehCompatiblePylons = _exportClass getCompatiblePylonMagazines 0;
            //diag_log format["%1 getCompatiblePylonMagazines 0 = %2", _exportClass, _vehCompatiblePylons];
            _classBody = _classBody + format['"%2": "%3",', _propertyNameLast, getText _property];
            _classBody = _classBody + format['"pylonmagazines": ['];
            {
                _classBody = _classBody + str _x + ",";
            } forEach _vehCompatiblePylons;
            _classBody = _classBody + "],";
        }
        else {_i = _i + 1; _classBody = _classBody + format['"%1": "%2",', _propertyNameLast, ((getText _property) splitString "\" joinString "/") splitString '"' joinString "`"];};
    };
    if (isNumber _property) then { _classBody = _classBody + format['"%1": %2,', _propertyNameLast, getNumber _property]; };
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

                    //diag_log format["_ammoName: %1 | selectPos: %2 | typeName of _ammoName: %3", _ammoName, _y + _possibilityCount, typeName _ammoName];
                    if (typeName (getArray _property select (_y + _possibilityCount)) == "SCALAR") then {
                        //diag_log(format["Submunitionammo = %1 | Chance = %2 | _y = %3", _x, (getArray _property select (_y + _possibilityCount)), str _y]);
                        _classBody = _classBody + format['"%1": {"_dictAmmoName": "%2","_dictAmmoChance": "%3",', "submunitionammo" +  str _y, _x, (getArray _property select (_y + _possibilityCount))];
                        _possibilityCount = _possibilityCount + 1;
                    }
                    else {
                        diag_log(format["Submunitionammo = %1 | No Chance Found", _x]);
                        _classBody = _classBody + format['"%1": {"_dictAmmoName": "%2",', "submunitionammo" +  str _y, _x];
                    };

                    _ammoProperties = configProperties [configFile >> "CfgAmmo" >> _x];
                    {
                        _addition = [_x, _configCategory, (((str _x) splitString "\") joinString "/"), _i, _exportClass] call getPropertyValue;
                        _classBody = _classBody + _addition;
                        _i = _i + 1;
                    } forEach _ammoProperties;
                    _classBody = _classBody + "},";

                    _y = _y + 1;
                };
            } forEach _ammoName;
        };
        if (_propertyNameLast == "magazines") then {
            //entryClass = weapon/vehicle/etc class (im very lazy)
            _entryClass = _propertyNameArray select 3;
            _weaponCompatableMagazines = [_exportClass] call BIS_fnc_compatibleMagazines;

            if ((_entryClass != "Default") && (count _weaponCompatableMagazines > 0)) then {

                //Beautify _weaponCompatableMagazines (seperate into rows)
                _lastMagazine = _weaponCompatableMagazines select ((count _weaponCompatableMagazines) - 1);
                _magazineRowCount = 0;
                _compatibleMagazinesString = "[";
                {
                    _compatibleMagazinesString = _compatibleMagazinesString + '"' + _x + '"';
                    _magazineRowCount = _magazineRowCount + 1;
                    _compatibleMagazinesString  = _compatibleMagazinesString + ",";
                } forEach _weaponCompatableMagazines;
                _compatibleMagazinesString = _compatibleMagazinesString + "]";

                //Append to _classBody
                _classBody = _classBody + format['"magazines": %1,', _compatibleMagazinesString];
            }
            else {
                _classBody = _classBody + format['"%1": %2,', _propertyNameLast, (str getArray _property) splitString "\" joinString "/"];
            };
        }
        else {_classBody = _classBody + '"' + _propertyNameLast + '": ' + ((str getArray _property) splitString "\" joinString "/") + ",";}
    };
    if (isClass _property) then {
        _classBody = [_property, _classBody, _propertyNameLast, _configCategory, _exportClass] call getClass;
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
    //  Get all properties from the sub-sub-class "MainTurret" in the "Turrets" sub-class
    //  _properties append configProperties [configFile >> _configCategory >> _newClass >> "Turrets" >> "MainTurret"];
    // };

    _i = 1;
    {
        //Sanitized property name for writing to file
        _propertyName =  str _x splitString "\" joinString "/";

        _addition = [_x, _configCategory, _propertyName, _i, _newClass] call getPropertyValue;
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


//_basePath = "F:\USBBACKUP\GitHub\Arma-Class-Exporter\Exports\Archive RHS\RHS\";
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
                // "d" instead of class name:
                //  My new procedure in Exports/Archive-RHS-Improved
                //   requires a constant dictionary name for importing
                //    as it imports each dictionary individually instead
                //     of using a combined dict
                _classBody = "d" + " = {";

                _classBody = [_x, _classBody, _configCategory] call getProperties;
                //Create path to write class data to
                _path = _basePath + _folder + "/" + toLower _x + ".py";

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