startTime = 0;
player allowDamage false;


disEH = (findDisplay 46) displayAddEventHandler ["KeyDown", {
	if ((_this select 1) == 19) then {
		startTime = time;
		reloadedEH = player addEventHandler ["Reloaded", {
			endTime = time;
			hint format["Start Time: %1\n  End Time: %2\nTime to reload: %3", startTime, endTime, endTime-startTime];
		}];
	};
}];

remove = player addAction ["Remove reload tracker", {
	player removeEventHandler ["Reloaded", reloadedEH];
	(findDisplay 46) displayRemoveEventHandler ["KeyDown",disEH];
	player removeAction remove;
}]
