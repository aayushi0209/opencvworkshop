import numpy as np
import cv2
# create black image
img=np.zeros((300,300),np.uint8)
# thickness
# line
img=cv2.line(img,(0,0),(100,100),(255,0,0),5)
# circle
img=cv2.circle(img,(150,130),50,(0,0,255),-1)


# img=cv2.putText(img,"Aayushi",(200,50))
cv2.imshow("frame",img)
cv2.waitKey(0)

