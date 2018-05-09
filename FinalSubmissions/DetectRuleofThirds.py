#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 16:33:25 2018

@author: Squibley
"""

import cv2

# this function checks to see if any images that didnt intersect the points
# at least run parallel to the points either vertically or horizontally
iter = 0
def checkParallel(intersectPts, w, h):
    ptX = intersectPts[0][0]
    ptY = intersectPts[0][1]
    ptX2 = intersectPts[1][0]
    ptY2 = intersectPts[1][1]
    ptX3 = intersectPts[2][0]
    ptY3 = intersectPts[2][1]
    ptX4 = intersectPts[3][0]
    ptY4 = intersectPts[3][1]
    horiz1 = ptX2 - ptX
    horiz2 = ptX4 - ptX3
    vert1 = ptY2 - ptY
    vert2 = ptY4 - ptY3
    
    if(w >= horiz1 or w >= horiz2):
        hPar = 1
    else:
        hPar = 0
    if(h >= vert1 or h >= vert2):
        vPar = 1
    else:
        vPar = 0
    
    parallels = [hPar, vPar]
    return parallels
        

# read in jpeg image
# convert it to greyscale 
# add biulateral filter which kind of intensifies the edges of objects in the picture
# use cv's canny edge detection to intensify the edges even more
img = cv2.pyrDown(cv2.imread('/Users/Squibley/Documents/horse1.jpg', cv2.IMREAD_UNCHANGED))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 11, 17, 17)
edged = cv2.Canny(gray, 30, 200)



# threshold image
ret, threshed_img = cv2.threshold(edged, 127, 255, cv2.THRESH_BINARY)
# find contours and get the external one
image, contours, hier = cv2.findContours(threshed_img, cv2.RETR_TREE,
                cv2.CHAIN_APPROX_SIMPLE)

# get one-third of the image's height + width to create the rule of thirds grid 
getSize = img.shape
imgHeight = getSize[0]
imgWidth = getSize[1]
imgThirdH = imgHeight//3
imgThirdW = imgWidth//3

# list of 4 intersection points of interest
intersectPts = []
# Start with upper left intersection point
intersectPts.append([imgThirdW, imgThirdH])
# Upper right
intersectPts.append([imgThirdW*2, imgThirdH])
# Lower left
intersectPts.append([imgThirdW, imgThirdH*2])
# Lower right
intersectPts.append([imgThirdW*2, imgThirdH*2])

iter = 0
for i in intersectPts:
    x = intersectPts[iter][0]
    y = intersectPts[iter][1]
    cv2.circle(img,(x, y), 5, (0, 0, 255), -1)
    iter = iter + 1
    
# Create a threshold for the bounding rectangle. 
# Any "object" smaller than 20% of the photo probably isnt important
minW = int(imgWidth * (.2))
minH = int(imgHeight * (.2))
minArea = minW * minH

rectBounds = []
for c in contours:
    
    # get the bounding rect for any objects in the picture
    x, y, w, h = cv2.boundingRect(c)
    getArea = w * h
 
    if(getArea > minArea or w > minW):
        if(h > minH):
            x2 = x + w
            y2 = y + h
            values = [x, y, x2, y2, w, h]
            cv2.rectangle(img, (x, y), (x2, y2), (0, 255, 0), 2)
            rectBounds.append(values)
            rect = cv2.minAreaRect(c)
            box = cv2.boxPoints(rect)
           

#checks every object to see if it intersects with the four points of interest
iterBounds = 0
boundsIntersect = []
pars = []
for i in rectBounds:
    iterPts = 0
    rX = rectBounds[iterBounds][0]
    rY = rectBounds[iterBounds][1]
    rX2 = rectBounds[iterBounds][2]
    rY2 = rectBounds[iterBounds][3]
    w = rectBounds[iterBounds][4]
    h = rectBounds[iterBounds][5]
    
    result = []
    
    for j in intersectPts:
           ptX = intersectPts[iterPts][0]
           ptY = intersectPts[iterPts][1]
           
           if rX < ptX < rX2 and rY < ptY < rY2:
               result.append(1)
           else:
               result.append(0)
               
           iterPts = iterPts + 1
           if iterPts == 4:               
               r1 = result[0]
               r2 = result[1]
               r3 = result[2]
               r4 = result[3]
               rSet = [r1, r2, r3, r4]
               
               
               # if the object didn't intersect any points
               # we will now check it to see if it at least runs parallel to the points
               if rSet == [0, 0, 0, 0]:
                   pars = checkParallel(intersectPts, w, h)
                   rSet.append(pars[0])
                   rSet.append(pars[1])
    boundsIntersect.append(rSet)
    iterBounds = iterBounds + 1

# holds a list for every object in the image
# the list will contain four or six elements of 0 or 1
# the first four elements correspond to the four points of 
#interest (top left, top right, bottom left, bottom right)
# if the object intersected that point, 1, if not 0
# any object that didnt intersect any points will have a list of six elements instead
# the first four will be 0's since there were no intersections
# elements five and six will account for whether the object runs parallel to the points
# the fifth element accounting for horizontal parallelism and six for vertical     
print(boundsIntersect) 


iter = 0                 
tot = 0
for i in boundsIntersect:
    elems = len(boundsIntersect[iter])
    tot = tot + elems
    iter = iter+1
    
print(tot) 
   
# the comments below just drew the rule of thirds grid 
cv2.line(img,(imgThirdW, 0),(imgThirdW, imgHeight),(255,0,0),2)
cv2.line(img,(imgThirdW*2, 0),(imgThirdW*2, imgHeight),(255,0,0),2)
cv2.line(img,(0, imgThirdH),(imgWidth, imgThirdH),(255,0,0),2)
cv2.line(img,(0, imgThirdH*2),(imgWidth, imgThirdH*2),(255,0,0),2)

#show the image, with objects outlined and points of interests shown 
cv2.imshow("contours", img)
 
ESC = 27
while True:
    keycode = cv2.waitKey()
    if keycode != -1:
        keycode = 0xFF
        if keycode == ESC:
            break
cv2.destroyAllWindows()

