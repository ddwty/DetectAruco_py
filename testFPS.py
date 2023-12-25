import cv2
import time

cap = cv2.VideoCapture(0)

def testFPS():
    # 获取 OpenCV version
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

    # 对于 webcam 不能采用 get(CV_CAP_PROP_FPS) 方法
    # 而是：
    if int(major_ver) < 3:
        fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)
        print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
    else:
        fps = cap.get(cv2.CAP_PROP_FPS)
        print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

    # Number of frames to capture
    num_frames = 120
    print("Capturing {0} frames".format(num_frames))

    # Start time
    start = time.time()
    # Grab a few frames
    for i in range(0, num_frames):
        ret, frame = cap.read()
    # End time
    end = time.time()

    # Time elapsed
    seconds = end - start
    print("Time taken : {0} seconds".format(seconds))

    # 计算FPS，alculate frames per second
    fps = num_frames / seconds;
    print("Estimated frames per second : {0}".format(fps))



while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)

    testFPS()
    print(cap.get(3))

    # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 5000)
    # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 5000)

    size = (int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)), int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
    _, frame = cap.read()
    print(frame.shape)

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


