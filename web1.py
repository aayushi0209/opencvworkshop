# face Detection on web cam
import numpy
import cv2
facecasecade=cv2.CascadeClassifier('face.xml')
webcam=cv2.VideoCapture(0)
while(True):
	# capture frame by frame
	ret,frame=webcam.read()
	# operations on framecam
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	faces=facecasecade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=5)
	for (x,y,w,h) in faces:
		font=cv2.FONT_HERSHEY_SIMPLEX
		# fontscale
		fontScale=1
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),10)
		cv2.putText(frame,"Aayushi",(x-20,y-20),font,fontScale,(255,0,0),5)
	cv2.imshow("aayushi",frame)
	if cv2.waitKey(1)& 0xFF == ord('q'):
		break;
webcam.release()
cv2.destroyAllWindows
