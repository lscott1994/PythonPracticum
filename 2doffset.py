# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 22:02:42 2018

@author: lscot
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 16:36:38 2018

@author: lscot
"""

import numpy as np

infile = open('C:/Users/lscot/Documents/preoffset.ppm')   
readin = infile.read()
pixellist=readin.split()
ppmformat = pixellist[0]                 #Get format    
w = int(pixellist[1])                    #Get width    
h = int(pixellist[2])                    #Get height
maxval = float(pixellist[3])             #Get max value
r = np.array(pixellist[4:-2:3])          #Add reds, greens and blues from list into array
g = np.array(pixellist[5:-1:3])
b = np.array(pixellist[6::3])

r = [float(x) for x in r]                #Convert string arrays to integers so it can do all the maths
g = [float(x) for x in g]
b = [float(x) for x in b]

    
avgr = []     
avgrcol = []                        #Init lists
avgg = []   
avggcol = []
avgb = []     
avgbcol = []
avgrgb = []
avgrgbcol = []
avgarr = []
offsetr = []
offsetg = []
offsetb = []
offsetarr = []

for i in range(len(r)//2):         #Average all the colors
    index1= 2 * i
    index2 = 2 * i + 1  
  
    avgri = ((r[index1] + r[index2])/2)
    avgr.append(avgri)
    offr = (avgri - r[index2])
    offsetr.append(offr)

    avggi = ((g[index1] + g[index2])/2)
    avgg.append(avggi)
    offg = (avggi - g[index2])
    offsetg.append(offg)

    avgbi = ((b[index1] + b[index2])/2)
    avgb.append(avgbi)
    offb = (avgbi - b[index2])
    offsetb.append(offb)
  
for i in range(len(avgr)):           #Merge lists
    getavg = (avgr[i])
    avgarr.append(getavg)
    getavg = (avgg[i])
    avgarr.append(getavg)
    getavg = (avgb[i])
    avgarr.append(getavg)
   
for i in range(len(offsetr)):
    getoset = (offsetr[i])
    offsetarr.append(getoset)
    
    getoset = (offsetg[i])
    offsetarr.append(getoset)

    getoset = (offsetb[i])
    offsetarr.append(getoset)
   
avgarr = np.array(avgarr)           
avgarr = [float(x) for x in avgarr]
for i in range(len(avgarr)):        #Make sure the averaged values are 255 or under
    if avgarr[i] > maxval:
        avgarr[i] = avgarr[i] - maxval

w = w//2
temp = []
getcolor = w * 3

for i in range (h):
    for j in range(w):
        index = (i * w * 3) + (j*3)
        temp.append(avgarr[index])
        temp.append(avgarr[index+1])
        temp.append(avgarr[index+2])
    for j in range(w):
        index = (i * w * 3) + (j*3)
        temp.append(offsetarr[index])
        temp.append(offsetarr[index+1])
        temp.append(offsetarr[index+2])

w = ((w * 2)*3)
for j in range(w):
    row1 = j
    row2 = (j + w)
    row3 = (j + (w*2))
    row4 = (j + (w*2) + w)
    
    avg1 = ((temp[j] + temp[row2])/2)
    avg2 = ((temp[row3] + temp[row4])/2)
    off1 = (avg1 - temp[row2])
    off2 = (avg2 - temp[row4])

    temp[row1] = avg1
    temp[row2] = avg2
    temp[row3] = off1
    temp[row4] = off2 
      
f = open("C:/Users/user/Documents/2doffset.ppm", "w+")        #Create, format, and write to new ppm file
f.write(ppmformat + "\n" + str(w/3) + " " + str(h) + "\n" + str(maxval) + "\n")

for i in range(len(temp)):
    f.write(str(temp[i]) + "\n")

f.close()
    
    