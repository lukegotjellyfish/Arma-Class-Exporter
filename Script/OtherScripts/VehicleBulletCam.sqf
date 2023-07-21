(vehicle player) addeventhandler ["Fired", {(_this select 0) setvehicleammo 1}];
bulletA = player addAction ["Enable Bullet Cam", {nBulletCam = (vehicle player) addEventHandler ["Fired", {
	_null = _this spawn {
		_missile = _this select 6;
		_cam = "camera" camCreate (position (vehicle player));
		_cam cameraEffect ["External", "Back"];
		
		velCache = [0,0,0];
		while {true} do {
			if ((velocity _missile) isNotEqualTo velCache) then {
				if (!(isNull _missile)) then {
					velCache = velocity _missile;
					_cam camSetTarget _missile;
					_cam camSetRelPos [0,-10,1.5];
					_cam camCommit 0;
					//diag_log format["Distance: %1 | Velocity: %2 | Pos: %3", (vehicle player) distance2D _missile, velocity _missile, getPos _missile];
					systemChat format["Distance: %1 | Speed: %2 | Pos: %3", (vehicle player) distance2D _missile, velocity _missile select 1, getPos _missile, isNull _missile];
				} else {
					break;
				}
			}
		};
		sleep 0.5;
		//Can't show hints while in a camera (big sad)
		_cam cameraEffect ["Terminate", "Back"];
		camDestroy _cam;
	};
}]}];
bulletB = player addAction ["Disable Bullet Cam", {player removeEventHandler["Fired", nBulletCam]}];
bulletC = player addAction ["Remove BulletCam Options", {player removeaction bulletA; player removeaction bulletB; player removeaction bulletC; _var = missionNameSpace getVariable ["nBulletCam",-1]; if (_var != -1) then {player removeEventHandler ["Fired", nBulletCam]} else {}}];