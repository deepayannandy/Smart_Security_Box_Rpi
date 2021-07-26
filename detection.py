import os
import cv2 
import numpy as np

current_path=os.getcwd() 
print(current_path)

def roi_detect(roi,pos):
	pass


def detection(cam_name,cam_address):
	# Setup capture
	cap = cv2.VideoCapture(cam_address)
	width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
	height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
	# getting the roi
	config_path=current_path+"/config_files/"+cam_name+"ROI.conf"
	file = open(config_path,"r")
	roi=res = tuple(map(int, file.read().split(','))) 
	file.close()
	print(roi,type(roi))
	while True: 
	    ret, frame = cap.read()
	    detection_frame=cv2.resize(frame, (800, 600))
	    x,y,w,h=roi
	    #print(x,y,w,h)
	    cv2.rectangle(detection_frame,(x,y),(x+w,y+h),(0,0,225),1 )


	    cv2.imshow(cam_address, detection_frame)
	    
	    if cv2.waitKey(1) & 0xFF == ord('q'):
	        cap.release()
	        cv2.destroyAllWindows() 
	        break