vehicle player addeventhandler ["Fired", {(_this select 0) setvehicleammo 1}];
bulletA = player addAction ["Enable Prox", {firedEH = vehicle player addEventHandler ["Fired", {
/*
	Modified from:
		SACLOS guidiance
		rhs_fnc_saclosGuide

		a: reyhard

	Projectile proximity(to vehicles) detonation
*/
params["_u","_w","_m","","_a","","_p","_g"];

// exit if unit is local to headless client or dedicated server
if(!hasInterface)exitWith{hint "exit15";};

//exit if not a player
if( (call rhs_fnc_findPlayer) != _g )exitWith{hint "exit18";};

private _v = vehicle (call rhs_fnc_findPlayer);

private _cfgA = configFile >> "cfgAmmo" >> _a;
private _proximityMode = 1;//getNumber (_cfgA >> "rhs_proximityFuse");
private _proximityRange = 15;//getNumber (_cfgA >> "rhs_proximityRange");
private _deleteParentWhenTriggered = getNumber (_cfgA >> "deleteParentWhenTriggered");

if(_proximityMode isEqualTo 1) then {
	private _pfhTop = "rhs_pfh_prox_" + str _p;

	//Delay to prevent triggering on near vehicles (maybe use as a fuze arming timer?)
	[] spawn {uisleep 0.5;};

	private _vehList = [];
	private _vehPrepList = vehicles select {(_p distance _x < 10000) AND (_x isKindOf "AllVehicles") AND (_x distance _u >= 200)};
	{
		private _bbR = 0 boundingBoxReal _p;
		private _bbRf = _bbR select 0;
		private _bbRs = _bbR select 1;

		//Middle areas:
		private _bbRw_mid = (_bbRf select 0) + (_bbRs select 0);
		private _bbRl_mid = (_bbRf select 1) + (_bbRs select 1);
		private _bbRh_mid = (_bbRf select 2) + (_bbRs select 2);

		//Left side of vehicle
		  //Bottom
		private _bbR_botlayer_left_f = [(_bbRf select 0),(_bbRf select 1),(_bbRf select 2)];
		private _bbR_botlayer_left_m = [(_bbRf select 0),_bbRl_mid,       (_bbRf select 2)];
		private _bbR_botlayer_left_b = [(_bbRf select 0),(_bbRs select 1),(_bbRf select 2)];
		  //Middle
		private _bbR_midlayer_left_f = [(_bbRf select 0),(_bbRf select 1),_bbRh_mid];
		private _bbR_midlayer_left_m = [(_bbRf select 0),_bbRl_mid,       _bbRh_mid];
		private _bbR_midlayer_left_b = [(_bbRf select 0),(_bbRs select 1),_bbRh_mid];
		  //Top
		private _bbR_toplayer_left_f = [(_bbRf select 0),(_bbRf select 1),(_bbRs select 2)];
		private _bbR_toplayer_left_m = [(_bbRf select 0),_bbRl_mid,       (_bbRs select 2)];
		private _bbR_toplayer_left_b = [(_bbRf select 0),(_bbRs select 1),(_bbRs select 2)];

		//Middle of vehicle
		  //Bottom
		private _bbR_botlayer_mid_f = [_bbRw_mid,(_bbRf select 1),(_bbRf select 2)];
		private _bbR_botlayer_mid_m = [_bbRw_mid,_bbRl_mid,       (_bbRf select 2)];
		private _bbR_botlayer_mid_b = [_bbRw_mid,(_bbRs select 1),(_bbRf select 2)];
		  //Middle
		private _bbR_midlayer_mid_f = [_bbRw_mid,(_bbRf select 1),_bbRh_mid];
		//private _bbR_mid_m = [_bbRw_mid,_bbRl_mid,       _bbRh_mid];
		private _bbR_midlayer_mid_b = [_bbRw_mid,(_bbRs select 1),_bbRh_mid];
		  //Top
		private _bbR_toplayer_mid_f = [_bbRw_mid,(_bbRf select 1),(_bbRs select 2)];
		private _bbR_toplayer_mid_m = [_bbRw_mid,_bbRl_mid,       (_bbRs select 2)];
		private _bbR_toplayer_mid_b = [_bbRw_mid,(_bbRs select 1),(_bbRs select 2)];

		//Right side of vehicle
		  //Bottom
		private _bbR_botlayer_right_f = [(_bbRs select 0),(_bbRf select 1),(_bbRf select 2)];
		private _bbR_botlayer_right_m = [(_bbRs select 0),_bbRl_mid,       (_bbRf select 2)];
		private _bbR_botlayer_right_b = [(_bbRs select 0),(_bbRs select 1),(_bbRf select 2)];
		  //Middle
		private _bbR_midlayer_right_f = [(_bbRs select 0),(_bbRf select 1),_bbRh_mid];
		private _bbR_midlayer_right_m = [(_bbRs select 0),_bbRl_mid,       _bbRh_mid];
		private _bbR_midlayer_right_b = [(_bbRs select 0),(_bbRs select 1),_bbRh_mid];
		  //Top
		private _bbR_toplayer_right_f = [(_bbRs select 0),(_bbRf select 1),(_bbRs select 2)];
		private _bbR_toplayer_right_m = [(_bbRs select 0),_bbRl_mid,       (_bbRs select 2)];
		private _bbR_toplayer_right_b = [(_bbRs select 0),(_bbRs select 1),(_bbRs select 2)];

		// Middle of height layer
		// private _frontLeft   = _x modelToWorld _bbR_left_f;
		// private _frontMiddle = _x modelToWorld _bbR_mid_f;
		// private _frontRight  = _x modelToWorld _bbR_right_f;
		// private _leftMiddle  = _x modelToWorld _bbR_left_m;
		// private _rightMiddle = _x modelToWorld _bbR_right_m;
		// private _backLeft    = _x modelToWorld _bbR_left_b;
		// private _backMiddle  = _x modelToWorld _bbR_mid_b;
		// private _backRight   = _x modelToWorld _bbR_right_b;

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
		params["_p","_vehList","_pfhTop","_proximityRange","_deleteParentWhenTriggered"];

		private _tgtList = _vehList select {_p distance (_x select 0) < 100};
		{
			//diag_log("Started points");

			//Use length+width here for detection? test efficiency with all scenarios
			if ((_p distance ((_x select 0) modelToWorld (_x select 1 select 0)) <= _proximityRange * 2) AND (_p distance ((_x select 0) modelToWorld (_x select 1 select 7)) <= _proximityRange * 2)) then
			{
				private _veh = _x select 0;
				{
					diag_log(format["Distance to this point: %1",_p distance (_veh modelToWorld _x)]);
					private _projectileToTarget = _p distance (_veh modelToWorld _x);
					if (_projectileToTarget <= _proximityRange) then {
						triggerAmmo _p;
						diag_log("detonated");

						//If the projectile will still exist when triggered,
						if (_deleteParentWhenTriggered isEqualTo 0) then {
							//We have deployed the submunition, so delete projectile
							// (or find a way to make it detonate as if hitting a surface)
							[_p] spawn {params ["_p"]; uiSleep 0.1; deleteVehicle _p;}; //"HelicopterExploSmall" createVehicle (getpos _p);
						};
						break; //Arma 2.02 Added break for loops
					};
				} forEach (_x select 1);
			};

			//diag_log("Finished points");


			// //If projectile is in prox range
			// //Will replace with boundingbox method
			// if (_p distance _x <= _proximityRange) exitWith {
			// 	triggerAmmo _p;

			// 	//If the projectile will still exist when triggered,
			// 	if (_deleteParentWhenTriggered isEqualTo 0) then {
			// 		//We have deployed the submunition, so delete projectile
			// 		// (or find a way to make it detonate as if hitting a surface)
			// 		[_p] spawn {params ["_p"]; uiSleep 0.1; deleteVehicle _p;}; //"HelicopterExploSmall" createVehicle (getpos _p); 
			// 	};
			// };
		} forEach _tgtList;

		if(!alive _p)exitWith{
			[_pfhTop, "onEachFrame"] call BIS_fnc_removeStackedEventHandler;
		};
	}, [_p,_vehList,_pfhTop,_proximityRange,_deleteParentWhenTriggered]] call BIS_fnc_addStackedEventHandler;
};
}]}];
bulletB = player addAction ["Disable Prox", {vehicle player removeEventHandler["Fired", firedEH]}];
bulletC = player addAction ["Remove Prox Options", {player removeaction bulletA; player removeaction bulletB; player removeaction bulletC; _var = missionNameSpace getVariable ["firedEH",-1]; if (_var != -1) then {player removeEventHandler ["Fired", firedEH]} else {}}];