#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import binascii
import numpy as np

infile = open('/Users/Squibley/Documents/colors.ppm')   
readin = infile.read()
listin=readin.split()

#Get format, width, and height
ppmformat = listin[0]                 
w = int(listin[1])                    
h = int(listin[2])                  
maxval = int(listin[3])               

#Get the list of pixels
pixelList = np.array(listin[4:]) 
pixelList =  [int(x) for x in pixelList]      
maxChars = (len(pixelList)//8)

binList = []
messageOk = 0

# Get the message to encode, make sure it wont exceed the length of the picture
while(messageOk !=1):
   message = input("Enter a message:")
   if(len(message) > maxChars):
       print("Message must be shorter than " + str(maxChars))
       messageOk = 0
   else:
       messageOk = 1

# Convert the message to binary
messBin = []
for i in range(len(message)):
    getBin = bin(int.from_bytes(message[i].encode(), 'little'))[2:].zfill(8)
    messBin.append(getBin)


# Convert the picture to binary
for i in range(len(pixelList)):
    getBin = pixelList[i]
    getBin = bin(getBin)
    binList.append(getBin)


count = 0
finalList = []

# For every character in the message,
for i in range(len(messBin)):
    value = messBin[i]

    # Add the binary from the massage to the picture
    for j in range(len(value)):
        # If done adding everything, add the last binary number
        # Then add '!!' which I use to signify the end of the message
        if((i == len(messBin)-1) and (j == len(value)-1)):
            getAdded = binList[count][:-1]
            binList[count] = getAdded + ""+ value[j]
            binList[count+1] = ('!!')
   
        else:
            getAdded = binList[count][:-1]
            binList[count] = getAdded + ""+ value[j]
            count = count+1

print(binList)

# Create a new encoded image     
for i in range(len(binList)):
    if(binList[i] !='!!'):
        toInt = int(binList[i], 2)
        binList[i] = toInt            
    else:
        binList[i] = binList[i]
f = open("/Users/Squibley/Documents/encodePic2.ppm", "w+")        
f.write(ppmformat + "\n" + str(w) + " " + str(h) + "\n" + str(maxval) + "\n")

for i in range(len(binList)):
    f.write(str(binList[i]) + "\n")
f.close()



