# -*- coding: utf-8 -*-
import re
import os
import csv
import rhs_200rnd_556x45_B_SAW as rhs


def getAttrib(attrib):
    try:
        return rhs.rhs_200rnd_556x45_B_SAW[attrib]
    except:
        print("Failed to find a match")
        return attrib


print(getAttrib("ammo"), getAttrib("caliber"))