import cv2
import uuid   # allows us to give unique identifiers
import os
import numpy as np
import time
import atexit
from DatabaseManagers import MongoDBClient

labels = ["panda", "milo", "bubby"]


class Camera:
	
	cap = cv2.VideoCapture(0)
	
	
	@classmethod
	def tear_down(cls):
		cls.cap.release()
		cv2.destroyAllWindows()
	
	@staticmethod
	def capture_image(name:str ="bubby", cap=cap) -> None:
		"""
		
		"""
		time.sleep(5)
		ret, frame = cap.read()
		MongoDBClient.add_image("ObjectDetection", Camera.convert_binary(frame), f"{name}_{uuid.uuid1()}")
		# cv2.imwrite(f"{name}.jpg", frame)
		# cv2.imshow("frame", frame)
		time.sleep(2)
		
		
	@staticmethod
	def camera_test(cap=cap) -> None:
		print("press q to quit")
		while True:
			ret, frame = cap.read()
			cv2.imshow("frame", frame)
			if cv2.waitKey(1) & 0xff == ord('q'):
				break
	 
	@staticmethod 
	def convert_binary(frame: np.ndarray) -> str:
		return cv2.imencode(".jpg", frame)[1].tostring()
	
	@staticmethod 	
	def convert_image(binary):
		nparr = np.fromstring(binary, np.uint8)
	 	return cv2.imdecode(binary, cv2.CV_LOAD_IMAGE_COLOR)	
	 	
	 	
atexit.register(Camera.tear_down)
	 
