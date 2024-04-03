import imageio
import numpy as np
import cv2

video1 = imageio.get_reader('static\demo\sr\\lego_coarse.mp4')
video2 = imageio.get_reader('static\demo\sr\\lego_fine.mp4')
img1 = imageio.imread('static\demo\sr\\lego_input.png')


fps = video1.get_meta_data()['fps']
frame_width = video1.get_meta_data()['source_size'][0]
frame_height = video1.get_meta_data()['source_size'][1]
fps = video1.get_meta_data()['fps']

output_file = 'static\demo\sr\\lego_coarse_fine.mp4'
writer = imageio.get_writer(output_file, fps=fps)

for i, (frame1, frame2) in enumerate(zip(video1, video2)):
    frame1 = video1.get_data(i)
    frame2 = video2.get_data(i)
    frame1 = cv2.resize(frame1, (256, 256), interpolation=cv2.INTER_NEAREST)
    new_frame = np.concatenate((img1, frame1, frame2), axis=1) 
    writer.append_data(new_frame)

writer.close()