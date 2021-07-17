player addeventhandler ["Fired", {(_this select 0) setvehicleammo 1}];
player allowDamage false;
player setUnitRecoilCoefficient 0;
bulletA = player addAction ["Enable Bullet Cam", {YEETUS = vehicle player addEventHandler ["Fired", {
    diag_log(position player);
    missile = _this select 6;
    velCache = [0,0,0];
	startTime = time;
    _null = _this spawn {
        while {!(isNull missile)} do {
            vel = velocity missile;
            if (vel select 0 != velCache select 0) then {
                hint(format["Distance: %1\nVelocity: %2\nTime: %3", player distance2D missile, velocity missile, time-startTime]);
                velCache = vel;
            };
        };
    };
}]}];
bulletB = player addAction ["Disable Bullet Cam", {player removeEventHandler["Fired", YEETUS]}];
bulletC = player addAction ["Remove BulletCam Options", {player removeaction bulletA; player removeaction bulletB; player removeaction bulletC; _var = missionNameSpace getVariable ["YEETUS",-1]; if (_var != -1) then {player removeEventHandler ["Fired", YEETUS]} else {}}];
//bullet cam