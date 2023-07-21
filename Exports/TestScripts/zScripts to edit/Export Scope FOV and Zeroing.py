import os
import ast
import sys
from decimal import *

#Set Decimal precision
getcontext().prec = 30

RHS_VERSION = "RHS_0.5.6_FixedRecoilClass"
BASEFOV = 0.75
ROUNDDIGITS = 3

with open(RHS_VERSION+" Scopes.csv", "a") as scopeFile:
	#clear file
	scopeFile.truncate(0)
	#Write header
	scopeFile.write("Scope Class,Scope Name,Scope mode,Magnification Min,Magnification Max,Zero Min,Zero Max,Scope mode,Magnification Min,Magnification Max,Zero Min,Zero Max,Scope mode,Magnification Min,Magnification Max,Zero Min,Zero Max,Scope mode,Magnification Min,Magnification Max,Zero Min,Zero Max,Scope mode,Magnification Min,Magnification Max,Zero Min,Zero Max\n")

	#Get current (working) directory
	cwd = os.getcwd()
	for root, dirs, files in os.walk(cwd + "\\" + RHS_VERSION + "\\Weapons", topdown = False):
		for file in files:
			if file.count("_acc_") > 0:
				try:
					with open(cwd + "\\" + RHS_VERSION + "\\Weapons\\" + file, "r", encoding="utf-8") as _dict:
						_scope = eval("".join(["{\n"] + _dict.readlines()[1:]))
						try:
							_opticsModes = list(_scope["iteminfo"]["opticsmodes"].keys())
							_fovs = []
							_zeros = []
							for mode in _opticsModes:
								_fovList = []
								_fetchedFOVs = [_scope["iteminfo"]["opticsmodes"][mode]["opticszoommax"],_scope["iteminfo"]["opticsmodes"][mode]["opticszoommin"]]
								for _fov in _fetchedFOVs:
									if type(_fov) is str:
										split_fov = _fov.split("/")
										#print("Double div: " + str(split_fov))
										splitDivide = Decimal(split_fov[0])/Decimal(split_fov[1])
										print("Split divide: " + str(splitDivide))
										magnification = Decimal(BASEFOV)/splitDivide
										print("Magnification = " + str(BASEFOV) + "/" + str(splitDivide))
										print("Magnificaton: " + str(magnification)+"\n-----")
									else:
										magnification = Decimal(BASEFOV)/Decimal(_fov)
									_fovList.append(round(magnification,ROUNDDIGITS))
								_zeros.append([_scope["iteminfo"]["opticsmodes"][mode]["distancezoommin"],_scope["iteminfo"]["opticsmodes"][mode]["distancezoommax"]])
								_fovs.append(_fovList)


							values=[]
							x = 0
							for mode in _opticsModes:
								values.append([_opticsModes[x],';'.join(map(str,_fovs[x])),';'.join(map(str,_zeros[x]))])
								x+=1


							scopeFile.write(file[:-3]+";"+_scope["displayname"] + ";"+ ";".join(map(str,values)).replace("[","").replace("]","") + "\n")  #";" + ''.join(map(str, _opticsModes)) + ";" + ''.join(map(str, _fovs)) + ";" + ''.join(map(str, _zeros))
						except KeyError as e:
							#print("KeyError: [" + file + "] ", str(e))
							continue
						except:
							print("Unexpected error:", sys.exc_info()[0])
							raise
				except:
					print("Unexpected error:", sys.exc_info()[0])
					raise

input("Press ENTER to exit...")
