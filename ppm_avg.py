import numpy as np
infile = open('C:/Users/user/path/colors.ppm')   
pixels = infile.read()
list=pixels.split()
ppmformat = list[0]                 #Get format    
w = int(list[1])                    #Get width    
h = int(list[2])                    #Get height
w = w//2                            #Set width and height for after blur/average
h = h//2
maxval = int(list[3])               #Get max value
    
r = np.array(list[4:-2:3])          #Add reds, greens and blues from list into array
g = np.array(list[5:-1:3])
b = np.array(list[6::3])

r = [int(x) for x in r]             #Convert string arrays to integers so it can do all the maths
g = [int(x) for x in g]
b = [int(x) for x in b]

    
avgr = []                           #Init lists
avgg = []   
avgb = []     
avgrgb = []
avgarr = []


for i in range(len(r)//2):          #Average all the colors
    index = 2 * i
    index2 = 2 * i + 1
    avgri = ((r[index] + r[index2])//2)
    avgr.append(avgri)
   
    avggi = ((g[index] + g[index2])//2)
    avgg.append(avggi)
    
    avgbi = ((b[index] + b[index2])/2)
    avgb.append(avgbi)

    
for i in range(len(avgr)):           #Merge lists
    getavg = (avgr[i])
    avgarr.append(getavg)
    getavg = (avgg[i])
    avgarr.append(getavg)
    getavg = (avgb[i])
    avgarr.append(getavg)
    
    
avgarr = np.array(avgarr)           
avgarr = [int(x) for x in avgarr]
for i in range(len(avgarr)):        #Make sure the averaged values are 255 or under
    if avgarr[i] > maxval:
        avgarr[i] = avgarr[i] - maxval
    

f = open("C:/Users/myuser/Documents/path/avgppm.ppm", "w+")        #Create, format, and write to new ppm file
f.write(ppmformat + "\n" + str(w) + " " + str(h) + "\n" + str(maxval) + "\n")

for i in range(len(avgarr)):
    f.write(str(avgarr[i]) + "\n")

f.close()


    
    