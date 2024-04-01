import imageio
import numpy as np

video1 = imageio.get_reader('static\mesh_video\\ficus_coarse.mkv')
video2 = imageio.get_reader('static\mesh_video\\ficus_fine.mkv')


fps = video1.get_meta_data()['fps']
frame_width = video1.get_meta_data()['source_size'][0]
frame_height = video1.get_meta_data()['source_size'][1]
fps = video1.get_meta_data()['fps']

output_file = 'static\mesh_video\\ficus_coarse_fine.mp4'
writer = imageio.get_writer(output_file, fps=fps)

for i, (frame1, frame2) in enumerate(zip(video1, video2)):
    frame1 = video1.get_data(i)
    frame2 = video2.get_data(i)
    new_frame = np.concatenate((frame1, frame2), axis=1) 
    writer.append_data(new_frame)

writer.close()