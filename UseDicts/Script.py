# -*- coding: utf-8 -*-
import re
import os
import csv
import BluForMagazines


def getAttrib(a, b):
    try:
        return BluForMagazines.BluFor_Magazines[a][b]
    except:
        print("Failed to find a match")
        return "failed"


print(getAttrib("rhs_200rnd_556x45_B_SAW", "author"))