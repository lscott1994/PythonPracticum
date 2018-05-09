#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np


def getBox(w, h, list):
    count = 1
    color = list[w][h]
    col = len(list) - 1
    row = len(list[0]) - 1
    # The tries basically account for the pixels on the edge of the picture
    # Since they're on the edge, they have less neighbors to average
    # For every neighboring pixel, that neighbor's color is added to the total color and count __
    # At the end, it gets the average with the total color and count.

        
        
    # If top middle index exists    
    try:
        list[w][h-1]
        if(h-1 < 0): raise IndexError()
        currColor = list[w][h-1]
        color = color + currColor
        count = count + 1
    except IndexError:
        color = color
        
   

    #Index left of current   
    try:
        list[w-1][h]
        if(w-1 < 0): raise IndexError()
        currColor = list[w-1][h]
        color = color + currColor
        count = count + 1
    except IndexError:
        color = color
               
 
    # Index right of current
    try:
        list[w+1][h]
        if(w+1 > row): raise IndexError()
        currColor = list[w+1][h]
        color = color + currColor
        count = count + 1
    except IndexError:
        color = color


    # Index bottom middle    
    try:
        list[w][h+1]
        if(h+1 > col): raise IndexError()
        currColor = list[w][h+1]
        color = color + currColor
        count = count + 1
    except IndexError:
        color = color   
      

    averagedColor = (color/count)
    return averagedColor




def setBlur(w, h, list, avgColor):
    colorList = list
    col = len(list) - 1
    row = len(list[0]) - 1
    colorList[w][h] = avgColor
    
    # This function just takes the average value calculated from getBox
    # And sets the value of the neighboring pixels to that calculated value


        
    # If top middle index exists    
    try:
        colorList[w][h-1]
        if(h-1 < 0): raise IndexError()
        colorList[w][h-1] = avgColor
    except IndexError:
        avgColor = avgColor


    #Index left of current   
    try:
        colorList[w-1][h]
        if(w-1 < 0): raise IndexError()
        colorList[w-1][h] = avgColor
    except IndexError:
       avgColor = avgColor        
 
    # Index right of current
    try:
        colorList[w+1][h]
        if(w+1 > row): raise IndexError()
        colorList[w+1][h] = avgColor
    except IndexError:
        avgColor = avgColor


    # Index bottom middle    
    try:
        colorList[w][h+1]
        if(h+1 > col): raise IndexError()
        colorList[w][h+1] = avgColor
    except IndexError:        
        avgColor = avgColor            

       
          
    return colorList

#Read in file, get width, height, the format, and the max value
infile = open('/Users/Squibley/Documents/colors.ppm')   
pixels = infile.read()
list=pixels.split()
ppmformat = list[0]                   
w = int(list[1])                     
h = int(list[2])                    
maxval = int(list[3])               

#Add reds, greens, and blues from list into array
r = np.array(list[4:-2:3])          
g = np.array(list[5:-1:3])
b = np.array(list[6::3])
r = [int(x) for x in r]             
g = [int(x) for x in g]
b = [int(x) for x in b]
 
red = [[0 for x in range(w)] for y in range(h)] 
green = [[0 for x in range(w)] for y in range(h)] 
blue = [[0 for x in range(w)] for y in range(h)] 

#Format the arrays into 2d for easier readability/manipulation
for i in range(h):
    for j in range(w):
        index = ((i * w) + j)
        red[j][i] = r[index]
        green[j][i] = g[index]
        blue[j][i] = b[index]
avgList = []       
#Averages the color depending on that pixels immediate neighboring pixels
for i in range(h//2):
    for j in range(w//2):
        avgColor = getBox(j, i, red)
        avgList.append(avgColor)
        
        avgColor = getBox(j, i, green)
        avgList.append(avgColor)
        
        avgColor = getBox(j, i, blue)
        avgList.append(avgColor)



    
#Make sure the averaged values are 255 or under
avgList = np.array(avgList)           
avgList = [int(x) for x in avgList]
for i in range(len(avgList)):        
    if avgList[i] > maxval:
        avgList[i] = avgList[i] - maxval
        
#Write new PPM file    
f = open("/Users/Squibley/Documents/colorsBox.ppm", "w+")        
f.write(ppmformat + "\n" + str(w/2) + " " + str(h//2) + "\n" + str(maxval) + "\n")

for i in range(len(avgList)):
    f.write(str(avgList[i]) + "\n")
f.close()