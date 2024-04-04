import imageio
import numpy as np
import cv2

video1 = imageio.get_reader('static\demo\\mixed_degradation\\hotdog_coarse.mp4')
video2 = imageio.get_reader('static\demo\\mixed_degradation\\hotdog_fine.mp4')


fps = video1.get_meta_data()['fps']
frame_width = video1.get_meta_data()['source_size'][0]
frame_height = video1.get_meta_data()['source_size'][1]
fps = video1.get_meta_data()['fps']

output_file = 'static\demo\\mixed_degradation\\hotdog_coarse_fine.mp4'
writer = imageio.get_writer(output_file, fps=fps)

for i, (frame1, frame2) in enumerate(zip(video1, video2)):
    frame1 = video1.get_data(i)
    frame2 = video2.get_data(i)
    frame1 = cv2.resize(frame1, (frame2.shape[1], frame2.shape[0]), interpolation=cv2.INTER_NEAREST)
    new_frame = np.concatenate((frame1, frame2), axis=1) 
    writer.append_data(new_frame)

writer.close()