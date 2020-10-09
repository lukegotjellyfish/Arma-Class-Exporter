import os


def writeToFile(file, root, side):
	print(file)
	fileContents = '    "' + file.replace(".py", "") + '": {\n'
	with open(os.path.join(root, file), "r", encoding="latin-1") as catDict:
		lines = catDict.readlines()
		for line in lines:
			fileContents += "        " + line
	side.write(fileContents + "\n    }")
	return

sides = ["BluFor", "OpFor"]
combineFiles = ["LauncherMagazines", "Launchers", "Magazines", "VehicleMagazines", "Vehicles", "VehicleWeapons", "Weapons", "Uniforms", "Backpacks", "Glasses"]
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
				outFile.write(joinedFile.replace("|", "\\\\"))
				print("      Written to " + output + "\n")


# Clear files:
open("CombinedBluFor.py", 'w').close()
open("CombinedOpFor.py", 'w').close()
with open("CombinedBluFor.py", "a", encoding="utf-8") as BluFor,  open("CombinedOpFor.py", "w", encoding="utf-8") as OpFor:
	for root, dirs, files in os.walk(cwd + "\\" + "Exports", topdown = False):
		x = 0
		onBlu = 0
		onOpf = 0
		for file in files:

			if file[:3] == "Blu":
				if (onBlu == 0):
					onBlu = 1
					BluFor.write("BluFor = {\n")

				writeToFile(file, root, BluFor)

				if (files[x+1][:3] == "Blu"):
					BluFor.write(",")
				BluFor.write("\n")

			if file[:2] == "Op":
				if (onOpf == 0):
					onOpf = 1
					OpFor.write("OpFor = {\n")

				writeToFile(file, root, OpFor)

				if (file != files[len(files)-1]):
					OpFor.write(",")
				OpFor.write("\n")

				if (onBlu == 1):
					onBlu = 0
					BluFor.write("}")

			x += 1
	OpFor.write("}")