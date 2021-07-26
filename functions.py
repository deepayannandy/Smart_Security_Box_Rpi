import os
import roi
import detection
import threading
import requests

config_path=os.path.join(os.getcwd(),"config_files")

def deleate_conf():
	files=os.listdir(config_path)
	for file in files:
		os.remove(os.path.join(config_path ,file))
	print("Reset")
def generate_conf(cam_num,cam_address):
	filename="cam"+cam_num+".conf"
	f = open(os.path.join(config_path ,filename), "w")
	f.write(cam_num)
	f.write("\n"+cam_address)
	f.close()
	print("Conf saved")
def get_configs():
	files=os.listdir(config_path)
	return files
def run_roi_selector(cam_name):
	file_name=cam_name+'.conf'
	f = open(os.path.join(config_path ,file_name), "r")
	cam_num=f.readline().replace('\n','')
	cam_address=f.readline()
	print(cam_num,cam_address)
	roi.show(cam_num,cam_address)
def run_roi_preview(cam_name):
	file_name=cam_name+'.conf'
	f = open(os.path.join(config_path ,file_name), "r")
	cam_num=f.readline().replace('\n','')
	cam_address=f.readline()
	roi.previewROI(cam_name,cam_address)
def star_detection():
	for i in get_configs():
    		if 'ROI' in i:
    			pass
    		else:
    			file_name=i
    			f = open(os.path.join(config_path ,file_name), "r")
    			cam_num=f.readline().replace('\n','')
    			cam_address=f.readline()
    			cam_name=i.replace('.conf','')
    			t1 = threading.Thread(target=detection.detection, args=(cam_name,cam_address))
    			t1.start()
def save_contact(r1,r2,r3):
	filename="contacts.conf"
	f = open(os.path.join(config_path ,filename), "w")
	f.write(r1)
	f.write("\n"+r2)
	f.write("\n"+r3)
	f.close()
	print("Conf saved")
def send_alart():
	message="Hey there is some problem detected!"
	filename="contacts.conf"
	f = open(os.path.join(config_path ,filename), "r")
	contacts=f.readlines()
	f.close()
	for contact in contacts:
		contact.replace('\n','')
		if len(contact)>0:
			try:
				path=f"https://api.telegram.org/bot1068445966:AAGUxOgEp5Kd-87gfiUs9cIFrr5gqbAL2tQ/sendMessage?chat_id={contact}&text={message}"
				response = requests.get(path)
				print("sent")
			except:
				print("Something Went Wrong")