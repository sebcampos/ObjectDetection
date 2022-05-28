import cv2
import uuid   # allows us to give unique identifiers
import os
import numpy as np
import time
from DatabaseManagers import MongoDBClient

labels = ["panda", "milo", "bubby"]



def capture_image(name="bubby"):
	cap = cv2.VideoCapture(0)
	time.sleep(5)
	ret, frame = cap.read()
	MongoDBClient.add_image("ObjectDetection", convert_binary(frame), f"{name}{uuid.uuid1()}")
	# cv2.imwrite(f"{name}.jpg", frame)
	# cv2.imshow("frame", frame)
	time.sleep(2)
	cap.release()
	cv2.destroyAllWindows()
	
 
 
def convert_binary(frame):
	return cv2.imencode(".jpg", frame)[1].tostring()
 	
def convert_image(binary):
	# nparr = np.fromstring(binary, np.uint8)
 	return cv2.imdecode(binary, cv2.CV_LOAD_IMAGE_COLOR)	
