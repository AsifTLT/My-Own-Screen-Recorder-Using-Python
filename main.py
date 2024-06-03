import datetime
from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics

#dynamic default  height width
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

#dynamic file name 
time_stamp = datetime.datetime.now().strftime('%Y-%m-%d')
file_name = f'{time_stamp}.mp4'

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
captured_video = cv2.VideoWriter(file_name, fourcc , 20.0, (width, height))

while True:
    img = ImageGrab.grab(bbox=(0, 0, width, height))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    cv2.imshow("Screen Recorder", img_final)
    captured_video.write(img_final)
    if cv2.waitKey(10) == ord("s"):
        break
    