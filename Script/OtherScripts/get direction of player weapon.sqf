missileVelLast = [0,0,0];

bulletA = player addAction ["Enable Weapon Tracker", {YEETUS = player addEventHandler ["Fired", {
	_null = _this spawn {
		_missile = _this select 6;
		while {!(isNull _missile)} do {
			_velMissile = velocity _missile;
			if (_velMissile select 1 != missileVelLast select 1) then {
				hint str _velMissile;
				diag_log str _velMissile;
				missileVelLast = _velMissile;
				//_array = player weaponDirection currentWeapon player;
				//diag_log(format["X: %1 | Y: %2", _array select 0, _array select 1]);
			};
		};
	};
}]}];
bulletB = player addAction ["Disable Weapon Tracker", {player removeEventHandler["Fired", YEETUS]}];
bulletC = player addAction ["Remove Weapon Tracker Options", {
		player removeaction bulletA; player removeaction bulletB;
		player removeaction bulletC;
		_var = missionNameSpace getVariable ["YEETUS",-1];
		if (_var != -1) then {
			player removeEventHandler ["Fired", YEETUS]
		} else {}
	}
];
