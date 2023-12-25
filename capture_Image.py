import cv2
import os
import time

# 连接到相机
cap = cv2.VideoCapture(0)

# 创建文件夹用于保存图像
folder = 'saved_images'
if not os.path.exists(folder):
    os.makedirs(folder)

frame_count = 0
max_images = 1000  # 最大保存图像数
frames = []
start_time = time.time()  # 开始计时

while frame_count < max_images:
    ret, frame = cap.read()
    if not ret:
        break

    # 将帧添加到列表中
    frames.append(frame)
    frame_count += 1

    # 显示图像
    # cv2.imshow('Frame', frame)

    # 按 'q' 提前退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



end_time = time.time()  # 结束计时
total_time = end_time - start_time  # 总用时
print(f"总用时: {total_time:.2f} 秒")


# 保存所有的帧
for i, frame in enumerate(frames):
    filename = os.path.join(folder, f'image_{i}.png')
    cv2.imwrite(filename, frame)

# 释放资源并关闭窗口
cap.release()
cv2.destroyAllWindows()