import cv2

def record_video(filepath, duration):
    # Open the USB camera
    cap = cv2.VideoCapture(0)

    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(filepath, fourcc, 20.0, (640, 480))

    # Record video for the specified duration
    start_time = cv2.getTickCount()
    while (cv2.getTickCount() - start_time) / cv2.getTickFrequency() < duration:
        ret, frame = cap.read()
        if ret:
            # Write the frame to the video file
            out.write(frame)
        else:
            break

    # Release the resources
    cap.release()
    out.release()

# Set the filepath and duration
filepath = '/path/to/save/video.avi'
duration = 10

# Call the function to record the video
record_video(filepath, duration)
