# -*- coding: utf-8 -*-
import re
import os
import csv
import BluFor_Magazines


def getAttrib(a, b):
    try:
        return BluFor_Magazines.BluFor_Magazines[a][b]
    except:
        print("Failed to find a match")
        return "failed"


print(getAttrib("rhs_200rnd_556x45_B_SAW", "author"))