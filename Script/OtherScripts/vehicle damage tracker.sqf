//Start values at zero to see damage that has already occured [SET TO 1]
//Start values at the current values [SET TO 0]
assumeVehicleIsUndamaged = 0;
//List all hitpoints in the hint [SET TO 1]
//List all recently damaged hitpoints [SET TO 0]
listAllHitpoints = 1;

//https://community.bistudio.com/wiki/DIK_KeyCodes
diagToggleKey   = 39; // ;
updateDamageKey = 6;  // 5
healTargetKey   = 7; //6
designateV1Key  = 35; // H
designateV2Key  = 36; // J
designateV3Key  = 37; // K


startVehicle = (vehicle player);
vehicleFired = startVehicle addeventhandler ["Fired", {
	(_this select 0) setvehicleammo 1;
	// startVehicle setWeaponReloadingTime [gunner startVehicle, currentMuzzle (gunner startVehicle), 0];
}];
playerFired = player addeventhandler ["Fired", {(_this select 0) setvehicleammo 1}];
//Toggle values for each addAction
v1Toggle = 0;
v2Toggle = 0;
v3Toggle = 0;
v1Success = 0;
v2Success = 0;
v3Success = 0;
//Strings
hintStart = "<t align='left'>"; //fix vscode syntax highlighting "</t>"
hintEnd = "</t>";
hitpointDamageText = "<t color='#FF0000'>+"; //fix vscode syntax highlighting "</t>"
hitpointHealText = "<t color='#00FF00'>"; //fix vscode syntax highlighting "</t>"
hitpointTextEnd = "</t>";

// gameIsDiag = false;
// if ((productVersion select 4) == "Diag") then {
// 	diagToggle = (findDisplay 46) displayAddEventHandler ["KeyDown", {
// 		params["_display", "_keyCode", "_shft", "_ctr", "_alt" ];
// 		if (_keyCode == diagToggleKey) then {
// 			//diag_toggle is a function of the dev branch https://community.bistudio.com/wiki/Arma_3_Diagnostics_Exe
// 			//diag_toggle causes scripts to fail when not run on devbranch??
// 			diag_toggle "shots";
// 			[] spawn {uiSleep 0.001; diag_toggle 'shots'};
// 			//To have two diag_toggles, there needs to be a delay
// 		};
// 	}];
// 	gameIsDiag = true;
// };

countHitpoints = {
	params ["_vx", "_hintTitle"];

	//_damageEntry: array of hitpoints damage values
	_damageEntry = getAllHitPointsDamage _vx select 2;  //By default set to existing damage values
	if (assumeVehicleIsUndamaged == 1) then {
		{
			//Set new array item value to 0 as that is the default damage state
			_damageEntry set [_x, 0];
		} forEach _damageEntry;
	};
	//getAllHitPointsDamage _vx returns:
	// array of hit point names
	// array of hit selection names
	// array of damage values
	//As all we need right now is the number of hitpoints, take the name array

	//_dbg: string to show the number of hitpoints for the vehicle
	// Will appear as ""
	_dbg = _hintTitle + str(count _damageEntry);
	hint _dbg;
	diag_log _dbg;

	//Returning:
	// _damageEntry
	// Total vehicle damage
	[_damageEntry, damage _vx];
};

formatHitpointDamage = {
	params ["_newHealth", "_oldHealth"];

	_damageText = str(_newHealth - _oldHealth);

	//damage has been done
	if (_newHealth > _oldHealth) then {
		_damageText = hitpointDamageText + _damageText + hitpointTextEnd;
	} else {
		//hitpoint has healed
		if (_oldHealth > _newHealth) then {
			_damageText = hitpointHealText + _damageText + hitpointTextEnd;
		};
	};
	
	//return damageText
	_damageText
};

damageLog = {
	params ["_vx", "_vxDamageEntry", "_vxTotalDamage", "_vx_HitPointsNames"];

	//vx_HitpointsDamageArray: Array to store the arrays from getAllHitPointsDamage <vehicle>
	vx_HitpointsDamageArray = getAllHitPointsDamage _vx;

	//vx_HitpointsDamage: Array of all current hitpoint damages
	vx_HitpointsDamage = vx_HitpointsDamageArray select 2;

	//diag_log format["Previous Damage ((%1))", _vxDamageEntry];
	//diag_log format["Current Damage ((%1))", vx_HitpointsDamage];

	//_damageDone: string to build the list of damaged hitpoints on
	// to then display to the user as a hint
	_damageDone = "";
	{
		//_damage: Saved damage value for the current hitpoint
		_damage = _vxDamageEntry select _forEachIndex;


		if (listAllHitpoints == 1) then {
			//Save the damage to the damage array to be compared next run
			_vxDamageEntry set [_forEachIndex, _x];
			
			//_name: name of the current hitpoint
			_name = vx_HitPointsNames select _forEachIndex;
			if !(["glass", _name] call BIS_fnc_inString) then {
				if !(["pylon", _name] call BIS_fnc_inString) then {
					//Append the information for the current hitpoint onto the damaged hitpoints string
					_damageDone = _damageDone + _name + ": " + str(_x) + " (" + ([_x, _damage] call formatHitpointDamage) + ")<br/>";
				}
			}
		} else {
			//If saved damage is not the current damage, there has been a change to display
			if (_x != _damage) then {
				//Save the damage to the damage array to be compared next run
				_vxDamageEntry set [_forEachIndex, _x];
				//_name: name of the current hitpoint
				_name = vx_HitPointsNames select _forEachIndex;
				//Append the information for the current hitpoint onto the damaged hitpoints string
				_damageDone = _damageDone + _name + ": " + str(_x) + " (" + ([_x, _damage] call formatHitpointDamage) + ")<br/>";
			};
		};

	} forEach vx_HitpointsDamage; //Loop through every hitpoint damage value

	//Get current Total damage of the vehicle
	_damage = damage _vx;
	//Display the damage analysis string:
	// Total Damage: 0-1
	// <hitpointname>: <hitpoint damage> (<damage change>)...
	hintParsed = parseText format["Total Damage: %2 (%3)%1<br/>%4%5",hintStart,_damage,(_damage-_vxTotalDamage),_damageDone,hintEnd];
	hint hintParsed;
	diag_log [(_damage-_vxTotalDamge),_damageDone];

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
		//_damageArray = [hitpoints, overallDamage]
		_damageArray = [_vx, _nameCount] call countHitPoints;		
		//vx_HitPointsNames: Array of all hitpoint names
		vx_HitPointsNames = (getAllHitPointsDamage _vx) select 0;

		vxDamageEntry = _damageArray select 0;
		vxTotalDamage = _damageArray select 1;

		vxDisplayHandler = (findDisplay 46) displayAddEventHandler ["KeyDown", {
			params["_display", "_keyCode", "_shft", "_ctr", "_alt" ];

			if (_keyCode == updateDamageKey) then {
				vxDamageArray = [_display getVariable "_vx", vxDamageEntry, vxTotalDamage, vx_HitPointsNames] call damageLog;
				vxDamageEntry = vxDamageArray select 0;
				vxTotalDamage = vxDamageArray select 1;
			} else {
				if (_keyCode == healTargetKey) then {
					(_display getVariable "_vx") setDamage 0;
				};
			};
		}];
	} else {
		(findDisplay 46) displayRemoveEventHandler ["KeyDown", vxDisplayHandler];
	};
};


if !(v1 isEqualTo objNull) then {
	v1AddAction = player addAction [format["<t color='#FF0000'>1. Toggle |%1| monitor</t>", v1Name], {
		if (v1Toggle == 0) then {v1Toggle = 1};
		[v1, v1Toggle, v1Name] call toggleLogger;
	}, nil, 15];
	v1Success = 1;
} else {diag_log("v1 not valid")};

if !(v2 isEqualTo objNull) then {
	v2AddAction = player addAction [format["<t color='#00FF00'>2. Toggle |%1| monitor</t>r", v2Name], {
		if (v2Toggle == 0) then {v2Toggle = 1};
		[v2, v2Toggle, v2Name] call toggleLogger;
	}, nil, 14];
	v2Success = 1;
} else {diag_log("v2 not valid")};

if !(v3 isEqualTo objNull) then {
	v3AddAction = player addAction [format["<t color='#0000FF'>3. Toggle |%1| monitor</t>", v3Name], {
		if (v3Toggle == 0) then {v3Toggle = 1};
		[v3, v3Toggle, v3Name] call toggleLogger;
	}, nil, 13];
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

	//Remove keydown event handlers
	(findDisplay 46) displayRemoveAllEventHandlers "KeyDown";

	//Remove diag_toggle eventhandler
	// if (gameIsDiag == true) then {(findDisplay 46)  displayRemoveEventHandler ["KeyDown", diagToggle]};
	//Remove unlimited ammo eventhandlers
	try {
		startVehicle removeEventHandler ["Fired", vehicleFired];
	} catch {
		diag_log(format["Error in <vehicleFired removeEventHandler>: %1", _exception]);
	};
	player removeEventHandler ["Fired", playerFired];
}];


newTargetEH = (findDisplay 46) displayAddEventHandler ["KeyDown", {
	params["_display", "_keyCode", "_shft", "_ctr", "_alt" ];

	if (_keyCode == designateV1Key) then
	{
		v1 = cursorObject;
		v1Name = getText (configFile >> "CfgVehicles" >> typeOf v1 >> "displayName");

		if !(v1AddAction isEqualTo objNull) then {
			player removeAction v1AddAction;
			if (v1Toggle == 1) then {[v1, 0, v1Name] call toggleLogger};
		};
		v1AddAction = player addAction ["<t color='#FF0000'>" + format["1. Toggle [%1] monitor", v1Name] + "</t>", {
			if (v1Toggle == 0) then {v1Toggle = 1};
			[v1, v1Toggle, v1Name] call toggleLogger;
		}, nil, 15];
		v1Success = 1;
	};
	if (_keyCode == designateV2Key) then
	{
		v2 = cursorObject;
		v2Name = getText (configFile >> "CfgVehicles" >> typeOf v2 >> "displayName");

		if !(v1AddAction isEqualTo objNull) then {
			player removeAction v2AddAction;
			if (v2Toggle == 1) then {[v2, 0, v2Name] call toggleLogger};
		};
		v2AddAction = player addAction [format["<t color='#00FF00'>2. Toggle [%1] monitor</t>", v2Name], {
			if (v2Toggle == 0) then {v2Toggle = 1};
			[v2, v2Toggle, v2Name] call toggleLogger;
		}, nil, 14];
		v2Success = 1;
	};
	if (_keyCode == designateV3Key) then
	{
		v3 = cursorObject;
		v3Name = getText (configFile >> "CfgVehicles" >> typeOf v3 >> "displayName");

		if !(v3AddAction isEqualTo objNull) then {
			player removeAction v3AddAction;
			if (v3Toggle == 1) then {[v3, 0, v3Name] call toggleLogger};
		};
		v3AddAction = player addAction [format["<t color='#0000FF'>3. Toggle [%1] monitor</t>", v3Name], {
			if (v3Toggle == 0) then {v3Toggle = 1};
			[v3, v3Toggle, v3Name] call toggleLogger;
		}, nil, 13];
		v3Success = 1;
	};
}];
