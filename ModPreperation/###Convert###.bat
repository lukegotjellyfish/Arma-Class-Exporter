for /r %%I in (config.bin) do (
	CD %%~pI
	@IF EXIST %%I CfgConvert -txt -dst "config.cpp" "config.bin"
	CD %~dp0
)