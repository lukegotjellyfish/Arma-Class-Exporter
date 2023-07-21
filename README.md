# Arma-Class-Exporter
## Introduction
The main export script: RHSClassExport.sqf (Automatically export all RHS classes of specified source (see links just below))

I highly recommend running RHSClassExport.sqf on Windows for the functionality of AcceptWrites.ahk to auto-confirm the thousands of file write confirmation dialogs from make_file. However, you may be able to do the same with Wine (I haven't tested this yet).

Edit lines 26-35 accordingly to change RHSClassExport to export another mod(s) or basegame:<br>
https://community.bistudio.com/wiki/configClasses<br>
https://community.bistudio.com/wiki/configSourceMod<br>
https://community.bistudio.com/wiki/configSourceModList<br> 

The Exports folder contains the script RHSExportScript.py used to get/export details of (currently) any Weapon, Magazine, Scope or Infantry Armour for a given mod(s) exported with /Script/RHSClassExport.sqf<br>
The functionality for Vehicle parameter export is currently abandoned.

-----
## RHSClassExport Setup
make_file 32bit: http://killzonekid.com/arma-extension-make_file-dll-v1-0/<br>
make_file 64bit: http://killzonekid.com/arma-64-bit-extensions/<br>

1. Download make_file_x64 (or 32bit version) and put it in your Arma 3 directory (Where the .exe is).
2. Copy RHSClassExport.sqf and edit as described in the Introduction to modify for other mods.
3. Run regex replace //.*|/\*[\s\S\n]*\*/ with a blank replacement box to remove all comments because sqf cannot run the script with them in.
4. Set the folder to export to in *\_basePath* on line 4 (Create this folder yourself).
5. Create the folders Magazines,Vehicles,Weapons,Glasses in this folder.
6. Run your version of RHSClassExport.sqf in the debug console.
7. Run ./Script/AcceptWrites.ahk to auto-accept the make_file confirmation dialogs.
8. Customize ./Exports/RHSExportScript.py to export a CSV for the provided loadouts as shown.

## Other Notable Scripts
### ./Script/OtherScripts/*.sqf
- [**vehicle damage tracker.sqf**](https://github.com/lukegotjellyfish/Arma-Class-Exporter/blob/master/Script/OtherScripts/vehicle%20damage%20tracker.sqf)
- [Proximity projectile script.sqf](https://github.com/lukegotjellyfish/Arma-Class-Exporter/blob/master/Script/OtherScripts/Proximity%20projectile%20script.sqf)
- [ProjectileSpeedTracker.sqf](https://github.com/lukegotjellyfish/Arma-Class-Exporter/blob/master/Script/OtherScripts/ProjectileSpeedTracker.sqf)
<br>Vehicle Damage Tracker is a script that allows for full view of all damage being dealt to a vehicle.
