player allowDamage false;

timeArray = [];
reloadTimes = [];

disEH = vehicle player AddEventHandler ["Fired", {
	timeArray pushBack time;
	if (count timeArray = 2) then {
		timeArray select 1 - timeArray select 0;
		timeArray = [];
		hint format["Reload Time: %1", reloadTime];
	};
}];

remove = player addAction ["Remove reload timer", {
	vehicle player removeEventHandler ["Fired",disEH];
}]
