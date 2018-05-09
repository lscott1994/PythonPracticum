#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  8 16:54:33 2018

@author: Squibley
"""

import numpy as np

# Reads in ppm file, gets the format, width, height, and max value
infile = open('/Users/Squibley/Documents/colors.ppm')   
pixels = infile.read()
list=pixels.split()
ppmformat = list[0]                     
w = int(list[1])                       
h = int(list[2])                    
w = w//2                            
h = h//2
maxval = int(list[3])               

#Add reds, greens, and blues from list into array
r = np.array(list[4:-2:3])          
g = np.array(list[5:-1:3])
b = np.array(list[6::3])

#Convert string arrays to integers so it can do all the maths
r = [int(x) for x in r]             
g = [int(x) for x in g]
b = [int(x) for x in b]

#Init lists
avgr = []     
avgrcol = []                      
avgg = []   
avggcol = []
avgb = []     
avgbcol = []
avgrgb = []
avgrgbcol = []
avgarr = []

#Average all the colors horizontally
for i in range(len(r)//2):          
    index = 2 * i
    index2 = 2 * i + 1
    avgri = ((r[index] + r[index2])//2)
    avgr.append(avgri)
   
    avggi = ((g[index] + g[index2])//2)
    avgg.append(avggi)

    avgbi = ((b[index] + b[index2])/2)
    avgb.append(avgbi)

#Average all the colors vertically
for i in range(len(avgr)//2):
    irow = w + i    
    avgrrow = ((avgr[i] + avgr[irow])//2)
    avgtotr = ((avgr[i] + avgrrow)//2)
    avgrcol.append(avgtotr)
    
    avggrow = ((avgg[i] + avgg[irow])//2)
    avgtotg = ((avgg[i] + avggrow)//2)
    avggcol.append(avgtotg)
    
    avgbrow = ((avgb[i] + avgb[irow])//2)
    avgtotb = ((avgb[i] + avgbrow)//2)
    avgbcol.append(avgtotb)
    
#Merge lists    
for i in range(len(avgrcol)):           
    getavg = (avgrcol[i])
    avgarr.append(getavg)
    getavg = (avggcol[i])
    avgarr.append(getavg)
    getavg = (avgbcol[i])
    avgarr.append(getavg)
    
#Make sure the averaged values are 255 or under    
avgarr = np.array(avgarr)           
avgarr = [int(x) for x in avgarr]
for i in range(len(avgarr)):        
    if avgarr[i] > maxval:
        avgarr[i] = avgarr[i] - maxval
        
#Create, format, and write to new ppm file    
f = open("/Users/Squibley/Documents/colorsAveraged.ppm", "w+")        
f.write(ppmformat + "\n" + str(w) + " " + str(h) + "\n" + str(maxval) + "\n")

for i in range(len(avgarr)):
    f.write(str(avgarr[i]) + "\n")
f.close()