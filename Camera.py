import cv2
import uuid   # allows us to give unique identifiers
import os
import numpy as np
import time
from DatabaseManagers import MongoDBClient, DataFrame

labels = ["panda", "milo", "bubby"]
labels_2 = ["person", "dog"]
labels_3 = ["licence plates"]

# todo learn to read camera data
# todo learn to `Label` dataset
# todo learn to train dataset (mobile net)


class Camera:
		
	
	@staticmethod
	def list_images(frame: bool = False) -> None or DataFrame:
		"""
		This method retrives the images stored in mongo db as a dataframe
		then prints out the filenames and upload date. it returns None
		or the dataframe based on the frame bool
		:param frame: boolean set to false if true returns the dataframe
		:return: void or bool
		"""
		df = MongoDBClient.get_dataframe("ObjectDetection", "fs.files")
		print(df[["filename", "uploadDate"]])
		if frame:
			return df
	
	@staticmethod
	def capture_image(name:str ="bubby", interactive:bool = False, local:bool = False) -> None:
		"""
		This method captures and image using cv2 and saves the image 
		as a jpg with the given name arguement
		:param name: string to save the file
		:param local: bool if set to true saves localy on disk if not saves to mongodb
		:return: void
		"""
		cap = cv2.VideoCapture(0)
		
		if interactive:
			while True:
				ret, frame = cap.read()
				cv2.imshow("frame", frame)
				if cv2.waitKey(1) & 0xff == ord('q'):
					break
			Camera.save_image(name, frame, local)
		elif not interactive:
			time.sleep(5)
			ret, frame = cap.read()
			Camera.save_image(name, frame, local)		
				
		time.sleep(2)
		cap.release()
		cv2.destroyAllWindows()
	
	
	@staticmethod
	def save_image(name, frame, local):
		if local:
			Camera.save_localy(name, frame)
			return
		Camera.save_to_mongo(name, frame)
	
	
	
	@staticmethod
	def save_to_mongo(name, frame):
		MongoDBClient.add_fs_file("ObjectDetection", Camera.convert_to_jpg_binary(frame), f"{name}_{uuid.uuid1()}")
		
	
	
	@staticmethod
	def save_localy(name, frame):
		cv2.imwrite(f"{name}.jpg", frame)
	
	
	@staticmethod
	def delete_image(_id:str) -> None:
		MongoDBClient.delete_fs_file("ObjectDetection", _id)
			
			
			
	
	@staticmethod
	def retrieve_image(name:str, write:bool = False) -> str or None:
		"""
		This method is used to retrive the binary data of an image from the mongodb
		:param name: string of the image to retrieve
		:write bool: if set to True writes image to disk if not returns binary data as a string
		:return void or str: if write is False the binary data is returned as a string 
		"""
		binary_image_data = MongoDBClient.retrieve_fs_file("ObjectDetection", name)
		if write:
			with open(f"{name}.jpg", "wb") as f:
				f.write(binary_image_data)
			return
		return binary_image_data
		
		
		
	@staticmethod
	def video_camera(filename="test.avi", test:bool = False) -> None:
		"""
		This method tests the camera by opening the software using the
		cv2 imshow gui feature
		:return: void
		"""
		cap = cv2.VideoCapture(0)
		if not cap.isOpened():
			print("ERROR OPENING CAMERA")
			return
		
		
		size = ( int(cap.get(3)),  int(cap.get(4)) )
		
		result = cv2.VideoWriter(
			filename,
			cv2.VideoWriter_fourcc(*'MJPG'),
			10,
			size
		)
		
		print("press q to quit")
		while True:
			ret, frame = cap.read()
			result.write(frame)
			cv2.imshow("frame", frame)
			if cv2.waitKey(1) & 0xff == ord('q'):
				break
		cap.release()
		result.release()
		cv2.destroyAllWindows()
	 
	@staticmethod 
	def convert_to_jpg_binary(frame: np.ndarray) -> str:
		"""
		This method calls the cv2 imencode method
		to convert the np ndarray into a jpg format represented in a string
		:return : string of jpg data
		"""
		return cv2.imencode(".jpg", frame)[1].tostring()

	 	
	 
	 
