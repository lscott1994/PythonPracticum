#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import binascii
import numpy as np


infile = open('/Users/Squibley/Documents/encodePic2.ppm')   
readin = infile.read()
listin=readin.split()

#Get format, width, and height
ppmformat = listin[0]                 
w = int(listin[1])                    
h = int(listin[2])                  
maxval = int(listin[3])               

listin = listin[4:]

#Get the list of pixels
pixelList = [] 
getKey = 0

for iter in range(len(listin)):
    
    while(getKey != 1):
        if(listin[iter] != "!!"):
            pixelList.append(listin[iter])
            print(listin[iter])
            getKey = 0
            iter = iter + 1
        else:
            getKey = 1
        
     
getMessage = []


# Get the picture and convert to binary
for i in range(len(pixelList)):

    if(binary != '!!'):
        binary = bin(int(pixelList[i]))[2:]
        getMessage.append(binary)
    else:
        break
 
    

# Get just the single digit for the message
for i in range(len(getMessage)):
    getStr = int(len(getMessage[i]))
    if(getStr == 1):
        getMessage[i] = getMessage[i]
    if(getStr < 9):
        getInt = getMessage[i][getStr-1:]
        getMessage[i] = getInt
    if(getStr == 9):
        getint = 1
        getMessage[i] = getInt


combineMess = []

# Combine the digits to get binaries to decode the message
for i in range(len(getMessage)//8):
    combineStr = ""
    for j in range(8):
        combineStr = combineStr + "" + getMessage[j + (i*8)]
    combineMess.append(combineStr)
 
message = ""
# Convert the bianries back to ASCII and decode the message!
for i in range(len(combineMess)):
    message = message + chr(int(combineMess[i],2))

print("The message is: " + message)