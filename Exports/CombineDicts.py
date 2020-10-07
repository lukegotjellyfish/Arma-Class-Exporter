import os


def writeToFile(file, root, side, left):
	print(file)
	fileContents = '"' + file.replace(".py", "") + '" = {\n'
	with open(os.path.join(root, file), "r", encoding="latin-1") as catDict:
		lines = catDict.readlines()
		for line in lines:
			if line == lines[0]:
				fileContents += "    " + line.replace(" =", ":")
			else:
				fileContents += "    " + line
	fileContents += "\n}"
	if (left == 1):
		fileContents += ","
	fileContents += "\n"
	side.write(fileContents)
	return

sides = ["BluFor", "OpFor"]
combineFiles = ["LauncherMagazines", "Launchers", "Magazines", "VehicleMagazines", "Vehicles", "VehicleWeapons", "Weapons"]
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
				ignore = 0
				for name in files:
					foundFile = os.path.join(root, name)
					with open(foundFile, "r", encoding="latin-1") as f:
						print("        At: " + foundFile)
						if (name[:3].lower() == "rhs"):
							if (folderIterate > 0):
								if (name != files[len(files) - 1]):
									joinedFile += ","
								else:
									if (ignore > 0):
										joinedFile += ","
										ignore -= 1
								joinedFile += "\n"
							joinedFile += ''.join(f.readlines())
							folderIterate += 1
						else:
							ignore += 1
						print("        Ignore level: " + str(ignore))
				outFile.write(joinedFile.replace("|", "\\\\"))
				print("      Written to " + output + "\n")


# Clear files:
open("CombinedBluFor.py", 'w').close()
open("CombinedOpFor.py", 'w').close()
with open("CombinedBluFor.py", "a", encoding="utf-8") as BluFor,  open("CombinedOpFor.py", "w", encoding="utf-8") as OpFor:
	for root, dirs, files in os.walk(cwd + "\\" + "Exports", topdown = False):
		x = 0
		for file in files:
			if file[:2] == files[x][:2]:
				left = 1
			else:
				left = 0
			if file[:3] == "Blu":
				writeToFile(file, root, BluFor, left)
			if file[:2] == "Op":
				writeToFile(file, root, OpFor, left)
			x += 1

	BluFor.write

input("HALT")