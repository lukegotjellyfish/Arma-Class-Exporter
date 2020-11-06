# -*- coding: utf-8 -*-
import os


def writeToFile(file, root, side):
	print(file)
	fileContents = '    "' + file.replace(".py", "") + '": {\n        '
	with open(os.path.join(root, file), "r", encoding="utf-8") as catDict:
		lines = catDict.readlines()
		fileContents += '        '.join(lines)
	side.write(fileContents.replace("Â","") + "\n    }")
	return

sides = ["rhs"]
combineFiles = ["Magazines", "Vehicles","Weapons", "Glasses"]
for side in sides:
	print("Side: " + side)
	for category in combineFiles:
		print("  Category: " + category)
		# root = directory to folder
		# files = list of dicts
		cwd = os.getcwd()
		output = str(cwd) + "\\" + "Exports" + "\\" + side + category + ".py"
		print("  Output file: " + output)
		print("  Looking in: " + str(cwd) + "\\" + side + "\\" + category)
		for root, dirs, files in os.walk(cwd + "\\" + side + "\\" + category, topdown = False):
			joinedFile = ""
			with open(output, "w", encoding="utf-8") as outFile:
				folderIterate = 0
				for name in files:
					foundFile = os.path.join(root, name)
					with open(foundFile, "r", encoding="latin-1") as f:
						print("        At: " + foundFile)
						if (folderIterate > 0):
							joinedFile += ",\n"
						readLines = f.readlines()
						readLines[0] = '"' + readLines[0].replace(" = ", '": ')
						joinedFile += ''.join(readLines)
						folderIterate += 1
						outFile.write(joinedFile.replace("|", "\\\\"))  #.replace("ÃÂ","")
						joinedFile = ""
				print("      Written to " + output + "\n")


# Clear files:
open("CombinedRHS.py", 'w').close()
with open("CombinedRHS.py", "a", encoding="utf-8") as RHS:
	RHS.write("RHS = {\n")
	for root, dirs, files in os.walk("E:\\USBBACKUP\\GitHub\\Arma-Class-Exporter\\Exports\\Exports", topdown = False):
		x = 0
		for file in files:
			writeToFile(file, root, RHS)
			RHS.write(",\n")
			x += 1
	RHS.write("\n}")