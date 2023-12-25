import cv2
import numpy as np
import time
import os

cap = cv2.VideoCapture(0)
print(cv2.__version__)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("width: ", width)
print("height: ", height)
num_frames = 120
index = 0
begin = time.time()
j = 0
while cap.isOpened():
    ret, img = cap.read()
    index += 1

    # 测试不显示图像的情况
    # start = time.time()
    # for i in range(0, num_frames):
    #     ret, img = cap.read()
    # end = time.time()
    # # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # second = end - start
    # fps = num_frames / second
    # print("fps: ", fps)
    img = cv2.resize(img, (1920, 1080))
    # cv2.imshow('frame', img)
    # if cv2.waitKey(1) == 27:
    #     break

    # 测试显示图像的情况
    if index % 120 == 0 and index != 0:
        j += 1
        endTime = time.time()
        print('index: ', index)
        seconds = endTime - begin
        print('seconds: ', seconds)
        print('fps2', 120 * j / seconds)

cap.release()
cv2.destroyAllWindows()
