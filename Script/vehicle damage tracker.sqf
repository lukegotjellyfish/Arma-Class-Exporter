//SCRIPT START
//Assign vehicles
v1 = t72b;
v2 = t80uk;
v3 = t90sm;
v4 = t14;
//Init toggle addaction values
v1_toggle = 0;  //T-72B
v2_toggle = 0;  //T-80UK
v3_toggle = 0;  //T-90SM
v4_toggle = 0;  //T-14
//Player's vehicle for each option
v1_vehicle = "";
v2_vehicle = "";
v3_vehicle = "";
v4_vehicle = "";
//HitPoint damage array for each vehicle
_dbg = "";


v3_DamageEntry = [];
_size = 0;
{_size = _size + 1; v3_DamageEntry resize _size; v3_DamageEntry set [_size -1, 0]} forEach (getAllHitPointsDamage v3 select 0);
_dbg = _dbg + "T-90SM Hitpoints: " + str(_size);

hint _dbg;

vehicle_3 = player addAction ["Toggle T-90SM monitor", {
	if (v3_toggle == 0) then {
		v3_toggle = 1;
		v3_vehicle = vehicle player;
		v3_fire = v3_vehicle addEventHandler ["Fired", {
			v3_HitpointsDamageArray = getAllHitPointsDamage v3;
			v3_HitPointsNames = v3_HitpointsDamageArray select 0;
			v3_HitpointsDamage = v3_HitpointsDamageArray select 2;

			_damageDone = "";
			_i = 0;
			{
				_damage = v3_DamageEntry select _i;
				if (_x != 0 && _x != _damage) then {
						v3_DamageEntry set [_i, _x];
						_name = v3_HitPointsNames select _i;
						_damageDone = _damageDone + _name + ": " + str(_x) + " (+" + str(_x - _damage) + ")\n";
					};
				_i = _i + 1;
			} forEach v3_HitpointsDamage;
			hint _damageDone;
			v3_DamageEntry = v3_HitpointsDamage;
		}];
	}
	else {v3_toggle = 0;v3_vehicle removeEventHandler ["Fired", v3_fire];};
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

	_var = missionNameSpace getVariable ["v3_fire",-1];
	if (_var != -1) then { player removeEventHandler ["Fired", v3_fire]; } else {};

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