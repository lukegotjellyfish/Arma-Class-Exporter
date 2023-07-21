////https://community.bistudio.com/wiki/DIK_KeyCodes
diagToggleKey = 5;

upOneMagKey   = 3;
downOneMagKey = 4;
upTenMagKey   = 6;
downTenMagKey = 7;

switchWeaponTypeKey = 8;
// 3 = 2 Key
// 4 = 3 Key
// 5 = 4 Key
// 6 = 5 Key
// 7 = 6 Key
// 8 = 7 Key






//If the unit has a pistol it will interfere with default keys:
_playerLoadout = getUnitLoadout player;
_handgun = _playerLoadout select 2 select 0;
player removeWeapon _handgun;


changeMag = {
	params ["_x","_weapon","_magazine"];
 
	player removeWeapon _weapon;
	player addMagazine format[_magazine + str _x + "mm_rha"];
	player addWeapon _weapon;
};

x = 1;
weaponIndex = 0;
weaponList=["rhs_weap_M107_Neko_Armour","rhs_weap_M107_Neko_HEAT"];
weapon = weaponList select weaponIndex;
magazine = "neko_mag_";
magazineList=["neko_mag_","neko_HEAT_mag_"];
magazineKeyHandler = (findDisplay 46) displayAddEventHandler ["KeyDown", {
	params["_display", "_keyCode", "_shft", "_ctr", "_alt"];

	switch (_keyCode) do {
		case upOneMagKey: {if (x < 1500) then {x = x + 1; [x,weapon,magazine] call changeMag;};};
		case downOneMagKey: {if (x > 1) then {x = x - 1; [x,weapon,magazine] call changeMag;};};
		case upTenMagKey: {if (x <= 1490) then {x = x + 10; [x,weapon,magazine] call changeMag;};};
		case downTenMagKey: {if (x > 10) then {x = x - 10; [x,weapon,magazine] call changeMag;};};
		case switchWeaponTypeKey: {
			if (weaponIndex isEqualTo 0) then {weaponIndex = 1} else {weaponIndex = 0};
			weapon = weaponList select weaponIndex;
			magazine = magazineList  select weaponIndex;
			[x,weapon,magazine] call changeMag;
		};

		//REMOVE THIS PART IF YOU ARE NOT ON DEVBRANCH--------------------------------------------------------------------
		case diagToggleKey: {                                                                                          //|
			gameIsDiag = true;                                                                                         //|
			if ((productVersion select 4) == "Diag") then {                                                            //|
				//diag_toggle is a function of the dev branch https://community.bistudio.com/wiki/Arma_3_Diagnostics_Exe |
				//diag_toggle causes scripts to fail when not run on devbranch                                           |
				diag_toggle 'shots';                                                                                   //|
				//To have two diag_toggles, there needs to be a delay                                                    |
				[] spawn {uiSleep 0.001; diag_toggle 'shots'};                                                         //|
			};                                                                                                         //|
		//END OF THIS PART-----------------------------------------------------------------------------------------------|

		};
		default {hint "Default on switch _keyCode"};
	};
}];


removeHandlers = player addAction ["Stop script", {
	(findDisplay 46) displayRemoveEventHandler ["KeyDown", magazineKeyHandler];
}];