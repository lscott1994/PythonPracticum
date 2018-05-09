import numpy as np
from itertools import *

def toRLE(getPixels):
    count = 0
    getList = []
    lastIndex = len(getPixels) - 1
    
    #Gets value from index and compares to next index
    #If they have the same value, count goes up by 1
    # When the index doesn't have the same value as the next index
    # Then add the index's count and value to a list
    for i in range(len(getPixels)):
        if(i != lastIndex):
            if(getPixels[i] != getPixels[i+1]): 
                if(i == 0 ):
                    count = 1
                    getList.append([str(count), str(getPixels[i])])
          
                else: 
                    getList.append([str(count), str(getPixels[i])])
                    count = 1
            else:
                count = count + 1
        else: 
            getList.append([str(count), str(getPixels[i])])
 
    return getList
    
def toPPM(getList):
    ppmList =[]
    #Iterates through the RLE
    #Adds the value of index to list for the number of times 'repeat' says to
    for i in range(len(getList)):
        repeat = getList[i][0]
        value = getList[i][1]
        for j in range(int(repeat)):
            ppmList.append(value)          
    return ppmList
     

   
infile = open('/Users/Squibley/Documents/sampleppm.ppm')   
readin = infile.read()
listin=readin.split()

#Get format, width, and height
ppmformat = listin[0]                 
w = int(listin[1])                    
h = int(listin[2])                  
maxval = int(listin[3])               

#Get list of pixels
pixelList = np.array(listin[4:])         
pixelList = [int(x) for x in pixelList]            

# Produces RLE from file
getList = toRLE(pixelList)

# Takes RLE and returns list of pixels
decodedList = toPPM(getList)

#Create, format, and write to new ppm file
f = open("C:/Users/myuser/Documents/path/RWVfromRLE.ppm", "w+")        
f.write(ppmformat + "\n" + str(w) + " " + str(h) + "\n" + str(maxval) + "\n")

for i in range(len(decodedList)):
    f.write(str(decodedList[i]) + "\n")

f.close()

print(getList)
print(decodedList)