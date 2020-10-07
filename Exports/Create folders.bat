@echo off

MKDIR BluFor\LauncherMagazines
MKDIR BluFor\Launchers
MKDIR BluFor\Magazines
MKDIR BluFor\VehicleMagazines
MKDIR BluFor\Vehicles
MKDIR BluFor\VehicleWeapons
MKDIR BluFor\Weapons

MKDIR OpFor\LauncherMagazines
MKDIR OpFor\Launchers
MKDIR OpFor\Magazines
MKDIR OpFor\VehicleMagazines
MKDIR OpFor\Vehicles
MKDIR OpFor\VehicleWeapons
MKDIR OpFor\Weapons

MKDIR Exports

REM CD BluFor
REM for /r %%i in (*.cpp *.py) do (
	REM echo Recycled %%~fi
	REM recycle %%i
REM )
REM CD ..\
REM CD OpFor
REM for /r %%i in (*.cpp *.py) do (
	REM echo Recycled %%~fi
	REM recycle %%i
REM )
REM PAUSE