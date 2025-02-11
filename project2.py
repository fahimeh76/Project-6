import cv2

frameWidth = 640
frameHeight = 480
minArea = 200
plateCascade = cv2.CasadeClassifier("resources/cascade.xml")

cap = cv2.VideoCapture("resources/mygeneratedvideo.avi")

cap.set(3,frameWidth)
cap.set(4,frameHeight)

count = 0
while True:
    success, img = cap.read()
    imgGrey = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)
    numberPlates = plateCascade.detectMultiScale(imgGrey , 1.1, 10)

    for (x,y,w,h) in numberPlates:
        area = w*h
        if area > minArea:
            cv2.rectangle(img, (x,y) , (x+w , y+h), (255,0,255) , 2)
            cv2.putText(img, "Plate Detected" , (x,y-10), cv2.FONT_HERSHY_COMPLEX_SMALL, 1, (255,0,255) , 2)
            imgRoi = img [y:y+h,x:x+w]

    cv2.imshow("Result" , img)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("resources/scanned/{}.jpg".format(count),imgRoi)
        count+=1

