# # -*- coding: utf-8 -*-
# import os


# def writeToFile(file, root, side):
# 	print(file)
# 	fileContents = '    "' + file.replace(".py", "") + '": {\n        '
# 	with open(os.path.join(root, file), "r", encoding="utf-8") as catDict:
# 		lines = catDict.readlines()
# 		fileContents += '        '.join(lines)
# 	side.write(fileContents.replace("Â","") + "\n    }")
# 	return

# combineFiles = ["Magazines", "Vehicles","Weapons", "Glasses"]
# for category in combineFiles:
# 	print("  Category: " + category)
# 	# root = directory to folder
# 	# files = list of dicts
# 	cwd = os.getcwd()
# 	_dir = "\\" + "RHS 0.5.5" + "\\" + category
# 	output = str(cwd) + _dir + ".py"
# 	print("  Output file: " + output)
# 	print("  Looking in: " + str(cwd) + _dir)
# 	for root, dirs, files in os.walk(cwd + _dir, topdown = False):
# 		joinedFile = ""
# 		with open(output, "w", encoding="utf-8") as outFile:
# 			folderIterate = 0
# 			for name in files:
# 				foundFile = os.path.join(root, name)
# 				with open(foundFile, "r", encoding="latin-1") as f:
# 					print("        At: " + foundFile)
# 					if (folderIterate > 0):
# 						joinedFile += ",\n"
# 					readLines = f.readlines()
# 					readLines[0] = '"' + readLines[0].replace(" = ", '": ')
# 					joinedFile += ''.join(readLines)
# 					folderIterate += 1
# 					outFile.write(joinedFile.replace("|", "\\\\"))  #.replace("ÃÂ","")
# 					joinedFile = ""
# 			print("      Written to " + output + "\n")

# -*- coding: utf-8 -*-
import os


def writeToFile(file, root, side):
	print("          writeToFile: " + file)
	fileContents = '    "' + file.replace(".py", "") + '": {\n        '
	with open(os.path.join(root, file), "r", encoding="utf-8") as catDict:
		lines = catDict.readlines()
		fileContents += '        '.join(lines)
	side.write(fileContents.replace("Â","") + "\n    }")
	return


RHS_FOLDER = "RHS 0.5.5"
combineFiles = ["Magazines", "Vehicles","Weapons", "Glasses"]
for category in combineFiles:
	print("  Category: " + category)
	# root = directory to folder
	# files = list of dicts
	cwd = os.getcwd()
	output = str(cwd) + "\\" + RHS_FOLDER + "\\" + category + ".py"
	print("  Output file: " + output)
	print("  Looking in: " + str(cwd) + "\\" + "\\" + category)
	for root, dirs, files in os.walk(cwd + "\\" + "\\" + category, topdown = False):
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
with open("CombinedRHS.py", "a", encoding="utf-8") as rhs:
	for root, dirs, files in os.walk(cwd + "\\" + RHS_FOLDER, topdown = False):
		rhs.write("RHS = {\n")
		for file in files:
			writeToFile(file, root, rhs)
			rhs.write(",\n")
		rhs.write("}")