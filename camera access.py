import cv2

vs=cv2.VideoCapture(0)# camera 0= maincamera
# 1 is second camera

while True:
    a,img=vs.read()
    print(a)
    cv2.imshow("videostram",img)

    key=cv2.waitKey(1)
    print(key)
    if key==ord("q"):
        break
vs.release()
cv2.destroyAllWindows

    







    
               
