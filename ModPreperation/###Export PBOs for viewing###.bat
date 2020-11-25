@ECHO Off

::Put this .bat file in your arma directory and set exportDir to your
:: folder to export PBOs
::
::Requres the following on PATH:
:: PBOConsole (cmdl)  https://github.com/winseros/PBOManager/releases/tag/v0.1.0
:: CfgConvert         https://community.bistudio.com/wiki/CfgConvert
:: RECYCLE (cmdUtils) http://www.maddogsw.com/cmdutils/
:: DeP3               Dhttps://community.bistudio.com/wiki/DeP3d
:: Pal2PcE            https://community.bistudio.com/wiki/TexView_2

::Folder to export PBOs to
SET exportDir=E:\Games\Arma 3 Mod Files

for /r %%I in (*.pbo) do (
	for /f "delims==" %%F in ("%%I\.\..\..") do (
	
		ECHO ====Found pbo in %%~dpnxF====
		::Create directory for MOD
		MKDIR "%exportDir%\%%~nF"
		
		::If PBO has already been extracted, skip it
		IF NOT EXIST "%exportDir%\%%~nF\%%~nI" (
			::Extract PBO contents
			PBOConsole -unpack "%%I" "%exportDir%\%%~nF\%%~nI"
			CfgConvert -txt -dst "%exportDir%\%%~nF\%%~nI\config.cpp" "%exportDir%\%%~nF\%%~nI\config.bin"
			RECYCLE -f "%exportDir%\%%~nF\%%~nI\config.bin"
			RECYCLE -f "%exportDir%\%%~nF\%%~nI\texHeaders.bin"

			::Change directory to unpacked pbo
			CD /D "%exportDir%\%%~nF\%%~nI"
			
			
			::Go through all .p3d files in directory
			FOR /R %%P in (*.p3d) do (
				::Append file to be processed
				ECHO %%P>>toRecycle.txt
			)
			::Go through files to delete processed p3d files
			for /f "tokens=*" %%a in (toRecycle.txt) do (
				::Run dep3d on p3d file to convert to mlod
				DEP3D "%%a"
				::Recycle processed file
				RECYCLE -f "%%a"
			)
			::Recycle file of files to recycle
			RECYCLE -f toRecycle.txt
			
			
			::Go through all .paa files in directory
			for /R %%f in (*.paa) do ( 
				Pal2PacE "%%f" "%%~dpnf.png"
				RECYCLE -f "%%f"
			)
			
			
			::Return to arma directory
			CD /D %~dp0
		)
		REM IF NOT EXIST <PBO>
	)
	REM for /f "delims==" %%F in ("%%I\.\..\..")
)
REM for /r %%I in (*.pbo)
PAUSE