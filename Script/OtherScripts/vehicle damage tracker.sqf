//SCRIPT START
vehiclePlayer = (vehicle player);
_vehicleFired = vehiclePlayer addeventhandler ["Fired", {(_this select 0) setvehicleammo 1}];
_playerFired = player addeventhandler ["Fired", {(_this select 0) setvehicleammo 1}];
//Assign vehicles (vehicle variable name)
v1 = t72;
v2 = t80;
v3 = t90;
//Init toggle addaction values
v1_toggle = 0;
v2_toggle = 0;
v3_toggle = 0;
//Player's vehicle for each option
v1_vehicle = "T-72 Test";
v2_vehicle = "";
v3_vehicle = "";

//https://community.bistudio.com/wiki/DIK_KeyCodes
//16 = Q
//18 = E
//I couldn't be bothered to figure out a way to actually toggle this off and on without presing it twice so i just use a macro :p
//diag_toggle is a function of the dev branch, exclude this for stable/profiling/rc
diag_toggleToggle = (findDisplay 46) displayAddEventHandler ["KeyDown", "if ((_this select 1) == 16) then {diag_log('single diag_toggle'); diag_toggle 'shots';};"];


countHitpoints = {
	params ["_vx", "_hintTitle"];

	//diag_log(format["On countHitpoints: %1|%2", _vx, _hintTitle]);

	_dbg = "";
	_damageEntry = [];
	_size = 0;
	{
		_size = _size + 1; _damageEntry resize _size; _damageEntry set [_size -1, 0]
	} forEach (getAllHitPointsDamage _vx select 0);
	_dbg = _dbg + _hintTitle + str(_size);
	hint _dbg;

	_damageEntry;
};

damageLog = {
	params ["_vx", "_vxDamageEntry"];

	//diag_log(format["On damageLog: %1|%2", _vx, _vxDamageEntry]);

	vx_HitpointsDamageArray = getAllHitPointsDamage _vx;
	vx_HitPointsNames = vx_HitpointsDamageArray select 0;
	vx_HitpointsDamage = vx_HitpointsDamageArray select 2;

	_damageDone = "";
	_i = 0;
	{
		_damage = _vxDamageEntry select _i;
		if ((_x != 0) && (_x != _damage)) then {
			_vxDamageEntry set [_i, _x];
			_name = vx_HitPointsNames select _i;
			_damageDone = _damageDone + _name + ": " + str(_x) + " (+" + str(_x - _damage) + ")\n";
		};
		_i = _i + 1;
	} forEach vx_HitpointsDamage;
	hint _damageDone;
	vx_HitpointsDamage;
};

toggleLogger = {
	params ["_vx", "_vxToggle", "_vxName"];
	vx = _vx;  //Otherwise calling damageLog will be [any], there is almost definintely a better way of doing this but eeeeeeeh :p

	//diag_log(format["On toggleLogger: %1|%2|%3", _vx, _vxToggle, _vxName]);

	if !(alive _vx) then {
		if (_vxToggle == 0) then {
			try {
				(findDisplay 46) displayRemoveEventHandler ["KeyDown", vxDisplayHandler];
			}
			catch {
				diag_log(format["Error in <1(alive _vx -> removeEventHandler>: %1", _exception])
			};
		};
	}
	else
	{
		if (_vxToggle == 1) then {
			vxDamageEntry = [_vx, (_vxName + " Hitpoints: ")] call countHitPoints;
			//diag_log(format["Passing [%1,%2] to damageLog", _vx, vxDamageEntry]);
			vxDisplayHandler = (findDisplay 46) displayAddEventHandler ["KeyDown", "if ((_this select 1) == 18) then {vxDamageEntry = [vx, vxDamageEntry] call damageLog;};"];
		}
		else {(findDisplay 46) displayRemoveEventHandler ["KeyDown", vxDisplayHandler];};
	};
};


vehicle_1 = player addAction [format["Toggle %1 monitor", v1_vehicle], {
	if (v1_toggle == 0) then {v1_toggle = 1;}
	else {v1_toggle = 0;};
	[v1, v1_toggle, v1_vehicle] call toggleLogger;
}];
vehicle_2 = player addAction [format["Toggle %1 monitor", v2_vehicle], {
	[v2, v2_toggle, v2_vehicle] call toggleLogger;
}];
vehicle_3 = player addAction [format["Toggle %1 monitor", v3_vehicle], {
	[v3, v3_toggle, v3_vehicle] call toggleLogger;
}];

vehicle_remove = player addAction ["Remove and disable options", {
	//Remove vehicle toggle actions
	player removeaction vehicle_1;
	player removeaction vehicle_2;
	player removeaction vehicle_3;

	//Remove this action because where else would it be removed
	player removeaction vehicle_remove;

	//Remove diag_toggle eventhandler
	(findDisplay 46) displayRemoveEventHandler ["KeyDown", diag_toggleToggle];
	//Remove unlimited ammo eventhandlers
	vehiclePlayer removeEventHandler ["Fired", "_vehicleFired"];
	player removeEventHandler ["Fired", "_playerFired"];
}];