//SCRIPT START
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

//16 = Q
//Enable/disable diag_toggle shots
diag_toggleToggle = (findDisplay 46) displayAddEventHandler ["KeyDown", "if ((_this select 1) == 16) then {diag_log('single diag_toggle'); diag_toggle 'shots';};"];

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

vehicle_3 = player addAction ["Toggle T-90 monitor", {
	if (v3_toggle == 0) then {
		_dbg = "";
		v3_DamageEntry = [];
		_size = 0;
		{
			_size = _size + 1; v3_DamageEntry resize _size; v3_DamageEntry set [_size -1, 0]
		} forEach (getAllHitPointsDamage v3 select 0);
		_dbg = _dbg + "T-90 Hitpoints: " + str(_size);
		hint _dbg;
		v3_toggle = 1;

		//https://community.bistudio.com/wiki/DIK_KeyCodes
		//18 = E
		v3_displayHandler = (findDisplay 46) displayAddEventHandler ["KeyDown", "if ((_this select 1) == 18) then {v3_DamageEntry = [v3, v3_DamageEntry] call damageLog;};"];
	}
	else {v3_toggle = 0; (findDisplay 46) displayRemoveEventHandler ["KeyDown", v3_displayHandler];};
}];


vehicle_remove = player addAction ["Remove and disable options", {
	// player removeaction vehicle_1;
	// player removeaction vehicle_2;
	player removeaction vehicle_3;
	// player removeaction vehicle_4;
	player removeaction vehicle_remove;

	// _var = missionNameSpace getVariable ["t72b_fire",-1];
	// if (_var != -1) then { player removeEventHandler ["Fired", t72b_fire]; } else {};

	// _var = missionNameSpace getVariable ["t80uk_fire",-1];
	// if (_var != -1) then { player removeEventHandler ["Fired", t80uk_fire]; } else {};

	_var = missionNameSpace getVariable ["v3_displayHandler",-1];
	if (_var != -1) then { (findDisplay 46) displayRemoveEventHandler ["KeyDown", v3_displayHandler]; } else {};

	//Remove diag_toggle "shots" eventHandlers
	(findDisplay 46) displayRemoveEventHandler ["KeyDown", diag_toggleToggle];
	// _var = missionNameSpace getVariable ["t14_fire",-1];
	// if (_var != -1) then { player removeEventHandler ["Fired", t14_fire]; } else {};
}];




//Testing GUIs, want an SQF on-screen display that doesn't block inputAction
// disableSerialization;
// private _display = findDisplay 46 createDialog "RscDisplayChat";
// private _ctrlGroup = _display ctrlCreate ["RscControlsGroupNoScrollbars", -1];
// private _ctrlBackground = _display ctrlCreate ["RscTextMulti", -1, _ctrlGroup];
// _ctrlGroup ctrlCommit 0;
// _ctrlBackground ctrlSetPosition [0, 0, 0.5, 1.5];
// _ctrlBackground ctrlSetBackgroundColor [0.5, 0.5, 0.5, 0.9];
// _ctrlBackground ctrlSetText "Tank:";
// _ctrlBackground ctrlEnable false;
// _ctrlBackground ctrlCommit 0;
// _ctrlGroup ctrlSetPosition [-0.686, -0.2, 0.5, 1.5];
// _ctrlGroup ctrlCommit 0.1;