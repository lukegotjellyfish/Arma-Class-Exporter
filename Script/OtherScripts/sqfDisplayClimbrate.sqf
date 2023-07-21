[]spawn {
	previousPos=getPosASL(vehicle player);
	sleepTime=0.33;
	while {true} do {
		sleep sleepTime;
		currentPos=getPosASL(vehicle player);
		climbRate=(currentPos select 2) - (previousPos select 2);
		hintSilent format["Climb Rate: %1m/s",climbRate*(1/sleepTime)];
		previousPos=currentPos;
	};
};