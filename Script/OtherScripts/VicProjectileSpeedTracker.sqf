(vehicle player) addeventhandler ["Fired", {(_this select 0) setvehicleammo 1}];
(vehicle player) allowDamage false;
bulletA = player addAction ["Enable Bullet Cam", {YEETUS = (vehicle player) addEventHandler ["Fired", {
    diag_log(position (vehicle player));
    missile = _this select 6;
    velCache = [0,0,0];
    _null = _this spawn {
		_startTime = time;
        while {!(isNull missile)} do {
            vel = velocity missile;
            if (vel select 0 != velCache select 0) then {
				_timePassed = time - _startTime;
                hint(format["Distance: %1\nTime: %2\nSpeed (M/s): %3", (vehicle player) distance2D missile, _timePassed, (speed missile)/3.6]);
                velCache = vel;
            };
        };
    };
}]}];
bulletB = player addAction ["Disable Bullet Cam", {player removeEventHandler["Fired", YEETUS]}];
bulletC = player addAction ["Remove BulletCam Options", {player removeaction bulletA; player removeaction bulletB; player removeaction bulletC; _var = missionNameSpace getVariable ["YEETUS",-1]; if (_var != -1) then {player removeEventHandler ["Fired", YEETUS]} else {}}];

