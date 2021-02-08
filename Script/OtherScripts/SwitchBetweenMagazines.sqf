changeMag = {
	params ["_x"];

	player removeWeapon "rhs_weap_m107";
	player addMagazine format["neko_mag_" + str _x + "mm_rha"];
	player addWeapon "rhs_weap_m107";
};


////https://community.bistudio.com/wiki/DIK_KeyCodes
// 3 = 2 Key
// 4 = 3
// 5 = 4
// 6 = 5
// 7 = 6
diag_toggleToggle = (findDisplay 46) displayAddEventHandler ["KeyDown", "if ((_this select 1) == 5) then {diag_log('single diag_toggle'); diag_toggle 'shots';};"];

x = 100;
upOneMag = (findDisplay 46) displayAddEventHandler ["KeyDown", "if ((_this select 1) == 3) then {
		if (x < 1500) then {
			x = x + 1; [x] call changeMag;
		};
	};"];
downOneMag = (findDisplay 46) displayAddEventHandler ["KeyDown", "if ((_this select 1) == 4) then {
		if (x > 1) then {
			x = x - 1; [x] call changeMag;
		};
	};"];
upTenMag = (findDisplay 46) displayAddEventHandler ["KeyDown", "if ((_this select 1) == 5) then {
		if (x <= 1490) then {
			x = x + 10; [x] call changeMag;
		};
	};"];
downTenMag = (findDisplay 46) displayAddEventHandler ["KeyDown", "if ((_this select 1) == 6) then {
		if (x > 10) then {
			x = x - 10; [x] call changeMag;
		};
	};"];


removeHandlers = player addAction ["Stop script", {
	(findDisplay 46) displayRemoveEventHandler ["KeyDown", diag_toggleToggle];
	(findDisplay 46) displayRemoveEventHandler ["KeyDown", upOneMag];
	(findDisplay 46) displayRemoveEventHandler ["KeyDown", downOneMag];
	(findDisplay 46) displayRemoveEventHandler ["KeyDown", upTenMag];
	(findDisplay 46) displayRemoveEventHandler ["KeyDown", downTenMag];
}];