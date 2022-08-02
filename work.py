import numpy as np
from PIL import Image
import cv2

cap = cv2.VideoCapture(0)
# Capture frame
ret, frame = cap.read()
if ret:
	cv2.imwrite('/home/img.jpg', frame)

cap.release()
img = Image.open('/home/img.jpg')
img = img.resize((416, 416), Image.ANTIALIAS)
img.save('/home/img1.jpg')

