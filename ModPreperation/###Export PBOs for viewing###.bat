@ECHO Off
REM Put this .bat file in your arma directory and set exportDir to your
REM  folder to export PBOs
REM 
REM Requres the following on PATH:
REM  PBOConsole (cmdl)  https://github.com/winseros/PBOManager/releases/tag/v0.1.0
REM  CfgConvert         https://community.bistudio.com/wiki/CfgConvert
REM  DeP3D              https://community.bistudio.com/wiki/DeP3d
REM  Pal2PcE            https://community.bistudio.com/wiki/TexView_2
REM  OptiPNG            http://optipng.sourceforge.net/

REM Get start datetime
set startDateTime=%date% %time:~0,-3%


REM Folder to export PBOs to
SET exportDir=E:\Games\Arma 3 Mod Files
REM Set stringS
set EXCLUDEDSTRING=        [Excluded]
set DEP3DSTRING=       [DE-P3D]
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
	ECHO %%~nI | findstr "bin.pbo vegetation radio core.pbo dubbing ui cargoposes signs rocks roads props structures map_ language supplies music plants missions anims animals radio" > nul || (

		CALL :EchoLog "=============================New-PBO=============================="
		CALL :EchoLog "."

		CALL "#DateTime.bat" "%startDateTime%"
		
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
					echo %%P | findstr /V /I "rhs coxhound" > nul || (
						REM Run dep3d on p3d file to convert to mlod
						CALL :EchoLog "%DEP3DSTRING% '%%~pnxP' TO Mlod"
						DEP3D "%%P" > nul
						REM Delete processed file
						CALL :EchoLog "%DELSTRING% '%%~pnxP'"
						DEL "%%P"
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
					DEL "%%f"
					REM Lossless compression of png
					REM -o 2 usually gives better results but takes much longer
					REM -o 3-7(max) usually doesn't improve (by much) filesize and takes ages
					CALL :EchoLog "%OPTISTRING% '%%~pnxf' TO '%%~nf.png'"
					CALL :EchoLog "%OPTISTRING% OPTIPNG START: %time:~0,-3%"
					CALL :EchoLog "%OPTISTRING%        %%~dpnf.png"
					OPTIPNG -o 1 -preserve "%%~dpnf.png" > nul 2>nul
					CALL :EchoLog "%OPTISTRING% OPTIPNG END: %time:~0,-3%"
				)
				REM Go through all .rvmat files in directory
				for /R %%f in (*.rvmat) do (
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
	ECHO [%LOGTIME%] %~1 >> "%exportDir%\ExportPBOsLog.txt"
) else (
	ECHO.
	ECHO [%LOGTIME%] >> "%exportDir%\ExportPBOsLog.txt"
)
EXIT /B





