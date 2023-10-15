addMissionEventHandler ["Draw3D", {
	private _veh = vehicle player;

	private _bbr  = 0 boundingBoxReal _veh;
	private _bbrf = _bbr select 0;
	private _bbrs = _bbr select 1;

	//Variables to hold values from array (more time efficient)
	private _bbrA_sel_zer = _bbrf select 0;
	private _bbrA_sel_one = _bbrf select 1;
	private _bbrA_sel_two = _bbrf select 2;
	private _bbrB_sel_zer = _bbrs select 0;
	private _bbrB_sel_one = _bbrs select 1;
	private _bbrB_sel_two = _bbrs select 2;

    //Stats
    private _maxWidth = abs (_bbrB_sel_zer - _bbrA_sel_zer);
    private _maxLength = abs (_bbrB_sel_one - _bbrA_sel_one);
    private _maxHeight = abs (_bbrB_sel_two - _bbrA_sel_two);

	//Middle areas:
	private _bbrw_mid = _bbrA_sel_zer + _bbrB_sel_zer;
	private _bbrl_mid = _bbrA_sel_one + _bbrB_sel_one;
	private _bbrh_mid = _bbrA_sel_two + _bbrB_sel_two;

	//Left side of vehicle
	private _bbr_botlayer_left_AAA = [_bbrA_sel_zer,_bbrA_sel_one,_bbrA_sel_two];
	private _bbr_botlayer_left_ABA = [_bbrA_sel_zer,_bbrB_sel_one,_bbrA_sel_two];
	private _bbr_toplayer_left_AAB = [_bbrA_sel_zer,_bbrA_sel_one,_bbrB_sel_two];
	private _bbr_toplayer_left_ABB = [_bbrA_sel_zer,_bbrB_sel_one,_bbrB_sel_two];
	//Right side of vehicle
	private _bbr_botlayer_right_BAA = [_bbrB_sel_zer,_bbrA_sel_one,_bbrA_sel_two];
	private _bbr_botlayer_right_BBA = [_bbrB_sel_zer,_bbrB_sel_one,_bbrA_sel_two];
	private _bbr_botlayer_right_BAB = [_bbrB_sel_zer,_bbrA_sel_one,_bbrB_sel_two];
	private _bbr_botlayer_right_BBB = [_bbrB_sel_zer,_bbrB_sel_one,_bbrB_sel_two];

	private _bbr_botlayer_left_AAA_mtw = _veh modelToWorldWorld _bbr_botlayer_left_AAA;
	private _bbr_botlayer_right_BAA_mtw = _veh modelToWorldWorld _bbr_botlayer_right_BAA;
	private _bbr_botlayer_left_ABA_mtw = _veh modelToWorldWorld _bbr_botlayer_left_ABA;
	private _bbr_botlayer_right_BBA_mtw = _veh modelToWorldWorld _bbr_botlayer_right_BBA;

	private _bbr_toplayer_left_AAB_mtw = _veh modelToWorldWorld _bbr_toplayer_left_AAB;
	private _bbr_botlayer_right_BAB_mtw = _veh modelToWorldWorld _bbr_botlayer_right_BAB;
	private _bbr_toplayer_left_ABB_mtw = _veh modelToWorldWorld _bbr_toplayer_left_ABB;
	private _bbr_botlayer_right_BBB_mtw = _veh modelToWorldWorld _bbr_botlayer_right_BBB;

	//Calculate 2D bounds
    //Crate arrays for x,y,z coordinates
	private _bbr_x_coords = [_bbr_botlayer_left_AAA_mtw select 0,_bbr_botlayer_right_BAA_mtw select 0,_bbr_botlayer_left_ABA_mtw select 0,_bbr_botlayer_right_BBA_mtw select 0,_bbr_toplayer_left_AAB_mtw select 0,_bbr_botlayer_right_BAB_mtw select 0,_bbr_toplayer_left_ABB_mtw select 0,_bbr_botlayer_right_BBB_mtw select 0];
	private _bbr_y_coords = [_bbr_botlayer_left_AAA_mtw select 1,_bbr_botlayer_right_BAA_mtw select 1,_bbr_botlayer_left_ABA_mtw select 1,_bbr_botlayer_right_BBA_mtw select 1,_bbr_toplayer_left_AAB_mtw select 1,_bbr_botlayer_right_BAB_mtw select 1,_bbr_toplayer_left_ABB_mtw select 1,_bbr_botlayer_right_BBB_mtw select 1];
	private _bbr_z_coords = [_bbr_botlayer_left_AAA_mtw select 2,_bbr_botlayer_right_BAA_mtw select 2,_bbr_botlayer_left_ABA_mtw select 2,_bbr_botlayer_right_BBA_mtw select 2,_bbr_toplayer_left_AAB_mtw select 2,_bbr_botlayer_right_BAB_mtw select 2,_bbr_toplayer_left_ABB_mtw select 2,_bbr_botlayer_right_BBB_mtw select 2];
    //Find min and max values for x,y,z coordinates
	private _min_x = selectMin _bbr_x_coords;
	private _max_x = selectMax _bbr_x_coords;
	private _min_y = selectMin _bbr_y_coords;
	private _max_y = selectMax _bbr_y_coords;
	private _maxHeight = selectMax _bbr_z_coords;
	// _minHeight = selectMin _bbr_z_coords;
	// _vehHeight = _maxHeight - _minHeight;

    //Convert ASL coordinates to AGL coordinates for use in drawX3D
	private _2d_coord_min = ASLToAGL [_min_x, _min_y, _maxHeight];
	private _2d_coord_max = ASLToAGL [_max_x, _max_y, _maxHeight];
	private _2d_coord_xmin_ymax = ASLToAGL [_min_x, _max_y, _maxHeight];
	private _2d_coord_xmax_ymin = ASLToAGL [_max_x, _min_y, _maxHeight];

    //Display AGL coordinates
	//hint format["%1\n%2\n%3\n%4", _2d_coord_min, _2d_coord_max, _2d_coord_xmin_ymax, _2d_coord_xmax_ymin];
    //Draw bound lines
    private _topRectangleColour = [1,0,0,1];
	drawLine3D [_2d_coord_min, _2d_coord_xmin_ymax, _topRectangleColour];
	drawLine3D [_2d_coord_min, _2d_coord_xmax_ymin, _topRectangleColour];
	drawLine3D [_2d_coord_max, _2d_coord_xmin_ymax, _topRectangleColour];
	drawLine3D [_2d_coord_max, _2d_coord_xmax_ymin, _topRectangleColour];
    //Draw bound coord labels
    drawIcon3D ["", [1,0,0,1], _2d_coord_min, 0, 0, 0, "Xmin,Ymin", 1, 0.05, "PuristaMedium"];
    drawIcon3D ["", [1,0,0,1], _2d_coord_max, 0, 0, 0, "Xmax,Ymin", 1, 0.05, "PuristaMedium"];
    drawIcon3D ["", [1,0,0,1], _2d_coord_xmin_ymax, 0, 0, 0, "Xmin,Ymax", 1, 0.05, "PuristaMedium"];
    drawIcon3D ["", [1,0,0,1], _2d_coord_xmax_ymin, 0, 0, 0, "Xmax,Ymax", 1, 0.05, "PuristaMedium"];


    

}];

