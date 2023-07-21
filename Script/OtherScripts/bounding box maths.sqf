private _bbR = 0 boundingBoxReal vehicle player;
private _bbRf = _bbR select 0;
private _bbRs = _bbR select 1;

//Middle areas:
private _bbRw_mid = (_bbRf select 0) + (_bbRs select 0);
private _bbRl_mid = (_bbRf select 1) + (_bbRs select 1);
private _bbRh_mid = (_bbRf select 2) + (_bbRs select 2);

//Left side of vehicle
private _bbR_left_f = [(_bbRf select 0),(_bbRf select 1),_bbRh_mid];
private _bbR_left_m = [(_bbRf select 0),_bbRl_mid,       _bbRh_mid];
private _bbR_left_b = [(_bbRf select 0),(_bbRs select 1),_bbRh_mid];

//Middle of vehicle
private _bbR_mid_f = [_bbRw_mid,(_bbRf select 1),_bbRh_mid];
//private _bbR_mid_m = [_bbRw_mid,_bbRl_mid,       _bbRh_mid];
private _bbR_mid_b = [_bbRw_mid,(_bbRs select 1),_bbRh_mid];

//Right side of vehicle
private _bbR_right_f = [(_bbRs select 0),(_bbRf select 1),_bbRh_mid];
private _bbR_right_m = [(_bbRs select 0),_bbRl_mid,       _bbRh_mid];
private _bbR_right_b = [(_bbRs select 0),(_bbRs select 1),_bbRh_mid];


private _frontLeft   = v2 modelToWorld _bbR_left_f;
private _frontMiddle = v2 modelToWorld _bbR_mid_f;
private _frontRight  = v2 modelToWorld _bbR_right_f;
private _leftMiddle  = v2 modelToWorld _bbR_left_m;
private _rightMiddle = v2 modelToWorld _bbR_right_m;
private _backLeft    = v2 modelToWorld _bbR_left_b;
private _backMiddle  = v2 modelToWorld _bbR_mid_b;
private _backRight   = v2 modelToWorld _bbR_right_b;


hint(format["FrontLeft: %1\nFrontMiddle: %2\nFrontRight: %3\nLeftMiddle: %4\nRightMiddle: %5\nBackLeft: %6\nBackMiddle: %7\nBackRight: %8",
			_frontLeft,_frontMiddle,_frontRight,_leftMiddle,_rightMiddle,_backLeft,_backMiddle,_backRight])

//_nearestCorner = [car, player] call BIS_fnc_boundingBoxCorner;

//hint(format["Left side: [%1,%2,%3]\nMiddle: [%4,%5,%6]\nRight: [%7,%8,%9]",_bbR_left_f,_bbR_left_m,_bbR_left_b,
//																		     _bbR_mid_f,_bbR_mid_m,_bbR_mid_b,
//																		     _bbR_right_f,_bbR_right_m,_bbR_right_b]);