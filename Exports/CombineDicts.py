# -*- coding: utf-8 -*-
import os


def writeToFile(file, root, side):
	print(file)
	fileContents = '    "' + file.replace(".py", "") + '": {\n'
	with open(os.path.join(root, file), "r", encoding="utf-8") as catDict:
		lines = catDict.readlines()
		for line in lines:
			fileContents += "        " + line.replace("Â","")
	side.write(fileContents + "\n    }")
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
				print("      Written to " + output + "\n")


# Clear files:
open("CombinedRHS.py", 'w').close()
with open("CombinedRHS", "a", encoding="utf-8") as RHS:
	for root, dirs, files in os.walk(cwd + "\\" + "Exports", topdown = False):
		x = 0
		for file in files:
			RHS.write("RHS = {\n")

			writeToFile(file, root, RHS)

			if (files[x+1][:3] == "Blu"):
				RHS.write(",")
			RHS.write("\n")

			x += 1
	RHS.write("}")