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

	//Delay to prevent triggering on self (maybe use as a fuze arming timer?)
	[] spawn {uisleep 0.1;};

	private _vehList = vehicles select {_p distance _x < 10000 AND (_x isKindOf "AllVehicles") AND (_x != _u)};

	[_pfhTop, "onEachFrame", {
		params["_p","_vehList","_pfhTop","_proximityRange","_deleteParentWhenTriggered"];

		//Simplify list for probable targets (might need to scale for speed and range)
		private _tgtList = _vehList select {_p distance _x < (_proximityRange * 15)};
		{
			//If projectile is in prox range
			//Will replace with boundingbox method
			if (_p distance _x <= _proximityRange) exitWith {
				triggerAmmo _p;  //Activate

				//If the projectile will still exist when triggered,
				if (_deleteParentWhenTriggered isEqualTo 0) then {
					//We have deployed the submunition, so delete projectile
					// (or find a way to make it detonate as if hitting a surface)
					[_p] spawn {params ["_p"]; sleep 0.1; deleteVehicle _p;};
				}
			};
		} forEach _tgtList;

		if(!alive _p)exitWith{
			[_pfhTop, "onEachFrame"] call BIS_fnc_removeStackedEventHandler;
		};
	}, [_p,_vehList,_pfhTop,_proximityRange,_deleteParentWhenTriggered]] call BIS_fnc_addStackedEventHandler;
};
}]}];
bulletB = player addAction ["Disable Prox", {vehicle player removeEventHandler["Fired", firedEH]}];
bulletC = player addAction ["Remove Prox Options", {player removeaction bulletA; player removeaction bulletB; player removeaction bulletC; _var = missionNameSpace getVariable ["firedEH",-1]; if (_var != -1) then {player removeEventHandler ["Fired", firedEH]} else {}}];