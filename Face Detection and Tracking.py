import cv2

alg="haarcascade_frontalface_default.xml"
haar_cascade=cv2.CascadeClassifier(alg)

cam=cv2.VideoCapture(0) #initializing cam

while True:
    _,img=cam.read() #read the frame
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face=haar_cascade.detectMultiScale(gray_img,1.3,4) #get coordinates

    for(x,y,w,h) in face: #segregation
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("FaceDetection",img)
    key=cv2.waitKey(10)
    if key==27:
        break
cam.release()
cv2.destroyAllWindows()