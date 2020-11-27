@echo off

set removeMarx=%1
set removeMarx=%removeMarx:~1,-1%

IF "%2" EQU "1" (
	ECHO        =====================================
	ECHO        =   Started at: %removeMarx% =
	ECHO        = Currently at: %date% %time:~0,-3% =
	ECHO        =====================================
	ECHO.
) ELSE (
	ECHO %removeMarx% [%~z3 Bytes] %time:~0,-3%
)