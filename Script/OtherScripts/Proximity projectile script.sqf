vehicle player addeventhandler ["Fired", {(_this select 0) setvehicleammo 1}];
bulletA = player addAction ["Enable Prox", {firedEH = vehicle player addEventHandler ["Fired", {

//	Modified from: @RHSUSAF/rhsusf_c_heavyweapons/functions/rhs_saclosGuide.sqf
//		SACLOS guidiance
//		rhs_fnc_saclosGuide
//
//		a: reyhard
//
//	Projectile proximity(to vehicles) detonation

// "_unit", "_weapon", "_muzzle", "_mode", "_ammo", "_magazine", "_projectile", "_gunner"
params["_u","_w","_m","","_a","","_p","_g"];

// exit if unit is local to headless client or dedicated server
if(!hasInterface)exitWith{hint "exit15";};

//exit if not a player
if( (call rhs_fnc_findPlayer) != _g )exitWith{hint "exit18";};

private _v = vehicle (call rhs_fnc_findPlayer);

private _cfgA = configFile >> "cfgAmmo" >> _a;
private _proximityMode = 1;
private _proximityRange = 5;
private _detonationRange = 5;
private _deleteParentWhenTriggered = getNumber (_cfgA >> "deleteParentWhenTriggered");

if(_proximityMode isEqualTo 1) then {
	private _pfhTop = "rhs_pfh_prox_" + str _p;

	//Delay to prevent triggering on near vehicles (maybe use as a fuze arming timer?)
	//[] spawn {uisleep 0.5;};

	private _vehList = [];
	private _vehPrepList = vehicles select {(_p distance _x < 10000) AND (_x isKindOf "AllVehicles") AND (_x distance _u >= 200)};
	{
		//Notes:
		//	bbR  = bounding box real
		//	bbRf = bbR first  (select 0)
		//	bbRs = bbR second (select 1)
		//	bbRw = bbR width
		//	bbRl = bbR length
		//	bbRh = bbR height

		private _bbR  = 0 boundingBoxReal _p;
		private _bbRf = _bbR select 0;
		private _bbRs = _bbR select 1;

		//Variables to hold values from array (more time efficient)
		private _bbrF_sel_zer = _bbRf select 0;
		private _bbrF_sel_one = _bbRf select 1;
		private _bbrF_sel_two = _bbRf select 2;
		private _bbrS_sel_zer = _bbRs select 0;
		private _bbrS_sel_one = _bbRs select 1;
		private _bbrS_sel_two = _bbRs select 2;

		//Middle areas:
		private _bbRw_mid = _bbrF_sel_zer + _bbrS_sel_zer;
		private _bbRl_mid = _bbrF_sel_one + _bbrS_sel_one;
		private _bbRh_mid = _bbrF_sel_two + _bbrS_sel_two;

		//Left side of vehicle
			//Bottom
		private _bbR_botlayer_left_f = [_bbrF_sel_zer,_bbrF_sel_one,_bbrF_sel_two];
		private _bbR_botlayer_left_m = [_bbrF_sel_zer,_bbRl_mid,    _bbrF_sel_two];
		private _bbR_botlayer_left_b = [_bbrF_sel_zer,_bbrS_sel_one,_bbrF_sel_two];
			//Middle
		private _bbR_midlayer_left_f = [_bbrF_sel_zer,_bbrF_sel_one,_bbRh_mid];
		private _bbR_midlayer_left_m = [_bbrF_sel_zer,_bbRl_mid,    _bbRh_mid];
		private _bbR_midlayer_left_b = [_bbrF_sel_zer,_bbrS_sel_one,_bbRh_mid];
			//Top
		private _bbR_toplayer_left_f = [_bbrF_sel_zer,_bbrF_sel_one,_bbrS_sel_two];
		private _bbR_toplayer_left_m = [_bbrF_sel_zer,_bbRl_mid,    _bbrS_sel_two];
		private _bbR_toplayer_left_b = [_bbrF_sel_zer,_bbrS_sel_one,_bbrS_sel_two];

		//Middle of vehicle
			//Bottom
		private _bbR_botlayer_mid_f = [_bbRw_mid,_bbrF_sel_one,_bbrF_sel_two];
		private _bbR_botlayer_mid_m = [_bbRw_mid,_bbRl_mid,    _bbrF_sel_two];
		private _bbR_botlayer_mid_b = [_bbRw_mid,_bbrS_sel_one,_bbrF_sel_two];
			//Middle
		private _bbR_midlayer_mid_f = [_bbRw_mid,_bbrF_sel_one,_bbRh_mid];
		//private _bbR_mid_m = [_bbRw_mid,_bbRl_mid,_bbRh_mid];
		private _bbR_midlayer_mid_b = [_bbRw_mid,_bbrS_sel_one,_bbRh_mid];
			//Top
		private _bbR_toplayer_mid_f = [_bbRw_mid,_bbrF_sel_one,_bbrS_sel_two];
		private _bbR_toplayer_mid_m = [_bbRw_mid,_bbRl_mid,    _bbrS_sel_two];
		private _bbR_toplayer_mid_b = [_bbRw_mid,_bbrS_sel_one,_bbrS_sel_two];

		//Right side of vehicle
			//Bottom
		private _bbR_botlayer_right_f = [_bbrS_sel_zer,_bbrF_sel_one,_bbrF_sel_two];
		private _bbR_botlayer_right_m = [_bbrS_sel_zer,_bbRl_mid,    _bbrF_sel_two];
		private _bbR_botlayer_right_b = [_bbrS_sel_zer,_bbrS_sel_one,_bbrF_sel_two];
			//Middle
		private _bbR_midlayer_right_f = [_bbrS_sel_zer,_bbrF_sel_one,_bbRh_mid];
		private _bbR_midlayer_right_m = [_bbrS_sel_zer,_bbRl_mid,   _bbRh_mid];
		private _bbR_midlayer_right_b = [_bbrS_sel_zer,_bbrS_sel_one,_bbRh_mid];
			//Top
		private _bbR_toplayer_right_f = [_bbrS_sel_zer,_bbrF_sel_one,_bbrS_sel_two];
		private _bbR_toplayer_right_m = [_bbrS_sel_zer,_bbRl_mid,    _bbrS_sel_two];
		private _bbR_toplayer_right_b = [_bbrS_sel_zer,_bbrS_sel_one,_bbrS_sel_two];

		_vehList pushBack [_x,	[_bbR_midlayer_left_f,_bbR_midlayer_mid_f,_bbR_midlayer_right_f,
								_bbR_midlayer_left_m,_bbR_midlayer_right_m,
								_bbR_midlayer_left_b,_bbR_midlayer_mid_b,_bbR_midlayer_right_b,

								_bbR_botlayer_left_f,_bbR_botlayer_mid_f,_bbR_botlayer_right_f,
								_bbR_botlayer_left_m,_bbR_botlayer_mid_m,_bbR_botlayer_right_m,
								_bbR_botlayer_left_b,_bbR_botlayer_mid_b,_bbR_botlayer_right_b,

								_bbR_toplayer_left_f,_bbR_toplayer_mid_f,_bbR_toplayer_right_f,
								_bbR_toplayer_left_m,_bbR_toplayer_mid_m,_bbR_toplayer_right_m,
								_bbR_toplayer_left_b,_bbR_toplayer_mid_b,_bbR_toplayer_right_b
								]];
	} forEach _vehPrepList;


	[_pfhTop, "onEachFrame", {
		params["_p","_vehList","_pfhTop","_proximityRange","_detonationRange","_deleteParentWhenTriggered"];

		private _tgtList = _vehList select {_p distance (_x select 0) < 100};
		{
			//diag_log("Started points");

			if ((_p distance ((_x select 0) modelToWorld (_x select 1 select 0)) <= _proximityRange * 2) OR (_p distance ((_x select 0) modelToWorld (_x select 1 select 7)) <= _proximityRange * 2)) then
			{
				private _veh = _x select 0;
				private _distances = [];
				{
					_distances pushBack (_p distance (_veh modelToWorld _x));
				} forEach (_x select 1);

				private _distanceToVeh = selectMin _distances;
				if (_distanceToVeh <= _proximityRange) then {

					//diag_log(format["before setpos _p position %1", position _p]);
					//_p setPos (_p modelToWorld [0,(_detonationRange - _distanceToVeh)-5,0]);
					//diag_log(format["Y: %1", (_detonationRange - _distanceToVeh)]);
					//diag_log(format["after setpos _p position %1", position _p]);
					triggerAmmo _p;

					//If the projectile will still exist when triggered,
					if (_deleteParentWhenTriggered isEqualTo 0) then {
						//We have deployed the submunition, so delete projectile
						// (or find a way to make it detonate as if hitting a surface)
						_whPos = getPos _p;
						_wh = createVehicle ["weaponHolder", _whPos, [], 0, "CAN_COLLIDE"];
						[_wh] spawn {
							params ["_wh"];
							uiSleep 1;
							deleteVehicle _wh;
						};
					};

					exit;
				};
			};
		} forEach _tgtList;

		if(!alive _p)exitWith{
			[_pfhTop, "onEachFrame"] call BIS_fnc_removeStackedEventHandler;
		};
	}, [_p,_vehList,_pfhTop,_proximityRange,_detonationRange,_deleteParentWhenTriggered]] call BIS_fnc_addStackedEventHandler;
};
}]}];
bulletB = player addAction ["Disable Prox", {vehicle player removeEventHandler["Fired", firedEH]}];
bulletC = player addAction ["Remove Prox Options", {player removeaction bulletA; player removeaction bulletB; player removeaction bulletC; _var = missionNameSpace getVariable ["firedEH",-1]; if (_var != -1) then {player removeEventHandler ["Fired", firedEH]} else {}}];