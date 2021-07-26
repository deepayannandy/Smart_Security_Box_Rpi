import cv2 
import numpy as np
import os

current_path=os.getcwd() 
'''
print(current_path)
name="cam1"
# define a video capture object 
cap = cv2.VideoCapture("human.mp4") 
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))'''

def save_config(cam_name, locations):
    if locations==(0,0,0,0):
        pass
    else:
        data=""
        item=0
        for i in locations:
            data=data+str(i)
            if item==3:
                pass
            else:
                data=data+","
            item+=1
        print(data)
        file = open(os.path.join(current_path,"config_files",cam_name),"w+")
        file.write(data)
        file.close()
        print("New Configaration Saved at:"+os.path.join(current_path,"config_files",cam_name))

def show(cam_num,cam_address):
    print(cam_address)
    try:
        cap = cv2.VideoCapture(cam_address)
        while(True): 
            ret, frame = cap.read() 
            frame=cv2.resize(frame, (800, 600))
            org=frame.copy()
            cv2.putText(frame,"""'s' to Select, 'enter' to save, 'c' to cancle """, (10,30),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3)
            cv2.imshow(cam_address,frame)
              
            if cv2.waitKey(1) & 0xFF == ord('q'): 
                break
            if  cv2.waitKey(1) & 0xFF == ord('s'):
                roi=cv2.selectROI(org)
                print(roi)
                name='cam'+cam_num+'ROI.conf'
                save_config(name,roi)
                cv2.destroyWindow("ROI selector")

        cap.release() 
        # Destroy all the windows 
        cv2.destroyAllWindows() 
    except:
        print("Camera is offline")
        cap.release() 
        # Destroy all the windows 
        cv2.destroyAllWindows() 
def previewROI(cam_name,cam_address):
    print(cam_address)
    try:
        # getting the roi
        config_path=current_path+"/config_files/"+cam_name+"ROI.conf"
        file = open(config_path,"r")
        roi=res = tuple(map(int, file.read().split(','))) 
        file.close()
        print(roi,type(roi))
        cap = cv2.VideoCapture(cam_address)
        while(True): 
            ret, frame = cap.read() 
            frame=cv2.resize(frame, (800, 600))
            x,y,w,h=roi
            #print(x,y,w,h)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,225),1 )
            cv2.imshow(cam_address,frame)
            if cv2.waitKey(1) & 0xFF == ord('q'): 
                break
        cap.release() 
        # Destroy all the windows 
        cv2.destroyAllWindows() 
    except:
        print("Camera is offline")
        # Destroy all the windows 
        cv2.destroyAllWindows() 