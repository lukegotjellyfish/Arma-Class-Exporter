@echo off

ECHO New Export Folder Name:
SET /P FOLDER_NAME="> "

MKDIR %FOLDER_NAME%\Magazines
MKDIR %FOLDER_NAME%\Vehicles
MKDIR %FOLDER_NAME%\Weapons
MKDIR %FOLDER_NAME%\Glasses
MKDIR %FOLDER_NAME%\Ammo