# face Detection
import numpy
import cv2
import math

image=cv2.imread('p.jpg')
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


facecasecade=cv2.CascadeClassifier('face.xml')
faces=facecasecade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=5,minSize=(10,10))
print(faces)

l=[]
i=1
lf=[]
for(x,y,w,h)in faces:
	cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),4)
	s=str(i)
	font=cv2.FONT_HERSHEY_SIMPLEX
	# fontscale
	fontScale=1
	cv2.putText(image,s,(x,y),font,fontScale,(0,255,0),2)
	i=i+1
	l=[]
	l.append(x)
	l.append(y)
	lf.append(l)
	print(l)
print(lf)
close_person=""
for i in range (len(lf)):
	print(lf[i])
	for j in range(i+1,len(lf)):
		print(lf[j])
		d=math.sqrt(((lf[j][1]-lf[i][1])**2)+((lf[j][0]-lf[i][0])**2))
		print(d)
		if d<300:
			close_person=close_person+"Person"+str(i+1)+"and Person"+str(j+1)+"\n"
	close_person+="are not following social distancing"
print(close_person)
cv2.imshow("aayushi",image)
cv2.waitKey(0)