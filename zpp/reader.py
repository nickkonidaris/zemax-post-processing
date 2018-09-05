

from astropy import units as uu
import numpy as np
import os


def read_image_analysis(filename):
    """ Read a Zemax `Image Analysis Histogram' file """

    f = open(filename, encoding="utf-16")
    lines = f.readlines()
    f.close()

    preamble = "Image analysis histogram listing\n"

    if lines[0] != preamble:
        raise Exception("Not an image analysis file, should start with:\n%s \n "
                        "but start with: \n%s" % (preamble, lines[0]))

    meta = {}
    for line in lines:
        sp = line.strip().split(":")
        if len(sp) == 2:
            key = sp[0].strip()
            key = key.replace(" ", "_")
            val = sp[1].lstrip()
            val = val.replace("Millimeters", "mm")
            val = val.replace("mm squared", "mm2")
            val = val.replace("Watts", "1 watt")


            try:
                val = uu.Quantity(val)
            except ValueError:
                print(val)
                pass
            except TypeError:
                pass
            meta[key] = val

            if key == "Number_of_pixels":
                sp = val.split("x")
                val = tuple(map(int, sp))
                meta[key] = val

    print(meta)
    width, height = meta["Number_of_pixels"]

    img = np.zeros((width, height))
    print(width,height)

    i = 0
    for line in lines:
        sp = line.strip().split("\t")
        if len(sp) == width:
            img[i, :] = np.array(sp)
            i+=1


    return meta, img





""" E.g. Image analysis histogram listing:
Image analysis histogram listing

File : path to file
Title: Title
Date : 9/4/2018
Configuration 2 of 4

Field Width                    : 0.117 Millimeters
Image Width                    : 0.09 Millimeters
Number of pixels               : 250 x 250
Total Weight of Rays Attempted :   5.004125E+06
Total Weight of Rays Passed    :   4.978420E+06
Total Rays Launched            : 5004125
Percent Efficiency             :   99.49 %
Total flux in watts            : 9.949E-01
Units                          : Watts/Millimeters squared
"""

