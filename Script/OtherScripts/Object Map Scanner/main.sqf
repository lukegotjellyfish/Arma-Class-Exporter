getTopDownProjection = {
	// Description:
	// Get an array of coordinates for the visual bounding box of object in 2D from a top-down perspective

	// Parameter(s):
	// _object = object to perform the operation on
	// _returnHeight = bool to determine whether to return min&max Z height as an additional array
	// _3D = bool to determine whether to return the Z height to return 3D coordinates

	// Example:
	// factory call getTopDownProjection;
	// [factory, true/1/false/0] getTopDownProjection;
	// [factory, true/1/false/0, true/1/false/0] getTopDownProjection;

	params ["_object", ["_returnHeight", false], ["_3d", false]];

	// bbr = boundingBoxReal
	// bbrA = boundingBoxReal First coordinate
	// bbrB = boundingBoxReal Second coordinate
	// _x = X
	// _y = Y
	// _z = Z

	//Get boundingBoxReal and save each coordinate to _bbrf and _bbrs
	private _bbr  = (0 boundingBoxReal _object) params ["_bbrf", "_bbrs"];
	//Variables to hold values from array (more time efficient)
	_bbrf params ["_bbrA_x","_bbrA_y","_bbrA_z"];
	_bbrs params ["_bbrB_x","_bbrB_y","_bbrB_z"];


	//Stats
	private _maxWidth = abs (_bbrB_x - _bbrA_x);
	private _maxLength = abs (_bbrB_y - _bbrA_y);
	private _maxHeight = abs (_bbrB_z - _bbrA_z);

	//Middle areas:
	private _bbrw_mid = _bbrA_x + _bbrB_x;
	private _bbrl_mid = _bbrA_y + _bbrB_y;
	private _bbrh_mid = _bbrA_z + _bbrB_z;

	//Left side of vehicle
	private _bbr_botlayer_left_AAA = [_bbrA_x,_bbrA_y,_bbrA_z];
	private _bbr_botlayer_left_ABA = [_bbrA_x,_bbrB_y,_bbrA_z];
	private _bbr_toplayer_left_AAB = [_bbrA_x,_bbrA_y,_bbrB_z];
	private _bbr_toplayer_left_ABB = [_bbrA_x,_bbrB_y,_bbrB_z];
	//Right side of vehicle
	private _bbr_botlayer_right_BAA = [_bbrB_x,_bbrA_y,_bbrA_z];
	private _bbr_botlayer_right_BBA = [_bbrB_x,_bbrB_y,_bbrA_z];
	private _bbr_botlayer_right_BAB = [_bbrB_x,_bbrA_y,_bbrB_z];
	private _bbr_botlayer_right_BBB = [_bbrB_x,_bbrB_y,_bbrB_z];

	private _bbr_botlayer_left_AAA_mtww = _object modelToWorldWorld _bbr_botlayer_left_AAA;
	private _bbr_botlayer_right_BAA_mtww = _object modelToWorldWorld _bbr_botlayer_right_BAA;
	private _bbr_botlayer_left_ABA_mtww = _object modelToWorldWorld _bbr_botlayer_left_ABA;
	private _bbr_botlayer_right_BBA_mtww = _object modelToWorldWorld _bbr_botlayer_right_BBA;

	private _bbr_toplayer_left_AAB_mtww = _object modelToWorldWorld _bbr_toplayer_left_AAB;
	private _bbr_botlayer_right_BAB_mtww = _object modelToWorldWorld _bbr_botlayer_right_BAB;
	private _bbr_toplayer_left_ABB_mtww = _object modelToWorldWorld _bbr_toplayer_left_ABB;
	private _bbr_botlayer_right_BBB_mtww = _object modelToWorldWorld _bbr_botlayer_right_BBB;

	//Calculate 2D bounds
	//Crate arrays for x,y,z coordinates
	private _bbr_x_coords = [_bbr_botlayer_left_AAA_mtww select 0,_bbr_botlayer_right_BAA_mtww select 0,_bbr_botlayer_left_ABA_mtww select 0,_bbr_botlayer_right_BBA_mtww select 0,_bbr_toplayer_left_AAB_mtww select 0,_bbr_botlayer_right_BAB_mtww select 0,_bbr_toplayer_left_ABB_mtww select 0,_bbr_botlayer_right_BBB_mtww select 0];
	private _bbr_y_coords = [_bbr_botlayer_left_AAA_mtww select 1,_bbr_botlayer_right_BAA_mtww select 1,_bbr_botlayer_left_ABA_mtww select 1,_bbr_botlayer_right_BBA_mtww select 1,_bbr_toplayer_left_AAB_mtww select 1,_bbr_botlayer_right_BAB_mtww select 1,_bbr_toplayer_left_ABB_mtww select 1,_bbr_botlayer_right_BBB_mtww select 1];
	private _bbr_z_coords = [_bbr_botlayer_left_AAA_mtww select 2,_bbr_botlayer_right_BAA_mtww select 2,_bbr_botlayer_left_ABA_mtww select 2,_bbr_botlayer_right_BBA_mtww select 2,_bbr_toplayer_left_AAB_mtww select 2,_bbr_botlayer_right_BAB_mtww select 2,_bbr_toplayer_left_ABB_mtww select 2,_bbr_botlayer_right_BBB_mtww select 2];
	//Find min and max values for x,y,z coordinates
	private _min_x = selectMin _bbr_x_coords;
	private _max_x = selectMax _bbr_x_coords;
	private _min_y = selectMin _bbr_y_coords;
	private _max_y = selectMax _bbr_y_coords;
	private _max_z = selectMax _bbr_z_coords;
	private _min_z = selectMin _bbr_z_coords;

	diag_log format["_max_z: %1 | _min_z: %2",_max_z,_min_z];

	// _objectHeight = _maxHeight - _minHeight;

	//Create varaible for return value
	private _return_val = [];

	if ((_3d isEqualTo 1) or (_3d isEqualTo true)) then {
		_return_val pushBack [[_min_x, _min_y,_maxHeight],[_max_x, _max_y,_maxHeight],[_min_x, _max_y,_maxHeight],[_max_x, _min_y,_maxHeight],[_min_z,_max_z]];
	} else {
		//Return array of coordinates of the 2D bounding box
		_return_val pushBack [[_min_x, _min_y],[_min_x, _max_y],[_max_x, _min_y],[_max_x, _max_y],[_min_z,_max_z]];
	};

	_return_val select 0;
};


checkLineIntersectsSurfaces = {
	params ["_x","_y","_min_z","_max_z"];

	lineIntersectsSurfaces [
		[_x,_y,_max_z], 
		[_x,_y,_min_z],
		objNull,objNull,true, 1, "GEOM", "NONE"
	];
};


getObjectOutline = {
	//Description:
	//
	//Parameter(s):
	//_2dcoords = [[minx,miny],[minx,maxy],[maxx,miny],[maxx,maxy]]
	//_resolution = distance between scan points in meters
	//Example:
	//

	params ["_object","_2dcoords",["_resolution", 0.01],["_marker_prefix","neko_marker_"]];

	_2dcoords params ["_minXminY","_minXmaxY","_maxXminY","_maxXmaxY","_zHeights"];

	_minXminY params ["_minX","_minY"];
	_maxXmaxY params ["_maxX","_maxY"];
	_zHeights params ["_minZ","_maxZ"];

	diag_log format["_2dcoords: %1",_2dcoords];

	private _scanXlength = _maxX - _minX;
	private _scanYlength = _maxY - _minY;

	private _xStop = _scanXlength / _resolution;
	private _yStop = _scanYlength / _resolution;

	private _scan_coordinates = [];
	markerIds = [];

	private _loopcounter = 0;
	private _xval = _minx;
	private _yval = _miny;
	private _tempy = 0;
	private _scanResult = true;


	//First method scanning every possible point in the bounding box
    while {_xval < (_maxx + (_resolution*0.5))} do {
		_tempy = _yval;
		while {_yval < (_maxy + (_resolution*0.5))} do {

			
			_scanResult = [_xval,_yval,_minZ,_maxZ] call checkLineIntersectsSurfaces; // select 0 params ["","","","_scanObject"];
			diag_log format["_scanResult: %1", _scanResult];
			_scanResult select 0 params ["","","","_scanObject"];
			//diag_log format["mxz: %1, mnz: %2, _scanResult: %3 | _scanObject: %4",_maxZ,_minZ,_scanResult, _scanObject];
			if ((_scanObject isEqualTo _object) && (_scanObject isKindOf "House")) then {
				_markerName = format["%1%2",_marker_prefix,_loopcounter];
				_marker = createMarker [_markerName, [_xval, _yval]];
				//_markerName setMarkerSize [0.15, 0.15];
				_marker setMarkerType "hd_dot";
				diag_log format["lineIntersects coords: %1|%2", [_xval, _yval,_maxZ], [_xval,_yval,(_minZ-5)]];
			};
			_yval = _yval + _resolution;
			_loopcounter = _loopcounter + 1;
		};
		_yval = _tempy;
		_xval = _xval + _resolution;
	};

	private _not_outline = [];
	private _outline = [];
	//Second method scanning only the edges of the building
	//Start the scan from the bottom left corner
	

    _scan_coordinates;
};


// _2dBounds = [one, true] call getTopDownProjection;
// _aaa = [one, _2dBounds, 0.25] call getObjectOutline;

// _2dBounds = [two, true] call getTopDownProjection;
// _aaa = [two, _2dBounds, 0.25] call getObjectOutline;

// _2dBounds = [three, true] call getTopDownProjection;
// _aaa = [three, _2dBounds, 0.25] call getObjectOutline;

//_2dBounds = [four, true] call getTopDownProjection;
//_aaa = [four, _2dBounds, 0.25] call getObjectOutline;

_2dBounds = [five, true] call getTopDownProjection;
_aaa = [five, _2dBounds, 0.1] call getObjectOutline;

// _2dBounds = [six, true] call getTopDownProjection;
// _aaa = [six, _2dBounds, 0.25] call getObjectOutline;

