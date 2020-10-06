import os

sides = ["BluFor", "OpFor"]
combineFiles = ["LauncherMagazines", "Launchers", "Magazines", "VehicleMagazines", "Vehicles", "VehicleWeapons", "Weapons"]
for side in sides:
	for category in combineFiles:
		# root = directory to folder
		# files = list of dicts
		output = str(os.getcwd()) + "\Exports\\" + side + "\\" + category + "\\" + category + ".py"
		for root, dirs, files in os.walk(os.getcwd() + "\Exports\\" + side + "\\" + category, topdown = False):
			joinedFile = ""
			with open(output, "w", encoding="utf-8") as outFile:
				folderIterate = 0
				ignore = 0
				for name in files:
					foundFile = os.path.join(root, name)
					with open(foundFile, "r", encoding="latin-1") as f:
						print("At: " + foundFile)
						print("Ignore level: " + str(ignore))
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
				outFile.write(joinedFile)
			print("Written to " + output)