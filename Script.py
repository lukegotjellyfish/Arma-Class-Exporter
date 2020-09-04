#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import errno


os.system("")

cred     = '\033[91m'
cgreen   = '\33[32m'
cgrey    = '\33[90m'
cviolet2 = '\33[95m'

cbold    = '\33[1m'

cend     = '\033[0m'


def newFile(root, file, logfile):
	with open(root + "\\\\" + file, "r", encoding="UTF-8") as f:
		lines = f.readlines()

	modDir = re.search("@[^\\\\]*", root).group(0)
	folder = re.search("addons\\\\[^\\\\]*", root).group(0).replace("addons\\","")

	logfile.write("-------------------------------" + folder + "-------------------------------")
	print(cviolet2 + "-------------------------------" + cend + (cgreen + cbold + folder + cend) + cviolet2 + "-------------------------------" + cend)

	pathToCreate = "Mods\\" + modDir + "\\" + folder + "\\"
	fileToCreate = pathToCreate + "\\" + file

	if not os.path.exists(os.path.dirname(pathToCreate)):
		try:
			os.makedirs(os.path.dirname(pathToCreate))
		except OSError as exc:
			if exc.errno != errno.EEXIST:
				raise

	with open(fileToCreate, "w", encoding="UTF-8") as writeToThisFile:
		for line in lines:
			writeToThisFile.write(line)


mods = ["S:\\Steam\\steamapps\\common\\Arma 3\\!Workshop\\@RHSAFRF",
		"S:\\Steam\\steamapps\\common\\Arma 3\\!Workshop\\@RHSUSAF",
		"S:\\Steam\\steamapps\\common\\Arma 3\\!Workshop\\@RHSGREF",
		"S:\\Steam\\steamapps\\common\\Arma 3\\!Workshop\\@RHSSAF"]

with open("logfile.txt", "w", encoding="utf-8") as logfile:
	for x in mods:
		for root, dirs, files in os.walk(x):
			for file in files:
				if file == 'config.cpp':
					newFile(root, file, logfile)


#\n^\s*$  blanknewline





















#Tried using MySQL because why and why not
#There is literally no reason for me trying this, it would require faux sub-tables,
 #something I didn't even try although now I think about it - it sounds really good

#Database for each 
#Parent mod: table

"""
	modLine = re.search("@.*", filePath).group(0).split("\\")
	modName = modLine[0].replace("@","").lower()
	addonName = modLine[2].lower()

	cursor.execute("DROP database IF EXISTS " + modName)
	cursor.execute("CREATE DATABASE " + modName)

	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		password="rootpass",
		database=modName
	)
	cursor = mydb.cursor()

	cursor.execute("DROP TABLE IF EXISTS " + addonName)
	cursor.execute("CREATE TABLE " + addonName + " (id INT AUTO_INCREMENT PRIMARY KEY, line VARCHAR(5000), type VARCHAR(10))")

	for item in classList:
		sql = "INSERT INTO " + addonName + " (id, line, type) VALUES (%s, %s, %s)"
		val = (item, lines[item], "class")
		cursor.execute(sql, val)

	for item in attributeList:
		print(item)
		try:
			if item[0] == -1:
				for x in item:
					if x == -1: continue
					sql = "INSERT INTO " + addonName + " (id, line, type) VALUES (%s, %s, %s)"
					val = (x, lines[x], "attribute")
					cursor.execute(sql, val)
				continue
		except TypeError:
			pass
		sql = "INSERT INTO " + addonName + " (id, line, type) VALUES (%s, %s, %s)"
		val = (item, lines[item], "attribute")
		cursor.execute(sql, val)
	mydb.commit()
"""