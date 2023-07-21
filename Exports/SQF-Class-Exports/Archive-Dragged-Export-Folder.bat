@ECHO OFF

For /f "tokens=1-2 delims=/:" %%a in ('time /t') do (set sanitisedTime=%%a;%%b)
7z a "%1_%date:~0,2%-%date:~3,2%-%date:~6,4%_%sanitisedTime%" "%1" -xr!__pycache__