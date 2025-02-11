import cv2
import numpy as np

frameWidth = 640
frameHeight = 480


cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)

myColor = [(0,135,0),(10,255,255)]
myColorValue = [51,150,255]
myPoints = []

def findColor(img, myColor):
    imgHSV = cv2.CvtColor(img , cv2.COLOR_BGR2HSV)
    lower = np.array(myColor[0])
    upper = np.array(myColor[1])
    mask = cv2.inRange(imgHSV, lower, upper)

    x,y = getContours(mask)
    if x!= 0 & y!=0:
        cv2.circle(imgResult,(x,y) , 15,myColorValue, cv2.FILLED)
        return [x,y]

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            x,y,w,h = cv2.boundingRect(approx)
    return x+(w//2),y

def drawMyPoints(points):
    for point in points:
        cv2.circle(imgResult, (point[0], point[1], 15, myColorValue, cv2.FILLED))    

while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoint = findColor(img, myColor)
    if newPoint!= None:
        myPoints.append(newPoint)
    
    if len(myPoints):
        drawMyPoints(myPoints)
    cv2.imshow("Frame", img)
    cv2.imshow("Result", imgResult)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



