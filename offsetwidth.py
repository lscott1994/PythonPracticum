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

maxval = int(pixellist[3])               #Get max value

r = np.array(pixellist[4:-2:3])          #Add reds, greens and blues from list into array
g = np.array(pixellist[5:-1:3])
b = np.array(pixellist[6::3])

r = [float(x) for x in r]           #Convert string arrays to integers so it can do all the maths
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
avgarr = [int(x) for x in avgarr]
for i in range(len(avgarr)):        #Make sure the averaged values are 255 or under
    if avgarr[i] > maxval:
        avgarr[i] = avgarr[i] - maxval

w = w//2
getimg = []

print(avgarr)
print("")
print(offsetarr)
print("")

#print(len(avgarr)//3)

temp = []
getcolor = w * 3


#loop with height #of times, inside loop put together the half the loops 

for i in range (h):
    for j in range(w):
        index = (i * w * 3) + (j*3)
        temp.append(avgarr[index])
        temp.append(avgarr[index+1])
        temp.append(avgarr[index+2])
    for j in range(w):
        index = (i * w * 3) + (j*3)
        temp.append(offsetarr[index]+127.5)
        temp.append(offsetarr[index+1]+127.5)
        temp.append(offsetarr[index+2]+127.5)
  
f = open("C:/Users/lscot/Documents/offset.ppm", "w+")        #Create, format, and write to new ppm file
f.write(ppmformat + "\n" + str(w*2) + " " + str(h) + "\n" + str(maxval) + "\n")

for i in range(len(temp)):
    f.write(str(temp[i]) + "\n")

f.close()