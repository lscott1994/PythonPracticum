import numpy as np


infile = open('C:/Users/lscot/Documents/colors.ppm')   
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
 
avgr = []     
avgrcol = []                      #Init lists
avgg = []   
avggcol = []
avgb = []     
avgbcol = []
avgrgb = []
avgrgbcol = []
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
    
    
for i in range(len(avgrcol)):           #Merge lists
    getavg = (avgrcol[i])
    avgarr.append(getavg)
    getavg = (avggcol[i])
    avgarr.append(getavg)
    getavg = (avgbcol[i])
    avgarr.append(getavg)
    
    
avgarr = np.array(avgarr)           
avgarr = [int(x) for x in avgarr]
for i in range(len(avgarr)):        #Make sure the averaged values are 255 or under
    if avgarr[i] > maxval:
        avgarr[i] = avgarr[i] - maxval
    
f = open("C:/Users/lscot/Documents/2davg.ppm", "w+")        #Create, format, and write to new ppm file
f.write(ppmformat + "\n" + str(w) + " " + str(h) + "\n" + str(maxval) + "\n")

for i in range(len(avgarr)):
    f.write(str(avgarr[i]) + "\n")
f.close()







    