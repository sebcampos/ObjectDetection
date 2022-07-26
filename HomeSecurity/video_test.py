import cv2

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
if __name__ == "__main__":
    video_camera(test=True)
