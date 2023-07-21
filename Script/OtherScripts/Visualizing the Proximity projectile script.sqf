addMissionEventHandler ["Draw3D", {
	private _veh = vehicle player;

	private _bbR  = 0 boundingBoxReal _veh;
	private _bbRf = _bbR select 0;
	private _bbRs = _bbR select 1;

	//Variables to hold values from array (more time efficient)
	private _bbrF_sel_zer = _bbRf select 0;
	private _bbrF_sel_one = _bbRf select 1;
	private _bbrF_sel_two = _bbRf select 2;
	private _bbrS_sel_zer = _bbRs select 0;
	private _bbrS_sel_one = _bbRs select 1;
	private _bbrS_sel_two = _bbRs select 2;

	//Middle areas:
	private _bbRw_mid = _bbrF_sel_zer + _bbrS_sel_zer;
	private _bbRl_mid = _bbrF_sel_one + _bbrS_sel_one;
	private _bbRh_mid = _bbrF_sel_two + _bbrS_sel_two;

	//Left side of vehicle
		//Bottom
	private _bbR_botlayer_left_f = [_bbrF_sel_zer,_bbrF_sel_one,_bbrF_sel_two];
	private _bbR_botlayer_left_m = [_bbrF_sel_zer,_bbRl_mid,    _bbrF_sel_two];
	private _bbR_botlayer_left_b = [_bbrF_sel_zer,_bbrS_sel_one,_bbrF_sel_two];
		//Middle
	private _bbR_midlayer_left_f = [_bbrF_sel_zer,_bbrF_sel_one,_bbRh_mid];
	private _bbR_midlayer_left_m = [_bbrF_sel_zer,_bbRl_mid,    _bbRh_mid];
	private _bbR_midlayer_left_b = [_bbrF_sel_zer,_bbrS_sel_one,_bbRh_mid];
		//Top
	private _bbR_toplayer_left_f = [_bbrF_sel_zer,_bbrF_sel_one,_bbrS_sel_two];
	private _bbR_toplayer_left_m = [_bbrF_sel_zer,_bbRl_mid,    _bbrS_sel_two];
	private _bbR_toplayer_left_b = [_bbrF_sel_zer,_bbrS_sel_one,_bbrS_sel_two];

	//Middle of vehicle
		//Bottom
	private _bbR_botlayer_mid_f = [_bbRw_mid,_bbrF_sel_one,_bbrF_sel_two];
	private _bbR_botlayer_mid_m = [_bbRw_mid,_bbRl_mid,    _bbrF_sel_two];
	private _bbR_botlayer_mid_b = [_bbRw_mid,_bbrS_sel_one,_bbrF_sel_two];
		//Middle
	private _bbR_midlayer_mid_f = [_bbRw_mid,_bbrF_sel_one,_bbRh_mid];
	//private _bbR_mid_m = [_bbRw_mid,_bbRl_mid,_bbRh_mid];
	private _bbR_midlayer_mid_b = [_bbRw_mid,_bbrS_sel_one,_bbRh_mid];
		//Top
	private _bbR_toplayer_mid_f = [_bbRw_mid,_bbrF_sel_one,_bbrS_sel_two];
	private _bbR_toplayer_mid_m = [_bbRw_mid,_bbRl_mid,    _bbrS_sel_two];
	private _bbR_toplayer_mid_b = [_bbRw_mid,_bbrS_sel_one,_bbrS_sel_two];

	//Right side of vehicle
		//Bottom
	private _bbR_botlayer_right_f = [_bbrS_sel_zer,_bbrF_sel_one,_bbrF_sel_two];
	private _bbR_botlayer_right_m = [_bbrS_sel_zer,_bbRl_mid,    _bbrF_sel_two];
	private _bbR_botlayer_right_b = [_bbrS_sel_zer,_bbrS_sel_one,_bbrF_sel_two];
		//Middle
	private _bbR_midlayer_right_f = [_bbrS_sel_zer,_bbrF_sel_one,_bbRh_mid];
	private _bbR_midlayer_right_m = [_bbrS_sel_zer,_bbRl_mid,   _bbRh_mid];
	private _bbR_midlayer_right_b = [_bbrS_sel_zer,_bbrS_sel_one,_bbRh_mid];
		//Top
	private _bbR_toplayer_right_f = [_bbrS_sel_zer,_bbrF_sel_one,_bbrS_sel_two];
	private _bbR_toplayer_right_m = [_bbrS_sel_zer,_bbRl_mid,    _bbrS_sel_two];
	private _bbR_toplayer_right_b = [_bbrS_sel_zer,_bbrS_sel_one,_bbrS_sel_two];


	private _bottomRectangleColour = [0,0,1,1];
	private _bottomIntersectColour = [0,1,1,1];
	private _middleRectangleColour = [0,1,0,1];
	private _middleIntersectColour = [1,1,0,1];
	private _topRectangleColour    = [1,0,0,1];
	private _topIntersectColour    = [1,0,1,1];
	private _verticalLineColour    = [0,0,0,1];

	//Horizontal Lines
		//Botlayer rectangle
		drawLine3D [_veh modelToWorld _bbR_botlayer_left_f, _veh modelToWorld _bbR_botlayer_right_f,_bottomRectangleColour];
		drawLine3D [_veh modelToWorld _bbR_botlayer_left_f, _veh modelToWorld _bbR_botlayer_left_b, _bottomRectangleColour];
		drawLine3D [_veh modelToWorld _bbR_botlayer_right_f,_veh modelToWorld _bbR_botlayer_right_b,_bottomRectangleColour];
		drawLine3D [_veh modelToWorld _bbR_botlayer_right_b,_veh modelToWorld _bbR_botlayer_left_b, _bottomRectangleColour];
			//Intersecting lines
			drawLine3D [_veh modelToWorld _bbR_botlayer_left_f, _veh modelToWorld _bbR_botlayer_right_b,_bottomIntersectColour];
			drawLine3D [_veh modelToWorld _bbR_botlayer_left_b, _veh modelToWorld _bbR_botlayer_right_f,_bottomIntersectColour];
		//Midlayer rectangle
		drawLine3D [_veh modelToWorld _bbR_midlayer_left_f, _veh modelToWorld _bbR_midlayer_right_f,_middleRectangleColour];
		drawLine3D [_veh modelToWorld _bbR_midlayer_left_f, _veh modelToWorld _bbR_midlayer_left_b, _middleRectangleColour];
		drawLine3D [_veh modelToWorld _bbR_midlayer_right_f,_veh modelToWorld _bbR_midlayer_right_b,_middleRectangleColour];
		drawLine3D [_veh modelToWorld _bbR_midlayer_right_b,_veh modelToWorld _bbR_midlayer_left_b, _middleRectangleColour];
			//Intersecting lines
			drawLine3D [_veh modelToWorld _bbR_midlayer_left_f, _veh modelToWorld _bbR_midlayer_right_b,_middleIntersectColour];
			drawLine3D [_veh modelToWorld _bbR_midlayer_left_b, _veh modelToWorld _bbR_midlayer_right_f,_middleIntersectColour];
		//Toplayer rectangle
		drawLine3D [_veh modelToWorld _bbR_toplayer_left_f, _veh modelToWorld _bbR_toplayer_right_f,_topRectangleColour];
		drawLine3D [_veh modelToWorld _bbR_toplayer_left_f, _veh modelToWorld _bbR_toplayer_left_b, _topRectangleColour];
		drawLine3D [_veh modelToWorld _bbR_toplayer_right_f,_veh modelToWorld _bbR_toplayer_right_b,_topRectangleColour];
		drawLine3D [_veh modelToWorld _bbR_toplayer_right_b,_veh modelToWorld _bbR_toplayer_left_b, _topRectangleColour];
			//Intersecting lines
			drawLine3D [_veh modelToWorld _bbR_toplayer_left_f, _veh modelToWorld _bbR_toplayer_right_b,_topIntersectColour];
			drawLine3D [_veh modelToWorld _bbR_toplayer_left_b, _veh modelToWorld _bbR_toplayer_right_f,_topIntersectColour];
	//Vertical Lines
	drawLine3D [_veh modelToWorld _bbR_botlayer_left_f, _veh modelToWorld _bbR_topLayer_left_f, _verticalLineColour];
	drawLine3D [_veh modelToWorld _bbR_botlayer_left_m, _veh modelToWorld _bbR_topLayer_left_m, _verticalLineColour];
	drawLine3D [_veh modelToWorld _bbR_botlayer_left_b, _veh modelToWorld _bbR_topLayer_left_b, _verticalLineColour];
	drawLine3D [_veh modelToWorld _bbR_botlayer_mid_f, _veh modelToWorld _bbR_topLayer_mid_f, _verticalLineColour];
	drawLine3D [_veh modelToWorld _bbR_botlayer_mid_m, _veh modelToWorld _bbR_topLayer_mid_m, _verticalLineColour];
	drawLine3D [_veh modelToWorld _bbR_botlayer_mid_b, _veh modelToWorld _bbR_topLayer_mid_b, _verticalLineColour];
	drawLine3D [_veh modelToWorld _bbR_botlayer_right_f, _veh modelToWorld _bbR_topLayer_right_f, _verticalLineColour];
	drawLine3D [_veh modelToWorld _bbR_botlayer_right_m, _veh modelToWorld _bbR_topLayer_right_m, _verticalLineColour];
	drawLine3D [_veh modelToWorld _bbR_botlayer_right_b, _veh modelToWorld _bbR_topLayer_right_b, _verticalLineColour];
}];