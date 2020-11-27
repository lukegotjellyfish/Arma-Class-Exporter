for /r %%i in (*.pbo) do PBOConsole -unpack "%%i" "./%%~ni"

for /r %%I in (config.bin) do (
	CD %%~pI
	@IF EXIST %%I CfgConvert -txt -dst "config.cpp" "config.bin"
	CD %~dp0
)