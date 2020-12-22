@ECHO Off
REM Put this .bat file in your arma directory and set exportDir to your
REM  folder to export PBOs
REM 
REM Requres the following on PATH:
REM  PBOConsole (cmdl)  https://github.com/winseros/PBOManager/releases/tag/v0.1.0
REM  CfgConvert         https://community.bistudio.com/wiki/CfgConvert
REM  DeP3D              https://community.bistudio.com/wiki/DeP3d
REM  Pal2PacE           https://community.bistudio.com/wiki/TexView_2
REM  Disabling the OptiPNG function will save a lot of time, disabling dep3d will save a slightly smaller amount
REM   and disabling Pal2PacE will save less on top of that
REM  OptiPNG            http://optipng.sourceforge.net/

REM Folder to export PBOs to
SET exportDir=E:\Games\Arma 3 Mod Files

REM Get start datetime
set startDateTime=%date% %time:~0,-3%
REM Get sanitized start datetime for log title
set LogDateTime=%date:~0,-8%-%date:~3,-5%-%date:~6% %time:~0,-9%-%time:~3,-6%-%time:~6,-3%.%time:~9%
REM Create log folder
CALL :EchoLog "%MKDIRSTRING% '%exportDir%\logs'"
MKDIR "%exportDir%\logs" > nul 2>nul

REM Set strings
set EXCLUDEDSTRING=        [Excluded]
set P3DSTRING=       [DE-P3D]
set DELSTRING=          [DEL]
set WSSSTRING=   [WSS Decode]
set PAL2STRING=     [Pal2PacE]
set OPTISTRING=      [OptiPNG]
set CDSTRING=           [CD]
set CFGSTRING=   [CfgConvert]
set MKDIRSTRING=        [MKDIR]
set FOUNDPBOSTRING=    [Found PBO]
REM Loop through .pbo files in directory and subdirs
for /f "delims=" %%I in ('dir /s/b/a-d *.pbo') do (
	REM If filename matches one of these words, ignore it else run the script. || = Error level NEQ 0
	ECHO %%~nI | findstr "bin.pbo cup_ vegetation radio core.pbo dubbing ui cargoposes signs rocks roads props structures map_ language supplies music plants missions anims animals radio" > nul || (

		CALL :EchoLog "=============================New-PBO=============================="
		CALL :EchoLog "."

		CALL "%~dp0\#DateTime.bat" "%startDateTime%" 1

		for /f "delims==" %%F in ("%%I\.\..\..") do (
			CALL :EchoLog "%FOUNDPBOSTRING% '%%~nxI' in '%%~nF'"
			REM Create directory for MOD
			CALL :EchoLog "%MKDIRSTRING% '.\%%~nF'"
			MKDIR "%exportDir%\%%~nF" > nul 2> nul

			REM If PBO has already been extracted, skip it
			IF NOT EXIST "%exportDir%\%%~nF\%%~nI" (
				REM Extract PBO contents
				ECHO [Unpacking PBO] "%%~pnxI" TO ".\%%~nF\%%~nI"
				PBOConsole -unpack "%%I" "%exportDir%\%%~nF\%%~nI" > nul


				REM Change directory to unpacked pbo
				CALL :EchoLog "%CDSTRING% Going to '.\%%~nF\%%~nI'"
				CD /D "%exportDir%\%%~nF\%%~nI"
				CALL :EchoLog "%CDSTRING% At '.\%%~nF\%%~nI'"


				REM Convert config.bin's to config.cpp's
				FOR /R %%C in (config.bin) do (
					CALL :EchoLog "%CFGSTRING% '%%~dpnxC' TO '%%~nC.cpp'"
					CfgConvert -txt -dst "%%~dpC\config.cpp" "%%C" > nul
					CALL :EchoLog "%DELSTRING% %%C"
					DEL "%%C" > nul 2>nul
					DEL "$NOBIN$" > nul 2>nul
				)
				REM Delete texHeaders.bin if present
				CALL :EchoLog "%DELSTRING% '.\%%~nF\%%~nI\texHeaders.bin'"
				DEL "%exportDir%\%%~nF\%%~nI\texHeaders.bin" > nul 2> nul



				REM Go through files to delete processed p3d files
				FOR /R %%P in (*.p3d) do (
					(Echo "%%P" | FINDSTR /I "_mlod" >NUL) || (
						(Echo "%%P" | FINDSTR /V /I "rhs cba coxhound" >NUL) || (
							REM Run de-p3d on p3d file to convert to mlod
							CALL :EchoLog "%P3DSTRING% '%%~pnxP' TO Mlod"
							REM After adding :EchoLog, DEP3D fucks up if called in any way other
							REM  than this:
							DEP3D "%%P"
							REM Reset CMD colours, darn you DEP3D
							COLOR 07
							REM Delete processed file
							CALL :EchoLog "%DELSTRING% '%%~pnxP'"
							DEL "%%P"
						)
					)
				)
				REM Process WSS files TO wav and delete WSS
				FOR /R %%P in (*.wss) do (
					echo %%P | findstr /V /I "rhs jsrs coxhound" || (
						CALL :EchoLog "%WSSSTRING% '%%~pnxP' TO '%%~nP.wav'"
						WSSDecoder "%%P"
						CALL :EchoLog "%DELSTRING% '%%~pnxP'"
						DEL "%%P"
					)
				)

				REM Go through all .paa files in directory
				for /R %%f in (*.paa) do (
					CALL :EchoLog "%PAL2STRING% '%%~pnxf' TO '%%~nf.png'"
					Pal2PacE "%%f" "%%~dpnf.png" > nul
					CALL :EchoLog "%DELSTRING% '%%~pnxf'"
					REM Lossless compression of png
					REM -o 2 usually gives better results but takes much longer
					REM -o 3-7(max) usually doesn't improve (by much) filesize and takes ages
					CALL "%~dp0\#DateTime.bat" "%OPTISTRING% OptiPNG Start:" "2" "%%~dpnf.png"
					CALL "%~dp0\#DateTime.bat" "%OPTISTRING% OptiPNG Start:" "2" "%%~dpnf.png" >> "%exportDir%\logs\[%LogDateTime%] ExportPBOs.Log"
					CALL :EchoLog "%OPTISTRING%        %%~dpnf.png"
					OPTIPNG -o 1 -preserve "%%~dpnf.png" > nul 2>nul
					REM Get PNG end size
					CALL "%~dp0\#DateTime.bat" "%OPTISTRING%   OptiPNG End:" "2" "%%~dpnf.png"
					CALL "%~dp0\#DateTime.bat" "%OPTISTRING%   OptiPNG End:" "2" "%%~dpnf.png" >> "%exportDir%\logs\[%LogDateTime%] ExportPBOs.Log"
					DEL "%%f"
				)
				REM Go through all .rvmat files in directory
				for /R %%f in (*.rvmat) do (
					CALL :EchoLog "%DELSTRING% '%%~pnxf'"
					DEL "%%f"
				)
				REM Go through all .rtm files in directory
				for /R %%f in (*.rtm) do (
					CALL :EchoLog "%DELSTRING% '%%~pnxf'"
					DEL "%%f"
				)

				REM Return to arma directory
				CALL :EchoLog "%CDSTRING% '%~dp0'"
				CD /D %~dp0
			)
		)
		CALL :EchoLog "."
	)
)
PAUSE





:EchoLog
REM Fetch timestamp
For /f "tokens=1-2 delims=/:" %%a in ('time /t') do (set LOGTIME=%%a:%%b)
IF "%LOGTIME%" EQU "" (
	CALL :EchoLog "%~1"
	EXIT /B
)

IF "%~1" NEQ "." (
	ECHO %~1
	ECHO [%LOGTIME%] %~1 >> "%exportDir%\logs\[%LogDateTime%] ExportPBOs.Log"
) else (
	ECHO.
	ECHO [%LOGTIME%] >> "%exportDir%\logs\[%LogDateTime%] ExportPBOs.Log"
)
EXIT /B





