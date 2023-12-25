import cv2.aruco as aruco
import cv2
import numpy as np
import time
import os
import sys
import socket
import pickle

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(('127.0.0.1', 12345))

# 获取可执行文件所在的目录
if getattr(sys, 'frozen', False):
    exe_dir = os.path.dirname(sys.executable)
else:
    exe_dir = os.path.dirname(os.path.abspath(__file__))

camera_params_path = os.path.join(exe_dir, 'camera_params.npz')

intrinsic_camera = np.array([[971.2252, 0, 655.3664], [0, 970.7470, 367.5246], [0, 0, 1]])

if os.path.exists(camera_params_path):
    calibration_file = np.load(camera_params_path)
else: 
    print('No camera params file， using default camera params.')
    cx = 655.3664
    cy = 367.5246
    fx = 971.2252
    fy = 970.7470
    k1 = 0.0097
    k2 = -0.00745
    k3 = 0.00
    p1 = 0.00
    p2 = 0.00
    intrinsic_camera = np.array([[fx, 0, cx], [0, fy, cy], [0, 0, 1]])
    distortion = np.array([k1, k2, p1, p2, k3])


# calibration_file = np.load('camera_params.npz')
intrinsic_camera = calibration_file['mtx']
distortion = calibration_file['dist']
# Define aruco dictionary
arucoDict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
arucoParams = aruco.DetectorParameters()
arucoParams.cornerRefinementMethod = cv2.aruco.CORNER_REFINE_CONTOUR

# Camera calibration parameters
# intrinsic_camera = np.array([[fx, 0, cx], [0, fy, cy], [0, 0, 1]])
# distortion = np.array([k1, k2, p1, p2, k3])

# detect aruco marker from camera
cap = cv2.VideoCapture(0)
fps = cap.get(cv2.CAP_PROP_FPS)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
print("width: ", width)
print("height: ", height)


# loop_count = 0
# start_time = time.time()

while cap.isOpened():
    ret, img = cap.read()
    if not ret: break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((5, 5), np.float32) / 25
    gray = cv2.filter2D(gray, -1, kernel)

    corners, ids, rejected = cv2.aruco.detectMarkers(gray, arucoDict, parameters=arucoParams)
    if ids is not None:
        # print("ids: ", ids)
        for index in range(0, len(ids)):
            # print(f"ID length: {len(ids)}")
            rvec, tvec, _ = cv2.aruco.estimatePoseSingleMarkers(corners[index], 20, intrinsic_camera,
                                                                    distortion)
            cv2.aruco.drawDetectedMarkers(img, corners, ids)
            cv2.drawFrameAxes(img, intrinsic_camera, distortion, rvec, tvec, 10)
            rmat = cv2.Rodrigues(rvec)[0]
            homogenous_trans_mtx = np.append(rmat, [[tvec[0][0][0]], [tvec[0][0][1]], [tvec[0][0][2]]], axis=1)
            homogenous_trans_mtx = np.append(homogenous_trans_mtx, [[0, 0, 0, 1]], axis=0)

            homo_data = {'id': ids[index][0], 'pose': homogenous_trans_mtx}
            print('id: ', ids[index])
            print("homogenous_trans_mtx\n", np.array2string(homogenous_trans_mtx, precision=3, suppress_small=True))
            serialized_data = pickle.dumps(homo_data)
            # try:
            #     # 发送数据
            #     s.sendall(serialized_data)
            # except socket.error as e:
            #     print(f"Cannot send data, the server might be down.: {e}")
            

    cv2.imshow('frame', img)
    # 按下ESC键退出
    if cv2.waitKey(1) == 27:
        break

    # loop_count += 1
    # if time.time() - start_time >= 1: 
    #     print(f"loop_count: {loop_count}")
    #     loop_count = 0
    #     start_time = time.time()

cap.release()
cv2.destroyAllWindows()
