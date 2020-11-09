//SCRIPT START
vehicle player addeventhandler ["Fired", {(_this select 0) setvehicleammo 1}];
//Assign vehicles
v1 = t72;
v2 = t80;
v3 = t90;
//Init toggle addaction values
v1_toggle = 0;
v2_toggle = 0;
v3_toggle = 0;
//Player's vehicle for each option
v1_vehicle = "";
v2_vehicle = "";
v3_vehicle = "";

//https://community.bistudio.com/wiki/DIK_KeyCodes
//16 = Q
//18 = E
diag_toggleToggle = (findDisplay 46) displayAddEventHandler ["KeyDown", "if ((_this select 1) == 16) then {diag_log('single diag_toggle'); diag_toggle 'shots';};"];

countHitpoints = {
	params ["vx", "_hintTitle"];

	_dbg = "";
	_damageEntry = [];
	_size = 0;
	{
		_size = _size + 1; _damageEntry resize _size; _damageEntry set [_size -1, 0]
	} forEach (getAllHitPointsDamage vx select 0);
	_dbg = _dbg + _hintTitle + str(_size);
	hint _dbg;

	_damageEntry;
};

damageLog = {
	params ["_vx", "_vxDamageEntry"];

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


vehicle_1 = player addAction ["Toggle T-72 monitor", {
	if (v1_toggle == 0) then {
		v1_damageEntry = [v1, "T-72 Hitpoints: "] call countHitPoints;
		v1_toggle = 1;
		v1_displayHandler = (findDisplay 46) displayAddEventHandler ["KeyDown", "if ((_this select 1) == 18) then {v1_DamageEntry = [v1, v1_DamageEntry] call damageLog;};"];
	}
	else {v1_toggle = 0; (findDisplay 46) displayRemoveEventHandler ["KeyDown", v1_displayHandler];};
}];
vehicle_2 = player addAction ["Toggle T-80 monitor", {
	if (v2_toggle == 0) then {
		v3_damageEntry = [v2, "T-80 Hitpoints: "] call countHitPoints;
		v2_toggle = 1;
		v2_displayHandler = (findDisplay 46) displayAddEventHandler ["KeyDown", "if ((_this select 1) == 18) then {v2_DamageEntry = [v2, v2_DamageEntry] call damageLog;};"];
	}
	else {v2_toggle = 0; (findDisplay 46) displayRemoveEventHandler ["KeyDown", v2_displayHandler];};
}];
vehicle_3 = player addAction ["Toggle T-90 monitor", {
	if (v3_toggle == 0) then {
		v3_toggle = 1;
		v3_damageEntry = [v3, "T-90 Hitpoints: "] call countHitPoints;
		v3_displayHandler = (findDisplay 46) displayAddEventHandler ["KeyDown", "if ((_this select 1) == 18) then {v3_DamageEntry = [v3, v3_DamageEntry] call damageLog;};"];
	}
	else {v3_toggle = 0; (findDisplay 46) displayRemoveEventHandler ["KeyDown", v3_displayHandler];};
}];


vehicle_remove = player addAction ["Remove and disable options", {
	player removeaction vehicle_1;
	player removeaction vehicle_2;
	player removeaction vehicle_3;

	player removeaction vehicle_remove;

	_var = missionNameSpace getVariable ["v1_displayHandler",-1];
	if (_var != -1) then { (findDisplay 46) displayRemoveEventHandler ["KeyDown", v1_displayHandler]; } else {};

	_var = missionNameSpace getVariable ["v2_displayHandler",-1];
	if (_var != -1) then { (findDisplay 46) displayRemoveEventHandler ["KeyDown", v2_displayHandler]; } else {};

	_var = missionNameSpace getVariable ["v3_displayHandler",-1];
	if (_var != -1) then { (findDisplay 46) displayRemoveEventHandler ["KeyDown", v3_displayHandler]; } else {};

	(findDisplay 46) displayRemoveEventHandler ["KeyDown", diag_toggleToggle];
}];