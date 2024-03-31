import cv2

video_p1 = 'static\mesh_video\drums_coarse.mp4'
video_p2 = 'static\mesh_video\drums_fine.mp4'
video1 = cv2.VideoCapture(video_p1)
video2 = cv2.VideoCapture(video_p2)

width1 = int(video1.get(cv2.CAP_PROP_FRAME_WIDTH))
height1 = int(video1.get(cv2.CAP_PROP_FRAME_HEIGHT))

width2 = int(video2.get(cv2.CAP_PROP_FRAME_WIDTH))
height2 = int(video2.get(cv2.CAP_PROP_FRAME_HEIGHT))

output_width = width1 + width2
output_height = max(height1, height2)

# 创建输出视频的写入器
output = cv2.VideoWriter('static\mesh_video\drums_coarse_fine.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (output_width, output_height))

while True:
    # 读取第一个视频的帧
    ret1, frame1 = video1.read()
    
    # 读取第二个视频的帧
    ret2, frame2 = video2.read()

    # 如果两个视频都读取完毕，则退出循环
    if not ret1 or not ret2:
        break

    # 将两个帧拼接成新的帧
    new_frame = cv2.hconcat([frame1, frame2])

    # 将新帧写入输出视频
    output.write(new_frame)

# 释放资源
video1.release()
video2.release()
output.release()