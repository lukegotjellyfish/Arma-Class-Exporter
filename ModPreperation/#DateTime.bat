@echo off


IF "%2" EQU "1" (
ECHO        =======================================
ECHO        =   Started at: %1 =
ECHO        = Currently at: "%date% %time:~0,-3%" =
ECHO        =======================================
ECHO.
) ELSE (
	ECHO %1 %time:~0,-3%
)