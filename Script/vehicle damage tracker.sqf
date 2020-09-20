//To suppress errors in VSCode, do not include
t72b = "";
t80uk = "";
t90sm = "";
t14 = "";
//

//SCRIPT START

disableSerialization;
private _display = findDisplay 46 createDisplay "RscDisplayEmpty";
private _ctrlGroup = _display ctrlCreate ["RscControlsGroupNoScrollbars", -1];
private _ctrlBackground = _display ctrlCreate ["RscTextMulti", -1, _ctrlGroup];
_ctrlGroup ctrlCommit 0;
_ctrlBackground ctrlSetPosition [0, 0, 0.5, 1.5];
_ctrlBackground ctrlSetBackgroundColor [0.5, 0.5, 0.5, 0.9];
_ctrlBackground ctrlSetText "ENTER TEXT:";
//_ctrlBackground ctrlEnable false;
_ctrlBackground ctrlCommit 0;
_ctrlGroup ctrlSetPosition [-0.65, -0.2, 0.5, 1.5];
_ctrlGroup ctrlCommit 0.1;

















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
v1_DamageEntry = [];
_size = 0;
{_size = _size + 1;} forEach getAllHitPointsDamage v1;
v1_DamageEntry resize _size;

v2_DamageEntry = [];
_size = 0;
{_size = _size + 1;} forEach getAllHitPointsDamage v2;
v2_DamageEntry resize _size;

v3_DamageEntry = [];
_size = 0;
{_size = _size + 1;} forEach getAllHitPointsDamage v3;
v3_DamageEntry resize _size;

v4_DamageEntry = [];
_size = 0;
{_size = _size + 1;} forEach getAllHitPointsDamage v4;
v4_DamageEntry resize _size;


vehicle_3 = player addAction ["Toggle T-90SM monitor", {
	if (v3_toggle == 0) then {
		v3_toggle = 1;
		v3_vehicle = vehicle player;
		t90sm_fire = v3_vehicle addEventHandler ["Fired", {
			t90smHitpointsDamageArray = getAllHitPointsDamage t90sm;
			t90smHitPointsNames = t90smHitpointsDamageArray select 0;
			t90smHitpointsDamage = t90smHitpointsDamageArray select 2;


			_damageDone = "";
			_i = 0;
			{
				if (_x != 0 && _x != v3_DamageEntry select _i) then {
						v3_DamageEntry set [_i - 1, _x];
						_name = t90smHitPointsNames select _i;
						_damageDone = _damageDone + _name + ": " + str(_x) + "\n";
					};
				_i = _i + 1;
			} forEach t90smHitpointsDamage;
			hint _damageDone;
			v3_DamageEntry = t90smHitpointsDamage;
		}];
	}
	else {v3_toggle = 0;v3_vehicle removeEventHandler ["Fired", t90sm_fire];};
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

	_var = missionNameSpace getVariable ["t90sm_fire",-1];
	if (_var != -1) then { player removeEventHandler ["Fired", t90sm_fire]; } else {};

	// _var = missionNameSpace getVariable ["t14_fire",-1];
	// if (_var != -1) then { player removeEventHandler ["Fired", t14_fire]; } else {};
}];