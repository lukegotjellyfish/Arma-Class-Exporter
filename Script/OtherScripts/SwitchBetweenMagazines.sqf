changeMag = {
	params ["_x"];

	player removeWeapon "rhs_weap_m107";
	player addMagazine format["neko_mag_" + str _x + "mm_rha"];
	player addWeapon "rhs_weap_m107";
};


////https://community.bistudio.com/wiki/DIK_KeyCodes
diagToggleKey = 5;

upOneMagKey   = 3;
downOneMagKey = 4;
upTenMagKey   = 6;
downTenMagKey = 7;
// 3 = 2 Key
// 4 = 3 Key
// 5 = 4 Key
// 6 = 5 Key
// 7 = 6 Key

gameIsDiag = false;
if ((productVersion select 4) == "Diag") then {
	diagToggle = (findDisplay 46) displayAddEventHandler ["KeyDown", {
		params["_display", "_keyCode", "_shft", "_ctr", "_alt"];

		if (_keyCode == diagToggleKey) then {
			//diag_toggle is a function of the dev branch https://community.bistudio.com/wiki/Arma_3_Diagnostics_Exe
			diag_toggle 'shots';
			[] spawn {uiSleep 0.001; diag_toggle 'shots'};
			//To have two diag_toggles, there needs to be a delay
		};
	}];
	gameIsDiag = true;
};

x = 1;
upOneMag = (findDisplay 46) displayAddEventHandler ["KeyDown", {
	params["_display", "_keyCode", "_shft", "_ctr", "_alt"];

	if (_keyCode == 3) then {
		if (x < 1500) then {
			x = x + 1; [x] call changeMag;
		};
	};
}];
downOneMag = (findDisplay 46) displayAddEventHandler ["KeyDown", {
	params["_display", "_keyCode", "_shft", "_ctr", "_alt"];

	if (_keyCode == 4) then {
		if (x > 1) then {
			x = x - 1; [x] call changeMag;
		};
	};
}];
upTenMag = (findDisplay 46) displayAddEventHandler ["KeyDown", {
	params["_display", "_keyCode", "_shft", "_ctr", "_alt"];

	if (_keyCode == 6) then {
		if (x <= 1490) then {
			x = x + 10; [x] call changeMag;
		};
	};
}];
downTenMag = (findDisplay 46) displayAddEventHandler ["KeyDown", {
	params["_display", "_keyCode", "_shft", "_ctr", "_alt"];

	if (_keyCode == 7) then {
		if (x > 10) then {
			x = x - 10; [x] call changeMag;
		};
	};
}];


removeHandlers = player addAction ["Stop script", {
	if (gameIsDiag == true) then {(findDisplay 46) displayRemoveEventHandler ["KeyDown", diagToggle]};
	(findDisplay 46) displayRemoveEventHandler ["KeyDown", upOneMag];
	(findDisplay 46) displayRemoveEventHandler ["KeyDown", downOneMag];
	(findDisplay 46) displayRemoveEventHandler ["KeyDown", upTenMag];
	(findDisplay 46) displayRemoveEventHandler ["KeyDown", downTenMag];
}];