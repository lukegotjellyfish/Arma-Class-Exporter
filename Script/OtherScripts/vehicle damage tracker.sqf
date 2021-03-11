//Assign vehicles (vehicle variable name)
v1 = mk19;  //eg v1 = t72;
v2 = a10;
v3 = m1a1fep;

//Start values at zero to see damage that has already occured [SET TO 1]
//Start values at the current values
assumeVehicleIsUndamaged = 0;

//https://community.bistudio.com/wiki/DIK_KeyCodes
// 39 = ; Key
//  6 = 5 Key
diagToggleKey   = 39;
updateDamageKey = 6;
















startVehicle = (vehicle player);
vehicleFired = startVehicle addeventhandler ["Fired", {
	(_this select 0) setvehicleammo 1;
	startVehicle setWeaponReloadingTime [gunner startVehicle, currentMuzzle (gunner startVehicle), 0];
}];
playerFired = player addeventhandler ["Fired", {(_this select 0) setvehicleammo 1}];
//Toggle values for each addAction
v1Toggle = 0;
v2Toggle = 0;
v3Toggle = 0;
//Player's vehicle for each option
v1Name = getText (configFile >> "CfgVehicles" >> typeOf v1 >> "displayName");
v2Name = getText (configFile >> "CfgVehicles" >> typeOf v2 >> "displayName");
v3Name = getText (configFile >> "CfgVehicles" >> typeOf v3 >> "displayName");

gameIsDiag = false;
if ((productVersion select 4) == "Diag") then {
	diagToggle = (findDisplay 46) displayAddEventHandler ["KeyDown", {
		params["_display", "_keyCode", "_shft", "_ctr", "_alt" ];

		if (_keyCode == diagToggleKey) then {
			//diag_toggle is a function of the dev branch https://community.bistudio.com/wiki/Arma_3_Diagnostics_Exe
			diag_toggle 'shots';
			[] spawn {uiSleep 0.001; diag_toggle 'shots'};
			//To have two diag_toggles, there needs to be a delay
		};
	}];
	gameIsDiag = true;
};

countHitpoints = {
	params ["_vx", "_hintTitle"];

	//_damageEntry: array of hitpoints damage values
	_damageEntry = [];
	//_size: starting size of _damageEntry to be overwritten to manipulate it
	_size = 0;

	if (assumeVehicleIsUndamaged == 1) then {
		{
			//Increment _size by one for each hitpoint
			_size = _size + 1;
			//Increase array size by one to accomodate for the new value
			_damageEntry resize _size;
			//Set new array item value to 0 as that is the default damage state
			_damageEntry set [_size -1, 0];
		} forEach (getAllHitPointsDamage _vx select 0);
	} else {_ddamageEntry = getAllHitPointsDamage _vx select 2};
	//getAllHitPointsDamage _vx returns:
	// array of hit point names
	// array of hit selection names
	// array of damage values
	//As all we need right now is the number of hitpoints, take the name array

	//_dbg: string to show the number of hitpoints for the vehicle
	// Will appear as ""
	_dbg = _hintTitle + str(_size);
	hint _dbg;

	//Returning:
	// _damageEntry
	// Total vehicle damage
	[_damageEntry, damage _vx];
};

damageLog = {
	params ["_vx", "_vxDamageEntry", "_vxTotalDamage"];

	//vx_HitpointsDamageArray: Array to store the arrays from getAllHitPointsDamage <vehicle>
	vx_HitpointsDamageArray = getAllHitPointsDamage _vx;
	//vx_HitPointsNames: Array of all hitpoint names
	vx_HitPointsNames = vx_HitpointsDamageArray select 0;
	//vx_HitpointsDamage: Array of all current hitpoint damages
	vx_HitpointsDamage = vx_HitpointsDamageArray select 2;

	//_damageDone: string to build the list of damaged hitpoints on
	// to then display to the user as a hint
	_damageDone = "";
	//_i: int to be used as an index
	_i = 0;
	{
		//_damage: Saved damage value for the current hitpoint
		_damage = _vxDamageEntry select _i;
		//If saved damage is not the current damage, there has been a change to display
		if (_x != _damage) then {
			//Save the damage to the damage array to be compared next run
			_vxDamageEntry set [_i, _x];
			//_name: name of the current hitpoint
			_name = vx_HitPointsNames select _i;
			//Append the information for the current hitpoint onto the damaged hitpoints string
			_damageDone = _damageDone + _name + ": " + str(_x) + " (" + str(_x - _damage) + ")\n";
		};
		_i = _i + 1;
	} forEach vx_HitpointsDamage; //Loop through every hitpoint damage value

	//Get current Total damage of the vehicle
	_damage = damage _vx;
	//Display the damage analysis string:
	// Total Damage: 0-1
	// <hitpointname>: <hitpoint damage> (<damage change>)...
	hint format["Total Damage: %1 (%2)\n%3",_damage,(_damage-_vxTotalDamage),_damageDone];

	//Returning:
	// Array of hitpoint damages
	// Total damage of the vehicle
	[vx_HitpointsDamage,_damage];
};

toggleLogger = {
	params ["_vx", "_vxToggle", "_vxName"];

	(findDisplay 46) setVariable["_vx", _vx];

	if (_vxToggle == 1) then {
		_nameCount = _vxName + " Hitpoints: ";
		_damageArray = [_vx, _nameCount] call countHitPoints;
		vxDamageEntry = _damageArray select 0;
		vxTotalDamage = _damageArray select 1;

		vxDisplayHandler = (findDisplay 46) displayAddEventHandler ["KeyDown", {
			params["_display", "_keyCode", "_shft", "_ctr", "_alt" ];

			if (_keyCode == updateDamageKey) then {
				vxDamageArray = [_display getVariable "_vx", vxDamageEntry, vxTotalDamage] call damageLog;
				vxDamageEntry = vxDamageArray select 0;
				vxTotalDamage = vxDamageArray select 1;
			};
		}];
	}
	else {(findDisplay 46) displayRemoveEventHandler ["KeyDown", vxDisplayHandler];};
};


v1Success = 0;
v2Success = 0;
v3Success = 0;
if (count (str v1) > 0) then {
	v1AddAction = player addAction [format["Toggle %1 monitor", v1Name], {
		if (v1Toggle == 0) then {v1Toggle = 1} else {v1Toggle = 0};
		[v1, v1Toggle, v1Name] call toggleLogger;
	}];
	v1Success = 1;
} else {diag_log("v1 not valid")};

if (count (str v2) > 0) then {
	v2AddAction = player addAction [format["Toggle %1 monitor", v2Name], {
		if (v2Toggle == 0) then {v2Toggle = 1} else {v2Toggle = 0};
		[v2, v2Toggle, v2Name] call toggleLogger;
	}];
	v2Success = 1;
} else {diag_log("v2 not valid")};

if (count (str v3) > 0) then {
	v3AddAction = player addAction [format["Toggle %1 monitor", v3Name], {
		if (v3Toggle == 0) then {v3Toggle = 1} else {v3Toggle = 0};
		[v3, v3Toggle, v3Name] call toggleLogger;
	}];
	v3Success = 1;
} else { diag_log("v3 not valid")};


vRemove = player addAction ["Remove and disable options", {
	//Remove this action because where else would it be removed
	player removeaction vRemove;

	//Remove vehicle toggle actions
	if (v1Success == 1) then {
		player removeAction v1AddAction;
		if (v1Toggle == 1) then {[v1, 0, v1Name] call toggleLogger};
	};
	if (v2Success == 1) then {
		player removeAction v2AddAction;
		if (v2Toggle == 1) then {[v2, 0, v2Name] call toggleLogger};
	};
	if (v3Success == 1) then {
		player removeAction v3AddAction;
		if (v3Toggle == 1) then {[v3, 0, v3Name] call toggleLogger};
	};


	//Remove diag_toggle eventhandler
	if (gameIsDiag == true) then {(findDisplay 46)  displayRemoveEventHandler ["KeyDown", diagToggle]};
	//Remove unlimited ammo eventhandlers
	try {
		startVehicle removeEventHandler ["Fired", vehicleFired];
	} catch {
		diag_log(format["Error in <vehicleFired removeEventHandler>: %1", _exception]);
	};
	player removeEventHandler ["Fired", playerFired];
}];