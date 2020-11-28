vehicle player addeventhandler ["Fired", {(_this select 0) setvehicleammo 1}];
bulletA = player addAction ["Enable Bullet Cam", {YEETUS = vehicle player addEventHandler ["Fired", {
	_null = _this spawn {
		_missile = _this select 6;
		_cam = "camera" camCreate (position player);
		_cam cameraEffect ["External", "Back"];
		while {!(isNull _missile)} do {
			_cam camSetTarget getPos _missile;
			//diag_log format["Distance: %1 | Velocity: %2 | Pos: %3", player distance2D _missile, velocity _missile, getPos _missile];
			systemChat format["Distance: %1 | Velocity: %2 | Pos: %3", player distance2D _missile, velocity _missile, getPos _missile];
			_missilePos = getPos _missile;
			_cam camSetRelPos [10,10,0];
			_cam camCommit 0;
		};
		sleep 3;
		//Can't show hints while in a camera (big sad)
		_cam cameraEffect ["Terminate", "Back"];
		camDestroy _cam;
	};
}]}];
bulletB = player addAction ["Disable Bullet Cam", {vehicle player removeEventHandler["Fired", YEETUS]}];
bulletC = player addAction ["Remove BulletCam Options", {player removeaction bulletA; player removeaction bulletB; player removeaction bulletC; _var = missionNameSpace getVariable ["YEETUS",-1]; if (_var != -1) then {player removeEventHandler ["Fired", YEETUS]} else {}}];
//bullet cam