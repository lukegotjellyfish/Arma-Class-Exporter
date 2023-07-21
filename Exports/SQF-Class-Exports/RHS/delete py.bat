@echo off

for /r %%I in (*.py) do (
	DEL %%I
)
for /r %%I in (*.pyc) do (
	DEL %%I
)