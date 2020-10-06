@echo off

CD BluFor
for /r %%i in (*.cpp *.py) do recycle "%%i"
CD ..\
CD OpFor
for /r %%i in (*.cpp *.py) do recycle "%%i"

PAUSE