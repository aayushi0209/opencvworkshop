# face Detection
import numpy
import cv2

# webcam=cv2.VideoCapture(0)
# ret ,frame=webcam.read()
# print(ret)
# webcam.release()

# cv2.imshow("my image",frame)
# cv2.waitKey()
# cv2.destroyallWindows()

webcam=cv2.VideoCapture(0)
while(True):
	# capture frame by frame
	ret,frame=webcam.read()
	# operations on framecam
	# gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	# cv2.imshow("aayushi",gray)
	cv2.imshow("aayushi",frame)
	if cv2.waitKey(1)& 0xFF == ord('q'):
		break;
	elif cv2.waitKey(1)& 0xFF ==ord('a'):
		cv2.imwrite("myimage.jpg",frame)

# when everything done release the capture
webcam.release()
cv2.destroyallWindows()

# facecasecade=cv2.CascadeClassifier('face.xml')

# webcam=cv2.