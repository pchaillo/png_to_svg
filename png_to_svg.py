#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 16:31:46 2022

@author: pchaillo

"""
import os

#import nest_asyncio
#nest_asyncio.apply()
#__import__('IPython').embed()

from pathlib import Path
from svgtrace import trace

folder_name = 'img_to_convert'
new_folder = 'converted_img'
liste = os.listdir('./' + folder_name)
print(liste)

# récupère la localisation des fichiers
THISDIR = str(Path(__file__).resolve().parent)

# rows = read_csv_file('./'+folder_name+'/'+liste[i])

l = len(liste)
for i in range(l):

        raw = liste[i].split(".")

        print(raw[1])

        if raw[1] == "png" :
                bw = open(THISDIR + "/" + new_folder + "/" + raw[0]+".svg", "w")
                bw.write(trace(THISDIR + "/" + folder_name + "/" + liste[i], True))
                bw.close()
                colour = open(THISDIR + "/" + new_folder + "/" + raw[0]+".svg", "w")
                colour.write(trace(THISDIR + "/" + folder_name + "/" + liste[i]))
                colour.close()


# # converti le png en svg (bitmap trace equivalent)
# bw = open(THISDIR + "/" + folder_name + "/" + liste[i], "w")
# bw.write(trace(THISDIR + "/loutre_1p.png", True))
# bw.close()
# colour = open(THISDIR + "/loutre_1p_new.svg", "w")
# colour.write(trace(THISDIR + "/loutre_1p.png"))
# colour.close()

