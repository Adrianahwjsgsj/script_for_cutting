import numpy as np
from PIL import Image
from picamera import PiCamera
import subprocess

camera = PiCamera()
camera.resolution = (1920, 1080)
time.sleep(2)
camera.capture("/home/img.jpg")

img = Image.open('/home/img.jpg')
img = img.resize((416, 416), Image.ANTIALIAS)
img.save('/home/img.jpg')

subprocess.call("/home/yolov5/detect.py", shell=False)
