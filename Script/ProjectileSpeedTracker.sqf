player addeventhandler ["Fired", {(_this select 0) setvehicleammo 1}];
player allowDamage false;
player setUnitRecoilCoefficient 0;
enableCamShake false;
allowFire = true;
bulletA = player addAction ["Enable Bullet Cam", {YEETUS = player addEventHandler ["Fired", {
 _null = _this spawn {
  _timestart = time;
  _missile = _this select 6;
  _cam = "camera" camCreate (position player);
  _cam cameraEffect ["External", "Back"];
  while {!(isNull _missile)} do {
   //diag_log(format ["%1|%2", speed _missile, time - _timestart]);
   _cam camSetTarget getPos _missile;
   camdistance = player distance2D _cam;
   timeend = time;
   camposition = getPos _missile;
   hint str speed _missile;
   _cam camSetRelPos [0,-20,10];
   _cam camCommit 0;
  };
  sleep 2;
  //Can't show hints while in a camera (big sad)
  hintSilent format ["Distance: %1\nTime: %2\nLanded: %3", camdistance, timeend - _timestart, camposition];
  _cam cameraEffect ["Terminate", "Back"];
  camDestroy _cam;
 };
}]}];
bulletB = player addAction ["Disable Bullet Cam", {player removeEventHandler["Fired", YEETUS]}];
bulletC = player addAction ["Remove BulletCam Options", {player removeaction bulletA; player removeaction bulletB; player removeaction bulletC; _var = missionNameSpace getVariable ["YEETUS",-1]; if (_var != -1) then {player removeEventHandler ["Fired", YEETUS]} else {}}];
//bullet cam