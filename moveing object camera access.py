import cv2
import  imutils
cam=cv2.VideoCapture(0)

firstFrame=None
area=500

while True:
    a,img=cam.read()
    text="normal"
    img=imutils.resize(img,width=1000)
    grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gaussianimg=cv2.GaussianBlur(grayimg,(21,21),0)
    if firstFrame is None:
        firstFrame=gaussianimg
        continue
    imgdiff=cv2.absdiff(firstFrame,gaussianimg)
    threahimg=cv2.threshold(imgdiff,25,255,cv2.THRESH_BINARY)[1]
    threahimg=cv2.dilate(threahimg,None,iterations=2)
    cnts=cv2.findContours(threahimg.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts=imutils.grab_contours(cnts)
    for c in cnts:
        if cv2.contourArea(c) < area:
            continue
        (x,y,w,h)=cv2.boundingRect(c)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        text="moving object detected"
    print(text)
    cv2.putText(img,text,(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
    cv2.imshow("CAMERAFEED",img)

    key=cv2.waitKey(1)
    print(key)
    if key == ord("q"):
        break
    
cam.release()
cv2.destroyAllWindows
