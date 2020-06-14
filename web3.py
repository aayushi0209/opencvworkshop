import numpy as np
import cv2
# create black image
img=np.zeros((300,300),np.uint8)
font=cv2.FONT_HERSHEY_SIMPLEX
# fontscale
fontScale=1
img=cv2.putText(img,"Aayushi",(100,50),font,fontScale,(255,0,0),5)
cv2.imshow("frame",img)
cv2.waitKey(0)

