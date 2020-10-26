# Arma-Class-Exporter
 Currently set up for RHS vehicles and weapons used on the C4G V14 RHS KotH server:<br>
 Name: CodeFourGaming - King Of The Hill RHS Vics US #5 (and "- King of the Hill - RHS Inf No Towers EU #3 HC" by extension)<br>
 IP: 158.69.123.61:2402<br>
 Restart: 18:00 UTC+0<br>
 Mods: https://steamcommunity.com/sharedfiles/filedetails/?id=1290398866<br>
<br>
make_file 32bit: http://killzonekid.com/arma-extension-make_file-dll-v1-0/<br>
make_file 64bit: http://killzonekid.com/arma-64-bit-extensions/<br>

1. Download make_file_x64 (or 32bit version) and put it in your Arma 3 directory (Where the .exe is)
2. Run ./Exports/Create folders.bat to create directories to write to
3. Change "\_basePath" directory in ./Script/ClassExport.sqf on line 840 to the full path of where your "Exports" folder is, with the same formatting
4. Edit "\_sideMatrix" to your liking, each sub-array contains a category, each array in this category is for a faction, in this the first item is the folder to write to and the second item is the CfgFile the class is under in Arma
5. Copy and run ClassExport.sqf ingame, use AcceptWrites.ahk (install AHK at https://www.autohotkey.com/) or manually accept write-to-file prompts from make_file(\_x64).dll
6. Run ./Exports/Run CombineDicts.py.bat to get two .py dicts for BluFor and OpFor (or edit for more factions)
7. Run ./Exports/Script.py to get a csv export for BluFor and OpFor (or edit to select specific classes to export from CombinedBluFor.py and/or CombinedOpFor.py

The dict files for each side are for more extensive writing of all classes for Script.py to then extract the data needed for writing to CSV file. They are currently set-up for creating two CSV files for relevant infantry (not launchers or uniforms yet) weapons at https://docs.google.com/spreadsheets/d/15aMgHLaf82euwx455wdVyjPHwko8tDf93RkpLejiQrE
