# full body detection
import numpy
import cv2
import math

body_classifier=cv2.CascadeClassifier('haarcascade_fullbody.xml')
frame=cv2.imread('p1.jpg')
gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
bodies=body_classifier.detectMultiScale(gray,1.2,5)
print(bodies)
for(x,y,w,h)in bodies:
	cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

cv2.imshow("gray",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()